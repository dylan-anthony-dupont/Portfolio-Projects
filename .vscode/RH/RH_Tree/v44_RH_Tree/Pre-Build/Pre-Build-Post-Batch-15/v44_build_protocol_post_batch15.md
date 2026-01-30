# v44 BUILD PROTOCOL — post‑Batch‑15 (pre‑post‑build)

**Date:** 2026-01-30  
**Objective:** produce the v44 post‑build manuscript by integrating the Batch‑15 interface upgrade:
- UE layer becomes **signed k=2 coefficient** (single active box),
- UE‑REDUCE becomes an **identity** (no L1/phase loss),
- Weil/Li is retained as a **harness**, not a dependency.

---

## Step 1 — Freeze what is locked
Do **not** change:
1) GEO‑C1 hinge‑circle witness definition,  
2) coupling policy \(h=\kappa\delta\),  
3) forcing lemma statements/proofs,  
4) δ‑policy statement and admissibility definitions.

---

## Step 2 — Apply patch queue in order (P0 → P6)

### P0–P2 (mandatory, structural)
- Replace old UE‑INPUT(v43) box by **UE‑INPUT(k=2)** (v44).
- Insert Lemma `lem:P2-coefficient-identity`.
- Remove/disable the old `lem:geo-c4-ue-reduction` L1 bound as the *primary* UE reduction.

### P3 (mandatory, clarity)
- Keep the old L1 interface only as an archived remark/NO‑GO note.

### P4 (mandatory, navigation)
- Add the one‑page UE playbook appendix.

### P5–P6 (optional but recommended)
- Add Weil/Li harness note (explicitly non‑essential).
- Add the reader‑guide Part III interpretive remark.

---

## Step 3 — Compile + internal consistency checks

1) **Single‑active check:** confirm only one UE box is marked “single active” in the narrative.
2) **Chain check:** FORCE lower bound targets the same \(\Phi^\star\) used in UE‑INPUT(k=2).
3) **Dimension check:** make sure the normalization \(\delta^2/h\) is unchanged.
4) **Exponent‑budget check:** confirm the UE implication yields \((\log m)^{C'-4}\) (not worse).
5) **Admissibility check:** shift‑admissibility hypotheses are stated exactly once and used consistently.

---

## Step 4 — Patchlog + dashboard updates
After changes:
- update patchlog with “UE interface upgrade (k=2)” entries,
- update CR dashboard to reflect: UE‑INPUT(k=2) is the single open box.

---

## Step 5 — Repro pack
If your workflow packages a repro zip:
- include updated `.tex`, any new appendix figures, and updated md artifacts,
- re‑run compilation once from clean directory.

---

## Acceptance criteria for v44 post‑build
A v44 post‑build is acceptable if:

1) The manuscript’s frontier is unambiguous: **UE‑INPUT(k=2)** is the only active statement.
2) The UE chain is endpoint‑native (no L1 detours).
3) The Weil/Li discussion is clearly labeled as harness/future route (no dependency leaks).

