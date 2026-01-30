# Integration Notes — v44 Pre‑Build (Pre‑Batch‑15)

**Base manuscript:** v43 (locked build).  
**New input (this pass):** legacy “Weil/Li bridge target” quote + validation against primary sources.

## 0) Executive verdict: is the Weil/Li bridge a serious leap forward?

### What is real (and valuable)
1. **Weil’s positivity criterion is genuinely RH‑equivalent.** In particular, Burnol’s exposition states: RH holds iff
   \[
   \sum_{\rho}\,\widehat g(\rho)\,\widehat g(1-\rho)\ \ge 0\quad\text{for all smooth compactly supported }g\text{ on }(0,\infty).
   \]
   and it sketches the contrapositive via interpolation of Mellin values. citeturn1view0
2. **Li’s criterion is also RH‑equivalent** (positivity of Li/Keiper–Li coefficients). citeturn0search2turn0search5
3. The *structure* of GEO‑C4 (completed object, log‑derivative poles at zeros, finite‑differences in shift, harmonic extraction) is **explicit‑formula‑flavoured**, i.e. it produces **zero‑kernel sums** that are in the same ecosystem as Weil/Li.

### What is *not* automatic (key caution)
The bridge does **not** directly close UE‑INPUT unless we prove a **Bridge Lemma** identifying our GEO‑C4 channel functional with a Weil/Li functional (or a sufficiently rich subfamily). Weil’s criterion quantifies over *all* test functions; showing positivity for one rigid parametric family is not enough.

### Net assessment
**Yes, it’s a serious conceptual alignment** that can make future builds easier *if* we can (i) keep phase information and (ii) identify our k=2 channel as an explicit Weil/Li test (or build a dense family). Otherwise it remains a valuable **cross‑check/harness** but not a closure shortcut.

## 1) Current v43 posture (locked vs open)

### Locked
- GEO‑C4 witness (hinge circle) + endpoint \(\Phi^\star\) definition.
- FORCE chain (toy forcing + stability) producing \(\Phi^\star\ge c_0(\kappa)\).
- UE‑REDUCE lemma: \(\Phi^\star\) is bounded above by a constant multiple of \((\delta^2/h)\int |\mathcal D_{a,h}|\).

### Single active OPEN box (v43)
\[
\boxed{\ \int_0^{2\pi}\big|\mathcal D_{a,h}(v(\theta))\big|\,d\theta\ \le\ C\,h\,\frac{(\log(m+3))^{C'}}{a^2}\ }
\]
with \(v(\theta)=im+\delta e^{i\theta}\), \(h=\kappa\delta\), and nominal \(\delta=\eta a/(\log(m+3))^2\) (allowing smaller \(\delta\) for buffering).

## 2) What the Weil/Li bridge changes in our UE attack surface

### 2.1 The phase‑loss issue is now formal
Our v43 UE interface is an **absolute value** \(L^1\) bound. Weil/Li phenomena are **signed / phase‑sensitive** (pairings \(\widehat g(\rho)\widehat g(1-\rho)\), Li coefficients). This does not refute v43; it clarifies:

> v43 UE‑INPUT is a magnitude‑control sufficient condition; the Weil/Li bridge will likely require a **signed channel** control.

### 2.2 Candidate “bridge‑compatible” UE interfaces (do not change v43 yet)
We introduce two optional interfaces for investigation (not yet promoted):

**(UE‑k2)**: bound the k=2 coefficient directly:
\[
\Big|\int_0^{2\pi}\mathcal D_{a,h}(v(\theta))\,e^{-2i\theta}\,d\theta\Big|\ \le\ C\,h\,\frac{(\log(m+3))^{C'}}{a^2}.
\]

**(WEIL‑ID)**: represent the k=2 channel (or its square) as a Weil functional for a test \(g_{m,a,\delta}\):
\[
\text{GEO‑C4 channel}(m,a,\delta)\ \equiv\ \sum_{\rho}\widehat g_{m,a,\delta}(\rho)\widehat g_{m,a,\delta}(1-\rho)\ +\ \text{(prime/archimedean side)}.
\]

If either interface can be proven RH‑free using explicit‑formula machinery, it can become the new “single active box” in a future build (v45+). For v44, they are **targets** for Batch‑15 exploration.

## 3) Batch‑15 goals (what we need back)

1. **Primary:** attempt a proof (or sharp NO‑GO) for v43’s UE‑INPUT (L1 bound on \(\mathcal D_{a,h}\)).
2. **Bridge lemma attempt:** compute/express the **k=2 Fourier coefficient** of \(\mathcal D_{a,h}(v(\theta))\) as an explicit sum over zeros (residues) and compare its kernel to Mellin transforms.
3. **Weil feasibility:** determine whether the parametric family \((m,a,\delta)\mapsto g_{m,a,\delta}\) can be rich enough (density / interpolation) to inherit Weil’s contrapositive logic.
4. **Li feasibility:** determine whether our channel can be rewritten as a finite combination of Li coefficients (or their generating function) or as a positive quadratic form thereof.

## 4) Build intent for v44 (pre‑commitments)

v44 will be a **documentation + attack‑surface sharpening build**, not a frontier jump:

- Add an Appendix subsection “Weil/Li bridge harness” with precise statements and a Bridge‑Lemma target.
- Add/refresh the “UE Playbook” appendix page (definitions, open box, allowable decompositions, routes A–D).
- Keep the single open box unchanged unless Batch‑15 yields a strictly better replacement with a proof‑grade reduction.
