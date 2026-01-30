# batch15_RH-FORCE.md

## Executive verdict

**Outcome (2) NO‑GO for v43 UE‑INPUT (L¹ absolute value): PASS.**  
Given locked GEO‑C4 forcing, **any** RH‑free proof of the v43 absolute‑value bound would immediately exclude an off‑axis quartet (hence would be RH‑strength). This is exactly why UE‑INPUT is “hard”.

**Outcome (3) replacement interface (signed k=2 coefficient): CONDITIONAL (interface proposed + reduction proved).**  
I provide a **strictly weaker** UE interface (signed k=2 Fourier coefficient of the defect), and a **proof‑grade reduction** from that signed bound to the smallness of \(\Phi^\star\) (hence to the contradiction). What remains open is proving the signed bound RH‑freely.

---

## 0) Locked GEO‑C4 objects (for alignment)

We use v43 canonical objects:

* \(f(v)=E'(v)/E(v)\).
* \(\mathcal L_t(v)=f(v+t)-f(v-t)\).
* \(\mathcal D_{a,h}(v)=\mathcal L_{a+h}(v)-\mathcal L_{a-h}(v)\), i.e.
  \[
  \mathcal D_{a,h}(v)
  =f(v+a+h)-f(v-a-h)-f(v+a-h)+f(v-a+h).
  \]
  【1043:0†manuscript_v43.pdf†L1-L18】
* Hinge circle \(v(\theta)=im+\delta e^{i\theta}\), \(h=\kappa\delta\), and
  \(\psi(\theta)=\Im\mathcal D_{a,h}(v(\theta))\). 【1043:0†manuscript_v43.pdf†L1-L18】
* \(P_2\) is orthogonal projection to \(\mathrm{span}\{\cos2\theta,\sin2\theta\}\) and
  \[
  \|P_2\psi\|_{L^2}=\pi^{-1/2}(A_c^2+A_s^2)^{1/2},\quad
  \Phi^\star=\frac{\delta^2}{h}\|P_2\psi\|_{L^2},
  \]
  with \(A_c=\int_0^{2\pi}\psi(\theta)\cos2\theta\,d\theta\),
  \(A_s=\int_0^{2\pi}\psi(\theta)\sin2\theta\,d\theta\). 【1043:0†manuscript_v43.pdf†L1-L18】

---

## 1) Residue / zero‑kernel identity for the signed k=2 channel

### 1.1 Define the signed k=2 coefficient(s)

Define the complex k=2 Fourier coefficient of \(\psi\) by
\[
\widehat\psi(2):=\int_0^{2\pi}\psi(\theta)e^{-2i\theta}\,d\theta
=\underbrace{\int_0^{2\pi}\psi(\theta)\cos2\theta\,d\theta}_{A_c}
-i\underbrace{\int_0^{2\pi}\psi(\theta)\sin2\theta\,d\theta}_{A_s}.
\]
So \(|\widehat\psi(2)|=(A_c^2+A_s^2)^{1/2}\), hence **exactly**
\[
\|P_2\psi\|_{L^2}=\pi^{-1/2}|\widehat\psi(2)|.
\]
(This is immediate from the v43 definition of \(P_2\) via \(A_c,A_s\).) 【1043:0†manuscript_v43.pdf†L1-L18】

For residue computation it is convenient to also define the *meromorphic* coefficients of \(\mathcal D_{a,h}\):
\[
I_{+2}:=\int_0^{2\pi}\mathcal D_{a,h}(v(\theta))\,e^{-2i\theta}\,d\theta,\qquad
I_{-2}:=\int_0^{2\pi}\mathcal D_{a,h}(v(\theta))\,e^{+2i\theta}\,d\theta.
\]

### 1.2 Lemma (contour forms)

Let \(z=\delta e^{i\theta}\) so that \(v(\theta)=im+z\) and \(d\theta=dz/(iz)\). Then:
\[
I_{-2}=\frac{1}{i\delta^2}\oint_{|z|=\delta}\mathcal D_{a,h}(im+z)\,z\,dz,
\qquad
I_{+2}=\frac{\delta^2}{i}\oint_{|z|=\delta}\mathcal D_{a,h}(im+z)\,z^{-3}\,dz.
\]

**Proof (line‑by‑line skeleton).**
1) Substitute \(z=\delta e^{i\theta}\). Then \(e^{2i\theta}=(z/\delta)^2\), \(e^{-2i\theta}=(\delta/z)^2\), \(d\theta=dz/(iz)\).  
2) Multiply and simplify:
\[
\int \mathcal D(im+z)\,e^{2i\theta}\,d\theta
=\oint \mathcal D(im+z)\frac{z^2}{\delta^2}\frac{dz}{iz}
=\frac{1}{i\delta^2}\oint \mathcal D(im+z)\,z\,dz,
\]
and similarly for \(I_{+2}\). \(\square\)

### 1.3 Lemma (zero‑kernel / residue representation for \(I_{-2}\))

Let \(\mathcal Z(E)\) be the multiset of zeros of \(E\), and recall \(f=E'/E\) has simple poles at each \(\rho\in\mathcal Z(E)\) with residue \(1\). Assume the circle \(|z|=\delta\) is **shift‑admissible** so that \(\mathcal D_{a,h}(im+z)\) has no poles on \(|z|=\delta\). Then
\[
I_{-2}=\frac{2\pi}{\delta^2}\sum_{\rho\in\mathcal Z(E)}K_{-2}(\rho;m,a,\delta,h),
\]
where the kernel is the explicit *local* sum
\[
\boxed{
\begin{aligned}
K_{-2}(\rho)&:=
(\rho-im-a-h)\,\mathbf 1_{\{|\rho-im-a-h|<\delta\}}
-(\rho-im+a+h)\,\mathbf 1_{\{|\rho-im+a+h|<\delta\}}\\
&\quad-(\rho-im-a+h)\,\mathbf 1_{\{|\rho-im-a+h|<\delta\}}
+(\rho-im+a-h)\,\mathbf 1_{\{|\rho-im+a-h|<\delta\}}.
\end{aligned}}
\]

**Proof (line‑by‑line skeleton).**
1) Start from the contour form:
\[
I_{-2}=\frac{1}{i\delta^2}\oint_{|z|=\delta}\mathcal D_{a,h}(im+z)\,z\,dz.
\]
2) Expand \(\mathcal D_{a,h}\) using v43’s definition
\(\mathcal D_{a,h}(v)=f(v+a+h)-f(v-a-h)-f(v+a-h)+f(v-a+h)\). 【1043:0†manuscript_v43.pdf†L1-L18】
3) Each term has the form \(f(im+z+t)\), with \(t\in\{a+h,\,-a-h,\,a-h,\,-a+h\}\) and a sign \(+,-,-,+\).
4) If \(\rho\) is a zero of \(E\), then \(f(w)\sim 1/(w-\rho)\) near \(w=\rho\). Hence \(f(im+z+t)\) has a simple pole at
\(z=z_{\rho,t}:=\rho-im-t\), residue \(1\).
5) Therefore the integrand \(z\,f(im+z+t)\) has residue \(z_{\rho,t}\) at \(z=z_{\rho,t}\), provided \(|z_{\rho,t}|<\delta\).
6) By residue theorem,
\[
\oint_{|z|=\delta} z\,f(im+z+t)\,dz = 2\pi i\sum_{\rho:\,|z_{\rho,t}|<\delta} z_{\rho,t}.
\]
7) Sum the four shifts with their signs and divide by \(i\delta^2\). This produces exactly the boxed kernel \(K_{-2}\). \(\square\)

### 1.4 Forced contribution in the pure quartet model

If there is an off‑axis quartet at height \(m\), then the *top pair* of zeros at \(\rho=a+im\) and \(\rho=-a+im\) generate poles at \(z=\pm h\) inside \(|z|=\delta\) (since \(h=\kappa\delta<\delta\)). In the pair‑isolated regime these are the only contributing zeros, and the kernel lemma yields:
\[
I_{-2}=-\frac{8\pi h}{\delta^2}\quad\text{(pure quartet contribution)}.
\]
This matches the v43 toy computation where the singular part is \(-4h/(u^2-h^2)\) and the \(k=2\) carrier is pure. 【1033:0†manuscript_v43.pdf†L39-L56】【1033:0†manuscript_v43.pdf†L66-L75】

---

## 2) Interpretation as “continuous parity oscillator” (reader‑guide Part III mapping)

The locked GEO‑C4 endpoint isolates the **frequency‑2** subspace \(\{\cos2\theta,\sin2\theta\}\). Sampling at quarter‑turns \(\theta=\pi n/2\) gives
\[
e^{\pm 2i\theta}=e^{\pm i\pi n}=(-1)^n,
\]
so the \(k=2\) channel is the continuous analogue of the **parity oscillator** \(\cos(\pi n)\) used in the Part‑III “single‑frequency collapse” scaffold.

Concretely, the Part‑III toolbox records the trigonometric/projector identities
\(\sin^2(\pi n/2)=P_{\rm odd}(n)\), \(\cos^2(\pi n/2)=P_{\rm even}(n)\), and rewrites the collapsed stream in a single \(\cos(\pi n)\) face. 【1026:8†reader_guide_v1.pdf†L1-L37】【1026:4†manuscript_v17.pdf†L37-L63】  
This is the discrete “π/2‑carrier” picture; GEO‑C4’s \(k=2\) harmonic is exactly the continuous Fourier‑mode version of that parity selector.

---

## 3) Replacement UE interface: signed k=2 bound (strictly weaker than v43 UE‑INPUT)

### 3.1 Why the v43 absolute UE‑INPUT is RH‑strength

The v43 UE interface uses the *absolute value* bound
\[
\int_0^{2\pi}\left|\mathcal D_{a,h}(v(\theta))\right|\,d\theta
\le C\,\frac{h(\log(m+3))^{C'}}{a^2}
\quad\text{(with }\delta=\eta a/\log^2(m+3)\text{)}.
\]
【1043:2†manuscript_v43.pdf†L1-L18】

But the locked forcing shows an off‑axis quartet produces a **non‑vanishing** \(k=2\) carrier, hence \(\Phi^\star\ge c_0(\kappa)>0\). 【1033:0†manuscript_v43.pdf†L39-L56】【1033:0†manuscript_v43.pdf†L88-L103】  
Since v43’s UE‑REDUCE already gives \(\Phi^\star\lesssim(\delta^2/h)\int|\mathcal D|\), any RH‑free proof of the absolute UE‑INPUT would eliminate quartets. This is the precise sense in which the L¹ absolute interface is RH‑strength.

### 3.2 Signed UE‑INPUT (proposal)

Because \(\Phi^\star\) depends **only** on the \(k=2\) projection, a *strictly weaker* UE interface is to bound only the signed coefficient \(\widehat\psi(2)\) (equivalently \(A_c,A_s\)):

\[
\boxed{
\textbf{Signed UE‑INPUT:}\quad
|\widehat\psi(2)|
=\left|\int_0^{2\pi}\Im\mathcal D_{a,h}(v(\theta))\,e^{-2i\theta}\,d\theta\right|
\le C\,\frac{h(\log(m+3))^{C'}}{a^2}
}
\]
uniformly for \(a\in(0,1)\), \(\delta=\eta a/\log^2(m+3)\), \(h=\kappa\delta\).

This bound is **strictly weaker** than the v43 absolute UE‑INPUT because
\(|\widehat\psi(2)|\le \int_0^{2\pi}|\psi(\theta)|\,d\theta\le \int_0^{2\pi}|\mathcal D_{a,h}(v(\theta))|\,d\theta\).

### 3.3 Lemma (Signed UE‑INPUT ⇒ \(\Phi^\star\) small)

Assume Signed UE‑INPUT. Then
\[
\Phi^\star(m,a,\delta,h)=\frac{\delta^2}{h}\|P_2\psi\|_{L^2}
=\frac{\delta^2}{h}\,\pi^{-1/2}|\widehat\psi(2)|
\le \pi^{-1/2}C\,\frac{\delta^2(\log(m+3))^{C'}}{a^2}.
\]
In particular, under the program coupling \(\delta=\eta a/\log^2(m+3)\),
\[
\Phi^\star \le \pi^{-1/2}C\,\eta^2\,(\log(m+3))^{C'-4}.
\]

**Proof.** Immediate from the exact identity \(\|P_2\psi\|_{L^2}=\pi^{-1/2}|\widehat\psi(2)|\) and the definition of \(\Phi^\star\). 【1043:0†manuscript_v43.pdf†L1-L18】

### 3.4 Weil‑identifiability plausibility (what we can and cannot claim)

*What is proved here:* \(I_{-2}\) (and hence the forced \(k=2\) channel) is an explicit **linear statistic of zeros** with a concrete kernel \(K_{-2}(\rho)\) (Section 1.3). This is the “zero‑kernel identity” needed for an explicit‑formula bridge.

*What is not proved here:* that Signed UE‑INPUT follows from a known Weil/Li criterion. However, the kernel is now explicit and **signed** (no absolute values), which is the correct shape for a Weil‑type inequality to even be plausible.

(Bridge work belongs to RH‑BRIDGE; my contribution is supplying the kernel and the reduction.)

---

## 4) Resonance / clutter check for the signed coefficient

### Lemma (pair‑isolation implies no cancellation in the forced channel)

Assume **pair isolation** at \(\pm a+im\) at scale \(R\delta\) (fixed \(R>1\)), and shift‑admissibility on the hinge circle. Then in the kernel formula for \(I_{-2}\), the only zeros contributing are \(\rho=\pm a+im\), hence
\[
I_{-2}=-\frac{8\pi h}{\delta^2},
\]
and therefore \(|\widehat\psi(2)|\asymp h/\delta^2\) (up to the already‑locked stability error in v43 Lemma 12.22).

**Reason this addresses resonance:** any “extra quartet” outside those \(R\delta\) disks does **not** enter the indicator sets in the kernel \(K_{-2}\), so it literally cannot cancel the forced contribution.

(If pair isolation is weakened to an \(N_{\rm eff}\) bound, then the kernel identity still holds but the error term becomes a finite sum of additional \(z_{\rho,t}\) contributions; controlling that requires RH‑LOCAL’s local counting input.)

---

## 5) Patch map (v43 → v44)

**Insert/replace locations:**

1) **UE interface box:** Replace v43 Box “UE‑INPUT” (absolute L¹ bound) with **Signed UE‑INPUT** (Section 3.2), and insert Lemma “Signed UE ⇒ \(\Phi^\star\) small” (Section 3.3).  
2) **Kernel identity remark/lemma:** Insert Lemma 1.3 (“zero‑kernel identity for \(I_{-2}\)”) into the GEO‑C4 section as a bridge‑ready lemma for RH‑BRIDGE.  
3) **Reader‑guide mapping remark:** one paragraph remark in Part I or Part III link: “k=2 harmonic = continuous parity oscillator” (Section 2).

---

## Referee risk notes (anticipated objections)

1) **“You didn’t prove Signed UE‑INPUT.”** Correct; this deliverable is an interface redesign + reduction. It is **strictly weaker** than the absolute UE‑INPUT and is now a clean, signed, kernel‑based criterion that is potentially bridgeable to explicit‑formula/Weil tools.
2) **“Kernel uses hard indicators; not smooth/Paley–Wiener.”** True. This is intrinsic to the exact hinge‑circle Fourier coefficient. A smooth variant would require modifying the endpoint (not allowed in this batch). The bridge can approximate the indicator via smoothing if needed.
3) **“Resonance could still cancel if zeros cluster at the same scale.”** This is precisely why the lemma is stated under pair isolation. If the program wants to weaken it, RH‑LOCAL must supply an \(N_{\rm eff}\) disk count.

---

## MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* Callsign: RH‑FORCE
* Result classification: **CONDITIONAL**
* Target gaps closed (by ID): **(none directly)**; UE interface redesigned to a signed criterion; supplies bridge kernel for UE work.
* Target gaps still open (by ID): **UE‑INPUT** remains open (proof of signed criterion); any weakening of pair isolation requires RH‑LOCAL.
* Key conclusions (≤5 bullets):
  1. The forced \(k=2\) channel admits an explicit **zero‑kernel / residue** formula (Lemma 1.3).
  2. The v43 absolute L¹ UE‑INPUT is RH‑strength; a RH‑free proof would immediately eliminate off‑axis quartets.
  3. A **strictly weaker** replacement is “Signed UE‑INPUT” bounding only \(|\widehat\psi(2)|\).
  4. Signed UE‑INPUT implies \(\Phi^\star\) small by an **exact identity**, so it is a valid substitute interface.
  5. Under pair isolation, resonance/clutter cannot cancel the forced channel because non‑local zeros do not enter the kernel indicators.
* Paste‑ready manuscript edits (TeX blocks):
  (i) revised lemma/proposition statements
  (ii) revised definitions/remarks
  (iii) revised theorem/inequality lines

```tex
% --- NEW: signed k=2 coefficient (place near the GEO-C4 endpoint definition) ---
\begin{definition}[Signed $k=2$ coefficient of the defect]
Let $v(\theta)=im+\delta e^{i\theta}$, $\psi(\theta)=\Im \mathcal D_{a,h}(v(\theta))$.
Define
\[
\widehat\psi(2):=\int_0^{2\pi}\psi(\theta)e^{-2i\theta}\,d\theta
= \int_0^{2\pi}\psi(\theta)\cos 2\theta\,d\theta
-i\int_0^{2\pi}\psi(\theta)\sin 2\theta\,d\theta.
\]
\end{definition}

\begin{lemma}[Exact $k=2$ identity]
With $A_c=\int_0^{2\pi}\psi(\theta)\cos2\theta\,d\theta$ and
$A_s=\int_0^{2\pi}\psi(\theta)\sin2\theta\,d\theta$, we have
$|\widehat\psi(2)|=(A_c^2+A_s^2)^{1/2}$ and hence
\[
\|P_2\psi\|_{L^2}=\pi^{-1/2}|\widehat\psi(2)|.
\]
\end{lemma}

% --- NEW: residue / zero-kernel identity (bridge-ready) ---
\begin{lemma}[Residue identity for the forced channel]\label{lem:Ikernel}
Assume the hinge circle $|z|=\delta$ is shift-admissible for $(a,h)$.
Let
\[
I_{-2}:=\int_0^{2\pi}\mathcal D_{a,h}(im+\delta e^{i\theta})\,e^{2i\theta}\,d\theta.
\]
Then
\[
I_{-2}=\frac{2\pi}{\delta^2}\sum_{\rho\in\mathcal Z(E)}K_{-2}(\rho;m,a,\delta,h),
\]
where
\[
\begin{aligned}
K_{-2}(\rho):=
(\rho-im-a-h)\,\mathbf 1_{\{|\rho-im-a-h|<\delta\}}
-(\rho-im+a+h)\,\mathbf 1_{\{|\rho-im+a+h|<\delta\}}\\
-(\rho-im-a+h)\,\mathbf 1_{\{|\rho-im-a+h|<\delta\}}
+(\rho-im+a-h)\,\mathbf 1_{\{|\rho-im+a-h|<\delta\}}.
\end{aligned}
\]
\end{lemma}

% --- REPLACE: UE-INPUT box with signed interface (place where UE-INPUT currently sits) ---
\begin{boxed}[Signed UE-INPUT]\label{box:signed-ue-input}
There exist constants $C,C'>0$ such that for all $m\ge 10$, all $a\in(0,1)$, and
$\delta=\eta a/(\log(m+3))^2$, $h=\kappa\delta$, one has
\[
|\widehat\psi(2)|
=\left|\int_0^{2\pi}\Im \mathcal D_{a,h}(v(\theta))\,e^{-2i\theta}\,d\theta\right|
\le C\frac{h(\log(m+3))^{C'}}{a^2}.
\]
\end{boxed}

\begin{lemma}[Signed UE implies smallness of $\Phi^\star$]\label{lem:signed-ue-to-Phi}
Assuming Box~\ref{box:signed-ue-input}, one has
\[
\Phi^\star(m,a,\delta,h)\le \pi^{-1/2}C\,\frac{\delta^2(\log(m+3))^{C'}}{a^2}.
\]
\end{lemma}

\begin{remark}[Parity-oscillator interpretation]
The $k=2$ channel corresponds to the continuous analogue of the discrete parity oscillator
$\cos(\pi n)$: sampling $e^{\pm 2i\theta}$ at $\theta=\pi n/2$ yields $(-1)^n$.
\end{remark}
```

* Dependencies on other branches:
  * **RH‑BRIDGE:** to attempt Weil/Li identification or explicit‑formula proof of Signed UE‑INPUT using the kernel in Lemma \ref{lem:Ikernel}.
  * **RH‑LOCAL:** only if the program wants to weaken pair isolation to an \(N_{\rm eff}\) bound for clutter robustness.
* Referee risk notes (anticipated objections + how addressed):
  1. Signed UE‑INPUT remains a conditional analytic input; we make that explicit and replace the too‑strong absolute L¹ interface.
  2. Kernel is local/indicator-based; acceptable for an exact identity; smoothing (if desired) requires endpoint modification (out of scope).
  3. Resonance handled by explicit hypothesis (pair isolation) and a clear dependency statement for weakening it.

