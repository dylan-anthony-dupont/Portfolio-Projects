# v43 Next Build Plan — Diff (post Batch 13 → v43 pre-build)
Date: 2026-01-30

## Summary: what changes vs v42
This plan implements the **R2 decision**: keep all GEO‑C4 geometry and forcing machinery **unchanged**, but **optimize** the UE interface to match the harmonic endpoint.

### A) Replace the active UE box
- **Remove as active:** `Box ue-input-v42` (sup_θ, j=0..2 v-derivatives).
- **Add as active:** `UE‑INPUTᴴ¹(D)` — boundary `L¹`/`H¹` control of `𝒟_{a,h}` on the hinge circle:
  `∫ |𝒟_{a,h}(v(θ))| dθ ≤ C h (log m)^{C'}/a²`.

### B) Add a NO‑GO lemma (expository truth latch)
Insert a lemma showing that under an off-axis quartet,
`∂_t 𝓛_t(v(θ))|_{t=a} = -2 e^{-2iθ}/δ² + O(1)`,
so any δ-uniform pointwise bound is RH-strength.  
This justifies the replacement and prevents “hidden RH” accusations.

### C) Replace UE reduction lemma (simplify)
- **Delete/Archive:** current integration-by-parts UE reduction requiring UE‑INPUT derivatives.
- **Insert:** one-line `L¹` bridge lemma:
  `Φ⋆ ≤ (δ²/(h√π)) ∫ |𝒟|`.

### D) (Optional) Add a baseline lemma (RH-free, but too weak)
Add the generic baseline estimate (from Hadamard/zero-density control)
`|∂_t ∂_v^j 𝓛_t| ≲ (log m)/(buf·δ)^{2+j}`
to explain why v42’s UE goal could not close and why GEO‑C4 needs channel extraction.

---

## Section-level patch targets (TeX navigation)
- `§12.2.5` UE box: replace contents.
- `§12.2.4` UE reduction lemma: replace lemma/proof.
- Insert NO‑GO lemma immediately preceding UE box (end of `§12.2.4` or start of `§12.2.5`).
- Update “Dependency Map / Single Active Statement” subsection accordingly.

---

## Regression tests
1. PDF compiles; numbering and labels updated.
2. GEO‑C4 forcing lemmas unchanged (only references updated).
3. The paper now has **exactly one active OPEN box**: `UE‑INPUTᴴ¹(D)`.

