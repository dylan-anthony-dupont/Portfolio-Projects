#!/usr/bin/env python3
"""v31_generate_frontend_certificate.py

Generates a small, explicit "front-end" certificate JSON for the low-height region.

Important: This script does NOT attempt to re-run any large-scale RH verification
computation (e.g. Platt--Trudgian). Instead, it records:
  - the exact finite-height statement needed by manuscript v31, and
  - the external published verification result used to discharge it.

This is consistent with standard mathematical practice: an externally published,
peer-reviewed, rigorous computation can be cited as an input.

Usage:
  python3 v31_generate_frontend_certificate.py --H0 5 --out v31_frontend_certificate.json

The corresponding verifier script v31_verify_frontend_certificate.py checks that
H0 is indeed within the cited verification height.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone


# Published rigorous verification height used for discharge.
# Platt--Trudgian (BLMS 2021) proves RH for all zeros with 0 < Im(s) <= 3e12.
H_CITED = 3_000_000_000_000.0

REFERENCE = {
    "authors": "D. J. Platt and T. S. Trudgian",
    "title": "The Riemann hypothesis is true up to 3*10^12",
    "venue": "Bulletin of the London Mathematical Society",
    "year": 2021,
    "doi": "10.1112/blms.12460",
    "arxiv": "2004.09765",
    "statement": "All zeros beta+i gamma with 0<gamma<=3*10^12 satisfy beta=1/2 (rigorous interval arithmetic).",
}


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate a front-end certificate JSON (v31).")
    ap.add_argument("--H0", type=float, required=True, help="Finite height in the s-plane to be discharged (e.g. H0=5 when m*=10).")
    ap.add_argument("--out", required=True, help="Output JSON path")
    args = ap.parse_args()

    out = {
        "certificate_version": "v31",
        "created_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "needed_frontend_statement": {
            "type": "RH_to_height",
            "H0": args.H0,
            "text": "All nontrivial zeros rho=beta+i gamma with 0<gamma<=H0 satisfy beta=1/2.",
        },
        "discharged_by": {
            "type": "literature_citation",
            "verification_height": H_CITED,
            "reference": REFERENCE,
            "logic": "If RH holds for 0<gamma<=H_cited and H0<=H_cited, then RH holds for 0<gamma<=H0.",
        },
        "notes": [
            "This JSON is not itself a computation of zeros; it is a pinned statement+reference used by v31.",
            "For a fully self-contained proof without external computational input, one would need to implement and certify an argument-principle zero count in this region using ball arithmetic (not provided here).",
        ],
    }

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)

    print("[v31_frontend_generate] wrote", args.out)
    print("[v31_frontend_generate] H0 =", args.H0)
    print("[v31_frontend_generate] discharged by verification height =", H_CITED)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
