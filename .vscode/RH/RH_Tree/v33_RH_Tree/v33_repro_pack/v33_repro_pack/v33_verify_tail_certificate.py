#!/usr/bin/env python3
"""
v33_verify_tail_certificate.py

Verifier for v33_tail_certificate_m10.json. This script:
- loads the constants JSON and the pinned certificate JSON
- regenerates the certificate from constants
- checks exact JSON equality on the computed fields
- reports PASS/FAIL and prints the strict-separation check LHS_hi < RHS_lo.

Usage:
  python3 v33_verify_tail_certificate.py --constants v33_constants_m10.json --certificate v33_tail_certificate_m10.json

Exit codes:
- 0 on PASS
- nonzero on FAIL
"""

from __future__ import annotations

import argparse
import json
import sys

from v33_generate_tail_certificate import compute


def main() -> int:
    ap = argparse.ArgumentParser(description="Verify v33 tail certificate (m=10).")
    ap.add_argument("--constants", required=True, help="Path to v33_constants_m10.json")
    ap.add_argument("--certificate", required=True, help="Path to v33_tail_certificate_m10.json")
    args = ap.parse_args()

    with open(args.constants, "r", encoding="utf-8") as f:
        constants = json.load(f)

    with open(args.certificate, "r", encoding="utf-8") as f:
        cert = json.load(f)

    regen = {
        "certificate_version": "v33",
        "m_band": constants["m_band"],
        "eta": constants["eta"],
        "alpha": constants["alpha_worst"],
        "kappa": constants["kappa"],
    }
    regen.update(compute(constants, prec=90))

    # Compare all keys that regen produces (ignore any extra keys in cert)
    ok = True
    for k, v in regen.items():
        if cert.get(k) != v:
            ok = False
            print(f"MISMATCH key={k}")
            print("  cert :", cert.get(k))
            print("  regen:", v)

    lhs_hi = regen["lhs_interval"]["hi"]
    rhs_lo = regen["rhs_interval"]["lo"]
    strict = (float(lhs_hi) < float(rhs_lo))

    print("LHS_hi =", lhs_hi)
    print("RHS_lo =", rhs_lo)
    print("STRICT (LHS_hi < RHS_lo) =", strict)

    if not ok or not strict or not regen["pass"]:
        print("FAIL")
        return 1

    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
