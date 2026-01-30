# v43 Patchlog

**Date:** 2026-01-30  
**Base:** `manuscript_v42.tex` → **Target:** `manuscript_v43.tex`

## Executive summary
v43 is a convergence/closure refactor: it **removes the over-strong UE-INPUT (v42)** and replaces the UE interface with the **minimal boundary \(H^1\)/\(L^1\)** control that the GEO–C4 endpoint actually needs.

No other manuscript machinery is modified.

---

## Applied patches (from v43_patch_queue_post_batch14)

### P0.1 — GEO–C4 closure schema box rewrite
- Replaced the “OPEN-GEO closure schema” box with **`box:geo-c4-v43`**.
- The box now explicitly displays:
  - FORCE (toy + stability),
  - UE-REDUCE (deterministic lemma),
  - the single remaining UE-INPUT requirement (`box:ue-input-v43`),
  - and the exponent-budget implication \(\Phi^\star\ll \eta^2(\log m)^{C'-4}\).

### P0.2 — Replace UE reduction lemma
- Removed the derivative-field lemma (sup-in-θ + v-derivative stack).
- Inserted **Lemma `lem:geo-c4-ue-reduction`**:
  \[
  \Phi^\star(m,a,\delta,h)\ \le\ rac{\delta^2}{\sqrt\pi\,h}\int_0^{2\pi}ig|\mathcal D_{a,h}(v(	heta))ig|\,d	heta.
  \]
- Proof uses only the geometry of the \(k=2\) channel and the unit-vector inequality
  \(\sqrt{A_c^2+A_s^2}\le \int|\psi|\).

### P0.3 — Replace UE-INPUT box
- Replaced the v42 pointwise field-derivative box with the **single \(L^1\) boundary control** statement:
  \[
  \int_0^{2\pi}ig|\mathcal D_{a,h}(v(	heta))ig|\,d	heta
  \ \le\ C\,h\,rac{(\log(m+3))^{C'}}{a^{2}}.
  \]
- Labeled as **`box:ue-input-v43`** and treated as the single active open frontier.

### P1.1 — NO-GO / diagnostic lemma
- Added **Lemma `lem:geo-c4-l1-blowup`** (toy model):
  \[
  \int_0^{2\pi}ig|\mathcal D^{\mathrm{sing}}_{a,h}(v(	heta))ig|\,d	heta
  \ \ge\ rac{8\pi}{1+\kappa^2}\,rac{h}{\delta^2},
  \]
  emphasizing that any δ-uniform \(L^1\) bound of UE-INPUT type excludes off-axis quartets.

### Build hygiene
- Updated version strings and compilation stamp to **v43 / 2026-01-30**.
- Added `\label{app:repro}` to the reproducibility appendix to resolve the front-matter reference.
- Copied `v42_repro_pack.zip` contents into `v43_repro_pack/` and updated the README title to v43.

---

## Outputs produced
- `manuscript_v43.tex`
- `manuscript_v43.pdf`
- `integration_notes_v43.md`
- `v43_patchlog.md`
- `v43_repro_pack.zip` (see repro appendix + README)

