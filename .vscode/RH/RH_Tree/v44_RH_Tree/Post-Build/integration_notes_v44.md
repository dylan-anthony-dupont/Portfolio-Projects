# v44 Integration Notes (locked)

**Build:** v44 (post-build)  
**Compiled:** 2026-01-30  
**Status:** GEO–C4 machinery locked; single active UE frontier is now phase-preserving.

---

## What is now locked in v44

### GEO–C4 witness + endpoint
- Witness: hinge circle at height `m`, centered on the critical axis:
  \[
  v(\theta)=im+\delta e^{i\theta}.
  \]
- Field: \(\mathcal L_t(v)=\frac{E'}{E}(v+t)-\frac{E'}{E}(v-t)\), and \(\mathcal D_{a,h}=\mathcal L_{a+h}-\mathcal L_{a-h}\).
- Signal: \(\psi(\theta)=\Im(\mathcal D_{a,h}(v(\theta)))\).
- Endpoint:
  \[
  \Phi^\star=\frac{\delta^2}{h}\|P_2\psi\|_{L^2}
  =\frac{\delta^2}{h\sqrt\pi}\,|\widehat\psi(2)|.
  \]
  (Lemma `lem:geo-c4-ue-reduction-k2`.)

### FORCE side (truth-latching)
- Off-axis quartet \(\pm a\pm im\) forces a nonzero \(k=2\) channel on the hinge circle.
- Toy model gives an explicit constant forcing; stability lemma gives a robust absolute lower bound.

### Structural change from v43
- v44 **retires** the UE interface that relied on an \(L^1\) absolute-value bound on \(\mathcal D_{a,h}\) (phase-loss).
- v44 promotes a **signed** coefficient interface: the only thing we need to bound is \(|\widehat\psi(2)|\).

---

## Single active frontier

### UE-INPUT($k=2$) (Box `box:ue-input-v44`)
At the nominal policy \(\delta=\eta a/(\log(m+3))^2\), \(h=\kappa\delta\), prove constants \(C,C'>0\) such that
\[
|\widehat\psi(2)| \le C\,\frac{(\log(m+3))^{C'}}{a^2}\,h.
\]

This implies \(\Phi^\star=o(1)\) (or \(\Phi^\star\ll\eta^2\) at the exponent boundary), contradicting FORCE.

---

## Preferred analytic routes (UE playbook, Appendix `app:ue-playbook`)

1. **Archimedean absorption**: isolate the smooth Gamma-factor contribution (expected \(O(h)\)), reduce UE to the \(\zeta'/\zeta\) component.
2. **Kernel sum over zeros**: express \(\widehat\psi(2)=\sum_\rho K_{m,a,h,\delta}(\rho)\); show decay away from height `m`; use the certified tail harness for far zeros.
3. **Hardy/Poisson / disk functional**: reinterpret the coefficient as a boundary pairing and bound it by interior norms without taking absolute values.
4. **Optional Weil/Li bridge (scoping)**: attempt to match \(K\) to a Weil kernel \(\widehat g(\rho)\widehat g(1-\rho)\); not load-bearing yet.

---

## Next build guidance
If UE-INPUT($k=2$) is not closed internally, the next batch should exclusively target:
- an explicit kernel representation for \(\widehat\psi(2)\),
- provable decay of that kernel off the height window,
- and a clean separation of archimedean vs non-archimedean contributions.
