# v36 Patch Queue — Batch 5 (pre‑build)

Date: 2026-01-24  
Baseline: v35 locked (2026-01-23)  
Goal: **guardrail build** (encode S5 acceptance gates + NO‑GO results; prevent drift)

---

## Patch list (apply in order)

### P36.1 — S5 acceptance criterion (ABSORB) — **MANDATORY**
- **Insert:** Section 12 (start of S5 frontier).
- **TeX:** `rem:S5-accept` block.
- **Risk:** LOW (meta-level gate; no new analytic claim).
- **Purpose:** forbids “endpoint vibes”; forces explicit \((p,\theta,q)\) and forceability mode.

### P36.2 — S5 Budget Theorem (ABSORB) — **MANDATORY**
- **Insert:** Section 12 (after acceptance remark; before NO‑GO subsection).
- **TeX:** `thm:S5-budget`.
- **Risk:** LOW/MED (needs careful quantifiers: δ‑uniformity, κ‑admissibility, growth model).
- **Purpose:** single canonical feasibility test: \(2(p-\theta)\ge q\), plus monotonicity \(p-\theta\ge 0\).

### P36.3 — Forceability gate hardening (FORCE) — **MANDATORY**
- **Insert:** Section 12 near v35 Remark 12.1.
- **TeX:** `lem:forceability-domination` + `rem:s5-forceability-gate`.
- **Risk:** LOW (logical hygiene).
- **Purpose:** prevents invalid S5 proposals that change the forced object.

### P36.4 — NO‑GO: absolute \(L^r\) endpoints (BRIDGE) — **MANDATORY**
- **Insert:** Section 12, new subsection `subsec:S5-nogo-baseline`.
- **TeX:** `lem:S5_Lp_collapse`, `prop:S5_Lp_nogo`, `rem:S5_endpoint_implication`.
- **Risk:** LOW (guardrail; scaling sharp; independent of residual envelope).
- **Purpose:** closes “swap sup → absolute L^r” endpoint drift permanently.

### P36.5 — NO‑GO: projection endpoints (ENVELOPE) — **MANDATORY**
- **Insert:** same NO‑GO subsection as P36.4 (immediately after it).
- **TeX:** `lem:S5-projection-nogo` + `rem:S5-nogo-consequence` (and any needed prelim).
- **Risk:** LOW (guardrail; simple counterexample).
- **Purpose:** closes “project away local term” endpoint drift permanently (under current forcing).

### P36.6 — Local toolkit: \(L^2\) collar bound (LOCAL) — **RECOMMENDED**
- **Insert:** near collar/local split (after Lemma 10.8).
- **TeX:** `lem:Zloc-L2-collar`.
- **Risk:** LOW (derived from existing pointwise collar bound; explicitly scale-tracked).
- **Purpose:** records local scaling facts for future cancellation endpoints that measure \(Z'_{\rm loc}/Z_{\rm loc}\) in \(L^2\)-type spaces.

### P36.7 — Projection definition + “kills local term” lemma (LOCAL) — **OPTIONAL / APPENDIX**
- **Insert:** Appendix D6 as supporting material (not as an S5 candidate).
- **TeX:** `def:KB-projection`, `lem:proj-kills-Zloc`, `rem:proj-conditioning`.
- **Risk:** MED (can confuse readers if placed in main text; must be explicitly labelled “discarded route support”).
- **Purpose:** makes the projection NO‑GO concrete: we can exhibit a projection that annihilates the local term, hence the NO‑GO applies.

### P36.8 — Appendix expansion (ENVELOPE) — **MANDATORY**
- **Insert:** Appendix “Discarded closure routes”.
- **TeX:** D5 + D6 entries (edit D5 to reference the Bridge package to avoid duplication).
- **Risk:** LOW.
- **Purpose:** “line in the sand” documentation; prevents future re-litigation.

### P36.9 — Repro pack schema latch (FORCE/CR) — **MANDATORY**
- **Insert:** repro-pack README / schema.
- **Risk:** LOW.
- **Purpose:** enforce G‑12: S5 experiments must declare endpoint + exponents + forceability mode.

---

## Integration dependencies

- None of these patches require new computation.
- These patches do **not** solve S5; they narrow it and hard‑gate future attempts.

