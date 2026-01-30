# Batch 13 — RH-ABSORB-13  
## UE-INPUT hygiene package (v42)

**Scope:** This is a *sanity / hygiene* audit for the v42 GEO–C4 frontier statement **UE-INPUT** (Box `box:ue-input-v42`).  
I am not attempting to prove UE-INPUT; I am making the quantifiers, admissibility hypotheses, and shrink policy logically watertight.

---

## 1) UE-INPUT rewritten in quantifier-perfect form

### 1.1 Ground-truth objects (v42)

- Hinge circle: \(C_{m,\delta}=\{v(\theta)= i m+\delta e^{i\theta}:\theta\in[0,2\pi]\}\).
- Coupling: \(h=\kappa\delta\) with fixed \(\kappa\in(0,1)\).
- Two-sided field:
  \[
    \mathcal L_t(v)=\frac{E'}{E}(v+t)-\frac{E'}{E}(v-t),\qquad
    \mathcal D_{a,h}(v)=\mathcal L_{a+h}(v)-\mathcal L_{a-h}(v).
  \]
- Endpoint: \(\Phi^\star=(\delta^2/h)\,\|P_2\Im(\mathcal D_{a,h}\circ v)\|_{L^2([0,2\pi])}\).

The *only* open analytic obligation is UE-INPUT, and the closure logic is: **FORCE** (lower bound) + **UE-INPUT** (upper bound \(\to 0\)) \(\Rightarrow\) contradiction \(\Rightarrow\) no off-axis quartets.

### 1.2 Problem: current admissibility definition vs UE-INPUT’s use of \(\partial_t\)

In v42:

- Definition `def:shift-admissible-hinge` is stated only at the **four endpoint shifts** \(t\in\{\pm(a\pm h)\}\), sufficient to define \(\mathcal D_{a,h}(v(\theta))\).
- The UE-INPUT *field bound* version takes \(\sup_{t\in[a-h,a+h]}\partial_t\partial_v^j\mathcal L_t\), which implicitly requires that **\(\mathcal L_t\)** be well-defined and differentiable for *all* \(t\in[a-h,a+h]\) on the relevant boundary trace.

Therefore, the present “equivalently (by MVT in \(t\))” line is only valid if we assume an admissibility condition on the entire **shift corridor** \([a-h,a+h]\), not just the endpoints.

### 1.3 Recommendation: state UE-INPUT in a corridor-safe form

You have two clean options. **Pick exactly one** in v43+ to avoid silent hypothesis drift.

#### Option A (preferred): make UE-INPUT an inequality directly on \(\mathcal D_{a,h}\)

This avoids corridor admissibility entirely.

> **UE-INPUT\(_\mathcal D\)** *(cleanest quantifier form; no \(\partial_t\))*  
> Fix \(\kappa\in(0,1)\) and choose a buffer parameter \(\mathrm{buf}\in(0,1)\).  
> Then there exist constants \(C>0\), \(C'>0\), \(\eta_0\in(0,1)\), and \(m_0\ge 1\) such that for all  
> \[
> m\ge m_0,\qquad a\in(0,1),\qquad \eta\in(0,\eta_0],
> \]
> defining the nominal scale  
> \[
> \delta_0(m,a)=\frac{\eta a}{(\log(m+3))^2},
> \]
> the following holds:
>
> For every \(\delta\) with \(0<\delta\le \delta_0(m,a)\), set \(h=\kappa\delta\).  
> Assume \(C_{m,\delta}\) is \(\mathrm{buf}\)-admissible at \((a,h)\) in the *endpoint-only* sense of Definition `def:shift-admissible-hinge`.  
> Then for \(j=0,1,2\),
> \[
> \boxed{
> \sup_{\theta\in[0,2\pi]}\bigl|\partial_v^j\mathcal D_{a,h}(v(\theta))\bigr|
> \ \le\ 
> 2h\,C\,\frac{(\log(m+3))^{C'}}{a^{2+j}}.}
> \]
>
> (This implies, via Lemma `lem:geo-c4-ue-reduction`, that \(\Phi^\star(m,a,\delta,h)\ll_\kappa (\log m)^{C'}(\delta/a)^3\).)

This is the statement actually used by Lemma `lem:geo-c4-ue-reduction`. It keeps “what must be proved” aligned to “what is consumed.”

#### Option B: keep the \(\partial_t\)-field form, but upgrade admissibility to a corridor condition

If you want the \(\partial_t\) version for conceptual clarity, then you must *explicitly* require corridor admissibility:

> **UE-INPUT\(_{\partial_t}\)** *(corridor version; requires stronger admissibility)*  
> Same quantifiers \((\kappa,\mathrm{buf},C,C',\eta_0,m_0)\) as above.  
> For every \(\delta\in(0,\delta_0]\), \(h=\kappa\delta\), assume **corridor \(\mathrm{buf}\)-admissibility**:
> \[
> E(v(\theta)\pm t)\neq 0 \ \text{and}\ \mathrm{dist}(v(\theta)\pm t,Z(E))\ge \mathrm{buf}\cdot\delta
> \]
> for all \(\theta\in[0,2\pi]\) and all \(t\in[a-h,a+h]\).
> Then for \(j=0,1,2\),
> \[
> \boxed{
> \sup_{\theta}\sup_{t\in[a-h,a+h]}
> \bigl|\partial_t\partial_v^j\mathcal L_t(v(\theta))\bigr|
> \ \le\ C\,\frac{(\log(m+3))^{C'}}{a^{2+j}}.}
> \]
> Consequently, by the mean-value theorem in \(t\),
> \[
> \sup_{\theta}\bigl|\partial_v^j\mathcal D_{a,h}(v(\theta))\bigr|
> \le 2h\,C\,\frac{(\log(m+3))^{C'}}{a^{2+j}}.
> \]

---

## 2) Minimal buffering hypotheses required for each derivative order \(j=0,1,2\)

Here “buffering” is about staying away from poles of \(E'/E\), i.e. zeros of \(E\), on the **shifted boundary traces**.

### 2.1 For the \(\mathcal D\)-form (Option A)

- **\(j=0\) (value bound):**  
  *Minimal* requirement is **shift-admissibility at endpoints** (Definition `def:shift-admissible-hinge`), because that makes \(\mathcal D_{a,h}(v(\theta))\) well-defined and continuous on \([0,2\pi]\).

- **\(j=1,2\) (derivative bounds):**  
  To even talk about \(\partial_v^j\mathcal D_{a,h}(v(\theta))\) as a bounded quantity *uniformly in \(\theta\)*, you need that \(\mathcal D_{a,h}\) is holomorphic on a neighborhood of the trace.  
  A sufficient and essentially minimal hypothesis is **\(\mathrm{buf}\)-admissibility**:
  \[
  \min_{\theta}\min_{\pm,\pm}\mathrm{dist}\bigl(v(\theta)\pm(a\pm h),Z(E)\bigr)\ge \mathrm{buf}\cdot\delta.
  \]
  This guarantees a uniform analytic neighborhood (radius \(\asymp\delta\)) around each boundary point where \(\mathcal D_{a,h}\) is holomorphic, making \(\partial_v\mathcal D\) and \(\partial_v^2\mathcal D\) well-defined and controllable by standard complex-analytic estimates.

### 2.2 For the \(\partial_t\)-field form (Option B)

In addition to the above:

- For \(\partial_t\) and the MVT step to be legitimate, you need \(E(v(\theta)\pm t)\neq 0\) for **all** \(t\in[a-h,a+h]\), not merely \(t=a\pm h\).  
- For \(\partial_t\partial_v^j\mathcal L_t\) to be uniformly bounded, you also need a **corridor buffer** ensuring a uniform zero-free tube around those shifted traces for all \(t\) in the interval.

---

## 3) Monotone shrink lemma (UE-INPUT specific)

### 3.1 What is actually needed

The program’s policy is: *we may shrink \(\delta\) to enforce admissibility, and UE must remain valid under this shrink.*  
For UE-INPUT this must be interpreted at the level of the **consumed conclusion** (an upper bound for \(\Phi^\star\)), not as a pointwise claim that the raw field automatically decreases when \(\delta\) decreases (that is generally false for meromorphic fields with moving poles).

### 3.2 Proof-grade monotone-shrink statement

> **Lemma (UE-INPUT shrink safety, consumption-level).**  
> Assume UE-INPUT is stated in a \(\delta\)-uniform form (Option A or B): it holds for **every** \(\delta\in(0,\delta_0(m,a)]\) satisfying the relevant admissibility hypothesis, with constants independent of \(\delta\).  
> Then for any admissible shrink choice \(\delta'\le \delta_0(m,a)\), with \(h'=\kappa\delta'\),
> \[
> \Phi^\star(m,a,\delta',h')\ \ll_\kappa\ (\log(m+3))^{C'}\Big(\frac{\delta'}{a}\Big)^3
> \ \le\ 
> (\log(m+3))^{C'}\Big(\frac{\delta_0(m,a)}{a}\Big)^3,
> \]
> and the right-hand side is monotone non-increasing under further \(\delta\)-shrink.

*Proof.* Apply Lemma `lem:geo-c4-ue-reduction` with \(A(m,a)=C(\log(m+3))^{C'}\) to the chosen \((\delta',h')\). Since \(\delta'/a\le \delta_0/a\), the last inequality follows. ∎

### 3.3 Referee note (why a stronger monotonicity claim would be invalid)

Without the explicit **“for all \(\delta\le\delta_0\)”** quantifier in UE-INPUT, the monotone-shrink policy is not justified: the boundary trace changes with \(\delta\), and \(\mathcal D_{a,h}\) has poles whose absolute distance to the trace scales with \(\delta\).  
Therefore, any claim of the form “if UE holds at \(\delta_0\) it automatically holds at smaller \(\delta\)” would require an additional analytic lemma that is **not present** in v42.

---

## 4) NO-GO alignment note (v42 guards vs GEO–C4)

The v42 Executive Status already scope-audits the NO-GO list so that none of them forbids GEO–C4:

- The “projection endpoints are dead” NO-GO is explicitly limited to projections that **annihilate the forced local kernel** or collapse to pointwise UE. GEO–C4 projects onto the **forced** \(k=2\) harmonic of the dipole kernel; it does not fall under that NO-GO.
- The pointwise/sup UE ceiling NO-GO concerns \(\sup_{\partial B}|E'/E|\)-style endpoints and is orthogonal to the GEO–C4 harmonic extraction route.

**Edit recommendation:** keep the NO-GO statements explicitly *endpoint-class-scoped* (as in v42) to prevent future readers from misapplying them against GEO–C4.

---

## 5) Paste-ready TeX edits (minimal)

### 5.1 (If using Option B) strengthen admissibility definition

```tex
% Add after Definition  \ref{def:shift-admissible-hinge}
\begin{definition}[Corridor buf--admissible hinge circle]
Fix $(m,a,\delta,h)$ with $0<h<\delta$.  We say $C_{m,\delta}$ is \emph{corridor $\mathrm{buf}$--admissible at $(a,h)$} if
\[
E\bigl(v(\theta)\pm t\bigr)\neq 0
\quad\text{and}\quad
\mathrm{dist}\bigl(v(\theta)\pm t, Z(E)\bigr)\ge \mathrm{buf}\cdot\delta
\]
for all $\theta\in[0,2\pi]$ and all $t\in[a-h,a+h]$.
\end{definition}
```

### 5.2 Replace UE-INPUT box statement by Option A (recommended)

```tex
% Replace the UE-INPUT field bound in Box \ref{box:ue-input-v42} by:
\medskip
\noindent\textbf{UE-INPUT (quantifier-perfect; D-form).}
Fix $\kappa\in(0,1)$ and $\mathrm{buf}\in(0,1)$.  
There exist $C,C'>0$, $\eta_0\in(0,1)$ and $m_0\ge 1$ such that for all
$m\ge m_0$, $a\in(0,1)$, $\eta\in(0,\eta_0]$, with $\delta_0=\eta a/(\log(m+3))^2$, the following holds:
for every $\delta\in(0,\delta_0]$, setting $h=\kappa\delta$ and assuming $C_{m,\delta}$ is $\mathrm{buf}$--admissible at $(a,h)$,
one has for $j=0,1,2$,
\[
\sup_{\theta\in[0,2\pi]}\bigl|\partial_v^j\mathcal D_{a,h}(v(\theta))\bigr|
\le
2h\,C\,\frac{(\log(m+3))^{C'}}{a^{2+j}}.
\]
```

### 5.3 Add the shrink-safety lemma (consumption-level)

```tex
\begin{lemma}[UE-INPUT shrink safety]
Assume UE-INPUT holds $\delta$--uniformly for all $0<\delta\le\delta_0(m,a)$ satisfying the admissibility hypothesis, with constants independent of $\delta$.
Then for any admissible shrink choice $\delta'\le\delta_0(m,a)$ (with $h'=\kappa\delta'$),
the GEO--C4 endpoint satisfies
\[
\Phi^\star(m,a,\delta',h')\ll_\kappa (\log(m+3))^{C'}\Big(\frac{\delta'}{a}\Big)^3
\le
(\log(m+3))^{C'}\Big(\frac{\delta_0(m,a)}{a}\Big)^3.
\]
\end{lemma}
```

---

### Deliverable recap (what this package fixes)

- Removes the silent hypothesis gap between endpoint-only shift-admissibility and \(\partial_t\)-corridor requirements.
- Makes UE-INPUT quantifiers explicit in the form actually consumed by the closure lemma.
- Replaces informal “monotone shrink makes UE easier” with a proof-grade, consumption-level lemma.

