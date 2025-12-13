#!/usr/bin/env python3

"""
verify_tail_certificate.py (v28)

Deterministically re-computes the algebraic tail inequality (Theorem Tail Closure)
from the JSON certificate files:

  - constants.json
  - tail_certificate.json

It prints interval bounds and exits with code 0 iff the certificate passes:
  LHS.hi < RHS.lo

This script is algebra-only; it does not compute the constants C1,C2,C_up,C_hpp.
Those must already be certified and stored in constants.json.

Usage:
  python3 verify_tail_certificate.py constants.json tail_certificate.json
"""

import json
import math
import sys

def read_json(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    if len(sys.argv) != 3:
        print("Usage: verify_tail_certificate.py constants.json tail_certificate.json", file=sys.stderr)
        sys.exit(2)

    constants_path = sys.argv[1]
    tail_path = sys.argv[2]

    C = read_json(constants_path)
    T = read_json(tail_path)

    eta = float(C["eta"])
    m = float(T["m"])
    alpha = float(T["alpha"])

    # Read constant intervals
    C1_lo = float(C["constants"]["C1"]["lo"])
    C1_hi = float(C["constants"]["C1"]["hi"])
    C2_lo = float(C["constants"]["C2"]["lo"])
    C2_hi = float(C["constants"]["C2"]["hi"])
    Cup_lo = float(C["constants"]["C_up"]["lo"])
    Cup_hi = float(C["constants"]["C_up"]["hi"])
    Ch_lo = float(C["constants"]["C_hpp"]["lo"])
    Ch_hi = float(C["constants"]["C_hpp"]["hi"])

    logm = math.log(m)
    delta = eta*alpha/(logm**2)

    # Fixed numeric constants (exact as in the paper)
    c0 = (1.0/(4.0*math.pi))*math.log(2.0*math.sqrt(2.0))
    c  = c0*math.pi/2.0
    Kalloc = 3.0 + 8.0*math.sqrt(3.0)

    # L interval
    L_lo = C1_lo*logm + C2_lo
    L_hi = C1_hi*logm + C2_hi

    # LHS interval upper bound
    lhs_hi = 2.0*Cup_hi*(delta**1.5)*L_hi
    lhs_lo = 2.0*Cup_lo*(delta**1.5)*L_lo

    # RHS interval lower bound
    sub_hi = delta*(Kalloc*c0*L_hi + Ch_hi*(logm+1.0))
    sub_lo = delta*(Kalloc*c0*L_lo + Ch_lo*(logm+1.0))
    rhs_lo = c - sub_hi
    rhs_hi = c - sub_lo

    ok = lhs_hi < rhs_lo

    print("m =", m)
    print("eta =", eta)
    print("alpha =", alpha)
    print("log m =", logm)
    print("delta =", delta)
    print("")
    print("L interval =", (L_lo, L_hi))
    print("LHS interval =", (lhs_lo, lhs_hi))
    print("RHS interval =", (rhs_lo, rhs_hi))
    print("")
    print("PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
