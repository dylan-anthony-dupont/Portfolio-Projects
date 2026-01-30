# v43 Integration Notes (LOCKED build)

**Build date:** 2026-01-30 (Europe/London)

## 0) What changed from v42 → v43 (canonical summary)

v43 is a **surgical manuscript rebuild** whose only purpose is to make the RH–closing “UE side” both:

1) **as weak as possible while still closing GEO–C4**, and  
2) **structurally aligned with the channel nature of the endpoint** (Fourier/harmonic extraction).

Concretely:

- **UE-INPUT (v42) was retired**: the previous box required *pointwise* control of a **shift-derivative field** (sup in θ, plus v–derivatives). Batch13/14 and the legacy analysis emphasized this is effectively **RH-strength** and not the minimal interface.
- **UE interface is replaced by a single boundary \(H^1\)/\(L^1\) control** on the GEO–C4 second-difference \(\mathcal D_{a,h}\) on the hinge circle.
- A **deterministic UE reduction lemma** was inserted: it converts that \(L^1\) boundary control directly into an upper bound for the **\(k=2\)** harmonic endpoint \(\Phi^\star\).
- A short **NO-GO / diagnostic lemma** was added (toy model): an off-axis quartet forces an \(L^1\) blow-up \(\int|\mathcal D_{a,h}|\gtrsim h/\delta^2\). This makes it explicit that the new UE box is still RH-closing (as it must be), but without the unnecessary pointwise derivative load.

Everything outside the GEO–C4 block is treated as **locked** and carried over unchanged.

---

## 1) Latched dependency map (single active closure statement)

### Definitions (locked)
- Witness: hinge circle \(v(	heta)=im+\delta e^{i	heta}\).
- Operators:  
  \(\mathcal L_t(v)=rac{E'}{E}(v+t)-rac{E'}{E}(v-t)\),  
  \(\mathcal D_{a,h}(v)=\mathcal L_{a+h}(v)-\mathcal L_{a-h}(v)\).
- Endpoint: \(\Phi^\star=rac{\delta^2}{h}\|P_2\psi\|_{L^2}\) with \(\psi(	heta)=\Im(\mathcal D_{a,h}(v(	heta)))\).

### FORCE (locked)
- Toy forcing + stability: if an off-axis quartet exists at \((a,m)\), then \(\Phi^\star\ge c_0(\kappa)>0\).

### UE-REDUCE (NEW, now locked)
- **Lemma (UE reduction from boundary \(H^1\))**:
  \[
  \Phi^\star(m,a,\delta,h)\ \le\ rac{\delta^2}{\sqrt\pi\,h}\int_0^{2\pi}ig|\mathcal D_{a,h}(v(	heta))ig|\,d	heta.
  \]

### Single active open statement (ONLY remaining gap)
- **UE-INPUT (v43)** (Box `box:ue-input-v43`):
  \[
  \int_0^{2\pi}ig|\mathcal D_{a,h}(v(	heta))ig|\,d	heta
  \ \le\ C\,h\,rac{(\log(m+3))^{C'}}{a^{2}}
  \]
  at the nominal policy \(\delta=\eta\,a/(\log(m+3))^2\), \(h=\kappa\delta\) (allowing smaller \(\delta\) for buffering).

### Closure (mechanical)
- UE-REDUCE + UE-INPUT ⇒
  \(\Phi^\star\ll \eta^2(\log(m+3))^{C'-4}\),
  contradicting FORCE for any \(C'<4\) (or \(C'=4\) with \(\eta\) chosen small).

---

## 2) Patch inventory (what was actually edited)

### GEO–C4 closure box
- Rewritten as **“Active closure lever (v43)”**, explicitly showing FORCE, UE-REDUCE, and the single UE-INPUT requirement.

### UE reduction section
- Subsection retargeted from “integration by parts / derivative field” to **boundary \(H^1\) control**.
- Inserted Lemma `lem:geo-c4-ue-reduction` with proof.

### UE-INPUT box
- Replaced with the single \(L^1\) boundary statement (Box `box:ue-input-v43`).

### NO-GO diagnostic
- Added Lemma `lem:geo-c4-l1-blowup` (toy-model \(L^1\) blow-up) immediately after forcing stability.

### Repro appendix wiring
- Added `\label{app:repro}` to the existing reproducibility appendix to resolve the front-matter reference.

---

## 3) What remains for v44 / next batch (brief)
- Prove UE-INPUT (v43) or reduce it to a further, cleaner analytic surrogate (but keep it single-box).
- Priority is a **contour \(L^1\) bound for \(\mathcal D_{a,h}\)** under shift-admissibility, with exponent budget \(C'\le 4\).

