# Batch 10 — RH-ABSORB  
**Ground truth:** v39 locked build.  
**Deliverable:** v39→v40 “Gate Calculator” (S5\(^\mathrm{def}\)) + corrected exponent requirement + stop‑loss clause.

## 1) Anchors from v39 (what is already latched)

* **Nominal scale:** \(\delta_0(m,\alpha)=\eta \alpha/(\log m)^2\), with \(\alpha\approx a\) for an off‑axis quartet. 【840:5†manuscript_v39.pdf†L1-L22】
* **Forceable phase endpoint closure template:** Theorem 12.13 is the controlling closure schema: forcing lower bound + phase‑class UE+split upper bound + gate conditions \(2p\ge 1\), \(2(p-\theta)\ge q\), \(p-\theta>0\). 【840:5†manuscript_v39.pdf†L1-L22】
* **\(\kappa\)-shrink monotonicity test:** the envelope RHS is monotone in \(\delta\) only if the relevant \(\delta\)-exponents are \(\ge 0\); otherwise shrinking can *worsen* the inequality. 【840:12†manuscript_v39.pdf†L1-L36】
* **Missing Lever (v39):** ML‑1..ML‑3 are the conditional bridge from forcing to a defect endpoint class. 【836:14†manuscript_v39.pdf†L6-L42】

What follows is a **calculator** that (i) reduces any proposed ML‑2/ML‑3 package to explicit exponent inequalities, and (ii) produces an immediate PASS/FAIL for “can the forcing–vs–envelope contradiction be made uniform by \(\eta\)-shrinking at \(\delta=\delta_0(m,a)\)?”.

---

## 2) Deliverable A — One‑page “Gate Calculator” (defect + resonance)

### 2.1 Input format (what ENVELOPE/LOCAL must hand you)

Assume ML‑1..ML‑3 provide bounds of the schematic form:

1. **(FORCE)** Under an off‑axis quartet with displacement \(a>0\) at height \(m\), there exists a \(\kappa\)-admissible aligned \(B=B(\pm a,m,\delta)\) such that  
   \[
   \widetilde D_B(W)\ \ge\ c_{\rm force}-\delta\,\Xi(m)
   \]
   with \(c_{\rm force}>0\) absolute. (In many sub-lemmas \(c_{\rm force}=\pi/2\).) 【840:5†manuscript_v39.pdf†L1-L22】

2. **(Transfer / ML‑1)**  
   \[
   \widetilde D_B(W)\ \le\ C_{\rm tr}\,\Phi^{\rm def}_{\widehat B}(a)\ +\ {\rm Err}_{\rm tr}(m,a,\delta).
   \]
   (Here \(\widehat B\) is the buffered contour/box as in ML‑1.) 【836:14†manuscript_v39.pdf†L6-L42】

3. **(Defect UE / ML‑2)**  
   \[
   \Phi^{\rm def}_{\widehat B}(a)\ \le\ C_0\,\delta^{p}(\log m)^{u}\ +\ C_1\,\delta^{p-\theta}(\log m)^q\cdot{\mathsf{Res}}(m,a,\delta),
   \]
   with **\(\delta\)-uniform** constants \(C_0,C_1\) and explicit exponents \(p>0\), \(\theta\ge 0\).  
   (v39’s “target” version is \(p=1,\theta=0,u=q=1\), with \({\mathsf{Res}}=a\,\mathcal R_a(m)\).) 【836:12†manuscript_v39.pdf†L43-L50】

4. **(Resonance bound / ML‑3)**  
   \[
   {\mathsf{Res}}(m,a,\delta)\ \le\ C_R\,(\log m)^{q_R}\,a^{-r}\,\delta^{-r_\delta},
   \]
   with **\(\delta\)-uniform** \(C_R\) and explicit \(q_R,r,r_\delta\ge 0\).  
   If any structural NO‑GO is present (e.g. a \(\delta\)-inert resonance lower bound), that must be stated explicitly. 【836:5†manuscript_v39.pdf†L53-L76】

---

### 2.2 Algebraic reduction (the calculator)

Combine (Transfer)+(Defect UE)+(Resonance) to get an explicit envelope upper bound

\[
\widetilde D_B(W)\ \le\ A_0\,\delta^p(\log m)^u\ +\ A_1\,\delta^{p-\theta-r_\delta}(\log m)^{q+q_R}\,a^{-r}\ +\ {\rm Err}_{\rm tr}(m,a,\delta),
\]
where \(A_0:=C_{\rm tr}C_0\) and \(A_1:=C_{\rm tr}C_1C_R\).

Now evaluate at the nominal scale \(\delta=\delta_0(m,a)=\eta a/(\log m)^2\). Then:

* **Residual term**
  \[
  A_0\,\delta_0^p(\log m)^u
  =A_0\,\eta^p\,a^p\,(\log m)^{u-2p}.
  \]

* **Local/resonance term**
  \[
  A_1\,\delta_0^{p-\theta-r_\delta}(\log m)^{q+q_R}\,a^{-r}
  =A_1\,\eta^{p-\theta-r_\delta}\,a^{(p-\theta-r_\delta)-r}\,(\log m)^{(q+q_R)-2(p-\theta-r_\delta)}.
  \]

Define the **effective exponents**:

\[
p_{\rm eff}:=p,\qquad \theta_{\rm eff}:=\theta+r_\delta,\qquad q_{\rm tot}:=q+q_R,
\]
and the **log/a budgets**
\[
L_{\rm res}:=u-2p_{\rm eff},\qquad L_{\rm loc}:=q_{\rm tot}-2(p_{\rm eff}-\theta_{\rm eff}),\qquad A_{\rm loc}:=(p_{\rm eff}-\theta_{\rm eff})-r.
\]

---

### 2.3 Output conditions (PASS/FAIL tests)

The forcing–vs–envelope contradiction can be made **uniform** by choosing \(\eta\) small **provided** the following hold:

**(GC‑1) \(\delta\)-shrink monotonicity (safety under \(\kappa\)-shrinking).**  
All \(\delta\)-exponents appearing in the envelope RHS are \(\ge 0\). Concretely:
\[
p_{\rm eff}\ge 0,\qquad p_{\rm eff}-\theta_{\rm eff}\ge 0,
\]
and every \(\delta\)-power in \({\rm Err}_{\rm tr}\) is also \(\ge 0\).  
(Otherwise shrinking \(\delta\le\delta_0\) can *increase* the RHS.) 【840:12†manuscript_v39.pdf†L1-L36】

**(GC‑2) \(m\)-uniformity (log budget).**  
The log‑exponents at \(\delta=\delta_0\) do not grow with \(m\):
\[
L_{\rm res}\le 0\quad\text{and}\quad L_{\rm loc}\le 0,
\]
i.e.
\[
2p_{\rm eff}\ge u,\qquad 2(p_{\rm eff}-\theta_{\rm eff})\ge q_{\rm tot}.
\]
(This is the defect/resonance analogue of the \(q-2(p-\theta)\le 0\) constraint in the S5 budget proof.) 【840:12†manuscript_v39.pdf†L7-L33】

**(GC‑3) \(a\)-uniformity as \(a\downarrow 0\) (no hidden blow‑ups).**  
The local/resonance term does not blow up as \(a\to 0^+\):
\[
A_{\rm loc}\ge 0\quad\text{i.e.}\quad p_{\rm eff}-\theta_{\rm eff}\ge r.
\]
(If \(A_{\rm loc}<0\), then at \(\delta=\delta_0(m,a)\) the envelope upper bound diverges like \(a^{A_{\rm loc}}\), defeating any \(\eta\)-shrinking strategy under constant‑limited forcing.)

**(GC‑4) \(\eta\)-shrinkability (true contradiction leverage).**  
You must have strict \(\eta\)-decay in every non‑negligible term:
\[
p_{\rm eff}>0,\qquad p_{\rm eff}-\theta_{\rm eff}>0.
\]
If \(p_{\rm eff}-\theta_{\rm eff}=0\), the local term is \(\delta\)-inert and cannot be suppressed by \(\eta\)-shrinking (this is exactly the failure mode v39 rules out for absolute \(L^r\) endpoint swaps). 【840:12†manuscript_v39.pdf†L30-L33】【840:14†manuscript_v39.pdf†L21-L25】

**(GC‑5) Forcing correction budget.**  
To retain a positive forcing lower bound under \(\widetilde D_B(W)\ge c_{\rm force}-\delta\Xi(m)\), require
\[
\delta_0(m,a)\,\Xi(m)\ \le\ \tfrac14\,c_{\rm force}
\quad\text{uniformly for }m\ge 10,\ a\in(0,1].
\]
(This is a separate, explicit “forcing margin” condition; it is typically easiest at small \(\delta\).) 【840:5†manuscript_v39.pdf†L1-L22】

**Decision rule:** If (GC‑1)–(GC‑5) hold and \({\rm Err}_{\rm tr}(\delta_0)\) obeys the same budgets, then choosing \(\eta\le \eta_\star\) small enough forces  
\[
\widetilde D_B(W)\ <\ \tfrac12\,c_{\rm force}\ \le\ \widetilde D_B(W),
\]
a contradiction. (Supremum occurs at \(m=10\) and \(a=1\) once \(L_{\rm res},L_{\rm loc}\le 0\) and \(A_{\rm loc}\ge 0\).)

---

## 3) Deliverable B — What is the *true* “\(p>1\)” requirement?

v39’s structural closure gate is **not** “\(p>1\)”. It is a **budget inequality** in terms of the *effective* gap \(p_{\rm eff}-\theta_{\rm eff}\) plus log/a budgets.

* In the **old pointwise+collar** regime, \(\theta=1\) (local term behaves like \(\delta^{-1}\) per zero), and \(q\approx 1\) from \(N_{\rm loc}(m)\sim\log m\). Then the log‑budget condition \(2(p-\theta)\ge q\) forces \(p\ge 3/2\), which is why the “\(p>1\)” slogan appeared historically. 【840:5†manuscript_v39.pdf†L6-L12】【840:14†manuscript_v39.pdf†L21-L25】

* In the **defect endpoint** architecture targeted by ML‑2, the intended gain is \(\theta=0\) (true cancellation/local softening) with \(p=1\). If, additionally, resonance is **\(\delta\)-independent** (\(r_\delta=0\)) and the resonance majorant is no worse than \(a^{-1}\) (so \(r\le 1\), which the \(\delta_0\propto a\) scaling can absorb), then the calculator yields **PASS** with \(p=1\):  
  \(2p\ge 1\), \(2(p-\theta_{\rm eff})\ge q_{\rm tot}\) (typically \(2\ge 1\)), and \(p-\theta_{\rm eff}>0\).  
  In other words: **\(p=1\) is sufficient** if the local exponent truly drops to \(\theta_{\rm eff}=0\) and resonance is not \(\delta\)-singular.

* Therefore the correct v40 dashboard statement should read:

  > “What is required is **\(p_{\rm eff}-\theta_{\rm eff}\ge 1/2\)** (more generally \(2(p_{\rm eff}-\theta_{\rm eff})\ge q_{\rm tot}\)) with \(p_{\rm eff}-\theta_{\rm eff}>0\), plus \(a\)-uniformity; **\(p>1\) is not a standalone requirement**.”

---

## 4) Deliverable C — Stop‑loss clause (boxed NO‑GO decision rule)

A proof‑grade stop‑loss is:

> **If the best available ML‑2/ML‑3 package yields \(p_{\rm eff}-\theta_{\rm eff}\le 0\) or \(2(p_{\rm eff}-\theta_{\rm eff})<q_{\rm tot}\) (or any \(\delta\)-inert resonance obstruction), then no choice of global \(\eta\in(0,1)\) can make the S5\(^\mathrm{def}\) tail inequality close uniformly in \(m\ge 10\).**  
> In that event, the current architecture cannot produce an RH contradiction without new analytic input (new local cancellation or a different forceable endpoint class).

This is consistent with (i) the \(\delta\)-inert resonance NO‑GO already recorded in v39, and (ii) the general monotonicity/budget calculus in the S5 proof skeleton. 【836:5†manuscript_v39.pdf†L53-L76】【840:12†manuscript_v39.pdf†L30-L36】

---

## 5) S6 harness cross‑check (explicit‑formula amplitude leak)

Let \(\rho=\beta+i\gamma\) be an off‑critical‑line zero in the \(s\)-frame. In the \(v\)-frame used here, its horizontal displacement is  
\[
a = 2\beta-1>0,\qquad m=2\gamma.
\]
In explicit‑formula terms, such a zero contributes an oscillatory term with amplitude on the order of \(x^\beta = x^{1/2+a/2}\). A **gate PASS** contradiction excludes the existence of any \(a>0\), hence forbids all \(x^{1/2+a/2}\) amplitude leaks and is therefore RH‑equivalent at the level of zero locations. (No stronger prime error term is claimed beyond the RH implication.)

---

# MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* **Callsign:** RH-ABSORB  
* **Result classification:** **CONDITIONAL** (calculator is proof‑grade; ML‑1..ML‑3 still decide closure)  
* **Target gaps closed (by ID):**  
  - **Closes “drift risk”** on the S5\(^\mathrm{def}\) budget: makes exponent requirements explicit (new v40 latch).  
* **Target gaps still open (by ID):**  
  - ML‑1..ML‑3 remain the decisive open obligations (as already latched in v39). 【836:14†manuscript_v39.pdf†L6-L42】  
* **Key conclusions (≤5 bullets):**
  1. The correct closure requirement is **budget‑based**: \(p_{\rm eff}-\theta_{\rm eff}\) and the log/a exponents, not “\(p>1\)” as a slogan.
  2. Under defect cancellation with \(\theta_{\rm eff}=0\) and \(\delta\)-benign resonance, **\(p=1\) can pass** the gate.
  3. Any \(\delta\)-singular resonance factor (\(r_\delta>0\)) effectively increases \(\theta_{\rm eff}\) and can force failure.
  4. \(\delta\)-shrink monotonicity is non‑optional: negative \(\delta\)-exponents break the \(\kappa\)-shrink policy. 【840:12†manuscript_v39.pdf†L33-L36】
  5. A boxed stop‑loss clause prevents “proof tone” until ML‑1..ML‑3 satisfy the calculator.

* **Paste‑ready manuscript edits (TeX blocks):**

  (i) **New Remark: “Gate Calculator for S5\(^\mathrm{def}\)”** (insert immediately after Box `box:missing-lever-v39`)

```tex
\begin{remark}[S5$^{\mathrm{def}}$ Gate Calculator (v40 line in the sand; no drift)]
Assume the Missing Lever chain supplies:
\begin{align*}
\text{(FORCE)}\quad & \widetilde D_B(W)\ge c_{\rm force}-\delta\,\Xi(m),\\
\text{(Transfer)}\quad & \widetilde D_B(W)\le C_{\rm tr}\,\Phi^{\rm def}_{\widehat B}(a)+{\rm Err}_{\rm tr}(m,a,\delta),\\
\text{(Defect UE)}\quad & \Phi^{\rm def}_{\widehat B}(a)\le C_0\,\delta^{p}(\log m)^u + C_1\,\delta^{p-\theta}(\log m)^q\,{\mathsf{Res}}(m,a,\delta),\\
\text{(Resonance)}\quad & {\mathsf{Res}}(m,a,\delta)\le C_R(\log m)^{q_R}a^{-r}\delta^{-r_\delta}.
\end{align*}
Set $\delta=\delta_0(m,a)=\eta a/(\log m)^2$ and define
$p_{\rm eff}:=p$, $\theta_{\rm eff}:=\theta+r_\delta$, $q_{\rm tot}:=q+q_R$.
Then the envelope bound becomes
\[
\widetilde D_B(W)\le A_0\,\eta^{p_{\rm eff}}a^{p_{\rm eff}}(\log m)^{u-2p_{\rm eff}}
+A_1\,\eta^{p_{\rm eff}-\theta_{\rm eff}}a^{(p_{\rm eff}-\theta_{\rm eff})-r}
(\log m)^{q_{\rm tot}-2(p_{\rm eff}-\theta_{\rm eff})}
+{\rm Err}_{\rm tr}(\delta_0),
\]
with $A_0=C_{\rm tr}C_0$ and $A_1=C_{\rm tr}C_1C_R$.

\emph{Gate PASS sufficient conditions (uniform tail closure by $\eta$-shrinking):}
\begin{enumerate}
\item[$(\mathrm{GC}1)$] (\textbf{$\delta$-shrink monotonicity}) all $\delta$-exponents in the RHS are $\ge 0$,
in particular $p_{\rm eff}\ge 0$ and $p_{\rm eff}-\theta_{\rm eff}\ge 0$ (and the same for ${\rm Err}_{\rm tr}$).
\item[$(\mathrm{GC}2)$] (\textbf{log budget}) $2p_{\rm eff}\ge u$ and $2(p_{\rm eff}-\theta_{\rm eff})\ge q_{\rm tot}$.
\item[$(\mathrm{GC}3)$] (\textbf{$a$-uniformity}) $p_{\rm eff}-\theta_{\rm eff}\ge r$.
\item[$(\mathrm{GC}4)$] (\textbf{$\eta$-shrinkability}) $p_{\rm eff}>0$ and $p_{\rm eff}-\theta_{\rm eff}>0$.
\item[$(\mathrm{GC}5)$] (\textbf{forcing margin}) $\delta_0(m,a)\Xi(m)\le \tfrac14c_{\rm force}$ uniformly for $m\ge 10$.
\end{enumerate}
If $(\mathrm{GC}1)$--$(\mathrm{GC}5)$ hold and ${\rm Err}_{\rm tr}(\delta_0)$ obeys the same budgets, then there exists
$\eta_\star\in(0,1)$ such that for all $\eta\le\eta_\star$ the forcing inequality contradicts the envelope bound,
hence no off-axis quartet exists for any $m\ge 10$.
\end{remark}
```

  (ii) **Replace any “\(p>1\)” slogan** near the Missing Lever box by the correct statement:

```tex
\begin{remark}[Correct exponent requirement (no slogans)]
The closure requirement is not ``$p>1$'' in isolation. What matters is the \emph{effective gap}
$p_{\rm eff}-\theta_{\rm eff}$ (including any $\delta$-loss from resonance) together with the log/a budgets
in Remark~\ref{rem:S5def-gate-calculator}. In particular, $p=1$ is sufficient if $\theta_{\rm eff}=0$ and the
log/a constraints pass.
\end{remark}
```

  (iii) **Stop‑loss clause** (boxed policy; insert at end of Section 12):

```tex
\begin{remark}[Stop-loss clause (budget failure implies no closure in this architecture)]
If the best available Missing Lever estimates yield either
$p_{\rm eff}-\theta_{\rm eff}\le 0$ or $2(p_{\rm eff}-\theta_{\rm eff})<q_{\rm tot}$ (or any $\delta$-inert resonance
obstruction), then no global $\eta\in(0,1)$ can make the S5$^{\mathrm{def}}$ tail inequality close uniformly in
$m\ge 10$. In that event, the current architecture cannot derive an RH contradiction without new analytic input
(e.g. a genuine local cancellation/isolation lemma or a new forceable endpoint class).
\end{remark}
```

* **Dependencies on other branches:**  
  - ENVELOPE/LOCAL must supply ML‑2/ML‑3 with explicit \((p,\theta,u,q,q_R,r,r_\delta)\) and \(\delta\)-uniform constants.  
  - FORCE must supply \(c_{\rm force}\), \(\Xi(m)\) with explicit growth so (GC‑5) can be checked.  
  - BRIDGE must validate Transfer error \({\rm Err}_{\rm tr}\) with explicit exponent data.

* **Referee risk notes (anticipated objections + how addressed):**
  1. **Hidden \(\delta\)-dependence** in “constants”: the calculator forces all \(\delta\)-exponents to be declared (GC‑1).
  2. **A‑blow‑ups** as \(a\to 0\): explicitly gated by (GC‑3); failure is immediately visible.
  3. **\(\kappa\)-shrinking non‑monotone**: explicitly latched by (GC‑1) and cited from v39’s monotonicity proof. 【840:12†manuscript_v39.pdf†L33-L36】
  4. **Resonance δ‑inertia:** explicitly treated as a stop‑loss failure mode (consistent with the in‑text NO‑GO). 【836:5†manuscript_v39.pdf†L53-L76】
