# v43 next build plan diff — post Batch 14 (apply to v42 baseline)

This is a *plan-level diff*: what the v43 build should change relative to v42 (and relative to v43 post‑Batch‑13 prebuild).

---

## 1) GEO‑C4 hygiene: centralize and enforce (NEW / strengthened)

**Add / strengthen a single “Hygiene & Admissibility” subsection** at the start of the GEO‑C4 section:

- Declare \(E\) is even entire and real-symmetric.
- Define hinge circle \(C_{m,\delta}\) and fix \(\kappa\in(0,1)\), \(h=\kappa\delta\).
- Define **shift‑admissibility / buffering**:
  \[
  \min_{\theta}\min_{\pm,\pm}\mathrm{dist}(v(\theta)\pm(a\pm h),Z(E))\ge \mathrm{buf}\,\delta.
  \]
- Explicitly allow shrinking \(\delta\) to enforce admissibility, with \(h\) shrinking proportionally.

**Rationale:** prevents invalid uses of \(E'/E\) on contours that cross poles.

---

## 2) UE reduction lemma: replace with BRIDGE version (UPDATED)

Replace the existing UE reduction inequality with the sharpened BRIDGE lemma:

\[
\Phi^\star \le \frac{\delta^2}{\sqrt\pi\,h}\int_0^{2\pi}|\mathcal D_{a,h}(v(\theta))|\,d\theta.
\]

Include the intermediate norm bound:

\[
\|P_2\psi\|_{L^2}\le \|\psi\|_{L^2}\le \frac{1}{\sqrt\pi}\int_0^{2\pi}|\mathcal D_{a,h}(v(\theta))|\,d\theta.
\]

---

## 3) NO‑GO lemma/remark: UE‑INPUT is RH‑strength (NEW)

Add a boxed remark or lemma immediately after FORCE:

- Under an off‑axis quartet, the forced \(k=2\) harmonic implies
  \[
  \int_0^{2\pi}|\mathcal D_{a,h}(v(\theta))|\,d\theta \gtrsim h/\delta^2.
  \]
- Therefore any UE input which bounds \(\int|\mathcal D|\) by \(O(h(\log m)^{C'}/a^2)\) is an RH‑closing statement (not “routine”).

**Rationale:** prevents “self-sabotage” where the final brick is mis-described as an easy corollary.

---

## 4) Active box replacement: keep one open statement only (LOCK)

Replace v42 UE‑INPUT (pointwise + derivative stack) with the v43 active statement:

\[
\boxed{
\int_0^{2\pi}|\mathcal D_{a,h}(v(\theta))|\,d\theta
\le C\,h\,\frac{(\log(m+3))^{C'}}{a^2}\quad (m\ge M).
}
\]

Add the exponent-budget note: aim for \(C'\le 4\) (or \(C'=4\) with \(\eta\) chosen small).

---

## 5) Editorial alignment: legacy language bridge (OPTIONAL but helpful)

Add a short remark: k=2 harmonic on the hinge circle is the contour analogue of π/2-carrier / mod‑4 lattice projector (odd/even lane orthogonality).

This is expository only; not used in proofs.

---

## 6) “Nothing else moves” rule

All other sections/lemmas remain unchanged from v42 unless they directly reference the old UE‑INPUT box.

