# Batch 12 — RH‑ENVELOPE  
**Callsign:** RH‑ENVELOPE  
**Mission:** Close the **UE‑INPUT brick** for **GEO‑C4** (harmonic endpoint on hinge‑circle).  
**Route chosen:** **Route B (IBP / derivative UE)** (as preferred in the prompt).

## 0) Executive verdict (decision‑grade)

**Result:** **CONDITIONAL**.

* The **reduction UE ⇒ UE‑INPUT is proof‑grade**: the endpoint \(\Phi^*\) is controlled by explicit \(\delta\)-powers times sup‑bounds for \((E'/E)''\) and \((E'/E)'''\) on a concrete union of shifted hinge circles.  
* The **archimedean / completion part** of \((E'/E)^{(j)}\) is **RH‑free and harmless** (Stirling gives decay for \(j\ge 1\)).  
* The remaining contribution is a **local reciprocal‑power sum over zeros**. In the regime \(\delta=\eta a/\log^2(m+3)\), the bound \(\Phi^*=o(1)\) is equivalent to showing that this local reciprocal‑power sum does **not** reach the “\(\delta^{-3}\)” scale; but a single zero in the target configuration produces exactly that scale.  
* Therefore the **single missing sub‑inequality** is isolated precisely (Section 4.3): it is a local‑window “cubic (and quartic) reciprocal sum” bound that rules out \(\delta\)-scale proximity of zeros to the shifted hinge circles. Proving it RH‑free would essentially *be* the RH‑exclusion step.

This response provides:  
(1) a clean **UE‑INPUT lemma** (derivative‑field form),  
(2) a line‑by‑line reduction from \(\Phi^*\) to UE‑INPUT,  
(3) the maximal RH‑free proof progress (archimedean + far‑zeros), and  
(4) the **single missing inequality**, with a toy‑model obstruction.

---

## 1) GEO‑C4 objects (as locked target)

Frames: \(u=2s\), \(v=u-1\). An off‑axis zero \(s=\beta+i\gamma\) corresponds to  
\[
v = a + i m,\qquad a=2\beta-1,\quad m=2\gamma.
\]

Assume \(E(v)\) is the **even entire** completion in \(v\)-coordinates (e.g. \(E(v)=\Xi_2(1+v)=\xi((1+v)/2)\)), so \(E(v)=E(-v)\) and zeros occur in quartets \(\pm a\pm i m\).

Operators:
\[
\mathcal L_t(v)=\frac{E'}{E}(v+t)-\frac{E'}{E}(v-t),\qquad
\mathcal D_{a,h}(v)=\mathcal L_{a+h}(v)-\mathcal L_{a-h}(v).
\]

Hinge circle:
\[
C_{m,\delta}:\ v(\theta)= i m + \delta e^{i\theta},\qquad \theta\in[0,2\pi].
\]

Phase signal and endpoint:
\[
\psi_{a,h}(\theta):=\Im(\mathcal D_{a,h}(v(\theta))),\qquad
\Phi^*(m,a,\delta,h)=\frac{\delta^2}{h}\,\bigl\|P_2\psi_{a,h}\bigr\|_{L^2([0,2\pi])},
\]
where \(P_2\) is orthogonal projection onto \(\mathrm{span}\{\cos(2\theta),\sin(2\theta)\}\).

Coupling: \(h=\kappa\delta\), fixed \(\kappa\in(0,1)\) (use \(\kappa=1/2\) unless changed).  
Nominal policy: \(\displaystyle \delta=\eta\,\frac{a}{\log^2(m+3)}\).

---

## 2) Harmonic extraction: \(P_2\) controlled by \(\theta\)-derivatives (proof‑grade)

### Lemma 2.1 (Fourier/IBP inequality for the \(k=2\) mode)
Let \(f\in H^2(\mathbb T)\) be \(2\pi\)-periodic. Then
\[
\|P_2 f\|_{L^2([0,2\pi])}\ \le\ \frac14\,\|f''\|_{L^2([0,2\pi])}.
\]

**Proof (Fourier, 4 lines).** Write \(f(\theta)=\sum_{k\in\mathbb Z}\widehat f(k)e^{ik\theta}\), so \(f''(\theta)=\sum (-k^2)\widehat f(k)e^{ik\theta}\). Then \(\widehat{f''}(2)=-4\widehat f(2)\) and \(\widehat{f''}(-2)=-4\widehat f(-2)\). Parseval gives
\[
\|P_2 f\|_2^2 = 2\pi\big(|\widehat f(2)|^2+|\widehat f(-2)|^2\big)
\le \frac1{16}\,2\pi\big(|\widehat{f''}(2)|^2+|\widehat{f''}(-2)|^2\big)
\le \frac1{16}\|f''\|_2^2.
\]
Taking square roots yields the claim. \(\square\)

---

## 3) Chain rule on the hinge circle (explicit \(\delta\)-powers)

Let \(H\) be complex‑differentiable in a neighborhood of \(C_{m,\delta}\), and define
\[
g(\theta):=H(v(\theta)),\qquad v(\theta)=im+\delta e^{i\theta}.
\]
Then \(v'(\theta)=i\delta e^{i\theta}\) and \(v''(\theta)=-\delta e^{i\theta}\). Hence
\[
g'(\theta)=H'(v(\theta))\,v'(\theta),\qquad
g''(\theta)=H''(v(\theta))\,(v'(\theta))^2 + H'(v(\theta))\,v''(\theta).
\]
Taking absolute values,
\[
|g''(\theta)|\ \le\ \delta^2\,|H''(v(\theta))| + \delta\,|H'(v(\theta))|.
\]

Applying this to \(H=\mathcal D_{a,h}\) and \(\psi(\theta)=\Im(H(v(\theta)))\), we have \(|\psi''|\le |g''|\), hence
\[
\|\psi''\|_{L^2}\ \le\ \sqrt{2\pi}\,\sup_{v\in C_{m,\delta}}\Big(\delta\,|\mathcal D_{a,h}'(v)|+\delta^2\,|\mathcal D_{a,h}''(v)|\Big).
\]

Combining with Lemma 2.1,
\[
\|P_2\psi\|_{L^2}\ \le\ \frac14\|\psi''\|_{L^2}
\ \le\ \frac{\sqrt{2\pi}}{4}\,\sup_{v\in C_{m,\delta}}\Big(\delta\,|\mathcal D_{a,h}'(v)|+\delta^2\,|\mathcal D_{a,h}''(v)|\Big).
\]

Multiplying by \(\delta^2/h\), we obtain the core reduction:
\[
\Phi^*(m,a,\delta,h)
\ \le\ \frac{\sqrt{2\pi}}{4}\,\left(\frac{\delta^3}{h}\sup_{C_{m,\delta}}|\mathcal D_{a,h}'|
+\frac{\delta^4}{h}\sup_{C_{m,\delta}}|\mathcal D_{a,h}''|\right).
\tag{UE‑RED}
\]

---

## 4) Factor out one \(h\) and reduce to bounds on \((E'/E)''\), \((E'/E)'''\)

Write \(F(v):=E'(v)/E(v)\). Then
\[
\mathcal L_t(v)=F(v+t)-F(v-t),\qquad
\mathcal D_{a,h}(v)=\mathcal L_{a+h}(v)-\mathcal L_{a-h}(v)=\int_{a-h}^{a+h}\partial_t\mathcal L_t(v)\,dt.
\]

Differentiate explicitly:
\[
\partial_v\mathcal L_t(v)=F'(v+t)-F'(v-t),\qquad
\partial_t\partial_v\mathcal L_t(v)=F''(v+t)+F''(v-t).
\]
Similarly,
\[
\partial_v^2\mathcal L_t(v)=F''(v+t)-F''(v-t),\qquad
\partial_t\partial_v^2\mathcal L_t(v)=F'''(v+t)+F'''(v-t).
\]

Therefore:
\[
\mathcal D_{a,h}'(v)
=\int_{a-h}^{a+h}\partial_t\partial_v\mathcal L_t(v)\,dt
=\int_{a-h}^{a+h}\big(F''(v+t)+F''(v-t)\big)\,dt,
\]
\[
\mathcal D_{a,h}''(v)
=\int_{a-h}^{a+h}\partial_t\partial_v^2\mathcal L_t(v)\,dt
=\int_{a-h}^{a+h}\big(F'''(v+t)+F'''(v-t)\big)\,dt.
\]

Hence, for any \(v\),
\[
|\mathcal D_{a,h}'(v)|\le 2h\,M_2,\qquad
|\mathcal D_{a,h}''(v)|\le 2h\,M_3,
\]
where the derivative‑field suprema are
\[
M_2:=\sup_{\substack{t\in[a-h,a+h]\\ v\in C_{m,\delta}}}\max\{|F''(v+t)|,|F''(v-t)|\},
\qquad
M_3:=\sup_{\substack{t\in[a-h,a+h]\\ v\in C_{m,\delta}}}\max\{|F'''(v+t)|,|F'''(v-t)|\}.
\]

Plugging these into (UE‑RED), the \(h\) cancels:

### Proposition 4.1 (UE reduction to a derivative‑field input)
Assume \(F''\) and \(F'''\) are finite on the shifted traces \(C_{m,\delta}\pm t\) for \(t\in[a-h,a+h]\) (e.g. \(E\neq 0\) on those traces). Then
\[
\Phi^*(m,a,\delta,h)\ \le\ C_\mathrm{UE}\,\big(\delta^3\,M_2+\delta^4\,M_3\big),
\qquad
C_\mathrm{UE}:=\frac{\sqrt{2\pi}}{2}.
\tag{UE→INPUT}
\]

**Interpretation.** The endpoint \(\Phi^*\) has been reduced to **one** analytic object: a uniform bound on \((E'/E)''\) and \((E'/E)'''\) along a concrete union of shifted hinge circles.

---

### 4.2 UE‑INPUT lemma (paste‑ready target)

The cleanest “brick” version is:

> **UE‑INPUT (GEO‑C4).**  
> Fix \(\kappa\in(0,1)\) and \(\eta\in(0,1)\). For all \(m\ge 10\), \(a\in(0,1]\), let  
> \[
> \delta=\eta\,\frac{a}{\log^2(m+3)},\qquad h=\kappa\delta,
> \]
> and define \(C_{m,\delta}\) as above. Assume \(E\) is even entire and \(E\neq 0\) on the shifted traces \(C_{m,\delta}\pm t\) for every \(t\in[a-h,a+h]\).  
> Then there exist constants \(A_2,A_3>0\) independent of \((m,a,\delta)\) such that
> \[
> M_2\ \le\ \frac{A_2(\log(m+3))^{u_2}}{a^3},\qquad
> M_3\ \le\ \frac{A_3(\log(m+3))^{u_3}}{a^4},
> \tag{UE‑INPUT}
> \]
> for fixed exponents \(u_2,u_3\) (preferably small integers).
>
> Consequently, \(\Phi^*(m,a,\delta,h)=o(1)\) as \(m\to\infty\), uniformly in \(a\in(0,1]\).

**Why the \(a^{-3},a^{-4}\) scaling?** If all nontrivial zeros satisfy \(\Re(v_\rho)=0\), then every point on \(C_{m,\delta}\pm t\) has real part \(\pm t + O(\delta)\) with \(t\asymp a\), and thus sits at distance \(\gtrsim a\) from every local-window zero. Then \(F^{(j)}\) is dominated by sums of \(\asymp a^{-(j+1)}\).

---

### 4.3 What remains: the single missing inequality (explicitly)

Using the Hadamard product / partial fraction expansion for an even entire function of order 1 (as for \(\Xi_2\)), one has schematically
\[
F^{(2)}(w)\ =\ O(1)\ +\sum_{\rho\in Z(E)}\frac{2}{(w-\rho)^3},
\qquad
F^{(3)}(w)\ =\ O(1)\ +\sum_{\rho\in Z(E)}\frac{6}{(w-\rho)^4},
\]
where the \(O(1)\) comes from the exponential prefactor and the archimedean completion terms.

Thus UE‑INPUT is equivalent to the following **local reciprocal‑power sum bound** on the shifted traces:

> **Missing sub‑inequality (the only real blocker).**  
> Show that for \(w\) ranging over
> \[
> \Omega_{m,a,\delta,h}:=\bigcup_{t\in[a-h,a+h]}\big(C_{m,\delta}+t\big)\ \cup\ \big(C_{m,\delta}-t\big),
> \]
> one has
> \[
> \sup_{w\in\Omega_{m,a,\delta,h}}\ \sum_{\rho\in Z(E)}\frac{1}{|w-\rho|^3}
> \ \ll\ \frac{(\log(m+3))^{u_2}}{a^3},
> \quad
> \sup_{w\in\Omega_{m,a,\delta,h}}\ \sum_{\rho\in Z(E)}\frac{1}{|w-\rho|^4}
> \ \ll\ \frac{(\log(m+3))^{u_3}}{a^4},
> \tag{★}
> \]
> with implied constants independent of \((m,a,\delta)\).

This is the brick that—if proved RH‑free—would imply the desired UE shrink \(\Phi^*=o(1)\) by Proposition 4.1.

---

## 5) RH‑free proof progress toward UE‑INPUT

### 5.1 Completion / archimedean terms (Stirling ⇒ harmless)
For the \(\Xi_2\) (or \(\xi\)) completion, \(F(v)\) is (up to a factor \(1/2\)) the log‑derivative of \(\xi(s)\) with \(s=(1+v)/2\). The gamma/digamma terms satisfy:

* \(\psi(z)=\log z+O(1/|z|)\) as \(|z|\to\infty\) in \(|\arg z|\le \pi-\epsilon\).  
* For \(n\ge 1\), \(\psi^{(n)}(z)=O_n(|z|^{-n})\).

With \(z=s/2\) and \(|\Im s|\asymp m\), this yields:
\[
\text{for }j\ge 1,\quad \partial_v^j\Big(\text{gamma part of }F(v)\Big)=O_j(m^{-j}).
\]
So gamma‑part contributions to \(M_2,M_3\) are \(O(m^{-2})\) and \(O(m^{-3})\), hence negligible.

### 5.2 Far‑height zeros are harmless (zero counting ⇒ \(O(\log m)\))
Fix \(w\) with \(\Im w\in[m-\delta,m+\delta]\) and \(|\Re w|\le 2\) (true for \(\Omega_{m,a,\delta,h}\) since \(a\le 1\), \(\delta\ll 1\)). Partition zeros by vertical distance:
\[
\mathcal Z_n := \{\rho\in Z(E): n\le |\Im\rho-m|<n+1\},\qquad n\ge 1.
\]
Then \(|w-\rho|\ge n\), so
\[
\sum_{\rho\in\mathcal Z_n}\frac{1}{|w-\rho|^3}\ \le\ \frac{|\mathcal Z_n|}{n^3},\qquad
\sum_{\rho\in\mathcal Z_n}\frac{1}{|w-\rho|^4}\ \le\ \frac{|\mathcal Z_n|}{n^4}.
\]
Using the Riemann–von Mangoldt count \(N(T+1)-N(T-1)\ll \log T\) (already present in the lineage as an explicit bound), we have \(|\mathcal Z_n|\ll \log(m+n+3)\). Therefore:
\[
\sum_{n\ge 1}\frac{|\mathcal Z_n|}{n^3}\ll \sum_{n\ge 1}\frac{\log(m+n)}{n^3}\ll \log(m+3),
\]
and similarly the \(n^{-4}\) sum is also \(O(\log m)\).

**Conclusion.** All zeros with \(|\Im\rho-m|\ge 1\) contribute \(O(\log m)\) to \(\sum|w-\rho|^{-3}\) and \(\sum|w-\rho|^{-4}\), uniformly in \(w\in\Omega_{m,a,\delta,h}\).

### 5.3 Local window \(|\Im\rho-m|\le 1\): this is the entire difficulty
Let \(\mathcal Z_{\mathrm{loc}}:=\{\rho:|\Im\rho-m|\le 1\}\). This set is finite and \(|\mathcal Z_{\mathrm{loc}}|\ll \log m\). But without a *lower bound* on \(|w-\rho|\) for \(w\in\Omega_{m,a,\delta,h}\), we cannot control
\[
\sum_{\rho\in\mathcal Z_{\mathrm{loc}}}\frac{1}{|w-\rho|^3}.
\]

* If \(\Re(\rho)=0\) for all \(\rho\in\mathcal Z_{\mathrm{loc}}\) (critical line in \(v\)-frame), then \(|w-\rho|\gtrsim a\) because \(\Re(w)=\pm t+O(\delta)\) with \(t\in[a-h,a+h]\) and \(\delta\ll a\). Hence
  \[
  \sum_{\rho\in\mathcal Z_{\mathrm{loc}}}\frac{1}{|w-\rho|^3}\ \ll\ \frac{|\mathcal Z_{\mathrm{loc}}|}{a^3}\ \ll\ \frac{\log m}{a^3},
  \]
  which is exactly the scaling needed in UE‑INPUT.

* If there exists an off‑axis zero \(\rho=a+im\), then for the shifted trace \(C_{m,\delta}+a\) we have points with \(|w-\rho|\asymp\delta\), giving
  \[
  \sup_{w\in C_{m,\delta}+a}\frac{1}{|w-\rho|^3}\ \asymp\ \delta^{-3},
  \]
  and therefore \(\delta^3 M_2\) is \(\asymp 1\), preventing \(\Phi^*\) from being \(o(1)\).

This is the precise “single‑inequality” bottleneck: proving UE‑INPUT requires an RH‑free mechanism that rules out \(\delta\)-scale proximity of \(\mathcal Z_{\mathrm{loc}}\) to the shifted traces.

---

## 6) Toy model obstruction (why UE‑INPUT is nontrivial)

Take a toy entire function with a single simple zero at \(\rho=a+im\): \(E_\mathrm{toy}(v)=v-\rho\). Then \(F_\mathrm{toy}(v)=1/(v-\rho)\). One computes explicitly that \(\mathcal D_{a,h}(v(\theta))\) contains the pole‑pair contribution
\[
\frac{1}{\delta e^{i\theta}+h}\ -\ \frac{1}{\delta e^{i\theta}-h}
\ =\ -\frac{2h}{\delta^2e^{2i\theta}-h^2},
\]
whose \(\theta\mapsto \Im(\cdot)\) has a nonzero \(k=2\) Fourier component of size \(\asymp h/\delta^2\). Therefore
\[
\Phi^*_\mathrm{toy} \asymp \frac{\delta^2}{h}\cdot \frac{h}{\delta^2}\asymp 1,
\]
independent of \(\delta\). This shows that **no argument based solely on smoothness/size of \(E\)** can force \(\Phi^*=o(1)\); the required input must use a **structural fact about the actual \(\Xi_2\) zero set** that forbids the toy model configuration.

---

## 7) What LOCAL/BRIDGE would need (interface statement)

To make UE‑INPUT provable, some branch must supply a statement of the form:

> **(Shift‑separation lemma, local window).** For the actual \(E=\Xi_2(1+\cdot)\), for every \(m\ge 10\), \(a\in(0,1]\), with \(\delta=\eta a/\log^2(m+3)\), the local window zeros satisfy  
> \[
> \mathrm{dist}\big(\Omega_{m,a,\delta,h},\,\mathcal Z_{\mathrm{loc}}\big)\ \gtrsim\ a
> \]
> (or any condition strong enough to replace \(\delta\) by \(a\) in the local reciprocal sums).

This is **essentially the RH‑exclusion statement** in local form. If a weaker statement exists (e.g., “bad configurations are impossible” by global resonance constraints), it must still imply the cubic reciprocal sum bound (★).

---

## 8) S6 harness cross‑check: explicit formula / amplitude‑leak interpretation

Mapping: \(s=\beta+i\gamma\), \(u=2s\), \(v=u-1=(2\beta-1)+i(2\gamma)=a+im\).  
Off‑axis means \(a>0\iff \beta=\tfrac12+\tfrac a2\).

In the explicit formula, a zero \(s=\beta+i\gamma\) contributes terms of size \(x^\beta\) (more precisely \(x^{\rho}/\rho\) plus conjugate), i.e.
\[
x^\beta = x^{1/2}\cdot x^{a/2}.
\]
Thus an off‑axis zero corresponds to an **amplitude leak factor** \(x^{a/2}\) relative to the critical line baseline.

The defect operators \(\mathcal L_t\) and \(\mathcal D_{a,h}\) compare the log‑derivative field at horizontally shifted points \(v\pm t\) near height \(m\). Heuristically, this is the \(v\)-plane analogue of comparing \(\zeta'/\zeta\) at \(\sigma=\tfrac12\pm \tfrac a2\), which in prime‑sum representations weights primes by \(p^{\pm a/2}\), i.e. precisely the mechanism by which an \(x^{a/2}\) amplitude leak would manifest.

**However:** in the present GEO‑C4 package, the implication “\(\Phi^*\) small \(\Rightarrow\) no \(x^{a/2}\) leak” is **only qualitative** unless FORCE supplies a lemma linking the \(k=2\) harmonic endpoint \(\Phi^*\) to an explicit‑formula witness. At audit level, we should treat the amplitude‑leak link as **consistent but not yet proved**.

---

# MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* **Callsign:** RH‑ENVELOPE  
* **Result classification:** **CONDITIONAL**  
* **Target gaps closed (by ID):** UE‑INPUT brick **reduced to a single explicit analytic inequality** (derivative‑field form) for GEO‑C4.  
* **Target gaps still open (by ID):** UE‑INPUT proof itself remains OPEN; specifically the **local reciprocal‑power sum bound** (★) on \(\Omega_{m,a,\delta,h}\), which appears RH‑strength.  
* **Key conclusions (5 bullets max):**
  1. \(\Phi^*\) admits a clean IBP reduction: \(\Phi^*\ll \delta^3 M_2+\delta^4 M_3\), where \(M_2,M_3\) are suprema of \((E'/E)''\), \((E'/E)'''\) on shifted hinge circles.
  2. Archimedean completion terms contribute \(o(1)\) to \(\Phi^*\) (Stirling ⇒ decay for derivatives).
  3. Zeros with \(|\Im\rho-m|\ge 1\) contribute \(O(\log m)\) to the needed reciprocal‑power sums, hence \(o(1)\) after multiplying by \(\delta^3\) under the nominal policy.
  4. The *only* obstruction is the local window \(|\Im\rho-m|\le 1\): a single zero at \(v=a+im\) forces \(\Phi^*\asymp 1\) (toy model), so proving \(\Phi^*=o(1)\) requires a genuine RH‑strength exclusion mechanism.
  5. GEO‑C4’s UE side is therefore now “truth‑latched”: the UE requirement is a single explicit inequality (★) that cannot be hand‑waved.

* **Paste‑ready manuscript edits:**

  (i) **Revised lemma/proposition statements**

```tex
% --- GEO-C4: harmonic UE input (RH-ENVELOPE) ---

\begin{lemma}[Fourier control of the $k=2$ mode]\label{lem:P2-by-second-derivative}
Let $f\in H^2(\mathbb T)$ be $2\pi$-periodic and let $P_2$ denote orthogonal projection onto
$\mathrm{span}\{\cos(2\theta),\sin(2\theta)\}$. Then
\[
\|P_2 f\|_{L^2([0,2\pi])}\le \frac14\,\|f''\|_{L^2([0,2\pi])}.
\]
\end{lemma}

\begin{proposition}[UE reduction to a derivative-field bound]\label{prop:UE-reduction-derivative-field}
Fix $\kappa\in(0,1)$. Let $m\ge 10$, $a\in(0,1]$, $0<\delta\le 1$, and set $h=\kappa\delta$.
Let $C_{m,\delta}=\{im+\delta e^{i\theta}:\theta\in[0,2\pi]\}$ and define
\[
\mathcal L_t(v)=\frac{E'}{E}(v+t)-\frac{E'}{E}(v-t),\qquad
\mathcal D_{a,h}(v)=\mathcal L_{a+h}(v)-\mathcal L_{a-h}(v).
\]
Assume $E\neq 0$ on $C_{m,\delta}\pm t$ for every $t\in[a-h,a+h]$. Define
\[
M_2:=\sup_{\substack{t\in[a-h,a+h]\\ v\in C_{m,\delta}}}\max\Big\{\Big|\Big(\frac{E'}{E}\Big)''(v+t)\Big|,
\Big|\Big(\frac{E'}{E}\Big)''(v-t)\Big|\Big\},
\]
\[
M_3:=\sup_{\substack{t\in[a-h,a+h]\\ v\in C_{m,\delta}}}\max\Big\{\Big|\Big(\frac{E'}{E}\Big)'''(v+t)\Big|,
\Big|\Big(\frac{E'}{E}\Big)'''(v-t)\Big|\Big\}.
\]
Then the harmonic endpoint
\[
\Phi^*(m,a,\delta,h)=\frac{\delta^2}{h}\,\|P_2\Im(\mathcal D_{a,h}\!\circ v)\|_{L^2([0,2\pi])}
\]
obeys
\[
\Phi^*(m,a,\delta,h)\le C_{\mathrm{UE}}\big(\delta^3 M_2+\delta^4 M_3\big),
\qquad C_{\mathrm{UE}}=\frac{\sqrt{2\pi}}{2}.
\]
\end{proposition}

\begin{lemma}[UE--INPUT for GEO--C4]\label{lem:UE-INPUT-GEO-C4}
Fix $\kappa\in(0,1)$ and $\eta\in(0,1)$. For $m\ge 10$, $a\in(0,1]$, set
\[
\delta=\eta\,\frac{a}{\log^2(m+3)},\qquad h=\kappa\delta.
\]
Assume $E$ is even entire and $E\neq 0$ on $C_{m,\delta}\pm t$ for all $t\in[a-h,a+h]$.
Then there exist constants $A_2,A_3>0$ and exponents $u_2,u_3$ such that
\[
M_2\le \frac{A_2(\log(m+3))^{u_2}}{a^3},\qquad
M_3\le \frac{A_3(\log(m+3))^{u_3}}{a^4}.
\]
Consequently $\Phi^*(m,a,\delta,h)=o(1)$ as $m\to\infty$, uniformly for $a\in(0,1]$.
\end{lemma}
```

  (ii) **Revised definitions/remarks**

```tex
\begin{remark}[What remains OPEN in the GEO--C4 UE]\label{rem:UE-INPUT-open}
Proposition~\ref{prop:UE-reduction-derivative-field} reduces the upper envelope control of the
harmonic endpoint $\Phi^*$ to bounding $(E'/E)''$ and $(E'/E)'''$ on the shifted hinge traces.
The archimedean completion terms are RH--free and negligible for these derivatives (Stirling).
The only nontrivial part is the local reciprocal--power sum over zeros in the window
$|\Im\rho-m|\le 1$; a single zero at $v=a+im$ forces $M_2\asymp \delta^{-3}$ and hence
$\Phi^*\asymp 1$ (toy-model obstruction). Any RH--free proof of Lemma~\ref{lem:UE-INPUT-GEO-C4}
must therefore supply a structural mechanism that rules out this $\delta$--scale proximity.
\end{remark}
```

  (iii) **Revised theorem/inequality lines**

```tex
% In the GEO-C4 contradiction budget, replace informal UE lines by:
By Proposition~\ref{prop:UE-reduction-derivative-field} and Lemma~\ref{lem:UE-INPUT-GEO-C4},
the harmonic endpoint satisfies $\Phi^*(m,a,\delta,h)=o(1)$ under the nominal policy
$\delta=\eta a/\log^2(m+3)$, uniformly in $a\in(0,1]$.
```

* **Dependencies on other branches:**
  - To turn CONDITIONAL → PASS, some branch must prove the **local reciprocal‑power sum bound** (★) for the actual \(\Xi_2\) zeros (or an equivalent “no \(\delta\)-scale local proximity” statement), without RH smuggling. This is a LOCAL/BRIDGE‑type obligation, not ENVELOPE algebra.

* **Referee risk notes (anticipated objections + how addressed):**
  1. **Objection:** “You assumed away zeros by requiring \(E\neq 0\) on shifted traces.”  
     **Response:** This is only boundary well‑posedness. It is standard to shrink \(\delta\) slightly (isolated zeros) to avoid boundary hits; the key difficulty is not boundary contact but the size of \(F^{(2)},F^{(3)}\) caused by interior zeros.
  2. **Objection:** “UE‑INPUT looks RH‑equivalent.”  
     **Response:** Yes; the toy model demonstrates that proving \(\Phi^*=o(1)\) forces a structural exclusion of the target local configuration. This response truth‑latches that fact and isolates the single missing inequality.
  3. **Objection:** “Where do the \(\delta\)-powers come from; are constants \(\delta\)-uniform?”  
     **Response:** The \(\delta\)-powers are explicit from chain rule and the \(k=2\) Fourier bound; constants depend only on \(\kappa\) and universal Fourier constants, not on \((m,a,\delta)\).
