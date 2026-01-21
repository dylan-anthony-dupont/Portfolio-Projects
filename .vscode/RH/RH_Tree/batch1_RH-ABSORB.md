## 1) v32 target interface for RH-ABSORB

Your δ‑uniformity / κ‑policy obligations live exactly at the **v32 tail interface**:

- **Tail inequality (v32 Theorem 11.1 / Eq. (18))** fixes  
  \[
  \delta=\delta(m,\alpha)=\frac{\eta\alpha}{(\log m)^2},\qquad \kappa\in(0,1/10),
  \]
  and asserts “absence of off-axis quartets at height \(m\)” follows from the strict inequality  
  \[
  2C_{\rm up}\Big(\delta^{3/2}L(m)+\delta^{1/2}\frac{N_{\rm up}(m)}{\kappa}\Big)
  \;<\;
  c-\delta\Big(K_{\rm alloc}\,c_0\,L(m)+C''_h(\log m+1)\Big). \tag{18}
  \]  
  This is the exact inequality whose **η‑absorption** is used to close the tail. 【390:1†manuscript_v32.pdf†L38-L81】【390:3†manuscript_v32.pdf†L21-L35】

- **η‑absorption rewrite (v32 §12)** at \((m,\alpha)=(10,1)\) is explicitly  
  \[
  A\eta^{3/2}+B\eta^{1/2}<c-D\eta
  \]
  with coefficients  
  \[
  A=\frac{2C_{\rm up}L(10)}{(\log 10)^3},\quad
  B=\frac{2C_{\rm up}N_{\rm up}(10)}{\kappa\log 10},\quad
  D=\frac{K_{\rm alloc}c_0L(10)+C''_h(\log 10+1)}{(\log 10)^2},
  \]
  and Proposition 12.1 gives an explicit sufficient \(\eta_\star\). 【390:10†manuscript_v32.pdf†L4-L42】

So **G‑4/G‑5** reduce to: do all quantities entering \(A,B,D\) stay **δ‑uniform** (independent of η), and is the **collar shrinking** (Definition 10.3) both non‑circular and monotone‑safe?

---

## 2) δ‑uniformity ledger (G‑4) — every δ‑sensitive term classified

Below, “δ‑uniform” means: *independent of* \(\delta\) (equivalently independent of η), except through the explicit δ‑powers shown in Eq. (18).

### 2.1 Explicit δ‑power terms in Eq. (18)

1) **\(\delta^{3/2}L(m)\)** (in LHS)  
- **Where:** Eq. (18) LHS. 【390:1†manuscript_v32.pdf†L69-L81】  
- **δ‑status:** **δ‑helpful** (vanishes as \(\delta\to 0\)).  
- **Risk note:** only becomes problematic if \(L(m)\) secretly blows up faster than \(\delta^{-3/2}\). In v32, \(L(m)=C_1\log m+C_2\) is asserted independent of δ. 【390:1†manuscript_v32.pdf†L39-L41】【390:3†manuscript_v32.pdf†L37-L53】

2) **\(\delta^{1/2}\,N_{\rm up}(m)/\kappa\)** (in LHS)  
- **Where:** Eq. (18) LHS. 【390:1†manuscript_v32.pdf†L69-L81】  
- **Origin (important):** comes from the collar/log‑derivative split  
  \[
  \sup_{\partial B}\Big|\frac{E'}{E}\Big|\le L(m)+\frac{N_{\rm loc}(m)}{\kappa\delta}\le L(m)+\frac{N_{\rm up}(m)}{\kappa\delta},
  \]
  then multiplied by the UE prefactor \(\delta^{3/2}\), giving \(\delta^{1/2}N_{\rm up}(m)/\kappa\). 【390:3†manuscript_v32.pdf†L39-L53】  
- **δ‑status:** **δ‑helpful** in its *final* form; internally it hides a **δ‑harmful** \(1/\delta\) that is safely offset by UE’s \(\delta^{3/2}\).

3) **\(-\delta(\cdots)\)** on RHS  
- **Where:** Eq. (18) RHS. 【390:1†manuscript_v32.pdf†L75-L81】  
- **δ‑status:** **δ‑helpful** in the global contradiction sense: shrinking δ *increases* RHS because it subtracts less.

### 2.2 Constants and functions that must be δ‑uniform for absorption to be legitimate

4) **\(C_{\rm up}\)** (upper envelope “shape-only” constant)  
- **Where:** appears in Eq. (18) LHS; UE lemma is used in the assembly. 【390:1†manuscript_v32.pdf†L69-L81】【390:3†manuscript_v32.pdf†L36-L55】  
- **δ‑status:** **δ‑uniform** *provided* “shape-only invariance” is correctly formalized: \(C_{\rm up}\) depends only on the normalized square boundary/operator norms, not on \((\alpha,m,\delta)\). (This is consistent with the post-pivot architecture and the way Eq. (18) is written.) 【390:1†manuscript_v32.pdf†L61-L66】

5) **\(\kappa\)** (collar parameter)  
- **Where:** fixed in tail section and used in collar bound / local term. 【390:1†manuscript_v32.pdf†L41-L48】  
- **δ‑status:** **δ‑uniform** by definition.

6) **\(N_{\rm up}(m)=A_N\log m+B_N\)**  
- **Where:** defined at start of tail section; used in Eq. (18) and §12 coefficients. 【390:1†manuscript_v32.pdf†L39-L41】【390:10†manuscript_v32.pdf†L8-L19】  
- **δ‑status:** **δ‑uniform**, assuming the “local window bound” producing \(A_N,B_N\) is truly δ‑independent (as stated in Theorem 11.1 assumptions). 【390:1†manuscript_v32.pdf†L66-L67】

7) **\(L(m)=C_1\log m+C_2\)** (residual envelope surrogate)  
- **Where:** defined in tail section, assumed from Lemma 7.1, used everywhere: Eq. (18), §12. 【390:1†manuscript_v32.pdf†L39-L41】【390:1†manuscript_v32.pdf†L60-L61】【390:10†manuscript_v32.pdf†L8-L19】  
- **δ‑status:** **δ‑uniform is REQUIRED**.  
- **Referee reality:** this is the single biggest δ‑uniformity obligation: v32 explicitly relies on Lemma 7.1 providing \(\sup_{\partial B}|F'/F|\le C_1\log m+C_2\) *uniformly in \(\delta\) and \(\alpha\)* (and both signs). This is listed as a **critical remaining obligation** in the audit status memo. 【390:0†v32_status_decision_v2.md†L13-L16】

8) **\(C''_h:=4\max\{C_1,C_2\}\)** (horizontal budget constant)  
- **Where:** Lemma 10.9 defines and uses it; Theorem 11.1 assumes it is independent of \((\alpha,m,\delta)\). 【390:1†manuscript_v32.pdf†L1-L37】【390:1†manuscript_v32.pdf†L61-L66】  
- **δ‑status:** **δ‑uniform iff \(C_1,C_2\) are δ‑uniform**.  
- **δ‑risk mode:** if \(\sup_{\partial B}|F'/F|\) had hidden \(1/\delta\)-type growth, then the HB term \(4\delta\,\sup|F'/F|\) could stop being small as \(\delta\to 0\). Lemma 10.9’s *structure* is δ‑helpful, but it inherits δ‑uniformity from the residual envelope input.

9) **Forcing-side constants \(c_0,c,K_{\rm alloc}\)**  
- **Where:** Theorem 11.1 assumes they come from “the forcing lemma” (and bookkeeping). 【390:1†manuscript_v32.pdf†L48-L60】  
- **δ‑status:** intended **δ‑uniform** (absolute constants).  
- **Scope note:** per your branch boundary, I treat \(K_{\rm alloc}\) symbolically (provenance belongs to RH‑FORCE), but δ‑dependence is not expected: it is a fixed allocation coefficient.

### 2.3 δ‑classification summary (what matters for η‑absorption)

- **δ‑uniform (must stay independent of δ):** \(C_{\rm up}\), \(\kappa\), \(A_N,B_N\), \(c_0,c,K_{\rm alloc}\), \(C_1,C_2\) (critical), hence \(C''_h\). 【390:1†manuscript_v32.pdf†L48-L67】【390:10†manuscript_v32.pdf†L8-L21】  
- **δ‑helpful:** every explicit δ‑power in Eq. (18): \(\delta^{3/2}\), \(\delta^{1/2}\), \(\delta\). 【390:1†manuscript_v32.pdf†L69-L81】  
- **δ‑harmful but neutralized:** the collar/log‑derivative local term contributes \(1/(\kappa\delta)\) inside \(\sup|E'/E|\), but UE multiplies by \(\delta^{3/2}\), leaving net \(\delta^{1/2}\). 【390:3†manuscript_v32.pdf†L39-L53】  
- **δ‑fatal scenarios (must be excluded explicitly):** any hidden dependence in the residual envelope or HB of the form  
  \(\sup|F'/F|\gtrsim \delta^{-p}\) with \(p\ge 1\) (because HB has a prefactor \(\delta\), so \(p=1\) gives an \(O(1)\) term and \(p>1\) blows up).  
  v32’s intent is to prevent this by making \(F\) residual/zero‑free on a neighborhood and proving a strip‑type bound independent of δ (Lemma 7.1 obligation). 【390:1†manuscript_v32.pdf†L24-L37】【390:0†v32_status_decision_v2.md†L13-L16】

---

## 3) κ‑admissibility / shrink‑δ policy safety (G‑5)

### 3.1 What v32 currently asserts (and what must be proven)

- **Definition 10.3 (collar‑admissible)** defines κ‑admissibility by  
  \[
  \dist(\partial B, Z(E))\ge \kappa\delta,
  \]
  and then states: if not κ‑admissible, **replace \(\delta\) by a smaller value until κ‑admissible**, and that *all bounds become easier as δ decreases*. 【378:2†manuscript_v32.pdf†L4-L13】  
- The “becomes easier” claim is exactly what must be formalized to remove any “miracle inequality” risk.

### 3.2 Lemma package needed (minimal, referee‑grade)

#### Lemma (Existence of a κ‑admissible shrink; non‑circular contour choice)

**Statement (paste‑ready logic):**  
Fix a box center \(v_0\in\mathbb{C}\), an initial \(\delta_0>0\), and \(\kappa\in(0,1)\).  
Assume \(E\) is analytic on a neighborhood of \(\overline{B(v_0,\delta_0)}\). Then there exists \(\delta'\in(0,\delta_0]\) such that  
\[
\dist(\partial B(v_0,\delta'), Z(E))\ge \kappa\delta'.
\]

**Proof skeleton (non‑circular):**  
Zeros of a nonzero analytic function are isolated. Hence there exists \(\varepsilon>0\) such that the punctured neighborhood  
\(\{v:0<\|v-v_0\|_\infty\le \varepsilon\}\) contains **no zeros of \(E\)** (except possibly \(v_0\) itself).  
Take \(\delta'=\min\{\delta_0,\varepsilon/(1+\kappa)\}\). Then for any \(v\in\partial B(v_0,\delta')\) and any zero \(\rho\neq v_0\),  
\[
\|v-\rho\|_\infty\ge \|\rho-v_0\|_\infty-\|v-v_0\|_\infty \ge \varepsilon-\delta'\ge \kappa\delta',
\]
and if \(v_0\in Z(E)\) then \(\dist(\partial B(v_0,\delta'),\{v_0\})=\delta'\ge \kappa\delta'\).  
This uses only “zeros are isolated,” not their locations.

This resolves the circularity concern: δ is not “chosen by knowing zeros,” it is chosen by the existence of a zero‑free collar, which is guaranteed abstractly.

#### Lemma (Monotonicity under δ‑shrinking for the assembled tail inequality)

From Eq. (18), define (for fixed \(m,\alpha\) and fixed constants)
\[
\mathrm{LHS}(\delta)=2C_{\rm up}\Big(\delta^{3/2}L(m)+\delta^{1/2}\frac{N_{\rm up}(m)}{\kappa}\Big),
\quad
\mathrm{RHS}(\delta)=c-\delta\Big(K_{\rm alloc}c_0L(m)+C''_h(\log m+1)\Big).
\]
Then:

- \(\mathrm{LHS}(\delta)\) is **increasing** in \(\delta>0\) (sum of increasing powers \(\delta^{3/2},\delta^{1/2}\));
- \(\mathrm{RHS}(\delta)\) is **decreasing** in \(\delta>0\) (affine \(c-\delta\Xi\), \(\Xi\ge 0\)).

Therefore, if Eq. (18) holds at \(\delta_0\), it automatically holds for every \(0<\delta\le \delta_0\).  
This is exactly the missing formal justification for “shrinking δ makes things easier.” 【390:1†manuscript_v32.pdf†L69-L81】【390:3†manuscript_v32.pdf†L63-L65】

#### Remark (η relabelling keeps the program syntactically consistent)

If the manuscript insists on the functional relation \(\delta=\eta\alpha/(\log m)^2\), then replacing δ by a smaller \(\delta'\) can be expressed as replacing η by a smaller  
\[
\eta'=\delta'\,\frac{(\log m)^2}{\alpha}\le \eta.
\]
This is compatible with Proposition 12.1 / Theorem 13.1 which already quantifies over **all** \(\eta\in(0,\eta_\star]\). 【390:10†manuscript_v32.pdf†L22-L42】【390:10†manuscript_v32.pdf†L44-L51】

### 3.3 Shrink‑δ monotonicity check against each tail component (explicitly)

- **Forcing:** the short‑side forcing lemma is stated as a raw \(\ge \pi/2\) bound under \(0<\delta\le 1\) and \(|\alpha-a|\le\delta\); shrinking δ preserves \(0<\delta\le1\) and does not invalidate the forcing direction. 【386:11†manuscript_v32.pdf†L8-L16】  
- **UE:** post‑pivot UE uses \(\delta^{3/2}\sup_{\partial B}|E'/E|\) and then bounds \(\sup|E'/E|\le L(m)+N_{\rm up}(m)/(\kappa\delta)\), giving net \(\delta^{3/2}L(m)+\delta^{1/2}N_{\rm up}(m)/\kappa\); shrinking δ decreases this quantity. 【390:3†manuscript_v32.pdf†L39-L53】  
- **HB:** \(\Delta_{\rm nonforce}(B)\le 4\delta \sup_{\partial B}|F'/F|\), hence decreases with δ *provided* \(\sup|F'/F|\) is δ‑uniform (this circles back to Lemma 7.1). 【390:1†manuscript_v32.pdf†L1-L37】

Conclusion: the only place where “δ‑shrinking makes things easier” could fail is if **the residual envelope bound is not δ‑uniform** (because HB involves \(\delta\,\sup|F'/F|\)).

---

## 4) Absorption feasibility verdict (PASS/FAIL/CONDITIONAL)

### What v32 already proves syntactically
If \(A,B,D<\infty\) are *constants* independent of η, then Proposition 12.1 correctly forces the anchor inequality by choosing η small enough. 【390:10†manuscript_v32.pdf†L20-L42】

### What is still logically required
To make “\(A,B,D<\infty\)” proof‑grade and δ‑uniform, the decisive requirement is:

- **Residual envelope lemma completeness and δ‑uniformity**:  
  \(\sup_{\partial B}|F'/F|\le C_1\log m+C_2\) **uniformly in \(\delta\) and \(\alpha\)** (and both signs), so that \(C''_h\) is δ‑uniform and HB remains \(O(\delta\log m)\). This is explicitly flagged as a critical remaining obligation. 【390:0†v32_status_decision_v2.md†L13-L16】

With that in hand, the κ‑policy and δ‑monotonicity can be made fully rigorous via the lemmas above, and η‑absorption is structurally sound.

---

# MANDATORY FINAL SECTION — PATCH PACKET FORMAT

- **Prompt Batch Number:** 1

- **Callsign:** RH-ABSORB

- **Result classification:** **CONDITIONAL**

- **Target gaps closed (by ID):**
  - **G‑5 (κ‑admissibility / shrink‑δ policy)** — *closed modulo paste‑ready lemmas below* (no new analytic input required beyond “zeros are isolated”).

- **Target gaps still open (by ID):**
  - **G‑4 (δ‑uniformity required for η‑absorption)** — *conditional on one decisive lemma*: a full, δ‑uniform residual envelope bound (Lemma 7.1) as described below.

- **Key conclusions (≤5 bullets):**
  1. v32’s η‑absorption is algebraically correct once \(A,B,D\) are η‑independent constants. 【390:10†manuscript_v32.pdf†L20-L42】
  2. Every explicit δ‑term in Eq. (18) is δ‑helpful; the only δ‑fragility is hidden in \(\sup|F'/F|\) (HB path) if Lemma 7.1 is not δ‑uniform. 【390:1†manuscript_v32.pdf†L1-L37】【390:0†v32_status_decision_v2.md†L13-L16】
  3. The collar term’s internal \(1/\delta\) dependence is safe because UE carries a \(\delta^{3/2}\) prefactor, yielding net \(\delta^{1/2}\). 【390:3†manuscript_v32.pdf†L39-L53】
  4. “Shrink δ until κ‑admissible” can be made non‑circular using only isolation of zeros, and the tail inequality is monotone‑safe under δ‑shrinking. 【378:2†manuscript_v32.pdf†L4-L13】【390:3†manuscript_v32.pdf†L63-L65】
  5. Therefore η‑absorption is **viable** provided Lemma 7.1 is upgraded to a full δ‑uniform theorem (single decisive blocker for G‑4). 【390:0†v32_status_decision_v2.md†L13-L16】

- **Paste-ready manuscript edits: (i) lemma statements (ii) definitions/remarks (iii) inequality lines**

  **(i) Add immediately after Definition 10.3 (collar-admissible):**
  ```tex
  \begin{lemma}[Existence of a $\kappa$--admissible shrink]\label{lem:collar-existence}
  Let $E$ be analytic on a neighborhood of $\overline{B(v_0,\delta_0)}$, and fix $\kappa\in(0,1)$.
  Then there exists $\delta'\in(0,\delta_0]$ such that
  \[
    \dist(\partial B(v_0,\delta'), Z(E)) \ge \kappa\,\delta'.
  \]
  \end{lemma}
  \begin{proof}
  Zeros of an analytic function are isolated. Hence there exists $\varepsilon>0$ such that
  $Z(E)\cap\{v:\ 0<\|v-v_0\|_\infty\le \varepsilon\}=\emptyset$.
  Set $\delta'=\min\{\delta_0,\varepsilon/(1+\kappa)\}$.
  For $v\in\partial B(v_0,\delta')$ and any $\rho\in Z(E)$ with $\rho\neq v_0$ we have
  $\|v-\rho\|_\infty\ge \|\rho-v_0\|_\infty-\|v-v_0\|_\infty\ge \varepsilon-\delta'\ge \kappa\delta'$.
  If $v_0\in Z(E)$ then $\dist(\partial B(v_0,\delta'),\{v_0\})=\delta'\ge \kappa\delta'$.
  \end{proof}
  ```

  **(ii) Add immediately after Lemma 11.1 / Eq. (18):**
  ```tex
  \begin{lemma}[Monotonicity under $\delta$--shrinking]\label{lem:delta-shrink-monotone}
  Fix $m\ge 10$, $\alpha\in(0,1]$, and constants
  $C_{\rm up}>0$, $\kappa\in(0,1)$, $c>0$, $c_0>0$, $K_{\rm alloc}\ge 0$, $C_h''\ge 0$,
  and functions $L(m)\ge 0$, $N_{\rm up}(m)\ge 0$ independent of $\delta$.
  Define for $\delta>0$
  \[
    \mathrm{LHS}(\delta)=2C_{\rm up}\Big(\delta^{3/2}L(m)+\delta^{1/2}\frac{N_{\rm up}(m)}{\kappa}\Big),
    \qquad
    \mathrm{RHS}(\delta)=c-\delta\Big(K_{\rm alloc}c_0L(m)+C_h''(\log m+1)\Big).
  \]
  Then $\mathrm{LHS}$ is increasing and $\mathrm{RHS}$ is decreasing in $\delta$.
  Consequently, if $\mathrm{LHS}(\delta_0)<\mathrm{RHS}(\delta_0)$ for some $\delta_0>0$,
  then $\mathrm{LHS}(\delta)<\mathrm{RHS}(\delta)$ for all $0<\delta\le \delta_0$.
  \end{lemma}
  \begin{proof}
  $\delta^{3/2}$ and $\delta^{1/2}$ are increasing for $\delta>0$, hence $\mathrm{LHS}$ increases.
  The factor in parentheses on $\mathrm{RHS}$ is nonnegative and independent of $\delta$, so
  $\mathrm{RHS}(\delta)=c-\delta\Xi$ decreases in $\delta$.
  \end{proof}
  ```

  **(iii) Add a clarifying remark (immediately after Lemma \ref{lem:delta-shrink-monotone}):**
  ```tex
  \begin{remark}[Collar shrinking is non-circular and compatible with $\delta=\eta\alpha/(\log m)^2]
  By Lemma \ref{lem:collar-existence} we may replace a nominal $\delta_0$ by any smaller
  $\delta'\le \delta_0$ to enforce $\kappa$--admissibility, without using any knowledge of zero locations.
  By Lemma \ref{lem:delta-shrink-monotone}, the strict tail inequality becomes easier as $\delta$ decreases.
  If we insist on the parameterization $\delta=\eta\alpha/(\log m)^2$, shrinking $\delta$ is equivalent
  to shrinking $\eta$ to $\eta'=\delta'(\log m)^2/\alpha\le \eta$.
  \end{remark}
  ```

- **Dependencies on other branches:**
  - **RH-ENVELOPE / residual control:** upgrade Lemma 7.1 to a full proof giving  
    \(\sup_{\partial B}|F'/F|\le C_1\log m+C_2\) **uniform in \(\delta\) and \(\alpha\)** (and both signs). This is the decisive dependency for G‑4. 【390:0†v32_status_decision_v2.md†L13-L16】
  - **RH-FORCE:** provenance/existence/bound for \(K_{\rm alloc}\) (treated symbolically here). 【390:1†manuscript_v32.pdf†L48-L60】
  - **RH-LOCAL:** the window-count constants \(A_N,B_N\) (treated as inputs here). 【390:1†manuscript_v32.pdf†L66-L67】

- **Referee risk notes:**
  - The collar policy is only safe if theorems/lemmas are stated for **all sufficiently small δ** (or equivalently for **all \(\eta\le \eta_\star\)**). Otherwise, “shrink δ” can become an illicit parameter change.
  - The single δ‑uniformity “fatal mode” is any residual/HB bound that implicitly allows \(\sup|F'/F|\) to grow like \(\delta^{-1}\) or worse; v33 must nail Lemma 7.1 at theorem level with explicit quantifiers in \(\delta,\alpha\). 【390:0†v32_status_decision_v2.md†L13-L16】
