# Batch 15 — RH‑BRIDGE  
**Mission:** Burnol/Weil/Li identification audit: *does GEO‑C4’s \((k=2)\) functional equal a Weil/Li functional, and does that materially simplify UE?*  
**Ground truth:** v43 locked; UE surface only is mutable (v44 pre‑build).  
**Callsign:** RH‑BRIDGE  

## Executive verdict (binary)

**BRIDGE‑FAIL / NO‑GO (in the current v43 architecture).**  

The GEO‑C4 \((k=2)\) extracted quantity is a **local Fourier/Taylor coefficient** of a **meromorphic log‑derivative difference field** \(\mathcal D_{a,h}\) near \(v=im\). As a function of the zero variable \(\rho\), its per‑zero kernel is **meromorphic with poles**. In contrast, standard Weil/Li criteria are formulated in terms of **entire transforms** (Mellin/Fourier transforms of test functions in admissible classes) and typically yield **signed quadratic forms**.

Therefore:

* There is **no exact identification** of the GEO‑C4 kernel with a Weil/Li functional in the standard admissible classes.
* The current **absolute‑value \(L^1\)** UE interface cannot carry the phase/sign information that Weil/Burnol witness technology needs.
* Any Weil/Li import would require a **signed interface upgrade** plus an **entire‑kernel regularization layer** (a major v45+ pivot), not a v44 patch.

---

## 1) What a “real Weil bridge” would minimally require (so we can test it)

A legitimate Weil/Li bridge would need all of:

1. A test family \(g=g_{m,a,\delta,h}\) in a Weil‑admissible class (e.g. compact support in log‑variable / Paley–Wiener type) so that \(\widehat g(s)\) is **entire** and obeys the symmetry constraints required by the explicit formula / positivity form.
2. An identity (or domination) of the endpoint by a Weil/Li form, e.g. schematically
   \[
   \Phi^\star \stackrel{?}{=}\mathcal W(g)
   \quad\text{or}\quad
   \Phi^\star \stackrel{?}{\le}\mathcal W(g),
   \]
   where \(\mathcal W(g)\) is the explicit‑formula quadratic form over zeros plus archimedean/primes terms.
3. Parameter flexibility: the family \((m,a,\delta,h)\) must be rich enough to approximate the witness functions whose existence is guaranteed when RH fails (Burnol‑style arguments). If the family is too rigid, existence theorems are irrelevant.

We fail at (1)–(2) already, *before* the flexibility question.

---

## 2) What GEO‑C4’s \((k=2)\) object actually is (and why it is not Weil‑class)

### 2.1 Locked v43 definitions (recall)
* \(E(v)\): completed even entire object in the \(v\)-plane; \(f(v):=E'(v)/E(v)\).
* \(\mathcal L_t(v):=f(v+t)-f(v-t)\).
* \(\mathcal D_{a,h}(v):=\mathcal L_{a+h}(v)-\mathcal L_{a-h}(v)\).
* Hinge circle: \(v(\theta)=im+\delta e^{i\theta}\).
* \(\psi(\theta)=\Im \mathcal D_{a,h}(v(\theta))\).
* Endpoint: \(\displaystyle \Phi^\star=\frac{\delta^2}{h}\,\|P_2\psi\|_{L^2_\theta}\).

### 2.2 Signed coefficient reformulation (does not change GEO‑C4)
Define
\[
\widehat\psi(2):=\frac1{2\pi}\int_0^{2\pi}\psi(\theta)e^{-2i\theta}\,d\theta,
\qquad
\widehat{\mathcal D}(2):=\frac1{2\pi}\int_0^{2\pi}\mathcal D_{a,h}(v(\theta))e^{-2i\theta}\,d\theta.
\]
Then \(\widehat\psi(2)=\Im\widehat{\mathcal D}(2)\) and, for real \(\psi\),
\[
\|P_2\psi\|_{L^2_\theta}=2\sqrt{\pi}\,|\widehat\psi(2)|
\quad\Longrightarrow\quad
\Phi^\star=\frac{2\sqrt{\pi}\,\delta^2}{h}\,|\widehat\psi(2)|.
\]

So the endpoint is (up to a universal factor) just the magnitude of the \(k=2\) Fourier coefficient of the hinge field’s imaginary part.

### 2.3 Kernel structure: meromorphic in \(\rho\)
Assume only **shift‑admissibility**: \(\mathcal D_{a,h}\) holomorphic on a neighborhood of the hinge circle. Then Fourier/Taylor extraction gives
\[
\widehat{\mathcal D}(2)=\frac{\delta^2}{2}\,\mathcal D_{a,h}''(im).
\]

Write the log‑derivative in its standard partial fraction form
\[
f(v)=\sum_{\rho}\frac{1}{v-\rho}+H(v),
\]
where \(H\) is holomorphic (archimedean/trivial contributions absorbed).

Differentiate twice and apply the \((\pm a\pm h)\) shifts. One obtains
\[
\mathcal D_{a,h}''(im)=\sum_{\rho}K_{m,a,h}(\rho)\;+\;H_{m,a,h},
\]
where \(H_{m,a,h}\) is holomorphic and the explicit kernel is
\[
K_{m,a,h}(\rho)
=
2!\Bigg(
\frac1{(im+a+h-\rho)^3}
-\frac1{(im+a-h-\rho)^3}
-\frac1{(im-a+h-\rho)^3}
+\frac1{(im-a-h-\rho)^3}
\Bigg).
\]

**Structural consequence:** \(K_{m,a,h}(\rho)\) is **meromorphic** in \(\rho\) with cubic poles at
\[
\rho = im \pm (a\pm h).
\]

This pole structure is incompatible with standard Weil/Li frameworks (entire transforms).

---

## 3) NO‑GO proposition (proof‑grade): no Weil/Li identification “as‑is”

### Proposition (No exact Weil factorization for the GEO‑C4 \(k=2\) kernel)
Let \(g\) lie in any standard Weil‑admissible test class for which \(\widehat g(s)\) is **entire** (e.g. smooth compact support in the log variable, Paley–Wiener type). Then there is no identity of the form
\[
K_{m,a,h}(\rho)\equiv \widehat g(\rho)\widehat g(1-\rho)
\]
valid as a function of \(\rho\), nor any finite linear combination of such products.

#### Proof (one‑page referee proof)
* If \(\widehat g\) is entire, then \(\widehat g(\rho)\widehat g(1-\rho)\) is entire in \(\rho\). Finite linear combinations remain entire.
* The kernel \(K_{m,a,h}(\rho)\) has cubic poles at \(\rho=im\pm(a\pm h)\), hence is not entire.
* An entire function cannot equal a meromorphic function with poles. Contradiction. \(\square\)

### Consequence for Burnol “negativity witness exists”
Burnol‑style existence theorems produce witnesses **inside** the Weil‑admissible class (entire transforms). Since the GEO‑C4 kernel is **outside** that class, such existence results do not apply unless the manuscript introduces an **entire‑kernel regularization/smoothing layer**. None exists in v43.

### Additional obstruction: v43 UE‑INPUT is sign‑blind
Even ignoring the kernel‑class mismatch, the v43 UE interface bounds \(\int|\mathcal D|\), which is insensitive to the oscillatory sign/phase structure that Weil negativity witnesses exploit. So a “Weil shortcut” cannot replace UE‑INPUT unless UE‑INPUT itself is upgraded to a **signed coefficient control**.

---

## 4) Minimal signed upgrade needed if the program still wants a Weil bridge (v45+ pivot)

If you decide to pursue Weil/Li as a convergence jump later, the minimum viable redesign is:

1. Treat \(\widehat{\mathcal D}(2)\) (or \(\widehat\psi(2)\)) as the UE interface, not \(\int|\mathcal D|\):
   \[
   \boxed{\ |\widehat{\mathcal D}(2)| \le \text{(δ‑uniform bound in }a,h,m,\delta)\ }.
   \]
2. Replace the meromorphic kernel \(1/(z-\rho)^3\) by an **entire** approximation coming from a genuine Weil‑admissible \(g\) (Paley–Wiener / compact support in log variable). This is nontrivial because δ‑uniformity will interact with the test function’s exponential type.
3. Then (and only then) ask whether the parameter family can approximate Burnol witnesses.

This is a true architecture pivot, not a v44 clean‑up.

---

## 5) Dependency map update (UE surface only)

**Current v43 closure chain (unchanged):**  
GEO‑C4 forcing \(\Rightarrow\) \(\Phi^\star \gtrsim 1\) (off‑axis)  
UE‑REDUCE \(\Rightarrow\) \(\Phi^\star \le C\frac{\delta^2}{h}\int |\mathcal D\circ v|\)  
UE‑INPUT \(\Rightarrow\) \(\int |\mathcal D\circ v| \le C\frac{h(\log(m+3))^{C'}}{a^2}\)  
δ‑policy \(\Rightarrow \Phi^\star=o(1)\) \(\Rightarrow\) contradiction \(\Rightarrow a=0\).

**Weil bridge would only be relevant if it replaced UE‑INPUT.**  
This batch concludes it cannot, under the current endpoint/interface definitions.

---

## 6) Reader‑Guide hook (exploratory; not proof‑grade for v44)
The reader‑guide Part III “\(\pi/2\) carrier / \(\chi_4\) rectifier / parity projector” calculus strongly resembles mod‑4 frequency selection, which is *heuristically* aligned with isolating the \(k=2\) harmonic. This is suggestive but does not supply a Weil identification: those are structural post‑collapse identities, whereas a Weil bridge requires an explicit‑formula identification in a Weil‑admissible test class.

---

## S6 harness cross‑check (explicit‑formula interpretation)

*Mapping:* \(u=2s\), \(v=u-1\), so an off‑axis zero \(s=\beta+i\gamma\) corresponds to \(v_\rho=(2\beta-1)+i\,2\gamma\), with \(a=2\beta-1\), \(m=2\gamma\).  

**Interpretation:** GEO‑C4’s endpoint measures a *local phase/field oscillation witness* near \(v=im\) built from \(E'/E\) shifts. It is **not yet** an explicit‑formula “\(x^\beta\) amplitude leak functional” on the prime side, because no prime‑side explicit formula for \(\widehat{\mathcal D}(2)\) is currently in the manuscript. If a future Weil bridge were built, it would *create* that mapping; today the endpoint is internal analytic geometry rather than a direct prime‑amplitude observable.

---

# MANDATORY PATCH PACKET

* Callsign: RH‑BRIDGE  
* Result classification: **FAIL / NO‑GO** (Weil/Li identification does not hold “as‑is”)  
* Target gaps closed (by ID): UE‑INPUT “Weil/Burnol shortcut” attempt (classified + ruled out under current endpoint/interface)  
* Target gaps still open (by ID): UE‑INPUT proof itself; any future Weil‑bridge redesign layer  
* Key conclusions (≤5 bullets):
  1. GEO‑C4 \(k=2\) extraction yields a per‑zero kernel meromorphic in \(\rho\) with cubic poles at \(\rho=im\pm(a\pm h)\).
  2. Standard Weil/Li frameworks use entire transforms; thus no exact equality or finite combination match is possible.
  3. v43’s \(L^1\) UE interface is sign‑blind and cannot support Weil/Burnol witness imports.
  4. Any real Weil bridge requires a signed coefficient UE interface plus entire‑kernel regularization (major pivot).
  5. Therefore Weil/Li does not currently make v44 easier; UE‑INPUT must be attacked directly.

* Paste‑ready manuscript edits (TeX blocks):

(i) **(Optional) define the signed coefficient once (clarity + future‑proofing):**
```tex
\begin{definition}[Signed $k=2$ coefficient of the hinge field]
Let $v(\theta)=im+\delta e^{i\theta}$ and $\psi(\theta)=\Im\mathcal D_{a,h}(v(\theta))$.
Define
\[
\widehat{\mathcal D}(2):=\frac1{2\pi}\int_0^{2\pi}\mathcal D_{a,h}(v(\theta))e^{-2i\theta}\,d\theta,
\qquad
\widehat\psi(2):=\frac1{2\pi}\int_0^{2\pi}\psi(\theta)e^{-2i\theta}\,d\theta.
\]
Then $\widehat\psi(2)=\Im\widehat{\mathcal D}(2)$ and $\|P_2\psi\|_{L^2_\theta}=2\sqrt{\pi}\,|\widehat\psi(2)|$.
\end{definition}
```

(ii) **Insert scope remark + NO‑GO proposition near UE‑INPUT (prevents overclaiming):**
```tex
\begin{proposition}[No exact Weil/Li identification for the GEO--C4 $k=2$ kernel]\label{prop:no_weil_bridge}
Assume $\mathcal D_{a,h}$ is holomorphic on a neighborhood of the hinge circle.
Then $\widehat{\mathcal D}(2)=\frac{\delta^2}{2}\mathcal D''_{a,h}(im)$ and, writing
$f=E'/E=\sum_\rho \frac1{v-\rho}+H(v)$ with $H$ holomorphic, one gets
\[
\mathcal D''_{a,h}(im)=\sum_\rho K_{m,a,h}(\rho)+H_{m,a,h},
\]
where
\[
K_{m,a,h}(\rho)=2!\Big(\frac1{(im+a+h-\rho)^3}-\frac1{(im+a-h-\rho)^3}
-\frac1{(im-a+h-\rho)^3}+\frac1{(im-a-h-\rho)^3}\Big)
\]
is meromorphic in $\rho$ (cubic poles at $\rho=im\pm(a\pm h)$).
In particular, $\widehat{\mathcal D}(2)$ cannot be represented exactly as a Weil/Li
functional built from test data whose transforms are entire (e.g. Paley--Wiener / compact support classes).
\end{proposition}

\begin{remark}[Scope boundary: not a Weil/Li functional]
The present UE chain does not rely on Weil/Li criteria. Any future attempt to import Weil/Burnol
technology would require a signed coefficient interface on $\widehat{\mathcal D}(2)$ and an entire-kernel
regularization layer; neither is used here.
\end{remark}
```

* Dependencies on other branches:
  - RH‑ENVELOPE, if (and only if) the program later pursues explicit‑formula identification / entire‑kernel regularization.
  - RH‑FORCE only to ensure no forcing statement claims Weil identification.

* Referee risk notes:
  1. “But distributions can yield meromorphic transforms.” True; however the Weil/Burnol positivity/negativity statements are proven for specific admissible test classes. Enlarging the class requires re‑proving the explicit formula + positivity framework.
  2. “Approximate identification might suffice.” Only if approximation error is δ‑uniform and integrates into the budget theorem; no such control exists in v43.
  3. “You are blocking a route.” This NO‑GO blocks only the *shortcut claim*; it does not assert UE‑INPUT is false.
