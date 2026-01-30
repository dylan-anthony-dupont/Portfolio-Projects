# CR Master Dashboard — v44 Pre‑Build (Pre‑Batch‑15)

**Canonical posture:** v43 locked; v44 aims to sharpen/close UE via explicit‑formula and (optional) Weil/Li harness.

## 1) Status board (gaps)

### Locked / CLOSED
- GEO‑C4 geometry (hinge circle; k=2 harmonic endpoint).
- FORCE chain: off‑axis quartet forces Φ⋆ ≥ c₀(κ).
- UE‑REDUCE lemma: Φ⋆ ≤ (const)·(δ²/h)∫|ᵀ_{a,h}(v(θ))|dθ.
- Hygiene: ENT, shift‑admissibility/buffering, coupling h=κδ.

### OPEN (single active)
- **UE‑INPUT(v43)**: ∫₀^{2π} |ᵀ_{a,h}(v(θ))| dθ ≤ C h (log(m+3))^{C'} / a^2.

### Exploratory / Harness (not yet active)
- **WEIL/Li bridge harness:** attempt to identify GEO‑C4 channel as a Weil functional / Li coefficient combination.
- **Signed channel interface (UE‑k2):** bound | ∫ ᵀ_{a,h}(v(θ)) e^{-2 iθ} dθ |.

## 2) Blocker queue (ranked)
1. **B1 (Primary):** Prove (or NO‑GO) UE‑INPUT(v43) in an RH‑free manner.
2. **B2 (Bridge Lemma):** Express k=2 channel as an explicit sum over zeros and test if it matches a Weil kernel family.
3. **B3 (Phase retention):** Determine if the absolute‑value L1 UE interface is too lossy for a Weil/Li route; if yes, propose a replacement interface with a proof‑grade reduction.

## 3) Dependency DAG (minimal)

Off‑axis quartet at (a,m)
  → FORCE: Φ⋆ ≥ c₀(κ)
  → (need) UE‑INPUT: ∫|ᵀ| ≤ C h (log)^C'/a^2
  → UE‑REDUCE: Φ⋆ ≤ const · (δ^2/h) ∫|ᵀ|
  → contradiction for large m (and/or small η)
  → no off‑axis quartets → RH.

Optional harness:
  k=2 channel ↔ (candidate) Weil functional / Li coefficients 
  → may replace UE‑INPUT with a signed/quadratic positivity or boundedness statement.

## 4) Batch‑15 work orders (what we need back)
- ENVELOPE: prove or NO‑GO UE‑INPUT(v43) with explicit decomposition + constants.
- LOCAL: isolate near‑trace contributions to ∫|ᵀ|; determine unavoidable lower bounds under off‑axis and what that implies.
- BRIDGE: produce clean coefficient identities + any Hardy/Carleson tools usable on hinge circles.
- ABSORB: quantifier discipline (δ shrink, buffering) and what monotonicity is legitimate.
- FORCE: “clutter robustness” and any lower bound on ∫|ᵀ| under quartet hypothesis (for NO‑GO classification).
- LEGACY: translate k=2 harmonic extraction into π/2‑carrier / mod‑4 projector language and identify candidate Weil/Li kernels.
