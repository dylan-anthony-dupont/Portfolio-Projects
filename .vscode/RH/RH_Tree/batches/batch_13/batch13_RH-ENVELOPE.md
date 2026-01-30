# Batch 13 — RH-ENVELOPE-13  
**Target:** UE-INPUT (Box 12.2.5, v42) for the completed even entire object \(E\)  
**Scope:** Prove UE-INPUT as stated, or (if impossible) give the minimal corrected statement that still closes GEO–C4, with TeX-ready patch blocks.

---

## (A) Best-shot proof attempt

### A1. Restate UE-INPUT (v42)

In v42, UE-INPUT is the derivative-field bound (Box 12.2.5):

For fixed \(\kappa\in(0,1)\), \(h=\kappa\delta\), \(v(\theta)=im+\delta e^{i\theta}\), and  
\[
\mathcal L_t(v)=f(v+t)-f(v-t),\qquad f(z)=\frac{E'(z)}{E(z)},
\]
the requested bound is: there exist **absolute** constants \(C,C'>0\) such that, for \(j=0,1,2\),
\[
\sup_{\theta\in[0,2\pi]}\ \sup_{t\in[a-h,a+h]}
\left|\partial_t\,\partial_v^{\,j}\,\mathcal L_t\big(v(\theta)\big)\right|
\ \le\ C\,\frac{\big(\log(m+3)\big)^{C'}}{a^{2+j}}.
\tag{UE-INPUT}
\]
v42 then uses the mean-value theorem in \(t\) to transfer this to \(\partial_v^j\mathcal D_{a,h}(v(\theta))\), and Lemma 12.23 to conclude  
\(\Phi^\star(m,a,\delta,h)\ll_\kappa (\delta/a)^3(\log m)^{C'}\).

### A2. Reduce \(\partial_t\partial_v^j\mathcal L_t\) to derivatives of \(f\)

Differentiate explicitly:

\[
\partial_t \mathcal L_t(v)= f'(v+t)+f'(v-t).
\]

Since \(\partial_v\) is the same as the complex derivative with respect to the argument,
\[
\partial_v^{\,j}\partial_t \mathcal L_t(v)= f^{(j+1)}(v+t)+f^{(j+1)}(v-t).
\tag{A.1}
\]

So UE-INPUT reduces to bounding \(f^{(k)}(z)\) for \(k=1,2,3\) at points
\[
z\in \{v(\theta)\pm t:\ \theta\in[0,2\pi],\ t\in[a-h,a+h]\},
\quad\text{with}\quad v(\theta)=im+\delta e^{i\theta}.
\]

### A3. RH-free representation of \(f^{(k)}\) and baseline bound

Because \(E\) is an even entire order-1 completion of zeta in the \(v\)-frame (v42, “completed even entire object”), it admits a genus-1 Hadamard product. In particular, for \(k\ge 1\),
\[
f^{(k)}(z)=\frac{d^k}{dz^k}\left(\frac{E'}{E}(z)\right)
= (-1)^k\,k!\sum_{\rho\in Z(E)}\frac1{(z-\rho)^{k+1}},
\tag{A.2}
\]
where the series converges absolutely (since exponent \(k+1\ge 2\)).

Hence
\[
|f^{(k)}(z)|\ \le\ k!\sum_{\rho\in Z(E)}\frac1{|z-\rho|^{k+1}}.
\tag{A.3}
\]

Assume **buf-admissibility** for the shifted traces (v42 Definition 12.19), i.e.
\[
\operatorname{dist}\big(z,Z(E)\big)\ \ge\ \mathrm{buf}\cdot \delta
\quad\text{for all shifted points }z=v(\theta)\pm(a\pm h).
\tag{A.4}
\]

Then every denominator obeys \(|z-\rho|\ge \mathrm{buf}\,\delta\). Split the zero sum into:
- “near” zeros with \(|\Im\rho-\Im z|\le 2\),
- “far” zeros with \(|\Im\rho-\Im z|>2\).

Using only the Riemann–von Mangoldt zero counting for \(\xi\) (hence for \(E\)), one has
\[
\#\{\rho\in Z(E): |\Im\rho-T|\le 2\}\ \ll\ \log(T+3)
\quad(T\asymp m),
\tag{A.5}
\]
unconditionally.

Therefore the near part contributes
\[
\sum_{|\Im\rho-\Im z|\le 2}\frac1{|z-\rho|^{k+1}}
\ \ll\ \frac{\log(m+3)}{(\mathrm{buf}\,\delta)^{k+1}}.
\tag{A.6}
\]

For the far part, \(|z-\rho|\gg |\Im\rho-\Im z|\), and dyadic decomposition with (A.5) yields
\[
\sum_{|\Im\rho-\Im z|> 2}\frac1{|z-\rho|^{k+1}}
\ \ll\ \log(m+3)\sum_{n\ge 2}\frac1{n^{k+1}}
\ \ll\ \log(m+3),
\tag{A.7}
\]
since \(k+1\ge 2\).

Combining (A.3), (A.6), (A.7) gives the **provable baseline**:
\[
\boxed{
\sup_{z\in\text{shifted traces}}
|f^{(k)}(z)|
\ \ll_k\ 
\frac{\log(m+3)}{(\mathrm{buf}\,\delta)^{k+1}}
\qquad (k=1,2,3).
}
\tag{A.8}
\]

Insert (A.8) into (A.1) with \(k=j+1\) to obtain
\[
\boxed{
\sup_{\theta}\sup_{t\in[a-h,a+h]}
\left|\partial_t\,\partial_v^{\,j}\mathcal L_t(v(\theta))\right|
\ \ll_j\ 
\frac{\log(m+3)}{(\mathrm{buf}\,\delta)^{2+j}}
\qquad (j=0,1,2).
}
\tag{A.9}
\]

### A4. What this yields under the nominal policy \(\delta=\eta a/\log^2(m+3)\)

Under \(\delta=\eta a/\log^2(m+3)\),
\[
\delta^{-(2+j)} = \eta^{-(2+j)}\,\frac{(\log(m+3))^{2(2+j)}}{a^{2+j}}.
\]

So (A.9) becomes
\[
\sup_{\theta,t}\left|\partial_t\,\partial_v^{\,j}\mathcal L_t(v(\theta))\right|
\ \ll_j\ 
\eta^{-(2+j)}\,
\frac{(\log(m+3))^{\,2(2+j)+1}}{a^{2+j}}.
\tag{A.10}
\]

For \(j=2\) this is \(\ll \eta^{-4}(\log(m+3))^9/a^4\).

**Crucial point:** (A.10) is the *natural RH-free scale* for this quantity once the shifted traces are only known to stay \(\asymp \delta\) away from zeros. It is also **saturated by the one-quartet toy model** (up to constant/log factors), because the local singular kernel has size \(\asymp \delta^{-(2+j)}\) on the shifted traces when an off-axis quartet exists.

### A5. Why this does *not* close GEO–C4 (and why UE-INPUT “as used” is RH-equivalent)

v42’s “Payoff” line after Box 12.2.5 asserts:
\[
\Phi^\star(m,a,\delta,h)\ \ll_\kappa\ (\delta/a)^3(\log m)^{C'}\ =\ o(1).
\]

But if the only available bound is at the baseline scale (A.10), then the induced \(A(m,a)\) in Lemma 12.23 is at least of order \(\eta^{-4}(\log m)^9\) (to dominate the \(j=2\) case). Lemma 12.23 then gives only
\[
\Phi^\star\ \ll\ \eta^{-4}(\log m)^9\cdot (\delta/a)^3
\ =\ \eta^{-4}(\log m)^9\cdot \frac{\eta^3}{(\log m)^6}
\ =\ \eta^{-1}(\log m)^3,
\]
which **diverges** with \(m\). This is far too weak to contradict the forcing lower bound \(\Phi^\star\ge 2\sqrt\pi\) (Lemma 12.22) even qualitatively.

More structurally:

* If an off-axis quartet at \(\pm a\pm i m\) exists, then \(\mathcal D_{a,h}\) has poles at \(v=im\pm h\) inside the witness disk (this is exactly the dipole kernel computed in Lemma 12.21), and the \(k=2\) harmonic channel of \(\Im \mathcal D_{a,h}\) has **constant-size** contribution after the normalization in \(\Phi^\star\).  
* Any RH-free estimate that only controls \(f^{(k)}\) by “distance-to-zeros” at scale \(\delta\) cannot rule this out; it produces (A.10), which is compatible with (indeed, saturated by) the off-axis quartet model.

**Conclusion (for this batch):** A direct RH-free proof of UE-INPUT in the strength required to make \(\Phi^\star=o(1)\) is not obtainable from the classical “Hadamard + counting + Stirling” toolkit alone. Achieving the needed improvement would itself exclude the pole-at-\(im\pm h\) configuration and is therefore RH-equivalent in effect.

---

## (B) Minimal corrected UE-INPUT (what is actually provable vs what is needed)

### B1. Provable baseline (honest statement)

The strongest statement I can justify *purely* from RH-free Hadamard/counting inputs is the baseline (A.9):

> **Lemma (UE-INPUT\(_{\rm base}\), RH-free).**  
> Under the buf-admissibility hypothesis for the shifted traces, for each \(j=0,1,2\),
> \[
> \sup_{\theta}\sup_{t\in[a-h,a+h]}
> \left|\partial_t\,\partial_v^{\,j}\mathcal L_t(v(\theta))\right|
> \ \le\ C_j\ \frac{\log(m+3)}{(\mathrm{buf}\,\delta)^{2+j}}.
> \]
> (Absolute constants \(C_j\) independent of \((m,a,\delta)\).)

This lemma is true but **insufficient** for closure: it does not yield an upper bound \(<\pi/2\) (or even \(o(1)\)) for \(\Phi^\star\) under the nominal \(\delta\)-policy, and is consistent with the one-quartet forcing model.

### B2. The minimal “closure-sufficient” corrected UE-INPUT is RH-equivalent

To actually close GEO–C4, one needs a UE-INPUT that forces
\[
\Phi^\star(m,a,\delta,h)\to 0 \quad (m\to\infty),
\]
uniformly for \(a\in(0,1)\) at \(\delta=\eta a/\log^2(m+3)\).

Via Lemma 12.23, this requires that the \(j=2\) field bound be **strictly better** than the dipole scale \(\delta^{-4}\) by at least a \(\log^{2}\) factor (at the nominal \(\delta\)-policy), i.e. schematically:
\[
\sup_{\theta,t}\left|\partial_t\partial_v^2\mathcal L_t(v(\theta))\right|
\ \ll\ \frac{(\log m)^{C'_{\rm eff}}}{a^4}
\quad\text{with}\quad C'_{\rm eff}< 6,
\]
and with **no hidden \(\eta^{-4}\)** dependence.

But the one-quartet model gives a matching *lower* scale (for some \(\theta\) and \(t\sim a\)):
\[
\left|\partial_t\partial_v^2\mathcal L_t(v(\theta))\right|
\ \asymp\ \delta^{-4}
\ =\ \eta^{-4}\frac{(\log m)^8}{a^4}.
\]

So any UE-INPUT strong enough to force \(\Phi^\star=o(1)\) must **exclude the quartet configuration**, i.e. it is RH-equivalent in effect.

> **Implication lemma (RH-equivalence direction).**  
> If UE-INPUT holds with constants independent of \(\eta\) and with log exponent \(C'<8\) in the \(j=2\) case (in the regime \(\delta=\eta a/\log^2(m+3)\)), then no off-axis quartet \(\{\pm a\pm i m\}\subset Z(E)\) can exist at that height.

This is already the logic v42 intends (FORCE + UE ⇒ contradiction); the key correction is: **the bound must be strong enough to beat the dipole scale**. The manuscript currently does not isolate this quantitative necessity.

### B3. Minimal patch that is still sufficient to close GEO–C4

There are two “minimal correction” options:

1) **Honesty patch (recommended):** keep GEO–C4, but explicitly mark UE-INPUT as RH-equivalent/open at proof-grade level (no “o(1)” claim unless the exponent budget is specified and proven).  
2) **Technology patch (not minimal, but closure-sufficient):** replace UE-INPUT by a *different* analytic input that directly bounds the relevant residue/Laurent coefficient (the \(k=2\) pole channel) in a way that excludes poles at \(v=im\pm h\). This is new technology beyond the classical toolkit and is not currently present.

For Batch-13 deliverable, I provide (1) as the minimal corrected statement that is logically coherent and preserves the manuscript’s dependency map.

---

## (C) Why the corrected framing still closes GEO–C4 (conditional closure statement)

If one supplies an analytic input that truly yields:
\[
\Phi^\star(m,a,\delta,h)\le \varepsilon(m,a),\quad \varepsilon(m,a)\to 0 \text{ as } m\to\infty,
\]
uniformly in \(a\in(0,1)\) and at nominal \(\delta=\eta a/\log^2(m+3)\), then the already proven forcing lemma (Lemma 12.22) gives \(\Phi^\star\ge 2\sqrt\pi\) whenever an off-axis quartet exists. This contradiction forces \(a=0\) for all large heights, hence PHU and RH, exactly as v42 states.

The issue is not the logical closure chain; it is that the **only RH-free baseline bounds** for the needed derivatives operate at the **dipole scale** and therefore cannot yield the required \(\varepsilon(m,a)\to0\) without excluding the quartet (i.e. without proving the desired conclusion).

---

## (D) TeX patch (copy-paste) for v42

### D1. Replace Box 12.2.5 with a corrected statement + baseline lemma

```tex
% --- PATCH START: replace the current Box 12.2.5 text ---

\subsubsection{The single open statement (corrected quantitative gate)}

\begin{tcolorbox}[title={UE-INPUT (v42, single active statement; quantitative gate)}]
Fix $\kappa\in(0,1)$ and let $E$ be the completed even entire object in the $v$--plane.
For all sufficiently large $m$ and all $a\in(0,1)$, set the nominal scale
\[
\delta=\delta(m,a):=\frac{\eta a}{(\log(m+3))^{2}},\qquad h:=\kappa\delta,
\]
and (if needed) shrink $\delta$ \emph{within a fixed-factor range} to enforce buf--admissibility
(Definition~\ref{def:shift-admissible-hinge}).

\medskip
\noindent\textbf{OPEN quantitative UE gate.}
Prove an RH-free upper bound, uniform in $a\in(0,1)$ and large $m$, that implies
\[
\Phi^\star(m,a,\delta,h)\ \le\ \varepsilon(m,a),\qquad \varepsilon(m,a)\to 0 \ \ (m\to\infty).
\]
A sufficient derivative-field formulation is the existence of constants $C,C'>0$
\emph{with an explicit exponent budget $C'<6$} such that for $j=0,1,2$,
\[
\sup_{\theta\in[0,2\pi]}\ \sup_{t\in[a-h,a+h]}
\Bigl|\partial_t\,\partial_v^{\,j}\mathcal L_t\bigl(v(\theta)\bigr)\Bigr|
\ \le\ C\,\frac{(\log(m+3))^{C'}}{a^{2+j}}.
\]
(Without $C'<6$ the decay $\Phi^\star=o(1)$ at the nominal policy does \emph{not} follow.)
\end{tcolorbox}

\begin{lemma}[UE-INPUT$_{\rm base}$ (RH-free baseline bound)]
\label{lem:ue-input-baseline}
Assume buf--admissibility for the shifted traces at $(a,h)$ with buffer $\mathrm{buf}\in(0,1)$.
Then for each $j\in\{0,1,2\}$,
\[
\sup_{\theta\in[0,2\pi]}\ \sup_{t\in[a-h,a+h]}
\Bigl|\partial_t\,\partial_v^{\,j}\mathcal L_t\bigl(v(\theta)\bigr)\Bigr|
\ \ll_j\ \frac{\log(m+3)}{(\mathrm{buf}\,\delta)^{2+j}},
\]
with an absolute implied constant.  This bound is consistent with (and sharp in) the
one-quartet dipole model, and by itself does not yield $\Phi^\star=o(1)$.
\end{lemma}

% --- PATCH END ---
```

### D2. Proof skeleton for Lemma `lem:ue-input-baseline`

```tex
\begin{proof}[Proof sketch]
Write $f=E'/E$. Then $\partial_t\mathcal L_t(v)=f'(v+t)+f'(v-t)$ and hence
$\partial_v^{\,j}\partial_t\mathcal L_t(v)=f^{(j+1)}(v+t)+f^{(j+1)}(v-t)$.
Since $E$ is entire of order $1$ it has a genus-$1$ Hadamard product, and for $k\ge 1$,
$f^{(k)}(z)=(-1)^k k!\sum_{\rho\in Z(E)}(z-\rho)^{-(k+1)}$ with absolute convergence.
Under buf--admissibility, every shifted point $z=v(\theta)\pm(a\pm h)$ stays at distance
$\ge \mathrm{buf}\,\delta$ from $Z(E)$, so each summand has modulus $\le (\mathrm{buf}\,\delta)^{-(k+1)}$.
Split zeros into $|\Im\rho-\Im z|\le 2$ and its complement.  The local count in a window of length
$4$ is $\ll\log(m+3)$ by Riemann--von Mangoldt, and the far tail converges for $k+1\ge 2$.
This yields $|f^{(k)}(z)|\ll_k \log(m+3)\,(\mathrm{buf}\,\delta)^{-(k+1)}$, hence the stated bound.
\end{proof}
```

---

## Patch Packet

* **Callsign:** RH-ENVELOPE-13  
* **Result classification:** **CONDITIONAL / NO-GO for “UE-INPUT closes v42 as written”**  
* **Target gaps closed (by ID):**  
  * UE-INPUT audit: **quantitative gate identified** (missing exponent-budget condition)  
* **Target gaps still open (by ID):**  
  * UE-INPUT (Box 12.2.5) remains OPEN in a strength that would actually force \(\Phi^\star=o(1)\).  
* **Key conclusions (≤5 bullets):**
  1. A purely RH-free Hadamard/counting argument gives only a **baseline** derivative bound at the **dipole scale** \(\sim \log(m)/\delta^{2+j}\), which is **sharp** in the one-quartet model.  
  2. Plugging baseline bounds into Lemma 12.23 yields \(\Phi^\star\) upper bounds that **grow** with \(m\) under the nominal \(\delta=\eta a/\log^2\) policy; no contradiction with forcing.  
  3. The “\(\Phi^\star=o(1)\)” payoff in Box 12.2.5 is **quantitatively under-specified**; it requires an explicit exponent budget (e.g. \(C'<6\)) and (effectively) exclusion of dipole-scale singularities.  
  4. Any UE-INPUT strong enough to yield \(\Phi^\star\to 0\) necessarily **excludes the off-axis quartet configuration** and is therefore RH-equivalent in effect.  
  5. Minimal patch for proof-grade honesty: separate **provable baseline** from the **closure-sufficient OPEN** gate, and remove the unqualified “\(=o(1)\)” assertion.
* **Paste-ready manuscript edits:** provided in (D1)–(D2).
* **Dependencies on other branches:** none required for the quantitative-gate correction (this is internal hygiene).  
* **Referee risk notes (anticipated objections + how addressed):**
  - **Objection:** “You didn’t prove UE-INPUT, only a weaker lemma.”  
    **Response:** Correct; the weaker lemma is the strongest available from standard RH-free tools and is sharp in the toy forcing model. This demonstrates the missing quantitative gate in the manuscript.  
  - **Objection:** “Maybe constants are chosen so \(C'<6\) anyway.”  
    **Response:** No such proof exists in v42; moreover the dipole model forces \(j=2\) growth at least \((\log m)^8/a^4\) when an off-axis quartet exists, so any \(C'<8\) bound is already exclusionary.
