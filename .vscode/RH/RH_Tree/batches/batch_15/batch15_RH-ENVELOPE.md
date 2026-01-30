# Batch 15 — RH-ENVELOPE  
**Verdict:** **(2) NO‑GO (UE‑INPUT is RH‑strength at closure‑grade parameter scales).**  

This note treats GEO‑C4 forcing + endpoint construction + UE‑REDUCE as locked. The only active surface is UE‑INPUT (v43):  
\[
\boxed{\ \int_0^{2\pi}\bigl|\mathcal D_{a,h}(v(\theta))\bigr|\,d\theta \ \le\ C\;\frac{h(\log(m+3))^{C'}}{a^2}\ }
\quad
\Bigl(v(\theta)=im+\delta e^{i\theta},\ \delta=\eta\frac{a}{(\log(m+3))^2},\ h=\kappa\delta\Bigr),
\]
with \(a\in(0,1)\), \(\kappa\in(0,1)\), \(m\ge 10\), and shift/buffer admissibility.

My conclusion is that any UE‑INPUT strong enough to yield the required **\(\Phi^\star<\pi/2\)** (i.e. strong enough to make the GEO‑C4 *upper bound* small at the nominal \(\delta\)-policy) is effectively equivalent to excluding an off‑axis quartet at \((\pm a\pm im)\). In that sense, UE‑INPUT is a *closure lemma*, not a “routine envelope estimate.”

I. **Objects and the local kernel expansion**  
We use the locked notation: \(E\) is even entire in the \(v\)-frame, \(f=E'/E\), and  
\[
\mathcal L_t(v)=f(v+t)-f(v-t),\qquad
\mathcal D_{a,h}(v)=\mathcal L_{a+h}(v)-\mathcal L_{a-h}(v).
\]
A useful algebraic identity (no assumptions):
\[
\mathcal D_{a,h}(v)=\bigl(f(v+a+h)-f(v+a-h)\bigr)\;+\;\bigl(f(v-a+h)-f(v-a-h)\bigr).
\tag{1}\label{eq:D-split}
\]

Because \(E\) is entire of order \(1\) (completed \(\xi\)-type object in the program lineage), its log-derivative admits a Hadamard-style representation
\[
f(z)=\frac{E'}{E}(z)=H(z)+\sum_{\rho\in Z(E)}\frac{1}{z-\rho},
\tag{2}\label{eq:log-derivative}
\]
where \(H\) is entire and \(Z(E)\) are zeros of \(E\) counted with multiplicity (the precise \(H\) depends on the chosen canonical product normalisation; only its *holomorphy and order‑1 growth* are used below).

Plugging \eqref{eq:log-derivative} into \eqref{eq:D-split}, \(\mathcal D_{a,h}\) decomposes as:
\[
\mathcal D_{a,h}(v)=\mathcal D_{a,h}^{(H)}(v)+\sum_{\rho\in Z(E)} K_{a,h}(v;\rho),
\tag{3}\label{eq:D-kernel-decomp}
\]
with
\[
\mathcal D_{a,h}^{(H)}(v)=\bigl(H(v+a+h)-H(v+a-h)\bigr)+\bigl(H(v-a+h)-H(v-a-h)\bigr),
\]
and the **zero‑kernel**
\[
K_{a,h}(v;\rho)
=\Bigl(\frac{1}{v+a+h-\rho}-\frac{1}{v+a-h-\rho}\Bigr)
+\Bigl(\frac{1}{v-a+h-\rho}-\frac{1}{v-a-h-\rho}\Bigr).
\tag{4}\label{eq:kernel}
\]

A generic envelope bound for a single kernel is:
\[
\Bigl|\frac{1}{z+h}-\frac{1}{z-h}\Bigr|=\frac{2h}{|z^2-h^2|}
\le \frac{2h}{(|z|-h)^2},
\qquad (|z|>h).
\tag{5}\label{eq:fd-bound}
\]
Thus whenever \(|v\pm a-\rho|\ge r>h\), each bracket is \(\ll h/r^2\).

II. **NO‑GO lemma: off‑axis quartet forces an \(L^1\) blow‑up \(\gtrsim 1/\delta\)**  

### Lemma (Local quartet \(L^1\) lower bound; UE‑INPUT is closure‑strength)
Assume \(E\) is even entire and has an off‑axis quartet at height \(m\):
\[
\rho_1=a+im,\quad \rho_2=-a+im,\quad \rho_3=a-im,\quad \rho_4=-a-im
\quad\text{for some }a\in(0,1),\ m>0.
\]
Fix \(\kappa\in(0,1)\). Let \(0<\delta\le a/10\) and \(h=\kappa\delta\). Define the hinge circle
\[
v(\theta)=im+\delta e^{i\theta}.
\]
Assume the **buffer admissibility** that, on the traces \(v(\theta)\pm a\pm t\) with \(t\in[0,h]\), the only zeros within distance \(\le a/5\) are \(\rho_1,\rho_2\) (this is consistent with the intended “shift/collar admissibility” regime and can always be enforced by shrinking \(\delta\) relative to \(a\) if needed).

Then there exist constants \(c_0=c_0(\kappa)>0\) and \(m_0=m_0(\kappa,\eta)\) such that for all \(m\ge m_0\),
\[
\int_0^{2\pi}\bigl|\mathcal D_{a,h}(v(\theta))\bigr|\,d\theta
\ \ge\ \frac{c_0}{\delta}.
\tag{6}\label{eq:L1-lower}
\]
Consequently, under the nominal policy \(\delta=\eta a/(\log(m+3))^2\),
\[
\int_0^{2\pi}\bigl|\mathcal D_{a,h}(v(\theta))\bigr|\,d\theta
\ \ge\ \frac{c_0}{\eta}\;\frac{(\log(m+3))^2}{a}.
\tag{7}\label{eq:L1-lower-policy}
\]

#### Proof (referee‑grade skeleton)
1. **Extract the two “near” poles \(\rho_1,\rho_2\).**  
Write \(f(z)=\frac1{z-\rho_1}+\frac1{z-\rho_2}+R(z)\), where \(R\) is analytic on the buffered trace region (by admissibility) and includes all other zeros and \(H(z)\).

2. **Compute the contribution of \(\rho_1\) and \(\rho_2\) explicitly.**  
Evaluate \(\mathcal D_{a,h}\) using \eqref{eq:D-split} at \(v(\theta)=im+\delta e^{i\theta}\).  
For \(\rho_1=a+im\), the first bracket in \eqref{eq:D-split} contributes:
\[
\frac{1}{v+a+h-\rho_1}-\frac{1}{v+a-h-\rho_1}
=\frac{1}{\delta e^{i\theta}+h}-\frac{1}{\delta e^{i\theta}-h}
=\frac{2h}{h^2-\delta^2e^{2i\theta}}.
\]
For \(\rho_2=-a+im\), the second bracket contributes the same expression (because \(v-a\pm h-\rho_2=\delta e^{i\theta}\pm h\)).  
Therefore the **local main term** is
\[
M(\theta):=\frac{4h}{h^2-\delta^2e^{2i\theta}}.
\tag{8}\label{eq:Mtheta}
\]

3. **Uniform lower bound for the main term.**  
Since \(h=\kappa\delta\),
\[
|M(\theta)|
=\frac{4\kappa}{\delta}\cdot \frac{1}{|\,\kappa^2-e^{2i\theta}\,|}
\ge \frac{4\kappa}{\delta}\cdot \frac{1}{1+\kappa^2}
=: \frac{c_M(\kappa)}{\delta},
\tag{9}\label{eq:M-lower}
\]
because \(|\kappa^2-e^{2i\theta}|\le 1+\kappa^2\).

4. **Bound the remainder \(R\)-contribution on the trace.**  
By analyticity of \(R\) on the buffered trace region and standard order‑1 growth for \(\log E\) (Hadamard product + Stirling for the gamma part, plus classical zero counting for the zero-sum), one gets a bound of the form
\[
\sup_{\theta}\Bigl(
|R(v(\theta)+a+h)-R(v(\theta)+a-h)|
+|R(v(\theta)-a+h)-R(v(\theta)-a-h)|
\Bigr)
\ \le\ C_R\;\frac{h\log(m+3)}{a^2}.
\tag{10}\label{eq:R-bound}
\]
(Heuristic: each finite difference is \(\le 2h\sup|R'|\); and \(\sup|R'|\ll \log(m+3)/a^2\) provided the evaluation points stay at distance \(\gg a\) from all zeros except \(\rho_{1,2}\), which were removed.)

5. **Dominate the remainder by the main term (large \(m\)).**  
Under nominal \(\delta\)-policy, \(1/\delta\asymp (\log(m+3))^2/a\) while the RHS of \eqref{eq:R-bound} is \(\asymp h\log(m+3)/a^2=\kappa\delta\log(m+3)/a^2\asymp \kappa\eta/(a\log(m+3))\).  
Thus for \(m\) sufficiently large (depending on \(\kappa,\eta,C_R\)), the remainder bound is \(\le \tfrac12 c_M(\kappa)/\delta\). Hence
\[
|\mathcal D_{a,h}(v(\theta))|
\ge |M(\theta)|-|(\mathcal D_{a,h}-M)(v(\theta))|
\ge \frac{c_M(\kappa)}{2\delta}
\quad\text{for all }\theta.
\]
Integrating over \(\theta\in[0,2\pi]\) gives \eqref{eq:L1-lower} with \(c_0=\pi c_M(\kappa)\). \(\square\)

---

III. **Why this certifies UE‑INPUT is RH‑strength (at closure‑grade scales)**  

GEO‑C4 uses UE‑REDUCE (locked):
\[
\Phi^\star \ \le\ C\frac{\delta^2}{h}\int_0^{2\pi}|\mathcal D_{a,h}(v(\theta))|\,d\theta.
\tag{11}\label{eq:UE-reduce}
\]
Under the quartet lower bound \eqref{eq:L1-lower}, and \(h=\kappa\delta\),
\[
\Phi^\star \ \gtrsim\ \frac{\delta^2}{h}\cdot\frac{1}{\delta} = \frac{\delta}{h}=\frac{1}{\kappa},
\]
i.e. **\(\Phi^\star\) is bounded below by a positive constant** in the one-quartet model. Therefore, to force the contradiction \(\Phi^\star<\pi/2\) at large \(m\), the UE mechanism must *exclude* the quartet configuration itself. That is exactly the closure problem.

More quantitatively, compare the lower bound \eqref{eq:L1-lower-policy} with UE‑INPUT:
\[
\frac{c_0}{\eta}\frac{(\log(m+3))^2}{a}
\ \lesssim\ 
C\frac{h(\log(m+3))^{C'}}{a^2}
=C\frac{\kappa\delta(\log(m+3))^{C'}}{a^2}
=C\frac{\kappa\eta(\log(m+3))^{C'-2}}{a}.
\]
This would force \((\log(m+3))^{4-C'}\lesssim \kappa\eta^2\). Hence:

* if \(C'<4\), UE‑INPUT is **incompatible** with a quartet for all sufficiently large \(m\);
* if \(C'=4\), UE‑INPUT still forces \(\eta\) to be **not small** (in tension with the closure regime that typically wants \(\eta\) small to tighten the circle);
* if \(C'>4\), UE‑INPUT is too weak to give \(\Phi^\star=o(1)\) via \eqref{eq:UE-reduce} (it would make \(\Phi^\star\) grow like \((\log m)^{C'-4}\)).

So at the strength actually needed for GEO‑C4 closure, UE‑INPUT is not a “routine estimate.” It is the RH‑exclusion statement in analytic clothing.

IV. **Optional replacement interface (not claimed provable; offered for v44 clarity)**  

If the program wants a *cleaner* statement of what UE is really doing, one can replace the absolute \(L^1\) UE‑INPUT by an explicitly “Weil/explicit-formula identifiable” **linear statistic**:

*Define the \(k=2\) coefficient functional*
\[
\mathfrak C_2(m,a,\delta,h)\ :=\ \Bigl|\int_0^{2\pi}\mathcal D_{a,h}\bigl(im+\delta e^{i\theta}\bigr)e^{-2i\theta}\,d\theta\Bigr|.
\tag{12}\label{eq:C2}
\]

Because \(P_2\) is exactly the projection onto \(\sin 2\theta,\cos 2\theta\), \(|P_2\psi|_{L^2}\) is equivalent (up to an explicit constant) to \(\mathfrak C_2\) (this is an identity of Fourier analysis, no estimates). This would make the open UE surface explicitly “harmonic coefficient control” rather than absolute \(L^1\) control.

However, \(\mathfrak C_2\) still detects the local poles and is still forced to be \(\asymp 1/\delta\) in the one‑quartet model (same scaling as above), so it does **not** bypass RH‑strength; it merely expresses the closure target in a more structurally transparent way.

V. **Reader‑guide structural corollaries (Part III) — relevance check**  

The reader‑guide and early manuscripts explicitly label the parity projectors / rectifier / \(\pi/2\) carrier identities as **structural corollaries after the collapse \(a(m)=0\)**, not analytic inputs. For example, the “Toolbox → structural consequences” discussion states that these items “are not inputs to the analytic proof” and become corollaries once \(a(m)=0\) is proved. This is consistent with the structural corollaries featuring \(\chi_4\), \(P_{\rm odd},P_{\rm even}\), and \(\sin(\pi n/2),\cos(\pi n/2)\) carrier collapses. As such, they cannot be imported into UE‑INPUT without circularity (they live on the *post‑RH* side of the implication).  

That said, they may still be valuable as a guide for what the *right* analytic witness should target, but they do not by themselves supply an RH‑free estimate for \(\int|\mathcal D|\).

VI. **Patch map (v43 → v44)**  

**Insert immediately after the UE‑INPUT box (or replace the box) a new lemma + remark:**

1) **Lemma:** “Off‑axis quartet \(\Rightarrow\) \(L^1\) blow‑up \(\gtrsim 1/\delta\)” (Lemma \ref{lem:UE-input-nogo-quartet}).  
2) **Remark:** “Any UE‑INPUT with log‑power \(\le 4\) sufficient for \(\Phi^\star<\pi/2\) is equivalent to excluding quartets; this is the closure lemma.”

This makes the manuscript audit‑honest: UE‑INPUT is not an envelope routine; it is the RH exclusion itself unless new deep technology is added.

---

## Paste‑ready TeX blocks (drop‑in)

```tex
% --- Insert near box:ue-input (v43→v44) ---
\begin{lemma}[NO-GO for UE-INPUT: local quartet forces $L^1$ blow-up]
\label{lem:UE-input-nogo-quartet}
Assume $E$ is even entire and has an off-axis quartet at height $m$:
\[
\rho_1=a+im,\ \rho_2=-a+im,\ \rho_3=a-im,\ \rho_4=-a-im
\quad\text{for some }a\in(0,1),\ m>0.
\]
Fix $\kappa\in(0,1)$ and let $0<\delta\le a/10$, $h=\kappa\delta$, and
$v(\theta)=im+\delta e^{i\theta}$.
Assume the shifted traces $v(\theta)\pm a\pm t$ ($t\in[0,h]$) are admissible in the sense that,
within distance $\le a/5$, the only zeros encountered are $\rho_1,\rho_2$.

Then there exists $c_0=c_0(\kappa)>0$ and $m_0=m_0(\kappa,\eta)$ such that for all $m\ge m_0$,
\[
\int_0^{2\pi}\bigl|\mathcal D_{a,h}(v(\theta))\bigr|\,d\theta \ \ge\ \frac{c_0}{\delta}.
\]
In particular under the nominal policy $\delta=\eta a/(\log(m+3))^2$,
\[
\int_0^{2\pi}\bigl|\mathcal D_{a,h}(v(\theta))\bigr|\,d\theta
\ \ge\ \frac{c_0}{\eta}\,\frac{(\log(m+3))^2}{a}.
\]
\end{lemma}

\begin{proof}[Proof sketch (load-bearing)]
Write $f=E'/E$ and decompose $f(z)=\frac1{z-\rho_1}+\frac1{z-\rho_2}+R(z)$, where $R$ is analytic
on the buffered trace region.
Using $\mathcal D_{a,h}(v)=[f(v+a+h)-f(v+a-h)]+[f(v-a+h)-f(v-a-h)]$, the poles at $\rho_1,\rho_2$
contribute the explicit main term
\[
M(\theta)=\frac{4h}{h^2-\delta^2e^{2i\theta}},
\]
hence $|M(\theta)|\ge \frac{4\kappa}{(1+\kappa^2)\delta}$ uniformly in $\theta$.
The remainder satisfies a uniform bound of the form
$\sup_\theta |(\mathcal D_{a,h}-M)(v(\theta))|\ll \frac{h\log(m+3)}{a^2}$ by analyticity of $R$
and order-$1$ growth of $E$ away from zeros.
Under the nominal coupling $\delta=\eta a/\log^2(m+3)$ and $h=\kappa\delta$, the remainder term is
$o(1/\delta)$ as $m\to\infty$, so $|\mathcal D_{a,h}(v(\theta))|\ge c/\delta$ for all $\theta$ and
integration gives the claim.
\end{proof}

\begin{remark}[Interpretation]
\label{rem:UE-input-closure-strength}
Lemma~\ref{lem:UE-input-nogo-quartet} shows that any UE-INPUT estimate strong enough to yield
$\Phi^\star=o(1)$ (hence $\Phi^\star<\pi/2$ for $m$ large) must exclude the quartet itself.
Thus UE-INPUT at closure-strength is not a routine envelope bound; it is the RH-exclusion step.
\end{remark}
```

---

## Dependency latch

This NO‑GO lemma uses only:

* the algebraic identity \(\mathcal D_{a,h}=[f(\cdot+a+h)-f(\cdot+a-h)]+[f(\cdot-a+h)-f(\cdot-a-h)]\);  
* the log-derivative pole structure \(f=E'/E\) for an entire function;  
* admissibility (“shift/buffer avoids other zeros”), and the standard order‑1 growth bounds for the completed object to control the analytic remainder.

It plugs directly at the UE‑INPUT box and does not touch GEO‑C4 forcing, the \(k=2\) endpoint, or the reduction inequality.

---

## Patch Packet (mandatory)

* **Callsign:** RH‑ENVELOPE  
* **Result classification:** **FAIL (NO‑GO delivered)**  
* **Target gaps closed (by ID):** UE‑INPUT status clarified as **closure‑strength** (eliminates “routine proof” drift).  
* **Target gaps still open (by ID):** UE‑INPUT itself (or a strictly stronger replacement witness) remains the single active closure brick.  
* **Key conclusions (≤5 bullets):**
  1. An off‑axis quartet at \((\pm a\pm im)\) forces \(\int_0^{2\pi}|\mathcal D_{a,h}(v(\theta))|d\theta\gtrsim 1/\delta\).
  2. Under nominal coupling \(\delta=\eta a/\log^2(m+3)\), this lower bound is \(\gtrsim (\log m)^2/a\), hence prevents \(\Phi^\star=o(1)\).
  3. Therefore UE‑INPUT at any strength sufficient to yield \(\Phi^\star<\pi/2\) is effectively equivalent to excluding off-axis quartets; it is RH‑strength.
  4. Any “envelope proof” of UE‑INPUT must introduce genuinely new technology (not generic \(\xi'/\xi\) bounds).
  5. A cleaner (optional) interface is to state the open UE target directly as \(k=2\) harmonic coefficient control, but it does not bypass RH‑strength.
* **Paste‑ready manuscript edits:** included above (Lemma \ref{lem:UE-input-nogo-quartet} + Remark \ref{rem:UE-input-closure-strength}).  
* **Dependencies on other branches:** none (uses only generic entire-function log-derivative structure + admissibility).  
* **Referee risk notes (anticipated objections + how addressed):**
  1. *Objection:* “Remainder bound \(\ll h\log(m)/a^2\) not fully proved.”  
     *Response:* The NO‑GO only needs it to be \(o(1/\delta)\) under nominal coupling; a standard order‑1 Hadamard product + zero-counting estimate supplies this once traces are buffered away from zeros.
  2. *Objection:* “Admissibility hypothesis hides the conclusion.”  
     *Response:* The lemma assumes only that the two relevant poles \(\rho_1,\rho_2\) are isolated on the trace; this is consistent with the program’s own shift/buffer admissibility policy and does not preclude the quartet.
  3. *Objection:* “Could cancellations reduce \(|\mathcal D|\)?”  
     *Response:* The local main term has uniform size \(\asymp 1/\delta\) and dominates any order‑\(\log(m)\) remainder when \(\delta=\eta a/\log^2(m)\) and \(m\) is large, so cancellation cannot suppress the absolute value.
