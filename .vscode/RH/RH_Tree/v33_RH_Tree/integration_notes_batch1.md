# Integration Notes — Batch 1 (compressed digest)

This digest records what Batch‑1 patch packets changed and what was merged into **v33**.

## Merged into v33 (manuscript-level)

### RH‑FORCE → G‑3 (PASS)
- Restored the forcing constant **K_alloc** to the correct value `3+8√3` and propagated it through the tail inequality and absorption coefficients.
- Removes the “silent looseness” that could mask a forcing deficit.

### RH‑BRIDGE → G‑6 (PASS / merged)
- Replaced Bridge‑1’s boundary‑modulus ambiguity with:
  - Dirichlet outer factor on the rectangle.
  - Inner collapse via Dirichlet uniqueness (no max‑modulus/boundary regularity loopholes).
- Adopted in v33 as the canonical Bridge‑1 statement.

### RH‑LOCAL → G‑8 (PASS)
- Replaced qualitative `N_loc(m) << log m` with explicit unconditional bound:
  - `N_loc(m) ≤ 1.01 log m + 17` for `m≥10`.
- Integrated directly into the residual+local corollary and the tail inequality.

### RH‑ABSORB → G‑4/G‑5 (CONDITIONAL → partial merge)
- Implemented the hygiene pieces that are safe to merge immediately:
  - separation of nominal scale `δ0` from chosen admissible `δ ≤ δ0`,
  - existence of κ‑admissible shrink (non‑circular),
  - monotonic safety under δ‑shrinking.
- Remaining work is to prove δ‑uniformity of all constants used in the inequality chain.

### RH‑ENVELOPE → G‑2/G‑4/G‑12 (CONDITIONAL → partial merge)
- Merged the **interface hardening** warning:
  - no “residual proxying” (F'/F does not directly bound E'/E).
- Did **not** (yet) replace the residual envelope lemma proof; that remains the core OPEN blocker.

## Still OPEN after v33

- **G‑1 / G‑12:** independent proof + provenance of `C1,C2,C_up,C_h''`, with δ‑uniformity discipline.
- **G‑2:** scaling audit in upper‑envelope chain (δ‑exponent bookkeeping end‑to‑end).
- **G‑7:** free‑m / quantifier hygiene sweep (global).
- **G‑11:** internal replacement for finite‑height verification is optional; keep as labeled external input for now.

