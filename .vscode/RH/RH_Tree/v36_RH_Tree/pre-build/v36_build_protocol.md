# v36 Build Protocol (post‑Batch‑5)

Date: 2026-01-24  
Baseline: **v35 locked** (2026-01-23)  
Purpose: build **v36** as a guardrail release: encode S5 acceptance gates + NO‑GO results so the program cannot drift.

---

## 0) Inputs required (files)

- `manuscript_v35.tex` (baseline)
- Batch‑5 patch packets:
  - `batch5_RH-ABSORB.md`
  - `batch5_RH-BRIDGE.md`
  - `batch5_RH-ENVELOPE.md`
  - `batch5_RH-FORCE.md`
  - `batch5_RH-LOCAL.md`
- Current CR artifacts:
  - `CR_master_dashboard_v35_locked.md`
  - `integration_notes_v35.md`

---

## 1) Build steps (deterministic)

1. **Copy baseline**  
   Duplicate v35 sources to `manuscript_v36.tex` (no content changes yet).

2. **Apply patch queue in order**  
   Apply P36.1 → P36.9 exactly (see `v36_patch_queue_batch5.md`).
   - If P36.7 is included, it must live in Appendix D6 and be explicitly tagged “supporting documentation for a NO‑GO route”.

3. **Cross‑reference and compile**  
   - Run LaTeX twice (resolve refs).  
   - Confirm: no label collisions; new labels appear only in Section 12 and Appendix A.

4. **No‑drift audit (mandatory checklist)**
   - v35 statements about forcing target \(D_B(W)\), exponent budget, and retired S1 route remain unchanged.  
   - v36 introduces **no new closure claims** (S5 is still OPEN; only acceptance/NO‑GO are added).  
   - All new theorems/lemmas quantify δ‑uniformly over:
     \(m\ge 10\), \(\alpha\in(0,1]\), and all κ‑admissible \(0<\delta\le \delta_0(m,\alpha)\).

5. **Update repro pack (schema‑only)**
   - Add “S5 endpoint metadata” fields.
   - Add fail‑closed validation rule: missing endpoint/exponent/forceability fields ⇒ certificate invalid.
   - No new computations; no new numeric certificates.

6. **Produce lock artifacts**
   - `manuscript_v36.pdf`  
   - `v36_repro_pack.zip` (schema update)
   - `v36_patchlog.md` (diff vs v35; list patch IDs and insert locations)
   - `integration_notes_v36.md` (one page)
   - `CR_master_dashboard_v36_locked.md` (one page)
   - `v36_next_build_plan_diff.md` (forward plan: cancellation endpoint search)

---

## 2) PASS/FAIL conditions for the v36 build

### PASS if all are true
- All P36.1–P36.5 and P36.8–P36.9 are present in the manuscript and consistent.
- The Appendix records D5/D6 as explicitly discarded.
- No new analytic claims of S5 closure appear.

### FAIL if any occur
- Any S5 endpoint class is implied viable without passing the acceptance criterion (missing explicit \(p,\theta,q\) and δ‑uniform constants).
- The manuscript suggests projection endpoints can close S5 without changing forcing.
- Any quantifier drift: δ‑dependence hidden in constants, or loss of “for all κ‑admissible δ≤δ0” scope.

---

## 3) After v36 lock: what Batch‑6 should target

S5 must now be pursued only in **cancellation / less‑singular** endpoint classes.
Batch‑6 prompts should therefore ask for:
- concrete cancellation endpoints \(\Phi_B\) that remain forceable (domination or new forcing lemma),
- explicit UE exponent \(p\),
- explicit local exponent \(	heta\) and growth model \(q\),
- and a residual envelope bound in the same endpoint class with proof‑grade constants.

