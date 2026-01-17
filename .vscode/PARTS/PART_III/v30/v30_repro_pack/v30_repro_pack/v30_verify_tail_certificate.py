#!/usr/bin/env python3
"""v30_verify_tail_certificate.py

Canonical verifier entrypoint shipped with manuscript v30.

This verifier:
1) Regenerates a fresh tail certificate from a constants JSON file using the v29
   directed-rounding generator implementation.
2) Checks that the provided/pinned certificate matches the regenerated certificate
   on a fixed set of required fields.
3) Checks the strict interval inequality:
       lhs_interval.hi < rhs_interval.lo

Exit codes:
- 0 on PASS
- nonzero on FAIL

Usage:
  python3 v30_verify_tail_certificate.py \
    --constants v29_constants.json \
    --certificate v29_tail_certificate.json
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
from decimal import Decimal
from typing import Any, Dict, List


def _load_module_from_path(module_name: str, path: str):
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load module {module_name} from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore[attr-defined]
    return module


def main() -> int:
    ap = argparse.ArgumentParser(description="Verify the v29 tail certificate using a v30 stable entrypoint.")
    ap.add_argument("--constants", required=True, help="Path to constants JSON (e.g., v29_constants.json)")
    ap.add_argument("--certificate", required=True, help="Path to pinned tail certificate JSON")
    ap.add_argument(
        "--generator",
        default=os.path.join(os.path.dirname(__file__), "v29_generate_tail_certificate.py"),
        help="Path to v29_generate_tail_certificate.py (default: alongside this script)",
    )
    ap.add_argument("--prec", type=int, default=90, help="Decimal precision used by the generator (default: 90)")
    args = ap.parse_args()

    with open(args.constants, "r", encoding="utf-8") as f:
        constants: Dict[str, Any] = json.load(f)
    with open(args.certificate, "r", encoding="utf-8") as f:
        cert: Dict[str, Any] = json.load(f)

    gen = _load_module_from_path("v29_generate_tail_certificate", args.generator)

    regen: Dict[str, Any] = {
        "certificate_version": "v29",
        "m_band": constants["m_band"],
        "eta": constants["eta"],
        "alpha": constants["alpha_worst"],
    }
    regen.update(gen.compute(constants, prec=args.prec))

    # Compare a fixed set of required keys (independent of JSON pretty-print formatting).
    required_keys: List[str] = [
        "certificate_version",
        "m_band",
        "eta",
        "alpha",
        "prec",
        "pi_interval",
        "logm_interval",
        "delta_interval",
        "L_interval",
        "lhs_interval",
        "rhs_interval",
        "derived_constants",
        "pass",
    ]

    mism: List[str] = [k for k in required_keys if regen.get(k) != cert.get(k)]

    lhs_hi = Decimal(str(cert["lhs_interval"]["hi"]))
    rhs_lo = Decimal(str(cert["rhs_interval"]["lo"]))
    strict_ok = lhs_hi < rhs_lo

    print("m_band =", cert.get("m_band"))
    print("eta    =", cert.get("eta"))
    print("alpha  =", cert.get("alpha"))
    print("LHS interval =", cert.get("lhs_interval"))
    print("RHS interval =", cert.get("rhs_interval"))
    print(f"CHECK: lhs.hi < rhs.lo : {strict_ok}")

    if mism:
        print("FAIL: certificate mismatch in keys:", ", ".join(mism))
        return 1
    if not cert.get("pass", False):
        print("FAIL: certificate 'pass' field is false")
        return 1
    if not strict_ok:
        print("FAIL: inequality does not hold")
        return 1

    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
