# Batch 12 — RH-FORCE  
**Mission:** Make GEO‑C4 **FORCE** proof‑grade and robust (constant forcing survives remainder + admissibility).  
**Chosen robustness mechanism:** **(A) Pair isolation** (zero‑exclusion in a fixed-radius micro‑disk).

---

## 1) Setup and exact endpoint (TeX-ready)

### 1.1 Frame mapping (no RH-smuggling)

Let \(\rho_s=\beta+i\gamma\) be a nontrivial zero of \(\zeta\) in the \(s\)-frame.  
Define the width‑2 and centered frames
\[
u:=2s,\qquad v:=u-1.
\]
Then \(\rho_s\) maps to
\[
u_\rho=2\rho_s=2\beta+i\,2\gamma,\qquad v_\rho=u_\rho-1=(2\beta-1)+i\,2\gamma.
\]
Write
\[
a:=2\beta-1,\qquad m:=2\gamma,
\]
so “off‑critical‑line” means \(a\neq 0\). A single off‑axis quartet corresponds to zeros of the completed even object \(E(v)\) at
\[
v=\pm a \pm i m,\qquad a>0,\ m>0.
\]

### 1.2 Hinge circle and shift-difference operator

Fix \(m>0\) and \(\delta>0\). Define the **hinge circle**
\[
C_{m,\delta}:=\{v(\theta):= i m+\delta e^{i\theta}:\ \theta\in[0,2\pi]\}.
\]

Let \(E(v)\) denote the completed even entire object in the \(v\)-frame (so \(E(v)=E(-v)=\overline{E(\overline v)}\)).  
Set
\[
F(v):=\frac{E'}{E}(v),
\]
a meromorphic function with simple poles at the zeros of \(E\) (with residue equal to the multiplicity).

Fix \(a>0\) and \(h>0\). Define the 4‑term **shift-difference** (this is the corrected “\(L_{a+h}-L_{a-h}\)” form)
\[
\boxed{\ \mathcal D_{a,h}(v):=
F(v+a+h)-F(v+a-h)+F(v-a+h)-F(v-a-h)\ }.
\]

### 1.3 Shift-admissibility (needed to define \(\arg\) and \(\Im\))

We say \(C_{m,\delta}\) is **\((a,h)\)-shift-admissible** for \(E\) if
\[
E\bigl(v(\theta)\pm a \pm h\bigr)\neq 0\quad\text{for all }\theta\in[0,2\pi],
\]
i.e. none of the four shifted circles intersects the zero set of \(E\).  
This makes \(\mathcal D_{a,h}(v(\theta))\) finite for all \(\theta\).

### 1.4 The GEO‑C4 endpoint (exact normalization)

Define
\[
\psi(\theta):=\Im\bigl(\mathcal D_{a,h}(v(\theta))\bigr),\qquad v(\theta)= i m+\delta e^{i\theta}.
\]

Let \(P_2\) be the **orthogonal projection** on \(L^2([0,2\pi],d\theta)\) onto
\[
\mathrm{span}\{\cos(2\theta),\sin(2\theta)\}.
\]
(So \(P_2\psi(\theta)=A_2\cos(2\theta)+B_2\sin(2\theta)\) with \(A_2,B_2\) given by the usual \(L^2(d\theta)\) inner products.)

Define the endpoint
\[
\boxed{\ \Phi^*(m,a,\delta,h):=\frac{\delta^2}{h}\,\bigl\|P_2\psi\bigr\|_{L^2(0,2\pi)}\ }.
\]

Throughout Batch‑12 we take \(h=\kappa\delta\) with fixed \(\kappa\in(0,1)\).

---

## 2) Toy computation of the forced carrier and \(c_0(\kappa)\)

Assume (for the toy computation) that \(E\) has **exactly** the two upper zeros at
\[
\rho_+:=a+i m,\qquad \rho_-:=-a+i m,
\]
both **simple**, and ignore all other contributions (treated later as remainder).

Then near \(\rho_+\) and \(\rho_-\),
\[
F(z)\approx \frac1{z-\rho_+}\quad\text{or}\quad F(z)\approx\frac1{z-\rho_-}.
\]

For \(v(\theta)= i m+\delta e^{i\theta}\), we have
\[
v(\theta)+a\pm h-\rho_+=\delta e^{i\theta}\pm h,\qquad
v(\theta)-a\pm h-\rho_-=\delta e^{i\theta}\pm h.
\]
Thus the pole contribution to \(\mathcal D_{a,h}(v(\theta))\) is
\[
\mathcal D_{\mathrm{sing}}(\theta)
=\Bigl(\frac1{\delta e^{i\theta}+h}-\frac1{\delta e^{i\theta}-h}\Bigr)
+\Bigl(\frac1{\delta e^{i\theta}+h}-\frac1{\delta e^{i\theta}-h}\Bigr)
=2\Bigl(\frac1{\delta e^{i\theta}+h}-\frac1{\delta e^{i\theta}-h}\Bigr).
\]
A direct algebraic simplification gives
\[
\mathcal D_{\mathrm{sing}}(\theta)=\frac{-4h}{\delta^2e^{2i\theta}-h^2}
=\frac{-4\kappa/\delta}{e^{2i\theta}-\kappa^2}.
\]
Taking imaginary parts and using the convergent Fourier expansion
\[
\frac1{e^{2i\theta}-\kappa^2}
= e^{-2i\theta}\sum_{n\ge 0}\kappa^{2n}e^{-2in\theta},
\qquad (|\kappa|<1),
\]
we obtain
\[
\psi_{\mathrm{sing}}(\theta):=\Im\mathcal D_{\mathrm{sing}}(\theta)
=\frac{4\kappa}{\delta}\Bigl(\sin(2\theta)+\kappa^2\sin(4\theta)+\kappa^4\sin(6\theta)+\cdots\Bigr).
\]
Therefore
\[
P_2\psi_{\mathrm{sing}}(\theta)=\frac{4\kappa}{\delta}\sin(2\theta),
\]
and since \(\|\sin(2\theta)\|_{L^2(0,2\pi)}=\sqrt{\pi}\), we get
\[
\bigl\|P_2\psi_{\mathrm{sing}}\bigr\|_{L^2(0,2\pi)}
=\frac{4\kappa}{\delta}\sqrt{\pi}.
\]
Finally, with \(h=\kappa\delta\),
\[
\boxed{\ \frac{\delta^2}{h}\,\bigl\|P_2\psi_{\mathrm{sing}}\bigr\|_{L^2}
=\frac{\delta^2}{\kappa\delta}\cdot \frac{4\kappa}{\delta}\sqrt{\pi}
=4\sqrt{\pi}.\ }
\]

**Conclusion (normalized constant):** under this exact endpoint definition,
\[
\boxed{\ c_0(\kappa)=4\sqrt{\pi}\ \ \text{(independent of \(\kappa\in(0,1)\)).}\ }
\]
If the upper zeros have multiplicity \(r\ge 1\) each, then \(c_0(\kappa)=4r\sqrt{\pi}\).

---

## 3) FORCE lemma for the true \(E\) (pair-isolation robust)

### 3.1 Local remainder hypothesis (mechanism A)

Fix \(R>1+\kappa\). Define the two disks
\[
D_\pm:=\{z\in\mathbb C:\ |z-(\pm a+i m)|<R\delta\}.
\]

**Pair isolation hypothesis (A):**  
\(E\) has no zeros in \(D_+\cup D_-\) except \(\rho_+=a+i m\) and \(\rho_-=-a+i m\), each of multiplicity \(r\ge 1\).  

Then (by standard local factorization of holomorphic functions) there exist holomorphic, nonvanishing functions \(H_\pm(z)\) on \(D_\pm\) such that
\[
E(z)=(z-\rho_\pm)^r\,H_\pm(z)\quad (z\in D_\pm),
\]
and hence
\[
\frac{E'}{E}(z)=\frac{r}{z-\rho_\pm}+\frac{H_\pm'}{H_\pm}(z)\quad (z\in D_\pm).
\]

Define the **analytic remainders**
\[
G_\pm(z):=\frac{H_\pm'}{H_\pm}(z)\quad (z\in D_\pm),
\]
and let
\[
M:=\max\Bigl\{\sup_{z\in D_+}|G_+(z)|,\ \sup_{z\in D_-}|G_-(z)|\Bigr\}.
\]

> In the full program, \(M\) is the only “remainder control” input you need from RH‑LOCAL (see §4).

### 3.2 FORCE lemma (TeX-ready statement)

```tex
\begin{lemma}[GEO--C4 forcing on the hinge circle]\label{lem:geoC4-force}
Fix $\kappa\in(0,1)$ and $R>1+\kappa$.
Let $E$ be the completed even entire object in the $v$-frame and set $F:=E'/E$.
Assume there exist $a>0$, $m>0$ such that $E$ has an off-axis quartet of zeros at $v=\pm a\pm i m$,
and assume the hinge circle $C_{m,\delta}=\{i m+\delta e^{i\theta}\}$ is $(a,h)$-shift-admissible
with $h=\kappa\delta$.

Assume moreover (pair isolation) that, for some integer $r\ge 1$, the only zeros of $E$ in the disks
$D_\pm:=\{\,|z-(\pm a+i m)|<R\delta\,\}$ are the two upper zeros $\rho_\pm=\pm a+i m$, each of multiplicity $r$.

Define
\[
\mathcal D_{a,h}(v):=
F(v+a+h)-F(v+a-h)+F(v-a+h)-F(v-a-h),
\qquad
\psi(\theta):=\Im\bigl(\mathcal D_{a,h}(i m+\delta e^{i\theta})\bigr),
\]
let $P_2$ be orthogonal projection in $L^2([0,2\pi],d\theta)$ onto $\mathrm{span}\{\cos(2\theta),\sin(2\theta)\}$,
and set
\[
\Phi^*(m,a,\delta,h):=\frac{\delta^2}{h}\,\|P_2\psi\|_{L^2(0,2\pi)}.
\]

Then
\[
\Phi^*(m,a,\delta,h)\ \ge\ c_0(r)\ -\ \Err,
\qquad c_0(r):=4r\sqrt{\pi},
\]
where the error satisfies
\[
\Err\ \le\ C(\kappa,R)\,\delta\, M,
\qquad
C(\kappa,R):=\frac{4\sqrt{\pi}}{R^3}\cdot
\frac{3+(\kappa/R)^2}{\bigl(1-(\kappa/R)^2\bigr)^3}.
\]
In particular, for simple zeros ($r=1$), $c_0=4\sqrt{\pi}$.
\end{lemma}
```

### 3.3 Proof (line-by-line)

**Proof.** Fix \(\kappa\in(0,1)\), \(R>1+\kappa\), and set \(h=\kappa\delta\).

**Step 1 (decompose \(F=E'/E\) locally).**  
By pair isolation, the factorization
\[
E(z)=(z-\rho_\pm)^r H_\pm(z)
\]
holds on each \(D_\pm\) with \(H_\pm\) holomorphic and nonzero. Therefore
\[
F(z)=\frac{E'}{E}(z)=\frac{r}{z-\rho_\pm}+G_\pm(z),
\qquad G_\pm:=H_\pm'/H_\pm,
\]
on \(D_\pm\), with \(|G_\pm(z)|\le M\) there by definition.

**Step 2 (the shifted evaluation points lie in \(D_\pm\)).**  
For \(v(\theta)= i m+\delta e^{i\theta}\) we have
\[
v(\theta)\pm a\pm h-(\pm a+i m)=\delta e^{i\theta}\pm h,
\]
so
\[
\bigl|v(\theta)\pm a\pm h-(\pm a+i m)\bigr|\le \delta+h=(1+\kappa)\delta<R\delta.
\]
Hence all four points \(v(\theta)\pm a\pm h\) lie in \(D_+\cup D_-\), and the local expansions for \(F\) apply.

**Step 3 (split \(\mathcal D_{a,h}\) into singular + remainder).**  
Write \(\mathcal D_{a,h}=\mathcal D_{\mathrm{sing}}+\mathcal D_{\mathrm{rem}}\), where \(\mathcal D_{\mathrm{sing}}\) collects
the pole terms from \(\rho_\pm\), and \(\mathcal D_{\mathrm{rem}}\) collects the analytic remainders \(G_\pm\):
\[
\mathcal D_{\mathrm{sing}}(v)
:=\Bigl(\frac{r}{v+a+h-\rho_+}-\frac{r}{v+a-h-\rho_+}\Bigr)
+\Bigl(\frac{r}{v-a+h-\rho_-}-\frac{r}{v-a-h-\rho_-}\Bigr),
\]
\[
\mathcal D_{\mathrm{rem}}(v)
:=\bigl(G_+(v+a+h)-G_+(v+a-h)\bigr)+\bigl(G_-(v-a+h)-G_-(v-a-h)\bigr).
\]
Then for \(\psi(\theta)=\Im\mathcal D_{a,h}(v(\theta))\),
\[
\psi(\theta)=\psi_{\mathrm{sing}}(\theta)+\psi_{\mathrm{rem}}(\theta),
\qquad
\psi_{\mathrm{sing}}:=\Im\mathcal D_{\mathrm{sing}}(v(\theta)),\ 
\psi_{\mathrm{rem}}:=\Im\mathcal D_{\mathrm{rem}}(v(\theta)).
\]

**Step 4 (compute the forced \(k=2\) carrier exactly).**  
Using \(v(\theta)= i m+\delta e^{i\theta}\) and \(\rho_\pm=\pm a+i m\),
\[
v(\theta)+a\pm h-\rho_+=\delta e^{i\theta}\pm h,\qquad
v(\theta)-a\pm h-\rho_-=\delta e^{i\theta}\pm h.
\]
Therefore
\[
\mathcal D_{\mathrm{sing}}(v(\theta))
=2r\Bigl(\frac{1}{\delta e^{i\theta}+h}-\frac{1}{\delta e^{i\theta}-h}\Bigr)
=\frac{-4r h}{\delta^2e^{2i\theta}-h^2}.
\]
As in §2, this implies
\[
P_2\psi_{\mathrm{sing}}(\theta)=\frac{4r h}{\delta^2}\sin(2\theta),
\]
hence
\[
\|P_2\psi_{\mathrm{sing}}\|_{L^2(0,2\pi)}=\frac{4r h}{\delta^2}\,\|\sin(2\theta)\|_{L^2}
=\frac{4r h}{\delta^2}\sqrt{\pi}.
\]
Multiplying by \(\delta^2/h\) gives
\[
\frac{\delta^2}{h}\,\|P_2\psi_{\mathrm{sing}}\|_{L^2}=4r\sqrt{\pi}=c_0(r).
\]

**Step 5 (bound the \(k=2\) remainder by a local analytic estimate).**  
We bound the \(k=2\) Fourier coefficient of \(\psi_{\mathrm{rem}}\) using only analyticity and the bound \(|G_\pm|\le M\).

Fix the “+” term; the “−” term is identical. Consider the analytic function on \(D_+\),
\[
g_+(z):=G_+(z),\qquad |g_+(z)|\le M\ \ (z\in D_+).
\]
Define \(w=\delta e^{i\theta}\) and consider
\[
R_+(\theta):=g_+(a+i m+w+h)-g_+(a+i m+w-h).
\]
Because \(|w\pm h|\le (1+\kappa)\delta<R\delta\), both arguments lie in \(D_+\), so \(R_+\) is well-defined.

Expand \(g_+\) into a Taylor series about \(a+i m\):
\[
g_+(a+i m+z)=\sum_{n\ge 0} c_n z^n\quad\text{for }|z|<R\delta,
\]
with Cauchy bounds
\[
|c_n|\le \frac{M}{(R\delta)^n}\quad (n\ge 0).
\]
Then
\[
R_+(\theta)=\sum_{n\ge 0} c_n\bigl((w+h)^n-(w-h)^n\bigr).
\]
The coefficient of \(e^{2i\theta}\) in \(R_+(\theta)\) equals the coefficient of \(w^2\) in this series, hence
\[
\mathrm{coeff}_{e^{2i\theta}}(R_+)
=\delta^2\sum_{\substack{n\ge 3\\ n\ \mathrm{odd}}} c_n\,n(n-1)\,h^{n-2}.
\]
Taking absolute values and using \(|c_n|\le M/(R\delta)^n\) and \(h=\kappa\delta\) yields
\[
\bigl|\mathrm{coeff}_{e^{2i\theta}}(R_+)\bigr|
\le \delta^2\sum_{\substack{n\ge 3\\ n\ \mathrm{odd}}} \frac{M}{(R\delta)^n}\,n(n-1)\,(\kappa\delta)^{n-2}
= M\sum_{\substack{n\ge 3\\ n\ \mathrm{odd}}} n(n-1)\,\frac{\kappa^{n-2}}{R^n}.
\]
A closed-form evaluation of this odd series gives
\[
\sum_{\substack{n\ge 3\\ n\ \mathrm{odd}}} n(n-1)\,\frac{\kappa^{n-2}}{R^n}
=\frac{2\kappa}{R^3}\cdot\frac{3+(\kappa/R)^2}{\bigl(1-(\kappa/R)^2\bigr)^3}.
\]
Therefore
\[
\bigl|\mathrm{coeff}_{e^{2i\theta}}(R_+)\bigr|
\le M\cdot \frac{2\kappa}{R^3}\cdot\frac{3+(\kappa/R)^2}{\bigl(1-(\kappa/R)^2\bigr)^3}.
\]
Since \(\psi_{\mathrm{rem}}=\Im(R_+)+\Im(R_-)\) is real-valued, its \(k=2\) projection has \(L^2\) norm bounded by
\[
\|P_2\psi_{\mathrm{rem}}\|_{L^2(0,2\pi)}
\le \sqrt{\pi}\cdot \Bigl|\mathrm{coeff}_{e^{2i\theta}}(R_+)+\mathrm{coeff}_{e^{2i\theta}}(R_-)\Bigr|
\le 2\sqrt{\pi}\,M\cdot \frac{2\kappa}{R^3}\cdot\frac{3+(\kappa/R)^2}{\bigl(1-(\kappa/R)^2\bigr)^3}.
\]
Multiplying by \(\delta^2/h=\delta/(\kappa)\) gives
\[
\frac{\delta^2}{h}\,\|P_2\psi_{\mathrm{rem}}\|_{L^2}
\le \delta\,M\cdot \frac{4\sqrt{\pi}}{R^3}\cdot\frac{3+(\kappa/R)^2}{\bigl(1-(\kappa/R)^2\bigr)^3}
=: \Err.
\]

**Step 6 (finish by triangle inequality).**  
By linearity of \(P_2\) and the triangle inequality in \(L^2\),
\[
\|P_2\psi\|_{L^2}
\ge \|P_2\psi_{\mathrm{sing}}\|_{L^2}-\|P_2\psi_{\mathrm{rem}}\|_{L^2}.
\]
Multiply by \(\delta^2/h\) and insert the bounds from Steps 4–5:
\[
\Phi^*(m,a,\delta,h)
\ge c_0(r)-\Err,
\]
with \(c_0(r)=4r\sqrt{\pi}\) and \(\Err\) as displayed.  \(\square\)

---

## 4) Exactly what is needed from RH‑LOCAL (single lemma)

To turn Lemma \(\ref{lem:geoC4-force}\) into a usable forcing module, the only “external” input is the ability to **verify or guarantee** the pair isolation hypothesis (and thereby obtain a usable bound \(M\)) at the program’s \(\delta\)-scale.

A minimal RH‑LOCAL deliverable is:

```tex
\begin{lemma}[Local pair isolation / remainder bound needed for GEO--C4]\label{lem:local-geoC4-remainder}
Fix $\kappa\in(0,1)$ and $R>1+\kappa$.
Assume an off-axis quartet exists at $v=\pm a\pm i m$ with $a>0$.
Let $\delta=\delta_0(m,a)$ be the program's micro-scale and $h=\kappa\delta$.

Then either:
(i) (pair isolation) the only zeros of $E$ in $D_\pm=\{|z-(\pm a+i m)|<R\delta\}$ are $\rho_\pm=\pm a+i m$, and
\[
\sup_{z\in D_\pm}\Bigl|\frac{E'}{E}(z)-\frac{r}{z-\rho_\pm}\Bigr|\ \le\ A\log(m+2)+B,
\]
with absolute constants $A,B$, or
(ii) else the manuscript must treat the additional zeros in $D_\pm$ as part of the contradiction mechanism
(because the GEO--C4 carrier need not be stable under arbitrary micro-clustering).
\end{lemma}
```

*Referee note:* If RH‑LOCAL can only prove a weaker “\(N_{\rm eff}\)” weighted bound rather than strict pair isolation,
Lemma \(\ref{lem:geoC4-force}\) can be re-run with an explicit \(\Err\) depending on that weighted count; but without **some**
quantitative exclusion of micro‑clustering at scale \(\asymp \delta\), a uniform positive forcing constant cannot be certified.

---

## 5) Mandatory S6 harness cross-check (explicit-formula interpretation)

### 5.1 Correct scaling language

An off-axis zero \(\rho_s=\beta+i\gamma\) maps to \(v_\rho=(2\beta-1)+i\,2\gamma=a+i m\).  
Thus \(a=2\beta-1\) and \(m=2\gamma\) throughout.

### 5.2 Does the forcing constant correspond to an \(x^\beta\) amplitude leak?

**Yes, indirectly.** The GEO‑C4 forcing detects (via a local pole fingerprint in \(E'/E\)) the existence of a zero with \(\Re(v)=a>0\),
equivalently \(\beta=\tfrac12+\tfrac{a}{2}>1/2\) in the \(s\)-frame. In the explicit formula for \(\psi(x)\) (Chebyshev),
each such zero contributes an oscillatory term of size
\[
\frac{x^{\beta}}{\rho_s}\ \asymp\ x^{1/2+a/2}\quad (\text{up to log factors and phase } \gamma\log x),
\]
i.e. an **amplitude leak** beyond the square-root barrier. The endpoint \(\Phi^*\) is not itself an \(x\)-space observable,
but it is a **local analytic diagnostic** that would certify the existence of precisely the poles that generate the \(x^{\beta}\) leak.

---

# MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* **Callsign:** RH-FORCE  
* **Result classification:** **CONDITIONAL** (proof-grade given pair isolation + remainder bound; unconditional status depends on RH‑LOCAL)  
* **Target gaps closed (by ID):** **OPEN-GEO / GEO‑C4‑FORCE** (forcing constant and robustness estimate for \(\Phi^*\))  
* **Target gaps still open (by ID):** Local remainder control for micro-disks (**RH‑LOCAL dependency**; see Lemma \(\ref{lem:local-geoC4-remainder}\))  
* **Key conclusions (≤5 bullets):**
  1. Under the exact endpoint definition \(\Phi^*=\frac{\delta^2}{h}\|P_2\psi\|_{L^2(d\theta)}\), the forced constant is \(c_0(\kappa)=4\sqrt{\pi}\) (independent of \(\kappa\)) for simple upper zeros; multiplicity \(r\) scales \(c_0\) to \(4r\sqrt{\pi}\).
  2. The forced singular contribution produces a **pure \(k=2\) carrier** after \(P_2\), eliminating the micro-step “absolute forcing kills” pathology.
  3. With pair isolation on disks of radius \(R\delta\) (any \(R>1+\kappa\)), the \(k=2\) remainder is bounded by an explicit \(\Err \le C(\kappa,R)\delta M\), hence is \(o(1)\) under the program’s \(\delta\)-policy provided \(M\lesssim \log m\).
  4. The only nontrivial external requirement is a proof-grade local lemma supplying pair isolation (or an equivalent quantitative anti-clustering bound) plus a bound on the analytic remainder \(M\).
  5. Explicit-formula meaning: the forced carrier detects the poles corresponding to off-line zeros, hence indirectly detects an \(x^\beta\) amplitude leak.

* **Paste-ready manuscript edits:**
  (i) **Revised lemma/proposition statements:** Insert Lemma \(\ref{lem:geoC4-force}\) exactly as in §3.2.  
  (ii) **Revised definitions/remarks:** Insert Definitions §1.2–§1.4 (hinge circle, \((a,h)\)-shift-admissibility, \(\mathcal D_{a,h}\), \(P_2\), \(\Phi^*\)).  
  (iii) **Revised theorem/inequality lines:** None in this batch (this is the forcing module; downstream budget/tail inequalities will reference \(c_0=4\sqrt{\pi}\) once the contradiction chain chooses the normalization).  

* **Dependencies on other branches:** **RH‑LOCAL** must supply Lemma \(\ref{lem:local-geoC4-remainder}\) (or a stronger variant) to remove conditionality.  
* **Referee risk notes (anticipated objections + how addressed):**
  1. **Normalization ambiguity:** fixed explicitly by declaring \(L^2\) is on \([0,2\pi]\) with measure \(d\theta\) and \(P_2\) is the \(L^2\)-orthogonal projection.
  2. **Micro-clustering/cancellation risk:** addressed by making pair isolation an explicit hypothesis; without it the carrier need not be stable.
  3. **Analytic remainder bound \(M\):** isolated as the single quantitative input needed from RH‑LOCAL; the forcing proof itself uses only holomorphic factorization + Fourier coefficient bounds.
