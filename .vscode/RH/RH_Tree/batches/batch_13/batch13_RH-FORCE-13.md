# Batch 13 — RH-FORCE-13  
**Callsign:** RH-FORCE-13  
**Ground truth:** v42 (`manuscript_v42.pdf`) + `integration_notes_v42.md`  
**Mission:** (i) sharpen the *FORCE* side for the GEO–C4 endpoint under **pair isolation + buffering**, (ii) state/prove the **UE-INPUT obstruction** cleanly (UE-INPUT ⇒ no off-axis quartet), and (iii) recommend a manuscript-safe conditional reframing if UE-INPUT remains open.

---

## 1) Forcing upgrade lemma (true \(E\), pair isolation + buffering)

### 1.1 Setup (as in v42 Box 12.1 / Def. 12.19)

Work in the \(v\)-frame, where \(E(v)\) is even and entire.  
Fix \(m>0\), \(a\in(0,1)\), \(0<\delta\ll 1\), and \(h=\kappa\delta\) with fixed \(\kappa\in(0,1)\).  
Let the hinge circle be
\[
C_{m,\delta}:\quad v(\theta)= i m+\delta e^{i\theta},\qquad \theta\in[0,2\pi].
\]

Define the two-sided field and double-difference (v42 §12.2):
\[
\mathcal L_t(v):=\frac{E'}{E}(v+t)-\frac{E'}{E}(v-t),\qquad 
\mathcal D_{a,h}(v):=\mathcal L_{a+h}(v)-\mathcal L_{a-h}(v).
\]
Let \(\psi_{a,h}(\theta):=\Im\big(\mathcal D_{a,h}(v(\theta))\big)\).  
Let \(P_2\) denote orthogonal projection onto \(\mathrm{span}\{\cos(2\theta),\sin(2\theta)\}\subset L^2([0,2\pi])\).  
The GEO–C4 endpoint is
\[
\Phi^\star(m,a,\delta,h):=\frac{\delta^2}{h}\,\big\|P_2\psi_{a,h}\big\|_{L^2([0,2\pi])}.
\]

### 1.2 Pair isolation hypothesis (minimal, forcing-focused)

Assume:

1. **Off-axis quartet:** \(E(\pm a\pm i m)=0\) with \(a>0\).
2. **Shift buffering (v42 Def. 12.19):** \(C_{m,\delta}\) is **buf-admissible** for \((a,h)\), i.e.
   \[
   \min_{\theta\in[0,2\pi]}\min_{\pm,\pm}\operatorname{dist}\big(v(\theta)\pm (a\pm h),\,Z(E)\big)\ \ge\ \mathrm{buf}\cdot\delta
   \]
   for some fixed \(\mathrm{buf}\in(0,1)\).
3. **Pair isolation (local, scale-separated):** there exists a fixed \(R\ge 10\) such that the only zeros of \(E\) in
   \[
   \bigcup_{\pm}\,D(\pm a+i m,\ R\delta)
   \]
   are the two **top** zeros \(\pm a+i m\). (No other zeros within \(R\delta\) of the top pair.)

This is deliberately *local*: it is the minimum needed to treat every non-top contribution as analytic on a fixed annulus around \(C_{m,\delta}\) after the \(t=\pm(a\pm h)\) shifts.

### 1.3 Forcing upgrade (statement)

> **Lemma (FORCE upgrade: quantitative remainder control).**  
> Assume the setup above, and suppose \(E(\pm a\pm i m)=0\) with \(a>0\).  
> Fix \(\kappa\in(0,1)\) and \(h=\kappa\delta\). Assume buf-admissibility and pair isolation (as in §1.2).  
> Then for all sufficiently small \(\delta\) (depending on \(E,m,a,\kappa,\mathrm{buf},R\) only through a local remainder bound stated below),
> \[
> \Phi^\star(m,a,\delta,h)\ \ge\ 4\sqrt{\pi}\ -\ \mathrm{Err}_{\rm rem}(m,a,\delta,h).
> \]
> Moreover one may take the explicit error proxy
> \[
> \mathrm{Err}_{\rm rem}(m,a,\delta,h)\ :=\ \frac{\delta}{\kappa}\,\sqrt{2\pi}\,
> \sup_{\theta\in[0,2\pi]}\Big|\Im\big(\mathcal R_{a,h}(v(\theta))\big)\Big|,
> \]
> where \(\mathcal R_{a,h}\) is the “non-top remainder” defined in the proof. In particular, if
> \(\sup_\theta|\mathcal R_{a,h}(v(\theta))|\le M_{\rm rem}(m,a,\kappa,\mathrm{buf},R)\) uniformly for \(0<\delta\le\delta_\ast\),
> then
> \[
> \Phi^\star(m,a,\delta,h)\ \ge\ 4\sqrt{\pi}\ -\ \frac{\delta}{\kappa}\sqrt{2\pi}\,M_{\rm rem}.
> \]
> Hence after shrinking \(\delta\) (monotone admissibility shrink), one obtains a uniform absolute lower bound
> \(\Phi^\star(m,a,\delta,h)\ge 2\sqrt{\pi}\) (the v42 Lemma 12.22 bound), but now with an explicit remainder-to-error interface.

### 1.4 Proof (line-by-line, forcing-only)

**Step 1 (decomposition of \(\mathcal D_{a,h}\)).**  
Write \(F(v):=E'(v)/E(v)\), meromorphic with simple poles at simple zeros of \(E\).  
Define the “top-pair singular model” by extracting only the poles coming from \(\rho_{\pm}:=\pm a+i m\) in the *top half*:
\[
F_{\rm top}(v):=\frac{1}{v-\rho_+}+\frac{1}{v-\rho_-}.
\]
Let \(F_{\rm rem}:=F-F_{\rm top}\). Then define
\[
\mathcal D_{a,h}^{\rm top}(v):=\Big(F_{\rm top}(v+a+h)-F_{\rm top}(v-(a+h))\Big)\ -\ \Big(F_{\rm top}(v+a-h)-F_{\rm top}(v-(a-h))\Big),
\]
and similarly \(\mathcal D_{a,h}^{\rm rem}\) with \(F_{\rm rem}\) in place of \(F_{\rm top}\). Then
\[
\mathcal D_{a,h}=\mathcal D_{a,h}^{\rm top}+\mathcal D_{a,h}^{\rm rem}.
\]

**Step 2 (the top term forces the \(k=2\) carrier).**  
Exactly as in v42 Lemma 12.21 (toy forcing), the top term \(\mathcal D_{a,h}^{\rm top}\) produces the dipole kernel
\[
\mathcal D_{a,h}^{\rm top}(v)= -\frac{4h}{(v-i m)^2-h^2}\ +\ \text{(terms with poles at }\pm 2a+i m\pm h\text{)}.
\]
On the hinge circle \(v(\theta)=i m+\delta e^{i\theta}\) with \(h=\kappa\delta\), the interior dipole contribution has a pure \(\sin(2\theta)\) carrier in the \(k=2\) projection and yields the normalization constant
\[
\frac{\delta^2}{h}\,\big\|P_2\Im\big(\mathcal D_{a,h}^{\rm dipole}\circ v\big)\big\|_{L^2}=4\sqrt{\pi}.
\]
(Under the v42 normalization this constant is independent of \(\kappa\).)

**Step 3 (define the remainder \(\mathcal R_{a,h}\)).**  
Let \(\mathcal R_{a,h}\) denote *everything else* in \(\mathcal D_{a,h}\) beyond the dipole top contribution:
\[
\mathcal D_{a,h}(v(\theta)) \ =\ \mathcal D^{\rm dipole}_{a,h}(v(\theta))\ +\ \mathcal R_{a,h}(v(\theta)).
\]
Pair isolation + buf-admissibility ensures \(\mathcal R_{a,h}\circ v\) is continuous in \(\theta\) and remains bounded on \([0,2\pi]\) for fixed \((m,a,\kappa,\mathrm{buf},R)\) as \(\delta\downarrow 0\).

**Step 4 (project and bound the remainder contribution).**  
Let \(\psi_{\rm dip}=\Im(\mathcal D^{\rm dipole}_{a,h}\circ v)\) and \(\psi_{\rm rem}=\Im(\mathcal R_{a,h}\circ v)\). Then
\[
\|P_2(\psi_{\rm dip}+\psi_{\rm rem})\|_{2}\ \ge\ \|P_2\psi_{\rm dip}\|_2-\|P_2\psi_{\rm rem}\|_2.
\]
Since \(P_2\) is an orthogonal projection, \(\|P_2\psi_{\rm rem}\|_2\le \|\psi_{\rm rem}\|_2\le \sqrt{2\pi}\sup_\theta|\psi_{\rm rem}(\theta)|\). Multiplying by \(\delta^2/h=\delta/\kappa\) gives
\[
\Phi^\star(m,a,\delta,h)\ \ge\ 4\sqrt{\pi}\ -\ \frac{\delta}{\kappa}\sqrt{2\pi}\sup_\theta|\psi_{\rm rem}(\theta)|,
\]
which is the claimed bound with the stated error proxy.

**Step 5 (recover the uniform positive constant).**  
If \(\sup_\theta|\psi_{\rm rem}|\le M_{\rm rem}\), choose \(\delta\le \delta^\ast:=\min\{\delta_0,\,\kappa\cdot 2\sqrt{\pi}/(\sqrt{2\pi}M_{\rm rem})\}\). Then
\(\Phi^\star\ge 2\sqrt{\pi}\), recovering v42 Lemma 12.22 with an explicit remainder interface.

\(\square\)

---

## 2) UE-INPUT obstruction lemma (why UE-INPUT is RH-strength)

### 2.1 What UE-INPUT is (v42 Box 12.2.5, restated)

UE-INPUT postulates a **uniform derivative field bound** for the shifted two-sided field, at the nominal micro-coupling
\[
\delta=\eta\,\frac{a}{(\log(m+3))^2},\qquad h=\kappa\delta,
\]
(and allowing smaller \(\delta\) via monotone admissibility shrink), of the form
\[
\sup_{\theta\in[0,2\pi]}\sup_{t\in[a-h,a+h]}
\Big|\partial_t\,\partial_v^j\,\mathcal L_t\big(v(\theta)\big)\Big|
\ \le\ C\,\frac{(\log(m+3))^{C'}}{a^{2+j}}
\qquad (j=0,1,2),
\]
equivalently (mean value theorem in \(t\)),
\[
\sup_\theta \big|\partial_v^j\,\mathcal D_{a,h}(v(\theta))\big|
\ \le\ 2h\,C\,\frac{(\log(m+3))^{C'}}{a^{2+j}}
\qquad (j=0,1,2).
\]

### 2.2 Endpoint payoff (v42 Lemma 12.23)

Under the derivative field bound above, v42 Lemma 12.23 yields
\[
\Phi^\star(m,a,\delta,h)\ \ll_\kappa\ (\log(m+3))^{C'}\left(\frac{\delta}{a}\right)^3.
\]
Under the nominal policy \(\delta/a=\eta/(\log(m+3))^2\), this becomes
\[
\Phi^\star(m,a,\delta,h)\ \ll_\kappa\ \eta^3\,(\log(m+3))^{C'-6}.
\]
In particular, any form of UE-INPUT that implies \(\Phi^\star(m,a,\delta,h)=o(1)\) as \(m\to\infty\) (uniformly in \(a\in(0,1)\)) forces the endpoint to vanish asymptotically.

### 2.3 Obstruction lemma (UE-INPUT forbids off-axis quartets)

> **Lemma (UE-INPUT obstruction / RH-strength checkpoint).**  
> Fix \(\kappa\in(0,1)\), \(\eta\in(0,1)\). Assume UE-INPUT holds in the v42 sense, i.e. it implies
> \[
> \Phi^\star(m,a,\delta,h)\le \varepsilon(m,a)\quad\text{with}\quad \varepsilon(m,a)\to 0\ \ (m\to\infty)
> \]
> uniformly for \(a\in(0,1)\), with \(\delta=\eta a/(\log(m+3))^2\) and \(h=\kappa\delta\) (and allowing smaller \(\delta\)).  
> Then there exists \(M_0\) such that for all \(m\ge M_0\), \(E\) has **no** off-axis quartet \(\{\pm a\pm i m\}\) with \(a>0\).  
> Consequently, combined with any finite-height “front-end” verification up to \(M_0\), UE-INPUT implies RH.
>
> **Proof.**  
> Suppose (for contradiction) \(E(\pm a\pm i m)=0\) for some \(a>0\) and arbitrarily large \(m\).  
> After shrinking \(\delta\) to enforce buf-admissibility (monotone shrink is allowed), the forcing lemma (v42 Lemma 12.22, or the upgraded Lemma in §1) gives a uniform lower bound
> \[
> \Phi^\star(m,a,\delta,h)\ \ge\ c_0\quad\text{with }c_0=2\sqrt{\pi}>0.
> \]
> On the other hand, UE-INPUT gives \(\Phi^\star(m,a,\delta,h)\le \varepsilon(m,a)\to 0\) as \(m\to\infty\), contradiction for all sufficiently large \(m\).  
> Hence no such quartet can exist for \(m\ge M_0\). \(\square\)
>
> **Interpretation (“why UE-INPUT is hard”).**  
> The lemma shows UE-INPUT is not a “technical bound”; it is a *structural exclusion principle*: if proven unconditionally, it would exclude off-axis quartets and hence prove RH (after the finite-height front-end). Thus UE-INPUT is intrinsically RH-strength in the sense “UE-INPUT ⇒ RH”.

---

## 3) Manuscript-safe reframing if UE-INPUT remains conditional

If UE-INPUT is not closed, the manuscript can still be proof-grade as a **conditional criterion**—but must state that fact explicitly and avoid “proof claim” ambiguity.

### 3.1 Recommended v43/v44 storyline

1. **Unconditional core:** GEO–C4 endpoint definition, toy forcing computation, and forcing stability for the true \(E\) (v42 §§12.2.1–12.2.3).  
2. **Reduction:** the integration-by-parts lemma (v42 Lemma 12.23) reducing endpoint control to the derivative field bound.  
3. **Single conditional lever:** UE-INPUT (boxed), followed immediately by the obstruction theorem “UE-INPUT ⇒ RH” (the lemma above, promoted to a theorem once the finite-height front-end is included).

### 3.2 What classical analytic improvement would suffice (safe, non-handwavy)

A manuscript-safe sufficiency statement should **not** claim UE-INPUT is “plausible”; it should state exactly what estimate is missing:

*It suffices to prove the v42 Box 12.2.5 derivative field bound*:
\[
\sup_{\theta}\sup_{t\in[a-h,a+h]}
\Big|\partial_t\,\partial_v^j\,\mathcal L_t\big(v(\theta)\big)\Big|
\ \ll\ \frac{(\log(m+3))^{C'}}{a^{2+j}}
\quad (j=0,1,2),
\]
with a polylog exponent \(C'\) small enough that Lemma 12.23 yields \(\Phi^\star=o(1)\) under \(\delta=\eta a/\log^2(m+3)\). (The manuscript can present this simply as the boxed “UE-INPUT” obligation.)

Optionally (if you want one “translation layer” for readers): express \(\partial_t\partial_v^j\mathcal L_t\) via the Hadamard/explicit-formula representation of \(E'/E\) as a sum of Cauchy kernels over zeros plus an archimedean remainder, and note that UE-INPUT is a uniform bound on a *shifted second-difference* of those kernels on a shrinking circle.

---

## 4) S6 explicit-formula mapping (required)

**Frame mapping:** \(u=2s\), \(v=u-1\), so an off-axis zero \(\rho=\beta+i\gamma\) corresponds to \(v_\rho=(2\beta-1)+i(2\gamma)\). Here \(a=2\beta-1\), \(m=2\gamma\).

**Does the forcing constant correspond to an explicit-formula amplitude leak?**  
Not directly. \(\Phi^\star\) is a *local boundary harmonic* built from the shifted log-derivative field of the completed object \(E\) on a circle around \(im\). It detects a dipole-type local signature forced by an off-axis quartet (a geometric/analytic winding defect), rather than measuring an \(x^\beta\) term in the explicit formula. The connection is indirect: an off-axis zero with \(\beta\neq 1/2\) would create an \(x^\beta\) amplitude term in prime-counting explicit formulas, and the same zero manifests locally as the quartet \(\{\pm a\pm i m\}\) that forces the \(k=2\) carrier. But \(\Phi^\star\) itself is not a direct amplitude-leak observable; it is a *local obstruction detector* in the \(v\)-plane.

---

# Patch Packet

* **Callsign:** RH-FORCE-13
* **Result classification:** **PASS (deliverables met; UE-INPUT remains conditional)**
* **Target gaps closed (by ID):** none newly closed; this patch **strengthens FORCE** and **formalizes the UE obstruction**.
* **Target gaps still open (by ID):** UE-INPUT (v42 Box 12.2.5).
* **Key conclusions (≤5 bullets):**
  1. Under v42 normalization, toy forcing constant is **\(4\sqrt{\pi}\)** (Lemma 12.21).
  2. A quantitative FORCE upgrade holds: **\(\Phi^\star\ge 4\sqrt{\pi}-\mathrm{Err}_{\rm rem}\)** with an explicit remainder-to-error proxy.
  3. UE-INPUT is **RH-strength**: UE-INPUT ⇒ no off-axis quartets for large \(m\) ⇒ RH (with finite front-end).
  4. Therefore, if UE-INPUT remains open, the manuscript must be framed as a **conditional criterion**.
  5. The “missing analytic improvement” is exactly the boxed derivative field bound; do not claim more.
* **Paste-ready manuscript edits (TeX blocks):**

  **(i) Add a quantitative FORCE lemma (after v42 Lemma 12.22):**
  ```tex
  \begin{lemma}[FORCE upgrade: quantitative remainder interface]\label{lem:force-upgrade-quant}
  Fix $\kappa\in(0,1)$ and set $h=\kappa\delta$. Let $E$ be even entire in the $v$-plane and assume
  $E(\pm a\pm i m)=0$ for some $a>0$. Assume the hinge circle $C_{m,\delta}:v(\theta)=im+\delta e^{i\theta}$
  is buf--admissible at $(a,h)$ (Def.~\ref{def:shift-admissible-hinge-circle}), and assume pair isolation:
  the only zeros of $E$ in $\cup_{\pm}D(\pm a+im,R\delta)$ are $\pm a+im$ for some fixed $R\ge 10$.
  Then
  \[
    \Phi^\star(m,a,\delta,h)\ \ge\ 4\sqrt{\pi}\ -\ \Err_{\rm rem}(m,a,\delta,h),
  \]
  where one may take
  \[
    \Err_{\rm rem}(m,a,\delta,h):=\frac{\delta}{\kappa}\sqrt{2\pi}\,
    \sup_{\theta\in[0,2\pi]}\Big|\Im\big(\mathcal R_{a,h}(v(\theta))\big)\Big|,
  \]
  with $\mathcal R_{a,h}$ denoting the non-top remainder in the decomposition
  $\mathcal D_{a,h}=\mathcal D^{\rm dipole}_{a,h}+\mathcal R_{a,h}$ on $C_{m,\delta}$.
  In particular, if $\sup_\theta|\mathcal R_{a,h}(v(\theta))|\le M_{\rm rem}$ for $0<\delta\le\delta_\ast$,
  then $\Phi^\star\ge 4\sqrt{\pi}-\frac{\delta}{\kappa}\sqrt{2\pi}\,M_{\rm rem}$.
  \end{lemma}
  ```

  **(ii) Add an explicit “UE-INPUT obstruction” criterion statement (near Box 12.2.5 / Executive Status):**
  ```tex
  \begin{lemma}[UE-INPUT obstruction: UE-INPUT $\Rightarrow$ no off-axis quartets]\label{lem:ue-input-obstructs-quartets}
  Assume UE-INPUT (Box~\ref{box:ue-input}) holds in a form implying
  $\Phi^\star(m,a,\delta,h)\le \varepsilon(m,a)$ with $\varepsilon(m,a)\to 0$ as $m\to\infty$
  uniformly for $a\in(0,1)$ at the nominal coupling $\delta=\eta a/\log^2(m+3)$, $h=\kappa\delta$
  (allowing smaller $\delta$ by monotone admissibility shrink).
  Then there exists $M_0$ such that for all $m\ge M_0$ there is no quartet $\{\pm a\pm im\}\subset Z(E)$
  with $a>0$. Consequently, combined with a finite-height front-end up to $M_0$, UE-INPUT implies RH.
  \end{lemma}
  ```

  **(iii) Add a “status/claim hygiene” remark (optional but recommended):**
  ```tex
  \begin{remark}[Status clarity: UE-INPUT is RH-strength]\label{rem:ue-input-rh-strength}
  Lemma~\ref{lem:ue-input-obstructs-quartets} shows UE-INPUT is not a routine estimate: if proven
  unconditionally it would exclude off-axis quartets and thus prove RH (after the finite-height front-end).
  The manuscript therefore presents UE-INPUT as the single explicit remaining analytic obligation.
  \end{remark}
  ```

* **Dependencies on other branches:** none required for the statements above. (If RH-LOCAL later provides a quantitative bound on the remainder proxy \(M_{\rm rem}\), it can be inserted into Lemma \ref{lem:force-upgrade-quant}, but it is not needed for the obstruction logic.)
* **Referee risk notes (anticipated objections + how addressed):**
  1. **“Your forcing bound hides dependence in \(M_{\rm rem}\).”** Addressed by making the dependence explicit in \(\Err_{\rm rem}\) and isolating it as a bounded trace term under buffering.
  2. **“UE-INPUT looks like RH in disguise.”** Addressed by proving the explicit implication UE-INPUT ⇒ (no quartets) ⇒ RH, and recommending conditional framing if UE-INPUT remains open.
  3. **“Pair isolation is too strong / non-checkable.”** Lemma is optional strengthening; the core obstruction already follows from v42 Lemma 12.22 (which uses only admissibility shrink). Pair isolation is presented as an *upgrade interface*, not as a hidden assumption in the main chain.
