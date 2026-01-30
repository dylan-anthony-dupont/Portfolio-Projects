# v43 — Pre-build (post Batch 13) — Integration Notes
Date: 2026-01-30 (Europe/London)

## 0. Mission snapshot
**Locked:** v42 geometry + GEO‑C4 endpoint/forcing architecture.  
**Objective of this ingestion:** decide **R1 vs R2** for the only active closure interface (UE‑INPUT), then publish a single, optimized, truth‑latched UE statement with a clean dependency map for the v43 build.

**R1:** keep `Box ue-input-v42` as-is (pointwise / sup-in-θ, plus v-derivatives).  
**R2:** replace it with the *minimum* non-pointwise, channel-compatible UE interface actually needed to bound the GEO‑C4 harmonic endpoint.

---

## 1. Canonical decision (R1 vs R2)
### Decision: **R2 (hybrid, but with one active box).**
We **retire** the current v42 UE‑INPUT box as the active claim (it is *RH-strength* and strictly stronger than needed), and we **replace it** with a single **channel-compatible** UE interface:

> **UE‑INPUTᴴ¹(D)**: an `H^1` / boundary-`L^1` control of the double-shift difference field `𝒟_{a,h}` on the hinge circle.

We keep the old UE‑INPUT box only as a *“stronger-than-necessary (archived)”* criterion, preceded by an explicit **NO‑GO lemma** explaining why it is not the right active interface for the GEO‑C4 program.

**Why this is the convergent move:** every branch converged on the same diagnosis—pointwise derivative control is over-specified, fights the hinge geometry, and is not the minimal closure lever. The bridge branch gives the cleanest replacement that closes the endpoint with the fewest moving parts.

---

## 2. Truth‑latched observations from Batch 13 (PASS/FAIL + conflict resolution)

### 2.1 What is now locked as “fact” inside the manuscript narrative

**(F‑1) The GEO‑C4 endpoint is a *harmonic channel* (k=2) on a hinge‑centred trig contour.**  
So UE must be expressed in **channel norms** (L²/H¹) rather than pointwise maxima.

**(F‑2) v42 UE‑INPUT (sup_θ + v-derivatives) is RH‑strength.**  
A single off-axis quartet creates a `δ^{-2}` blow-up in `∂_t 𝓛_t` on the hinge circle at `t=a`.  
So requiring a δ-uniform pointwise bound is essentially **the closure itself in disguise**, not an auxiliary estimate.

**(F‑3) Baseline unconditional bounds exist, but are too weak to close.**  
From generic Hadamard/zero-density control: `|∂_t ∂_v^j 𝓛_t| ≲ (log m)/(buf·δ)^{2+j}` on admissible traces.  
This explains *why* v42 could not close UE‑INPUT; it also clarifies what exponent-gain GEO‑C4 is designed to buy.

**(F‑4) Quantifier hygiene matters (avoid “corridor” assumptions unless we really need them).**  
If the UE interface depends on `t∈[a-h,a+h]`, then “corridor admissibility” becomes an extra hidden hypothesis.  
A `𝒟`-based UE input uses only `t=a±h` and therefore needs only **four shift traces**.

**(F‑5) Resonance is not best handled pointwise.**  
Near-resonant quartets can produce spikes on small arcs, but **L²/H¹** control remains stable under δ-shrink provided we do not demand pointwise uniformity.

### 2.2 Branch verdicts
- **RH‑FORCE‑13:** **PASS** (correctly classifies UE‑INPUT as RH‑strength; recommends demotion + channel UE).  
- **RH‑BRIDGE‑13:** **PASS** (gives the cleanest minimal replacement: `H¹` bound on `𝒟` and a one-line UE reduction).  
- **RH‑ENVELOPE:** **PASS** (extracts the baseline bound and explains why it cannot close; aligns with replacement strategy).  
- **RH‑LOCAL‑13:** **PASS (conditional)** (useful about pair-isolation/buffer policy; but “corridor” assumptions should be avoided unless essential).  
- **RH‑ABSORB‑13:** **PASS** (quantifier and interface hygiene; recommends `𝒟`-based UE to avoid hidden corridor dependence).

---

## 3. The optimized single active closure statement (TeX-ready)

### 3.1 Definitions (already locked in v42, restated only where needed)
- Hinge circle: `v(θ)=im+δ e^{iθ}`, `θ∈[0,2π]`.
- Log-derivative difference:
  `𝓛_t(v) := E'/E(v+t) − E'/E(v−t)`.
- Double-shift difference:
  `𝒟_{a,h}(v) := 𝓛_{a+h}(v) − 𝓛_{a−h}(v)`.
- GEO‑C4 endpoint (k=2 harmonic channel):
  `Φ⋆(m,a,δ,h) := (δ²/h) ⋅ ||P₂(Im 𝒟_{a,h}(v(θ)))||_{L²_θ}`  
  (exact constants as in v42, unchanged).

### 3.2 Active box to replace `Box ue-input-v42`
> **UE‑INPUTᴴ¹(D) — v43 (single active statement).**  
> Fix `κ∈(0,1)` and set `h:=κδ`. Let `E` be the completed even entire object in the v-plane.  
> For all sufficiently large `m` and all `a∈(0,1)`, set the nominal scale  
> `δ₀ := η a/(log(m+3))²` and allow any `δ∈(0,δ₀]` needed to enforce buffer-admissibility of the four shift traces  
> `v(θ) ± (a±h)`.  
> Then there exist constants `C,C'>0` such that for every admissible `(m,a,δ,h)`:
> 
> `∫₀^{2π} |𝒟_{a,h}(v(θ))| dθ  ≤  C · h · (log(m+3))^{C'} / a².`

### 3.3 UE reduction (one-line bridge lemma)
From the endpoint definition and `||P₂f||_{L²} ≤ (1/√π) ||f||_{L¹}`:
`Φ⋆(m,a,δ,h) ≤ (δ²/(h√π)) ∫₀^{2π} |𝒟_{a,h}(v(θ))| dθ.`
So UE‑INPUTᴴ¹(D) implies:
`Φ⋆(m,a,δ,h) ≤ (C/√π) (δ/a)² (log(m+3))^{C'}.`

Under `δ≤δ₀=η a/(log(m+3))²`, this yields:
`Φ⋆ ≤ (C/√π) η² (log(m+3))^{C'−4}.`
This is `o(1)` if `C'<4`, and is uniformly `O(η²)` if `C'=4`.

---

## 4. Dependency map (truth‑latched DAG)
Everything in v42 stays locked except the UE box. The closure chain is now:

1. **(FORCE, locked):**  
   If an off-axis quartet exists at height `m` with tilt `a>0`, then (under admissibility/isolation)  
   `Φ⋆(m,a,δ,h) ≥ c₀(κ) > 0` (δ-independent forcing constant).

2. **(UE‑INPUTᴴ¹(D), single active):**  
   `∫ |𝒟_{a,h}(v(θ))| dθ ≤ C h (log m)^{C'}/a²` for `δ≤η a/log² m`.

3. **(UE reduction, immediate):**  
   UE‑INPUTᴴ¹(D) ⇒ `Φ⋆(m,a,δ,h) ≤ (C/√π) η² (log m)^{C'−4}`.

4. **(Contradiction):**  
   For large `m` (and/or small enough `η`), the upper bound is `< c₀(κ)`, contradicting forcing.  
   Therefore no off-axis quartet exists at that height. Since `m` was arbitrary, RH follows.

**Single point of failure / single active box:** step (2).

---

## 5. Patch map for v43 (what changes vs v42)

### 5.1 Add a NO‑GO lemma (expository truth latch)
Insert a lemma immediately before the UE‑INPUT box:

- Show local factorization implies  
  `∂_t 𝓛_t(v(θ))|_{t=a} = -2 e^{-2iθ}/δ² + O(1/a²+1/m²+...)`, hence `sup_θ |∂_t 𝓛_t| ≳ δ^{-2}` under an off-axis quartet.
- Conclude: the v42 UE‑INPUT box is RH-strength and stronger than necessary for GEO‑C4.

### 5.2 Replace `Box ue-input-v42` with `UE‑INPUTᴴ¹(D)`
- Remove the sup_θ / v-derivative formulation as the **active** box.
- Move it to an appendix or “stronger sufficient criterion” subsection (optional).

### 5.3 Replace Lemma `lem:geo-c4-ue-reduction`
Swap the current integration-by-parts lemma for the one-line bridge bound:
`Φ⋆ ≤ (δ²/(h√π)) ∫ |𝒟|`.

### 5.4 (Optional) Keep the integration-by-parts route as a *secondary* refinement
If later we can prove v-derivative bounds, we can regain an extra `δ` power, but this is not required for the main closure chain.

---

## 6. What is now the precise “math work” to do (and only that)
To close v43 we must prove UE‑INPUTᴴ¹(D) for the true completed zeta object:

- Expand `E'/E` as (archimedean smooth term) + sum over zeros.
- Show the double-shift difference `𝒟_{a,h}` gains an `h` factor and an `a^{-2}` factor after circular averaging / H¹ norm.
- Control near-trace contributions using admissibility buffer + an effective local counting bound (at most `O(log m)` zeros in each fixed-width neighborhood), without assuming RH.

This is the sole remaining lever.

---

## 7. Sanity check vs v42 machinery
- GEO‑C4 geometry (hinge circle + k=2 harmonic) is unchanged.
- FORCE lemmas are unchanged.
- Only the UE interface and UE reduction lemma are altered, in a way that **reduces** complexity and eliminates corridor/pointwise assumptions.

**Net effect:** v43 is easier than v42 (fewer derivatives, fewer quantifiers, one active statement).
