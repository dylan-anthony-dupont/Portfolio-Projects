# v40 Patchlog

Build date: 2026-01-28  
Base: `manuscript_v39.tex` → `manuscript_v40.tex`

## Executive summary

v40 is an **architecture convergence build** whose purpose is to (i) **close drift** by formally retiring the v39-centered defect endpoint route (S5$^{\rm def}$), and (ii) **reframe the single open analytic frontier** as one boxed statement:

> **Missing Lever (ML-Δa):** a δ-aware, resonance-robust **non‑pointwise** endpoint redesign via a *two‑sided shift‑difference* functional.

This reframing is based on Batch‑10 consensus and the two legacy “Master Prompt” responses: the centered defect endpoint cannot be forced (π/2 forcing does not transfer), and any attempt to salvage it is blocked by explicit NO‑GO latches. v40 therefore installs the ML‑Δa endpoint family as the sole active closure target.

## Manuscript changes (v39 → v40)

### 1) S5 frontier reframed to **S5(Δa)**

- Renamed the S5 frontier section to emphasize the two‑sided shift‑difference redesign.
- Inserted definitions:
  - `def:two-sided-shift-diff` for **D_{a,h}(v) = L_{a+h}(v) − L_{a-h}(v)**
  - `def:two-sided-endpoint` for the **two‑sided phase endpoint** Φ^{(2s)}_B(a;h), with nominal coupling h=δ and δ=η a/(log m)^2.

### 2) New NO‑GO latches that “pin” the old S5^{def} route

Inserted the following proof‑grade barriers (truth‑latching):

- `lem:ML1-samebox-nogo` — **No δ‑uniform transfer** from aligned forcing to the centered defect endpoint at the *same* δ.
- `lem:defect-p-ceiling` — **Side‑length ceiling**: any bound derived from δ‑uniform pointwise control of |L_a| can have **at most δ¹** gain.
- `lem:defectbox-nogo-ML1` — **Defect‑box pole winding** forces Φ^{def} ≥ π/2, so defect‑endpoint δ‑gain claims cannot hold uniformly.

### 3) Resonance bookkeeping upgraded to be δ‑aware (archived benchmark)

- Added `def:resonance-sum-delta` and `def:near-resonance-count` plus remarks clarifying why the earlier δ‑blind resonance sum cannot police near-resonance at the nominal δ‑scale.

### 4) Missing Lever box replaced

- Replaced Box `box:missing-lever-v39` with **Box `box:missing-lever-v40`**, which now states ML‑Δa as the single open statement:
  - forcing lower bound,
  - δ‑uniform UE upper bound passing the exponent-budget gate,
  - resonance robustness.
- Archived S5^{def} as a benchmark-only route (explicitly demoted in-text and in the Discarded Routes appendix).

### 5) S6 harness cross‑check updated

- Added an S6 paragraph explaining how ML‑Δa is a **tilt‑sensitivity / amplitude‑leak detector** in explicit‑formula language.

### 6) Reproducibility pack bumped to v40

- Copied the v39 harness pack → `v40_repro_pack.zip`.
- Updated file names to the `v40_...` convention and updated `README.md` + `SHA256SUMS.txt`.

## Net effect on the proof frontier

- **What is now closed / pinned**: any attempt to obtain closure by transferring aligned-box forcing to a centered defect endpoint at the same δ; and any hope of gaining δ^p with p>1 from pointwise bounds on |L_a|.
- **What is now the only active frontier**: ML‑Δa on Φ^{(2s)}.

## Next build pointer (v41)

The v41 workplan is now unambiguous: prove the three ML‑Δa bullets (forcing / UE / resonance robustness) at the nominal coupling, and show the UE passes the exponent-budget gate.
