# v44 NEXT BUILD PLAN DIFF — post‑Batch‑15

**Date:** 2026-01-30  
**Scope:** v43 → v44 (post‑Batch‑15).  
**Theme:** Replace phase‑losing UE interface by **signed k=2 coefficient interface**; keep Weil/Li as harness only.

---

## 1) Promote UE‑INPUT(k=2) (single active box)

### Remove / archive (v43)
- `box:ue-input-v43` (L1/H¹ bound on \(\int|\mathcal D|\)) becomes *non‑active*:
  - Keep as a remark: “stronger than necessary; loses phase; likely RH‑strength”.

### Add (v44)
- New box `box:ue-input-k2-v44`:
  \[
  \Big|\int_0^{2\pi}\Im(\mathcal D_{a,h}(v(\theta)))e^{-2i\theta}d\theta\Big|
  \le C h(\log(m+3))^{C'}/a^2.
  \]
- Explicit exponent budget note: target \(C'<4\).

---

## 2) Replace UE‑REDUCE lemma by an exact identity

### Replace
- `lem:geo-c4-ue-reduction` (triangle inequality via \(\int|\mathcal D|\))

### With
- `lem:geo-c4-P2-coefficient-identity`:
  \[
  \|P_2\psi\|_{L^2}=\frac1{\sqrt\pi}\Big|\int_0^{2\pi}\psi(\theta)e^{-2i\theta}d\theta\Big|
  \quad\Rightarrow\quad
  \Phi^\star=\frac{\delta^2}{h\sqrt\pi}\Big|\int \psi e^{-2i\theta}\Big|.
  \]
- Corollary: UE‑INPUT(k=2) ⇒ \(\Phi^\star\ll \delta^2(\log m)^{C'}/a^2\).

---

## 3) Add “UE playbook” appendix (one page)

Appendix should include:
1) Definitions: \(E,\mathcal L_t,\mathcal D_{a,h}, v(\theta),\psi,P_2,\Phi^\star\).
2) Target inequality: UE‑INPUT(k=2).
3) Decomposition: \(E'/E = (\zeta'/\zeta)+(\Gamma'/\Gamma)+\text{const}\) (in your chosen frame).
4) Candidate routes:
   - Hardy/Carleson bounds for a k=2 boundary pairing,
   - explicit kernel sum over zeros and exponent‑budget bookkeeping,
   - Weil/Li harness conditions (non‑essential).

---

## 4) Weil/Li bridge: downgrade to harness

- Keep a short section “Weil/Li compatibility”:
  - state criterion and the contrapositive existence of a negativity witness \(g\),
  - explicitly mark **no identification lemma is proved**,
  - write a “Bridge Lemma target” (what would be needed later).

---

## 5) Reader‑guide Part III: add interpretive remark

- Add a remark after GEO‑C4 definition:
  - “k=2 carrier on hinge circle corresponds to π/2‑carrier/mod‑4 projector in the lane calculus.”
  - Not load‑bearing; purely explanatory.

---

## 6) Sanity checks for v44 build

1) Ensure only **one** UE box is marked “single active”.
2) Ensure the forcing lower bound still targets the same \(\Phi^\star\).
3) Ensure δ‑policy and admissibility hypotheses are unchanged.
4) Ensure all new TeX blocks compile.

