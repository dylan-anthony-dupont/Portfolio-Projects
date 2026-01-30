# Batch 13 — RH-BRIDGE-13  
**Mission:** Replace UE-INPUT’s pointwise/sup field bound with a **pure boundary-norm** interface that is RH-free and still yields the UE reduction bound \(\Phi^\star=o(1)\) under the nominal \(\delta\)-policy.

---

## 0) Scope and fixed objects (v42 ground truth)

This batch is **interface-only**: we do **not** change

* the forcing endpoint definition \(\Phi^\star\),
* GEO–C4,
* or the forcing lemma chain.

We only replace the **UE-INPUT** hypothesis class so the UE step no longer depends on a pointwise/supremum derivative field bound (the boxed statement `UE-INPUT (v42, single active statement)`).

We work with the v42 GEO–C4 definitions (Box `GEO–C4 hinge–circle harmonic endpoint`):

* \(C_{m,\delta}=\{v(\theta)= i m+\delta e^{i\theta}\}\),
* \(h=\kappa\delta\) with fixed \(\kappa\in(0,1)\),
* \(f=E'/E\),
* \(\mathcal L_t(v)= f(v+t)-f(v-t)\),
* \(\mathcal D_{a,h}(v)=\mathcal L_{a+h}(v)-\mathcal L_{a-h}(v)\),
* \(\psi_{a,h}(\theta)=\Im(\mathcal D_{a,h}(v(\theta)))\),
* \(\Phi^\star(m,a,\delta,h)=\dfrac{\delta^2}{h}\,\|P_2\psi_{a,h}\|_{L^2([0,2\pi])}\).

The only analytic hygiene needed here is **shift-admissibility** so that \(E(v(\theta)\pm(a\pm h))\neq 0\) for all \(\theta\), hence \(\mathcal D_{a,h}(v(\theta))\) is pointwise defined and integrable on \([0,2\pi]\).

---

## 1) Replacement UE reduction lemma (boundary \(H^1\)/\(L^1\) interface)

### Lemma (UE from \(L^1\) boundary control; no derivatives, no pointwise sup)
Let \(\psi(\theta)=\Im(\mathcal D_{a,h}(v(\theta)))\) on \(v(\theta)=im+\delta e^{i\theta}\) and define the (unnormalized) \(k=2\) Fourier coefficient
\[
\widehat\psi(2):=\int_0^{2\pi}\psi(\theta)\,e^{-2i\theta}\,d\theta.
\]
Then
\[
\|P_2\psi\|_{L^2([0,2\pi])}\ =\ \frac{1}{\sqrt{\pi}}\,|\widehat\psi(2)|
\ \le\ \frac{1}{\sqrt{\pi}}\int_0^{2\pi}|\psi(\theta)|\,d\theta
\ \le\ \frac{1}{\sqrt{\pi}}\int_0^{2\pi}\Bigl|\mathcal D_{a,h}(v(\theta))\Bigr|\,d\theta.
\]
Consequently,
\[
\boxed{\ \Phi^\star(m,a,\delta,h)\ \le\ \frac{\delta^2}{h\sqrt{\pi}}\int_0^{2\pi}\Bigl|\mathcal D_{a,h}(v(\theta))\Bigr|\,d\theta\ }.
\]

#### Proof (referee-grade, RH-free)
Since \(P_2\psi(\theta)=\alpha\cos(2\theta)+\beta\sin(2\theta)\), direct computation gives
\[
\widehat\psi(2)=\int_0^{2\pi}(\alpha\cos(2\theta)+\beta\sin(2\theta))e^{-2i\theta}\,d\theta
=\pi(\alpha-i\beta),
\]
so \(|\widehat\psi(2)|=\pi\sqrt{\alpha^2+\beta^2}\). Also,
\[
\|P_2\psi\|_{L^2}^2=\int_0^{2\pi}(\alpha\cos(2\theta)+\beta\sin(2\theta))^2\,d\theta
=\pi(\alpha^2+\beta^2),
\]
hence \(\|P_2\psi\|_{L^2}=(1/\sqrt{\pi})|\widehat\psi(2)|\).
Finally,
\[
|\widehat\psi(2)|\le \int_0^{2\pi}|\psi(\theta)|\,d\theta
\le \int_0^{2\pi}\big|\mathcal D_{a,h}(v(\theta))\big|\,d\theta,
\]
since \(|\Im z|\le |z|\). This proves the bound for \(\Phi^\star\). \(\square\)

---

## 2) New UE-INPUT (replace the v42 pointwise/sup derivative field bound)

### UE-INPUT\(^\mathbf{(H^1)}\) (proposed replacement)
Replace Box `UE-INPUT (v42, single active statement)` with the following boundary-norm hypothesis:

> Fix \(\kappa\in(0,1)\) and let \(E\) be the completed even entire object in the \(v\)-plane.  
> For all sufficiently large \(m\) and all \(a\in(0,1)\), set the nominal scale
> \[
> \delta=\delta(m,a):=\eta\,\frac{a}{(\log(m+3))^2},\qquad h:=\kappa\delta,
> \]
> and allow smaller \(\delta\) if needed to enforce \(\mathrm{buf}\)-shift-admissibility.  
> Prove that there exist absolute constants \(C,C'>0\) such that
> \[
> \boxed{\ 
> \int_0^{2\pi}\Bigl|\mathcal D_{a,h}\bigl(v(\theta)\bigr)\Bigr|\,d\theta
> \ \le\ 
> C\cdot h\,\frac{(\log(m+3))^{C'}}{a^{2}}
> }\tag{UE-INPUT\(^\mathrm{(H^1)}\)}
> \]
> (equivalently, \(\|\mathcal D_{a,h}\|_{H^1(C_{m,\delta})}\ll h(\log m)^{C'}/a^2\) in the normalized Hardy \(H^1\) boundary norm).

**Payoff chain:** By the lemma in §1,
\[
\Phi^\star(m,a,\delta,h)\ \ll_\kappa\ \frac{\delta^2}{h}\cdot h\,\frac{(\log m)^{C'}}{a^2}
\ =\ (\log m)^{C'}\Big(\frac{\delta}{a}\Big)^2
\ =\ \eta^2\,\frac{(\log m)^{C'}}{(\log(m+3))^{4}}
\ =\ o(1)
\]
provided \(C'<4\). (This is a strictly weaker UE requirement than the v42 integration-by-parts reduction, but still closes the contradiction against the forcing constant.)

---

## 3) Explicit chain (DAG) from the new interface to \(\Phi^\star=o(1)\)

**Inputs fixed by GEO–C4:**

* endpoint definition \(\Phi^\star=\dfrac{\delta^2}{h}\|P_2\psi\|_{L^2}\),
* forcing lemma: off-axis quartet \((\pm a\pm i m)\Rightarrow \Phi^\star\ge c_0(\kappa)>0\).

**New UE interface:**

* UE-INPUT\(^\mathrm{(H^1)}\): \(\displaystyle \int_0^{2\pi}|\mathcal D_{a,h}(v(\theta))|\,d\theta \ll h(\log m)^{C'}/a^2\).

**Bridge lemma (this batch):**

* \(\Phi^\star \le \dfrac{\delta^2}{h}\cdot C \int|\mathcal D_{a,h}(v(\theta))|\,d\theta\).

**Conclusion:**

* \(\Phi^\star \ll (\log m)^{C'}(\delta/a)^2 = \eta^2 (\log m)^{C'-4}=o(1)\) for \(C'<4\).

---

## 4) Non-circularity audit (why this is RH-free)

1. **No RH smuggling.** Nothing here assumes zeros lie on \(\Re(v)=0\) or uses an RH-equivalent bound.
2. **No analyticity-inside-disc assumptions.** The lemma uses only boundary values of \(\mathcal D_{a,h}\) along \(C_{m,\delta}\); it does **not** assume \(\mathcal D_{a,h}\) is holomorphic in the disk.
3. **Classical tools only.** The proof uses:
   * orthogonal projection onto \(\{\cos 2\theta,\sin 2\theta\}\),
   * Fourier coefficient identities,
   * triangle inequality and \(|\Im z|\le |z|\).
4. **Admissibility is non-circular.** The only analytic hygiene is “no zeros on the shifted traces” so \(E'/E\) is defined there. This is enforced by **shrinking \(\delta\)** (monotone admissibility) and does not assume any zero-free region in the interior.

---

## 5) Patch insertion map (v42 → next build)

### Where to patch
In v42, the relevant block is:

* `\subsubsection{UE reduction via harmonic extraction (integration by parts)}`
* Lemma `\ref{lem:geo-c4-ue-reduction}` (“UE from a derivative field bound”)
* Box `UE-INPUT (v42, single active statement)` labeled `\ref{box:ue-input-v42}`.

### How to patch (minimal)
1. **Replace** Lemma `\ref{lem:geo-c4-ue-reduction}` statement+proof with the lemma in §1.
2. **Replace** Box `UE-INPUT` with UE-INPUT\(^\mathrm{(H^1)}\) in §2.
3. **Update** the payoff line in the box: the exponent becomes \((\delta/a)^2\) (not \((\delta/a)^3\)), and the decay becomes \((\log m)^{C'-4}\) (not \((\log m)^{C'-6}\)).

---

## Mandatory Patch Packet

* **Callsign:** RH-BRIDGE-13  
* **Result classification:** CONDITIONAL  
* **Target gaps closed (by ID):**  
  - UE-INPUT interface pointwise/sup removal (Batch-13 target; not previously numbered in G-list)  
* **Target gaps still open (by ID):**  
  - UE-INPUT itself remains open (now as a boundary \(H^1\) control statement).  
* **Key conclusions (≤5 bullets):**
  1. A pointwise/sup derivative field bound is not structurally required to upper-bound \(\Phi^\star\); a boundary \(L^1/H^1\) control of \(\mathcal D_{a,h}\) suffices.
  2. The revised UE reduction lemma is RH-free and requires no analyticity inside the hinge disk.
  3. Under the nominal \(\delta=\eta a/(\log(m+3))^2\) policy, UE-INPUT\(^\mathrm{(H^1)}\) implies \(\Phi^\star=o(1)\) so long as the log-loss exponent satisfies \(C'<4\).
  4. This patch cleanly eliminates the “pointwise/sup” NO-GO interface leakage at the UE gate.
  5. The open mathematical burden is now a single boundary-norm estimate on \(\mathcal D_{a,h}\) along shifted hinge traces.

* **Paste-ready manuscript edits (TeX blocks):**

  **(i) Revised lemma/proposition statement (replace Lemma `lem:geo-c4-ue-reduction`)**
  ```tex
  \begin{lemma}[UE from a boundary $H^1/L^1$ control]\label{lem:geo-c4-ue-reduction}
  Fix $\kappa\in(0,1)$ and set $h=\kappa\delta$ with $0<h<\delta$.
  Let $\psi(\theta)=\Im(\mathcal D_{a,h}(v(\theta)))$ on $v(\theta)=i m+\delta e^{i\theta}$ and define
  \[
  \widehat\psi(2):=\int_0^{2\pi}\psi(\theta)e^{-2i\theta}\,d\theta.
  \]
  Then
  \[
  \|P_2\psi\|_{L^2([0,2\pi])}=\frac{1}{\sqrt{\pi}}|\widehat\psi(2)|
  \le \frac{1}{\sqrt{\pi}}\int_0^{2\pi}|\psi(\theta)|\,d\theta
  \le \frac{1}{\sqrt{\pi}}\int_0^{2\pi}\bigl|\mathcal D_{a,h}(v(\theta))\bigr|\,d\theta.
  \]
  In particular,
  \[
  \boxed{\ \Phi^\star(m,a,\delta,h)\ \le\ \frac{\delta^2}{h\sqrt{\pi}}\int_0^{2\pi}\bigl|\mathcal D_{a,h}(v(\theta))\bigr|\,d\theta\ }.
  \]
  \end{lemma}

  \begin{proof}
  Since $P_2\psi(\theta)=\alpha\cos(2\theta)+\beta\sin(2\theta)$, a direct computation gives
  \[
  \widehat\psi(2)=\int_0^{2\pi}(\alpha\cos(2\theta)+\beta\sin(2\theta))e^{-2i\theta}\,d\theta=\pi(\alpha-i\beta),
  \]
  hence $|\widehat\psi(2)|=\pi\sqrt{\alpha^2+\beta^2}$.
  Also $\|P_2\psi\|_{L^2}^2=\int_0^{2\pi}(\alpha\cos(2\theta)+\beta\sin(2\theta))^2\,d\theta=\pi(\alpha^2+\beta^2)$,
  so $\|P_2\psi\|_{L^2}=(1/\sqrt{\pi})|\widehat\psi(2)|$.
  Finally, $|\widehat\psi(2)|\le\int_0^{2\pi}|\psi(\theta)|\,d\theta\le\int_0^{2\pi}|\mathcal D_{a,h}(v(\theta))|\,d\theta$
  since $|\Im z|\le |z|$. This yields the bound for $\Phi^\star$.
  \end{proof}
  ```

  **(ii) Revised definitions/remarks (replace Box `UE-INPUT (v42, single active statement)`)**
  ```tex
  \begin{center}
  \fbox{%
  \begin{minipage}{0.95\textwidth}
  \textbf{UE-INPUT$^{(H^1)}$ (replacement UE gate).}\label{box:ue-input-v42}

  \smallskip
  Fix $\kappa\in(0,1)$ and let $E$ be the completed even entire object in the $v$--plane.
  For all sufficiently large $m$ and all $a\in(0,1)$, set
  \[
  \delta=\delta(m,a):=\eta\,\frac{a}{(\log(m+3))^2},\qquad h:=\kappa\delta,
  \]
  and allow smaller $\delta$ if needed to enforce $\mathrm{buf}$--admissibility (Definition~\ref{def:shift-admissible-hinge}).

  \smallskip
  Prove a uniform boundary-norm control: there exist absolute constants $C,C'>0$ such that
  \[
  \int_0^{2\pi}\bigl|\mathcal D_{a,h}(v(\theta))\bigr|\,d\theta
  \ \le\ C\cdot h\,\frac{(\log(m+3))^{C'}}{a^{2}}.
  \]

  \smallskip
  \emph{Payoff.}  By Lemma~\ref{lem:geo-c4-ue-reduction}, UE-INPUT$^{(H^1)}$ implies
  $\Phi^\star(m,a,\delta,h)\ll_\kappa (\delta/a)^2(\log m)^{C'}=\eta^2(\log m)^{C'-4}=o(1)$ provided $C'<4$.
  Combined with the forcing lower bound from Lemma~\ref{lem:geo-c4-force-stable}, this contradicts the existence of any off-axis quartet at height $m$.
  \end{minipage}}
  \end{center}
  ```

  **(iii) Revised theorem/inequality lines**
  *Update any “UE-INPUT implies \((\delta/a)^3\)” lines to \((\delta/a)^2\)* and the decay \((\log m)^{C'-6}\) to \((\log m)^{C'-4}\).

* **Dependencies on other branches:** None required for this interface patch. (ENVELOPE/LOCAL will still own the substantive estimate proving UE-INPUT\(^\mathrm{(H^1)}\).)

* **Referee risk notes (anticipated objections + how addressed):**
  1. **“You used analyticity inside the disk.”** No: the reduction uses only boundary integrals and Fourier identities.
  2. **“Your endpoint is ill-defined without a log branch.”** No: \(\Phi^\star\) is defined from \(\Im(\mathcal D_{a,h})\) and requires only \(E'/E\) values on admissible traces.
  3. **“Admissibility shrink is circular.”** No: it enforces nonvanishing *on the boundary traces only*; this is always achievable because zeros are discrete, independent of RH.
