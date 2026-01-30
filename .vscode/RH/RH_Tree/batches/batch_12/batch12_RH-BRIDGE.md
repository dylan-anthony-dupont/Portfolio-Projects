# Batch 12 — RH-BRIDGE  
**Mission:** Bulletproof GEO‑C4 hinge‑circle setup: endpoint well-defined (no log branches), shift‑admissibility + buffering coherent, and NO‑GO scope does not overblock the new harmonic endpoint class.

This response is **v42‑ready** (pre‑build patch blocks), consistent with the v42 patch queue items Q42.1/Q42.7/Q42.10.

---

## 1) Definition hygiene package (endpoint is log‑free)

### Paste‑ready TeX block (Definitions + endpoint)

```tex
% =========================
% GEO-C4: hinge-circle setup
% =========================

\begin{definition}[Completed object in the centered $v$--frame]\label{def:E-vframe}
Let $\xi(s)$ denote the completed Riemann xi--function and define the width--$2$ completion
\[
\Xi_2(u):=\xi(u/2).
\]
In the centered coordinate $v=u-1$ we define
\[
E(v):=\Xi_2(1+v)=\xi\!\Big(\frac{1+v}{2}\Big).
\]
Then $E$ is entire and even:
\[
E(-v)=E(v),
\]
and satisfies the reality symmetry $E(\overline v)=\overline{E(v)}$.  Consequently, if $\rho$ is a zero of $E$ then
$\{\rho,\,-\rho,\,\overline\rho,\,-\overline\rho\}$ are also zeros (counted with multiplicity).
\end{definition}

\begin{definition}[Log--derivative and two--sided shift differences]\label{def:DaH-LaH}
Let
\[
f(v):=\frac{E'(v)}{E(v)},
\]
which is meromorphic with simple poles at the zeros of $E$.
For $t\in\mathbb R$ define the two--sided shift difference
\[
\mathcal L_t(v):= f(v+t)-f(v-t),
\]
and for parameters $a>0$ and $h>0$ define the second difference operator
\[
\mathcal D_{a,h}(v):=\mathcal L_{a+h}(v)-\mathcal L_{a-h}(v).
\]
Equivalently,
\[
\mathcal D_{a,h}(v)
=
\big(f(v+a+h)-f(v+a-h)\big)
+
\big(f(v-a+h)-f(v-a-h)\big).
\]
\end{definition}

\begin{definition}[Hinge circle, trace observable, and the $n=2$ Fourier mode]\label{def:hinge-circle-endpoint}
Fix $m>0$ and $\delta>0$.  The hinge circle centered at $im$ is
\[
C_{m,\delta}:=\{v(\theta): \theta\in[0,2\pi]\},\qquad v(\theta):=im+\delta e^{i\theta}.
\]
Assuming $\mathcal D_{a,h}(v(\theta))$ is well-defined for all $\theta$, define the real--valued trace observable
\[
\psi_{a,h}(\theta):=\Im\big(\mathcal D_{a,h}(v(\theta))\big)\in\mathbb R.
\]
For $g\in L^2([0,2\pi])$ write its Fourier coefficients as
\[
\widehat g(n):=\frac1{2\pi}\int_0^{2\pi} g(\theta)e^{-in\theta}\,d\theta,
\]
and define the $n=2$ Fourier projection
\[
(P_2 g)(\theta):=\widehat g(2)e^{2i\theta}+\widehat g(-2)e^{-2i\theta}.
\]
(Equivalently, $P_2 g(\theta)=A\cos(2\theta)+B\sin(2\theta)$ for some $A,B\in\mathbb R$.)

Define the harmonic endpoint
\[
\Phi^*(a,m,\delta,h):=\frac{\delta^2}{h}\,\|P_2\psi_{a,h}\|_{L^2([0,2\pi],\,d\theta)}.
\]
\end{definition}

\begin{remark}[No logarithm branch is used]\label{rem:no-log-branch}
The endpoint $\Phi^*$ depends only on the meromorphic quantity $f=E'/E$ evaluated on admissible traces.
No global branch of $\log E$ is ever chosen: we do not form $\log E$ or $\arg E$ pointwise.
All phase information is extracted from $f$ (and its finite differences) via integration / Fourier projection on the circle.
\end{remark}
```

**Referee note:** This explicitly decouples the endpoint from any “choose a branch of log” ambiguity: only the meromorphic function \(E'/E\) is used.

---

## 2) Shift‑admissibility and buffering (with monotone‑safe shrink)

### What must be true (minimum)

On the hinge circle \(v(\theta)=im+\delta e^{i\theta}\), the operator \(\mathcal D_{a,h}(v(\theta))\) samples \(f=E'/E\) at the four shifted traces
\[
v(\theta)+t,\qquad t\in T_{a,h}:=\{a+h,\ a-h,\ -a+h,\ -a-h\}.
\]
To avoid poles on the integration contour, we need **no zeros of \(E\) on these shifted circles**.

### Paste‑ready TeX block (definition + shrink lemma)

```tex
% =========================
% Shift-admissibility for hinge-circle traces
% =========================

\begin{definition}[Shift-admissibility for $(C_{m,\delta},a,h)$]\label{def:shift-admissibility}
Let $m>0$, $\delta>0$, $a>0$, $h>0$, and define
\[
T_{a,h}:=\{a+h,\ a-h,\ -a+h,\ -a-h\}.
\]
We say the hinge circle $C_{m,\delta}$ is \emph{$(a,h)$--shift-admissible} if
\[
E\big(v(\theta)+t\big)\neq 0\qquad\text{for all }\theta\in[0,2\pi]\text{ and all }t\in T_{a,h}.
\]
Equivalently, $f=E'/E$ is holomorphic on each shifted trace $C_{m,\delta}+t$ $(t\in T_{a,h})$.

We say $C_{m,\delta}$ is \emph{$(a,h)$--shift-admissible with buffer constant $c_{\rm buf}\in(0,1)$} if, in addition,
\[
\dist\!\big(C_{m,\delta}+t,\ Z(E)\big)\ \ge\ c_{\rm buf}\,\delta
\qquad\text{for all }t\in T_{a,h},
\]
where $Z(E)$ denotes the multiset of zeros of $E$ (with multiplicity).
\end{definition}

\begin{lemma}[Monotone-safe shrink to enforce shift-admissibility]\label{lem:shift-admiss-shrink}
Fix $m>0$, $a>0$, and a coupling constant $\kappa\in(0,1)$, and set $h=\kappa\delta$.
There exists $\delta_*(m,a,\kappa,E)>0$ such that for every $\delta\in(0,\delta_*]$ the hinge circle $C_{m,\delta}$
is $(a,h)$--shift-admissible with buffer constant $c_{\rm buf}=1-\kappa$.

In particular, once $\delta\le \delta_*$ has been chosen, any further shrink $\delta'\in(0,\delta]$
(with $h'=\kappa\delta'$) remains shift-admissible with the same buffer constant.
\end{lemma}

\begin{proof}
For $\sigma\in\{\pm1\}$ define the limiting centers $c_\sigma:=im+\sigma a$.
Since $E$ is entire, its zeros are isolated.  Hence for each $\sigma$ there exists $r_\sigma>0$ such that the closed disk
$\overline{D}(c_\sigma,r_\sigma)$ contains no zeros of $E$ other than possibly a zero at $c_\sigma$ itself.
Let $r:=\min(r_{+1},r_{-1})$ and set $\delta_*:=r/4$.

Fix $\delta\in(0,\delta_*]$ and set $h=\kappa\delta$.
For each choice of signs $(\sigma,\tau)\in\{\pm1\}^2$ consider the shifted circle
\[
C_{\sigma,\tau}:=\{\,im+\sigma a+\tau h+\delta e^{i\theta}:\ \theta\in[0,2\pi]\,\}.
\]
This circle has center $im+\sigma a+\tau\kappa\delta$ and radius $\delta$.
Every point of $C_{\sigma,\tau}$ lies within distance $(1+\kappa)\delta\le 2\delta\le r/2$ of the limiting center $c_\sigma$,
so $C_{\sigma,\tau}\subset \overline{D}(c_\sigma,r/2)\subset \overline{D}(c_\sigma,r_\sigma)$.

By construction of $r_\sigma$, the only possible zero of $E$ in $\overline{D}(c_\sigma,r_\sigma)$ is at $c_\sigma$.
If $c_\sigma$ is not a zero, then $C_{\sigma,\tau}$ contains no zeros and we are done.
If $c_\sigma$ is a zero, then its distance to the circle center equals $\kappa\delta<\delta$, hence $c_\sigma$ lies strictly
inside $C_{\sigma,\tau}$ and not on the boundary.  Therefore $E$ has no zeros on $C_{\sigma,\tau}$ in all cases.

Moreover, if $c_\sigma$ is a zero, then its distance to the boundary circle $C_{\sigma,\tau}$ is exactly $\delta-\kappa\delta=(1-\kappa)\delta$.
Any other zero lies outside $\overline{D}(c_\sigma,r_\sigma)$ and therefore has distance $\ge r/2\ge 2\delta\ge (1-\kappa)\delta$ from $C_{\sigma,\tau}$.
Hence $\dist(C_{\sigma,\tau},Z(E))\ge (1-\kappa)\delta$.
Since the four shifts $t\in T_{a,h}$ correspond to the four choices of $(\sigma,\tau)$, the claim follows.
\end{proof}

\begin{remark}[How the shrink lemma is used]\label{rem:shrink-usage}
If a proof step requires shift-admissibility at the nominal scale $\delta_0(a,m)$ but admissibility fails at $\delta=\delta_0$,
one may replace $\delta_0$ by any smaller $\delta\le \min(\delta_0,\delta_*)$ (with $h=\kappa\delta$) until admissibility holds.
This does not assume RH: it uses only that $E$ is entire and its zeros are isolated.
Under the GEO-C4 normalization $\Phi^*=\frac{\delta^2}{h}\|P_2\psi\|_{L^2}$, the forcing constant is $\delta$--independent once $\kappa$ is fixed,
while δ-shrinking can only strengthen any UE upper bound that is monotone in $\delta$.
\end{remark}
```

**Referee note:** the key is that we never need “no zeros in the interior.” We only require **no poles on the trace** (plus a quantitative buffer so derivatives are bounded).

---

## 3) Non‑circularity check (no RH smuggling)

* Shift‑admissibility is a **contour selection / regularity** condition: the trace must not pass through zeros of \(E\).  
* The shrink lemma uses only: **\(E\) entire ⇒ zeros isolated**, hence each limit center has a punctured neighborhood free of other zeros.  
* Nothing in the definition or lemma asserts zeros lie on \(\Re(v)=0\) (or \(\Re(s)=1/2\)), and nothing assumes the absence of off‑axis zeros.

This is therefore **referee‑safe** with respect to RH‑equivalent smuggling.

---

## 4) Compatibility with v41 NO‑GO archive (avoid accidental overblocking)

### Potential confusion points

1. **D5 “absolute \(L^r\) endpoints (NO‑GO)”** is about endpoints built from absolute norms of \(E'/E\) (or similar) *without* extra small parameters or signed cancellation.
2. **D6 “projection endpoints (NO‑GO)”** is about the \(L^2(\partial B)\) orthogonal projection \(\Pi_B\) onto the local Cauchy kernel span \(K_B\) on a *rectangle* box, used to annihilate the local term.

### Why these do not block GEO‑C4

* The GEO‑C4 endpoint \(\Phi^*\) is **not** an absolute \(L^r\) norm of \(E'/E\); it is a **harmonic (Fourier‑mode) functional** of the **second shift difference** \(\mathcal D_{a,h}\), with a built‑in small parameter \(h=\kappa\delta\) and a mode extraction \(P_2\). This is exactly the type of “extra small factor / smoothing before triangle inequality” that the scope audits already identify as outside the pointwise ceiling class.
* The “projection” \(P_2\) is a **Fourier projection on the hinge circle**, not the \(L^2(\partial B)\) projection \(\Pi_B\) used in D6 to kill local kernels. The D6 NO‑GO is irrelevant unless one attempts to use \(\Pi_B\) to remove local poles while still controlling a forced endpoint.

### Paste‑ready TeX scope clarification (recommended insertion)

```tex
\begin{remark}[NO--GO scope: D5/D6 vs.\ harmonic GEO-C4 endpoints]\label{rem:nogo-scope-geoC4}
The archived NO--GO latches D5 and D6 are endpoint-class statements for earlier rectangle witnesses.
D5 concerns \emph{absolute} $L^r(\partial B)$ endpoints applied directly to $E'/E$ (or $|E'/E|$-type quantities),
and D6 concerns the orthogonal projection $\Pi_B:L^2(\partial B)\to K_B$ onto the local Cauchy-kernel span on a rectangle,
used to annihilate the local term without a new forcing link.

These do not apply to the GEO--C4 hinge-circle endpoint $\Phi^*$, which is a \emph{harmonic Fourier-mode functional}
of the \emph{second shift difference} $\mathcal D_{a,h}$ on $C_{m,\delta}$.
In particular, the Fourier projection $P_2$ on the circle is unrelated to $\Pi_B$ and should not be conflated with D6.
\end{remark}
```

---

## 5) Mandatory S6 harness cross‑check (explicit‑formula relevance)

Shift‑admissibility is **local analytic hygiene**, not a prime‑side phenomenon:

* If a shifted trace intersects a zero, \(E'/E\) has a pole on the integration contour and the endpoint is ill‑defined.
* Enforcing admissibility by shrinking \(\delta\) corresponds to choosing a contour that avoids singularities.  
* This does **not** directly correspond to an explicit‑formula “\(x^\beta\) amplitude leak.” The amplitude leak corresponds to the **existence of an off‑axis quartet** \(\pm a\pm im\) (i.e., \(\beta\neq 1/2\)), while shift‑admissibility is the condition needed to *measure* a witness endpoint associated to that quartet without encountering poles on the trace.

Frame mapping reminder (program standard): if \(\rho=\beta+i\gamma\) is a zero in \(s\)-frame, then \(v_\rho=(2\beta-1)+i\,2\gamma\). Thus \(a=2\beta-1\) and \(m=2\gamma\). Shift‑admissibility does not constrain \(a\); it only ensures the circle probes \(E'/E\) safely.

---

# MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* Callsign: RH-BRIDGE
* Result classification: **PASS** (setup package is referee-grade under explicit hypotheses)
* Target gaps closed (by ID):
  - **Q42.1** (definition hygiene for $\mathcal D_{a,h}$ / hinge circle / endpoint $\Phi^*$)
  - **Q42.7** (shift-admissibility definition + monotone-safe shrink lemma)
  - **Q42.10** (NO-GO scope guard to prevent accidental overblocking)
* Target gaps still open (by ID):
  - Any **forcing** or **UE** inequalities for $\Phi^*$ (these are not Bridge/setup; owned by FORCE/ENVELOPE/LOCAL)
  - Any **resonance bookkeeping** beyond the setup layer (owned by LOCAL/ENVELOPE)
* Key conclusions (≤5 bullets):
  1. $\Phi^*$ is definable **without any $\log$ or $\arg$ branch**, purely from $E'/E$ on admissible traces.
  2. Shift-admissibility is a **trace nonvanishing** condition; it is enforceable by δ-shrink using only “$E$ entire ⇒ zeros isolated.”
  3. Under coupling $h=\kappa\delta$ with $\kappa\in(0,1)$, one obtains a **quantitative buffer** $\dist\ge (1-\kappa)\delta$ on all shifted circles for all sufficiently small δ.
  4. The v41/v40 NO-GO latches D5/D6 do **not** block GEO‑C4: they apply to different endpoint classes (absolute norms of $E'/E$ and rectangle-kernel projections).
  5. Shift-admissibility has no direct explicit-formula meaning; it is **analytic well-posedness**, not a prime irregularity witness.
* Paste-ready manuscript edits:
  (i) revised lemma/proposition statements  
  - Insert `def:E-vframe`, `def:DaH-LaH`, `def:hinge-circle-endpoint`, `rem:no-log-branch`.  
  - Insert `def:shift-admissibility`, `lem:shift-admiss-shrink`, `rem:shrink-usage`.  

  (ii) revised definitions/remarks  
  - Insert `rem:nogo-scope-geoC4` near the NO‑GO scope remark / GEO box so “projection” is not misread.

  (iii) revised theorem/inequality lines  
  - None (setup-only batch; no inequality claims added).
* Dependencies on other branches:
  - FORCE: needs forcing lower bound stated for $\Phi^*$ (toy calculation already exists; proof-grade in v42+).
  - ENVELOPE/LOCAL: need δ-uniform UE bound and resonance-safe decomposition for the same endpoint.
* Referee risk notes (anticipated objections + how addressed):
  - **“You used $\log E$ implicitly.”** Addressed: endpoint uses only $E'/E$ and Fourier projection; explicit “no log branch” remark added.
  - **“Admissibility assumes RH / zero-freeness.”** Addressed: shrink lemma uses only isolation of zeros of an entire function; does not constrain zero locations.
  - **“Projection NO-GO (D6) kills this.”** Addressed: clarified that $P_2$ is Fourier projection on a circle, not the kernel-annihilating $\Pi_B$ projection on rectangles.
