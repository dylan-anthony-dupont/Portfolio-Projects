# v41 Next Build Plan (Diff‑Only) — v40 → v41

Build target: **v41**  
Goal: lock the **geometry pivot** and prevent accidental self‑blocking via mis‑scoped NO‑GO latches.

---

## 0) Non‑negotiables carried from v40

- Do **not** revive S5^{def} “centered defect endpoint closure” attempts:
  - `lem:ML1-samebox-nogo` (no centered transfer at same δ),
  - `lem:defect-p-ceiling` (pointwise δ¹ ceiling),
  - `lem:defect-resonance-nogo` (δ‑inert resonance).
- Retain the Gate Calculator / exponent‑budget theorem as the master acceptance test.

---

## 1) What changed (post‑v40 audit)

The v40 ML‑Δa box requires forcing/UE/resonance on **aligned boxes** `B(±a,m,δ)` with nominal coupling `h=δ`. A proof‑grade computation in the toy even‑quartet model shows this **forcing clause is false**:

> On aligned boxes, `Φ^{(2s)}_{B(a,m,δ)}(a;h) ≤ C·δ h/a^2` (hence →0 at the nominal scale), so no absolute lower bound `c0>0` can hold.

Therefore v41 must:

1) insert the NO‑GO lemma (aligned‑box Δa forcing fails), and
2) replace the ML‑Δa box by a **Geometry Change Requirement** box that specifies the correct closure criteria.

---

## 2) v41 deliverables (must produce)

### D0. Hygiene fix (definition coherence)
- Verify the expansion of `D_{a,h}` matches `D_{a,h} := L_{a+h} − L_{a−h}`.
- If a sign/term mismatch exists, fix the displayed “equivalent form” so the manuscript is internally consistent.

### D1. New NO‑GO lemma (truth‑latching)
Insert:
- **`lem:deltaa-alignedbox-nogo`** (NG‑Δa‑A): aligned‑box forcing for `Φ^{(2s)}` is impossible at nominal coupling.

This lemma must:
- be stated in the manuscript’s own notation,
- give a clean proof (toy model suffices because ML‑Δa(1) purports to follow from structural hypotheses + symmetry),
- explicitly show the contradiction with Box `box:missing-lever-v40` bullet (1).

### D2. Replace the active frontier box
- Replace Box `box:missing-lever-v40` with:
  - **Box `box:geometry-change-v41`** (OPEN‑GEO): a single boxed open statement describing the *necessary* geometry/coupling redesign.

The new box must include:
1) **Geometry requirement:** specify a witness family `𝔅(a,m,δ,h)` (box family + buffering policy) not restricted to aligned boxes.
2) **Endpoint requirement:** specify the endpoint class to be used on `𝔅`.
3) **Coupling requirement:** specify the admissible coupling regimes (e.g. `h=δ`, `h≪δ`, or `h=δ^α`) that are allowed, with the key goal: forceability + gate‑passing UE on the same family.
4) **Resonance requirement:** δ‑aware resonance bookkeeping must be built into the statement.

### D3. Sanity check and scope‑tightening for existing NO‑GO latches
Add a short scoped remark (one paragraph) clarifying:
- which NO‑GO lemmas forbid only **pointwise‑in‑a** endpoints,
- which forbid only **δ‑gain** claims (and do not block δ‑inert harness uses),
- which do **not** preclude a geometry/coupling redesign.

### D4. Optional (toy‑model guide rails)
Add a short “toy‑model compass” remark that records:
- aligned boxes kill Δa forcing,
- but hinge‑centered geometry may produce O(1) side increments for Δa endpoints on buffered contours,
- therefore the frontier is **choosing geometry/coupling that makes forcing compatible with UE gain**, not merely locating another forcing constant.

---

## 3) Manuscript patch targets (where changes go)

- In Section `sec:S5-frontier`:
  - insert `lem:deltaa-alignedbox-nogo` immediately after Definitions `def:two-sided-shift-diff` / `def:two-sided-endpoint`,
  - replace Box `box:missing-lever-v40` with Box `box:geometry-change-v41`.
- In the Discarded Routes appendix:
  - add a brief “why ML‑Δa on aligned boxes fails” entry (so drift cannot revive it).

---

## 4) Repro pack

No new numerical certificates are required for v41, since v41 is a **proof‑spine correction** (not a constants update).
If any constant statements are edited, bump the text metadata and regenerate `SHA256SUMS.txt` only.
