# CR Master Dashboard — v43 Pre-build (post Batch 13)
Date: 2026-01-30

## Executive state
- **Current locked manuscript:** v42 (post-build)
- **Next target:** v43 (pre-build post Batch 13)
- **Only active closure lever:** **UE‑INPUTᴴ¹(D)** (new optimized UE interface; see Integration Notes)

## R1 vs R2 decision
- **R1 (keep v42 UE‑INPUT):** NO‑GO as active interface (RH-strength; over-specified).
- **R2 (replace with channel-compatible UE):** **SELECTED**.

---

## The one-page dependency DAG
**Assume** an off-axis quartet exists at height `m` with tilt `a>0`.

1. **FORCE (LOCKED):** `Φ⋆(m,a,δ,h) ≥ c₀(κ)` for hinge circle + k=2 projection.
2. **UE‑INPUTᴴ¹(D) (OPEN / ACTIVE):** `∫ |𝒟_{a,h}(v(θ))| dθ ≤ C h (log(m+3))^{C'} / a²`.
3. **UE reduction (PATCH):** `Φ⋆ ≤ (δ²/(h√π)) ∫ |𝒟|`.
4. **Contradiction:** choose `δ≤η a/log² m` so upper bound `< c₀(κ)`.

Therefore: no off-axis quartet; RH follows.

---

## Workstream status table (v43 pre-build)
| Workstream | Item | Status | Owner | Notes |
|---|---|---:|---|---|
| FORCE | GEO‑C4 forcing constant & stability | LOCKED | CR1 | Keep as in v42; optional remainder interface later |
| LOCAL | Shift/buffer admissibility definition | LOCKED | CR1 | But update quantifiers: only 4 traces needed for `𝒟`-UE |
| BRIDGE | UE reduction lemma (endpoint → boundary norm) | **PATCH** | CR1 | Replace IBP lemma with one-line `L¹` bridge |
| ENVELOPE | Baseline RH‑free bound (explains why v42 stalled) | ADD (EXPO) | CR1 | Include as “baseline too weak” lemma |
| UE‑INPUT | v42 box (sup_θ, v‑derivatives) | DEMOTE | CR1 | Move to appendix; precede with NO‑GO lemma |
| UE‑INPUT | **New active box:** UE‑INPUTᴴ¹(D) | **OPEN** | CR1 | Single active statement for closure |

---

## Patch queue (high-level)
1. Add NO‑GO lemma: “pointwise UE‑INPUT is RH-strength / δ^{-2} blow-up under quartet”.
2. Replace `Box ue-input-v42` with `UE‑INPUTᴴ¹(D)` as the active box.
3. Replace Lemma `lem:geo-c4-ue-reduction` with the `L¹` bridge lemma.
4. (Optional) Add baseline lemma (RH-free) to show what is provable and why it’s insufficient.

---

## Stop conditions (for convergence discipline)
- If UE‑INPUTᴴ¹(D) cannot be reduced to *one clean analytic sub-claim* (e.g. a controllable zero-sum + archimedean term bound), we pause and re-factor.
- Otherwise: all further prompts/builds must target only **UE‑INPUTᴴ¹(D)**.

