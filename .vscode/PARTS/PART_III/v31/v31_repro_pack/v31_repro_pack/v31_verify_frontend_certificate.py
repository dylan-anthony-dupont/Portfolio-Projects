#!/usr/bin/env python3
"""v31_verify_frontend_certificate.py

Verifier for the front-end certificate JSON produced by v31_generate_frontend_certificate.py.

This verifier checks the internal logic only:
- parses the JSON
- confirms that the required finite-height H0 is <= the cited verification height

It does NOT re-run the cited large-scale computation (Platt--Trudgian); that result is treated as an
external, peer-reviewed input in the manuscript.

Usage:
  python3 v31_verify_frontend_certificate.py --certificate v31_frontend_certificate.json

Exit codes:
- 0 on PASS
- nonzero on FAIL
"""

from __future__ import annotations

import argparse
import json


def main() -> int:
    ap = argparse.ArgumentParser(description="Verify v31 front-end certificate JSON (internal logic only).")
    ap.add_argument("--certificate", required=True, help="Path to v31_frontend_certificate.json")
    args = ap.parse_args()

    with open(args.certificate, "r", encoding="utf-8") as f:
        cert = json.load(f)

    needed = cert.get("needed_frontend_statement", {})
    discharged = cert.get("discharged_by", {})

    H0 = float(needed.get("H0"))
    Hc = float(discharged.get("verification_height"))

    ok = H0 <= Hc

    print("H0 (needed) =", H0)
    print("H_cited     =", Hc)
    print(f"CHECK: H0 <= H_cited : {ok}")

    if not ok:
        print("FAIL")
        return 1

    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
