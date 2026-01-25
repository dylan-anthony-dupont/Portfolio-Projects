# CR Master Dashboard — v36 LOCKED (one page)

## Posture
- **Primary frontier:** **S5** (non-pointwise UE redesign) — *OPEN*
- **Audit harness:** S2 (certified tail check / finite height front-end) — *kept as scaffold*
- **Retired:** S1 tail-absorption closure as previously framed (pointwise UE)

## Ranked blockers (must-close order)
1. **S5 endpoint invention**: produce a forceable endpoint with `p−θ>0` and `2(p−θ)≥q` (Theorem `thm:S5-budget`).
2. **Forcing compatibility**: endpoint must dominate `D_B(W)` or come with a new forcing lemma (Remark `rem:s5-forceability-gate`).
3. **Local interface redesign**: must reduce θ below the endpoint’s p (current collar gives θ=1 pointwise; and θ(r)=1−1/r for absolute L^r).
4. **Bridge regularity / boundary meaning**: keep Bridge-1 directionality; no “boundary modulus ⇒ interior zero-free” (Remark `rem:no-converse`).

## Locked NO–GO constraints (v36 line-in-sand)
- **Pointwise/sup UE:** cannot achieve `p>1` (Lemma `lem:UE-scaling-nogo`).
- **Absolute L^r endpoints:** `p(r)=θ(r)=1−1/r` ⇒ δ-inert local term (Prop `prop:S5_Lp_nogo`).
- **Projection-killing-local endpoints:** cannot control forced `D_B(W)` without new forcing link (Lemma `lem:S5-projection-nogo`).

## Minimal S5 dependency DAG (current)
(Bridge-1 / outer factor) → (UE inequality: `D_B(W) ≤ δ^p Φ_B(E'/E)`)  
→ (split: residual + local) → (local endpoint bound: `Φ_B(Zloc'/Zloc) ≤ δ^{-θ} G(Nloc,κ)`)  
→ (S5 budget theorem: `2(p−θ) ≥ q`, `p−θ>0`)  
→ (tail inequality closure under δ₀ = ηα/(log m)²)  
↘ forcing: off-axis quartet ⇒ lower bound on **forced object** (currently `D_B(W)`)

## Gap board (compressed)
- **OPEN:** S5 endpoint redesign; new forcing link if endpoint ≠ `D_B(W)`; local-interface improvement.
- **CLOSED (guardrail-level):** exponent budget logic; pointwise UE scaling ceiling; absolute L^r endpoint NO–GO; projection endpoint NO–GO; repro-pack metadata latch.

