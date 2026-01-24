# batch5_RH-LOCAL — Local term behavior under S5 endpoint redesign (v35 ground truth)

**Prompt context:** Batch‑5 decision batch. Baseline is **v35**. My scope is the *local term technology*—how
\(\displaystyle L_{\rm loc}(v):=Z'_{\rm loc}(v)/Z_{\rm loc}(v)\) behaves on \(\partial B\) under candidate endpoint norms, and whether an S5 endpoint can make the local contribution *subcritical in \(\delta\)* without hidden \(\delta\)-dependence.

I do **not** attempt to prove any new UE inequality or forcing lemma here (those are ENVELOPE/FORCE ownership), but I deliver the sharp, proof‑grade *local* bounds that would feed such an S5 design.

---

## 0) Ground-truth local identities in v35 (for anchoring)

1. **\(\kappa\)-admissibility**: an aligned box \(B=B(\alpha,m,\delta)\) is \(\kappa\)-admissible if
\(\operatorname{dist}(\partial B,Z(E))\ge \kappa\delta\).【622:0†manuscript_v35.pdf†L4-L13】

2. **Log-derivative decomposition** (local/residual split): on regions where \(E\) and \(Z_{\rm loc}\) are holomorphic and nonvanishing (in particular on \(\partial B\) under the boundary-contact convention),
\[
\frac{E'}{E}=\frac{F'}{F}+\frac{Z'_{\rm loc}}{Z_{\rm loc}}.
\]
【622:0†manuscript_v35.pdf†L47-L61】

3. **Pointwise collar bound (existing, \(\theta=1\))**:
\[
\sup_{v\in\partial B}\left|\frac{Z'_{\rm loc}(v)}{Z_{\rm loc}(v)}\right|\le \frac{N_{\rm loc}(m)}{\kappa\,\delta},
\]
where \(N_{\rm loc}(m)\) counts zeros in the local window (with multiplicity).【622:0†manuscript_v35.pdf†L62-L81】

4. **Explicit sum representation + \(s\)-frame mapping**: v35 records
\[
\frac{Z'_{\rm loc}(v)}{Z_{\rm loc}(v)}=\sum_{\rho\in Z(m)}\frac{m_\rho}{v-\rho}
=\frac12\sum_{\rho_s\in Z_s(m)}\frac{m_{\rho_s}}{s-\rho_s},
\]
with \(v=2s-1\) and \(Z_s(m)\) defined by \(|\gamma-m/2|\le 1/2\).【622:8†manuscript_v35.pdf†L43-L67】

5. **Exponent-budget diagnostic** (v35 UE gate language): if the UE step gives a prefactor \(\delta^p\) against a boundary endpoint and the collar/local split costs \(\delta^{-\theta}\), then the local contribution scales like \(\delta^{p-\theta}N_{\rm loc}(m)/\kappa\). Under the nominal \(\delta_0(m,\alpha)=\eta\alpha/(\log m)^2\) and \(N_{\rm loc}\ll\log m\), uniform \(\eta\)-shrinking closure requires \(p-\theta\ge 1/2\).【622:7†manuscript_v35.pdf†L18-L61】

This batch’s purpose is to show how \(\theta\) changes when the endpoint is changed away from pointwise/sup, and what a projection endpoint does to the local term.

---

## 1) Task 1 — Local term bounds in candidate boundary norms

Let \(B=B(\alpha,m,\delta)\) be \(\kappa\)-admissible and define
\(\displaystyle L_{\rm loc}(v)=\frac{Z'_{\rm loc}(v)}{Z_{\rm loc}(v)}=\sum_{\rho\in Z_{\rm loc}(m)}\frac{m_\rho}{v-\rho}\)
on \(\partial B\).

### 1.1 Endpoint (A): \(L^\infty(\partial B)\)

This is exactly v35 Lemma 10.8:

\[
\|L_{\rm loc}\|_{L^\infty(\partial B)}\le \frac{N_{\rm loc}(m)}{\kappa\,\delta}.
\]
**Local blow‑up exponent:** \(\theta=1\).【622:0†manuscript_v35.pdf†L62-L81】

This is the mechanism behind the v35 “pointwise UE endpoint is dead” verdict, because with \(p=1\) one has \(p-\theta=0\).【622:7†manuscript_v35.pdf†L62-L66】

### 1.2 Endpoint (B): \(L^2(\partial B,ds)\)

Here we can keep the *existing* pointwise collar lemma and convert it to \(L^2\) using \(|\partial B|=8\delta\) (perimeter of a \(\|\cdot\|_\infty\) box):

\[
\|L_{\rm loc}\|_{L^2(\partial B)}\le \sqrt{|\partial B|}\,\|L_{\rm loc}\|_{L^\infty(\partial B)}
\le \sqrt{8\delta}\cdot \frac{N_{\rm loc}(m)}{\kappa\,\delta}
=\frac{\sqrt{8}\,N_{\rm loc}(m)}{\kappa\,\delta^{1/2}}.
\]

**Local blow‑up exponent in \(L^2\):** \(\theta=1/2\).

**Key point for S5:** if an S5 UE inequality has the *same* prefactor power \(p=1\) but with an \(L^2\) endpoint,
\(\;D_B(W)\lesssim \delta^1\cdot \Phi_B\) with \(\Phi_B=\|E'/E\|_{L^2(\partial B)}\),
then the local term contributes at scale
\(\delta^{p-\theta}N_{\rm loc}/\kappa=\delta^{1/2}N_{\rm loc}/\kappa\),
which meets the v35 exponent budget threshold \(p-\theta\ge 1/2\).【622:7†manuscript_v35.pdf†L53-L61】

Under the nominal \(\delta_0(m,\alpha)=\eta\alpha/(\log m)^2\) and the v35 majorant \(N_{\rm loc}(m)\ll\log m\), this becomes
\(\delta_0^{1/2}N_{\rm loc}(m)\asymp \sqrt{\eta\alpha}\,(\log m)/(\log m)=O(\sqrt{\eta})\),
so the local term is **\(\eta\)-suppressible** (unlike the pointwise/sup case).【622:7†manuscript_v35.pdf†L53-L66】

### 1.3 General \(L^p\) scaling (optional but clean)

For any \(1\le p\le\infty\),
\[
\|L_{\rm loc}\|_{L^p(\partial B)}
\le |\partial B|^{1/p}\,\|L_{\rm loc}\|_{L^\infty(\partial B)}
\le (8\delta)^{1/p}\frac{N_{\rm loc}(m)}{\kappa\,\delta}
=\frac{8^{1/p}N_{\rm loc}(m)}{\kappa\,\delta^{1-1/p}}.
\]

So in \(L^p\), the local exponent is \(\theta=1-1/p\). In particular:
- \(p=2\Rightarrow \theta=1/2\) (the “budget‑threshold” case),
- \(p=1\Rightarrow \theta=0\) (no \(\delta\)-blowup, but likely too weak to control the dial deviation unless UE is redesigned accordingly).

---

## 2) Task 2 — Projection endpoint feasibility check (R1)

The prompt’s R1 candidate is:

- \(K_B:=\operatorname{span}\{(v-\rho)^{-1}:\rho\in Z_{\rm loc}(m)\}\subset L^2(\partial B)\),
- \(\Pi_B\) = orthogonal projection onto \(K_B\) in \(L^2(\partial B)\).

### 2.1 Is \(L_{\rm loc}\in K_B\) exactly?

**Yes, exactly.** Using the explicit local log-derivative identity already recorded in v35,【622:8†manuscript_v35.pdf†L43-L67】
\[
L_{\rm loc}(v)=\frac{Z'_{\rm loc}(v)}{Z_{\rm loc}(v)}=\sum_{\rho\in Z_{\rm loc}(m)}\frac{m_\rho}{v-\rho}.
\]
Each summand \((v-\rho)^{-1}\) lies in the spanning set; multiplicities \(m_\rho\) are just scalar coefficients.
Therefore \(L_{\rm loc}\in K_B\) and
\[
\Pi_B L_{\rm loc}=L_{\rm loc},\qquad (I-\Pi_B)L_{\rm loc}=0
\quad\text{in }L^2(\partial B).
\]

Because \(\partial B\) stays a positive distance from all \(\rho\in Z(E)\) by \(\kappa\)-admissibility,【622:0†manuscript_v35.pdf†L4-L13】
each kernel \((v-\rho)^{-1}\) is continuous on \(\partial B\), so the equality is not merely “a.e.”: the remainder is **identically zero as a boundary function**.

**Local conclusion:** any endpoint of the form \(\|(I-\Pi_B)(\cdot)\|_X\) will *annihilate the local term* if it is applied to \(E'/E\) using the exact split \(E'/E=F'/F+Z'_{\rm loc}/Z_{\rm loc}\).【622:0†manuscript_v35.pdf†L47-L61】

### 2.2 Can \(\|\Pi_B\|\) be bounded uniformly in \(\delta\to 0\) and \(N_{\rm loc}\sim\log m\)?

If \(\Pi_B\) is the **orthogonal projection in \(L^2\)**, then **yes trivially**:
\[
\|\Pi_B\|_{L^2\to L^2}=1,\qquad \|I-\Pi_B\|_{L^2\to L^2}=1,
\]
independent of \(\delta\), \(N_{\rm loc}\), and the positions of the zeros. This is a general Hilbert‑space fact (orthogonal projections are contractions).

#### Important nuance: Gram-matrix conditioning is *not* uniformly bounded (NO‑GO for coefficient control)

Even though \(\|\Pi_B\|_{2\to 2}=1\), **uniform bounds on the inverse Gram matrix of the spanning kernels are impossible** without additional (unavailable) zero separation hypotheses.

Reason: \(\kappa\)-admissibility only separates zeros from the boundary; it does not prevent two distinct zeros \(\rho_1,\rho_2\in Z_{\rm loc}(m)\) from approaching each other arbitrarily closely. When \(\rho_2\to\rho_1\), the functions
\(k_{\rho_j}(v):=(v-\rho_j)^{-1}\) become nearly linearly dependent on \(\partial B\), and the Gram determinant tends to \(0\), forcing \(\|G^{-1}\|\to\infty\).

**Practical consequence for ENVELOPE’s R1 implementation:**
- If the manuscript defines \(\Pi_B\) abstractly as the orthogonal projection (existence guaranteed), **no δ/N blow-up enters the constant ledger** at the operator level.
- If the manuscript requires *explicit coefficient formulas* for \(\Pi_B f\) in the non-orthonormal kernel basis, it will inherit an **unavoidable** potential blow-up through \(G^{-1}\) unless extra spacing structure is proved (not expected unconditionally).

This is not a proof obstruction per se, but it is a **referee risk** if the text implicitly assumes “nice conditioning”.

---

## 3) Task 3 — Compatibility with “no residual proxying”

The only identity used here is the v35 log-derivative split (no RH content):
\[
\frac{E'}{E}=\frac{F'}{F}+\frac{Z'_{\rm loc}}{Z_{\rm loc}}.
\]【622:0†manuscript_v35.pdf†L47-L61】

Applying a *linear* boundary operator \(T\) yields
\[
T\!\left(\frac{E'}{E}\right)=T\!\left(\frac{F'}{F}\right)+T\!\left(\frac{Z'_{\rm loc}}{Z_{\rm loc}}\right).
\]

For \(T=I-\Pi_B\) with \(\Pi_B\) as in §2, we have \(T(Z'_{\rm loc}/Z_{\rm loc})=0\) exactly (§2.1), hence
\[
(I-\Pi_B)\!\left(\frac{E'}{E}\right)=(I-\Pi_B)\!\left(\frac{F'}{F}\right)
\quad\text{on }\partial B.
\]

This is **not** residual proxying: it is an exact algebraic cancellation of the explicitly defined local term.

---

## 4) Ranked verdict (local-only): viable vs dead endpoint choices

This ranking is **only** about the *local term scaling*; ENVELOPE/FORCE must still supply an S5 UE inequality and forceability in the same endpoint class (v35 “S5 checklist”).【626:3†manuscript_v35.pdf†L9-L19】

### Rank 1 (most viable locally): \(L^2(\partial B)\) endpoint without projection

- Local exponent improves from \(\theta=1\) to \(\theta=1/2\) (§1.2).
- If the redesigned UE inequality still has \(p=1\) (as in the v35 chain but stopping at \(L^2\)), then \(p-\theta=1/2\), exactly meeting the budget threshold in v35.【622:7†manuscript_v35.pdf†L53-L61】
- Under \(\delta_0=\eta\alpha/(\log m)^2\) and \(N_{\rm loc}\ll\log m\), the local contribution becomes \(O(\sqrt{\eta})\) and is \(\eta\)-suppressible.

**Local risk profile:** LOW. (It uses only Lemma 10.8 + a perimeter estimate.)

### Rank 2 (best local cancellation, but higher global risk): projected endpoint \(\Phi_B(E):=\|(I-\Pi_B)(E'/E)\|_{L^2(\partial B)}\)

- Local term is annihilated exactly: \((I-\Pi_B)(Z'_{\rm loc}/Z_{\rm loc})=0\). (§2.1)
- Operator norm is uniformly bounded (\(\|\Pi_B\|=1\)) in \(L^2\). (§2.2)

**Local risk profile:** MED (local is perfect, but the *global* UE inequality may fail if the endpoint is too small to control \(D_B(W)\); also any coefficient‑level treatment must not assume bounded Gram inverses).

### Dead-on-arrival locally (already v35): pointwise/sup endpoint

- \(\theta=1\) and v35 records that within this endpoint class, \(p>1\) is forbidden; hence budget cannot be met.【622:7†manuscript_v35.pdf†L62-L66】

---

## 5) Paste-ready manuscript edits (TeX blocks) — S5‑LOC payload

These blocks are designed to be dropped into the S5 implementation draft (v36+), near the S5 checklist or directly after Lemma 10.8.

### 5.1 Lemma: \(L^2\) collar bound for the local log-derivative (improves \(\theta\) to \(1/2\))

```tex
% --- S5-LOC candidate: L2 local collar bound ---
\begin{lemma}[Local log-derivative bound in $L^2(\partial B)$]\label{lem:Zloc-L2-collar}
Let $B=B(\alpha,m,\delta)$ be $\kappa$--admissible (Definition~10.5), and let
$Z_{\rm loc}$ be the local factor with local zero-count $N_{\rm loc}(m)$ as in Section~10.1.
Then
\[
\left\|\frac{Z'_{\rm loc}}{Z_{\rm loc}}\right\|_{L^2(\partial B)}
\le \frac{\sqrt{8}\,N_{\rm loc}(m)}{\kappa\,\delta^{1/2}}.
\]
More generally, for any $1\le p\le\infty$,
\[
\left\|\frac{Z'_{\rm loc}}{Z_{\rm loc}}\right\|_{L^p(\partial B)}
\le \frac{8^{1/p}N_{\rm loc}(m)}{\kappa\,\delta^{1-1/p}}.
\]
\end{lemma}

\begin{proof}
Lemma~10.8 gives $\|Z'_{\rm loc}/Z_{\rm loc}\|_{L^\infty(\partial B)}\le N_{\rm loc}(m)/(\kappa\delta)$.
Since $|\partial B|=8\delta$, we have
$\|f\|_{L^p(\partial B)}\le |\partial B|^{1/p}\|f\|_{L^\infty(\partial B)}$ for every $1\le p\le\infty$,
which yields the stated bounds.
\end{proof}
```

### 5.2 Corollary line: local term becomes \(\eta\)-suppressible at nominal \(\delta_0\) if UE endpoint is \(L^2\)

```tex
% --- Consequence for the exponent budget under an L2 endpoint ---
\begin{remark}[Local term scaling under an $L^2$ endpoint]\label{rem:S5-L2-budget}
Assume an S5 upper-envelope inequality of the form
$D_B(W)\le 2C_{\rm up}\,\delta^p\,\Phi_B(E)$
with $\Phi_B(E)=\|E'/E\|_{L^2(\partial B)}$ and $p=1$.
Using the log-derivative split $E'/E=F'/F+Z'_{\rm loc}/Z_{\rm loc}$ (Lemma~10.7) and
Lemma~\ref{lem:Zloc-L2-collar}, the local contribution in $\Phi_B(E)$ enters as
$\delta\,\|Z'_{\rm loc}/Z_{\rm loc}\|_{L^2(\partial B)}\le (\sqrt{8}/\kappa)\,N_{\rm loc}(m)\,\delta^{1/2}$.
Under the nominal scaling $\delta_0(m,\alpha)=\eta\alpha/(\log m)^2$ and $N_{\rm loc}(m)\ll\log m$,
this term is $O(\sqrt{\eta})$ uniformly in $m$.
\end{remark}
```

### 5.3 Optional (R1): Projection definition + lemma that the projected endpoint kills the local term

```tex
% --- Optional S5-LOC/R1: projected endpoint that annihilates the local term ---
\begin{definition}[Local Cauchy subspace and $L^2$ projection]\label{def:KB-projection}
Let $B=B(\alpha,m,\delta)$ be $\kappa$--admissible and let $Z_{\rm loc}(m)$ denote the multiset
of zeros of $E$ used to define $Z_{\rm loc}$ (counted with multiplicity).
Define the finite-dimensional subspace
\[
K_B:=\mathrm{span}\{\,k_\rho:\partial B\to\mathbb{C},\ k_\rho(v)=(v-\rho)^{-1}\ :\ \rho\in Z_{\rm loc}(m)\,\}
\subset L^2(\partial B,|dv|),
\]
and let $\Pi_B:L^2(\partial B)\to K_B$ be the orthogonal projection.
\end{definition}

\begin{lemma}[Projection kills the local log-derivative]\label{lem:proj-kills-Zloc}
With notation as in Definition~\ref{def:KB-projection},
\[
\frac{Z'_{\rm loc}}{Z_{\rm loc}}(v)=\sum_{\rho\in Z_{\rm loc}(m)}\frac{m_\rho}{v-\rho}\in K_B
\quad (v\in\partial B).
\]
Hence $\Pi_B(Z'_{\rm loc}/Z_{\rm loc})=Z'_{\rm loc}/Z_{\rm loc}$ and
$(I-\Pi_B)(Z'_{\rm loc}/Z_{\rm loc})=0$ in $L^2(\partial B)$ (and thus pointwise on $\partial B$).
Consequently, using Lemma~10.7,
\[
(I-\Pi_B)\!\left(\frac{E'}{E}\right)=(I-\Pi_B)\!\left(\frac{F'}{F}\right)
\quad\text{on }\partial B.
\]
Moreover $\|\Pi_B\|_{L^2\to L^2}=1$.
\end{lemma}
```

```tex
\begin{remark}[Conditioning caveat for coefficient representations]\label{rem:proj-conditioning}
Lemma~\ref{lem:proj-kills-Zloc} uses only the abstract orthogonal projection $\Pi_B$ (a contraction).
No uniform bound on the inverse Gram matrix of the spanning kernels $k_\rho$ is available without
a lower bound on pairwise zero separations in $Z_{\rm loc}(m)$.
Therefore any coefficient-level formula for $\Pi_B$ must be treated as non-uniform unless additional
spacing structure is proved.
\end{remark}
```

---

## MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* Callsign: RH-LOCAL
* Result classification: **CONDITIONAL**
* Target gaps closed (by ID):
  - **G‑8 (local term control)** — extended to S5 endpoint classes by supplying proof‑grade bounds for \(\|Z'_{\rm loc}/Z_{\rm loc}\|_{L^2}\) and projected endpoints.
* Target gaps still open (by ID):
  - **S5–UE / S5–FORCE / S5–RES** (v35 checklist items owned by ENVELOPE/FORCE): redesigned UE inequality in the new endpoint, forceability link, and residual envelope in the same endpoint class.【626:3†manuscript_v35.pdf†L9-L19】
  - **G‑1/G‑12** residual constants ledger completeness (still global blocker; not local-owned).
* Key conclusions (≤5 bullets):
  1. In v35, pointwise collar control gives \(\theta=1\) (Lemma 10.8), making the local term \(\delta\)-inert when \(p=1\); this is the recorded NO‑GO mechanism.【622:0†manuscript_v35.pdf†L62-L81】【622:7†manuscript_v35.pdf†L62-L66】
  2. Switching the endpoint to \(L^2(\partial B)\) improves the local blow-up exponent to \(\theta=1/2\) with an explicit bound \(\|Z'_{\rm loc}/Z_{\rm loc}\|_2\le \sqrt{8}\,N_{\rm loc}/(\kappa\delta^{1/2})\).
  3. If an S5 UE inequality has \(p=1\) in an \(L^2\) endpoint (consistent with the v35 chain without the \(L^2\to\sup\) step), then \(p-\theta=1/2\) meets the budget threshold, and the local term becomes \(O(\sqrt{\eta})\) under \(\delta_0=\eta\alpha/(\log m)^2\).【622:7†manuscript_v35.pdf†L53-L61】
  4. Under the R1 projection proposal in \(L^2\), the local term is annihilated exactly: \((I-\Pi_B)(Z'_{\rm loc}/Z_{\rm loc})=0\), with \(\|\Pi_B\|=1\); however coefficient-level Gram inverses are not uniformly bounded without zero separation hypotheses.
* Paste-ready manuscript edits (TeX blocks):
  (i) revised lemma/proposition statements:
  - `lem:Zloc-L2-collar`, `lem:proj-kills-Zloc` (blocks in §5.1 and §5.3)
  (ii) revised definitions/remarks:
  - `def:KB-projection`, `rem:S5-L2-budget`, `rem:proj-conditioning` (blocks in §5.2 and §5.3)
  (iii) revised theorem/inequality lines:
  - Replace any S5 local-interface placeholder “\(\theta=1\)” with the \(L^2\) interface “\(\theta=1/2\)” when \(\Phi_B=\|E'/E\|_{L^2(\partial B)}\), per Remark `rem:S5-L2-budget`.
* Dependencies on other branches:
  - **RH-ENVELOPE:** must prove the UE inequality in the chosen \(\Phi_B\) endpoint and supply a residual envelope bound in the *same* endpoint class (S5–UE, S5–RES).
  - **RH-FORCE:** must provide a forceability link compatible with \(\Phi_B\) (S5–FORCE), as required by v35’s S5 checklist.【626:3†manuscript_v35.pdf†L9-L19】
* Referee risk notes (anticipated objections + how addressed):
  - **“Your \(L^2\) collar bound is just \(\sqrt{|\partial B|}\cdot L^\infty\)”** — yes, intentionally: it is unconditional, explicit, and δ‑uniform once κ‑admissibility holds.
  - **“Projection depends on unknown zeros; is that allowed / forceable?”** — local analysis only: cancellation is exact, but a usable S5 must still prove a UE inequality and forceability in that projected endpoint (ENVELOPE/FORCE ownership).
  - **“You implicitly assumed Gram matrices are well-conditioned.”** — explicitly *not* assumed; the patch adds `rem:proj-conditioning` stating uniform \(G^{-1}\) bounds are unavailable without zero separation hypotheses.
