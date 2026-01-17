#!/usr/bin/env python3
"""v30_generate_tail_certificate.py

Canonical generator entrypoint shipped with manuscript v30.

This is a thin wrapper around the v29 generator implementation
(v29_generate_tail_certificate.py). It exists so that v30 provides stable,
versioned entrypoints without modifying the v29 artifacts.

Properties:
- deterministic (no network, no randomness)
- uses directed-rounding interval arithmetic (decimal ROUND_FLOOR/ROUND_CEILING)
  as implemented in the v29 generator

CLI:
  python3 v30_generate_tail_certificate.py \
    --constants v29_constants.json \
    --out regen_tail_certificate.json

Notes:
- The generated JSON is intended to match the v29 pinned certificate exactly
  when run with the same constants file.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
from typing import Any, Dict


def _load_module_from_path(module_name: str, path: str):
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load module {module_name} from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore[attr-defined]
    return module


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate tail_certificate.json deterministically (v30 wrapper around v29).")
    ap.add_argument("--constants", required=True, help="Path to constants JSON (e.g., v29_constants.json)")
    ap.add_argument("--out", required=True, help="Output path for generated certificate JSON")
    ap.add_argument(
        "--v29-generator",
        default=os.path.join(os.path.dirname(__file__), "v29_generate_tail_certificate.py"),
        help="Path to v29_generate_tail_certificate.py (default: alongside this script)",
    )
    ap.add_argument("--prec", type=int, default=90, help="Decimal precision used by the generator (default: 90)")
    args = ap.parse_args()

    with open(args.constants, "r", encoding="utf-8") as f:
        constants: Dict[str, Any] = json.load(f)

    gen = _load_module_from_path("v29_generate_tail_certificate", args.v29_generator)

    # Compute exactly as v29 generator does.
    out: Dict[str, Any] = {
        "certificate_version": "v29",
        "m_band": constants["m_band"],
        "eta": constants["eta"],
        "alpha": constants["alpha_worst"],
    }
    out.update(gen.compute(constants, prec=args.prec))

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)

    print("[v30_generate] wrote", args.out)
    print("[v30_generate] PASS =", bool(out.get("pass")))
    print("[v30_generate] lhs_interval.hi =", out["lhs_interval"]["hi"])
    print("[v30_generate] rhs_interval.lo =", out["rhs_interval"]["lo"])

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
