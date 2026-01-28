# Integration Notes — v40 (post-build)

Build date: 2026-01-28  
Inputs: Batch‑10 ingestion + two legacy “Master Prompt” responses (initial + refined) + v39 baseline.

## 1) What we locked in as “truth-latching” in v40

### A. The decisive diagnosis: why v39 couldn’t close
- **Centered defect endpoint is not forceable.** The aligned-box forcing constant (π/2) does **not** transfer to the centered defect endpoint at the same δ-scale (formalized as `lem:ML1-samebox-nogo`).
- **Pointwise → endpoint UE has a hard δ¹ ceiling.** Any UE estimate derived only from δ-uniform pointwise control of |L_a| cannot produce δ^p with p>1 (formalized as `lem:defect-p-ceiling`).
- **Near-resonance can be δ-inert for Φ^{def}.** The δ-inert resonance obstruction remains valid for the defect endpoint class (retained as `lem:defect-resonance-nogo`).

### B. The reframing: Missing Lever = ML-Δa
We replaced the v39 “transfer + defect UE + resonance bookkeeping” triad by a single boxed open statement:

> **Missing Lever (ML‑Δa):** build a δ-aware, resonance-robust **non‑pointwise** endpoint redesign based on a two‑sided shift‑difference in the tilt parameter.

This is captured in Box `box:missing-lever-v40` and the new endpoint definitions:

- `def:two-sided-shift-diff` (D_{a,h} = L_{a+h} − L_{a-h})
- `def:two-sided-endpoint` (Φ^{(2s)}_B(a;h) with nominal h=δ and δ=η a/(log m)^2)

### C. Resonance bookkeeping upgraded (archived benchmark)
We installed δ-aware resonance tracking (Definitions `def:resonance-sum-delta`, `def:near-resonance-count`) to prevent any future return to δ-blind resonance summaries.

## 2) What changed in the manuscript

- S5 frontier renamed to emphasize S5(Δa) endpoint redesign.
- Missing Lever box replaced (v39 → v40).
- New NO‑GO lemmas inserted to permanently rule out centered transfer and “p>1” endpoint hopes for Φ^{def}.
- Discarded closure routes appendix updated to explicitly retire S5^{def} as a closure route.
- S6 harness appendix updated with an “explicit-formula amplitude leak” interpretation of ML‑Δa.

## 3) What is now the single active frontier (and what is demoted)

### Active frontier (only)
- **ML‑Δa on Φ^{(2s)}** (forcing / UE / resonance robustness).

### Demoted (archived)
- The centered defect endpoint class Φ^{def} as a load‑bearing closure device.
- Any transfer-style argument attempting to push aligned forcing into centered defect boxes at the same δ.

## 4) Repro pack status (v40)

- A v40 repro pack has been generated (`v40_repro_pack.zip`) by bumping the v39 harness pack to the v40 naming convention and updating metadata + SHA256 sums.
- The repro pack continues to certify the *finite-height front-end* and *m=10 tail check*.
- The ML‑Δa Missing Lever remains open and is tracked only in-text (Box `box:missing-lever-v40`).

## 5) What we need next (v41 pointer)

v41 should be laser-focused on proving the ML‑Δa package:

1) a clean forcing lower bound for Φ^{(2s)} on an admissible aligned box containing a quartet,
2) a δ-uniform UE upper bound that passes the exponent-budget gate,
3) a resonance-robustness lemma showing near-resonant quartets cannot invalidate (2) at nominal δ.

