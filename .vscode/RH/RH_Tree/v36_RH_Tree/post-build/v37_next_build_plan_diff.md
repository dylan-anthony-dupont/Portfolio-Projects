# v36 → next build plan (diff-only)

## What stays locked
- v36 NO–GO constraints (pointwise UE ceiling; absolute $L^r$ endpoints; projection endpoints) remain **non-negotiable**.
- Repro pack schema latch remains **fail-closed** on endpoint metadata.

## New work for v37 pre-build
1. **S5 endpoint candidates (outside D5/D6):**
   - signed/oscillatory endpoints compatible with forcing (argument-principle / Hilbert-transform / winding-number style),
   - BMO/Carleson-type endpoints for `log|E|` (not absolute norms of `E'/E`),
   - any endpoint proposal must ship `(p, θ, q)` and forceability mode.
2. **Forceability link:**
   - if endpoint does not dominate `D_B(W)`, produce a new forcing lemma (or show domination).
3. **Local-interface improvement:**
   - redesign the collar/local mechanism so that the endpoint local exponent θ is strictly smaller than p.
4. **Audit harness upkeep:**
   - keep the tail-check scripts and metadata; no new numeric certificates required unless a candidate endpoint reaches `p−θ>0`.

## Acceptance gate for merging any S5 patch
- Must satisfy Remark `rem:S5-accept` and clear Theorem `thm:S5-budget` with explicit `(p, θ, q)`.
- Must not fall into Appendix D5 or D6 endpoint classes.
