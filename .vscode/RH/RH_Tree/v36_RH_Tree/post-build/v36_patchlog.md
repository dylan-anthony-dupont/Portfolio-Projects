# v36 patchlog (relative to v35)

**Build type:** guardrail / no-drift consolidation  
**Date:** 2026-01-24  
**Scope rule:** no new analytic closures; only *acceptance gates*, *NO–GO constraints*, and *schema latch*.

## Summary of proof-spine changes

### P36.1 — S5 acceptance criterion (ABSORB → CR)
- Inserted **Remark `rem:S5-accept`** at the start of Section 12 (S5 frontier).
- Purpose: force every S5 attempt to declare (UE exponent p, local exponent θ, growth q, forceability mode) and pass the S5 budget calculus.

### P36.2 — S5 Budget Theorem (ABSORB → CR)
- Inserted **Theorem `thm:S5-budget`** (general endpoint functional) in Section 12.
- Encodes the **uniformity condition** `2(p−θ) ≥ q` and **shrinkability** condition `p−θ > 0` under δ₀ = ηα/(log m)².

### P36.3 — Forceability gate hardening (FORCE → CR)
- Added **Lemma `lem:forceability-domination`** and **Remark `rem:s5-forceability-gate`**.
- Codifies: forcing currently lower-bounds only `D_B(W)`; any redesign that changes the target endpoint is **NO–GO** unless it either dominates `D_B(W)` or supplies a new forcing lemma.

### P36.4 — Baseline NO–GO: absolute Lʳ endpoints (BRIDGE → CR)
- Added **Subsection `subsec:S5-nogo-baseline`** and:
  - Lemma `lem:S5_Lp_collapse`
  - Proposition `prop:S5_Lp_nogo`
  - Remark `rem:S5_endpoint_implication`
- Encodes: for absolute `L^r(∂B)` endpoints of `E'/E`, the UE exponent collapses to `p(r)=1−1/r` and the collar/local split has `θ(r)=1−1/r`, hence `p−θ=0` (δ-inert local term).

### P36.5 — Baseline NO–GO: projection endpoints (ENVELOPE → CR)
- Added Lemma `lem:S5-projection-nogo` and Remark `rem:S5-nogo-consequence`.
- Encodes: endpoints that annihilate the local kernel span cannot control the *forced* dial deviation without a new forcing link.

### P36.6 — Local toolkit: L² collar norm bound (LOCAL → CR)
- Added Lemma `lem:Zloc-L2-collar` adjacent to Lemma `lem:Zloc-logder-collar`.
- Records the general `L^r` collar scaling: `||Z'loc/Zloc||_{L^r} ≤ 8^{1/r} N_loc/(κ δ^{1−1/r})`.

### P36.8 — Appendix expansion (ENVELOPE/BRIDGE/LOCAL → CR)
- Expanded Appendix `app:discarded` with:
  - **D5:** absolute `L^r` endpoints (NO–GO)
  - **D6:** projection-killing-local-term endpoints (NO–GO) + supporting projection documentation (`def:KB-projection`, `lem:proj-kills-Zloc`).

### P36.9 — Repro pack schema latch (FORCE/CR)
- Updated repro pack to **v36** and added **fail-closed validation**:
  - required metadata: endpoint + `(p, θ, q)` + `forceability_mode` + `forcing_architecture`
  - missing fields ⇒ verifier errors (certificate invalid).
- Tail check remains reproducible and (expectedly) reports **FAIL** for `p=1`.

## Non-structural edits
- Version bump: `v35 → v36` in title, executive status, appendix headings, and repro-pack references.
- Executive “NO–GO constraints” list updated to include S5 acceptance gate + new NO–GO results.

## Repro harness status
- `v36_verify_tail_check.py` reports `REGEN_MATCH = True`, `INEQUALITY_STRICT = False`.
- Front-end reference verifier reports `PASS` (logic check only).

