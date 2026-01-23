# Batch 4 — RH-ENVELOPE (v34 ground truth)

**Scope owned (per Control Room):** envelope chain + residual envelope ledger interfaces + completion/entire hygiene.  
**Ground truth:** v34 (`manuscript_v34.tex/pdf`).  
**Key refs:** Lemma `\ref{lem:upper-envelope}`, Remark `\ref{rem:UE-gate}`, Lemma `\ref{lem:UE-d1-obstruction}`, Lemma `\ref{lem:residual-envelope}`.

---

## 1) PRIMARY TASK 1 — UE “p>1” NO‑GO (current pointwise/sup architecture)

### 1.1 Referee verdict

Under the **current v34 pointwise UE architecture** (Lemma `\ref{lem:upper-envelope}`), any claim of an inequality of the form

\[
\text{(dimensionless pointwise quantity)} \ \le\ C_{\text{shape}}\ \delta^{p}\ \sup_{\partial B}\Bigl|\frac{E'}{E}\Bigr|
\]

with **shape-only** constant \(C_{\text{shape}}\) cannot have **\(p>1\)**.  
This is a **scaling obstruction**: the only scale-invariant combination built from \(\sup_{\partial B}|E'/E|\) is \(\delta\sup_{\partial B}|E'/E|\), i.e. \(p=1\). Anything strictly better forces degeneration as \(\delta\to0\).

This matches (and strengthens) v34’s explicit **UE‑gate obstruction posture** (Remark `\ref{rem:UE-gate}` + Lemma `\ref{lem:UE-d1-obstruction}`).

### 1.2 Proof‑grade NO‑GO lemma (scaling obstruction)

#### What this lemma is and is not

- It is **not** re-proving Lemma `\ref{lem:upper-envelope}`.
- It is a **structural impossibility** statement: you cannot patch the UE proof to get \(p>1\) while keeping the same endpoint \(\sup_{\partial B}|E'/E|\) and a shape-only constant.

#### Paste‑ready TeX insertion (add immediately after Remark `\ref{rem:UE-gate}` or after Lemma `\ref{lem:UE-d1-obstruction}`)

```tex
\begin{lemma}[Scaling obstruction for pointwise UE with $\sup_{\partial B}|E'/E|$]
\label{lem:UE-scaling-nogo}
Fix the normalized square $Q=[-1,1]^2$.
Let $B_\delta:=v_0+\delta Q$ be its similarity image for some $v_0\in\C$ and $\delta>0$.
Let $E$ be holomorphic in a neighborhood of $\overline{B_\delta}$ and assume the boundary-contact
convention $E\neq 0$ on $\partial B_\delta$. Let $G_{\rm out}$ be the outer factor on $B_\delta$ built
from $\log|E|$ on $\partial B_\delta$, and set $W:=E/G_{\rm out}$ (so $|W|=1$ a.e.\ on $\partial B_\delta$).

Consider any pointwise functional $\mathcal D(W;B_\delta)$ that is \emph{scale-invariant} under similarities,
in the sense that for $T_\delta(z)=v_0+\delta z$ and $w(z):=W(T_\delta(z))$ one has
$\mathcal D(W;B_\delta)=\mathcal D(w;Q)$.

There is no exponent $p>1$ and no \emph{shape-only} constant $C$ (depending only on $Q$) such that
for all $\delta$ in a neighborhood of $0$ and all such $E$,
\[
\mathcal D(W;B_\delta)\ \le\ C\,\delta^{p}\,\sup_{\xi\in\partial B_\delta}\Bigl|\frac{E'(\xi)}{E(\xi)}\Bigr|.
\]
Equivalently: with the endpoint $\sup_{\partial B}|E'/E|$, the only non-degenerate scale exponent is $p=1$;
any putative $p>1$ forces collapse as $\delta\to 0$.
\end{lemma}

\begin{proof}
Let $T_\delta(z)=v_0+\delta z$ map $\partial Q$ onto $\partial B_\delta$ and set $e(z):=E(T_\delta(z))$.
Then
\[
\frac{E'(T_\delta(z))}{E(T_\delta(z))}=\delta^{-1}\,\frac{e'(z)}{e(z)},
\qquad\text{hence}\qquad
\sup_{\partial B_\delta}\Bigl|\frac{E'}{E}\Bigr|=\delta^{-1}\sup_{\partial Q}\Bigl|\frac{e'}{e}\Bigr|.
\]
Outer factors are similarity-covariant (Dirichlet data for $\log|E|$ pull back under $T_\delta$), so
the corresponding inner quotients satisfy $w(z)=W(T_\delta(z))$ and therefore, by the scale-invariance
assumption on $\mathcal D$, $\mathcal D(W;B_\delta)=\mathcal D(w;Q)$.

The claimed inequality would therefore imply
\[
\mathcal D(w;Q)\ \le\ C\,\delta^{p-1}\,\sup_{\partial Q}\Bigl|\frac{e'}{e}\Bigr|.
\]
Choose any fixed holomorphic $e$ on a neighborhood of $\overline Q$ with $e\neq 0$ on $\partial Q$ and
$\mathcal D(w;Q)>0$ while $\sup_{\partial Q}|e'/e|<\infty$ (e.g.\ a non-constant $e$ with no boundary zeros).
Then the right-hand side tends to $0$ as $\delta\to 0$ whenever $p>1$, contradicting the fixed positive value
of $\mathcal D(w;Q)$. Hence no such $p>1$ with shape-only $C$ can hold.
\end{proof}
```

#### Audit note (why this blocks “η‑absorption via p>1”)

The absorption mechanism requires a **strictly positive** leftover \(\delta\)-power after inserting the collar bound
for \(Z_{\rm loc}'/Z_{\rm loc}\), i.e. something of the form \(\delta^{p-1}\) with \(p>1\).
The lemma above shows that **within the pointwise/sup endpoint class**, \(p>1\) cannot be achieved
without changing the endpoint functional/hypotheses.

---

## 2) PRIMARY TASK 2 — ONE UE‑Gate redesign candidate (explicit package; high‑risk)

### 2.1 Candidate chosen: **R1 (change endpoint functional) via “projection endpoint”**

**Goal:** replace the UE endpoint \(\sup_{\partial B}|E'/E|\) by an endpoint functional that:
1) still controls the **same pointwise dial quantity** used in the tail inequality, but  
2) makes the **local term subcritical** (i.e., produces a leftover positive \(\delta\)-power after the split).

**Proposed mechanism (explicit, but not yet proved):** replace the raw endpoint by a *projected endpoint*
that annihilates the local Cauchy kernel contribution on the boundary, i.e. an endpoint that behaves like
a **bounded operator applied to** \(E'/E\) whose kernel contains the span of \(\{(v-\rho)^{-1}\}\) for
\(\rho\in\mathcal Z_{\rm loc}\).

This is the smallest redesign that can plausibly change the \(\delta\)-budget without requiring a pointwise
\(p>1\) miracle, because it attacks the **true obstruction**: the collar term is (by construction) a sum of
Cauchy kernels with coefficient \(1/\delta\), and any norm that treats it in a purely pointwise way will
cancel \(\delta\).

### 2.2 Lemma package (v35‑ready placeholders)

#### (R1‑Def) Projected endpoint functional (to be defined on each aligned box)

```tex
\begin{definition}[Projected UE endpoint on $\partial B$]
\label{def:UE-projected-endpoint}
Let $B$ be an aligned box and let $\mathcal V_{\rm loc}$ be the finite-dimensional subspace of
$L^2(\partial B,ds)$ spanned by the boundary traces of the Cauchy kernels
\[
k_\rho(v):=\frac{1}{v-\rho},\qquad \rho\in \mathcal Z_{\rm loc}(m).
\]
Let $\Pi_{\rm loc}$ denote the $L^2(\partial B)$-orthogonal projection onto $\mathcal V_{\rm loc}$.
Define the projected endpoint
\[
\mathcal N_{\rm UE}(E;B)
:=\bigl\|\,(I-\Pi_{\rm loc})\bigl(E'/E\bigr)\,\bigr\|_{L^\infty(\partial B)}.
\]
\end{definition}
```

#### (R1‑UE) Proposed projected UE bound (what replaces Lemma `\ref{lem:upper-envelope}` in the tail chain)

```tex
\begin{lemma}[Projected upper envelope bound (proposed)]
\label{lem:UE-projected}
Under the hypotheses of Lemma~\ref{lem:upper-envelope}, one has
\[
\sum_{\pm}|W(v_\pm)-e^{i\varphi_0^\pm}|
\ \le\ 2\,C_{\rm up}\,\delta\,\mathcal N_{\rm UE}(E;B),
\]
where $\mathcal N_{\rm UE}(E;B)$ is the projected endpoint from Definition~\ref{def:UE-projected-endpoint}.
\end{lemma}
```

#### (R1‑Why this could clear the gate)

If (and only if) one can prove that:
- the projection is **uniformly bounded** as an operator on the boundary function space used, and
- \((I-\Pi_{\rm loc})(Z_{\rm loc}'/Z_{\rm loc})=0\) (by construction),

then the split \(E'/E=F'/F+Z'_{\rm loc}/Z_{\rm loc}\) yields
\[
\mathcal N_{\rm UE}(E;B)=\mathcal N_{\rm UE}(F;B),
\]
so the tail bound becomes purely residual again without “proxying” (because the local part is removed by a
**declared operator**, not by an informal substitution).  

**Remaining hard obligation:** show the projected endpoint is itself controllable by an RH‑free residual bound
with constants compatible with the rest of v34.

### 2.3 What must be rewritten in v34 if Control Room selects R1

- Replace Lemma `\ref{lem:upper-envelope}` endpoint \(\sup_{\partial B}|E'/E|\) by \(\mathcal N_{\rm UE}(E;B)\).
- Replace Corollary `\ref{cor:UE-residual-local}` accordingly (local term should disappear at the endpoint).
- Add a new “projection well-definedness and boundedness” lemma for the chosen boundary space.

### 2.4 Remaining blockers even if R1 succeeds

- Projection must be canonical and **computable/definable without already knowing the zeros** in a circular way.
- Requires a rigorous function-space framework on \(\partial B\) and compatibility with outer factor construction.
- High referee risk: “You smuggled in the local zero set via the projection.” This must be confronted explicitly.

**Viability ranking:** High-risk / research-grade. Included because it is one of the few explicit redesigns that
attacks the true \(\delta\)-budget obstruction rather than trying to squeeze \(p>1\) from the same endpoint.

---

## 3) PRIMARY TASK 3 — FIX “ENTIRE” MISUSE (completion/holomorphy hygiene)

### 3.1 Decision: **ENT‑1 (preferred)** — switch to an entire completion in width‑2

v34 defines
\[
\Lambda_2(u)=\pi^{-u/4}\Gamma(u/4)\zeta(u/2),
\]
which is **meromorphic** (simple poles at \(u=0\) and \(u=2\)). The text currently claims “\(\Lambda_2\) is entire”
and propagates “\(E\) is entire” in proofs.

**Patch decision:** keep \(\Lambda_2\) as the width‑2 completed zeta (meromorphic), but define an *entire completion*
\[
\xi_2(u):=\frac{u(u-2)}{8}\Lambda_2(u),
\]
and set the manuscript’s working function to
\[
E(v):=\xi_2(1+v).
\]

This makes all “\(E\) is entire” usages correct and removes the need for pole-avoidance hypotheses.

### 3.2 Inventory — every incorrect “entire” usage in v34 and how it is fixed

These are incorrect **in current v34** because \(E(v)=\Lambda_2(1+v)\) is meromorphic.

1) **Width‑2 normalization section:** “\(\Lambda_2\) is entire”  
2) **Lemma `\ref{lem:zloc-finite}` proof:** “Since \(E\) is entire…”  
3) **Lemma `\ref{lem:collar-existence}` proof:** “Zeros of the entire function \(E\) are isolated.”  
4) **Lemma `\ref{lem:zloc-finite}` proof (later):** another “Since \(E\) is entire…”

Under ENT‑1, these become correct because \(E\) is redefined as an entire completion.

### 3.3 Paste‑ready TeX patch blocks (ENT‑1)

#### (ENT‑1a) Replace the start of Section `\ref{sec:width2}` (width‑2 normalization) with:

```tex
\subsection{Width-2 normalization}
\label{sec:width2}

Let $s$ denote the usual complex variable for $\zeta(s)$. We pass to the width-$2$ coordinate
\[
u:=2s,
\qquad \zeta_2(u):=\zeta(u/2).
\]
Define the width-$2$ completed zeta
\[
\Lambda_2(u):=\pi^{-u/4}\Gamma(u/4)\zeta(u/2).
\]
Then $\Lambda_2$ is meromorphic (simple poles at $u=0$ and $u=2$) and satisfies the functional equation
\[
\Lambda_2(u)=\Lambda_2(2-u).
\]
Define the entire completion
\[
\xi_2(u):=\frac{u(u-2)}{8}\,\Lambda_2(u),
\]
so that $\xi_2$ is entire and satisfies $\xi_2(u)=\xi_2(2-u)$.

Recenter at $u=1$:
\[
v:=u-1,
\qquad E(v):=\xi_2(1+v).
\]
Then $E$ is entire and obeys the centered functional equation $E(v)=E(-v)$, and complex conjugation gives
$E(\overline{v})=\overline{E(v)}$.
```

#### (ENT‑1b) Patch the residual-envelope identity in Lemma `\ref{lem:residual-envelope}` proof

Replace the displayed identity beginning “From \(\Lambda_2(u)=\cdots\) we obtain for \(u=1+v\)” by:

```tex
From $\xi_2(u)=\frac{u(u-2)}{8}\Lambda_2(u)$ and $\Lambda_2(u)=\pi^{-u/4}\Gamma(u/4)\zeta(u/2)$ we obtain,
for $u=1+v$,
\[
\frac{E'(v)}{E(v)}
=\frac{\xi_2'(u)}{\xi_2(u)}
=\Bigl(\frac{1}{u}+\frac{1}{u-2}\Bigr)\ -\ \frac14\log\pi\ +\ \frac14\frac{\Gamma'}{\Gamma}\Bigl(\frac{u}{4}\Bigr)
\ +\ \frac12\,\frac{\zeta'}{\zeta}\Bigl(\frac{u}{2}\Bigr),
\qquad (u=1+v).
\]
```

This is the only downstream identity change required by ENT‑1.

---

## 4) SECONDARY (if time) — Residual envelope lemma source closure (G‑1/G‑12 interface)

v34 Lemma `\ref{lem:residual-envelope}` still imports a “standard RH‑free” local-subtraction estimate for
\(\zeta'/\zeta\) without a pinned primary citation.

### 4.1 Minimal referee-acceptable patch (citation + proof sketch)

**Suggested insertion:** add a short lemma immediately before Lemma `\ref{lem:residual-envelope}`.

```tex
\begin{lemma}[Classical local-zero subtraction for $\zeta'/\zeta$ (RH-free)]
\label{lem:zeta-logder-local-subtraction}
Let $s=\sigma+it$ with $0\le \sigma\le 1$ and $t\ge 5$.
Let $\rho=\beta+i\gamma$ range over nontrivial zeros of $\zeta$.
Then
\[
\frac{\zeta'}{\zeta}(s)
=\sum_{|\gamma-t|\le 1}\frac{1}{s-\rho}\ +\ O(\log(t+2)),
\]
where the implied constant is absolute and uniform in $0\le\sigma\le 1$.
\end{lemma}
```

**Proof sketch (in-text):** derive from the Hadamard product for \(\xi(s)\) and Stirling for \(\Gamma'/\Gamma\),
then split the zero sum into \(|\gamma-t|\le 1\) and \(|\gamma-t|>1\) and bound the tail using the standard
zero-counting estimate \(N(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}+O(\log T)\).

**Primary sources (acceptable to cite):**
- E.C. Titchmarsh, *The Theory of the Riemann Zeta-Function* (2nd ed., revised by Heath-Brown), chapters on
  \(\xi'/\xi\) and the representation of \(\zeta'/\zeta\) in terms of zeros + \(O(\log t)\).
- A. Ivić, *The Riemann Zeta-Function*, sections on \(\zeta'/\zeta\) and zero-localized expansions.

(If Control Room requires theorem numbers, we should web-verify exact numbering; otherwise the above source-level
citation + proof outline is usually referee-acceptable.)

---

# MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* Callsign: RH-ENVELOPE
* Result classification: **FAIL** (UE “p>1” gate cannot be cleared in the current pointwise/sup architecture; a structural redesign is required)
* Target gaps closed (by ID):
  - (Decision closure) UE “p>1” mirage retired for the pointwise/sup endpoint class (supports v34’s UE-gate remark/obstruction posture).
  - (Hygiene) ENT misuse fix deliverable provided (completion/entire correction).
* Target gaps still open (by ID):
  - **G-2 (UE δ-exponent / tail absorption): OPEN** (and now provably blocked in the pointwise/sup endpoint class).
  - **G-1/G-12 (residual-envelope provenance): CONDITIONAL** until Control Room inserts the explicit lemma+citation (Section 4.1).
* Key conclusions (5 bullets max):
  1. Any UE bound of the form “pointwise ≤ shape-only·δ^p·sup|E'/E|” cannot have \(p>1\); the scale-invariant exponent is \(p=1\).
  2. Therefore η‑absorption via a “δ^{3/2} pointwise UE” is structurally dead unless the endpoint functional/hypotheses are changed.
  3. ENT‑1 (switch to \(\xi_2\) and set \(E(v)=\xi_2(1+v)\)) is the cleanest hygiene patch: it makes all “E entire” uses correct and removes pole-avoidance side conditions.
  4. ENT‑1 requires exactly one downstream identity patch (the log-derivative identity inside Lemma `\ref{lem:residual-envelope}` proof).
  5. Residual-envelope import should be hardened by inserting an explicit RH-free \(\zeta'/\zeta\) local-subtraction lemma with a Titchmarsh/Ivić citation and proof sketch.
* Paste-ready manuscript edits:
  (i) revised lemma/proposition statements
  - Add Lemma `lem:UE-scaling-nogo` (Section 1.2 TeX block).
  - (Optional future) Add the proposed “projection endpoint” definitions/lemmas if Control Room elects R1 (Section 2.2 blocks).
  (ii) revised definitions/remarks
  - Apply ENT‑1 width‑2 completion patch (Section 3.3 ENT‑1a).
  (iii) revised theorem/inequality lines
  - Patch the log-derivative identity in the residual-envelope proof (Section 3.3 ENT‑1b).
  - (Optional) Insert Lemma `lem:zeta-logder-local-subtraction` (Section 4.1).
* Dependencies on other branches:
  - None for the NO-GO lemma and ENT‑1 hygiene patch.
  - If Control Room pursues redesign R1, it will require a new, non-circular specification of the projection space \(\mathcal V_{\rm loc}\) (likely a Control Room decision).
* Referee risk notes (anticipated objections + how addressed):
  - **Objection:** “Your scaling no-go assumes \(\delta\to 0\), but the manuscript uses \(\delta\le\delta_0(m)\).”  
    **Response:** v34 already permits arbitrary shrink \(\delta\downarrow 0\) via the κ-admissible shrink lemma; also η is a free parameter, so a proof-grade UE claim must be stable under arbitrarily small scales.
  - **Objection:** “Outer factor covariance under similarities is asserted.”  
    **Response:** It follows because the Dirichlet solution for boundary data \(\log|E|\) is similarity-covariant; therefore the harmonic extension and its conjugate transport under pullback.
  - **Objection:** “ENT‑1 changes \(E'/E\) by rational terms.”  
    **Response:** ENT‑1b explicitly patches the identity; the added terms are uniformly \(O(1)\) on tail boxes (Im \(\asymp m\ge 10\)) and can be absorbed into the residual-envelope constants.
