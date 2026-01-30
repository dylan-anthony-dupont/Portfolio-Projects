# v43 build protocol — post Batch 14 (control-room procedure)

This protocol assumes v42 post-build is the locked baseline and that we apply only the v43 patch queue items.

---

## 0) Inputs to have open

- v42 manuscript source (TeX) and PDF (locked baseline).
- v43 patch queue (post Batch 14).
- v43 next build plan diff (post Batch 14).
- v43 CR dashboard + integration notes (post Batch 14).

---

## 1) Patch application order (strict)

1. **Apply P0.1 (Hygiene first).**  
   Add the GEO‑C4 “setup/admissibility” subsection *before* any lemma that integrates \(E'/E\).

2. **Apply P0.2 (UE reduction constants).**  
   Replace any older UE-reduction lemma with the BRIDGE lemma and ensure \(\sqrt\pi\) normalization is consistent with the definition of \(L^2([0,2\pi])\).

3. **Apply P0.3 (Active UE box swap).**  
   Remove the old UE‑INPUT box and insert UE‑INPUT\(^{{H^1}}(\mathcal D;M)\).  
   Ensure the box references the nominal policy \(\delta=\eta a/(\log(m+3))^2\) and coupling \(h=\kappa\delta\).

4. **Apply P1.1 (NO‑GO remark).**  
   Insert the “FORCE ⇒ \(\|\mathcal D\|_{L^1}\gtrsim h/\delta^2\)” remark right after FORCE.

5. (Optional) **Apply P1.2 (legacy translation remark).**

6. (Optional) **Apply P2.1 (FORCE stability under clutter)** if it can be stated cleanly with explicit separation hypotheses.

---

## 2) Consistency checks (must pass)

### 2.1 Hygiene checks
- Every contour integral of \(E'/E\) is preceded (directly or by reference) by shift‑admissibility.
- The coupling \(h=\kappa\delta\) is enforced globally (no stray “\(h\)” independent of \(\delta\) in GEO‑C4).

### 2.2 Closure chain checks
- FORCE statement implies \(\Phi^\star\ge c_0\) with the same \(\Phi^\star\) definition used in UE.
- UE reduction lemma is stated with the correct constant \(\delta^2/(\sqrt\pi h)\).
- UE‑INPUT\(^{{H^1}}(\mathcal D;M)\) is the *only* active/open box referenced in the contradiction.

### 2.3 No-Go archive checks
- Ensure the manuscript explicitly flags “δ⁻¹-type” UE bounds as insufficient.

---

## 3) Output artifacts to produce

- `manuscript_v43.tex`
- `manuscript_v43.pdf`
- `v43_patchlog.md` (record every patch queue item applied, with section anchors)
- `v43_repro_pack.zip` (source + build scripts, if present in baseline workflow)

---

## 4) Acceptance criteria (for “GO v43 build complete”)

A v43 build is accepted if:

1) The GEO‑C4 section reads linearly: setup → forcing → UE reduction → single active UE box → contradiction.  
2) There is exactly **one** open mathematical statement: UE‑INPUT\(^{{H^1}}(\mathcal D;M)\).  
3) All definitions and admissibility conditions are unambiguous and reusable.  
4) The build is objectively easier to audit than v42 (fewer moving parts, no derivative-stack UE).

