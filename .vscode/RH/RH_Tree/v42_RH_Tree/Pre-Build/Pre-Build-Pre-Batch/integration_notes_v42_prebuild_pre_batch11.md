# Integration Notes — v42 pre-build (pre–Batch 12)
**Scope:** Consolidate GEO‑C4 (trig-contour harmonic endpoint) as the canonical “Geometry Change Requirement” lever after v41, and specify the *single active analytic brick* that must be closed to drive RH via the v‑frame forcing/UE contradiction.

**Input sources for this note:** Legacy responses (1a, 1b) to MASTER LEGACY PROMPT v41 (GEO‑C4), plus our v41 posture: “geometry/endpoint redesign is mandatory,” and the NO‑GO archive remains binding unless explicitly re‑audited.

---

## 0) Executive posture (truth‑latching)

### Canonical closure schema (v42 target)
We now treat the “Geometry Change Requirement” as **one boxed schema**:

> **(GEO‑C Closure Schema).**  
> Fix a height \(m>0\). Assume there exists an off‑axis quartet \(\{\pm a \pm i m\}\) in the centered width‑2 \(v\)-frame (so \(a>0\)).  
> Choose a hinge‑centered trig contour \(\partial\mathfrak B\) around \(v=i m\) and define a *harmonic endpoint* \(\Phi^*\).  
> If we can show:
> 1. **FORCE:** the quartet implies \(\Phi^*\ge c_0>0\) (absolute), and  
> 2. **UE:** unconditionally \(\Phi^*\le \varepsilon(m,a)\) with \(\varepsilon(m,a)=o(1)\) under the nominal \(\delta\)-policy,  
> then no such \(a>0\) can exist at that height. Since \(m\) was arbitrary, all heights collapse and RH follows.

**v42 is the build where GEO‑C4 becomes canonical** (not exploratory). The remaining frontier becomes a single analytic “UE brick.”

---

## 1) Frame map (mandatory hygiene)
We remain in the same normalization chain:

- \(s=\beta+i\gamma\) (classical strip),
- \(u=2s\) (width‑2),
- \(v=u-1\) (hinge-centered):  
  \[
  v=(2\beta-1)+i(2\gamma)=a+i m.
  \]
So **off-axis** means \(a\neq 0\) and corresponds to \(\beta=\tfrac12+\tfrac a2\).

Let \(E(v)\) denote the **even entire completion in the \(v\)-plane** (the intended object is \(\xi\) expressed in \(v\)-coordinates), so:
- \(E\) is entire,
- \(E(v)=E(-v)\),
- zeros obey quartet symmetry (from FE + conjugation): if \(a+i m\) is a zero then \(\pm a\pm i m\) are zeros.

---

## 2) GEO‑C4 canonical objects

### 2.1 Shift‑difference operators
Let \(F(z):=\dfrac{E'(z)}{E(z)}\). Define for \(t>0\):
\[
\mathcal L_t(v):=F(v+t)-F(v-t).
\]
For “tilt” \(a>0\) and “coupling” \(h>0\):
\[
\mathcal D_{a,h}(v):=\mathcal L_{a+h}(v)-\mathcal L_{a-h}(v).
\]
Equivalently (algebraic identity, exact):
\[
\mathcal D_{a,h}(v)=\big(F(v+a+h)-F(v+a-h)\big)+\big(F(v-a+h)-F(v-a-h)\big).
\]
Also \(\mathcal D_{a,h}=\dfrac{Q'_{a,h}}{Q_{a,h}}\) where
\[
Q_{a,h}(v):=\frac{E(v+a+h)}{E(v+a-h)}\cdot\frac{E(v-a+h)}{E(v-a-h)}.
\]

### 2.2 Hinge‑centered trig contour (the “geometry change”)
Define the **hinge circle**:
\[
\partial\mathfrak B = C_{m,\delta}:\quad v(\theta)= i m+\delta e^{i\theta},\quad \theta\in[0,2\pi].
\]
This is GEO‑C1: the witness is centered at the hinge point \(v=i m\), not aligned at \(a+i m\).

### 2.3 Coupling policy (δ‑aware)
Adopt **commensurate coupling** (GEO‑C2):
\[
h=\kappa \delta,\qquad \kappa\in(0,1)\text{ fixed (e.g. }\kappa=\tfrac12\text{)}.
\]
Nominal δ‑policy (as elsewhere in the manuscript):
\[
\delta=\delta(m,a):=\eta\,\frac{a}{(\log(m+3))^2},
\quad \eta\in(0,1)\text{ fixed}.
\]
Key point: **FORCE is δ‑independent once \(\kappa\) is fixed**, while UE improves as \(\delta\to0\).

### 2.4 Endpoint functional (harmonic extraction)
Define the phase signal on the contour:
\[
\psi_{a,h}(\theta):=\Im\big(\mathcal D_{a,h}(v(\theta))\big).
\]
Let \(P_2\) denote orthogonal projection in \(L^2([0,2\pi])\) onto the \(k=2\) Fourier subspace
\(\mathrm{span}\{\cos(2\theta),\sin(2\theta)\}\).

Define the **GEO‑C4 endpoint**:
\[
\boxed{\ \Phi^*(m,a,\delta,h):=\frac{\delta^2}{h}\,\big\|P_2\psi_{a,h}\big\|_{L^2([0,2\pi])}\ }.
\]
This is GEO‑C4: “replace sidewise max / pointwise bounds by orthogonal harmonic extraction.”

---

## 3) Toy‑model forcing (truth‑latching computation)
In the quartet toy model (single quartet at \(\pm a\pm i m\)), one computes the singular forced part:
\[
\mathcal D^{\mathrm{sing}}_{a,h}(i m+u)=-\frac{4h}{u^2-h^2},
\quad u=\delta e^{i\theta}.
\]
Hence
\[
\Im\big(\mathcal D^{\mathrm{sing}}_{a,h}(v(\theta))\big)
=\frac{4h\delta^2\sin(2\theta)}{h^4-2h^2\delta^2\cos(2\theta)+\delta^4},
\]
which is a **pure \(k=2\) carrier**. A direct computation yields
\[
\int_0^{2\pi}\Im(\mathcal D^{\mathrm{sing}}_{a,h}(v(\theta)))\,\sin(2\theta)\,d\theta=\frac{4\pi h}{\delta^2},
\quad
\int_0^{2\pi}\Im(\cdot)\cos(2\theta)\,d\theta=0.
\]
Therefore \(\|P_2\psi\|_{L^2}\asymp h/\delta^2\) and so
\[
\boxed{\ \Phi^* \asymp 1\ \text{(indeed }=4\pi\text{ up to normalization conventions), independent of }\delta.\ }
\]
This is the **FORCE** signature that survives δ‑shrink and defeats the old NG‑Δa‑A trap.

---

## 4) UE roadmap (the only remaining analytic brick)
Harmonic extraction allows **integration‑by‑parts gains**.

Let \(\widehat\psi(2)=\int_0^{2\pi}\psi(\theta)e^{-2i\theta}\,d\theta\). Then:
\[
\widehat\psi(2)=\frac{1}{(-2i)^2}\int_0^{2\pi}\psi''(\theta)e^{-2i\theta}\,d\theta
\quad\Rightarrow\quad
|\widehat\psi(2)|\le \frac14\int_0^{2\pi}|\psi''(\theta)|\,d\theta.
\]
Chain rule with \(v(\theta)=i m+\delta e^{i\theta}\) gives schematically:
\[
|\psi''(\theta)|\lesssim \delta^2\,|\partial_v^2\mathcal D_{a,h}(v(\theta))|+\delta\,|\partial_v\mathcal D_{a,h}(v(\theta))|.
\]
Mean value theorem in the shift parameter:
\[
\mathcal D_{a,h}(v)=2h\,\partial_t\mathcal L_t(v)\big|_{t=t_*},\quad t_*\in[a-h,a+h],
\]
and similarly for \(v\)-derivatives.

### **ACTIVE BRICK (UE‑INPUT).**
A sufficient “field bound” to close UE is:

> For \(j=0,1,2\),
> \[
> \boxed{\ \sup_{t\in[a-h,a+h]}\ \sup_{\theta\in[0,2\pi]}\ 
> \big|\partial_t\partial_v^j\mathcal L_t(v(\theta))\big|
> \ \le\ C\,\frac{(\log(m+3))^{C_1}}{a^{2+j}}\ }.
> \]
> (All constants absolute / explicit; no RH input.)

Then:
\[
\partial_v^j\mathcal D_{a,h}(v(\theta))\ll h\,\frac{(\log m)^{C_1}}{a^{2+j}},
\]
and the IBP chain yields
\[
\Phi^*\ll \Big(\frac{\delta}{a}\Big)^3(\log m)^{C_1}=o(1)
\quad\text{under}\quad \delta=\eta\frac{a}{\log^2 m}.
\]
This is the *only* mathematical frontier after GEO‑C4 is installed.

---

## 5) Resonance / multi‑quartet handling (what changes vs old S5′)
Old failure modes:
- **O(\(\delta/a\)) cancellation** for centered defect endpoints;
- **δ‑inert resonance** from a second quartet at \(a-\varepsilon\sim a-\delta\).

GEO‑C4 changes the battleground:
- We are not taking sidewise maxima; we are taking a **single orthogonal channel**.
- The forced singular part is a **dipole mode** (pure \(k=2\)).
- “Resonance” now manifests as additional contributions to the \(k=2\) coefficient vector. These *can* in principle interfere, so **FORCE‑robustness** is a required lemma (see §6). It is not hand‑waved.

---

## 6) What is still open before v42 can claim closure
**Open Lemma F‑ROBUST:** show that the forced quartet contribution to \(\|P_2\psi\|_{L^2}\) cannot be cancelled below \(c_0\) by the remainder (archimedean terms + other zeros), under explicit hypotheses (shift‑admissibility + a quantitative “non‑forced remainder” bound derived from local zero counts and separation).

**Open Lemma SHIFT‑ADMISS:** a clean δ‑shrink policy to ensure the contour and all shifted traces avoid zeros, stated without circularity.

**Open Lemma UE‑INPUT:** the active brick in §4, with explicit constants.

These three are exactly what Batch‑12 must target.

---

## 7) S6 explicit‑formula harness (mandatory mapping)
Off‑axis means \(\beta=\tfrac12+\tfrac a2\), so in explicit‑formula terms the contribution of such a zero has amplitude \(x^{\beta}=x^{1/2}\cdot x^{a/2}\), i.e. an **amplitude leak** factor \(x^{a/2}\).

GEO‑C4’s endpoint is a *local amplitude‑leak detector*: an off‑axis quartet forces a non‑vanishing \(k=2\) harmonic in a hinge‑centered circular probe of the “tilt‑derivative field” \(\mathcal D_{a,h}\). UE‑INPUT bounds show the field is too small on the nominal δ‑scale for such a leak to exist. This is the intended conceptual correspondence; it is not used as an assumption.

---

## 8) Decisions locked for v42 pre-build
1. **Endpoint class:** GEO‑C4 harmonic endpoint \(\Phi^*\) (k=2 projection) is canonical.
2. **Geometry:** hinge‑centered circle \(C_{m,\delta}\) is canonical (not aligned boxes).
3. **Coupling:** \(h=\kappa\delta\) is canonical (no micro‑coupling).
4. **Frontier:** a single analytic UE‑INPUT brick + FORCE‑robustness and shift‑admissibility hygiene.

