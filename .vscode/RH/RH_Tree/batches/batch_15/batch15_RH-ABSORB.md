# Batch 15 — RH-ABSORB
**Focus:** UE‑INPUT (v43) — absorb Archimedean/completion contributions and isolate the genuinely hard “zero kernel” term.  
**Ground truth:** `manuscript_v43.pdf` (locked).  
**Executive outcome class:** **(3) absorption / reduction** (proves the Archimedean piece is harmless; UE‑INPUT reduces to a zero‑kernel bound).

---

## 0) Quick reference (v43 objects)

From v43, we have (centered width‑2 frame) the even entire completion
\[
E(v):=\Xi_2(1+v),\qquad E(v)=E(-v),
\]
and the basic log‑derivative and finite difference operators
\[
f(v):=\frac{E'(v)}{E(v)},\qquad 
\mathcal L_t(v):=f(v+t)-f(v-t),\qquad 
\mathcal D_{a,h}(v):=\mathcal L_{a+h}(v)-\mathcal L_{a-h}(v).
\]
On the hinge circle (GEO‑C4 geometry),
\[
v(\theta)=im+\delta e^{i\theta},\qquad \theta\in[0,2\pi],\qquad h=\kappa\delta,
\]
and the active UE‑INPUT target (v43 Box) is
\[
\boxed{\ \int_0^{2\pi}\big|\mathcal D_{a,h}(v(\theta))\big|\,d\theta \ \le\ C\,
\frac{h(\log(m+3))^{C'}}{a^2}\ },\qquad \delta=\frac{\eta a}{(\log(m+3))^2},\ a\in(0,1).
\]

This note proves that the **Archimedean/completion part** of \(\mathcal D_{a,h}\) satisfies a stronger bound with **room to spare**, so the only hard content of UE‑INPUT is the **\(\zeta'/\zeta\) (zero‑kernel) part**.

---

## 1) Task 1 — Decompose \(f=E'/E\) into completion vs zeta/zero contributions (v‑plane language)

### 1.1 Completed object factorization (exact)
In v43, the width‑2 completion is defined by
\[
\Xi_2(u):=\xi(u/2)=\frac{u(u-2)}{8}\,\Lambda_2(u),
\qquad 
\Lambda_2(u):=\pi^{-u/4}\Gamma(u/4)\zeta(u/2).
\]
Therefore
\[
E(v)=\Xi_2(1+v)=\frac{(1+v)(v-1)}{8}\,\pi^{-(1+v)/4}\Gamma\!\Big(\frac{1+v}{4}\Big)\,
\zeta\!\Big(\frac{1+v}{2}\Big)
=\underbrace{A(v)}_{\text{completion}}\cdot \underbrace{Z(v)}_{\zeta\text{ factor}},
\]
with
\[
A(v):=\frac{v^2-1}{8}\,\pi^{-(1+v)/4}\Gamma\!\Big(\frac{1+v}{4}\Big),\qquad
Z(v):=\zeta\!\Big(\frac{1+v}{2}\Big).
\]

### 1.2 Log‑derivative split (exact, pointwise away from zeros)
On any region where \(E\neq 0\) (in particular on buffered boundaries), we have the **linear split**
\[
f(v)=\frac{E'(v)}{E(v)}=\frac{A'(v)}{A(v)}+\frac{Z'(v)}{Z(v)}=:f^{\rm arch}(v)+f^{\zeta}(v),
\]
where explicitly
\[
f^{\rm arch}(v)=\frac{d}{dv}\log A(v)
=\frac{2v}{v^2-1}-\frac14\log\pi+\frac14\,\psi\!\Big(\frac{1+v}{4}\Big),
\qquad
f^{\zeta}(v)=\frac{d}{dv}\log Z(v)
=\frac12\,\frac{\zeta'}{\zeta}\!\Big(\frac{1+v}{2}\Big),
\]
and \(\psi=\Gamma'/\Gamma\) is the digamma function.

**Comment (referee‑grade):** This is an identity; no RH content. The simple pole of \(\zeta'/\zeta\) at \(s=1\) becomes a pole at \(v=1\) in \(f^{\zeta}\), and it is exactly cancelled by the \(+1/(v-1)\) pole from \(\frac{2v}{v^2-1}=\frac1{v-1}+\frac1{v+1}\) inside \(f^{\rm arch}\), consistent with \(E\) being entire.

### 1.3 Induced decomposition of \(\mathcal L_t\) and \(\mathcal D_{a,h}\) (exact)
Define
\[
\mathcal L^{\rm arch}_t(v):=f^{\rm arch}(v+t)-f^{\rm arch}(v-t),\quad
\mathcal D^{\rm arch}_{a,h}(v):=\mathcal L^{\rm arch}_{a+h}(v)-\mathcal L^{\rm arch}_{a-h}(v),
\]
and similarly \(\mathcal L^\zeta_t,\mathcal D^\zeta_{a,h}\) from \(f^\zeta\).  
By linearity:
\[
\mathcal D_{a,h}(v)=\mathcal D^{\rm arch}_{a,h}(v)+\mathcal D^{\zeta}_{a,h}(v)\quad
\text{(pointwise wherever both sides are defined)}.
\]

---

## 2) Task 2 — Lemma A: Archimedean UE bound with room to spare

### Lemma A (Archimedean UE bound)
Fix \(\kappa\in(0,1)\). There exists an absolute constant \(C_{\rm arch}>0\) such that for all
\[
m\ge 10,\quad a\in(0,1),\quad 0<\delta\le 1,\quad h:=\kappa\delta,
\]
and all \(\theta\in[0,2\pi]\) with \(v(\theta)=im+\delta e^{i\theta}\), one has
\[
\int_0^{2\pi}\big|\mathcal D^{\rm arch}_{a,h}(v(\theta))\big|\,d\theta\ \le\ C_{\rm arch}\,h.
\]
Consequently, under the nominal policy \(\delta=\eta a/(\log(m+3))^2\) (any \(0<\eta\le 1\)), the same bound implies
\[
\int_0^{2\pi}\big|\mathcal D^{\rm arch}_{a,h}(v(\theta))\big|\,d\theta
\ \le\ C_{\rm arch}\,\frac{h(\log(m+3))^{0}}{a^2},
\]
i.e. it satisfies UE‑INPUT with **\(C'=0\)** (strictly stronger than needed).

#### Proof (line‑by‑line skeleton; no handwaving)

**Step 1 (rewrite \(\mathcal D_{a,h}\) as an \(h\)–integral of \(v\)–derivatives).**  
For any differentiable function \(g\),
\[
g(z+h)-g(z-h)=\int_{-h}^{h} g'(z+t)\,dt.
\]
Apply this with \(g=f^{\rm arch}\) at \(z=v+a\) and \(z=v-a\), using the identity
\[
\mathcal D^{\rm arch}_{a,h}(v)
=\big(f^{\rm arch}(v+a+h)-f^{\rm arch}(v+a-h)\big)
+\big(f^{\rm arch}(v-a+h)-f^{\rm arch}(v-a-h)\big),
\]
to obtain
\[
\mathcal D^{\rm arch}_{a,h}(v)
=\int_{-h}^{h}\Big(f^{{\rm arch}\,\prime}(v+a+t)+f^{{\rm arch}\,\prime}(v-a+t)\Big)\,dt.
\]
Therefore, for any such \(v\),
\[
\big|\mathcal D^{\rm arch}_{a,h}(v)\big|
\le \int_{-h}^{h}\Big(\big|f^{{\rm arch}\,\prime}(v+a+t)\big|+\big|f^{{\rm arch}\,\prime}(v-a+t)\big|\Big)\,dt
\le 2h\cdot \sup_{\substack{|t|\le h\\ \sigma\in\{\pm 1\}}}\big|f^{{\rm arch}\,\prime}(v+\sigma a+t)\big|.
\tag{A.1}
\]

**Step 2 (explicit derivative \(f^{{\rm arch}\,\prime}\)).**  
From
\[
f^{\rm arch}(v)=\frac{2v}{v^2-1}-\frac14\log\pi+\frac14\psi\!\Big(\frac{1+v}{4}\Big),
\]
we differentiate:
\[
f^{{\rm arch}\,\prime}(v)
=\frac{d}{dv}\Big(\frac{1}{v-1}+\frac{1}{v+1}\Big)
+\frac14\cdot \frac14\,\psi_1\!\Big(\frac{1+v}{4}\Big)
=-\frac{1}{(v-1)^2}-\frac{1}{(v+1)^2}+\frac{1}{16}\psi_1\!\Big(\frac{1+v}{4}\Big),
\tag{A.2}
\]
where \(\psi_1=\psi'=\Gamma''/\Gamma-(\Gamma'/\Gamma)^2\) is the trigamma function.

**Step 3 (uniform bound on the rational pieces).**  
For \(v=v(\theta)+\sigma a+t\) with \(|t|\le h\le \delta\le 1\), \(|\sigma a|\le 1\), and \(|\Re v(\theta)|\le\delta\le 1\), we have
\[
|\Im v| \ge m-|\Im(\delta e^{i\theta})|\ge m-1\ge 9.
\]
Hence
\[
|v\pm 1|^2 = (\Re v \pm 1)^2 + (\Im v)^2 \ge (m-1)^2 \ge 81,
\]
so
\[
\Big|\frac{1}{(v-1)^2}\Big|+\Big|\frac{1}{(v+1)^2}\Big|
\le \frac{1}{|v-1|^2}+\frac{1}{|v+1|^2}
\le \frac{2}{81}.
\tag{A.3}
\]

**Step 4 (uniform bound on the trigamma piece).**  
Let
\[
z:=\frac{1+v}{4}.
\]
For our region, \(|\Im z|=|\Im v|/4 \ge 9/4\).  
We use the recurrence \(\psi_1(z)=\psi_1(z+1)+1/z^2\) to ensure positive real part:
choose \(M\in\{0,1\}\) so that \(\Re(z+M)\ge 1/4\). Then (for \(\Re w>0\)) the absolutely convergent series
\[
\psi_1(w)=\sum_{n=0}^\infty\frac{1}{(w+n)^2}
\]
implies the bound
\[
|\psi_1(w)|\le \sum_{n=0}^\infty \frac{1}{|w+n|^2}
\le \sum_{n=0}^\infty \frac{1}{(\Re w+n)^2 + (\Im w)^2}
\le \int_0^\infty \frac{dt}{(\Re w+t)^2 + (\Im w)^2} + \frac{1}{(\Re w)^2+(\Im w)^2}.
\]
The integral is \(\le \frac{\pi}{2|\Im w|}\), hence
\[
|\psi_1(w)| \le \frac{\pi}{2|\Im w|}+\frac{1}{(\Im w)^2}
\le \frac{\pi}{2\cdot (9/4)}+\frac{1}{(9/4)^2} < 1.
\]
Now return to \(z\) using the recurrence:
\[
|\psi_1(z)| \le |\psi_1(z+M)| + \frac{1}{|z|^2}
\le 1 + \frac{1}{(\Im z)^2}
\le 1+\frac{1}{(9/4)^2}< 1.2.
\tag{A.4}
\]
Combining (A.2)–(A.4) yields a uniform bound
\[
\sup_{\substack{|t|\le h\\ \sigma\in\{\pm 1\}}}\big|f^{{\rm arch}\,\prime}(v(\theta)+\sigma a+t)\big|
\le \frac{2}{81}+\frac{1}{16}\cdot 1.2
< 0.1.
\tag{A.5}
\]

**Step 5 (finish the \(L^1_\theta\) bound).**  
Insert (A.5) into (A.1) to get
\[
|\mathcal D^{\rm arch}_{a,h}(v(\theta))|
\le 2h \cdot 0.1 = 0.2h \quad\text{for all }\theta.
\]
Integrate over \(\theta\in[0,2\pi]\):
\[
\int_0^{2\pi}|\mathcal D^{\rm arch}_{a,h}(v(\theta))|\,d\theta \le 0.2h\cdot 2\pi \le C_{\rm arch}\,h,
\]
with (for instance) \(C_{\rm arch}=2\). This proves the claim.

\(\square\)

---

## 3) Task 3 — Carrier mode on the hinge circle and k=2 contamination check (interpretive, but with a rigorous bound)

### Claim (Archimedean term is a “k=0 carrier” at GEO‑C4 scale)
Let \(\psi_{\rm arch}(\theta):=\Im\mathcal D^{\rm arch}_{a,h}(v(\theta))\). Then its \(k=2\) Fourier coefficient is \(O(h\delta^2)\), hence the normalized \(k=2\) endpoint contribution is \(o(1)\) under the nominal scale \(\delta=\eta a/\log^2 m\).

#### Proof sketch (rigorous coefficient bound via analyticity)
For fixed \(a,h\), the function \(v\mapsto \mathcal D^{\rm arch}_{a,h}(v)\) is analytic on \(\{v:|v-im|\le 2\}\) for \(m\ge 10\), since its only singularities occur at \(v=\pm 1\) (and the \(\Gamma\) poles on the real axis), all at distance \(\gg m\). Thus, for \(\delta\le 1\), the restriction \(\theta\mapsto \mathcal D^{\rm arch}_{a,h}(im+\delta e^{i\theta})\) has a convergent Fourier–Taylor expansion
\[
\mathcal D^{\rm arch}_{a,h}(im+\delta e^{i\theta})
=\sum_{k\ge 0} c_k\,e^{ik\theta},
\qquad 
c_k=\frac{\delta^k}{k!}\,\partial_v^k\mathcal D^{\rm arch}_{a,h}(im).
\]
Hence the \(k=2\) coefficient satisfies
\[
|c_2|\le \frac{\delta^2}{2}\,\sup_{|v-im|\le 1}\big|\partial_v^2\mathcal D^{\rm arch}_{a,h}(v)\big|.
\tag{A.6}
\]
But \(\mathcal D^{\rm arch}_{a,h}\) is (by Step 1 above) an \(h\)–integral of \(f^{{\rm arch}\,\prime}\), and \(f^{\rm arch}\) is Stirling‑smooth in this region; differentiating under the integral gives
\[
\sup_{|v-im|\le 1}\big|\partial_v^2\mathcal D^{\rm arch}_{a,h}(v)\big|
\ll h\cdot \sup_{|v-im|\le 2}\big|f^{{\rm arch}\,(3)}(v)\big|
\ll h,
\]
where the last bound is uniform for \(m\ge 10\) (all \(v\) are far from the real‑axis poles, and polygamma derivatives are \(O(1)\) on such vertical strips).  
Insert into (A.6): \(|c_2|\ll h\delta^2\).

Now the GEO‑C4 endpoint scales \(\|P_2\psi\|_{L^2}\) by \(\delta^2/h\). Since \(P_2\) extracts the \(k=2\) Fourier component, \(\|P_2\psi_{\rm arch}\|_{L^2}\asymp |c_2|\), hence
\[
\Phi^\star_{\rm arch}\ \asymp\ \frac{\delta^2}{h}\,\|P_2\psi_{\rm arch}\|_{L^2}
\ \ll\ \frac{\delta^2}{h}\cdot h\delta^2\ =\ \delta^4.
\]
Under \(\delta=\eta a/\log^2 m\) with \(a\le 1\), \(\delta^4\to 0\) as \(m\to\infty\), so the Archimedean term cannot generate (or cancel) the forced \(k=2\) signal; it is a negligible “carrier noise floor”.

**Reader‑guide tie‑in (Part III, pages 4–5; interpretive only):** the identities
\(\sin^2\theta=\frac12(1-\cos2\theta)\), \(\cos^2\theta=\frac12(1+\cos2\theta)\)
show that a **\(k=2\)** component is a *second‑order curvature extraction* from smooth carriers (constant + oscillatory split). In this sense, \(\mathcal D^{\rm arch}\) lives primarily in the constant carrier lane (its \(k=2\) component is order \(\delta^2\)), and the harmonic projector \(P_2\) acts analogously to the “lane projectors” (and rectifiers like \(\chi_4\)) by removing dominant non‑oscillatory mass.

---

## 4) Task 4 — UE‑INPUT reduces to the hard “zero kernel” bound (formal corollary)

### Corollary (UE‑INPUT is equivalent to controlling only the \(\zeta'/\zeta\) part)
Let \(\mathcal D_{a,h}=\mathcal D^{\rm arch}_{a,h}+\mathcal D^\zeta_{a,h}\) be the decomposition induced by \(f=f^{\rm arch}+f^\zeta\) above. For \(m\ge 10\) and \(a\in(0,1)\), the following are equivalent up to enlarging the constant \(C\) by an absolute amount:

1. **UE‑INPUT (v43 active box):**
\[
\int_0^{2\pi}|\mathcal D_{a,h}(v(\theta))|\,d\theta \le C\,\frac{h(\log(m+3))^{C'}}{a^2}.
\]

2. **Zero‑kernel UE bound (the genuinely hard part):**
\[
\int_0^{2\pi}|\mathcal D^\zeta_{a,h}(v(\theta))|\,d\theta \le C\,\frac{h(\log(m+3))^{C'}}{a^2}.
\]

#### Proof (one line each direction)
Using the triangle inequality and Lemma A:
\[
\int|\mathcal D|
\le \int|\mathcal D^\zeta|+\int|\mathcal D^{\rm arch}|
\le \int|\mathcal D^\zeta|+C_{\rm arch}h
\le \Big(C + C_{\rm arch}\Big)\frac{h(\log(m+3))^{C'}}{a^2},
\]
since \((\log(m+3))^{C'}/a^2\ge 1\) for \(m\ge 10,a\in(0,1)\).  
The reverse direction is identical (swap roles of \(\mathcal D\) and \(\mathcal D^\zeta\)).

\(\square\)

**Conclusion (sharp):** UE‑INPUT is **equivalent** (up to constants) to a statement about the \(\zeta'/\zeta\) finite‑difference kernel on the shifted traces. There is **no Archimedean obstruction**; all difficulty lies in the zero‑kernel part.

---

## 5) Patch map (v43 → v44)

### 5.1 Where to insert
Recommended insertion in v44 (post‑Batch‑15 ingestion):
- Main text, UE section: immediately **before** the active UE‑INPUT box in §12.2 (or, if v44 keeps UE‑INPUT frozen, insert into the new Appendix “UE Playbook” as an approved decomposition route).

### 5.2 Paste‑ready TeX blocks

#### (i) Definition/decomposition block
```tex
% --- Decomposition: completion vs zeta factor (RH-free) ---
Recall from \S1 that
\[
E(v)=\Xi_2(1+v)
=\frac{v^2-1}{8}\,\pi^{-(1+v)/4}\Gamma\!\Big(\frac{1+v}{4}\Big)\,
\zeta\!\Big(\frac{1+v}{2}\Big)
=:A(v)\,Z(v).
\]
On any region where $E\neq 0$ we have the exact split
\[
f(v):=\frac{E'}{E}(v)=\frac{A'}{A}(v)+\frac{Z'}{Z}(v)=:f^{\rm arch}(v)+f^{\zeta}(v),
\]
where
\[
f^{\rm arch}(v)=\frac{2v}{v^2-1}-\frac14\log\pi+\frac14\psi\!\Big(\frac{1+v}{4}\Big),
\qquad
f^\zeta(v)=\frac12\frac{\zeta'}{\zeta}\!\Big(\frac{1+v}{2}\Big).
\]
Define $\mathcal L_t^{\rm arch},\mathcal D_{a,h}^{\rm arch}$ and $\mathcal L_t^\zeta,\mathcal D_{a,h}^\zeta$
by replacing $f$ with $f^{\rm arch}$ and $f^\zeta$, so that $\mathcal D_{a,h}=\mathcal D^{\rm arch}_{a,h}+\mathcal D^\zeta_{a,h}$.
```

#### (ii) Lemma A (Archimedean absorption)
```tex
\begin{lemma}[Archimedean absorption for UE-INPUT]\label{lem:UE-input-arch}
Fix $\kappa\in(0,1)$. There exists an absolute constant $C_{\rm arch}>0$ such that for all
$m\ge 10$, all $a\in(0,1)$, all $0<\delta\le 1$ with $h=\kappa\delta$, and all hinge circles
$v(\theta)=im+\delta e^{i\theta}$,
\[
\int_0^{2\pi}\big|\mathcal D^{\rm arch}_{a,h}(v(\theta))\big|\,d\theta \le C_{\rm arch}\,h.
\]
In particular, under $\delta=\eta a/(\log(m+3))^2$ this is $\ll h(\log(m+3))^{0}/a^2$.
\end{lemma}
```

#### (iii) Corollary (UE‑INPUT reduces to the zeta/zero part)
```tex
\begin{corollary}[UE-INPUT reduces to a zero-kernel bound]\label{cor:UE-input-zeta}
For $m\ge 10$ and $a\in(0,1)$, UE-INPUT holds (up to enlarging the constant) if and only if
\[
\int_0^{2\pi}\big|\mathcal D^\zeta_{a,h}(v(\theta))\big|\,d\theta \le C\,\frac{h(\log(m+3))^{C'}}{a^2},
\qquad v(\theta)=im+\delta e^{i\theta},\ \delta=\eta a/(\log(m+3))^2.
\]
\end{corollary}
```

#### (iv) Optional remark (carrier mode / k=2 contamination)
```tex
\begin{remark}[Archimedean term does not contaminate the $k=2$ channel]
The function $v\mapsto \mathcal D^{\rm arch}_{a,h}(v)$ is analytic near $v=im$ (for $m\ge 10$), hence
its restriction to the hinge circle has Fourier coefficients $c_k=\delta^k\partial_v^k\mathcal D^{\rm arch}_{a,h}(im)/k!$.
In particular the $k=2$ coefficient is $O(h\delta^2)$, and thus the normalized $k=2$ contribution to
$\Phi^\star$ is $O(\delta^4)=o(1)$ under $\delta=\eta a/\log^2 m$.
\end{remark}
```

---

## 6) Risks / borders / what remains open

1. **This does not prove UE‑INPUT.** It proves UE‑INPUT is equivalent (up to constants) to controlling only the \(\zeta'/\zeta\) finite‑difference term. That is the true frontier.
2. **No RH smuggling:** all steps are explicit factor identities + elementary analytic bounds on rational terms and polygamma; no use of zero location, no “zeros on \(\Re=1/2\)” in definitions.
3. **Boundary buffering not needed for Archimedean bound:** the only poles of \(f^{\rm arch}\) are on the real axis (\(v=\pm1\) and \(\Gamma\) poles), and the hinge traces for \(m\ge 10\) stay at imaginary part \(\asymp m\).
4. **What remains open (sharp):** a proof (or NO‑GO) for the zero‑kernel inequality
\(\int|\mathcal D^\zeta_{a,h}(v(\theta))|\,d\theta \ll h(\log m)^{C'}/a^2\).
This is precisely where Weil/Li phase‑sensitive ideas may become relevant: absolute value \(L^1\) bounds can lose the sign information needed to exploit positivity criteria.

---
