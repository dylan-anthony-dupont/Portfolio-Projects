# batch2_RH-ENVELOPE.md

## Scope and targets (Batch 2)

**Base:** `manuscript_v33.tex` (locked).  
**Callsign:** RH-ENVELOPE.  
**Primary targets:**  
- **Task A (CRITICAL):** close **G-1 / G-12** (Residual envelope lemma proof + constant provenance; δ/η independence).  
- **Task B (HIGH):** close **G-2 (scaling audit)** (explicit δ-exponent ledger across UE → split → collar → tail).  
- **Task C (interface hardening):** tighten “no residual proxying” enforcement.

This patch note is surgical: it only touches the constant-ledger gate and the δ-exponent chain that feeds W-control / tail inequality.

---

## A. Task A — Identify the v33 residual-envelope lemma and replace it with a proof-grade δ-uniform version (G-1/G-12)

### A.1 Locate the lemma in v33

In `manuscript_v33.tex`, the residual envelope bound is currently:

- **Section:** “Constant ledger for the residual term”  
- **Lemma label:** `\label{lem:residual-envelope}`  
- **Current role:** provides **δ-independent** constants `(C_1,C_2)` for  
  \[
    \sup_{v\in\partial B}\left|\frac{F'(v)}{F(v)}\right| \le C_1\log m + C_2,
  \]
  used downstream in **Corollary `\ref{cor:UE-residual-local}`** and then in **Theorem `\ref{thm:tail-inequality}`**.

The current lemma is explicitly marked in v33 as a “hard gate” and has no proof.

### A.2 Patch objective

Replace `Lemma \ref{lem:residual-envelope}` with a proof-grade statement that:

1. **States all hypotheses** explicitly (analyticity domain; parameter ranges; what depends on what).  
2. Makes **δ-uniformity** explicit (constants do *not* depend on δ, η, κ, or the zero configuration).  
3. Makes **constant provenance** explicit: what is proved inside the paper vs what is imported (unconditional analytic number theory input), and why it is not RH-equivalent.

### A.3 Paste-ready replacement: lemma statement + proof skeleton + provenance remark

**Patch location:** replace the entire existing lemma environment for `Lemma \ref{lem:residual-envelope}` (and its preceding “Hard gate” remark) with the block below.

```tex
% --- REPLACE the existing “Hard gate” remark + Lemma \ref{lem:residual-envelope} with:

\begin{remark}[Constant gate for the residual term (what is and is not assumed)]
\label{rem:residual-constant-gate}
The tail inequality uses a bound of the form
\[
\sup_{v\in\partial B(\alpha,m,\delta)}\Bigl|\frac{F'(v)}{F(v)}\Bigr|
\ \le\ C_1\log m + C_2,
\]
with constants that must be:
(i) **unconditional** (not RH-equivalent), and
(ii) **uniform in** $(\alpha,\delta,\eta,\kappa)$ once $m\ge10$ and $0<\alpha\le1$.
The proof below reduces this to standard, unconditional bounds for
$\zeta'/\zeta$ in the critical strip with local-zero subtraction, plus a Stirling-type bound for $\Gamma'/\Gamma$.
\end{remark}

\begin{lemma}[Residual envelope inequality (\texorpdfstring{$\delta$}{delta}-uniform)]
\label{lem:residual-envelope}
Fix $m\ge 10$ and $\alpha\in(0,1]$.
Let $\eta\in(0,1]$ and set the nominal width $\delta_0:=\eta\alpha/(\log m)^2$.
Let $\delta\in(0,\delta_0]$ and let $B:=B(\alpha,m,\delta)$.

Define $E(v)=\Lambda_2(1+v)$, $Z_{\rm loc}$ and $F:=E/Z_{\rm loc}$ as in \S\ref{sec:residual-ledger}.
Assume **boundary-contact** on $\partial B$ (equivalently: $E$ has no zeros on $\partial B$; hence $F$ is holomorphic and zero-free on a neighborhood of $\partial B$).

Then there exist absolute constants $C_1,C_2>0$ (independent of $m,\alpha,\delta,\eta,\kappa$ and of the zero configuration) such that
\[
\sup_{v\in\partial B}\Bigl|\frac{F'(v)}{F(v)}\Bigr|
\ \le\ C_1\log m + C_2.
\]
\end{lemma}

\begin{proof}[Proof sketch with explicit dependency control]
Write $u:=1+v$ and $s:=u/2=(1+v)/2$.
For $v\in\partial B(\alpha,m,\delta)$ we have
\[
\Re(s)\in\Bigl[\tfrac{1-(\alpha+\delta)}{2},\tfrac{1+(\alpha+\delta)}{2}\Bigr]\subset[0,1],
\qquad
\Im(s)=\tfrac{\Im(v)}{2}\in\Bigl[\tfrac m2-\tfrac\delta2,\tfrac m2+\tfrac\delta2\Bigr].
\]
Since $m\ge10$ and $\delta\le\delta_0\le 1/(\log 10)^2<1/5$, we have $\Im(s)\asymp m$ uniformly in $\delta$.

1) **Log-derivative identity in the $s$-frame.**
From $\Lambda_2(u)=\pi^{-u/4}\Gamma(u/4)\zeta(u/2)$ we obtain for $u=1+v$:
\[
\frac{E'(v)}{E(v)}
= -\frac14\log\pi + \frac14\frac{\Gamma'}{\Gamma}\Bigl(\frac{1+v}{4}\Bigr)
+ \frac12\frac{\zeta'}{\zeta}(s).
\]
Moreover, the local factor satisfies
\[
\frac{Z_{\rm loc}'(v)}{Z_{\rm loc}(v)}
=\sum_{\rho\in\mathcal Z(m)}\frac{m_\rho}{v-\rho}
=\frac12\sum_{|\gamma-\Im(s_0)|\le 1/2}\frac{1}{s-\rho_s}
\quad\text{with}\quad s_0:=\frac m2,
\]
using $v=2s-1$ and $\Im(\rho)=2\gamma$ for nontrivial zeros.

Thus
\[
\frac{F'(v)}{F(v)}
=\frac{E'(v)}{E(v)}-\frac{Z_{\rm loc}'(v)}{Z_{\rm loc}(v)}
= -\frac14\log\pi + \frac14\frac{\Gamma'}{\Gamma}\Bigl(\frac{1+v}{4}\Bigr)
+\frac12\Biggl(\frac{\zeta'}{\zeta}(s) - \sum_{|\gamma-s_0|\le 1/2}\frac{1}{s-\rho}\Biggr).
\]

2) **Unconditional residual bound for $\zeta'/\zeta$ with local-zero subtraction.**
Use the standard (unconditional) “local-zero decomposition” in the critical strip:
there exist absolute $A_\zeta,B_\zeta$ such that for $0\le\sigma\le1$ and $t\ge 5$,
\[
\Bigl|\frac{\zeta'}{\zeta}(\sigma+it) - \sum_{|\gamma-t|\le 1}\frac{1}{(\sigma+it)-\rho}\Bigr|
\ \le\ A_\zeta\log(t+2) + B_\zeta.
\tag{$\star$}
\]
(Reference: any standard RH-free treatment of the logarithmic derivative + explicit formula; if the paper prefers a self-contained route, ($\star$) can be proved from the Hadamard product for $\xi(s)$ plus a Riemann–von Mangoldt bound for $N(T)$.)

Now compare the window $|\gamma-t|\le1$ in ($\star$) with the manuscript’s window $|\gamma-s_0|\le1/2$.
For $v\in\partial B$ we have $|t-s_0|\le\delta/2<1/10$, hence any zero counted in $|\gamma-s_0|\le1/2$ is also counted in $|\gamma-t|\le1$.
Therefore
\[
\frac{\zeta'}{\zeta}(s)-\sum_{|\gamma-s_0|\le1/2}\frac{1}{s-\rho}
=
\underbrace{\Bigl(\frac{\zeta'}{\zeta}(s)-\sum_{|\gamma-t|\le1}\frac{1}{s-\rho}\Bigr)}_{\text{bounded by }A_\zeta\log(t+2)+B_\zeta}
\ +\ 
\sum_{\substack{|\gamma-t|\le1\\|\gamma-s_0|>1/2}}\frac{1}{s-\rho}.
\]
In the remaining sum we have $|\gamma-t|\ge 1/2-|t-s_0|\ge 2/5$, hence $|s-\rho|\ge 2/5$ and each term has modulus $\le 5/2$.
The number of zeros with $|\gamma-t|\le1$ is bounded by the manuscript’s explicit local count bound (Lemma \ref{lem:Nloc-bound}) evaluated at height $\asymp m$.
Hence this “difference-of-windows” sum is $\ll \log m$ with an absolute implied constant.

Combining these bounds yields absolute constants $A_{\rm res},B_{\rm res}$ such that
\[
\Bigl|\frac{\zeta'}{\zeta}(s)-\sum_{|\gamma-s_0|\le1/2}\frac{1}{s-\rho}\Bigr|
\ \le\ A_{\rm res}\log m + B_{\rm res},
\]
uniformly for all $v\in\partial B$ and all $\delta\in(0,\delta_0]$.

3) **Gamma factor bound (Stirling, uniform in $\delta$).**
For $z=(1+v)/4$ we have $\Re(z)\in[1/4,3/4]$ and $|\Im(z)|\asymp m$.
A uniform Stirling-type bound gives
\[
\Bigl|\frac{\Gamma'}{\Gamma}(z)\Bigr| \le \log(|\Im(z)|+2) + C_\Gamma
\ \le\ \log(m+2)+C_\Gamma,
\]
with an absolute constant $C_\Gamma$.

4) **Conclusion.**
Insert the bounds from (2)–(3) into the identity in (1), and absorb harmless constants into $(C_1,C_2)$.
All constants are independent of $(\alpha,\delta,\eta,\kappa)$ because:
(i) $\sigma$ ranges over a fixed compact interval $[0,1]$,
(ii) $t\asymp m$ with $m\ge10$ uniformly for $\delta\le\delta_0$, and
(iii) the local-zero difference sum is controlled by Lemma \ref{lem:Nloc-bound}, which is itself unconditional.
\end{proof}
```

#### Notes on what this patch **does** and **does not** claim

- It closes **G-1/G-12** in the sense required by the control room: the residual envelope constants are **not allowed to carry δ/η dependence**, and this patch enforces that explicitly.  
- The only imported analytic-number-theory input is the **RH-free local-zero decomposition** `($\star$)`. If the project requires complete self-containment, `($\star$)` should be promoted into its own lemma with a short proof from the Hadamard product for `\xi(s)` and the Riemann–von Mangoldt bound already used elsewhere in v33.

---

## B. Task B — δ-exponent ledger and scaling audit (G-2)

### B.1 Exponent ledger (as v33 is currently written)

This is the **intended** δ-power flow in v33:

1. **Upper-envelope (UE) lemma**:  
   \[
   \sum_{\pm}|W(v_\pm)-e^{i\varphi_0^\pm}|
   \le 2C_{\rm up}\,\delta^{3/2}\,\sup_{\partial B}|E'/E|.
   \]
2. **Split:** \(E'/E = F'/F + Z_{\rm loc}'/Z_{\rm loc}\).  
3. **Collar bound:** \(\sup_{\partial B}|Z_{\rm loc}'/Z_{\rm loc}| \le N_{\rm loc}(m)/(\kappa\delta)\).  
4. **Residual ledger:** \(\sup_{\partial B}|F'/F| \le L(m)=C_1\log m + C_2\).  
5. **Combine:**  
   \[
   \sup_{\partial B}|E'/E|\le L(m)+\frac{N_{\rm loc}(m)}{\kappa\delta}.
   \]
   Plug into UE gives  
   \[
   \text{dial dev}
   \le 2C_{\rm up}\Bigl(\delta^{3/2}L(m) + \delta^{1/2}\frac{N_{\rm loc}(m)}{\kappa}\Bigr).
   \]
6. This exact structure feeds the **tail inequality** and then **η-absorption**, relying crucially on the **positive** δ-power on the local term (here: δ^{1/2}).

### B.2 Scaling check inside the v33 UE proof (critical arithmetic mismatch)

In v33, the proof of **Lemma `\ref{lem:upper-envelope}`** explicitly enumerates the scale factors:

- Step 1: harmonic-measure evaluation from boundary contributes **\(\delta^{-1/2}\)**.  
- Step 2: periodic Poincaré contributes **\(\delta\)**.  
- Step 4: L2-to-sup contributes **\(\delta^{1/2}\)** (via \(\|\partial B\|^{1/2}\sim\delta^{1/2}\)).

Multiplying these yields the net power:
\[
\delta^{-1/2}\cdot\delta\cdot\delta^{1/2} = \delta^{1}.
\]

**Therefore the UE proof, as currently written, supports a δ¹ bound, not δ^{3/2}.**

This is not a cosmetic mismatch: if the true UE scaling is δ¹, then after the split+collar step the local term becomes δ⁰ (no shrink with η), and the η-absorption closure (and likely the whole S1 tail-cert spine) collapses.

### B.3 Minimal consistency patch (makes the manuscript internally consistent)

If the project chooses internal consistency over preserving the existing η-absorption form, the smallest patch is:

- Replace every occurrence of `\delta^{3/2}` produced *solely* by UE scaling with `\delta`.  
- Update downstream corollaries/theorems that directly substitute UE.

**Paste-ready edits (UE + immediate corollary):**

```tex
% --- In Lemma \ref{lem:upper-envelope} statement, replace δ^{3/2} -> δ:

\begin{lemma}[Upper envelope bound on dial deviation]
...
\begin{equation}
\label{eq:UE-EoverE}
\sum_{\pm}\bigl|W(v_\pm)-e^{i\varphi_0^\pm}\bigr|
\ \le\ 2\,C_{\rm up}\,\delta\,\sup_{v\in\partial B}\Bigl|\frac{E'(v)}{E(v)}\Bigr|.
\end{equation}
\end{lemma}
```

```tex
% --- In Corollary \ref{cor:UE-residual-local}, propagate the δ change:

\begin{corollary}[UE bound in terms of residual + local factors]
\label{cor:UE-residual-local}
Assume the aligned box $B=B(\pm a,m,\delta)$ is $\kappa$--admissible and boundary-contact.
Then
\[
\sum_{\pm}\bigl|W(v_\pm)-e^{i\varphi_0^\pm}\bigr|
\ \le\
2\,C_{\rm up}\,\delta\,\Bigl(L(m)+\frac{N_{\rm loc}(m)}{\kappa\,\delta}\Bigr)
\ =\
2\,C_{\rm up}\,\Bigl(\delta\,L(m)+\frac{N_{\rm loc}(m)}{\kappa}\Bigr).
\]
Replacing $N_{\rm loc}(m)$ by the explicit upper bound $N_{\rm up}(m)$ gives the same inequality with $N_{\rm up}(m)$.
\end{corollary}
```

### B.4 Consequence flag (cannot be ignored)

With the above correction, the **local term becomes δ⁰**:
\[
2C_{\rm up}\,\frac{N_{\rm up}(m)}{\kappa},
\]
which does **not** shrink as η→0 (or δ→0).

This means:

- The current **tail inequality** and **η-absorption** statements in v33 are no longer viable as written.  
- Either:
  1) a stronger UE inequality (restoring a δ^{p} with p>1) must be proved by a *different* argument than the present boundary-L2 chain, **or**
  2) the local factor/window technology must be redesigned so that the collar contribution carries an additional small parameter.

This is a **structural** issue for the S1 spine, not just bookkeeping.

I am not proposing a full redesign here (out of scope); I am flagging the forced implication of the exponent audit.

---

## C. Task C — Interface hardening: strengthen “no residual proxying”

v33 already includes `Remark \ref{rem:no-proxying}`. I recommend one tightening line to make the prohibition referee-proof:

```tex
% --- Append to Remark \ref{rem:no-proxying}:

In particular, statements of the form
\[
\sup_{\partial B}\Bigl|\frac{E'}{E}\Bigr| \ \le\ \sup_{\partial B}\Bigl|\frac{F'}{F}\Bigr|
\]
(or any implicit variant) are **invalid** unless one proves $Z_{\rm loc}\equiv 1$ on the relevant domain.
All uses of $\sup|E'/E|$ must be routed through Lemma \ref{lem:logder-split} plus the collar bound Lemma \ref{lem:collar-zloc}.
```

This ensures there is no pathway back to the pre-v32 “residual-only proxy” failure mode.

---

## MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* Callsign: RH-ENVELOPE
* Result classification: **CONDITIONAL**
* Target gaps closed (by ID):
  - **G-1** (Residual envelope bound is now δ-uniform and proof-graded, contingent only on an explicit RH-free local-zero decomposition lemma `($\star$)` being accepted/cited or proved in-paper.)
  - **G-12** (Constant provenance ledger: δ/η/κ independence is made explicit; imported inputs are labeled.)
* Target gaps still open (by ID):
  - **G-2 (scaling audit)** is *resolved as an arithmetic mismatch* but exposes a structural consequence: if UE scaling is truly δ¹, the S1 η-absorption/tail spine collapses. Restoring p>1 (e.g., δ^{3/2}) requires a new argument or a redesigned local window mechanism.
  - Any downstream absorption items impacted by the exponent change (interfaces with the control room; likely touches the global S1 decision).
* Key conclusions (5 bullets max):
  1. v33’s residual envelope lemma can be made proof-grade and δ-uniform without RH-equivalent assumptions (patch supplied).
  2. The current UE proof in v33 multiplies to **δ¹**, not δ^{3/2}; the δ^{3/2} in the statement is unsupported by the written proof.
  3. If UE is δ¹, the collar/local term becomes **δ⁰**, so η-absorption cannot shrink it; the tail-cert S1 closure as written cannot go through.
  4. “No residual proxying” is already present but should be strengthened with an explicit forbidden inequality line (patch supplied).
  5. Net: constant-ledger gate can be closed; exponent audit forces a global decision on whether S1 is salvageable (requires new UE mechanism).
* Paste-ready manuscript edits:
  (i) revised lemma/proposition statements
  - Replace `Lemma \ref{lem:residual-envelope}` + preceding remark with the block in **A.3**.
  - Replace UE exponent in `Lemma \ref{lem:upper-envelope}` statement: `\delta^{3/2} -> \delta` (see **B.3**).
  - Propagate UE change into `Corollary \ref{cor:UE-residual-local}` (see **B.3**).
  (ii) revised definitions/remarks
  - Replace “Hard gate” remark with `Remark \ref{rem:residual-constant-gate}` (see **A.3**).
  - Append the strengthening line to `Remark \ref{rem:no-proxying}` (see **C**).
  (iii) revised theorem/inequality lines
  - If the UE exponent patch is accepted, **every downstream inequality using UE’s δ^{3/2} must be recomputed** (tail inequality, monotonicity lemmas, η-absorption). This is not a cosmetic change; it is a structural consequence of the exponent audit.
* Dependencies on other branches:
  - Control Room / S1 spine decision: whether to (a) find a new UE proof yielding p>1, or (b) redesign the local-window mechanism so the collar term carries a small parameter even if UE is δ¹.
  - If a self-contained proof is required for the local-zero decomposition `($\star$)`, this needs either (i) an appendix proof from the Hadamard product for `\xi(s)` + the existing `N(T)` machinery, or (ii) an approved external reference with explicit constants.
* Referee risk notes (anticipated objections + how addressed):
  - **Objection:** “Λ₂ is not entire.”  
    **Response:** The patched lemma only uses analyticity on a neighborhood of the high-m box (true for m≥10). If desired, the manuscript should rephrase “Λ₂ is entire” to “meromorphic with poles at u∈{0,2}, hence holomorphic in the critical-strip boxes used here.”
  - **Objection:** “Residual envelope imports an unproven bound `($\star$)`.”  
    **Response:** The patch explicitly labels `($\star$)` as the only imported analytic-number-theory input and offers a self-contained route (Hadamard product + N(T)). This eliminates hidden assumptions.
  - **Objection:** “Changing UE exponent breaks the whole tail closure.”  
    **Response:** Correct; that is the forced outcome of the scaling audit. The patch does not pretend otherwise. The program must either prove a stronger UE inequality or redesign the local term so it shrinks.
