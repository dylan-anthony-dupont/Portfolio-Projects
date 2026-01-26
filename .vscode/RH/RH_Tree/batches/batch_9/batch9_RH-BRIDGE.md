# Batch 9 — RH‑BRIDGE
**Callsign:** RH‑BRIDGE  
**Mission:** Provide geometric/analytic bridge lemmas for the **defect log‑derivative**
\(\mathcal L_a(v):=\frac{E'}{E}(v+a)-\frac{E'}{E}(v-a)=\partial_v\log\mathcal Q_a(v)\)
on the **buffered collar contour**, with correct \(\delta\)-scaling and explicit collar/branch safety.

This is a **pre‑v39** decision batch: I am providing the Bridge‑side kernel and safety lemmas that ENVELOPE can slot into its endpoint upper bound. I am not asserting closure.

---

## 0) Frame map (mandatory; RH‑free)

- **s‑frame:** \(s=\sigma+it\). A nontrivial zero is \(\rho=\beta+i\gamma\) (no assumption \(\beta=\tfrac12\)).
- **u‑frame (width‑2):** \(u=2s\). Then \(u_\rho=2\beta+i\,2\gamma\).
- **v‑frame (centered):** \(v=u-1\). Then
  \[
  v_\rho=(2\beta-1)+i\,2\gamma.
  \]
  Define the **horizontal displacement** \(a:=\Re(v_\rho)=2\beta-1\) and the **height** \(m:=\Im(v_\rho)=2\gamma\).  
  Off‑critical‑line means \(a\neq 0\).

**Working function:** v35+ fixes completion: \(E(v)=\Xi_2(1+v)\) where \(\Xi_2(u)=\xi(u/2)\) is entire. Then \(E\) is entire and satisfies the exact symmetry
\[
E(v)=E(-v)
\]
(because \(\Xi_2(u)=\Xi_2(2-u)\) transports to \(v\mapsto -v\)).

---

## 1) Defect objects and collar-safe domains

### 1.1 Defect quotient and defect log‑derivative
For a fixed \(a>0\), define:
\[
\mathcal Q_a(v):=\frac{E(v+a)}{E(v-a)},\qquad
\mathcal L_a(v):=\partial_v\log\mathcal Q_a(v)=\frac{E'}{E}(v+a)-\frac{E'}{E}(v-a).
\]

### 1.2 Geometry: central box and shifted boxes
Let the **central box** be
\[
B_0:=B(0,m,\delta)=\{v:\ |\Re v|\le \delta,\ |\Im v-m|\le \delta\},
\]
and define shifted boxes:
\[
B_+(a):=B(a,m,\delta)=B_0+a,\qquad
B_-(a):=B(-a,m,\delta)=B_0-a.
\]

For \(\kappa\in(0,1)\), define the **buffered interior box**
\[
B_{0,\kappa/2}:=\{v\in B_0:\dist(v,\partial B_0)\ge \kappa\delta/2\},
\]
and similarly \(B_{\pm,\kappa/2}:=B_{\pm}(a)_{\kappa/2}=B_{0,\kappa/2}\pm a\).

### 1.3 Collar / branch safety hypothesis (mandatory)
Assume **\(\kappa\)-admissibility for the shifted boxes**:
\[
\dist(\partial B_{\pm}(a),\ \mathcal Z(E))\ \ge\ \kappa\delta.
\]
This is the correct hypothesis for \(\mathcal L_a\) on \(\partial B_{0,\kappa/2}\), because evaluating \(\mathcal L_a(v)\) requires \(E(v\pm a)\neq 0\).

---

## 2) Collar/branch safety lemma for \(\mathcal Q_a,\mathcal L_a\) (mandatory)

### Lemma 2.1 (defect objects are collar-safe on the buffered contour)
Assume \(E\) is holomorphic on a neighborhood of \(\overline{B_\pm(a)}\) and that \(\kappa\)-admissibility holds for both shifted boxes \(B_\pm(a)\). Then:

1. \(E\) is nonvanishing on an open neighborhood of \(\partial B_{\pm,\kappa/2}\).
2. For every \(v\in\partial B_{0,\kappa/2}\), the points \(v\pm a\) lie in \(\partial B_{\pm,\kappa/2}\), hence \(E(v\pm a)\neq 0\).
3. Therefore \(\mathcal Q_a\) and \(\mathcal L_a\) are holomorphic on an open neighborhood of \(\partial B_{0,\kappa/2}\).
4. For every oriented sub‑arc \(S\subset\partial B_{0,\kappa/2}\), the **phase increment**
   \[
   \Delta_S \arg \mathcal Q_a \ :=\ \Im\int_S \mathcal L_a(v)\,dv
   \]
   is well-defined and **branch-independent** (no choice of global \(\log\) is required).

**Why this is the correct “branch safety” statement:** \(\Delta_S\arg f\) is defined via \(\Im\int (f'/f)\) and requires only that \(f\) be nonzero on a neighborhood of \(S\).

---

## 3) Task A — Difference-kernel bounds (mandatory)

### 3.1 Single-zero model kernel
For a point \(\rho\in\mathbb C\) (think: a zero of \(E\)), define the local difference kernel
\[
K_a(v;\rho)\ :=\ \frac{1}{v+a-\rho}-\frac{1}{v-a-\rho}
\ =\ -\frac{2a}{(v-\rho)^2-a^2}.
\]

This is the exact contribution of a simple linear factor \((v-\rho)\) to \(\mathcal L_a\); for a zero of multiplicity \(m_\rho\), the contribution is \(m_\rho K_a(v;\rho)\).

### 3.2 Primitive identity (phase form)
On any path \(S\) avoiding the poles \(v=\rho\pm a\),
\[
K_a(v;\rho)=\partial_v\log\!\Big(\frac{v+a-\rho}{v-a-\rho}\Big),\quad\text{so}\quad
\Im\int_S K_a(v;\rho)\,dv
=\Delta_S\arg(v+a-\rho)-\Delta_S\arg(v-a-\rho).
\]
This representation is useful because each \(\Delta_S\arg(\cdot)\) is automatically bounded by \(\pi\) for a line segment \(S\), hence the trivial bound
\[
\Big|\Im\int_S K_a(v;\rho)\,dv\Big|\le 2\pi
\]
(always; no geometry needed).

### 3.3 Uniform geometric bound in terms of distance to shifted segment(s)
Let \(S\) be a \(C^1\) segment of length \(\ell(S)\le 2\delta\). Define the shifted segments \(S_\pm:=S\pm a\). Then for every \(v\in S\),
\(|v+a-\rho|=\dist(\rho, S_+)\) up to the usual “\(\ge\)” inequality, and similarly for \(S_-\). More precisely, set
\[
d_+(\rho;S):=\dist(\rho,S_+)=\dist(\rho-a,S),\qquad
d_-(\rho;S):=\dist(\rho,S_-)=\dist(\rho+a,S).
\]

#### Lemma 3.1 (difference-kernel integral bound; sharp δ scaling)
Assume \(d_+(\rho;S)>0\) and \(d_-(\rho;S)>0\). Then:
\[
\boxed{\ \Big|\int_S K_a(v;\rho)\,dv\Big|\ \le\ \frac{2|a|\,\ell(S)}{d_+(\rho;S)\,d_-(\rho;S)}\ \le\ \frac{4|a|\,\delta}{d_+(\rho;S)\,d_-(\rho;S)}.\ }
\]
Consequently,
\[
\boxed{\ \Big|\Im\int_S K_a(v;\rho)\,dv\Big|\ \le\ \frac{4|a|\,\delta}{d_+(\rho;S)\,d_-(\rho;S)}.\ }
\]

**Proof (1 line):** for \(v\in S\),
\(|K_a(v;\rho)|=\frac{2|a|}{|v+a-\rho|\,|v-a-\rho|}\le \frac{2|a|}{d_+d_-}\),
then integrate over \(\ell(S)\le 2\delta\).

#### Lemma 3.2 (optional L² bound on a segment)
Under the same hypotheses,
\[
\boxed{\ \int_S |K_a(v;\rho)|^2\,|dv|\ \le\ \ell(S)\,\Big(\frac{2|a|}{d_+d_-}\Big)^2\ \le\ 2\delta\,\Big(\frac{2|a|}{d_+d_-}\Big)^2.\ }
\]

**Comment on program constraints:** this is an *absolute* \(L^2\) statement, but it is on the **difference kernel**, not \(|E'/E|\). Whether ENVELOPE is allowed to use this depends on the current “absolute endpoints” posture for the defect class.

---

## 4) Task B — Near/far decomposition lemma (mandatory)

### 4.1 Definition (“near tube”)
Fix a tube radius \(r>0\). Define the **near tube** of zeros relative to \(S\) (for the defect shift \(a\)) by:
\[
\mathcal N_r(S;a)\ :=\ \bigl\{\rho\in\mathcal Z(E):\ \min\{d_+(\rho;S),d_-(\rho;S)\}\le r\bigr\}.
\]
Equivalently: \(\rho\) lies within distance \(r\) of either shifted segment \(S+a\) or \(S-a\).

### Lemma 4.1 (near/far split for phase contribution of \(K_a\))
Let \(S\) be a segment with \(\ell(S)\le 2\delta\). Then:

- (**Far zeros**) For any \(\rho\notin \mathcal N_r(S;a)\) (so \(d_+\ge r\) and \(d_-\ge r\)):
  \[
  \boxed{\ \Big|\Im\int_S K_a(v;\rho)\,dv\Big|\ \le\ \frac{4|a|\,\delta}{r^2}.\ }
  \]
- (**Near zeros**) For any \(\rho\in \mathcal N_r(S;a)\):
  \[
  \boxed{\ \Big|\Im\int_S K_a(v;\rho)\,dv\Big|\ \le\ 2\pi\ }
  \]
  (trivial geometric bound via the primitive identity).

**What this buys:** if ENVELOPE can show that the near-tube set \(\mathcal N_r(S;a)\) is small (or cancels structurally), then the far contribution is automatically \(O(|a|\delta/r^2)\). A natural choice compatible with \(\delta_0=\eta a/(\log m)^2\) is \(r\asymp a\), which yields far contributions \(O(\delta/a)=O((\log m)^{-2})\) per zero.

---

## 5) Task C — κ‑admissibility + branch safety (mandatory recap)

- κ‑admissibility on **both** shifted boxes \(B_\pm(a)\) is the clean hypothesis ensuring \(\mathcal Q_a,\mathcal L_a\) are holomorphic on a collar neighborhood of \(\partial B_{0,\kappa/2}\).  
- Phase increments \(\Delta_S\arg \mathcal Q_a\) are defined by \(\Im\int_S \mathcal L_a\,dv\) and are branch‑independent.

This is the correct “no branch vagueness” posture for the defect endpoint class.

---

## 6) Task D — Forced‑zero obstruction interface (mandatory)

The forced‑zero obstruction in the phase/winding endpoint class was: **one interior zero forces an \(O(1)\) topological term** (argument principle). For the defect class, the closed‑loop integral measures **a difference of zero counts** and is therefore *zero‑neutral* under symmetric quartets.

### Lemma 6.1 (argument principle for the defect quotient; no forced quartet term)
Assume \(\mathcal Q_a\) is holomorphic and nonvanishing on \(\partial B_{0,\kappa/2}\). Then:
\[
\Im\oint_{\partial B_{0,\kappa/2}}\mathcal L_a(v)\,dv
=\Im\oint_{\partial B_{0,\kappa/2}}\partial_v\log\mathcal Q_a(v)\,dv
=2\pi\Big(N_+(a)-N_-(a)\Big),
\]
where
\[
N_+(a)=\#\{\rho\in\mathcal Z(E)\cap B_{+,\kappa/2}\}\quad\text{and}\quad
N_-(a)=\#\{\rho\in\mathcal Z(E)\cap B_{-,\kappa/2}\},
\]
counted with multiplicity.

**Proof:** substitute \(\mathcal L_a=(E'/E)(v+a)-(E'/E)(v-a)\) and change variables \(w=v\pm a\); each loop integral counts zeros of \(E\) in the shifted interior box by the argument principle.

### Corollary 6.2 (zero‑neutrality under evenness)
If \(E\) is even and the contour/boxes are symmetric (as above: \(B_-(a)=-B_+(a)\)), then \(N_+(a)=N_-(a)\) for any \(a\), hence:
\[
\Im\oint_{\partial B_{0,\kappa/2}}\mathcal L_a(v)\,dv=0.
\]
In particular, an off-axis quartet at displacement \(\pm a\) contributes **no forced \(2\pi\)** winding to the defect quotient: the forced quartet does **not** reintroduce an unavoidable \(O(1)\) topological term in the defect endpoint class.

### Local cancellation at the “danger pole” (useful sanity check)
If \(E\) has zeros at \(\rho_+=a+im\) and \(\rho_-=-a+im\) (the height‑\(m\) symmetric pair), then the **poles at \(v=im\)** in \(K_a(v;\rho_+)\) and \(K_a(v;\rho_-)\) cancel exactly:
\[
K_a(v;\rho_+)+K_a(v;\rho_-)
=\Big(\frac{1}{v-im}-\frac{1}{v-2a-im}\Big)+\Big(\frac{1}{v+2a-im}-\frac{1}{v-im}\Big)
=\frac{1}{v+2a-im}-\frac{1}{v-2a-im}.
\]
Thus the pair’s combined contribution on a length-\(2\delta\) segment \(S\subset B_0\) is bounded by \(O(\delta/a)\), not \(O(1)\), consistent with “zero-neutral” design.

---

## 7) Task E — S6 explicit‑formula mapping (mandatory)

### What the defect shift \(a\) means
In v‑frame, \(a=\Re(v_\rho)=2\beta-1\). So \(\beta=\tfrac12+\tfrac a2\).  
In explicit formula language (e.g. for \(\psi(x)\)), an off-axis zero contributes oscillations with amplitude scaling like \(x^{\beta}\), i.e.
\[
x^{\beta}=x^{1/2}\,x^{a/2}.
\]
The **amplitude leak** is the factor \(x^{a/2}\) (growing when \(a>0\)).

### Why \(\mathcal Q_a\) and \(\mathcal L_a\) are a natural “leak witness” class (interpretation only)
The defect quotient compares the same analytic object at horizontally shifted points:
\(\mathcal Q_a(v)=E(v+a)/E(v-a)\). Under Mellin/explicit-formula heuristics, horizontal shifts correspond to changing the real part of the exponent in weights like \(x^{s}\), hence naturally producing factors of the form
\[
x^{(1+v+a)/2}-x^{(1+v-a)/2}
=x^{(1+v)/2}\big(x^{a/2}-x^{-a/2}\big)
=2\sinh\!\Big(\frac{a}{2}\log x\Big)x^{(1+v)/2}.
\]
Thus, the “difference” class \(\mathcal L_a=\partial_v\log\mathcal Q_a\) is aligned with isolating the **odd-in-\(a\)** component of horizontal sensitivity, which is the same direction in which an off-axis zero produces a growth factor \(x^{a/2}\).

**Important:** This is an *interpretation harness*, not a logical dependency in the proof spine.

---

# MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* Callsign: RH-BRIDGE
* Result classification: **CONDITIONAL**
* Target gaps closed (by ID):
  - **(Bridge-side) forced-zero obstruction interface for defect endpoints:** supplied via Lemma 6.1/Cor. 6.2 (argument principle gives **difference of zero counts**, not forced winding).
  - **(Bridge-side) δ-scaling kernel control:** supplied via Lemma 3.1–3.2 and Lemma 4.1 (difference kernel yields \(O(|a|\delta/r^2)\) far control).
* Target gaps still open (by ID):
  - **ENVELOPE integration gap:** ENVELOPE must choose the exact defect endpoint functional (signed phase increment vs energy) and propagate δ-uniform constants through the residual/local split.
  - **LOCAL interface gap:** ENVELOPE/LOCAL must prove that the near-tube set \(\mathcal N_r(S;a)\) is small or structurally canceling for the chosen \(r\) (or provide a certified majorant compatible with the budget gate).
* Key conclusions (≤5 bullets):
  1. Under κ-admissibility of the shifted boxes, \(\mathcal Q_a,\mathcal L_a\) are holomorphic on a collar neighborhood of the buffered contour, so phase increments are branch-safe and well-defined.
  2. The single-zero difference kernel obeys the sharp segment bound \(|\Im\int_S K_a|\le 4|a|\delta/(d_+d_-)\), with an optional \(L^2\) bound.
  3. A clean near/far decomposition exists: far zeros give \(O(|a|\delta/r^2)\), only zeros within an \(r\)-tube around \(S\pm a\) can contribute \(O(1)\).
  4. **Forced-zero obstruction is resolved by design**: the defect closed-loop integral counts **\(N_+(a)-N_-(a)\)**, hence symmetric quartets contribute zero net winding.
  5. The defect shift \(a\) aligns naturally with the explicit-formula amplitude leak factor \(x^{a/2}\) (interpretation harness only).

* Paste-ready manuscript edits (TeX blocks):

  (i) revised lemma/proposition statements
```tex
\begin{definition}[Defect quotient and defect log-derivative]\label{def:defect_Q_L}
Fix $a>0$ and define
\[
\mathcal Q_a(v):=\frac{E(v+a)}{E(v-a)},\qquad
\mathcal L_a(v):=\partial_v\log\mathcal Q_a(v)=\frac{E'}{E}(v+a)-\frac{E'}{E}(v-a),
\]
whenever $E(v\pm a)\neq 0$.
\end{definition}

\begin{lemma}[Collar safety for defect objects]\label{lem:defect_collar_safe}
Let $B_0=B(0,m,\delta)$ and $B_\pm(a):=B_0\pm a$.
Assume $E$ is holomorphic on a neighborhood of $\overline{B_\pm(a)}$ and that both shifted boxes
are $\kappa$--admissible:
\[
\dist(\partial B_\pm(a),\mathcal Z(E))\ge \kappa\delta.
\]
Then $\mathcal Q_a$ and $\mathcal L_a$ are holomorphic on an open neighborhood of
$\partial B_{0,\kappa/2}$, and for any oriented sub-arc $S\subset\partial B_{0,\kappa/2}$
the phase increment
\[
\Delta_S\arg\mathcal Q_a := \Im\int_S \mathcal L_a(v)\,dv
\]
is well-defined and branch-independent.
\end{lemma}

\begin{lemma}[Difference-kernel bound on a segment]\label{lem:diff_kernel_bound}
Let $S$ be a $C^1$ segment of length $\ell(S)\le 2\delta$ and let $\rho\in\mathbb C$.
Set
\[
K_a(v;\rho):=\frac{1}{v+a-\rho}-\frac{1}{v-a-\rho}.
\]
Let $d_+ := \dist(\rho,S+a)$ and $d_- := \dist(\rho,S-a)$, and assume $d_+,d_->0$.
Then
\[
\Big|\Im\int_S K_a(v;\rho)\,dv\Big| \le \Big|\int_S K_a(v;\rho)\,dv\Big|
\le \frac{2|a|\ell(S)}{d_+d_-} \le \frac{4|a|\delta}{d_+d_-}.
\]
Moreover,
\[
\int_S |K_a(v;\rho)|^2\,|dv| \le \ell(S)\Big(\frac{2|a|}{d_+d_-}\Big)^2 \le 2\delta\Big(\frac{2|a|}{d_+d_-}\Big)^2.
\]
\end{lemma}

\begin{lemma}[Near/far tube split]\label{lem:diff_kernel_near_far}
Let $S$ be a segment with $\ell(S)\le 2\delta$ and let $r>0$.
Define the near tube
\[
\mathcal N_r(S;a):=\{\rho\in\mathcal Z(E):\min\{\dist(\rho,S+a),\dist(\rho,S-a)\}\le r\}.
\]
If $\rho\notin\mathcal N_r(S;a)$ then
\[
\Big|\Im\int_S K_a(v;\rho)\,dv\Big| \le \frac{4|a|\delta}{r^2}.
\]
If $\rho\in\mathcal N_r(S;a)$ then the trivial bound holds:
\[
\Big|\Im\int_S K_a(v;\rho)\,dv\Big|\le 2\pi.
\]
\end{lemma}

\begin{lemma}[Argument principle for the defect quotient]\label{lem:defect_arg_principle}
Assume $\mathcal Q_a$ is holomorphic and nonvanishing on $\partial B_{0,\kappa/2}$.
Then
\[
\Im\oint_{\partial B_{0,\kappa/2}}\mathcal L_a(v)\,dv = 2\pi\bigl(N_+(a)-N_-(a)\bigr),
\]
where $N_\pm(a)$ counts the zeros of $E$ in $B_{\pm,\kappa/2}=B_{0,\kappa/2}\pm a$ (with multiplicity).
In particular, if $E$ is even and $B_-(a)=-B_+(a)$, then $N_+(a)=N_-(a)$ and the defect winding is zero.
\end{lemma}
```

  (ii) revised definitions/remarks
```tex
\begin{remark}[Forced-zero obstruction avoided in the defect class]\label{rem:defect_forced_zero}
In contrast to phase endpoints based directly on $\Delta\arg E$ (where one interior zero forces an $O(1)$
topological term), the defect endpoint built from $\mathcal Q_a$ is zero-neutral on symmetric boxes:
by Lemma~\ref{lem:defect_arg_principle}, the closed-loop winding equals $2\pi(N_+(a)-N_-(a))$,
so a symmetric off-axis pair at displacement $\pm a$ contributes no forced winding.
\end{remark}
```

  (iii) revised theorem/inequality lines
```tex
% (None from RH-BRIDGE in this batch; ENVELOPE will insert the chosen defect endpoint inequality.)
```

* Dependencies on other branches:
  - **ENVELOPE** must define the defect endpoint functional (phase increment vs energy) and propagate residual/local bounds without triggering the forbidden endpoint classes.
  - **LOCAL** must control the near-tube set (or prove structural cancellation) at the chosen tube radius \(r\), in a δ-uniform way compatible with \(\delta_0=\eta a/(\log m)^2\).
  - **FORCE** must supply the forceability link for whatever defect endpoint ENVELOPE chooses (or confirm the contradiction remains targeted at an already-forced endpoint).

* Referee risk notes:
  1. **Domain/singularity risk:** \(\mathcal L_a\) requires \(E(v\pm a)\neq 0\) on the contour; this is addressed by demanding κ-admissibility on the **shifted** boxes \(B_\pm(a)\), not only on the central box.
  2. **Branch ambiguity risk:** avoided by defining phase increments via \(\Im\int (f'/f)\) on a zero-free collar (Lemma \ref{lem:defect_collar_safe}).
  3. **Hidden absolute endpoint risk:** Lemma \ref{lem:diff_kernel_bound} provides both a signed phase bound and an optional absolute \(L^2\) bound; ENVELOPE must ensure it does not re-enter a globally rejected absolute-endpoint class unless explicitly allowed for the defect object.
  4. **Forced-zero obstruction:** explicitly neutralized by Lemma \ref{lem:defect_arg_principle} + symmetry (no automatic \(O(1)\) winding from a symmetric quartet).
