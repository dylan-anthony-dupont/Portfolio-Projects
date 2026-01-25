# v37 → next build plan (diff-only)

**Base:** v37 locked (2026-01-25)  
**Purpose:** identify the *minimal diffs* required for the next version to count as progress (no drift).

---

## 0) GO criteria for v38 (must move at least one blocker)
A next build counts as progress if it closes **any one** of:
- **G-2b:** forcing ↔ endpoint alignment for S5′ (`\widetilde D_B` rewrite or transfer to/from `D_B`),
- **G-4′:** phase-class UE/envelope inequality with `p ≥ 1/2` and δ-uniform constants,
- **G-8:** micro-window clustering / pair-isolation reducing effective local growth `q`.

---

## 1) Manuscript diffs (P38.*)

### P38.1 (FORCING/ENDPOINT ALIGNMENT)
Choose exactly one path and implement it end-to-end:

**Option A (preferred): rewrite tail to target `\widetilde D_B(W)`**
- Define the S5′ tail inequality explicitly in terms of `\widetilde D_B(W)` (replace `D_B` in the tail closure statement).
- Insert a lemma showing the tail bound for `\widetilde D_B(W)` follows from residual+local phase split on shifted segments / buffered contour.
- Connect forcing to tail directly via Lemma `lem:phase-forcing-argprinciple`.

**Option B (transfer): prove `\widetilde D_B(W) ≲ D_B(W)` or `D_B(W) ≲ \widetilde D_B(W)`**
- Add a transfer inequality on all κ-admissible boxes, with explicit constants.
- Update `Remark rem:forceability-phase-gate` to record which direction is proven.
- Update the S5′ closure theorem assumptions to use the proven transfer.

### P38.2 (PHASE-CLASS UE / ENVELOPE, p ≥ 1/2)
- Add a phase-class upper-envelope lemma (non-pointwise, not absolute-L^r) producing
  
- residual phase bound `O(δ log m)` (already present),
  
- local phase contribution with exponent `θ=0` *in the same endpoint class*,
  
- and an explicit exponent `p ≥ 1/2`.
- Codify δ-uniformity: quantifiers must be “for all 0<δ≤δ0(m,α)” with constants independent of δ.

### P38.3 (LOCAL MICRO-WINDOW)
Implement one decisive local improvement:
- **Micro-window clustering bound:** `N_micro(m,δ) = O(1)` at the nominal δ-scale, or
- **Pair isolation:** show only the forced pair contributes `O(1)` in the phase endpoint while the remaining cluster contributes `O(δ log m)`.

Update the exponent budget table accordingly (q reduced or effective q replaced by O(1)).

### P38.4 (BRIDGE-1: PHASE ENDPOINT COMPATIBILITY)
- Add a short compatibility lemma that:
  
- guarantees `G_out` and `W` are nonvanishing on neighborhoods of the *buffered contour* and *shifted segments* required by the phase toolkit,
  
- and explicitly ties this to κ-admissibility and collar policy (no “handwave analyticity”).

### P38.5 (OPEN box latch update)
- If and only if the missing lever is closed, flip the OPEN box to CLOSED and set `missing_lever_open = false` in the repro pack metadata.
- Otherwise the OPEN box stays OPEN.

---

## 2) Repro pack diffs (R38.*)
- Update `v*_constants_m10.json` fields:
  - `endpoint_family`, `forcing_target`, `budget_tuple`, `growth_model`, `missing_lever_open`.
- If a new phase endpoint is introduced as the forced object, add a **new pinned harness JSON** for that endpoint (even if it cannot yet close).

---

## 3) Optional harness (S6)
- If any new endpoint corresponds to an explicit-formula amplitude leak, add a 5–10 line statement in Appendix `app:S6-harness`:
  - map endpoint failure ⇒ existence of β>1/2 leak (or explicitly state why not).

