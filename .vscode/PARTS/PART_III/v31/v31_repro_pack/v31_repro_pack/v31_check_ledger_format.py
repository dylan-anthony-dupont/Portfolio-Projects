#!/usr/bin/env python3
"""v31_check_ledger_format.py

Self-consistency check for a constants-ledger JSON.

This script is NOT an independent certification of the mathematical truth of the
interval enclosures. It only checks that the file is syntactically well-formed
and internally consistent (interval endpoints parse as decimals and satisfy lo<=hi).

Usage:
  python3 v31_check_ledger_format.py --constants v29_constants.json

Exit codes:
- 0 on PASS
- nonzero on FAIL
"""

from __future__ import annotations

import argparse
import json
from decimal import Decimal


REQUIRED_INTERVALS = ["C1", "C2", "C_up", "C_hpp"]


def main() -> int:
    ap = argparse.ArgumentParser(description="Check internal consistency of a constants ledger JSON (v31).")
    ap.add_argument("--constants", required=True, help="Path to constants JSON")
    args = ap.parse_args()

    with open(args.constants, "r", encoding="utf-8") as f:
        c = json.load(f)

    if "intervals" not in c:
        print("FAIL: missing key 'intervals'")
        return 1

    intervals = c["intervals"]
    missing = [k for k in REQUIRED_INTERVALS if k not in intervals]
    if missing:
        print("FAIL: missing required intervals:", ", ".join(missing))
        return 1

    ok = True
    for k in REQUIRED_INTERVALS:
        lo_s = intervals[k]["lo"]
        hi_s = intervals[k]["hi"]
        lo = Decimal(str(lo_s))
        hi = Decimal(str(hi_s))
        if lo > hi:
            print(f"FAIL: interval {k} has lo>hi: {lo} > {hi}")
            ok = False
        else:
            print(f"{k}: [{lo}, {hi}]")

    if not ok:
        return 1

    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
