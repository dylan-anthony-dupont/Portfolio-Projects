# v39 next build plan (diff‑only) — Batch‑9 → (v38 → v39)

**Date:** 2026-01-26  
**Baseline:** manuscript_v38.* (locked)  
**Target:** v39 PRE‑BUILD plan (do not claim closure; install defect tooling + NO‑GOs + Missing Lever reframe)

---

## A) Spine posture edits (front matter + roadmap)

1. Update “Frontier / Open” paragraph:
   - Replace “Missing Lever = recover δ^{3/2}” language with:
     **Missing Lever = S5^def defect‑kernel UE + resonance control + domination link to forced endpoint.**
2. Keep S6 harness paragraph mandatory:
   - Add explicit mapping: `s=\beta+i\gamma` ↔ `u=2s` ↔ `v=u-1` so `a=2\beta-1`, `m=2\gamma`.
   - State: `\beta>1/2` corresponds to explicit‑formula amplitude leak `x^{\beta}`.

---

## B) New definitions to insert (one coherent block)

Insert a new “Defect primitives” subsection near the S5′ Missing‑Lever box:

- `\mathcal Q_a(v):=E(v+a)/E(v-a)`  
- `\mathcal L_a(v):=\mathcal Q_a'/\mathcal Q_a = E'/E(v+a)-E'/E(v-a)`
- Defect phase endpoint on κ‑buffered contour:
  - `\Phi_B^{\rm def}(a):=\max_{\rm sides} \left|\Im\int_{\rm side} \mathcal L_a(v)\,dv\right|`
- Add “resonance tracker” definitions (choose one and stick to it in v39):
  - Option 1: resonance sum `R_a(m)` (ENVELOPE)  
  - Option 2: near‑count `N_{\rm near}(a,m,\delta)` (LOCAL)

---

## C) Lemma inserts (proof‑grade “truth‑latching”)

1. **Local cancellation lemma** (LOCAL):
   - `\mathcal Q_a` removable singularity at `v=i m` under symmetric pair, hence `\mathcal L_a` holomorphic there.
   - Pair contribution bound: `\left|\Im\int \mathcal L_a^{\rm pair}\right| \le 2r\,\delta/a`.
2. **Bridge/collar lemmas for shifted boxes** (BRIDGE):
   - κ‑admissibility for `\partial B_{\kappa/2}` implies κ‑admissibility for shifted contours used by `v\mapsto v\pm a`.
   - Difference‑kernel bound:
     `\mathcal L_a(v)=\sum_{\rho} \left(\frac{1}{v+a-\rho}-\frac{1}{v-a-\rho}\right)+\cdots`
     and the coarse estimate `\lesssim a/|v-\rho|^2` away from the tube.
3. **Defect UE skeleton lemma** (ENVELOPE):
   - `\Phi_B^{\rm def}(a) \le C\,\delta\log m + C\,\delta a\,R_a(m)`
   - Explicitly label as: “reduces Missing Lever to bounding `R_a(m)`.”
4. **Horizontal resonance NO‑GO lemma** (ENVELOPE):
   - Provide explicit two‑quartet near‑resonant construction showing δ‑inert behavior.
   - Conclude: any proof of δ‑shrinking UE must control/exclude near‑resonant quartets.

---

## D) Replace / rewrite the boxed “Missing Lever” statement

Replace v38 boxed Missing Lever with v39 boxed Missing Lever:

> **OPEN (Missing Lever, v39):**  
> To close RH via the phase‑class endpoint, it suffices to prove:  
> (i) Domination link `\widetilde D_B(W) \le C_{\rm dom}\,\Phi_B^{\rm def}(a)+\mathrm{Err}`;  
> (ii) Defect UE bound `\Phi_B^{\rm def}(a) \le C\,\delta\log m + C\,\delta a\,R_a(m)` with η‑independent constants;  
> (iii) Resonance control: bound `R_a(m)` (or `N_{\rm near}`) in the regime `0<\delta\le \delta_0(m,a)`.

Also include:
- One‑pole NO‑GO (carry forward).
- Resonance NO‑GO (new).

---

## E) Harness‑only (optional appendix, keep minimal)

- Include RH‑FORCE pole‑winding forcing lemma as “diagnostic”: detects transported poles at `2a+i m` when choosing extremal a.
- Label explicitly: **not used for UE‑shrinking closure** (meromorphic endpoint).

---

## F) Repro pack / fail‑closed toggles

Add a tiny “latch checklist” subsection to the repro pack notes:

- `defect_tooling_installed = true`
- `horizontal_resonance_nogo_installed = true`
- `missing_lever_open = true` (must remain TRUE)

