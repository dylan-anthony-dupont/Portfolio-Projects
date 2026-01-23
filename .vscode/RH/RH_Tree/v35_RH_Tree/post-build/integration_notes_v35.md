# Integration Notes — v35 lock

Locked: 2026-01-23  
Baseline: v34 + Batch-4 patch queue  
Intent: **truth-latching build** (encode what is proved, and what is ruled out)

## Canonical posture (post-v35)

- **Primary frontier:** **S5** = *non-pointwise UE redesign* (endpoint + collar interface redesign).
- **Audit scaffold:** S2-style certified criterion/harness remains (per-height tail-check + finite-height front-end certificate).
- **Retired closure route:** S1/S1′ *pointwise/sup UE + collar + η-absorption* (moved to Appendix; NO-GO results proved in-text).

## What v35 made unambiguous

1) **Completion/entireness fixed.**  
   Working object is now the entire completion \(\Xi_2(u)=\xi(u/2)\) and \(E(v)=\Xi_2(1+v)\).  
   This eliminates a persistent “entire vs meromorphic” ambiguity at the foundation.

2) **Absorption obstruction is proof-grade.**  
   Under nominal scaling \(\delta_0=\eta\alpha/(\log m)^2\) and growth \(N_{\rm loc}(m)\ll\log m\), uniform η-shrinking needs
   \(p-\theta\ge 1/2\) (Exponent Budget Theorem).  
   In the proved pointwise regime: \(p=1\), \(\theta=1\) → local term is δ⁰ → absorption cannot shrink it.

3) **No “recover p>1” inside pointwise endpoint class.**  
   UE scaling NO-GO lemma forbids \(p>1\) with the pointwise/sup endpoint and shape-only constants.

4) **Forcing cannot be made to grow in the current architecture.**  
   Single-box forcing is constant-limited (phase variation ≤ 2π), so forcing cannot “outrun” the local term by height growth.

5) **Bridge-1 is one-way only.**  
   \(|W|=1\) on \(\partial B\) does not imply zero-freeness/constancy; the manuscript now encodes this explicitly to prevent silent converse use.

## What remains genuinely open (the frontier)

- **S5 redesign must be forceable.**  
  Either new endpoint \(\Phi_B\) dominates the dial deviation \(D_B(W)\), or a new forcing lemma must lower-bound \(\Phi_B\) directly.
- **Residual envelope ledger** still requires proof-grade sourcing with constants and uniformity.
- **Finite-height front-end** is still an external certificate input (kept quarantined as such).

## Drift locks added

- Executive Proof Status now includes explicit NO-GO bullets.
- Appendix “Discarded closure routes” records why S1/S1′ is invalid in its present form.
- Repro pack now records endpoint + forcing metadata to prevent silent mismatch under future S5 experiments.
