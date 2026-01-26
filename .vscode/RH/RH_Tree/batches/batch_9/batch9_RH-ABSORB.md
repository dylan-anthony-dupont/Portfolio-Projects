# Batch 9 — RH-ABSORB (pre‑v39 design audit; v38 locked baseline)

**Callsign:** RH‑ABSORB  
**Mission:** Audit the redesigned *defect endpoint* class \((\mathcal Q_a,\mathcal L_a)\) against the existing acceptance gate and rewrite the tail/absorption closure logic in this new endpoint class, **without** RH smuggling and with explicit \(s\to u\to v\) mapping and a forced‑zero obstruction note.

---

## 0) Frame mapping + defect objects (explicit \(s\to u\to v\))

- **\(s\)-frame:** \(s=\sigma+it\) in the critical strip.
- **\(u\)-frame (width‑2):** \(u=2s\).
- **\(v\)-frame (centered):** \(v=u-1\), so \(s=(1+v)/2\).

A nontrivial zero \(\rho=\beta+i\gamma\) in \(s\)-frame corresponds to  
\[
u_\rho=2\rho=2\beta+i\,2\gamma,\qquad v_\rho=u_\rho-1=(2\beta-1)+i\,2\gamma.
\]
Define:
\[
a:=2\beta-1\in(-1,1),\qquad m:=2\gamma>0.
\]
“Off‑critical‑line” means \(a\neq 0\) (wlog \(a>0\) by symmetry).

**Completed object (entire, even in \(v\) under the functional equation):**
\[
E(v):=\Xi_2(1+v)=\xi\!\left(\frac{1+v}{2}\right),\qquad\text{so }E(v)=E(-v)\ \text{(to be explicitly latched in-text)}.
\]

**Defect quotient and defect log‑derivative (preferred endpoint primitive):**
\[
\mathcal Q_a(v):=\frac{E(v+a)}{E(v-a)},\qquad 
\mathcal L_a(v):=\partial_v\log \mathcal Q_a(v)=\frac{E'}{E}(v+a)-\frac{E'}{E}(v-a).
\]

**Nominal box scale (Batch‑9 instruction):**
\[
\delta_0(m,a)=\frac{\eta\,a}{(\log m)^2},\qquad \eta\in(0,1].
\]

---

## A) Gate audit table (mandatory): check \((p,\theta,q)\) against the S5‑budget gate

### A1) What the gate checks

Assume ENVELOPE provides a defect‑endpoint UE+split inequality of schematic form
\[
\widetilde D_B^{\rm def}\ \le\ C_{\rm up}\,\delta^{p}\Bigl(\mathrm{Res}(m)+C_{\rm loc}\,\delta^{-\theta}\,G(N_{\rm eff}(m,\delta),\kappa)\Bigr),
\]
with growth model \(G(n,\kappa)\le C_G\kappa^{-u}n^q\) and δ‑uniform constants.

The **locked** acceptance gate to check is:
\[
2p\ge 1,\qquad 2(p-\theta)\ge q,\qquad p-\theta>0.
\]

### A2) Gate check table (fill with ENVELOPE’s proposed \((p,\theta,q)\))

Let \((p,\theta,q)\) be the proposed exponent triple.

| Gate inequality | LHS | RHS | PASS/FAIL | Referee note (what it controls) |
|---|---:|---:|:---:|---|
| \(2p\ge 1\) | \(2p\) | \(1\) | **PASS iff** \(p\ge \tfrac12\) | residual shrink at \(\delta_0\) when \(\mathrm{Res}(m)\sim \log m\) |
| \(2(p-\theta)\ge q\) | \(2(p-\theta)\) | \(q\) | **PASS iff** \(q\le 2(p-\theta)\) | local shrink at \(\delta_0\) when \(N_{\rm eff}\sim \log m\) |
| \(p-\theta>0\) | \(p-\theta\) | \(0\) | **PASS iff** \(p>\theta\) | η‑shrinkability + monotone δ‑shrink safety |

**Gate verdict (mandatory):**  
- **PASS** exactly when all three inequalities hold.  
- **FAIL** otherwise.

### A3) Concrete instantiation (the *expected* defect‑endpoint budget)

Based on the defect primitive \(\mathcal L_a\) and the typical estimate
\[
|\Delta\arg \mathcal Q_a|\ \lesssim\ \int | \mathcal L_a|\ \lesssim\ (2\delta)\,\sup_{\partial B}|\mathcal L_a|,
\]
a **plausible** exponent assignment is:

- \(p=1\) (coming from the segment length factor \(2\delta\)),
- \(\theta=0\) (if the defect difference removes the \(\delta^{-1}\) collar blow‑up),
- \(q=1\) (worst‑case \(N_{\rm eff}\sim N_{\rm loc}(m)\asymp \log m\)).

For \((p,\theta,q)=(1,0,1)\), the three gate inequalities read:
\[
2p=2\ge 1,\quad 2(p-\theta)=2\ge 1=q,\quad p-\theta=1>0,
\]
so **gate PASS**.

**Important (referee note):** this PASS is **conditional** on ENVELOPE/LOCAL actually proving the claimed \((p,\theta,q)\) with δ‑uniform constants in the defect endpoint class.

### A4) NEW (must not be hidden): “\(a\)-uniformity” check for defect endpoints

Because the defect kernel can introduce explicit factors of \(a^{-1}\) (typical after cancellation of the pole at \(v=im\)), there is an additional uniformity check as \(a\downarrow 0\):

> If the local bound contains an explicit \(a^{-r}\) factor (often \(r=1\)), then at \(\delta_0=\eta a/(\log m)^2\) one must also require  
> \[
> p-\theta-r\ \ge\ 0
> \]
> to prevent blow‑up as the off‑axis displacement \(a\to 0\).

This “\(a\)-budget” is **not** part of the legacy S5 gate, but it is mandatory for proof‑grade uniformity in the off‑axis parameter.

---

## B) δ‑policy compatibility (mandatory): what becomes absorbable under \(\delta_0=\eta a/(\log m)^2\)

### B1) General computation at the nominal scale

Assume the defect endpoint upper bound is of the form
\[
\widetilde D_B^{\rm def}
\le
C_{\rm up}\,\delta^{p}\Bigl(\mathrm{Res}(m)+C_{\rm loc}\,\delta^{-\theta}\,\kappa^{-u}\,N_{\rm eff}(m,\delta)^{q}\Bigr),
\]
and that \(N_{\rm eff}(m,\delta)\le C_N\log m\) (worst‑case model).

Set \(\delta=\delta_0(m,a)=\eta a/(\log m)^2\). Then:

**Residual term**
\[
\delta_0^{p}\,\mathrm{Res}(m)\ \sim\
\eta^{p}a^{p}\,(\log m)^{-2p}\,\mathrm{Res}(m).
\]
If \(\mathrm{Res}(m)\ll (\log m)^1\), the condition \(2p\ge 1\) ensures this is uniformly bounded in \(m\), and η‑shrinkable if \(p>0\).

**Local term**
\[
\delta_0^{p-\theta}\,N_{\rm eff}(m,\delta_0)^q
\ \ll\
\eta^{p-\theta}a^{p-\theta}\,(\log m)^{-2(p-\theta)}\,(\log m)^{q}
=
\eta^{p-\theta}a^{p-\theta}\,(\log m)^{q-2(p-\theta)}.
\]
Thus the legacy gate conditions \(2(p-\theta)\ge q\) and \(p-\theta>0\) ensure:
- **uniform boundedness in \(m\)** (no growth in \(\log m\)), and
- **η‑shrinkability** via the factor \(\eta^{p-\theta}\).

### B2) What does *not* absorb

- If \(2(p-\theta)<q\), then the local term grows like \((\log m)^{q-2(p-\theta)}\) and cannot be absorbed uniformly as \(m\to\infty\) under constant‑limited forcing.
- If \(p-\theta\le 0\), η‑shrinking does not reduce the local term, and δ‑shrink monotonicity breaks.

### B3) Defect‑specific warning (uniformity in \(a\))

If LOCAL/ENVELOPE bounds introduce an explicit \(a^{-r}\) penalty (typical \(r=1\)), then the local term at \(\delta_0\) becomes
\[
\eta^{p-\theta}a^{p-\theta-r}(\log m)^{q-2(p-\theta)}.
\]
To keep the closure uniform as \(a\downarrow 0\) (zeros arbitrarily close to the critical line), one must enforce:
\[
p-\theta-r\ge 0.
\]
Example: if \(r=1\) and \(p-\theta=1\), the \(a\)-factor cancels and the local term is uniformly shrinkable.

---

## C) Rewrite the “Missing Lever” OPEN box (mandatory; paste‑ready v38→v39 patch)

### C1) Forced‑zero obstruction (must be latched)

The defect endpoint class is **not automatically forceable** by a single interior zero in the way that the buffered phase endpoint \(\widetilde D_B(W)\) was.

**Reason (topological / cancellation):**
- Under an off‑axis quartet at \(v=\pm a\pm im\), the defect quotient \(\mathcal Q_a(v)=E(v+a)/E(v-a)\) has a *removable* singularity at \(v=im\) (it is \(0/0\) there).
- Correspondingly, \(\mathcal L_a(v)\) cancels the principal poles at \(v=im\) coming from the symmetric pair \(v=\pm a+im\).  
- Therefore, **argument‑principle forcing is not automatic** for any defect endpoint defined on a symmetric contour around \(v=im\): one interior quartet does not force a fixed nonzero winding/phase increment of \(\mathcal Q_a\) on that contour.

**Implication:** Any attempt to “replace the old forced endpoint by the defect endpoint” must include either:
1. a **domination/transfer lemma** (forced endpoint \(\Rightarrow\) defect endpoint is large), or
2. a **new forcing lemma** targeting the defect endpoint directly.

Without one of these, the defect endpoint is not a valid contradiction endpoint.

### C2) Paste‑ready TeX patch: replace the v38 Missing Lever box

Replace the entire v38 box beginning at the comment
`% OPEN (Missing Lever): budget-eligible S5' endpoint (v38)` with:

```tex
% ============================================================
% OPEN (Missing Lever): DEFECT endpoint class (pre-v39)
% ============================================================
\begin{center}
\fbox{\begin{minipage}{0.96\linewidth}
\textbf{OPEN (Missing Lever for S5$^{\rm def}$ tail closure; no silent closure).}
\vspace{2mm}

\textbf{Frame data.}
Assume an off-axis zero $\rho=\beta+i\gamma$ exists in $s$-frame with $\beta>1/2$ and set
$u=2s$, $v=u-1$, $a=2\beta-1>0$, $m=2\gamma$.
Fix $\eta\in(0,1]$, $\kappa\in(0,1/10)$, and the nominal scale
$\delta_0(m,a)=\eta a/(\log m)^2$.

\medskip
\textbf{Defect primitives.}
Define the completed even entire function $E(v)=\Xi_2(1+v)$ and the defect objects
\[
\mathcal Q_a(v):=\frac{E(v+a)}{E(v-a)},\qquad
\mathcal L_a(v):=\partial_v\log\mathcal Q_a(v)=\frac{E'}{E}(v+a)-\frac{E'}{E}(v-a).
\]
Let $\widetilde D_B^{\rm def}(E;a)$ denote the chosen defect endpoint functional on any
$\kappa$--admissible aligned box $B=B(\pm \alpha,m,\delta)$ with $0<\delta\le \delta_0(m,a)$.

\medskip
\textbf{FORCED-ZERO OBSTRUCTION (must be discharged).}
Unlike the buffered phase endpoint $\widetilde D_B(W)$, the defect quotient $\mathcal Q_a$
has a removable singularity at $v=im$ under the symmetric pair $v=\pm a+im$ (it is $0/0$ there),
and $\mathcal L_a$ cancels the principal poles at $v=im$.
Hence no argument-principle forcing lower bound for $\widetilde D_B^{\rm def}$ is automatic.
To make S5$^{\rm def}$ valid, one must prove either:
(i) a transfer lemma $\widetilde D_B(W)\le C\,\widetilde D_B^{\rm def}(E;a)$ (or $D_B(W)\le C\,\widetilde D_B^{\rm def}$),
so the existing FORCE chain transfers; or
(ii) a new forcing lemma directly giving $\widetilde D_B^{\rm def}(E;a)\ge c_{\rm force}-\delta\,\Xi(m)$.

\medskip
\textbf{ENVELOPE (missing).}
To activate the S5$^{\rm def}$ closure theorem, it remains to prove a defect-class UE+split bound
\[
\widetilde D_B^{\rm def}(E;a)\ \le\ C_{\rm up}\,\delta^{p}\Bigl(\mathrm{Res}(m)+C_{\rm loc}\,\delta^{-\theta}\,G(N_{\rm eff}(m,\delta),\kappa)\Bigr),
\]
uniformly for all $m\ge 10$, all $a\in(0,1]$, and all $\kappa$--admissible $0<\delta\le\delta_0(m,a)$,
with $C_{\rm up},C_{\rm loc}$ independent of $\delta$ and with $G(n,\kappa)\le C_G\kappa^{-u}n^{q}$.

\medskip
\textbf{BUDGET GATE (non-negotiable).}
The declared exponent tuple $(p,\theta,q)$ must satisfy
\[
2p\ge 1,\qquad 2(p-\theta)\ge q,\qquad p-\theta>0,
\]
and any explicit $a^{-r}$ loss in the local term must be declared and canceled at $\delta=\delta_0$.

\medskip
\textbf{NO CLAIM POLICY.}
Until the FORCE transfer/direct forcing and the ENVELOPE bound are proved in-text (or cited referee-grade),
the manuscript makes \emph{no} claim of tail closure and \emph{no} claim of RH from S5$^{\rm def}$.
\end{minipage}}
\end{center}
```

### C3) Paste‑ready TeX patch: closure theorem restatement (minimal)

Add **after** Theorem~\ref{thm:S5prime-closure}:

```tex
\begin{theorem}[S5$^{\rm def}$ closure from a defect endpoint]\label{thm:S5def-closure}
Fix $\kappa\in(0,1/10)$ and $\eta\in(0,1)$ and define $\delta_0(m,a)=\eta a/(\log m)^2$.
Let $\widetilde D_B^{\rm def}(E;a)$ be a defect endpoint assigned to each $\kappa$--admissible
aligned box $B=B(\pm \alpha,m,\delta)$ and the defect primitives $(\mathcal Q_a,\mathcal L_a)$.
Assume:
\begin{enumerate}[leftmargin=1.5em]
  \item[(S5$^{\rm def}$--FORCE)] Under an off-axis quartet at height $m$ with displacement $a>0$,
  there exists an aligned $\kappa$--admissible box $B$ (with $\alpha\asymp a$) such that
  $\widetilde D_B^{\rm def}(E;a)\ge c_{\rm force}-\delta\,\Xi(m)$ with $c_{\rm force}>0$ absolute and
  $\Xi(m)\ge 0$ explicit.
  \item[(S5$^{\rm def}$--UE+SPLIT)] For every $\kappa$--admissible aligned box,
  \[
    \widetilde D_B^{\rm def}(E;a)\le C_{\rm up}\,\delta^p\Big(\mathrm{Res}(m)+C_{\rm loc}\,\delta^{-\theta}\,G(N_{\rm eff}(m,\delta),\kappa)\Big),
  \]
  where $p>0$, $\theta\ge 0$, and $C_{\rm up},C_{\rm loc}$ are $\delta$--uniform, and
  $G(n,\kappa)\le C_G\,\kappa^{-u}n^q$ for fixed $u,q\ge 0$.
\end{enumerate}
Suppose additionally that $2p\ge 1$, $2(p-\theta)\ge q$, and $p-\theta>0$.
Then there exists $\eta_\star\in(0,1)$ (depending on the displayed constants and $\kappa$) such that
for every $\eta\in(0,\eta_\star]$ the S5$^{\rm def}$ tail inequality holds at $\delta=\delta_0(m,a)$
for all $m\ge 10$ and all $a\in(0,1]$, and hence no off-axis quartet exists at any height $m\ge 10$.
Combined with any finite-height front-end, this implies RH.
\end{theorem}
```

---

## D) S6 explicit‑formula mapping (mandatory; conservative)

If the closure theorem (S5\(^\text{def}\)) were proved, it would imply: **no zero with \(\beta>1/2\)**, i.e. RH.

Under the classical explicit formula for \(\psi(x)\), each zero \(\rho=\beta+i\gamma\) contributes a term of size roughly \(x^{\beta}\) (up to logarithmic factors). In \(v\)-coordinates, \(\beta=1/2+a/2\), so an off-axis displacement \(a>0\) corresponds to an **amplitude leak** of order
\[
x^{1/2+a/2}\quad\text{in prime-error terms}.
\]
Therefore:

- **Gate PASS + FORCE + ENVELOPE ⇒ no \(a>0\) ⇒ no \(x^{\beta}\) leak with \(\beta>1/2\).**
- This consequence is **RH-equivalent**, not merely RH-implied, in the usual explicit‑formula sense.

What is **not** claimed here: that the defect endpoint itself is *directly* an explicit-formula prime-amplitude functional. The mapping is by implication chain “S5\(^\text{def}\) closure ⇒ RH ⇒ explicit-formula error bounds,” unless a separate, explicit formula bridge lemma is added.

---

# PATCH PACKET

* Callsign: RH‑ABSORB
* Result classification: **CONDITIONAL**
* Target gaps closed (by ID):  
  - **(None fully closed)** — this batch converts the defect endpoint idea into a *proof‑grade acceptance gate + obstruction latch*, but does not prove FORCE/ENVELOPE.
* Target gaps still open (by ID):  
  - **NEW (recommended):** `G-2(def)` = forceability/transfer for the defect endpoint (forced‑zero obstruction must be discharged).  
  - **NEW (recommended):** `G-4(def)` = defect-class UE+split with declared \((p,\theta,q)\) and δ‑uniform constants.  
  - **Inherited:** κ‑admissibility for any shifted evaluation needed to define \(\mathcal Q_a,\mathcal L_a\) on buffered contours (BRIDGE/LOCAL dependency).
* Key conclusions (≤5 bullets):
  1. The legacy S5 gate \((2p\ge 1,\ 2(p-\theta)\ge q,\ p-\theta>0)\) still governs η‑shrinking at \(\delta_0=\eta a/(\log m)^2\).
  2. For defect endpoints, an additional **\(a\)-uniformity** check is mandatory if local bounds carry explicit \(a^{-r}\) losses.
  3. The defect endpoint class is **not automatically forceable**: the off-axis quartet yields a removable singularity in \(\mathcal Q_a\) at \(v=im\) and cancels poles in \(\mathcal L_a\), so argument‑principle forcing does not automatically apply.
  4. If ENVELOPE can prove (plausibly) \((p,\theta,q)=(1,0,1)\) with δ‑uniform constants (and declared \(a\)-dependence), the **budget gate would PASS**.
  5. Closure in the defect endpoint class is therefore **conditional** on a new FORCE transfer/direct forcing lemma plus the defect-class UE+split inequality.
* Paste‑ready manuscript edits:
  (i) revised lemma/proposition statements  
  - Add Theorem `thm:S5def-closure` (block above).  
  (ii) revised definitions/remarks  
  - Replace v38 Missing Lever box with the defect‑endpoint version (block above).  
  (iii) revised theorem/inequality lines  
  - None beyond inserting `thm:S5def-closure` and updating δ0 to \(\delta_0(m,a)=\eta a/(\log m)^2\) where used.
* Dependencies on other branches:
  - **RH‑FORCE:** must supply `G-2(def)` via a transfer lemma from \(D_B(W)\) / \(\widetilde D_B(W)\) to \(\widetilde D_B^{\rm def}\), or a direct forcing lemma for the defect endpoint.  
  - **RH‑ENVELOPE:** must supply defect-class UE+split with declared \((p,\theta,q)\), δ‑uniform constants, and declared \(a\)-dependence.  
  - **RH‑LOCAL / RH‑BRIDGE:** must ensure κ‑admissibility/contour nonvanishing is stable under the shifted evaluations \(v\mapsto v\pm a\) in \(\mathcal Q_a,\mathcal L_a\).
* Referee risk notes (anticipated objections + how addressed):
  - **Objection:** “You replaced a forced endpoint by an unforced one.”  
    **Answer:** Explicitly latched as the forced‑zero obstruction; closure theorem requires a new FORCE transfer/direct forcing input.
  - **Objection:** “You hid \(a\)-dependence in constants.”  
    **Answer:** Added an explicit \(a\)-uniformity check; any \(a^{-r}\) loss must be declared and canceled at \(\delta_0\).
  - **Objection:** “Branch/log issues for \(\log \mathcal Q_a\).”  
    **Answer:** Endpoint should be defined via \(\mathcal L_a=\partial_v\log\mathcal Q_a\) (log-derivative), avoiding branch choices; remaining nonvanishing assumptions must be explicit.
