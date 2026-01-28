# Batch 10 — RH-ENVELOPE  
**Artifact:** `batch10_RH-ENVELOPE.md`  
**Ground truth:** v39 locked build  
**Scope:** ML‑2 (Defect UE with effective \(p>1\), \(\delta\)-uniform) + resonance-object audit for consistency with Lemma `lem:defect-resonance-nogo`.

## Executive decision (decision‑grade)

**Route selected:** **(E‑1) Direct phase‑class UE** for the existing defect endpoint \(\Phi^{\rm def}_B(a)\) (Definition 12.2).【893:0†manuscript_v39.pdf†L3-L22】

**ML‑2 verdict (as stated in Box `box:missing-lever-v39`: “effective \(p>1\)”): _FAIL_.**  
Reason: with \(\Phi^{\rm def}_B(a)\) defined as a side phase increment (an integral of \(\mathcal L_a\) over a side of length \(\asymp\delta\)), the strongest \(\delta\)-scaling that follows from any \(\delta\)-uniform control on \(\mathcal L_a\) is **\(\Phi^{\rm def}=O(\delta)\)**, i.e. **\(p\le 1\)**. There is no proof‑grade mechanism in v39’s current toolchain that generates an extra \(\delta^{\varepsilon}\) beyond the side-length factor without changing the endpoint functional. This is already reflected in the manuscript’s own “OPEN target” bound (Remark 12.6), which is \(O(\delta\log m)+O(\delta\,\cdot\text{resonance})\), i.e. \(p=1\), not \(p>1\).【893:1†manuscript_v39.pdf†L43-L52】【893:0†manuscript_v39.pdf†L79-L83】

**Resonance audit (critical):** the current resonance sum \(\mathcal R_a(m)\) (Definition 12.5) is **\(\delta\)-blind** and therefore cannot serve as the “local obstruction accounting” term in a \(\delta\)-uniform UE statement that is consistent with the \(\delta\)-inert NO‑GO lemma `lem:defect-resonance-nogo`. In the NO‑GO model, \(\Phi^{\rm def}\) stays \(\gg 1\) as \(\delta\to 0\), but \(\delta a\mathcal R_a(m)\) stays \(O(\delta)\), so any UE bound of the schematic form in Remark 12.6 would contradict the NO‑GO example unless the resonance quantity is strengthened to become \(\delta\)-aware.【893:1†manuscript_v39.pdf†L53-L76】

**Minimal repair recommendation for v40 planning (without endpoint drift):**  
1) Treat **“\(p>1\)” as a mis-specified gate** for the current endpoint class; the realistic ML‑2 target is **\(p=1\)** with **explicit \(\delta\)-aware resonance term**.  
2) Upgrade \(\mathcal R_a(m)\) to a \(\delta\)-aware resonance quantity \(\mathcal R_{a,\delta}(m)\) so that the NO‑GO model is not contradicted and so that ML‑3 can plausibly bound/exclude resonance at the *nominal* \(\delta_0\).

---

## 1) Quantifier / domain block (as used below)

Throughout, assume:

- \(m\ge 10\), \(a\in(0,1]\), \(\kappa\in(0,1/10)\).
- \(B=B(0,m,\delta)\) is a \(\kappa\)-admissible aligned box (v39 Definition 12.26 referenced in Def. 12.2).【893:0†manuscript_v39.pdf†L3-L5】
- \(0<\delta\le \delta_0(m,a):=\eta a/(\log m)^2\) (nominal policy; v39 Box `box:missing-lever-v39`).【892:2†manuscript_v39.pdf†L15-L18】
- \(\partial B_{\kappa/2}\) is the buffered contour; \(\mathrm{Sides}(\partial B_{\kappa/2})\) are its four oriented sides.  
- \(E\) is the even entire width‑2 completion (Section 1; used in Definition 12.1).【892:14†manuscript_v39.pdf†L34-L36】

Defect primitives (Definitions 12.1–12.2):  
\(\mathcal Q_a(v)=E(v+a)/E(v-a)\), \(\mathcal L_a(v)=(\log \mathcal Q_a)'=E'/E(v+a)-E'/E(v-a)\), and
\[
\Phi^{\rm def}_B(a):=\max_{I\in \mathrm{Sides}(\partial B_{\kappa/2})}\Bigl|\Im\int_I \mathcal L_a(v)\,dv\Bigr|.
\]【893:0†manuscript_v39.pdf†L3-L22】

---

## 2) UE exponent ceiling for the *current* defect endpoint (NO‑GO for \(p>1\))

### Lemma (side-length ceiling: \(p\le 1\) for \(\Phi^{\rm def}\) under \(\delta\)-uniform pointwise control)

Let \(I\subset \partial B_{\kappa/2}\) be any side. If \(\mathcal L_a\) is holomorphic on a neighborhood of \(I\), then
\[
\Bigl|\Im\int_I \mathcal L_a(v)\,dv\Bigr|\le \int_I |\mathcal L_a(v)|\,|dv|\le |I|\cdot \sup_{v\in I}|\mathcal L_a(v)|.
\]
Since \(|I|\asymp \delta\) for each side of a \(\delta\)-scale rectangle, there is an absolute shape constant \(C_{\rm geom}\) such that
\[
\Phi_B^{\rm def}(a)\le C_{\rm geom}\,\delta\cdot \sup_{v\in \partial B_{\kappa/2}}|\mathcal L_a(v)|.
\]

**Consequence:** any proof strategy that bounds \(\Phi_B^{\rm def}(a)\) by first proving a \(\delta\)-uniform bound on \(\sup_{\partial B_{\kappa/2}}|\mathcal L_a|\) can produce **at most \(p=1\)**. Achieving \(p>1\) would require a genuinely new ingredient showing that the *mean imaginary part* of \(\mathcal L_a\) on each side is \(\delta\)-small beyond the trivial length factor (e.g. a structural cancellation moment on each side), which is not present in v39.

This ceiling is consistent with Lemma 12.3’s explicit decomposition: it already yields \(\Phi^{\rm def}_B(a)\le C r\,\delta/a + \delta\cdot\|H(\cdot+a)-H(\cdot-a)\|_{L^\infty(\partial B_{\kappa/2})}\), again with a **single** factor of \(\delta\).【893:0†manuscript_v39.pdf†L79-L83】

### ML‑2 implication

Because ML‑2 is currently phrased as “Defect UE with effective \(p>1\)” (Box `box:missing-lever-v39`)【892:2†manuscript_v39.pdf†L39-L42】, and because the installed endpoint is a side-length integral (Definition 12.2)【893:0†manuscript_v39.pdf†L3-L22】, **ML‑2 is unachievable as stated without changing the endpoint class** (Route E‑2) or introducing an additional per-side cancellation lemma that yields extra \(\delta\). Neither exists in v39. Therefore ML‑2(p>1) is **FAIL** in the current architecture.

---

## 3) Resonance object audit (critical for internal consistency)

### 3.1 Why the current \(\mathcal R_a(m)\) cannot be the correct UE “enemy”

v39 defines the horizontal resonance sum (Definition 12.5):
\[
\mathcal R_a(m):=\sum_{\rho:E(\rho)=0,\ |\Im(\rho)-m|\le 1}\frac{1}{|\Re(\rho)-a|+a},
\qquad \mathcal R_a(m)\le \frac{1}{a}N_{\rm loc}(m).
\]【893:1†manuscript_v39.pdf†L87-L97】

But the NO‑GO lemma `lem:defect-resonance-nogo` constructs an even polynomial \(E_\varepsilon\) with two quartets at real parts \(a\) and \(a-\varepsilon\), and shows that for \(\delta\asymp \varepsilon\),
\(\Phi_B^{\rm def}(a)\ge c_0>0\) independent of \(\delta\) and \(\varepsilon\).【893:1†manuscript_v39.pdf†L53-L76】

In that model, \(\mathcal R_a(m)\asymp 1/a\) remains **bounded** as \(\varepsilon\to 0\), so the target bound in Remark 12.6,
\(\Phi^{\rm def}_B(a)\lesssim \delta\log m+\delta a \mathcal R_a(m)\), would force \(\Phi^{\rm def}_B(a)=o(1)\) as \(\delta\to 0\), contradicting the NO‑GO lemma. Therefore:

> Any proof‑grade defect UE statement must use a resonance quantity that becomes large when “\(\varepsilon\sim\delta\)” resonance occurs.

### 3.2 δ‑aware resonance quantity (proposed replacement)

**Definition (δ‑aware horizontal resonance sum).** For \(a\in(0,1]\), \(m\ge 10\), and \(0<\delta\le a/4\), define
\[
\boxed{\ \mathcal R_{a,\delta}(m)\ :=\ \sum_{\rho:E(\rho)=0,\ |\Im(\rho)-m|\le 1}\frac{1}{|\Re(\rho)-a|+\delta}\ }.
\]

Basic bounds:
- \(\mathcal R_{a,\delta}(m)\le \delta^{-1}N_{\rm loc}(m)\).
- If there are **no** local zeros with \(|\Re(\rho)-a|\le \delta\) in the window, then \(\mathcal R_{a,\delta}(m)\ll \mathcal R_a(m)\) (up to constants).

**Toy model consistency check:** in the NO‑GO polynomial \(E_\varepsilon\) with a quartet at \(a-\varepsilon\) and \(\delta\asymp \varepsilon\), there is a zero with \(|\Re(\rho)-a|=\varepsilon\asymp \delta\), hence \(\mathcal R_{a,\delta}(m)\gg 1/\delta\). Therefore \(\delta\,\mathcal R_{a,\delta}(m)\gg 1\), so a UE bound with a term \(C\,\delta\,\mathcal R_{a,\delta}(m)\) is **not contradicted** by Lemma `lem:defect-resonance-nogo` (it correctly predicts \(\delta\)-inertness via blow‑up of \(\mathcal R_{a,\delta}\)).

---

## 4) What a *consistent* defect UE statement can look like (but note: \(p=1\))

The manuscript’s OPEN target (Remark 12.6) has the schematic form
\(\Phi^{\rm def}\lesssim \delta\log m+\delta a\mathcal R_a(m)\).【893:1†manuscript_v39.pdf†L98-L105】  
Given the resonance audit above, a consistent target should instead be **δ‑aware**.

### Proposed replacement for the OPEN target (truthful, consistent with NO‑GO)

> **Conjectural Lemma (Defect UE target, δ‑aware; replaces Remark 12.6).**  
> There exist absolute constants \(C_0,C_1>0\) (independent of \(m,a,\delta\)) such that for every \(m\ge 10\), \(a\in(0,1]\), and every \(\kappa\)-admissible box \(B=B(0,m,\delta)\) with \(0<\delta\le \delta_0(m,a)\) and \(\delta\le a/4\),
> \[
> \boxed{\ \Phi^{\rm def}_B(a)\ \le\ C_0\,\delta\log m\ +\ C_1\,\delta\,\mathcal R_{a,\delta}(m)\ }.
> \]
> (Any further “residual ledger” constants are absorbed into \(C_0\).)

**Exponent ledger:** this has **\(p=1\)** and a “local term” of the form \(\delta\,\mathcal R_{a,\delta}(m)\). The only way this becomes \(\delta\)-inert is when \(\mathcal R_{a,\delta}(m)\asymp 1/\delta\), i.e. when a near‑resonant quartet exists at \(|\Re(\rho)-a|\lesssim \delta\), exactly matching the NO‑GO mechanism.

**Status relative to ML‑2:** this does **not** satisfy “\(p>1\)” and therefore does not close ML‑2 as currently written. It is, however, the structurally consistent target for a defect UE statement in the current endpoint class.

---

## 5) S6 harness cross‑check (explicit‑formula amplitude leak)

**Frame mapping:** \(s=\beta+i\gamma\), \(u=2s\), \(v=u-1\). An off‑critical‑line zero \(\rho=\beta+i\gamma\) corresponds to
\[
v_\rho=(2\beta-1)+i(2\gamma)=a+i m,\qquad a=2\beta-1>0,\quad m=2\gamma.
\]
This is exactly the \(a,m\) used by the defect primitives in v39 (Definition 12.1).【892:14†manuscript_v39.pdf†L34-L36】

**Amplitude leak interpretation:** In the explicit formula for \(\psi(x)\), a zero with \(\beta>1/2\) contributes a term of size \(x^\beta=x^{1/2+a/2}\) (an “\(x^\beta\) leak”). The defect quotient \(\mathcal Q_a(v)=E(v+a)/E(v-a)\) is designed to compare the completed object at symmetric horizontal displacements \(\pm a\); therefore, a mechanism that forces \(\Phi_B^{\rm def}(a)\) to be \(\delta\)-small for all \(a>0\) (after transfer + forcing) would, at least at the heuristic level, be consistent with excluding such \(x^{1/2+a/2}\) contributions.

**However (referee-grade caution):** the present defect UE discussion is a *boundary phase* control statement, not a direct explicit‑formula amplitude estimate. In v39, the S6 mapping should be treated as a **consistency harness** (“does the parameter \(a\) match the explicit‑formula exponent shift?”), not as a proved implication from \(\Phi^{\rm def}\) bounds to explicit‑formula amplitude control.

---

## MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* Callsign: RH-ENVELOPE
* Result classification: **FAIL** (ML‑2 as stated: “effective \(p>1\)” cannot be met in the current endpoint class)
* Target gaps closed (by ID):
  - **ML‑2(p>1) → NO‑GO (architecture-level):** for \(\Phi_B^{\rm def}\) as defined (Definition 12.2), the endpoint is a side-length integral and yields at most \(p=1\) from \(\delta\)-uniform control; v39 has no additional per-side cancellation ingredient that would force \(p>1\).【893:0†manuscript_v39.pdf†L3-L22】
  - **Resonance-object mismatch identified:** current \(\mathcal R_a(m)\) is \(\delta\)-blind and cannot be the correct accounting object for the δ‑inert NO‑GO configuration (Lemma `lem:defect-resonance-nogo`).【893:1†manuscript_v39.pdf†L53-L76】
* Target gaps still open (by ID):
  - **ML‑1 Transfer/domination** \(D_B(W)\le C_{\rm tr}\,\Phi^{\rm def}_{\widehat B}(a)\) (untouched).
  - **ML‑2 (truthful version):** proving a δ‑uniform bound at \(p=1\) (not \(>1\)) remains OPEN.
  - **ML‑3 Resonance control:** bounding/excluding configurations with \(\mathcal R_{a,\delta}(m)\asymp 1/\delta\) remains OPEN.
* Key conclusions (≤5 bullets):
  1. With \(\Phi^{\rm def}\) defined as a side phase increment, the best attainable \(\delta\)-exponent from \(\delta\)-uniform bounds is \(p=1\); \(p>1\) would require new per-side cancellation technology not present in v39.
  2. The current boxed ML‑2 requirement “effective \(p>1\)” is inconsistent with the manuscript’s own target inequality (Remark 12.6), which is \(O(\delta)\).
  3. The resonance sum \(\mathcal R_a(m)\) is \(\delta\)-blind and cannot reconcile a UE claim with the δ‑inert NO‑GO lemma; a δ‑aware resonance object is mandatory.
  4. Replacing \(\mathcal R_a(m)\) by \(\mathcal R_{a,\delta}(m)\) restores toy‑model consistency: δ‑inertness manifests as \(\mathcal R_{a,\delta}(m)\gg 1/\delta\).
  5. A proof-grade defect UE route should target \(p=1\) + δ‑aware resonance + ML‑3 exclusion/bound, rather than \(p>1\) in the present endpoint class.
* Paste‑ready manuscript edits (TeX blocks):

  (i) revised lemma/proposition statements

  ```tex
  % New lemma (NO-GO for p>1 in the current defect endpoint class)
  \begin{lemma}[Side-length ceiling for the defect phase endpoint]\label{lem:defect-p-ceiling}
  Fix $a\in(0,1]$ and let $B=B(0,m,\delta)$ be a $\kappa$-admissible aligned box with buffered contour $\partial B_{\kappa/2}$.
  Assume $\mathcal L_a$ is holomorphic on an open neighborhood of $\partial B_{\kappa/2}$.
  Then
  \[
    \Phi_B^{\rm def}(a)\ \le\ C_{\rm geom}\,\delta\cdot \sup_{v\in\partial B_{\kappa/2}}|\mathcal L_a(v)|,
  \]
  where $C_{\rm geom}>0$ is an absolute rectangle-shape constant.
  In particular, any proof of $\Phi_B^{\rm def}(a)\ll \delta^p(\cdots)$ obtained solely from $\delta$-uniform pointwise bounds on
  $\sup_{\partial B_{\kappa/2}}|\mathcal L_a|$ cannot have $p>1$.
  \end{lemma}
  ```

  (ii) revised definitions/remarks

  ```tex
  % Replace Def. 12.5 by a delta-aware resonance sum (or add as Def. 12.5*)
  \begin{definition}[$\delta$-aware horizontal resonance sum (local window)]\label{def:resonance-sum-delta}
  For $a\in(0,1]$, $m\ge 10$, and $0<\delta\le a/4$, define
  \[
    \mathcal R_{a,\delta}(m)
    \ :=\
    \sum_{\rho:\,E(\rho)=0,\ |\Im(\rho)-m|\le 1}
    \frac{1}{|\Re(\rho)-a|+\delta},
  \]
  where zeros are counted with multiplicity.
  Then $\mathcal R_{a,\delta}(m)\le \delta^{-1}N_{\rm loc}(m)$.
  \end{definition}

  % Replace Remark 12.6 by a delta-aware target bound
  \begin{remark}[Target defect UE bound (OPEN; $\delta$-aware)]\label{rem:defect-UE-target-delta}
  A defect upper-envelope bound consistent with the resonance NO--GO (Lemma~\ref{lem:defect-resonance-nogo})
  should have the schematic form
  \[
    \Phi_B^{\rm def}(a)\ \le\ C_0\,\delta\log m\ +\ C_1\,\delta\,\mathcal R_{a,\delta}(m),
  \]
  uniformly for $0<\delta\le \delta_0(m,a)=\eta a/(\log m)^2$, with $C_0,C_1$ independent of $(m,a,\delta)$.
  In the toy-model configuration behind Lemma~\ref{lem:defect-resonance-nogo}, one has $\mathcal R_{a,\delta}(m)\gg 1/\delta$,
  so the right-hand side is $\gg 1$ and the bound does not contradict $\delta$-inertness.
  \end{remark}
  ```

  (iii) revised theorem/inequality lines

  ```tex
  % Patch Box 12.1: reconcile the p>1 phrase with the actual target scaling of Def. 12.2
  % (Minimal edit: remove the p>1 numeric claim and instead refer to "gate passing" via Theorem 12.12.)
  % Replace:
  %   "If (Transfer) and (Defect UE) are proven in a regime with effective p>1 (gate passing), ..."
  % By:
  %   "If (Transfer) and (Defect UE) are proven in a gate-passing regime (in the sense of Theorem~12.12),
  %    and (Resonance control) supplies the needed $\delta$-uniformity, ..."
  ```

* Dependencies on other branches:
  - **ML‑1 (Transfer):** any eventual closure still needs a domination lemma linking \(D_B(W)\) to a defect endpoint on a comparison box (Box `box:missing-lever-v39`).【892:2†manuscript_v39.pdf†L9-L20】
  - **ML‑3 (Resonance control):** must bound/exclude configurations forcing \(\mathcal R_{a,\delta}(m)\asymp 1/\delta\) at \(\delta=\delta_0(m,a)\).  
  - **Residual envelope ledger:** any “\(\delta\log m\)” term requires a clean RH‑free bound for the residual contributions (as assumed elsewhere in v3x–v39); not proved here.
* Referee risk notes (anticipated objections + how addressed):
  - **Objection:** “You did not prove a defect UE bound, only modified the target.”  
    **Response:** Correct; this branch result is a **NO‑GO for \(p>1\)** plus a **consistency repair**: without δ‑aware resonance, any δ‑uniform UE claim conflicts with Lemma `lem:defect-resonance-nogo`. The proposed edits prevent internal contradiction and clarify the true analytic obligation.
  - **Objection:** “Why alter Box `box:missing-lever-v39`?”  
    **Response:** Because the current ‘\(p>1\)’ requirement is inconsistent with the endpoint definition (Definition 12.2) and with the target bound (Remark 12.6). The patch replaces the numeric claim by the already‑formal gate language of Theorem 12.12.
  - **Objection:** “\(\mathcal R_{a,\delta}\) may be too strong / too hard to bound.”  
    **Response:** That is precisely the point: ML‑3 must either bound it or exclude the near‑resonant configuration; otherwise δ‑inertness is unavoidable by Lemma `lem:defect-resonance-nogo`.
