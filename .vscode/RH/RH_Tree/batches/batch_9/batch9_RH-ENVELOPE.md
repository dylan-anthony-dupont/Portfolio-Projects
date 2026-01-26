# Batch 9 — RH‑ENVELOPE  
**File:** `batch9_RH-ENVELOPE.md`  
**Status:** v39 not built (this is a pre‑build decision batch).  
**Mission:** Decide whether the defect endpoint built from \(\mathcal Q_a\) / \(\mathcal L_a\) can admit a **δ‑uniform upper envelope** with a usable exponent \(p>0\) (ideally \(p\ge \tfrac12\)) **without** reintroducing the forced‑zero obstruction.

---

## Executive decision (one page)

**Result classification:** **CONDITIONAL**.

- **Good news (forced‑zero obstruction cleared):** The defect log‑derivative \(\mathcal L_a(v)\) (and its phase endpoint) is **not topologically forced by a single interior zero** in the way \(\widetilde D_B(W)\) was. In the minimal quartet model, the would‑be pole cancels and the endpoint can be small.
- **New obstruction (horizontal resonance):** A δ‑uniform UE with \(p>0\) requires control of **near‑resonant zeros whose real parts lie within \(O(\delta)\) of the defect shift \(a\)** (or, equivalently, control of a “horizontal resonance sum” \(\sum 1/|a-\Re\rho|\)). Without such control, there are explicit even/quartet model counterexamples where the endpoint is **δ‑inert** (size \( \asymp 1\)) despite δ→0.

So: the defect endpoint is a **legitimate redesign direction**, but it is **not self‑closing**; it pushes the Missing Lever onto a concrete LOCAL‑type lemma: **exclude/quantify horizontal resonance** around \(a\).

---

## (A) Completion hygiene (mandatory)

### A1. Λ‑type vs ξ‑type: choose ξ‑type (entire) as in v35+

To keep all “entire” uses literally true and to preserve the evenness symmetry cleanly, the working function must be **ξ‑type** (entire), not Λ‑type (meromorphic).

### A2. Paste‑ready definition: entire + even in v‑frame

```tex
% === Completion / symmetry hygiene (v39 candidate; keep v35+ convention) ===

\begin{definition}[Width--2 entire completion and centered working function]
\label{def:Xi2_Ev}
Let $\xi(s)$ denote the standard entire completion of $\zeta(s)$ satisfying $\xi(s)=\xi(1-s)$.
Define the width--2 entire completion
\[
\Xi_2(u) := \xi(u/2),
\]
so $\Xi_2$ is entire and satisfies the width--2 functional equation
\[
\Xi_2(u)=\Xi_2(2-u).
\]
Define the centered v-frame working function
\[
E(v) := \Xi_2(1+v).
\]
Then $E$ is entire and even:
\[
E(v)=E(-v).
\]
Moreover, $E(\overline v)=\overline{E(v)}$ (reality on the real axis).
\end{definition}

\begin{proof}
From $\xi(s)=\xi(1-s)$ and $u=2s$ we have $\Xi_2(u)=\Xi_2(2-u)$.
Thus $E(v)=\Xi_2(1+v)=\Xi_2(1-v)=E(-v)$.
\end{proof}
```

### A3. Explicit s→u→v mapping (required)

- \(u = 2s\) (width‑2), \(v = u-1\), so \(s = \dfrac{1+v}{2}\).
- A zeta zero \( \rho=\beta+i\gamma\) corresponds to
  \[
  u_\rho = 2\rho = 2\beta + i\,2\gamma,\qquad
  v_\rho = u_\rho - 1 = (2\beta-1) + i\,2\gamma.
  \]
- Define the RH‑free displacement/height parameters:
  \[
  a := \Re(v_\rho)=2\beta-1,\qquad m := \Im(v_\rho)=2\gamma.
  \]
  Off‑critical means \(a\neq 0\).

---

## (B) Endpoint functional in the “phase class” (pick one; mandatory)

### Choice: **Option 2 (integral endpoint)** on buffered side segments

Use the defect log‑derivative (preferred object):
\[
\mathcal L_a(v):=\frac{E'}{E}(v+a)-\frac{E'}{E}(v-a)
\;=\;\partial_v\log\mathcal Q_a(v),
\qquad
\mathcal Q_a(v):=\frac{E(v+a)}{E(v-a)}.
\]

**Endpoint definition:** max over buffered sides of the **phase integral** of \(\mathcal L_a\). This is in the S5′ “phase class” because it is a signed \(\Im\int (\cdot)\,dv\) functional; it is **not** a pointwise/dial evaluation, and it is **not** an absolute \(L^r(\partial B)\) norm on \(|E'/E|\).

### Paste‑ready TeX

```tex
% === Defect objects and phase-class endpoint (v39 candidate) ===

\begin{definition}[Defect quotient and defect log-derivative]
\label{def:defect_Qa_La}
Fix $a\in(0,1]$. Define
\[
\mathcal Q_a(v):=\frac{E(v+a)}{E(v-a)},
\qquad
\mathcal L_a(v):=\partial_v\log\mathcal Q_a(v)
=\frac{E'}{E}(v+a)-\frac{E'}{E}(v-a).
\]
\end{definition}

\begin{definition}[Buffered defect phase endpoint]
\label{def:defect_phase_endpoint}
Let $B=B(0,m,\delta)$ be the centered aligned box and let $B_{\kappa/2}$ be its buffered sub-box.
Let $\{S_j\}_{j=1}^4$ be the four oriented sides of $\partial B_{\kappa/2}$.
Assume $\mathcal Q_a$ is holomorphic and nonvanishing on a neighborhood of each $S_j$ (so a continuous branch of $\arg\mathcal Q_a$ exists).
Define the defect phase endpoint
\[
\Phi^{\rm def}_B(a) \;:=\; \max_{1\le j\le 4}\left|\Im\int_{S_j}\mathcal L_a(v)\,dv\right|
\;=\;\max_{1\le j\le 4}\left|\Delta_{S_j}\arg\mathcal Q_a\right|.
\]
\end{definition}
```

**Why this avoids forbidden swaps:** The endpoint is a signed contour integral of a log‑derivative difference; no evaluation of \(W(v_\pm)\), no \(\sup_{\partial B}|E'/E|\), and no absolute \(L^r(\partial B)\) norm on \(|E'/E|\) is introduced as the endpoint.

---

## (C) Upper envelope target inequality (mandatory)

### C1. Natural UE target in the program’s budget template

We aim for a bound of the form
\[
\Phi^{\rm def}_B(a)
\ \le\
A\,\delta^{p}(\log m)^u
\ +\
B\,\delta^{p-\theta}\bigl(\text{local term}\bigr)^q
\ +\
D\,\delta^{p}(\log m)^w,
\]
with δ‑uniform constants and a usable \(p>0\) (ideally \(p\ge 1/2\)).

### C2. Candidate bound (conditional on a LOCAL “horizontal resonance” control)

Define the “horizontal resonance sum” in the local height window:
\[
\mathcal R_a(m)\;:=\;\sum_{\rho:\ E(\rho)=0,\ |\Im\rho-m|\le 1}\frac{1}{|a-\Re\rho|+a}.
\]
(This is finite because the local set is finite; it measures how many local zeros sit near the vertical lines \(\Re v=\pm a\).)

**Candidate UE inequality (what ENVELOPE can supply):**
\[
\boxed{
\Phi^{\rm def}_B(a)
\ \le\
C_0\,\delta\,(\log m)
\ +\
C_1\,\delta\,a\,\mathcal R_a(m)
}
\tag{UE-def}
\]
where \(C_0,C_1\) are shape‑only / κ‑only constants (δ‑uniform).

- Here \(p=1\).
- The “local term” is \(\mathcal R_a(m)\) with \(q=1\).
- The local δ‑exponent is **θ=0** (no δ blow‑up), **provided** \(\mathcal R_a(m)\) is controlled independently of δ.

**Why this is the right structural shape:** each local zero contributes to \(\mathcal L_a\) as a **dipole kernel** rather than a Cauchy kernel, and dipoles are integrable on the boundary with a factor of \(a\) in the numerator.

### C3. What LOCAL would need to prove to make this “usable” under the nominal δ-scale

Under the proposed nominal scale
\[
\delta_0(m,a)=\eta\,\frac{a}{(\log m)^2},
\]
the second term becomes
\[
\delta\,a\,\mathcal R_a(m)\ \le\ \eta\,\frac{a^2}{(\log m)^2}\,\mathcal R_a(m).
\]

A **usable** closure would follow if LOCAL can prove a bound like
\[
\mathcal R_a(m)\ \ll\ \frac{(\log m)^2}{a^2}\cdot (\log m)^{O(1)} \quad\text{(RH-free)}.
\]
Even the weaker
\[
\mathcal R_a(m)\ \ll\ \frac{\log m}{a}
\]
would already give \(\delta a\mathcal R_a(m)\ll \eta/\log m\), shrinkable in η.

This is a crisp, auditable target: **control a horizontal resonance sum**, not micro‑counting in a δ‑window.

### C4. Proof sketch for (UE-def) (ENVELOPE‑side; standard but needs to be written carefully)

- Expand \(E'/E\) in the v‑frame as “zero sum + completion terms” (Hadamard / \(\xi'/\xi\) representation); then
  \(\mathcal L_a(v)\) becomes a sum of dipole kernels:
  \[
  \frac{1}{v+a-\rho}-\frac{1}{v-a-\rho}
  =\frac{-2a}{(v-\rho)^2-a^2}.
  \]
- On each buffered side segment \(S_j\) of length \(\asymp \delta\), bound
  \(|\Im\int_{S_j} \mathcal L_a(v)\,dv|\le \int_{S_j}|\mathcal L_a(v)|\,|dv|\).
- For the completion terms, a horizontal difference across \(\pm a\) gives \(O(\log m)\) uniformly, hence contributes \(O(\delta\log m)\).
- For each local zero \(\rho\), estimate the dipole contribution by
  \[
  \int_{S_j}\frac{a}{|v-\rho|\,|v-\rho\pm a|}\,|dv| \ \ll\ \delta\,\frac{a}{|a-\Re\rho|+a},
  \]
  which sums to the \(\delta a\mathcal R_a(m)\) term.
- Zeros outside \(|\Im\rho-m|\le 1\) contribute \(O(\delta\log m)\) by standard tail bounds (as in the residual envelope lemma lineage).

**Bottom line:** ENVELOPE can plausibly supply \(p=1\) **provided** LOCAL supplies a bound on \(\mathcal R_a(m)\) that is not secretly δ‑dependent.

---

## (D) Forced‑zero obstruction check (mandatory)

You asked explicitly: “prove (or disprove) that your endpoint is **not** topologically forced by a single interior zero.”

### D1. What “forced” meant previously
For \(\widetilde D_B(W)\), a single interior zero forced a \(\pi/2\) lower bound by winding (argument principle). That killed any δ‑shrinking UE bound.

### D2. For the defect endpoint \(\Phi^{\rm def}_B(a)\), the one‑quartet model is **not forcing**

In the defect construction, a “single off‑axis quartet” produces **matched zeros** in numerator and denominator of \(\mathcal Q_a\) at the same v‑locations, yielding **removable** singularities in \(\mathcal Q_a\) and cancellation of poles in \(\mathcal L_a\). Therefore there is no topological forcing analogous to \(\widetilde D_B\ge \pi/2\).

#### Paste‑ready lemma (forced‑zero obstruction avoided)

```tex
\begin{lemma}[Defect endpoint is not topologically forced by a single quartet]
\label{lem:defect_not_forced_by_one_quartet}
Fix $a>0$ and $m>0$ and consider the even/quartet model
\[
E_{\rm qt}(v):=\bigl((v-im)^2-a^2\bigr)\,\bigl((v+im)^2-a^2\bigr),
\]
whose zeros are the quartet $\{\pm a\pm i m\}$.
Define $\mathcal Q_a$ and $\mathcal L_a$ from $E_{\rm qt}$ as in Definition~\ref{def:defect_Qa_La}.
Then $\mathcal Q_a$ is holomorphic and nonvanishing in a neighborhood of $v=im$, and
$\mathcal L_a$ is holomorphic at $v=im$ (no pole).
Consequently, for any sufficiently small centered box $B(0,m,\delta)$, the defect phase endpoint
$\Phi^{\rm def}_B(a)$ is not bounded below by a positive constant independent of $\delta$.
\end{lemma}

\begin{proof}
At $v=im$ we have $v+a=a+im$ and $v-a=-a+im$, both zeros of $E_{\rm qt}$ with the same multiplicity.
Thus the ratio $\mathcal Q_a(v)=E_{\rm qt}(v+a)/E_{\rm qt}(v-a)$ has a removable singularity at $v=im$ and extends holomorphically and nonvanishingly there.
Then $\mathcal L_a=\partial_v\log\mathcal Q_a$ is holomorphic at $v=im$.
\end{proof}
```

### D3. New obstruction: near‑resonant second quartet yields δ‑inert size (NO‑GO unless LOCAL controls it)

Even though one quartet does not force \(\Phi^{\rm def}\), a **nearby displacement** can.

If \(E\) contains **two quartets** at displacements \(a\) and \(a-\varepsilon\) with \(\varepsilon\asymp\delta\), then \(\mathcal L_a\) acquires a near‑pole at distance \(\asymp\varepsilon\) from the contour, and the defect endpoint can become \(\asymp \delta/\varepsilon \asymp 1\), i.e. δ‑inert.

#### Paste‑ready NO‑GO lemma (horizontal resonance obstruction)

```tex
\begin{lemma}[NO--GO unless horizontal resonance is controlled]
\label{lem:defect_horizontal_resonance_nogo}
Fix $a>0$ and $m>0$. For $\varepsilon\in(0,a/2)$ define the even/quartet model
\[
E_{\varepsilon}(v):=\bigl((v-im)^2-a^2\bigr)\bigl((v+im)^2-a^2\bigr)\cdot
\bigl((v-im)^2-(a-\varepsilon)^2\bigr)\bigl((v+im)^2-(a-\varepsilon)^2\bigr).
\]
Let $\mathcal L_a$ be the defect log-derivative built from $E_\varepsilon$.
Then on the centered box $B(0,m,\delta)$ with $\delta\asymp \varepsilon$, one has
\[
\Phi^{\rm def}_B(a)\ \ge\ c_0>0
\]
with $c_0$ an absolute constant independent of $\delta$.
In particular, no $\delta$--shrinking UE bound of the form
$\Phi^{\rm def}_B(a)\le C\,\delta^{p}\cdot(\text{δ-uniform RHS})$ with $p>0$ can hold without an additional
hypothesis excluding or controlling such near-resonant quartets.
\end{lemma}

\begin{proof}[Proof sketch]
The second quartet introduces dipole terms in $\mathcal L_a$ with denominators
$(v-\rho)^2-a^2$ that become $O(\varepsilon)$-small on $\partial B_{\kappa/2}$ when $\delta\asymp\varepsilon$,
creating an $O(1/\varepsilon)$ magnitude over a length-$\delta$ segment and hence an $O(1)$ phase integral.
A full proof is a direct residue/estimate computation for $E_\varepsilon$.
\end{proof}
```

**Interpretation:** the defect redesign trades the old “forced-zero” obstruction for a new, concrete obstruction: **horizontal resonance** (zeros with real parts within \(O(\delta)\) of the shift \(a\)). Any v39+ attempt must either rule these out or bound them in a δ‑compatible way.

---

## (E) S6 explicit-formula mapping (mandatory)

### E1. Map \(a=2\beta-1\) correctly
An off-axis zero with real part \(\beta>1/2\) corresponds to \(a=2\beta-1>0\). The explicit formula for \(\psi(x)\) contains a contribution of size \(\asymp x^\beta\) from that zero; relative to the critical-line size \(x^{1/2}\), the amplitude leak factor is \(x^{\beta-1/2}=x^{a/2}\).

### E2. What the defect object measures (qualitative harness)
For v on the imaginary axis \(v=i m\) (so \(s=(1+im)/2\) has \(\sigma=1/2\)), the shifts satisfy
\[
v\pm a \ \leftrightarrow\ s_\pm = \frac{1+v\pm a}{2} = \frac12 \pm \frac{a}{2} + i\frac{m}{2}.
\]
Thus
\[
\mathcal Q_a(i m) = \frac{E(i m+a)}{E(i m-a)}
= \frac{\xi\!\left(\frac12+\frac{a}{2}+i\frac{m}{2}\right)}{\xi\!\left(\frac12-\frac{a}{2}+i\frac{m}{2}\right)}.
\]
So the defect quotient compares \(\xi\) on the two symmetric vertical lines \(\sigma=\frac12\pm\frac a2\).

**S6 interpretation:** controlling \(\log \mathcal Q_a\) (or \(\mathcal L_a=\partial_v\log\mathcal Q_a\)) is plausibly a way of controlling how much “mass” of \(\xi\) sits to the right of the critical line. If an \(x^\beta\) amplitude leak is present (\(\beta>1/2\)), it corresponds to \(a>0\); a successful defect UE that enforces smallness at the nominal scale \(\delta_0\propto a/(\log m)^2\) would be consistent with ruling out such leaks.

**But:** This is still a harness‑level interpretation. A proof‑grade implication “defect UE failure ⇒ explicit‑formula leak” would require a separate lemma translating bounds on \(\xi'/\xi\) across \(\sigma\) into prime‑side growth; that is not supplied here.

---

# PATCH PACKET (mandatory)

* **Callsign:** RH‑ENVELOPE
* **Result classification:** **CONDITIONAL**
* **Target gaps closed (by ID):** none fully closed (v39 not built). This batch provides a **decision filter** and a **v39-ready insertion package** for the defect endpoint.
* **Target gaps still open (by ID):**
  - The Missing Lever remains open, now reframed as **horizontal resonance control** for the defect endpoint (new LOCAL obligation).
* **Key conclusions (≤5 bullets):**
  1. Completion hygiene remains ξ‑type: \(E(v)=\Xi_2(1+v)\) is **entire** and **even**, unconditionally.
  2. The defect phase endpoint built from \(\mathcal L_a=\partial_v\log\mathcal Q_a\) is a legitimate **phase‑class** endpoint (no pointwise/sup swap, no absolute \(L^r(|E'/E|)\) endpoint).
  3. The forced‑zero obstruction is **avoided**: a single off‑axis quartet does **not** topologically force \(\Phi^{\rm def}_B(a)\) (removable singularity / pole cancellation).
  4. Any δ‑uniform UE with \(p>0\) requires controlling **horizontal resonance** (zeros with \(|\Re\rho-a|\lesssim\delta\)); otherwise there are explicit quartet counterexamples with δ‑inert endpoint size.
  5. A plausible conditional UE has exponent \(p=1\) and local exponent \(\theta=0\), but the local term must be a controlled resonance sum \(\mathcal R_a(m)\).
* **Paste‑ready manuscript edits (TeX blocks):**
  (i) revised lemma/proposition statements:  
  - Definition/lemma `def:Xi2_Ev` (entire + even E)  
  - Definition `def:defect_Qa_La`  
  - Definition `def:defect_phase_endpoint`  
  - Lemma `lem:defect_not_forced_by_one_quartet` (forced-zero obstruction avoided)  
  - Lemma `lem:defect_horizontal_resonance_nogo` (new NO‑GO unless resonance controlled)

  (ii) revised definitions/remarks:  
  - Add a remark in the S5′ OPEN box: “Defect endpoint avoids forced-zero obstruction but requires horizontal resonance control.”

  (iii) revised theorem/inequality lines:  
  - Insert the candidate UE template (UE-def) with explicit local term \(\mathcal R_a(m)\) and the required LOCAL bound.
* **Dependencies on other branches:**
  - **RH-LOCAL:** must decide whether \(\mathcal R_a(m)\) (or a comparable resonance count) can be bounded RH‑freely in a way compatible with δ‑uniformity and the nominal scale \(\delta_0=\eta a/(\log m)^2\).
  - **RH-FORCE / RH-ABSORB:** must decide what contradiction/tail gate uses this defect endpoint and how forcing attaches (this batch does not supply a forcing lemma for \(\Phi^{\rm def}\)).
* **Referee risk notes (anticipated objections + how addressed):**
  - *Objection:* “Your NO‑GO uses model quartets, not \(\Xi_2\).”  
    *Answer:* Correct; it is a **design obstruction**: any UE proof relying only on local analytic structure must confront this resonance phenomenon unless a zeta‑specific hypothesis excludes it.
  - *Objection:* “You assumed \(\mathcal Q_a\) is nonvanishing on sides.”  
    *Answer:* Stated explicitly as a hypothesis in the endpoint definition; v39 must implement a λ‑shift/buffer policy analogous to earlier phase toolkits.
  - *Objection:* “δ‑uniformity might hide in \(\mathcal R_a(m)\).”  
    *Answer:* Exactly; the batch conclusion is conditional on LOCAL bounding \(\mathcal R_a(m)\) without δ‑dependence.
