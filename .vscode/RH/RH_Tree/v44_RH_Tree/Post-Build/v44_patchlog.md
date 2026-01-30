# v44 Patchlog

**Date:** 2026-01-30  
**Base:** `manuscript_v43.tex` → **Target:** `manuscript_v44.tex`

## Executive summary
v44 is a **UE-interface tightening** build. It keeps the GEO–C4 forcing machinery locked, but **replaces the remaining UE-INPUT (v43)** (an $L^1$ absolute-value bound) with a **signed $k=2$ coefficient interface** that preserves phase and is structurally compatible with explicit-formula / Weil-style bridges.

This is accompanied by a one-page **UE Playbook** appendix that isolates the attack surface and a **Weil/Li bridge scoping** appendix (non-load-bearing, future-facing).

---

## Applied patches (from v44_patch_queue_post_batch15)

### P0 — Version / label updates
- Updated version strings to **v44** and compilation stamp to **2026-01-30**.
- Promoted the active closure schema box to **`box:geo-c4-v44`**.
- Promoted the single active UE box to **`box:ue-input-v44`**.

### P1 — GEO–C4 closure schema box rewrite
- Rewrote the closure summary box to present the endpoint as a **single signed harmonic channel**:
  \[
  \Phi^\star=\frac{\delta^2}{h}\|P_2\psi\|_{L^2}
  =\frac{\delta^2}{h\sqrt\pi}\,|\widehat\psi(2)|.
  \]
- Updated the UE obligation pointer to the new coefficient bound (Box `box:ue-input-v44`).

### P2 — Replace UE reduction lemma (proof-grade)
- Removed the v43 deterministic $L^1$-based reduction lemma.
- Inserted **Lemma `lem:geo-c4-ue-reduction-k2`**:
  \[
  \|P_2\psi\|_{L^2_\theta}=\frac{|\widehat\psi(2)|}{\sqrt\pi},\qquad
  \Phi^\star=\frac{\delta^2}{h\sqrt\pi}|\widehat\psi(2)|.
  \]
- This makes UE control a **single signed Fourier coefficient** problem (no pointwise control, no absolute values).

### P3 — Replace UE-INPUT box with UE-INPUT($k=2$)
- Replaced the v43 $L^1$ boundary magnitude requirement with the **single signed coefficient bound**:
  \[
  |\widehat\psi(2)|\ \le\ C\,\frac{(\log(m+3))^{C'}}{a^2}\,h.
  \]
- This is explicitly the **only active open frontier** in v44.

### P4 — Add the “UE Playbook” and Weil/Li scoping appendices
- Added **Appendix `app:ue-playbook`** (“UE playbook”) that isolates:
  definitions → target inequality → standard decompositions → candidate analytic routes.
- Added **Appendix `app:weil-li-scope`** (“Weil/Li bridge scoping”), non-load-bearing for v44, recording:
  why the signed $k=2$ channel is structurally compatible with Weil/Li criteria and what remains to be proven for an actual identification.

### P5 — Repro pack bump
- Copied `v43_repro_pack.zip` contents into **`v44_repro_pack/`** and updated the README.
- Regenerated `SHA256SUMS.txt` inside the pack.
- Produced `v44_repro_pack.zip`.

---

## Outputs produced
- `manuscript_v44.tex`
- `manuscript_v44.pdf`
- `integration_notes_v44.md`
- `v44_patchlog.md`
- `v44_repro_pack.zip`
