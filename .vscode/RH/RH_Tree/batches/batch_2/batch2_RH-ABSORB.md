# Batch 2 — RH-ABSORB (v33 base)  
**Callsign:** RH-ABSORB  
**Targets:** Δ‑NEXT‑2 (**G‑4**) δ‑uniformity for η‑absorption; completion‑level (**G‑5**) κ‑admissibility / shrink‑δ compatibility.  
**Ground truth:** `manuscript_v33.tex/pdf` only (no v32 patching).

---

## 0) v33 absorption interface (what must be δ‑uniform)

### 0.1 Tail inequality (post‑pivot; v33)
v33’s tail inequality (Theorem `\ref{thm:tail-inequality}` / Eq. `\eqref{eq:tail-ineq}`) is:

\[
2C_{\mathrm{up}}\Bigl(\delta^{3/2}L(m)\; +\; \delta^{1/2}\,\frac{N_{\rm up}(m)}{\kappa}\Bigr)
\ <\
 c\ -\ \delta\Bigl(K_{\rm alloc}\,c_0\,L(m)+C_h''\,(\log m+1)\Bigr),
\tag{TAIL}
\]

with the **nominal** scale
\[
\delta_0(m,\alpha):=\frac{\eta\alpha}{(\log m)^2},
\]
and an **actual** chosen scale \(0<\delta\le \delta_0\) (to enforce κ‑admissibility), with safety under δ‑shrinking provided by Lemma `\ref{lem:delta-shrink-monotone}`.

### 0.2 Worst‑case η‑absorption reduction (v33)
At \((m,\alpha)=(10,1)\) and \(\delta=\delta_0(10,1)\), v33 rewrites the tail inequality as:

\[
A\,\eta^{3/2}+B\,\eta^{1/2} < c - D\,\eta,
\]

with coefficients (v33 §`\ref{sec:eta-absorption}`):

\[
A:=\frac{2C_{\rm up}L(10)}{(\log 10)^3},\qquad
B:=\frac{2C_{\rm up}N_{\rm up}(10)}{\kappa\,\log 10},\qquad
D:=\frac{K_{\rm alloc}c_0L(10)+C_h''(\log 10+1)}{(\log 10)^2}.
\]

Thus **η‑absorption is proof‑grade once \(A,B,D\) are finite and independent of \(\delta\)** (equivalently independent of η, except through the explicit powers shown).

---

## Task A (CRITICAL) — δ‑uniformity audit ledger (G‑4)

### A.1 Ledger: every constant entering (TAIL) and \((A,B,D)\)

Classification keys:

- **δ‑UNIFORM (proven in v33):** constant is independent of \(\delta\) (and hence η), with explicit v33 definition/quantifier.
- **δ‑DEPENDENT BUT HARMLESS:** explicit dependence remains but is controlled by a positive δ‑power in (TAIL).
- **OPEN DEPENDENCY:** v33 asserts existence but does not yet provide the proof-grade statement/quantifiers needed for δ‑uniform absorption.

| Symbol / package | Where it enters | v33 source | δ‑uniformity status | Notes for absorption |
|---|---|---|---|---|
| \(c_0,c\) | RHS forcing term | Theorem `\ref{thm:tail-inequality}` (assumption 1) | **δ‑UNIFORM (proven)** | Explicit constants \(c_0=\frac{3\log 2}{8\pi}\), \(c=\frac{3\log 2}{16}\). Independent of \(\delta\). |
| \(K_{\rm alloc}\) | RHS forcing term | Theorem `\ref{thm:tail-inequality}` (assumption 1) | **δ‑UNIFORM (proven)** | Restored to \(3+8\sqrt3\) in v33. Independent of \(\delta\). |
| \(\kappa\) | LHS local term denominator | Definition `\ref{def:collar-admissible}` | **δ‑UNIFORM (proven)** | Fixed parameter; δ‑dependence is explicit only through the \(\delta^{1/2}\) factor in (TAIL). |
| \(N_{\rm loc}(m)\) | local log‑derivative bound | Lemma `\ref{lem:Zloc-logder-collar}` | **δ‑DEPENDENT BUT HARMLESS (explicit)** | Appears as \(N_{\rm loc}(m)/(\kappa\delta)\) inside \(\sup|E'/E|\), but UE multiplies by \(\delta^{3/2}\), yielding net \(\delta^{1/2}N_{\rm loc}(m)/\kappa\). |
| \(N_{\rm up}(m)\) | tail majorant used in (TAIL) | Lemma `\ref{lem:Nloc-logm}`, §`\ref{sec:tail}` | **δ‑UNIFORM (proven)** | Explicit unconditional bound: \(N_{\rm loc}(m)\le N_{\rm up}(m):=1.01\log m+17\) for \(m\ge 10\). No \(\delta\) present. |
| \(C_{\rm up}\) | LHS prefactor and A,B | Lemma `\ref{lem:upper-envelope}` + Lemma `\ref{lem:shape-only}` | **δ‑UNIFORM (proven in statement)** | v33 defines \(C_{\rm up}\) as shape‑only (depends only on normalized square \(Q\)), hence independent of \((\alpha,m,\delta)\). Finiteness relies on standard boundedness of Poisson kernel sup and \(L^2\)-boundedness of boundary conjugation on \(\partial Q\) (should be cited if a referee insists). |
| \(C_1,C_2\) | \(L(m)=C_1\log m+C_2\) (LHS+RHS via D) and \(C_h''\) | Lemma `\ref{lem:residual-envelope}` | **OPEN DEPENDENCY (δ‑uniformity + proof missing)** | v33 asserts existence of absolute \(C_1,C_2\) at the *nominal* scale. To make κ‑shrinking compatible with the proof spine, the lemma must be strengthened to cover all \(0<\delta\le\delta_0\) (or an η‑free upper range), and proven unconditionally. |
| \(C_h''\) | RHS horizontal budget | Lemma `\ref{lem:horizontal-budget}` | **OPEN DEPENDENCY (inherits C1,C2)** | Defined as \(C_h'':=4\max\{C_1,C_2\}\). δ‑uniform iff \(C_1,C_2\) are δ‑uniform. |
| \(L(m)\) | both sides | §`\ref{sec:tail}` | **OPEN DEPENDENCY (inherits C1,C2)** | Defined from \(C_1,C_2\). Absorption requires \(L(10)\) finite and η‑independent. |
| \(\log 10\) (and fixed numerics) | denominators in A,B,D | §`\ref{sec:eta-absorption}` | **δ‑UNIFORM (trivial)** | Pure constants. |

**Bottom line for G‑4:**  
η‑absorption in v33 is **proof‑grade conditional** on a single analytic package: a δ‑uniform residual envelope bound producing absolute \(C_1,C_2\) valid at the **actual chosen κ‑admissible scale** \(0<\delta\le\delta_0\) (and therefore also \(C_h''\), \(L(m)\) δ‑uniform).

### A.2 v33‑correct worst‑case coefficients (m=10, α=1)

Using v33’s explicit local bound:
\[
N_{\rm up}(10)=1.01\log 10+17,
\]
and the restored allocation constant:
\[
K_{\rm alloc}=3+8\sqrt3,
\]
the worst‑case coefficients are exactly:

\[
A=\frac{2C_{\rm up}(C_1\log 10+C_2)}{(\log 10)^3},
\]
\[
B=\frac{2C_{\rm up}(1.01\log 10+17)}{\kappa\,\log 10},
\]
\[
D=\frac{(3+8\sqrt3)c_0(C_1\log 10+C_2)+C_h''(\log 10+1)}{(\log 10)^2}.
\]

No additional δ‑dependence is present **provided** \(C_{\rm up},C_1,C_2,C_h''\) are absolute (δ‑uniform).

### A.3 Acceptance-test theorem (clean conditional closure)

**Theorem (η‑absorption closure under δ‑uniform ledger).**  
Assume Lemma `\ref{lem:residual-envelope}` holds with **absolute** constants \(C_1,C_2\) uniformly for all \(m\ge 10\), all \(\alpha\in(0,1]\), and all scales \(0<\delta\le\delta_0(m,\alpha)\). Then \(A,B,D\) above are finite and independent of η, hence Proposition `\ref{prop:eta-absorption}` produces an \(\eta_\star>0\) such that for all \(\eta\le\eta_\star\) the tail inequality holds for all \(m\ge 10\) and \(\alpha\in(0,1]\) at the nominal scale, and therefore (by δ‑shrink monotonicity) for all κ‑admissible \(0<\delta\le\delta_0\).

This is the proof‑grade form of “η‑absorption closes once constants are finite and δ‑uniform.”

---

## Task B (HIGH) — Finish κ‑policy compatibility across the full spine (G‑5)

v33 already contains:

- κ‑admissible shrink existence (Lemma `\ref{lem:collar-existence}`),
- δ‑shrink monotonicity (Lemma `\ref{lem:delta-shrink-monotone}`),
- explicit local window bound independent of δ (Lemma `\ref{lem:Nloc-logm}`),
- and a tail closure reduction that explicitly invokes δ‑shrinking safety (Theorem `\ref{thm:tail-closure}`).

**What remains for completion‑level G‑5** is a single explicit compatibility lemma/remark that ties κ‑shrinking to each step where a referee could object.

### Proposed compatibility lemma (paste-ready; see Patch Packet)

Core content:

1) **Forcing allocation is preserved under δ‑shrinking:** in the quartet contradiction the dial is aligned by taking \(\alpha=a\), hence \(|\alpha-a|=0\le \delta\) for any \(\delta>0\), so Lemma `\ref{lem:short-side-forcing}` is not weakened by shrinking δ.

2) **UE hypotheses are preserved:** κ‑admissibility implies \(\dist(\partial B,\mathcal Z(E))\ge \kappa\delta>0\), hence no boundary zeros; this implies boundary‑contact holds and Lemma `\ref{lem:upper-envelope}` applies.

3) **Local window definition is unaffected:** \(N_{\rm loc}(m)\) depends only on the vertical window \(|\Im \rho-m|\le 1\), not on δ; shrinking δ does not change \(Z_{\rm loc}\)’s defining set, only improves collar separation.

4) **Monotonicity reductions remain valid:** once the tail inequality is checked at nominal \(\delta_0\), δ‑shrinking only improves it (Lemma `\ref{lem:delta-shrink-monotone}`), so worst‑case reductions (α=1, m=10) remain sound.

5) **Residual/horizontal budget compatibility:** requires the strengthened residual envelope statement to hold for all \(0<\delta\le\delta_0\) (this is the exact intersection of G‑4 and completion‑level G‑5).

---

## Task C — Coordination note (single decisive missing analytic input)

**Decisive missing input for proof‑grade η‑absorption (and for κ‑policy completeness):**

> **Upgrade Lemma `\ref{lem:residual-envelope}` to be δ‑robust and prove it unconditionally.**  
> Specifically, the residual envelope bound must apply at the **actual κ‑admissible scale** \(0<\delta\le\delta_0(m,\alpha)\), not only at \(\delta=\delta_0\).

This is the clean handoff for RH‑ENVELOPE: a single lemma statement + proof that removes all hidden δ‑dependence from \(L(m)\) and \(C_h''\).

---

# MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* **Callsign:** RH-ABSORB

* **Result classification:** **CONDITIONAL**

* **Target gaps closed (by ID):**
  - **G‑5 (completion-level):** closed **after** adding the κ‑policy compatibility lemma/remark below (no new analytic estimates required).

* **Target gaps still open (by ID):**
  - **G‑4:** still conditional on a proof‑grade, δ‑uniform residual envelope lemma producing δ‑uniform \(C_1,C_2\) (and hence δ‑uniform \(C_h''\), \(L(m)\)).

* **Key conclusions (5 bullets max):**
  1. v33’s η‑absorption closure is structurally correct: once \(A,B,D\) are finite and η‑independent, Proposition `\ref{prop:eta-absorption}` forces the anchor inequality and Theorem `\ref{thm:tail-closure}` propagates it.
  2. v33 now has an explicit unconditional local term: \(N_{\rm loc}(m)\le 1.01\log m+17\) (Lemma `\ref{lem:Nloc-logm}`), so the only remaining δ‑uniformity risk is the residual envelope ledger.
  3. κ‑admissible shrinking is non‑circular (Lemma `\ref{lem:collar-existence}`) and monotone‑safe for the tail inequality (Lemma `\ref{lem:delta-shrink-monotone}`).
  4. To be proof‑grade, κ‑shrinking must be shown compatible with forcing alignment and envelope hypotheses; this is solved by one short compatibility lemma/remark (below).
  5. The sole decisive missing analytic input for full G‑4 closure is a δ‑robust residual envelope lemma valid for all \(0<\delta\le\delta_0\) with absolute constants.

* **Paste-ready manuscript edits:**
  (i) revised lemma/proposition statements  
  (ii) revised definitions/remarks  
  (iii) revised theorem/inequality lines  

  **(i) Revise Lemma `\ref{lem:residual-envelope}` (δ‑robust form needed for absorption + κ‑policy):**
  ```tex
  \begin{lemma}[Residual envelope inequality (δ-uniform form)]
  \label{lem:residual-envelope}
  There exist absolute constants $C_1,C_2>0$ such that for all $m\ge 10$, all $\alpha\in(0,1]$, and all
  scales $0<\delta\le \delta_0(m,\alpha):=\eta\alpha/(\log m)^2$ (with any $\eta\in(0,1]$), one has
  \[
    \sup_{v\in\partial B(\alpha,m,\delta)} \left|\frac{F'(v)}{F(v)}\right|
    \le C_1\log m + C_2.
  \]
  In particular the bound holds at every $\kappa$--admissible choice $0<\delta\le\delta_0$.
  \end{lemma}
  ```
  *(If the proof prefers to remove $\eta$ entirely, it is enough to quantify $0<\delta\le \alpha/(\log m)^2$, since $\eta\le 1$.)*

  **(ii) Add a κ‑policy compatibility lemma immediately after Lemma `\ref{lem:delta-shrink-monotone}` (or after Definition `\ref{def:collar-admissible}`):**
  ```tex
  \begin{lemma}[$\kappa$--policy compatibility across forcing, UE, and tail reduction]
  \label{lem:kappa-policy-compat}
  Fix $m\ge 10$, $\alpha\in(0,1]$, $\eta\in(0,1)$ and let $\delta_0=\eta\alpha/(\log m)^2$.
  Choose any $0<\delta\le\delta_0$ such that $B(\pm\alpha,m,\delta)$ are $\kappa$--admissible.
  Then:
  (i) $\kappa$--admissibility implies $E\neq 0$ on $\partial B$, so boundary-contact holds and the
  Dirichlet outer factor and Lemma~\ref{lem:upper-envelope} apply;
  (ii) the local window definition $N_{\rm loc}(m)$ is independent of $\delta$, and Lemma~\ref{lem:Zloc-logder-collar}
  applies with the same $N_{\rm loc}(m)$;
  (iii) in the quartet contradiction one may take $\alpha=a$, hence $|\alpha-a|=0\le\delta$, so
  Lemma~\ref{lem:short-side-forcing} is not weakened by shrinking $\delta$;
  (iv) assuming Lemma~\ref{lem:residual-envelope} in δ-uniform form, the residual envelope and horizontal-budget bounds
  remain valid at the chosen $\delta$;
  (v) if the tail inequality holds at the nominal scale $\delta_0$, then it holds at the chosen $\delta$
  by Lemma~\ref{lem:delta-shrink-monotone}, so worst-case reductions (Lemma~\ref{lem:worst-alpha}, Lemma~\ref{lem:monotone-m})
  remain sound.
  \end{lemma}
  ```

  **(iii) Tighten one sentence in §`\ref{sec:eta-absorption}` (to make δ‑uniformity explicit):**
  ```tex
  Since $C_{\rm up},C_1,C_2,C_h''$ are absolute (δ-uniform) constants and $N_{\rm up}(10)=1.01\log 10+17$,
  the coefficients $A,B,D$ are finite and independent of $\eta$.
  ```

* **Dependencies on other branches:**
  - **RH-ENVELOPE:** prove Lemma `\ref{lem:residual-envelope}` in the revised δ‑uniform form (this is the decisive G‑4 input).
  - *(Optional analytic citation support)* If a referee demands it: cite a standard source for boundedness of the boundary conjugation operator on \(\partial Q\) and boundedness of the Poisson kernel at the center of a Lipschitz polygon, to justify finiteness of \(C_{\rm up}\).

* **Referee risk notes (anticipated objections + how addressed):**
  1. **Objection:** “You shrink δ; your residual envelope bound was only stated at δ=δ0.”  
     **Answer:** revise Lemma `\ref{lem:residual-envelope}` to quantify all \(0<\delta\le\delta_0\) with absolute constants; then δ‑shrinking preserves hypotheses and improves inequalities.
  2. **Objection:** “Shrinking δ could break the forcing hypothesis \(|\alpha-a|\le\delta\).”  
     **Answer:** the contradiction aligns the dial by taking \(\alpha=a\), so \(|\alpha-a|=0\) and the forcing lemma is unaffected (Lemma `\ref{lem:kappa-policy-compat}`).
  3. **Objection:** “Your local term hides a \(1/\delta\) blowup.”  
     **Answer:** v33 exposes it explicitly and shows it is neutralized by UE’s \(\delta^{3/2}\), leaving net \(\delta^{1/2}\) (Corollary `\ref{cor:UE-residual-local}` + Eq. (TAIL)).
  4. **Objection:** “Absorption is a ‘miracle inequality’ if constants depend on δ.”  
     **Answer:** the audit ledger isolates the only sensitive point: \(C_1,C_2\) (and hence \(C_h''\)). Once they are δ‑uniform, absorption is a standard small‑η dominance argument (Proposition `\ref{prop:eta-absorption}`).
