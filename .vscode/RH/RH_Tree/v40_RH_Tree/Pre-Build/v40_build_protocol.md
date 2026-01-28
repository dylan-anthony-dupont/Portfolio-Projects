# v40 Build Protocol (pre-build) — from v39 + Batch 10 + legacy synthesis

**Date:** 2026-01-28  
**Integrator:** RH‑CR  
**Goal:** Produce a v40 manuscript that (i) locks in Batch 10 NO‑GO borders, and (ii) replaces the v39 Missing Lever triad with a single redesigned endpoint obligation ML‑Δa (two‑sided shift‑difference).

> Note: This is a *protocol* and does not assert closure. v40 is a “truth-latching convergence” build whose purpose is to make subsequent builds easier and less ambiguous.

---

## 0) Inputs (required)

- Base TeX: `manuscript_v39.tex`
- Patch queue: `v40_patch_queue_batch10.md`
- Integration notes: `integration_notes_batch10.md`
- Dashboard: `CR_master_dashboard_batch10.md`

---

## 1) Pre-flight checks (before editing)

1. Confirm v39 compiles cleanly (PDF generation).
2. Locate the S5′ frontier section and Box `box:missing-lever-v39`.
3. Confirm existing labels:
   - `def:defect-quotient`, `def:defect-endpoint`
   - `lem:defect-cancellation`, `lem:defect-resonance-nogo`
   - `thm:exponent-budget`
   - `box:missing-lever-v39`

---

## 2) Apply patch queue (ordered)

Apply patches in `v40_patch_queue_batch10.md` in sequence:

1. Patch 40.1–40.3: lock NG‑1 (no centered transfer) + update Missing Lever text.
2. Patch 40.4–40.6: lock NG‑2 (side-length ceiling) + remove “p>1” slogans + add δ-aware resonance sum definition.
3. Patch 40.7: lock δ-blindness diagnosis + add δ-aware near-resonance count.
4. Patch 40.8: lock NG‑4 (defect-box forcing cannot replace transfer).
5. Patch 40.9–40.12: introduce S5Δa endpoint definitions, replace Missing Lever box with ML‑Δa, and extend S6 harness mapping.
6. Patch 40.13 (optional but recommended): add discarded-route note for \(\Phi^E_B\) to prevent drift.

---

## 3) Consistency audits (must pass)

### A) “No drift” audit
- Confirm the manuscript now explicitly states NG‑1…NG‑5 somewhere stable (either S5 section or discarded routes appendix).
- Confirm **Boxed open statement count = 1** (only ML‑Δa).

### B) “Endpoint hygiene” audit
- Confirm the old defect endpoint \(\Phi^{\rm def}_B(a)\) is still defined but is explicitly demoted (or placed in discarded routes).
- Confirm the new endpoint \(\Phi^{(2s)}_B(a;h)\) is defined with:
  - max over sides,
  - buffered contour,
  - explicit coupling \(h=\delta\) (or stated coupling rule).

### C) “Gate Calculator” audit
- Confirm Theorem `thm:exponent-budget` is still the global gate.
- Confirm the manuscript no longer uses “\(p>1\)” as the load-bearing slogan.

### D) “S6 harness” audit
- Confirm the S6 section explicitly maps:
  - \(a \leftrightarrow \beta=\tfrac12+\tfrac a2\),
  - and interprets the new endpoint as a tilt/β finite-difference (amplitude-leak detector).

---

## 4) Compile + package

1. Compile v40 TeX → PDF.
2. Produce v40 patchlog relative to v39:
   - list which NO‑GO latches were added,
   - which box was replaced,
   - new definitions introduced.
3. Update reproduction pack with:
   - `manuscript_v40.tex`, `manuscript_v40.pdf`,
   - `v40_patchlog.md`,
   - `CR_master_dashboard_v40_locked.md` (post-build),
   - `integration_notes_v40.md` (post-build digest),
   - `v40_next_build_plan_diff.md` (for the next iteration).

---

## 5) Acceptance criteria (what “v40 done” means)

v40 is accepted if:

- The old v39 Missing Lever box is gone and replaced by ML‑Δa.
- NG‑1…NG‑5 are explicitly codified in-text.
- The manuscript has a single clear frontier pointer (ML‑Δa) with definitions in place.
- The S6 mapping is updated and consistent with the u→v scaling.

---

## 6) If compilation breaks

- Resolve label collisions by:
  - keeping existing v39 labels when possible, and
  - renaming only new labels (`def:two-sided-shift-diff`, `def:two-sided-endpoint`, `box:missing-lever-v40`) if required.
- Do not relax any NO‑GO latch language to “maybe”: these are truth-latching constraints.

