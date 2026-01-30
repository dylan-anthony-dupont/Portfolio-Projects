# batch13 — RH-LOCAL-13

**CALLSIGN:** RH-LOCAL-13  
**MISSION:** Local singularity accounting around the *shifted hinge traces* in v42 (GEO–C4) and a resonance stress test: determine what UE-INPUT is really excluding, and whether the **k=2 harmonic extraction** provides any *automatic* suppression against near-resonant quartets.

---

## 0) Fixed setup (v42 anchors)

We work in the **v-plane** with the **hinge circle**
\[
C_{m,\delta}:\quad v(\theta)= i m + \delta e^{i\theta},\qquad \theta\in[0,2\pi].
\]
The shifted “field” and the k=2 endpoint are (v42):
\[
\mathcal L_t(v):=\frac{E'}{E}(v+t)-\frac{E'}{E}(v-t),\qquad 
\mathcal D_{a,h}(v):=\mathcal L_{a+h}(v)-\mathcal L_{a-h}(v),
\]
\[
\psi(\theta):=\Im\big(\mathcal D_{a,h}(v(\theta))\big),\qquad 
\Phi^\star(m,a,\delta,h):=\frac{\delta^2}{h}\,\|P_2\psi\|_{L^2([0,2\pi])}.
\]
(These are the objects in §12.2 / GEO–C4.)【930:11†manuscript_v42.pdf†L3-L29】

“Shift-admissibility / buffer-admissibility” is exactly the condition that all four shifted traces
\(v(\theta)\pm(a\pm h)\) stay away from zeros of \(E\), quantitatively by a buffer \(\mathrm{buf}\cdot\delta\).【930:3†manuscript_v42.pdf†L11-L33】

The “UE-INPUT” open statement (Box 12.2.5) is a uniform bound on 
\(\partial_t\partial_v^j \mathcal L_t\) on those shifted traces, for \(j=0,1,2\) and \(t\in[a-h,a+h]\).【930:4†manuscript_v42.pdf†L67-L117】

**Frame mapping reminder (s→u→v):**  
If \(s=\beta+i\gamma\), then \(u=2s\) and \(v=u-1\), so an s-zero \(\rho=\beta+i\gamma\) corresponds to
\[
v_\rho=(2\beta-1)+i(2\gamma) = a+ i m,\quad a:=2\beta-1,\quad m:=2\gamma.
\]
Off-critical-line \(\beta\neq\frac12\) is exactly \(a\neq 0\).

---

## 1) Local pole lemma: proximity to shifted traces forces δ-scale derivatives

### Lemma 1 (local pole proximity ⇒ δ-scale lower bound for the field derivatives)

Let \(E\) be holomorphic near \(\rho_+=a+i m\) and suppose \(E(\rho_+)=0\) with multiplicity \(r\ge1\).  
Fix \(\delta>0\) and \(h\in(0,\delta)\). For \(t\in\mathbb R\) define
\[
\mathcal L_t(v)=\frac{E'}{E}(v+t)-\frac{E'}{E}(v-t),\qquad v(\theta)=i m+\delta e^{i\theta}.
\]
Then for every \(t\) with \(|t-a|\le h\) and every integer \(j\ge0\), the **local contribution** of \(\rho_+\) to
\(\partial_t\partial_v^j\mathcal L_t(v(\theta))\) satisfies
\[
\sup_{\theta\in[0,2\pi]}
\Bigl|\bigl(\partial_t\partial_v^j\mathcal L_t\bigr)_{\rho_+}\!\bigl(v(\theta)\bigr)\Bigr|
\;=\;
r\,(j+1)!\,\bigl(\delta-|t-a|\bigr)^{-(2+j)}
\;\ge\;
r\,(j+1)!\,(\delta-h)^{-(2+j)}.
\]
In particular, under the nominal policy \(\delta_0=\eta a/(\log(m+3))^2\) (with \(a>0\)) this yields the forced scale
\[
\sup_{\theta}
\Bigl|\bigl(\partial_t\partial_v^j\mathcal L_t\bigr)_{\rho_+}(v(\theta))\Bigr|
\;\gtrsim\;
r\,(j+1)!\,\eta^{-(2+j)}\,a^{-(2+j)}(\log(m+3))^{4+2j}.
\]

#### Proof (one-pole accounting; proof-grade)
Write locally \(E(v)=(v-\rho_+)^{r}\,G(v)\) with \(G\) holomorphic and nonzero near \(\rho_+\). Then
\[
\frac{E'}{E}(v)=\frac{r}{v-\rho_+}+\frac{G'}{G}(v).
\]
The principal part contribution of \(\rho_+\) to \(E'/E(v+t)\) is \(r/(v+t-\rho_+)\).  
Differentiating \(j\) times in \(v\) and once in \(t\) gives
\[
\bigl(\partial_t\partial_v^j(E'/E)(v+t)\bigr)_{\rho_+}
=
r\,(-1)^{j+1}(j+1)!\,(v+t-\rho_+)^{-(2+j)}.
\]
The \(-E'/E(v-t)\) term is holomorphic in a neighborhood of \(\rho_+\) when \(|t-a|\le h\ll a\), so it does not contribute to the **principal part at \(\rho_+\)**.  

On the hinge circle, \(v(\theta)+t-\rho_+ = \delta e^{i\theta} + (t-a)\). As \(\theta\) varies, the set \(\{\delta e^{i\theta}+(t-a)\}\) is the circle of radius \(\delta\) centered at \(t-a\), so the minimum modulus is \(\delta-|t-a|\) (since \(|t-a|<\delta\)). Therefore
\[
\sup_\theta |v(\theta)+t-\rho_+|^{-(2+j)}=(\delta-|t-a|)^{-(2+j)},
\]
and the displayed identity follows. ∎

---

### Consequence (why this is the “toy-model scale”)

Lemma 1 formalizes the stress-test point: **as soon as a zero sits at distance \(\asymp \delta\) from a shifted trace, the \(t\)-derivative field naturally lives at scale \(\delta^{-(2+j)}\)**. This is exactly the blow-up scale the prompt highlighted.

So, UE-INPUT (as written) cannot hope for a bound smaller than \(\delta^{-(2+j)}\) in general; after converting \(\delta=\eta a/(\log m)^2\), this enforces at least a \((\log m)^{4+2j}\) “tax” in any \(a^{-(2+j)}\)-type bound.【930:4†manuscript_v42.pdf†L67-L117】

---

## 2) Resonance stress test: does k=2 harmonic extraction suppress near-resonant quartets?

### 2.1 What “near-resonant clutter” means locally
A *near-resonant* configuration at the same height \(m\) is:
- one quartet at \(v=\pm a \pm i m\), and
- another quartet at \(v=\pm(a-\varepsilon)\pm i m\) with \(\varepsilon\) on the **δ-scale** (e.g. \(\varepsilon\approx \delta\)).

For \(t=a\) (which lies in \([a-h,a+h]\)), the shifted trace \(C_{m,\delta}+t\) is the circle of radius \(\delta\) around \(a+i m\).  
The zero at \((a-\varepsilon)+i m\) lies at distance \(\varepsilon\) from the center, so its distance to the circle is \(|\delta-\varepsilon|\). Therefore:
- if \(\varepsilon\approx \delta\), then this *second* quartet places a zero within distance \(\ll \delta\) of the shifted trace, and
- the \(t\)-derivative kernels behave like \(|\delta-\varepsilon|^{-(2+j)}\), which can be much worse than \(\delta^{-(2+j)}\).

This is the exact “δ-inert resonance” geometry behind the earlier no-go phenomena: it is **not** about zeros *on* the contour (buffer-admissibility forbids that), but about zeros *just off* the contour on the δ-scale.

### 2.2 Does k=2 projection give automatic cancellation/suppression?

Two distinct questions:

1) **For UE-INPUT itself (sup bounds on \(\partial_t\partial_v^j\mathcal L_t\)):**  
No automatic suppression. UE-INPUT is a *supremum of absolute values* over \((t,\theta)\). Quartet symmetry and harmonic extraction occur **after** forming \(\psi(\theta)=\Im(\mathcal D_{a,h}(v(\theta)))\) and applying \(P_2\). They do not help you bound the raw field derivatives in the UE-INPUT box. In particular, Lemma 1 shows the forced δ-scale blow-up is structurally present whenever the shifted trace passes δ-close to any zero.

2) **For the endpoint \(\Phi^\star\) (k=2 Fourier coefficient):**  
There *is* an automatic suppression mechanism, but it is geometric and only helps against poles that are **well inside** the circle or **well outside** it.

A clean model calculation: if \(f(u)=1/(u-u_0)\) with \(|u_0|<\delta\) and \(u=\delta e^{i\theta}\), then its Fourier expansion on \(|u|=\delta\) gives a k=2 coefficient proportional to \(u_0/\delta^2\). Thus:
- poles very near the center (\(|u_0|\ll\delta\)) contribute **little** to k=2,
- poles near the boundary (\(|u_0|\asymp\delta\)) contribute **order \(1/\delta\)** to k=2.

Near-resonant quartets are exactly the dangerous case \(|u_0|\asymp\delta\), so **no automatic suppression** occurs there. GEO–C4’s harmonic extraction filters some clutter, but it does *not* magically kill δ-scale resonances.

**Bottom line:** harmonic extraction helps only when “other induced poles” are not sitting in the δ-annulus near \(|u|=\delta\). If there are additional quartets whose induced singularities land within \(O(\delta)\) of the hinge circle, they can survive the k=2 filter.

---

## 3) Is UE-INPUT equivalent to excluding near-trace zeros (RH-strength), or not?

### 3.1 What UE-INPUT is *structurally* asking for
UE-INPUT asks for a bound of the form
\[
\sup_{\substack{t\in[a-h,a+h]\\ \theta\in[0,2\pi]}}
\left|\partial_t\partial_v^j\mathcal L_t\bigl(v(\theta)\bigr)\right|
\ \lesssim\ \frac{(\log(m+3))^{C'}}{a^{2+j}}
\quad(j=0,1,2),
\]
uniformly for the whole band of shifted traces.【930:4†manuscript_v42.pdf†L67-L117】

By Lemma 1, if an off-axis zero exists at \(a+i m\), then the *local pole piece* alone forces a contribution of size \(\gtrsim \delta^{-(2+j)}\). Converting \(\delta=\eta a/(\log m)^2\), that’s consistent with the UE-INPUT RHS only if the log exponent can absorb at least \((\log m)^{4+2j}\).

So UE-INPUT is **not literally “exclude the forced quartet”**; it is compatible with a forced quartet.  
What it *does* start to exclude is **near-resonant clutter**: additional zeros that come within \(o(\delta)\) of one of the shifted traces (equivalently, induced singularities at distance \(o(\delta)\) from the hinge circle), because those would force \(|\partial_t\partial_v^j\mathcal L_t|\gg \delta^{-(2+j)}\) and break any fixed polylog bound.

### 3.2 Cancellation from symmetry?
At the level of \(\partial_t\partial_v^j\mathcal L_t\) in UE-INPUT: **no**.  
Symmetry is helpful after you form \(\mathcal D_{a,h}\) and project to k=2, but UE-INPUT as stated is a raw field bound and does not get a structural cancellation from quartet symmetry.

So **as currently phrased, UE-INPUT is morally a “no zeros too near any shifted trace” hypothesis plus a local counting/tail control statement**, not a pure harmonic-cancellation statement.

---

## 4) Patch proposal (LOCAL): make the “near-trace exclusion” obligation explicit (and weaker than RH)

### Proposed insertion: a “Near-trace isolation” hypothesis (weaker than RH, strong enough to neutralize resonance)

This is the cleanest way to state what must be ruled out to protect UE-INPUT from resonant clutter **without RH-smuggling** (it allows off-axis quartets, but forbids *δ-scale crowding around the shifted traces*).

#### Paste-ready TeX (new hypothesis/lemma near Box 12.2.5)

```tex
% --- LOCAL PATCH: make the resonance-exclusion obligation explicit ---
\begin{hypothesis}[Near-trace isolation for UE-INPUT]\label{hyp:near-trace-isolation}
Fix $\kappa\in(0,1)$ and $\mathrm{buf}\in(0,1)$. 
Let $m>0$, $a\in(0,1)$, and let $\delta\le \delta_0(m,a)$ with $h=\kappa\delta$.
Assume the hinge circle $C_{m,\delta}$ is $(a,h)$-shift-admissible and $(a,h)$-buf-admissible
in the sense of Definition~\ref{def:shift-admissible}.

In addition, assume the following \emph{near-trace isolation} condition:
for every zero $\rho\in Z(E)$ with $\rho\notin\{\pm a\pm i m\}$,
\[
\dist\!\Big(\rho,\ \bigcup_{t\in[a-h,a+h]}\big(C_{m,\delta}+t\big)\ \cup\ \big(C_{m,\delta}-t\big)\Big)
\ \ge\ \mathrm{buf}\,\delta.
\]
Equivalently: aside from the forced quartet (if present), there are no zeros within distance
$\mathrm{buf}\,\delta$ of any shifted hinge trace used by $\mathcal L_t$ for $t\in[a-h,a+h]$.
\end{hypothesis}

\begin{remark}[Why this isolates the resonance obstruction]
The $\delta$-inert resonance toy model corresponds to a second quartet at height $m$ whose
top zero sits within $O(\delta)$ of one of the shifted traces (typically $C_{m,\delta}+a$),
i.e. it violates Hypothesis~\ref{hyp:near-trace-isolation}. This hypothesis is strictly weaker
than RH: it permits off-axis quartets, but forbids $\delta$-scale crowding near the traces.
\end{remark}
```

**How ENVELOPE/FORCE would use it:** it is exactly the missing local condition that blocks the “near-resonant quartets” that make the derivative field (and hence UE-INPUT) blow up beyond the intended polylog/a scaling.

---

## 5) Resonance conclusion (one sentence)

**Conclusion:** GEO–C4’s k=2 harmonic extraction does *not* automatically suppress δ-scale near-resonant quartets; controlling UE-INPUT is structurally equivalent to excluding (or isolating away by δ-shrink) zeros that lie within \(O(\delta)\) of the shifted hinge traces, and this obligation should be stated explicitly as a near-trace isolation hypothesis.

---

### Patch Packet (minimal; for v43+ integration)

* Callsign: RH-LOCAL-13  
* Result classification: CONDITIONAL  
* Closed gaps: clarifies UE-INPUT’s true local exclusion content; provides a proof-grade local pole lemma (Lemma 1) and an explicit near-trace isolation hypothesis.  
* Open: proving near-trace isolation (or an alternative δ-aware UE-INPUT) from unconditional inputs.  
* Paste-ready edits: provided under §4.  
* Dependencies: ENVELOPE (UE-INPUT), FORCE (GEO–C4 forcing/robustness) may cite Hypothesis \ref{hyp:near-trace-isolation}.  
* Referee risk notes:  
  - A referee may object that Hypothesis \ref{hyp:near-trace-isolation} is ad hoc; response: it exactly matches the resonance stress mechanism and is strictly weaker than RH (permits off-axis quartets, forbids δ-scale crowding around the traces).  
  - Lemma 1 is local/elementary; it is not a new deep input, just a bookkeeping lemma clarifying scaling.
