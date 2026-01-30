# CR Master Dashboard — v43 LOCKED (2026-01-30)

## 0) Version stance
- **Manuscript:** `manuscript_v43.tex` / `manuscript_v43.pdf` (LOCKED)
- **Only active frontier:** **UE-INPUT (v43)** — Box `box:ue-input-v43`
- **Everything else:** treated as locked / unchanged from v42, except for the GEO–C4 UE interface refactor.

---

## 1) Single active closure statement (truth-latched)
### UE-INPUT (v43)
Witness: hinge circle \(v(	heta)=im+\delta e^{i	heta}\), nominal
\[
\delta=\eta\,\frac{a}{(\log(m+3))^2},\qquad h=\kappa\delta,\qquad \kappa\in(0,1),
\]
with shift-admissibility / buffering (allow smaller \(\delta\) if needed).

**Goal:**
\[
\boxed{
\int_0^{2\pi}\Big|\mathcal D_{a,h}(v(\theta))\Big|\,d\theta
\ \le\ C\,h\,\frac{(\log(m+3))^{C'}}{a^2}.
}
\]
Exponent budget: \(C'<4\) is “automatic closure”; \(C'=4\) still closes with \(\eta\) chosen sufficiently small.

---

## 2) Latched dependency map (one-pass closure chain)
### Definitions (locked)
- \(\mathcal L_t(v)=E'/E(v+t)-E'/E(v-t)\)
- \(\mathcal D_{a,h}(v)=\mathcal L_{a+h}(v)-\mathcal L_{a-h}(v)\)
- \(\psi(\theta)=\Im(\mathcal D_{a,h}(v(\theta)))\)
- \(P_2\): projection onto \(\mathrm{span}\{\cos(2\theta),\sin(2\theta)\}\)
- Endpoint:
  \[
  \Phi^\star=\frac{\delta^2}{h}\,\|P_2\psi\|_{L^2([0,2\pi])}.
  \]

### FORCE (locked)
- **Toy forcing** (Lemma `lem:geo-c4-toy-force`): off-axis quartet ⇒ \(\Phi^\star\ge c_0(\kappa)\).
- **Stability** (Lemma `lem:geo-c4-force-stable`): analytic remainders do not kill the forcing.

### UE-REDUCE (NEW but now locked)
- **Lemma `lem:geo-c4-ue-reduction`:**
  \[
  \Phi^\star\le \frac{\delta^2}{\sqrt\pi\,h}\int_0^{2\pi}|\mathcal D_{a,h}(v(\theta))|\,d\theta.
  \]

### Closure (mechanical)
UE-INPUT + UE-REDUCE ⇒
\[
\Phi^\star\ll \eta^2(\log(m+3))^{C'-4},
\]
contradicting FORCE for large enough \(m\) (or for small enough \(\eta\) if \(C'=4\)).

---

## 3) Diagnostics / NO-GO signals (kept in-text)
- **Lemma `lem:geo-c4-l1-blowup` (toy model):**
  \[
  \int_0^{2\pi}|\mathcal D^{\mathrm{sing}}_{a,h}(v(\theta))|\,d\theta\ \gtrsim\ \frac{h}{\delta^2}.
  \]
  Meaning: any δ-uniform boundary \(L^1\) bound of UE-INPUT type is inherently RH-closing (as expected).

---

## 4) Next action queue (v44 direction)
- Attack UE-INPUT (v43) directly:
  - express \(\mathcal D_{a,h}\) in a form suited to **contour averaging** (Hardy/Hilbert transform, Cauchy integral, or explicit formula),
  - isolate the δ-scale singular contributions and show they cannot persist without off-axis zeros,
  - retain the exponent budget \(C'\le 4\).

