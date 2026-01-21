#!/usr/bin/env python3
"""v30_tick_generator_audit.py

Supplementary tick-generator audit script (NOT used in the RH proof).

This is an optimized, reproducible v30 wrapper around the v29 tick audit idea.
Key changes vs v29_tick_generator_audit.py:
- Caches prime powers once per (C, J) run instead of recomputing inside bisection.
- Optionally consumes a frozen truth dataset file (JSON) instead of calling
  mpmath.zetazero at runtime.
- Prints simple runtime benchmarks.

WARNING / CLAIM HYGIENE:
- All computations here are floating-point (mpmath).
- Unless the truth dataset comes from an external verified source, results are
  "illustrative numerics" only and MUST NOT be described as "certified".

Usage examples:
  python3 v30_tick_generator_audit.py --truth v30_truth_zeros_mpmath_dps80_J50.json --J 50 --C 16 32 48
  python3 v30_tick_generator_audit.py --J 50 --C 16 32 48 --mp-dps 80
"""

from __future__ import annotations

import argparse
import json
import math
import time
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import mpmath as mp


# -----------------------------
# Utility: smooth cutoff weight
# -----------------------------

def smooth_weight(y: mp.mpf) -> mp.mpf:
    """W(y)=exp(1-1/(1-y)) for 0<=y<1; W(1)=0; W(y)=0 for y>1."""
    if y <= 0:
        return mp.mpf(1)
    if y >= 1:
        return mp.mpf(0)
    return mp.e ** (1 - 1 / (1 - y))


# -----------------------------
# Prime powers cache
# -----------------------------

def primes_up_to(n: int) -> List[int]:
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            step = p
            start = p * p
            sieve[start : n + 1 : step] = b"\x00" * (((n - start) // step) + 1)
    return [i for i in range(n + 1) if sieve[i]]


@dataclass(frozen=True)
class PrimePower:
    p: int
    k: int
    pk: int
    logp: mp.mpf
    coef_base: mp.mpf  # 1/(k * p^(k/2))


def prime_powers_up_to_cached(X: int) -> List[PrimePower]:
    ps = primes_up_to(X)
    out: List[PrimePower] = []
    for p in ps:
        pk = p
        k = 1
        logp = mp.log(p)
        while pk <= X:
            # coef_base = 1/(k * p^(k/2))
            coef_base = mp.mpf(1) / (mp.mpf(k) * (mp.mpf(p) ** (mp.mpf(k) / 2)))
            out.append(PrimePower(p=p, k=k, pk=pk, logp=logp, coef_base=coef_base))
            k += 1
            pk *= p
    out.sort(key=lambda t: t.pk)
    return out


# -----------------------------
# Tick generator core
# -----------------------------

def theta(t: mp.mpf) -> mp.mpf:
    return mp.siegeltheta(t)


def X_of_t(t: mp.mpf, C: int) -> mp.mpf:
    return mp.mpf(C) * (mp.log(t) ** (mp.mpf(3) / 2))


def P_X(
    t: mp.mpf,
    Delta: mp.mpf,
    C: int,
    pp_cache: Sequence[PrimePower],
) -> mp.mpf:
    """Prime-power smoothed sum with cached prime powers."""
    X = X_of_t(t, C)
    X_int = int(mp.floor(X))
    if X_int < 2:
        return mp.mpf(0)

    total = mp.mpf(0)
    # Only iterate pk <= X_int (cache sorted by pk)
    for pp in pp_cache:
        if pp.pk > X_int:
            break
        pk = mp.mpf(pp.pk)
        w = smooth_weight(pk / X)
        if w == 0:
            continue
        coef = pp.coef_base * w
        arg1 = (t + Delta) * pp.k * pp.logp
        arg0 = t * pp.k * pp.logp
        total -= coef * (mp.sin(arg1) - mp.sin(arg0))
    return total


def F_j(
    tj: mp.mpf,
    theta_tj: mp.mpf,
    Delta: mp.mpf,
    C: int,
    pp_cache: Sequence[PrimePower],
) -> mp.mpf:
    return (theta(tj + Delta) - theta_tj) + P_X(tj, Delta, C, pp_cache) - mp.pi


def next_tick(
    tj: mp.mpf,
    C: int,
    pp_cache: Sequence[PrimePower],
    tol: mp.mpf,
    max_expand: int = 120,
    max_iter: int = 140,
) -> mp.mpf:
    """Find next tick by bracketing + bisection on Delta > 0."""
    theta_tj = theta(tj)

    lo = mp.mpf(0)
    flo = F_j(tj, theta_tj, lo, C, pp_cache)  # should be -pi

    hi = mp.mpf(5)
    fhi = F_j(tj, theta_tj, hi, C, pp_cache)
    expand = 0
    while fhi <= 0 and expand < max_expand:
        hi *= 2
        fhi = F_j(tj, theta_tj, hi, C, pp_cache)
        expand += 1
    if fhi <= 0:
        raise RuntimeError("Failed to bracket root; increase max_expand.")

    for _ in range(max_iter):
        mid = (lo + hi) / 2
        fmid = F_j(tj, theta_tj, mid, C, pp_cache)
        if fmid <= 0:
            lo = mid
        else:
            hi = mid
        if hi - lo < tol:
            break
    return tj + hi


# -----------------------------
# Truth dataset
# -----------------------------

def load_truth_zeros(path: str) -> List[mp.mpf]:
    with open(path, "r", encoding="utf-8") as f:
        obj = json.load(f)
    gammas = obj.get("gammas")
    if not isinstance(gammas, list) or not gammas:
        raise ValueError("Truth file does not contain a 'gammas' list.")
    return [mp.mpf(s) for s in gammas]


def true_zeros_mpmath(J: int) -> List[mp.mpf]:
    return [mp.im(mp.zetazero(j)) for j in range(1, J + 1)]


# -----------------------------
# Reporting
# -----------------------------

def stats(errs: List[mp.mpf], truths: List[mp.mpf]) -> Tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf]:
    abs_err = [abs(e) for e in errs]
    rel_err = [abs(e) / abs(truths[i]) for i, e in enumerate(errs)]
    return max(abs_err), mp.fsum(abs_err) / len(abs_err), max(rel_err), mp.fsum(rel_err) / len(rel_err)


def run_audit(C_values: Sequence[int], J: int, truth_path: Optional[str], mp_dps: int) -> int:
    mp.mp.dps = mp_dps

    if truth_path:
        gammas = load_truth_zeros(truth_path)
        if len(gammas) < J:
            raise ValueError(f"Truth file contains only {len(gammas)} zeros, but J={J} requested")
        gammas = gammas[:J]
        truth_source = f"frozen truth file: {truth_path}"
    else:
        gammas = true_zeros_mpmath(J)
        truth_source = "mpmath.zetazero (computed at runtime; floating-point)"

    t1 = gammas[0]
    true_m = [2 * g for g in gammas]
    t_max = max(gammas)

    print("Prime-locked tick generator audit (SUPPLEMENTARY; NOT USED IN PROOF)")
    print("Truth source:", truth_source)
    print("mp.mp.dps =", mp.mp.dps)
    print("Stats exclude j=1 (seed); errors computed over j=2..J.\n")

    print("{:>6s}  {:>12s}  {:>12s}  {:>12s}  {:>12s}  {:>10s}".format("C", "max|Δm|", "mean|Δm|", "max rel", "mean rel", "sec"))

    for C in C_values:
        # Precompute prime powers once for this C.
        X_max = int(mp.floor(X_of_t(t_max, C)))
        pp_cache = prime_powers_up_to_cached(max(2, X_max))

        start = time.perf_counter()
        ticks = [t1]
        # Choose a tolerance consistent with mp_dps.
        tol = mp.mpf("1e-40") if mp_dps >= 80 else mp.mpf("1e-25")
        for _j in range(1, J):
            ticks.append(next_tick(ticks[-1], C, pp_cache, tol=tol))
        elapsed = time.perf_counter() - start

        tick_m = [2 * t for t in ticks]
        errs = [tick_m[j] - true_m[j] for j in range(1, J)]
        truths = [true_m[j] for j in range(1, J)]
        mx, mean, mxr, meanr = stats(errs, truths)

        print(
            "{:6d}  {:12.4e}  {:12.4e}  {:12.4e}  {:12.4e}  {:10.2f}".format(
                C, float(mx), float(mean), float(mxr), float(meanr), elapsed
            )
        )

    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Supplementary tick generator audit (v30, optimized).")
    ap.add_argument("--truth", default=None, help="Path to frozen truth zeros JSON (optional)")
    ap.add_argument("--J", type=int, default=50, help="Number of zeros/ticks (default: 50)")
    ap.add_argument("--C", type=int, nargs="+", default=[16, 32, 48], help="Cutoff constants C values")
    ap.add_argument("--mp-dps", type=int, default=80, help="mpmath precision in decimal digits (default: 80)")
    args = ap.parse_args()

    return run_audit(C_values=args.C, J=args.J, truth_path=args.truth, mp_dps=args.mp_dps)


if __name__ == "__main__":
    raise SystemExit(main())
