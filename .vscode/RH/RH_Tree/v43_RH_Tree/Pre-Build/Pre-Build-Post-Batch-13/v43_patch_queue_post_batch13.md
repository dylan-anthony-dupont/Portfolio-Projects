# v43 Patch Queue (post Batch 13 → v43 pre-build)
Date: 2026-01-30

> Goal: implement the **UE interface refactor** with minimal disturbance to locked machinery.

## P0 — Must land (closure-critical)
### P0.1 Insert NO‑GO lemma: “pointwise UE‑INPUT is RH-strength”
- **Where:** right before the UE box (currently `§12.2.5`).
- **Content:** local factorization near `ρ=a+im` implies `∂_t 𝓛_t(v(θ))|_{t=a} = -2 e^{-2iθ}/δ² + O(1/a²+1/m²+...)`.
- **Purpose:** formal justification for replacing v42 UE‑INPUT.

### P0.2 Replace active UE box
- **Replace:** `Box ue-input-v42`.
- **With:** `Box ue-input-v43` (name: `UE‑INPUTᴴ¹(D)`).
- **Quantifiers:** allow `δ≤δ₀` (nominal) to enforce admissibility; require only **four** shift traces (since we bound `𝒟_{a,h}` directly).

### P0.3 Replace UE reduction lemma
- **Replace:** `lem:geo-c4-ue-reduction`.
- **With:** `lem:geo-c4-ue-reduction-L1`:
  `Φ⋆ ≤ (δ²/(h√π)) ∫ |𝒟|`.
- **Dependencies:** none beyond `|P₂f|_{L²} ≤ (1/√π)||f||_{L¹}`.

## P1 — Strongly recommended (clarity + audit)
### P1.1 Archive old UE‑INPUT as “stronger sufficient criterion”
- Move v42 UE‑INPUT to an appendix or “discarded/over-strong interface” subsection.
- Cross-reference NO‑GO lemma.

### P1.2 Add baseline “RH-free but too weak” lemma
- Use ENVELOPE-derived baseline:
  `|∂_t ∂_v^j 𝓛_t| ≲ (log m)/(buf·δ)^{2+j}`.
- Include a one-paragraph explanation why it does **not** close against forcing under δ-policy.

## P2 — Optional (future tightening)
### P2.1 Force remainder interface
- Add explicit statement: forcing constant survives analytic remainder if shift-traces are buffered.
- Not required for v43, but could increase slack.

### P2.2 Resonance paragraph (monotone-safe under δ-shrink)
- Short lemma: if δ is reduced to maintain admissibility, UE bound becomes easier (RHS shrinks with h∼δ).

