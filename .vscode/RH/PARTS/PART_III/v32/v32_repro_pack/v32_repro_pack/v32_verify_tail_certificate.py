#!/usr/bin/env python3
"""Verify a v32 tail certificate.

We recompute the tail inequality bounds from the constants file using the same
interval arithmetic as the generator and compare key fields.

This verifier is intentionally strict: it expects the stored (string)
representations of the recomputed intervals to match exactly.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

def _get(o, path):
    cur = o
    for p in path:
        cur = cur[p]
    return cur


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: v32_verify_tail_certificate.py <constants.json> <certificate.json>", file=sys.stderr)
        return 2

    const_path = Path(sys.argv[1])
    cert_path = Path(sys.argv[2])

    const = json.loads(const_path.read_text())
    cert = json.loads(cert_path.read_text())

    # Import compute_certificate and sha256_file from the generator.
    ns: dict = {}
    gen_src = Path(__file__).with_name("v32_generate_tail_certificate.py").read_text()
    exec(gen_src, ns)
    compute_certificate = ns["compute_certificate"]
    sha256_file = ns["sha256_file"]

    recomputed = compute_certificate(const)
    recomputed_nested = {
        "inputs": {
            "constants_sha256": sha256_file(const_path),
        },
        "derived": recomputed["derived"],
        "inequality": {
            "lhs_hi": recomputed["inequality"]["lhs_hi"],
            "rhs_lo": recomputed["inequality"]["rhs_lo"],
            "pass": recomputed["inequality"]["pass"],
        },
    }

    must_match_paths = [
        ("inputs", "constants_sha256"),
        ("derived", "log_m", "lo"),
        ("derived", "log_m", "hi"),
        ("derived", "delta", "lo"),
        ("derived", "delta", "hi"),
        ("derived", "L", "hi"),
        ("derived", "N_up", "hi"),
        ("inequality", "lhs_hi"),
        ("inequality", "rhs_lo"),
        ("inequality", "pass"),
    ]

    mismatches = []
    for p in must_match_paths:
        a = _get(cert, p)
        b = _get(recomputed_nested, p)
        if a != b:
            mismatches.append((p, a, b))

    if mismatches:
        print("FAIL: mismatch between stored and recomputed values:")
        for p, a, b in mismatches:
            print(f"  {'.'.join(p)}: stored={a} recomputed={b}")
        return 1

    if not cert.get("inequality", {}).get("pass", False):
        print("FAIL: certificate PASS flag is false")
        return 1

    print("PASS: tail certificate verified")
    print(f"  lhs_hi = {cert['inequality']['lhs_hi']}")
    print(f"  rhs_lo = {cert['inequality']['rhs_lo']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
