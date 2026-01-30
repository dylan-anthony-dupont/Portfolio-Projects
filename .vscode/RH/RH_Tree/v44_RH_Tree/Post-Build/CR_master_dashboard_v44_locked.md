# CR Master Dashboard — v44 (locked)

**Build:** v44 (post-build)  
**Compiled:** 2026-01-30  
**Single active frontier:** UE-INPUT($k=2$) — Box `box:ue-input-v44`

---

## 0) Current closure chain (locked except one box)

### GEO–C4 endpoint (locked)
- Witness: hinge circle $v(\theta)=im+\delta e^{i\theta}$.
- Field: $\mathcal D_{a,h}=\mathcal L_{a+h}-\mathcal L_{a-h}$ with $\mathcal L_t=f(v+t)-f(v-t)$ and $f=E'/E$.
- Signal: $\psi(\theta)=\Im(\mathcal D_{a,h}(v(\theta)))$.
- Endpoint:
  \[
  \Phi^\star=\frac{\delta^2}{h}\|P_2\psi\|_{L^2}
  =\frac{\delta^2}{h\sqrt\pi}\,|\widehat\psi(2)|.
  \]
  (Lemma `lem:geo-c4-ue-reduction-k2`.)

### FORCE (locked)
- Off-axis quartet forces a non-vanishing $k=2$ channel on the hinge circle.
- Toy model forcing is constant in $\delta$; stability lemma gives a robust absolute lower bound $\Phi^\star\ge c_0$.

### UE (OPEN — single active box)
- Only remaining obligation is a bound on the **signed** $k=2$ coefficient $|\widehat\psi(2)|$.

---

## 1) Single active statement

### UE-INPUT($k=2$)  — Box `box:ue-input-v44`
At $\delta=\eta a/(\log(m+3))^2$ and $h=\kappa\delta$, for shift/buffer-admissible hinge circles,
prove constants $C,C'>0$ such that
\[
|\widehat\psi(2)| \le C\,\frac{(\log(m+3))^{C'}}{a^2}\,h.
\]

**Implication (locked):** this yields $\Phi^\star=o(1)$ (or $\Phi^\star\ll\eta^2$ at the exponent boundary),
contradicting FORCE.

---

## 2) Why v44 is an “every build gets easier” move
- v43 UE was phrased in absolute-value boundary norms (phase loss).
- v44 rewrites UE as a **single signed Fourier coefficient** problem, keeping exactly the information
needed for potential explicit-formula / Weil bridges while remaining compatible with the existing GEO–C4 forcing machinery.

See Appendix `app:ue-playbook` (attack surface) and Appendix `app:weil-li-scope` (scoping).

---

## 3) Next actions (if UE-INPUT($k=2$) is not closed in-chat)
Recommended Batch 16 axes:
1) explicit kernel identity for $\widehat\psi(2)$ as a sum over zeros,  
2) archimedean absorption lemma (Gamma-factor $O(h)$) in the manuscript,  
3) certified tail harness compatibility: decay of $K_{m,a,h,\delta}(\rho)$ off the height window,  
4) (optional) Weil/Li factorization / domination attempt for the kernel.

---

## 4) Artifacts (v44)
- `manuscript_v44.tex`, `manuscript_v44.pdf`
- `integration_notes_v44.md`
- `v44_patchlog.md`
- `v44_repro_pack.zip`
