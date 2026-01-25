# v37 patchlog (relative to v36)

**Build date:** 2026-01-25  
**Baseline:** `manuscript_v36.tex` → **Output:** `manuscript_v37.tex` / `manuscript_v37.pdf`  

This patchlog records proof-spine changes only (no prose-level diffs).

---

## 1) High-level intent (v37)
- v37 is an **S5′ architecture build**: it installs a phase/winding endpoint toolkit and a buffered phase forcing lemma.
- v37 makes **no claim** of uniform tail closure and **no claim** of RH.

---

## 2) Manuscript spine changes

### P37.0 Front-matter latch
- Abstract and Executive Proof Status updated to reflect: **S5′ phase endpoint toolkit installed; RH not claimed**.

### P37.1 Missing-lever box (OPEN)
- Inserted a boxed **OPEN (Missing Lever)** statement at the start of Section `sec:S5-frontier`.
- Explicitly lists the required deliverable class (forceable + δ-shrinkable + budget-eligible) and binding NO–GO reminders.

### P37.2 S5′ phase endpoint toolkit subsection
Inserted new subsection `subsec:S5prime-phase-toolkit` after `Remark rem:s5-forceability-gate`, adding:
- `Definition def:phase_increment` (phase increment as `Im ∫ (f'/f) dv` on a nonvanishing neighborhood).
- `Lemma lem:phase_increment_identity` (additivity + vertical specialization).
- `Remark rem:phase_parentheses_hygiene` (Im placement is non-negotiable).
- `Definition def:Iplus_lambda` + `Lemma lem:phase_split_Iplus_lambda` (shifted segment + phase split `E = F·Z_loc`).
- `Corollary cor:residual_phase_budget` (δ-uniform residual phase budget via existing residual-envelope lemma).
- `Lemma lem:local_phase_delta_inert` (per-zero phase contribution ≤ π) + `Corollary cor:prototype_phase_upper`.

### P37.3 Buffered phase endpoint + forcing lemma
Added:
- `Definition def:Db-tilde-phase` (buffered phase endpoint `\widetilde D_B(W)` on `∂B_{\kappa/2}`).
- `Lemma lem:phase-forcing-argprinciple` (if an interior zero exists then `\widetilde D_B(W) ≥ π/2`).
- `Remark rem:forceability-phase-gate` (forces explicit decision: rewrite tail in terms of `\widetilde D_B` or prove transfer to/from `D_B`).

### P37.4 S5′ closure criterion theorem (conditional)
Inserted (after `Theorem thm:S5-budget`):
- `Theorem thm:S5prime-closure` (budget closure criterion for a forceable phase endpoint; **assumptions only**).
- `Remark rem:S5prime-gate` (acceptance gate; `p=0` raw Δarg rejected; absolute-`L^r` endpoints rejected by existing NO–GO).

### P37.5 S6 harness appendix (interpretive only)
Inserted `Appendix app:S6-harness`:
- Maps v-displacement `a = 2β−1` to explicit-formula amplitude scaling `x^β`.
- Marked explicitly as **non-closure / interpretation harness** (no logical dependencies).

### P37.6 Version hygiene + repro appendix
- Updated appendix headings and file-path references from `v36_*` to `v37_*` and `v36_repro_pack/` to `v37_repro_pack/`.

---

## 3) Repro pack (v37) changes

### R37.1 Schema latch extension (fail-closed)
`v37_constants_m10.json` now additionally records:
- `endpoint_family` (string)
- `forcing_target` (string)
- `budget_tuple` (object: `p, theta, q`)
- `growth_model` (object; bookkeeping)
- `missing_lever_open = true`

Verifier now **fails closed** if any of these are missing, and explicitly checks:
- `missing_lever_open` is `true` in both constants and certificate.
- `budget_tuple` has keys `p, theta, q`.

### R37.2 Updated scripts + integrity hashes
- New scripts: `v37_generate_tail_check.py`, `v37_verify_tail_check.py`, `v37_verify_frontend_certificate.py`.
- `SHA256SUMS.txt` regenerated.

### R37.3 Expected result
- Tail harness at `m=10, α=1` remains **PASS: false** (expected for the legacy D1 pointwise endpoint class).
- Verifier output pinned in `v37_tail_check_verifier_output_m10.txt`.

---

## 4) Build checks
- `pdflatex` pass 1+2 succeeded (logs: `v37_pdflatex_pass1.log`, `v37_pdflatex_pass2.log`).
- `v37_verify_tail_check.py` succeeded (regen matches pinned certificate; meta latch enforced).
