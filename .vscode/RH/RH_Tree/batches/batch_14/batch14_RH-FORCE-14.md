# Batch 14 — RH-FORCE-14  
**Callsign:** RH-FORCE-14  
**Ground truth:** v42 locked (GEO–C4 forcing) + v43 prebuild UE-interface refactor (via `UE‑INPUTᴴ¹(D)`).  
**Mission:** stress-test the **FORCE** chain against the new **boundary L¹** UE interface and add the minimal “stability under clutter” statements needed to keep the contradiction airtight.

---

## 1) Forcing vs L¹ sanity (hinge double-difference must be large under a quartet)

### 1.1 Setup (notation matches v42 / v43 prebuild)

Work in the centered \(v\)-frame with \(E(v)\) even and entire.  
Fix parameters \(m>0\), \(a\in(0,1)\), \(0<\delta\ll 1\), and \(\kappa\in(0,1)\). Set
\[
h:=\kappa\delta,\qquad v(\theta):= i m+\delta e^{i\theta},\qquad \theta\in[0,2\pi].
\]
Define
\[
\mathcal L_t(v):=\frac{E'}{E}(v+t)-\frac{E'}{E}(v-t),
\qquad 
\mathcal D_{a,h}(v):=\mathcal L_{a+h}(v)-\mathcal L_{a-h}(v).
\]
Assume **shift buffering / admissibility** for \((a,h)\): the four shift traces
\[
v(\theta)\pm (a\pm h),\qquad \theta\in[0,2\pi],
\]
are zero-free for \(E\) (equivalently \(E'/E\) is holomorphic on a neighborhood of each trace).

---

### 1.2 Lemma: quartet forces an \(L^1\) blow-up at scale \(h/\delta^2\)

> **Lemma (FORCE–\(L^1\) lower bound on the hinge circle).**  
> \label{lem:force-L1-lower}
> Assume:
> 1. (**Off-axis quartet**) \(E(\pm a\pm i m)=0\) with \(a>0\).  
> 2. (**Buf-admissibility**) the four shift traces \(v(\theta)\pm (a\pm h)\) are zero-free for \(E\).  
> 3. (**Pair isolation at the top**) there exists \(R\ge 10\) such that the only zeros of \(E\) in
>    \[
>    D(a+i m,R\delta)\ \cup\ D(-a+i m,R\delta)
>    \]
>    are the two “top” zeros \(\pm a+i m\).  
>
> Then there is a decomposition on a neighborhood \(\Omega\) of the shift traces
> \[
> \frac{E'}{E}(z)=\frac{1}{z-(a+i m)}+\frac{1}{z-(-a+i m)}+H(z),
> \]
> where \(H\) is holomorphic on \(\Omega\). Writing \(M_1:=\sup_{z\in\Omega}|H'(z)|\), one has:
> \[
> \int_0^{2\pi}\Big|\mathcal D_{a,h}(v(\theta))\Big|\,d\theta
> \ \ge\
> \frac{8\pi}{1+\kappa^2}\cdot \frac{h}{\delta^2}
> \ -\ 8\pi\,h\,M_1.
> \]
> In particular, if \(M_1\ll 1/a^2\) on \(\Omega\), then
> \[
> \int_0^{2\pi}\Big|\mathcal D_{a,h}(v(\theta))\Big|\,d\theta
> \ \gtrsim_\kappa\ \frac{h}{\delta^2}\ -\ O_\kappa\!\left(\frac{h}{a^2}\right).
> \]

**Proof (line-by-line).**  
Let \(F(z):=E'(z)/E(z)\). Under pair isolation and buf-admissibility, \(F\) is meromorphic on \(\Omega\) with only two poles in \(\Omega\), at \(\rho_\pm:=\pm a+i m\), and hence admits the stated partial fraction decomposition with holomorphic \(H\).

Define the polar part \(F_{\rm top}(z):=(z-\rho_+)^{-1}+(z-\rho_-)^{-1}\). By direct substitution into the definition of \(\mathcal D_{a,h}\) one checks:
\[
\mathcal D_{a,h}^{\rm top}(v)
:=F_{\rm top}(v+a+h)-F_{\rm top}(v-a-h)-F_{\rm top}(v+a-h)+F_{\rm top}(v-a+h)
\]
equals
\[
\mathcal D_{a,h}^{\rm top}(v)
=
-\frac{4h}{(v-i m)^2-h^2}\ +\ \mathcal E_{\rm far}(v),
\]
where the “far” term \(\mathcal E_{\rm far}\) is a sum of differences of Cauchy kernels evaluated at points separated by \(\asymp a\) from \(v\) (e.g. denominators like \(v-(\pm 2a+i m)\pm h\)), hence satisfies the uniform bound on the hinge circle
\[
\sup_{\theta\in[0,2\pi]}|\mathcal E_{\rm far}(v(\theta))|\ \ll\ \frac{h}{a^2}
\qquad (\text{for }\delta,h\le a/4).
\]

Similarly, the remainder contribution
\[
\mathcal D_{a,h}^{\rm rem}(v)
:=H(v+a+h)-H(v-a-h)-H(v+a-h)+H(v-a+h)
\]
obeys, by the mean value theorem applied to each \(\pm h\) increment,
\[
|\mathcal D_{a,h}^{\rm rem}(v)|\ \le\ 4h\,\sup_{z\in\Omega}|H'(z)|\ =\ 4h\,M_1,
\]
hence
\[
\int_0^{2\pi}|\mathcal D_{a,h}^{\rm rem}(v(\theta))|\,d\theta\ \le\ 8\pi h M_1.
\]

Now evaluate the dipole term on the hinge circle. Since \(v(\theta)-i m=\delta e^{i\theta}\) and \(h=\kappa\delta\),
\[
\left|\frac{4h}{(v(\theta)-i m)^2-h^2}\right|
=
\frac{4h}{|\delta^2 e^{2i\theta}-h^2|}
\ \ge\
\frac{4h}{\delta^2+h^2}
=
\frac{4}{1+\kappa^2}\cdot\frac{h}{\delta^2},
\]
uniformly in \(\theta\). Integrating gives
\[
\int_0^{2\pi}\left|\frac{4h}{(v(\theta)-i m)^2-h^2}\right|\,d\theta
\ \ge\
\frac{8\pi}{1+\kappa^2}\cdot\frac{h}{\delta^2}.
\]

Finally, write
\(\mathcal D_{a,h}=\mathcal D_{a,h}^{\rm top}+\mathcal D_{a,h}^{\rm rem}\) and use the reverse triangle inequality:
\[
\int_0^{2\pi}|\mathcal D_{a,h}|
\ \ge\
\int_0^{2\pi}\left|\frac{4h}{(v-i m)^2-h^2}\right|
\ -\ \int_0^{2\pi}\Big(|\mathcal E_{\rm far}|+|\mathcal D_{a,h}^{\rm rem}|\Big).
\]
Absorb \(\int|\mathcal E_{\rm far}|\) into the \(O(h/a^2)\) term (or into \(M_1\) by enlarging \(\Omega\)). This yields the stated inequality. \(\square\)

---

### 1.3 Interaction with the new UE target \(UE\text{-}INPUT^{H^1}(D)\)

The v43 active UE box targets an upper bound of the form
\[
\int_0^{2\pi}|\mathcal D_{a,h}(v(\theta))|\,d\theta
\ \le\ 
C\cdot h\cdot (\log(m+3))^{C'}/a^2.
\]
Lemma~\ref{lem:force-L1-lower} shows what makes this hard:

*Under an off-axis quartet, the same integral is forced to be of size \(\asymp_\kappa h/\delta^2\), i.e.*
\[
\int_0^{2\pi}|\mathcal D_{a,h}(v(\theta))|\,d\theta
\ \gtrsim_\kappa\ \frac{h}{\delta^2}
\quad\text{(dominant as soon as }\delta\ll a).
\]

At the nominal coupling \(\delta=\eta a/(\log(m+3))^2\), this forced lower bound scales like
\[
\frac{h}{\delta^2}=\frac{\kappa\delta}{\delta^2}=\frac{\kappa}{\delta}
\asymp \frac{\kappa}{\eta}\cdot\frac{(\log m)^2}{a},
\]
whereas the UE target scales like
\[
\frac{h}{a^2}\cdot(\log m)^{C'}
\asymp \kappa\eta\cdot \frac{(\log m)^{C'-2}}{a}.
\]
So the UE target must beat the forced blow-up by essentially a \((\log m)^4\) factor (up to constants), which is precisely why \(UE\text{-}INPUT^{H^1}(D)\) is a “closure-level” estimate.

---

## 2) Clutter robustness (additional nearby quartets cannot erase forcing beyond the remainder norm)

The forcing endpoint is a **\(k=2\) harmonic channel**, not a pointwise quantity:
\[
\Phi^\star(m,a,\delta,h)=\frac{\delta^2}{h}\,\big\|P_2\Im(\mathcal D_{a,h}(v(\theta)))\big\|_{L^2_\theta}.
\]
Because \(P_2\) is linear, extra zeros can in principle introduce cancellation in the \(k=2\) coefficient unless we control their contribution to the \(k=2\) projection. The correct “robustness” statement is therefore:

> **Lemma (FORCE stability under analytic clutter; resonance is the only cancellation threat).**  
> \label{lem:force-stability-clutter}
> Assume the hypotheses of Lemma~\ref{lem:force-L1-lower}.  
> Decompose on the hinge circle
> \[
> \Im(\mathcal D_{a,h}\circ v)=\psi_{\rm dip}+\psi_{\rm rem},
> \]
> where \(\psi_{\rm dip}\) is the explicit dipole contribution
> \(
> \Im\!\left(-4h/((v-i m)^2-h^2)\right)\circ v
> \)
> and \(\psi_{\rm rem}\) collects *all other* contributions (including: other zeros of \(E\) away from the top pair, the bottom pair \(\pm a-i m\), the archimedean factor, and any additional quartets at the same height but separated from \(\pm a+i m\) by \(\ge R\delta\)).  
> Then
> \[
> \Phi^\star(m,a,\delta,h)
> \ \ge\
> 4\sqrt{\pi}\ -\ \frac{\delta^2}{h}\,\|\psi_{\rm rem}\|_{L^2_\theta}.
> \]
> In particular, using \(\|\psi_{\rm rem}\|_{L^2}\le \|\psi_{\rm rem}\|_{L^1}/\sqrt{2\pi}\),
> \[
> \Phi^\star(m,a,\delta,h)
> \ \ge\
> 4\sqrt{\pi}\ -\ \frac{\delta^2}{h\sqrt{2\pi}}\int_0^{2\pi}|\psi_{\rm rem}(\theta)|\,d\theta.
> \]
> Therefore **additional zeros cannot reduce the forcing constant** unless they create a remainder whose \(L^2\) (or \(L^1\)) norm is comparable to the dipole carrier. Equivalently: the only mechanism that can erase forcing is a near-resonant pile-up that breaks the pair-isolation/buffering regime (this is precisely what the local “resonance” accounting is designed to detect/control).

**Proof.**  
Because \(P_2\) is an orthogonal projection,
\[
\|P_2(\psi_{\rm dip}+\psi_{\rm rem})\|_2\ \ge\ \|P_2\psi_{\rm dip}\|_2-\|P_2\psi_{\rm rem}\|_2
\ \ge\ \|P_2\psi_{\rm dip}\|_2-\|\psi_{\rm rem}\|_2.
\]
Multiply by \(\delta^2/h\). Under the v42 normalization, \(\frac{\delta^2}{h}\|P_2\psi_{\rm dip}\|_2=4\sqrt{\pi}\). This gives the first displayed inequality. The second follows from \(\|f\|_2\le \|f\|_1/\sqrt{2\pi}\) on \([0,2\pi]\). \(\square\)

**Interpretation (what “clutter robustness” really means).**  
Extra quartets either:
- lie outside the local \(R\delta\) neighborhood of the top pair, hence enter \(\psi_{\rm rem}\) as an analytic/bounded perturbation (cannot erase forcing), or
- lie inside the neighborhood (near-resonant), in which case pair isolation fails and **one must account for them explicitly** (the program’s “resonance/local-count” branch).

So forcing is not weakened by clutter *within the declared hypothesis set*; if the hypotheses fail, the manuscript must say so explicitly.

---

## 3) Patch note paragraph (why UE-interface refactor does not change forcing)

> **Patch note (insert near the UE-interface replacement in v43).**  
> The GEO–C4 forcing constant \(c_0(\kappa)\) is produced by the **local dipole carrier** in the double-shift difference field \(\mathcal D_{a,h}\) on the hinge circle; it is a consequence of the local partial-fraction expansion of \(E'/E\) at a top off-axis pair \(\pm a+i m\), together with harmonic extraction \(P_2\).  
> The UE interface (whether pointwise, derivative-based as in v42, or boundary-\(L^1/H^1\) as in v43) is used only to upper-bound the same endpoint \(\Phi^\star\). Therefore replacing UE-INPUT by \(UE\text{-}INPUT^{H^1}(D)\) **does not modify the forcing statement or its constant**; it only changes the form of the single open analytic estimate needed to contradict forcing.

---

## MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* Callsign: RH-FORCE-14
* Result classification: **PASS**
* Target gaps closed (by ID): *(no new global gap ID assigned; this tightens GEO–C4 “FORCE ↔ UE interface” stability)*
* Target gaps still open (by ID): **UE‑INPUTᴴ¹(D)** remains the single active OPEN box (v43 plan).
* Key conclusions (≤5 bullets):
  1. Under an off-axis quartet, \(\int|\mathcal D_{a,h}(v(\theta))|\,d\theta\) is forced to scale like \(h/\delta^2\sim \kappa/\delta\), hence \(\asymp (\log m)^2/a\) at the nominal policy.
  2. Any UE bound of size \(O(h/a^2)\) (even with polylogs) must beat this forced blow-up by essentially a \((\log m)^4\) factor; this isolates why the UE input is closure-hard.
  3. Forcing robustness under “clutter” is exactly the statement that the remainder’s \(k=2\) projection norm is small; otherwise only near-resonant pile-ups can threaten cancellation (outside forcing scope).
  4. The UE-interface refactor does not affect forcing constants: forcing is local dipole geometry; UE is only an upper bound interface.
* Paste-ready manuscript edits (TeX blocks):
  (i) revised lemma/proposition statements  
  ```tex
  \begin{lemma}[FORCE--\(L^1\) lower bound on the hinge circle]
  \label{lem:force-L1-lower}
  Fix \(\kappa\in(0,1)\) and set \(h:=\kappa\delta\).
  Let \(v(\theta)=im+\delta e^{i\theta}\) be the hinge circle.
  Assume \(E(\pm a\pm im)=0\) with \(a>0\), and that the four shift traces
  \(v(\theta)\pm(a\pm h)\) are zero-free for \(E\).
  Assume further that in \(D(a+im,R\delta)\cup D(-a+im,R\delta)\) the only zeros of \(E\)
  are \(\pm a+im\) (pair isolation at the top).
  Then on a neighborhood \(\Omega\) of the shift traces one has
  \(\frac{E'}{E}(z)=\frac1{z-(a+im)}+\frac1{z-(-a+im)}+H(z)\) with \(H\) holomorphic, and
  with \(M_1:=\sup_{z\in\Omega}|H'(z)|\),
  \[
  \int_0^{2\pi}\Big|\mathcal D_{a,h}(v(\theta))\Big|\,d\theta
  \ \ge\
  \frac{8\pi}{1+\kappa^2}\cdot\frac{h}{\delta^2}\ -\ 8\pi h M_1.
  \]
  \end{lemma}
  ```
  ```tex
  \begin{lemma}[FORCE stability under analytic clutter]
  \label{lem:force-stability-clutter}
  Under the hypotheses of Lemma~\ref{lem:force-L1-lower}, write on the hinge circle
  \(\Im(\mathcal D_{a,h}\circ v)=\psi_{\rm dip}+\psi_{\rm rem}\), where \(\psi_{\rm dip}\)
  is the dipole contribution from the top pair \(\pm a+im\).
  Then
  \[
  \Phi^\star(m,a,\delta,h)\ \ge\ 4\sqrt{\pi}\ -\ \frac{\delta^2}{h}\,\|\psi_{\rm rem}\|_{L^2_\theta}.
  \]
  In particular \(\Phi^\star\ge 4\sqrt{\pi}-\frac{\delta^2}{h\sqrt{2\pi}}\int|\psi_{\rm rem}|\).
  \end{lemma}
  ```
  (ii) revised definitions/remarks  
  ```tex
  \begin{remark}[Why the \(L^1/H^1\) UE interface does not affect forcing]
  The forcing constant in the GEO--C4 endpoint comes from the local dipole carrier in
  \(\mathcal D_{a,h}\) induced by the top pair \(\pm a+im\).  Any UE interface is used only
  to upper-bound the same endpoint.  Therefore replacing the v42 pointwise UE box by
  \(UE\text{-}INPUT^{H^1}(D)\) does not change the forcing lemma or its constant; it only
  changes the single open analytic estimate required for the contradiction.
  \end{remark}
  ```
  (iii) revised theorem/inequality lines  
  *(none; this batch adds supporting lemmas + one explanatory remark only)*
* Dependencies on other branches:
  - If pair isolation is weakened to an \(N_{\rm eff}\) bound, RH-LOCAL must provide the exact local counting statement needed to bound \(\|\psi_{\rm rem}\|\).
* Referee risk notes (anticipated objections + how addressed):
  1. **“Your \(L^1\) lower bound depends on pair isolation.”** Yes—stated explicitly; without isolation, near-resonant cancellation must be handled in the resonance/local-count branch.
  2. **“You ignored the bottom pair \(\pm a-im\).”** They are far from the hinge circle at height \(+m\) and enter \(H\) with derivative bounds \(O(1/m^2)\); this is absorbed into \(M_1\).
  3. **“Can far poles in \(F_{\rm top}\) spoil the estimate?”** They contribute \(O(h/a^2)\) uniformly on the hinge circle when \(\delta,h\le a/4\); this is absorbed into the remainder term.
