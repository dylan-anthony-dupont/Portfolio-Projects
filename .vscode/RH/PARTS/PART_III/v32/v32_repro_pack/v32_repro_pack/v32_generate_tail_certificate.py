#!/usr/bin/env python3
"""Generate an interval-certified check of the v32 tail inequality over a band.

This script is designed to be *audit-friendly* rather than fast.
It uses Python's decimal module with directed rounding to compute conservative
interval enclosures for all quantities.

Inequality checked (worst-case over m in [m_lo,m_hi], alpha in [alpha_lo,alpha_hi]):

  2*C_up*( delta^(3/2)*L(m) + delta^(1/2)*(N_up(m)/kappa) )
      <  c - delta*( K_alloc*c0*L(m) + C_hpp*(log m + 1) ).

Where:
  L(m)    = C1*log m + C2,
  N_up(m) = A_N*log m + B_N,
  delta   = eta*alpha/(log m)^2,
  c0      = 3*log(2)/(8*pi),
  c       = 3*log(2)/16,
  K_alloc = 1/4.

Outputs a JSON certificate file containing the computed enclosures.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
from dataclasses import dataclass
from decimal import Decimal, localcontext, getcontext, ROUND_FLOOR, ROUND_CEILING
from pathlib import Path

# Global precision: plenty for our coarse inequality checks.
getcontext().prec = 80


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def d(s: str) -> Decimal:
    return Decimal(s)


def down(expr) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = getcontext().prec
        ctx.rounding = ROUND_FLOOR
        return +expr


def up(expr) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = getcontext().prec
        ctx.rounding = ROUND_CEILING
        return +expr


@dataclass(frozen=True)
class Interval:
    lo: Decimal
    hi: Decimal

    def __post_init__(self):
        if self.lo > self.hi:
            raise ValueError(f"Invalid interval: lo>{self.hi}")

    @staticmethod
    def from_str(lo: str, hi: str) -> "Interval":
        return Interval(d(lo), d(hi))

    @staticmethod
    def const(x: str) -> "Interval":
        X = d(x)
        return Interval(X, X)

    def add(self, other: "Interval") -> "Interval":
        return Interval(down(self.lo + other.lo), up(self.hi + other.hi))

    def sub(self, other: "Interval") -> "Interval":
        return Interval(down(self.lo - other.hi), up(self.hi - other.lo))

    def mul(self, other: "Interval") -> "Interval":
        # All quantities in this certificate are nonnegative, so this is safe.
        if self.lo < 0 or other.lo < 0:
            # Fallback to full 4-corner evaluation.
            candidates_lo = []
            candidates_hi = []
            for a in (self.lo, self.hi):
                for b in (other.lo, other.hi):
                    candidates_lo.append(down(a * b))
                    candidates_hi.append(up(a * b))
            return Interval(min(candidates_lo), max(candidates_hi))
        return Interval(down(self.lo * other.lo), up(self.hi * other.hi))

    def div(self, other: "Interval") -> "Interval":
        if other.lo <= 0:
            raise ValueError("Division by interval that meets 0 is not supported")
        if self.lo < 0:
            # Use 4-corner evaluation if needed.
            candidates_lo = []
            candidates_hi = []
            for a in (self.lo, self.hi):
                for b in (other.lo, other.hi):
                    candidates_lo.append(down(a / b))
                    candidates_hi.append(up(a / b))
            return Interval(min(candidates_lo), max(candidates_hi))
        return Interval(down(self.lo / other.hi), up(self.hi / other.lo))

    def sqrt(self) -> "Interval":
        if self.lo < 0:
            raise ValueError("sqrt of interval with negative part")
        return Interval(down(self.lo.sqrt()), up(self.hi.sqrt()))

    def ln(self) -> "Interval":
        if self.lo <= 0:
            raise ValueError("ln of interval that meets 0")
        return Interval(down(self.lo.ln()), up(self.hi.ln()))


def load_constants(path: Path) -> dict:
    return json.loads(path.read_text())


def compute_certificate(constants: dict) -> dict:
    # Bands
    m_lo = Interval.const(constants["m_band"]["lo"])
    m_hi = Interval.const(constants["m_band"]["hi"])
    # Create an interval for m, but keep endpoints for monotone functions.
    m_I = Interval(d(constants["m_band"]["lo"]), d(constants["m_band"]["hi"]))

    alpha_I = Interval(d(constants["alpha_band"]["lo"]), d(constants["alpha_band"]["hi"]))
    eta_I = Interval.const(constants["eta"])

    iv = constants["intervals"]
    C1 = Interval.from_str(iv["C1"]["lo"], iv["C1"]["hi"])
    C2 = Interval.from_str(iv["C2"]["lo"], iv["C2"]["hi"])
    C_up = Interval.from_str(iv["C_up"]["lo"], iv["C_up"]["hi"])
    C_hpp = Interval.from_str(iv["C_hpp"]["lo"], iv["C_hpp"]["hi"])
    A_N = Interval.from_str(iv["A_N"]["lo"], iv["A_N"]["hi"])
    B_N = Interval.from_str(iv["B_N"]["lo"], iv["B_N"]["hi"])
    kappa = Interval.from_str(iv["kappa"]["lo"], iv["kappa"]["hi"])

    # log m interval (natural log)
    x_I = m_I.ln()  # x in [ln(m_lo), ln(m_hi)]

    # delta = eta*alpha / x^2
    x2_I = x_I.mul(x_I)
    delta_I = eta_I.mul(alpha_I).div(x2_I)

    sqrt_delta_I = delta_I.sqrt()
    delta_3_2_I = delta_I.mul(sqrt_delta_I)

    # L(m) and N_up(m)
    L_I = C1.mul(x_I).add(C2)
    N_I = A_N.mul(x_I).add(B_N)

    # Conservative upper bounds for the LHS terms
    term1_hi = up(delta_3_2_I.hi * L_I.hi)
    term2_hi = up(sqrt_delta_I.hi * N_I.hi / kappa.lo)

    lhs_hi = up(Decimal(2) * C_up.hi * (term1_hi + term2_hi))

    # Constants c and c0 as *intervals*.
    # ln(2) from Decimal is correctly rounded in the chosen direction.
    ln2_I = Interval(down(Decimal(2).ln()), up(Decimal(2).ln()))

    # A very small enclosure of pi (hard-coded, but wide enough to certainly contain pi).
    # pi = 3.141592653589793238462643383279502884...
    pi_I = Interval(d("3.1415926535897932384626433832795028"), d("3.1415926535897932384626433832795029"))

    three = Interval.const("3")
    eight = Interval.const("8")
    sixteen = Interval.const("16")

    c_I = three.mul(ln2_I).div(sixteen)
    c0_I = three.mul(ln2_I).div(eight.mul(pi_I))

    # K_alloc = 1/4
    K_alloc = Interval.const("0.25")

    # Conservative lower bound for RHS: use c.lo and maximal subtractive term
    one = Decimal(1)
    x_plus_1_hi = up(x_I.hi + one)
    subtract_hi = up(delta_I.hi * (K_alloc.hi * c0_I.hi * L_I.hi + C_hpp.hi * x_plus_1_hi))

    rhs_lo = down(c_I.lo - subtract_hi)

    passed = lhs_hi < rhs_lo

    return {
        "computed_utc": dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
        "bands": {
            "m": {"lo": str(m_I.lo), "hi": str(m_I.hi)},
            "alpha": {"lo": str(alpha_I.lo), "hi": str(alpha_I.hi)},
            "eta": str(eta_I.lo),
        },
        "derived": {
            "log_m": {"lo": str(x_I.lo), "hi": str(x_I.hi)},
            "delta": {"lo": str(delta_I.lo), "hi": str(delta_I.hi)},
            "sqrt_delta": {"lo": str(sqrt_delta_I.lo), "hi": str(sqrt_delta_I.hi)},
            "delta_3_2": {"lo": str(delta_3_2_I.lo), "hi": str(delta_3_2_I.hi)},
            "L": {"lo": str(L_I.lo), "hi": str(L_I.hi)},
            "N_up": {"lo": str(N_I.lo), "hi": str(N_I.hi)},
            "ln2": {"lo": str(ln2_I.lo), "hi": str(ln2_I.hi)},
            "pi": {"lo": str(pi_I.lo), "hi": str(pi_I.hi)},
            "c": {"lo": str(c_I.lo), "hi": str(c_I.hi)},
            "c0": {"lo": str(c0_I.lo), "hi": str(c0_I.hi)},
            "K_alloc": str(K_alloc.lo),
        },
        "inequality": {
            "lhs_hi": str(lhs_hi),
            "rhs_lo": str(rhs_lo),
            "pass": passed,
            "notes": "PASS means lhs_hi < rhs_lo (strict).",
        },
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--constants", required=True, help="Path to v32 constants JSON")
    ap.add_argument("--out", required=True, help="Path to write the certificate JSON")
    args = ap.parse_args()

    const_path = Path(args.constants)
    out_path = Path(args.out)

    constants = load_constants(const_path)
    cert = compute_certificate(constants)

    cert["inputs"] = {
        "constants_path": str(const_path),
        "constants_sha256": sha256_file(const_path),
    }

    out_path.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")

    print("v32 tail certificate")
    print(f"  constants: {const_path}")
    print(f"  out:       {out_path}")
    print(f"  PASS:      {cert['inequality']['pass']}")
    print(f"  lhs_hi:    {cert['inequality']['lhs_hi']}")
    print(f"  rhs_lo:    {cert['inequality']['rhs_lo']}")

    return 0 if cert["inequality"]["pass"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
