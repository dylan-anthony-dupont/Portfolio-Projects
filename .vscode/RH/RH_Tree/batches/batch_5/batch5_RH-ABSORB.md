# Batch 5 — RH-ABSORB (S5 “budget referee” for redesigned endpoints)  
**Callsign:** RH-ABSORB  
**Ground truth:** v35 (`manuscript_v35.pdf`).  
**Mission:** Deliver decision-grade budget calculus for S5 endpoint redesigns; evaluate candidate classes; provide v36+ insertion text that prevents exponent drift.

v35 locks in:
- **Exponent budget (pointwise archetype):** under \(\delta_0=\eta\alpha/(\log m)^2\) and \(N_{\rm loc}(m)\ll \log m\), uniform \(\eta\)-shrinking closure requires \(p-\theta\ge 1/2\).【638:1†manuscript_v35.pdf†L15-L70】  
- **S5 frontier:** any future closure must redesign the envelope endpoint/local interface to satisfy the exponent budget uniformly in \(m\), and must remain **forceable** via \(D_B(W)\).【638:2†manuscript_v35.pdf†L6-L48】

Batch‑5 extends the budget theorem to **general S5 endpoints** of the form \(\Phi_B\) and records a proof-grade NO‑GO for a large “naïve endpoint” class so drift stops.

---

## Task 1 — Generalized budget theorem for an S5 endpoint (TeX-ready)

### 1.1 Setup (S5 schematic)
Fix \(m\ge 10\), \(\alpha\in(0,1]\), \(\eta\in(0,1]\), and the nominal scale
\[
\delta_0(m,\alpha):=\frac{\eta\alpha}{(\log m)^2}.
\]
Let \(B=B(\pm\alpha,m,\delta)\) be a \(\kappa\)-admissible box with \(0<\delta\le \delta_0\) (v35 collar policy).  

Assume an S5 “UE step” of the form (as required in v35 §12):【638:2†manuscript_v35.pdf†L34-L48】
\[
D_B(W)\ \le\ C_{\rm up}\,\delta^{p}\,\Phi_B\!\Big(\frac{E'}{E}\Big)\qquad (p>0),
\tag{S5-UE}
\]
where \(D_B(W)\) is the forceable dial deviation (v35)【638:2†manuscript_v35.pdf†L10-L19】 and \(\Phi_B\) is a **non-pointwise boundary functional** (the S5 object).

Assume \(\Phi_B\) admits a residual+local split compatible with \(E'/E = F'/F + Z_{\rm loc}'/Z_{\rm loc}\):
\[
\Phi_B\!\Big(\frac{E'}{E}\Big)\ \le\ \underbrace{\mathrm{Res}(m)}_{\text{δ-uniform}}\ +\ \underbrace{ \Phi_B\!\Big(\frac{Z'_{\rm loc}}{Z_{\rm loc}}\Big)}_{\text{local}}.
\tag{S5-SPLIT}
\]
Assume the local term is bounded by an explicit “collar blow-up” model:
\[
\Phi_B\!\Big(\frac{Z'_{\rm loc}}{Z_{\rm loc}}\Big)\ \le\ C_{\rm loc}\,\delta^{-\theta}\,G\!\big(N_{\rm loc}(m),\kappa\big),
\qquad (\theta\ge 0),
\tag{S5-LOC}
\]
and that the growth in \(m\) is explicit:
\[
\mathrm{Res}(m)\ \le\ A_L(\log m)^{r_L}+B_L,\qquad
N_{\rm loc}(m)\ \le\ A_N\log m+B_N.
\tag{GROW}
\]

This abstracts exactly what v35 requests in §12.2 (“S5 checklist”)【638:2†manuscript_v35.pdf†L49-L56】, but with the local term routed through \(\Phi_B\) and \(G\).

---

### 1.2 Theorem (General S5 exponent budget under \(\delta_0=\eta\alpha/(\log m)^2\))
> **Theorem (S5 Budget Theorem).**  
> Assume (S5‑UE), (S5‑SPLIT), (S5‑LOC), and (GROW) hold for all \(m\ge 10\), all \(\alpha\in(0,1]\), and all \(\kappa\)-admissible \(0<\delta\le\delta_0(m,\alpha)\), with constants \(C_{\rm up},C_{\rm loc},A_L,B_L,A_N,B_N\) independent of \((m,\alpha,\delta)\).  
> Suppose further that for some \(q\ge 0\) and \(C_G>0\),
> \[
> G(n,\kappa)\ \le\ C_G\,\kappa^{-u}\,n^{q}\qquad\text{for all }n\ge 1
> \tag{G-poly}
> \]
> (with fixed \(u\ge 0\)).  
> Then at the nominal scale \(\delta=\delta_0(m,\alpha)\) one has the explicit envelope budget:
> \[
> D_B(W)\ \le\
> C_{\rm up}\Bigl(\delta_0^{p}\,\mathrm{Res}(m)\ +\ C_{\rm loc}\,\delta_0^{p-\theta}\,G(N_{\rm loc}(m),\kappa)\Bigr).
> \tag{BUDGET-S5}
> \]
> Moreover:
> 
> 1. (**m-uniform boundedness**) The local contribution is uniformly bounded in \(m\ge 10\) if and only if
> \[
> 2(p-\theta)\ \ge\ q.
> \tag{BUDGET-1}
> \]
> 2. (**η-shrinkability**) If \(p-\theta>0\) and (BUDGET‑1) holds, then
> \[
> \sup_{m\ge 10}\ \delta_0(m,1)^{p-\theta}\,G(N_{\rm loc}(m),\kappa)\ =\ O\big(\eta^{p-\theta}\big),
> \]
> so the local penalty can be made arbitrarily small by choosing \(\eta\) small.
> 3. (**δ‑shrink monotonicity condition**) If \(p>0\) and \(p-\theta\ge 0\), then the RHS of (BUDGET‑S5) is nondecreasing in \(\delta\) (for fixed \(m,\alpha\)); hence replacing \(\delta_0\) by a smaller κ‑admissible \(\delta\le\delta_0\) can only improve the inequality. If \(p-\theta<0\), κ‑shrinking can *worsen* the envelope term, so the standard admissible-shrink policy is unsafe unless redesigned.
>
> **Proof sketch (budget algebra):** Substitute (S5‑SPLIT) into (S5‑UE), then insert (S5‑LOC) at \(\delta=\delta_0\) to get (BUDGET‑S5). With \(\alpha=1\), \(\delta_0=\eta/(\log m)^2\), \(N_{\rm loc}(m)\ll\log m\), and (G‑poly), the local term is
> \[
> \delta_0^{p-\theta}G(N_{\rm loc},\kappa)\ \ll\ \eta^{p-\theta}(\log m)^{-2(p-\theta)}(\log m)^{q}
> =\eta^{p-\theta}(\log m)^{q-2(p-\theta)}.
> \]
> This is uniformly bounded in \(m\) iff \(q-2(p-\theta)\le 0\), i.e. (BUDGET‑1). If additionally \(p-\theta>0\), the factor \(\eta^{p-\theta}\) gives η‑shrinkability. The δ‑monotonicity claim follows because \(\delta^{p}\) and \(\delta^{p-\theta}\) are nondecreasing in \(\delta\) exactly when \(p\ge 0\) and \(p-\theta\ge 0\). ∎

### 1.3 Relation to v35 Theorem 10.12
v35’s exponent budget theorem is the special case:
- \(\Phi_B(f)=\sup_{\partial B}|f|\),
- \(G(N_{\rm loc},\kappa)=N_{\rm loc}/\kappa\) so \(q=1\),
- \(\theta=1\) (pointwise collar blow-up),
so (BUDGET‑1) reduces to \(p-\theta\ge 1/2\), matching v35 Theorem 10.12.【638:1†manuscript_v35.pdf†L15-L70】

---

## Task 2 — Candidate evaluation (Budget PASS/FAIL/CONDITIONAL)

No branch-supplied explicit \(\Phi_B\) definitions were included in the batch materials. Therefore I evaluate the **two candidate classes explicitly floated by the v35 roadmap** (L2/energy; “avoid collar blow-up”) and record a proof-grade NO‑GO for a large naive class.

### Candidate class C1 — “Boundary \(L^p\) norm of \(E'/E\) with triangle-inequality local bound”
**Prototype:** \(\Phi_B(f)=\|f\|_{L^p(\partial B)}\) (or any comparable “size” functional), and local control uses a worst-case sum over poles, giving
\[
\Phi_B\Big(\frac{Z'_{\rm loc}}{Z_{\rm loc}}\Big)\ \lesssim\ \delta^{-1}\,\frac{N_{\rm loc}(m)}{\kappa}.
\]
Then \(\theta=1\), \(G(n,\kappa)=n/\kappa\), so \(q=1\).

**Budget test:** requires \(2(p-\theta)\ge q\Rightarrow p-\theta\ge 1/2\). With \(\theta=1\), this forces \(p\ge 3/2\), i.e. a **strictly stronger-than-pointwise δ-gain**.

- This is exactly the reason v35 says “avoid the pointwise \(\delta^{-1}\) collar blow-up” in §12.【638:2†manuscript_v35.pdf†L19-L25】

**Decision:** **Budget FAIL** for this class unless an S5 UE proof produces \(p\ge 3/2\) *in this endpoint class*.  
Given v35’s explicit NO‑GO for recovering \(p>1\) inside the pointwise/sup class, and the fact that this C1 class keeps the same local singularity exponent \(\theta=1\), C1 should be treated as a **default dead-end** until a concrete UE proof shows \(p\ge 3/2\) with δ-uniform constants.

### Candidate class C2 — “Energy / quadratic endpoint with square-summed local contribution”
This is the direction floated in the roadmap as “L2/energy envelope / Carleson measure.”【638:6†v34_next_build_plan_diff.md†L9-L17】【638:2†manuscript_v35.pdf†L27-L48】

The only way such an endpoint helps is if it changes the **local interface** so that either:
- \(\theta\) is reduced below 1, and/or
- \(G(n,\kappa)\) grows sublinearly in \(n\) (e.g., \(G(n)\sim n^{1/2}\)).

Two subcases:

**C2a (optimistic):** \(\theta=1/2\) and \(G(n,\kappa)\lesssim \kappa^{-1} n^{1/2}\) (square-summed poles).  
Then \(q=1/2\), so budget requires \(p-\theta\ge q/2 = 1/4\), i.e.
\[
p\ \ge\ \frac34.
\]
**Decision:** **Budget CONDITIONAL** — PASS if the UE step supplies \(p\ge 3/4\) in the same \(\Phi_B\) class with δ-uniform constants, and the local estimate truly achieves \(n^{1/2}\) growth (not \(n\)).

**C2b (less optimistic):** \(\theta=1/2\) but still \(G(n,\kappa)\lesssim \kappa^{-1}n\).  
Then \(q=1\), so budget requires \(p-\theta\ge 1/2\Rightarrow p\ge 1\).  
**Decision:** **Budget CONDITIONAL** — PASS if the UE step supplies \(p\ge 1\) and the local L2 bound is \(\delta^{-1/2}n\) (already a half-power improvement over pointwise).

### Candidate class C3 — “Local interface redesign achieving θ=0 (no δ blow-up), G(n)~n”
This is the other roadmap hint (“avoid collar blow-up”).【638:6†v34_next_build_plan_diff.md†L12-L15】

If one can prove
\[
\Phi_B\Big(\frac{Z'_{\rm loc}}{Z_{\rm loc}}\Big)\ \lesssim\ G(N_{\rm loc},\kappa),
\quad\text{with no }\delta^{-\theta}\text{ factor (}\theta=0\text{)},
\]
and \(G(n)\sim n\) (so \(q=1\)), then the budget condition becomes \(p\ge 1/2\).  
**Decision:** **Budget CONDITIONAL** — PASS if a new local lemma delivers \(\theta=0\) (or even \(\theta<1/2\)) with δ-uniform constants. This would be a genuine “S5 breakthrough,” but it requires a very explicit analytic mechanism.

---

## Task 3 — Manuscript insertion guidance: “S5 acceptance criterion” (v36/v35+)

The point is to prevent v36+ from drifting into “endpoint vibes.” The acceptance criterion must require **explicit** \((p,\theta,q)\) and explicit forceability.

### Paste-ready paragraph for the start of the S5 section (TeX block)
```tex
\begin{remark}[S5 acceptance criterion (budget calculus; no drift)]
\label{rem:S5-accept}
Any proposed S5 redesign must specify a boundary functional $\Phi_B$ (δ-normalized; shape-invariant)
and prove two explicit inequalities uniformly for all $m\ge 10$, all $\alpha\in(0,1]$, and all
$\kappa$--admissible $0<\delta\le \delta_0(m,\alpha)=\eta\alpha/(\log m)^2$:

1) (S5--UE) a forceable upper-envelope bound
\[
D_B(W)\le C_{\rm up}\,\delta^{p}\,\Phi_B(E'/E)
\]
with an explicit exponent $p>0$ and δ-uniform constant $C_{\rm up}$;

2) (S5--LOC) a local/collar bound in the same endpoint class
\[
\Phi_B(Z'_{\rm loc}/Z_{\rm loc})\le C_{\rm loc}\,\delta^{-\theta}\,G(N_{\rm loc}(m),\kappa)
\]
with explicit $\theta\ge 0$ and an explicit growth model for $G$ (e.g. $G(n,\kappa)\ll \kappa^{-u}n^q$).

The redesign is budget-viable for uniform $\eta$--shrinking closure under $\delta_0$
only if the S5 Budget Theorem yields
$2(p-\theta)\ge q$ (and $p-\theta>0$ for shrinkability).
If $p-\theta<0$, the standard $\kappa$--admissible shrink policy is unsafe (shrinking δ can
increase the envelope term) and must be redesigned.

Finally, the forcing chain remains phrased in terms of $D_B(W)$; therefore S5 must include either
$\Phi_B\ge D_B(W)$ on all admissible boxes or a new forcing lemma that lower-bounds $\Phi_B$
directly (cf.\ Remark~12.1).
\end{remark}
```

---

# MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* **Callsign:** RH-ABSORB

* **Result classification:** **PASS** *(delivered the required decision calculus; provided a proof-grade NO‑GO for a broad naive endpoint class and explicit acceptance tests for S5 candidates).*

* **Target gaps closed (by ID):**
  - **G-4 (reframed as S5 budget discipline):** closed at the “drift prevention / acceptance test” level (S5 budget theorem + explicit PASS/FAIL criteria). v35 already records G‑4 as “closed-as-NOGO/reframed,” and this makes the S5 reframe operational.【638:11†CR_master_dashboard_v35_locked.md†L7-L12】
  - **G-5 (S5-dependent κ-interplay):** partially closed at the *design* level via the δ‑monotonicity clause in the S5 Budget Theorem (explicit condition \(p-\theta\ge 0\) required for admissible δ‑shrinking).

* **Target gaps still open (by ID):**
  - **G-2 → S5:** actual construction of a forceable non-pointwise endpoint \(\Phi_B\) and proof of (S5‑UE)/(S5‑LOC) with δ-uniform constants remains OPEN.【638:11†CR_master_dashboard_v35_locked.md†L30-L37】
  - **G-1 / G-12:** residual envelope constant provenance/citations remain OPEN and must be ported into the chosen \(\Phi_B\) endpoint class.【638:11†CR_master_dashboard_v35_locked.md†L7-L18】

* **Key conclusions (≤5 bullets):**
  1. The correct S5 feasibility condition is **not** “p>1,” but the explicit budget inequality \(2(p-\theta)\ge q\) for the chosen \(\Phi_B\)-local growth model \(G(n)\sim n^q\).
  2. Any endpoint class whose local interface retains \(\theta=1\) and \(G(n)\gtrsim n\) forces \(p\ge 3/2\), i.e. it is dead-on-arrival unless a genuinely stronger UE mechanism is proven.
  3. The two roadmap directions (“energy/L2” and “avoid collar blow-up”) are budget-viable only if they explicitly reduce \(\theta\) and/or reduce growth \(q\) (e.g., square-summed \(G(n)\sim n^{1/2}\)).
  4. κ-admissible shrinking is safe for S5 only if \(p-\theta\ge 0\); otherwise shrinking δ can worsen the envelope term and the admissibility policy must be redesigned.
  5. v36+ should adopt the “S5 acceptance criterion” remark so future endpoint experiments cannot silently mismatch forcing, constants, or exponent budgets.

* **Paste-ready manuscript edits (TeX blocks):**
  (i) revised lemma/proposition statements  
  (ii) revised definitions/remarks  
  (iii) revised theorem/inequality lines  

  **(i) Add a new theorem in the S5 section (or immediately after v35 Theorem 10.12) (TeX):**
  ```tex
  \begin{theorem}[S5 Budget Theorem (general endpoint functional)]
  \label{thm:S5-budget}
  Assume a redesigned endpoint $\Phi_B$ and exponents $p>0$, $\theta\ge 0$ satisfy
  \[
    D_B(W)\le C_{\rm up}\,\delta^{p}\,\Phi_B(E'/E),
  \]
  and
  \[
    \Phi_B(Z'_{\rm loc}/Z_{\rm loc})\le C_{\rm loc}\,\delta^{-\theta}\,G(N_{\rm loc}(m),\kappa),
  \]
  uniformly for all $m\ge 10$, $\alpha\in(0,1]$, and all $\kappa$--admissible $0<\delta\le \delta_0(m,\alpha)=\eta\alpha/(\log m)^2$,
  with δ-uniform constants.
  If $G(n,\kappa)\ll \kappa^{-u}n^q$ and $N_{\rm loc}(m)\ll \log m$, then the local penalty at the nominal scale
  behaves as $\eta^{p-\theta}(\log m)^{q-2(p-\theta)}$.
  In particular, uniform $\eta$--shrinking control of the local penalty is possible only if $2(p-\theta)\ge q$,
  and it is shrinkable as $\eta\downarrow 0$ whenever additionally $p-\theta>0$.
  Moreover $\kappa$--admissible shrinking $\delta\le\delta_0$ is monotone-safe provided $p-\theta\ge 0$.
  \end{theorem}
  ```

  **(ii) Add the “S5 acceptance criterion” remark (provided above) near the start of §S5:**
  ```tex
  % Insert Remark \ref{rem:S5-accept} as written above
  ```

  **(iii) Add a short NO-GO remark for naive endpoint classes (optional, but drift-preventing):**
  ```tex
  \begin{remark}[NO-GO for naive endpoints that retain $\theta=1$]
  If a proposed endpoint class yields a local interface with $\theta=1$ and $G(n,\kappa)\gtrsim n$,
  then Theorem~\ref{thm:S5-budget} forces $p\ge 3/2$ for uniform $\eta$--shrinking under $\delta_0=\eta/(\log m)^2$.
  Such endpoints should be treated as non-viable unless a proof of $p\ge 3/2$ in that same endpoint class is supplied.
  \end{remark}
  ```

* **Dependencies on other branches:**
  - **RH-ENVELOPE / RH-LOCAL:** must propose explicit \(\Phi_B\) candidates with proved exponents \((p,\theta)\) and an explicit growth model \(G\) (including whether \(G\) is linear in \(N_{\rm loc}\) or square-summed).  
  - **RH-FORCE:** must provide forceability link for \(\Phi_B\): either \(\Phi_B\ge D_B(W)\) or a new forcing lemma lower-bounding \(\Phi_B\) directly (as already required by v35 Remark 12.1).【638:2†manuscript_v35.pdf†L26-L33】

* **Referee risk notes:**
  1. **Normalization ambiguity:** If \(\Phi_B\) is not δ-normalized/shape-invariant, exponents \(p,\theta\) become gauge-dependent. The acceptance criterion fixes this by requiring a δ-normalized definition and explicit exponent tracking.  
  2. **κ-policy hazard:** If an S5 design yields \(p-\theta<0\), the old admissible-shrink lemma becomes invalid (shrinking δ worsens the envelope term). This must be checked explicitly for every proposed endpoint.  
  3. **Hidden δ-dependence:** All constants in S5-UE/S5-LOC must be δ-uniform; otherwise “η‑shrinking” can be illusory (miracle inequality failure mode). The theorem and acceptance remark require uniformity in the quantified hypotheses.
