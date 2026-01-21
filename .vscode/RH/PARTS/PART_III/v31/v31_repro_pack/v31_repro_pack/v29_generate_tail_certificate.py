#!/usr/bin/env python3
"""
generate_tail_certificate.py  (v29)

Deterministically generates tail_certificate.json from constants.json using
directed-rounding interval arithmetic implemented with Python's decimal module.

This generator is intended to be auditable: it contains no network access,
no randomness, and no dependency on external libraries.

Usage:
  python3 generate_tail_certificate.py constants.json tail_certificate.json
"""

import json
import sys
from dataclasses import dataclass
from decimal import Decimal, getcontext, localcontext, ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_EVEN

# ---- Fixed enclosure for pi (50 decimal places) ----
# Verified digits: pi = 3.14159265358979323846264338327950288419716939937510...
# Hence:
PI_LO = Decimal("3.14159265358979323846264338327950288419716939937510")
PI_HI = Decimal("3.14159265358979323846264338327950288419716939937511")

@dataclass
class Interval:
    lo: Decimal
    hi: Decimal
    def __post_init__(self):
        if self.lo > self.hi:
            raise ValueError(f"Bad interval: {self.lo} > {self.hi}")

def ctx(prec: int, rounding):
    c = getcontext().copy()
    c.prec = prec
    c.rounding = rounding
    return c

def iv(lo: str, hi: str = None) -> Interval:
    if hi is None:
        hi = lo
    return Interval(Decimal(lo), Decimal(hi))

def add(a: Interval, b: Interval, prec: int) -> Interval:
    with localcontext(ctx(prec, ROUND_FLOOR)):
        lo = a.lo + b.lo
    with localcontext(ctx(prec, ROUND_CEILING)):
        hi = a.hi + b.hi
    return Interval(lo, hi)

def sub(a: Interval, b: Interval, prec: int) -> Interval:
    with localcontext(ctx(prec, ROUND_FLOOR)):
        lo = a.lo - b.hi
    with localcontext(ctx(prec, ROUND_CEILING)):
        hi = a.hi - b.lo
    return Interval(lo, hi)

def mul(a: Interval, b: Interval, prec: int) -> Interval:
    with localcontext(ctx(prec, ROUND_FLOOR)):
        cands_lo = [a.lo*b.lo, a.lo*b.hi, a.hi*b.lo, a.hi*b.hi]
        lo = min(cands_lo)
    with localcontext(ctx(prec, ROUND_CEILING)):
        cands_hi = [a.lo*b.lo, a.lo*b.hi, a.hi*b.lo, a.hi*b.hi]
        hi = max(cands_hi)
    return Interval(lo, hi)

def div(a: Interval, b: Interval, prec: int) -> Interval:
    if b.lo <= 0 <= b.hi:
        raise ZeroDivisionError("Interval division by an interval containing 0.")
    with localcontext(ctx(prec, ROUND_FLOOR)):
        rlo = Decimal(1) / b.hi
    with localcontext(ctx(prec, ROUND_CEILING)):
        rhi = Decimal(1) / b.lo
    return mul(a, Interval(rlo, rhi), prec)

def sqrt(a: Interval, prec: int) -> Interval:
    if a.lo < 0:
        raise ValueError("sqrt of negative interval")
    with localcontext(ctx(prec, ROUND_FLOOR)):
        lo = a.lo.sqrt()
    with localcontext(ctx(prec, ROUND_CEILING)):
        hi = a.hi.sqrt()
    return Interval(lo, hi)

def ln(a: Interval, prec: int) -> Interval:
    if a.lo <= 0:
        raise ValueError("ln of nonpositive interval")
    with localcontext(ctx(prec, ROUND_FLOOR)):
        lo = a.lo.ln()
    with localcontext(ctx(prec, ROUND_CEILING)):
        hi = a.hi.ln()
    return Interval(lo, hi)

def pow_3_2(a: Interval, prec: int) -> Interval:
    return mul(a, sqrt(a, prec), prec)

def compute(constants, prec: int = 90):
    m = iv(constants["m_band"])
    eta = iv(constants["eta"])
    alpha = iv(constants["alpha_worst"])

    C1 = iv(constants["intervals"]["C1"]["lo"], constants["intervals"]["C1"]["hi"])
    C2 = iv(constants["intervals"]["C2"]["lo"], constants["intervals"]["C2"]["hi"])
    Cup = iv(constants["intervals"]["C_up"]["lo"], constants["intervals"]["C_up"]["hi"])
    Chpp = iv(constants["intervals"]["C_hpp"]["lo"], constants["intervals"]["C_hpp"]["hi"])

    logm = ln(m, prec)
    delta = div(mul(eta, alpha, prec), mul(logm, logm, prec), prec)

    L = add(mul(C1, logm, prec), C2, prec)

    # ln 2
    ln2 = ln(iv("2"), prec)

    # c = (3 ln 2)/16
    c = div(mul(iv("3"), ln2, prec), iv("16"), prec)

    # c0 = (3 ln 2)/(8 pi), pi enclosed
    pi = Interval(PI_LO, PI_HI)
    c0 = div(mul(iv("3"), ln2, prec), mul(iv("8"), pi, prec), prec)

    # Kalloc = 3 + 8 sqrt(3)
    sqrt3 = sqrt(iv("3"), prec)
    Kalloc = add(iv("3"), mul(iv("8"), sqrt3, prec), prec)

    logm_plus1 = add(logm, iv("1"), prec)

    # LHS = 2*Cup*delta^(3/2)*L
    lhs = mul(mul(mul(iv("2"), Cup, prec), pow_3_2(delta, prec), prec), L, prec)

    # RHS = c - delta*(Kalloc*c0*L + Chpp*(logm+1))
    term1 = mul(mul(Kalloc, c0, prec), L, prec)
    term2 = mul(Chpp, logm_plus1, prec)
    rhs = sub(c, mul(delta, add(term1, term2, prec), prec), prec)

    passed = (lhs.hi < rhs.lo)

    return {
        "prec": prec,
        "pi_interval": {"lo": str(PI_LO), "hi": str(PI_HI)},
        "logm_interval": {"lo": str(logm.lo), "hi": str(logm.hi)},
        "delta_interval": {"lo": str(delta.lo), "hi": str(delta.hi)},
        "L_interval": {"lo": str(L.lo), "hi": str(L.hi)},
        "lhs_interval": {"lo": str(lhs.lo), "hi": str(lhs.hi)},
        "rhs_interval": {"lo": str(rhs.lo), "hi": str(rhs.hi)},
        "derived_constants": {
            "ln2_interval": {"lo": str(ln2.lo), "hi": str(ln2.hi)},
            "c_interval": {"lo": str(c.lo), "hi": str(c.hi)},
            "c0_interval": {"lo": str(c0.lo), "hi": str(c0.hi)},
            "Kalloc_interval": {"lo": str(Kalloc.lo), "hi": str(Kalloc.hi)},
        },
        "pass": bool(passed),
    }

def main():
    if len(sys.argv) != 3:
        print("Usage: generate_tail_certificate.py constants.json tail_certificate.json", file=sys.stderr)
        sys.exit(2)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        constants = json.load(f)

    out = {
        "certificate_version": "v29",
        "m_band": constants["m_band"],
        "eta": constants["eta"],
        "alpha": constants["alpha_worst"],
    }
    out.update(compute(constants, prec=90))

    with open(sys.argv[2], "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)

    print("[generate] wrote", sys.argv[2])
    print("[generate] PASS =", out["pass"])
    print("[generate] lhs_interval.hi =", out["lhs_interval"]["hi"])
    print("[generate] rhs_interval.lo =", out["rhs_interval"]["lo"])

if __name__ == "__main__":
    main()
