#!/usr/bin/env python3
"""v33_generate_frontend_certificate.py

Creates a pinned JSON certificate for the finite-height front-end assumption used by v33.

This script does NOT compute zeta zeros. It encodes a minimal (H0, citation) logic statement:
if RH has been verified up to H_cited and H0 <= H_cited, then RH holds up to height H0.

Usage:
  python3 v33_generate_frontend_certificate.py v33_frontend_certificate.json
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
import sys


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: v33_generate_frontend_certificate.py output.json", file=sys.stderr)
        return 2

    out = {
        "certificate_version": "v33",
        "created_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "needed_frontend_statement": {
            "type": "RH_to_height",
            "H0": 5.0,
            "text": "All nontrivial zeros rho=beta+i gamma with 0<gamma<=H0 satisfy beta=1/2."
        },
        "discharged_by": {
            "type": "literature_citation",
            "verification_height": 3e12,
            "reference": {
                "authors": "D. J. Platt and T. S. Trudgian",
                "title": "The Riemann hypothesis is true up to 3*10^12",
                "venue": "Bulletin of the London Mathematical Society",
                "year": 2021,
                "doi": "10.1112/blms.12460",
                "arxiv": "2004.09765",
                "statement": "All zeros beta+i gamma with 0<gamma<=3*10^12 satisfy beta=1/2 (rigorous interval arithmetic)."
            },
            "logic": "If RH holds for 0<gamma<=H_cited and H0<=H_cited, then RH holds for 0<gamma<=H0."
        },
        "notes": [
            "This JSON is not itself a computation of zeros; it is a pinned statement+reference used by v33.",
            "For a fully self-contained proof without external computational input, one would need to implement and certify an argument-principle zero count in this region using ball arithmetic (not provided here)."
        ]
    }

    with open(sys.argv[1], "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)

    print("[generate] wrote", sys.argv[1])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
