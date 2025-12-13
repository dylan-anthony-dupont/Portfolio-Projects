#!/usr/bin/env python3
"""
tick_generator_audit.py  (supplementary; NOT used in the proof)

Deterministic prime-locked tick generator and an audit against "true" zeta zeros
computed internally by mpmath (zetazero). This avoids any network dependency.

WARNING:
  - This is a floating-point audit (mpmath), not a certified proof computation.
  - It is included only as supplementary numerics and does not feed into the RH proof.

Usage:
  python3 tick_generator_audit.py

Outputs:
  A small table of max/mean absolute error and max/mean relative error for j=2..J
  for a few cutoff constants C in X(t)=C*(log t)^(3/2).
"""

import math
from typing import List, Tuple

import mpmath as mp

mp.mp.dps = 80

def smooth_weight(y: mp.mpf) -> mp.mpf:
    # W(y)=exp(1-1/(1-y)) for 0<=y<1; W(1)=0; W(y)=0 for y>1
    if y <= 0:
        return mp.mpf(1)
    if y >= 1:
        return mp.mpf(0)
    return mp.e ** (1 - 1/(1 - y))

def primes_up_to(n: int) -> List[int]:
    if n < 2:
        return []
    sieve = bytearray(b"\x01")*(n+1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(n**0.5)+1):
        if sieve[p]:
            step = p
            start = p*p
            sieve[start:n+1:step] = b"\x00"*(((n-start)//step)+1)
    return [i for i in range(n+1) if sieve[i]]

def prime_powers_up_to(X: int) -> List[Tuple[int,int,int]]:
    # returns list of (p, k, p**k) with p prime, k>=1, p^k <= X
    ps = primes_up_to(X)
    out = []
    for p in ps:
        pk = p
        k = 1
        while pk <= X:
            out.append((p,k,pk))
            k += 1
            pk *= p
    return out

def theta(t: mp.mpf) -> mp.mpf:
    # Continuous Riemann–Siegel theta (mpmath handles branches)
    return mp.siegeltheta(t)


def X_of_t(t: mp.mpf, C: int) -> mp.mpf:
    return mp.mpf(C) * (mp.log(t) ** (mp.mpf(3)/2))

def P_X(t: mp.mpf, Delta: mp.mpf, C: int) -> mp.mpf:
    X = X_of_t(t, C)
    X_int = int(mp.floor(X))
    if X_int < 2:
        return mp.mpf(0)
    pp = prime_powers_up_to(X_int)
    total = mp.mpf(0)
    for p,k,pk_int in pp:
        pk = mp.mpf(pk_int)
        w = smooth_weight(pk / X)
        if w == 0:
            continue
        coef = (1/(k * mp.mpf(p)**(k/2))) * w
        arg1 = (t+Delta) * k * mp.log(p)
        arg0 = t * k * mp.log(p)
        total -= coef * (mp.sin(arg1) - mp.sin(arg0))
    return total

def F_j(tj: mp.mpf, Delta: mp.mpf, C: int) -> mp.mpf:
    return (theta(tj+Delta) - theta(tj)) + P_X(tj, Delta, C) - mp.pi

def next_tick(tj: mp.mpf, C: int, max_expand: int = 120) -> mp.mpf:
    lo = mp.mpf(0)
    flo = F_j(tj, lo, C)  # should be -pi
    hi = mp.mpf(5)
    fhi = F_j(tj, hi, C)
    expand = 0
    while fhi <= 0 and expand < max_expand:
        hi *= 2
        fhi = F_j(tj, hi, C)
        expand += 1
    if fhi <= 0:
        raise RuntimeError("Failed to bracket root; increase max_expand.")

    # bisection
    for _ in range(140):
        mid = (lo+hi)/2
        fmid = F_j(tj, mid, C)
        if fmid <= 0:
            lo = mid
        else:
            hi = mid
    return tj + hi

def true_zeros(J: int) -> List[mp.mpf]:
    # mpmath provides approximate zeros on the critical line.
    # This is NOT certified, but is deterministic at the chosen mp.dps.
    return [mp.im(mp.zetazero(j)) for j in range(1, J+1)]

def stats(errs: List[mp.mpf], truths: List[mp.mpf]) -> Tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf]:
    abs_err = [abs(e) for e in errs]
    rel_err = [abs(e)/abs(truths[i]) for i,e in enumerate(errs)]
    return max(abs_err), mp.fsum(abs_err)/len(abs_err), max(rel_err), mp.fsum(rel_err)/len(rel_err)

def run_audit(C_values=(16,32,48), J=50):
    gammas = true_zeros(J)
    t1 = gammas[0]
    true_m = [2*g for g in gammas]

    print("Prime-locked tick generator audit (supplementary; floating point)")
    print("Truth zeros from mpmath.zetazero(j), mp.dps =", mp.mp.dps)
    print("Stats exclude j=1 (seed); errors computed over j=2..J.\n")

    print("{:>6s}  {:>14s}  {:>14s}  {:>14s}  {:>14s}".format("C","max|Δm|","mean|Δm|","max rel","mean rel"))
    for C in C_values:
        ticks = [t1]
        for j in range(1, J):
            ticks.append(next_tick(ticks[-1], C))
        tick_m = [2*t for t in ticks]
        errs = [tick_m[j]-true_m[j] for j in range(1, J)]
        truths = [true_m[j] for j in range(1, J)]
        mx, mean, mxr, meanr = stats(errs, truths)
        print("{:6d}  {:14.6e}  {:14.6e}  {:14.6e}  {:14.6e}".format(C, float(mx), float(mean), float(mxr), float(meanr)))

if __name__ == "__main__":
    run_audit()
