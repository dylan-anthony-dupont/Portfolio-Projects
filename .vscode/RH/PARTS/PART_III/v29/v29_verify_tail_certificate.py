#!/usr/bin/env python3
"""
verify_tail_certificate.py  (v29)

Verifies that:
  (1) tail_certificate.json is exactly the output produced by
      generate_tail_certificate.py from the given constants.json,
  (2) the tail inequality holds in certified interval form:
        lhs_interval.hi < rhs_interval.lo

Usage:
  python3 verify_tail_certificate.py constants.json tail_certificate.json
"""

import json
import sys
from decimal import Decimal

import subprocess
import tempfile
import os

def dec(s: str) -> Decimal:
    return Decimal(s)

def same_interval(a, b) -> bool:
    return a["lo"] == b["lo"] and a["hi"] == b["hi"]

def main():
    if len(sys.argv) != 3:
        print("Usage: verify_tail_certificate.py constants.json tail_certificate.json", file=sys.stderr)
        sys.exit(2)

    const_path = sys.argv[1]
    cert_path  = sys.argv[2]

    with open(const_path, "r", encoding="utf-8") as f:
        constants = json.load(f)
    with open(cert_path, "r", encoding="utf-8") as f:
        cert = json.load(f)

    # Re-generate in a temp file and compare byte-for-byte canonical JSON.
    with tempfile.TemporaryDirectory() as td:
        regen_path = os.path.join(td, "regen.json")
        gen_cmd = [sys.executable, os.path.join(os.path.dirname(__file__), "generate_tail_certificate.py"), const_path, regen_path]
        subprocess.check_call(gen_cmd)

        with open(regen_path, "r", encoding="utf-8") as f:
            regen = json.load(f)

    # Compare key fields; we avoid strict file equality because JSON formatting can vary.
    keys = [
        "certificate_version","m_band","eta","alpha","prec","pi_interval","logm_interval","delta_interval",
        "L_interval","lhs_interval","rhs_interval","derived_constants","pass"
    ]
    mism = []
    for k in keys:
        if regen.get(k) != cert.get(k):
            mism.append(k)

    lhs_hi = dec(cert["lhs_interval"]["hi"])
    rhs_lo = dec(cert["rhs_interval"]["lo"])
    passed = (lhs_hi < rhs_lo)

    print("m_band =", cert["m_band"])
    print("eta    =", cert["eta"])
    print("alpha  =", cert["alpha"])
    print("LHS interval =", cert["lhs_interval"])
    print("RHS interval =", cert["rhs_interval"])
    print("Check: lhs.hi < rhs.lo  ==> ", lhs_hi, "<", rhs_lo, "=", passed)

    if mism:
        print("FAIL: certificate mismatch in keys:", ", ".join(mism))
        sys.exit(1)
    if not cert.get("pass", False):
        print("FAIL: certificate 'pass' field is false")
        sys.exit(1)
    if not passed:
        print("FAIL: inequality does not hold")
        sys.exit(1)

    print("PASS")

if __name__ == "__main__":
    main()
