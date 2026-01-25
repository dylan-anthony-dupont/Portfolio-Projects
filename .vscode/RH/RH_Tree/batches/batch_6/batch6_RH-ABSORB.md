# Batch‑6 Global Header (for all branch messages)

**PROGRAM:** RH Convergence Program  
**LINE IN THE SAND:** v35/v36 truth‑latching. No drift.  
**CURRENT FRONTIER:** **S5′ = boundary phase endpoint (Δarg / ∫Im(log‑derivative))** that is **forceable** and has **δ‑uniform upper control** without pointwise UE, without absolute (L^r) endpoints, and without projection‑kill tricks that break forceability.

**Batch‑6 outputs must be decision‑grade:** PASS / FAIL / CONDITIONAL with explicit reasons and paste‑ready TeX blocks.

### Guardrails (non‑negotiable, already locked in v36)

1. **No pointwise UE** (disc‑based / dial evaluation / “recover δ^{3/2}”).
2. **No absolute (L^r(\partial B)) endpoints on (|E'/E|)** (dead by v36 NO‑GO class).
3. **No projection endpoints that annihilate local span unless you also redesign forcing** (projection NO‑GO).
4. **Forceability Gate:** Any new endpoint is invalid unless it either:
   * dominates the forced endpoint, or
   * comes with a new forcing lemma targeting it.

### Frame mapping (must be consistent)

* **s‑frame:** s=\sigma+it (critical strip).
* **u‑frame (width‑2):** u=2s. Then ζ(s)=ζ(u/2).
* **v‑frame (centered):** v=u−1, so u=1+v and s=(1+v)/2.
* A nontrivial zero ρ=β+iγ in s‑frame corresponds to u_ρ=2β+i·2γ and v_ρ=(2β−1)+i·2γ.
* **Off‑critical‑line means:** β≠1/2 ⇔ Re(v_ρ)≠0.
* “Height” in v‑frame is Im(v)=2γ (do not tie “height” to β=1/2 in definitions).

### Explicit‑formula interpretation (S6 harness check)

At the end: state whether your endpoint corresponds to an x^β amplitude leak and why.

---

# Batch 6 — RH‑ABSORB

**Callsign:** RH‑ABSORB  
**Role in Batch‑6:** close the *logical spine* for S5′ by turning a proposed **forceable boundary phase endpoint** into a **proof‑grade closure criterion**, or else deliver a clean **NO‑GO lemma** that kills the endpoint class.

Ground truth is **v36**. Key gates are already explicit:
- Forceability gate (Lemma 12.4 + Remark 12.5).
- Baseline NO‑GO: absolute L^r log‑derivative endpoints (Lemma 12.6 + Proposition 12.7).
- Baseline NO‑GO: projection endpoints (Lemma 12.9).

This response is written as a v37‑ready insertion package: it does **not** attempt to re‑audit BRIDGE, and it does **not** assume any unproved UE exponent.

---

## 1) Closure criterion template for S5′ endpoints (TeX‑ready)

### 1.1 Data: what S5′ must provide (inputs from FORCE/ENVELOPE/LOCAL)

Fix κ∈(0,1/10) and η∈(0,1). For each (m,α) with m≥10 and α∈(0,1], define the nominal scale
\[
\delta_0(m,\alpha)=\frac{\eta\alpha}{(\log m)^2}.
\]
Let B=B(\pm a,m,\delta) be a κ‑admissible aligned box and W the boundary quotient (as in v36).

An S5′ proposal must provide a boundary endpoint functional
\[
\widetilde D_B = \widetilde D_B(W)\quad(\text{built from boundary phase / }\Delta\arg / \Im(\log\text{-derivative)}),
\]
together with **two inequalities**:

**(S5′‑FORCE)** (forceability) Under an off‑axis quartet at height m with displacement a>0, there exists an aligned κ‑admissible box B (with α≈a) such that
\[
\widetilde D_B(W)\ \ge\ c_{\mathrm{force}}-\delta\,\Xi(m)
\]
for some absolute c_force>0 and some explicit nonnegative function Ξ(m) (constant‑limited forcing per Lemma 8.2).

**(S5′‑UE+SPLIT)** (δ‑uniform upper control, with local/residual split) For every κ‑admissible aligned box B and its quotient W,
\[
\widetilde D_B(W)\ \le\ C_{\mathrm{up}}\,\delta^{p}\,\Big( \mathrm{Res}(m)\ +\ C_{\mathrm{loc}}\ \delta^{-\theta}\,G(N_{\mathrm{loc}}(m),\kappa)\Big)
\]
with:
- explicit exponent p>0,
- explicit local blow‑up exponent θ≥0,
- **δ‑uniform** constants C_up, C_loc,
- explicit growth model \(G(n,\kappa)\) (e.g. \(G(n,\kappa)\ll \kappa^{-u}n^q\) for fixed u,q≥0),
- an unconditional window majorant \(N_{\mathrm{loc}}(m)\ll \log m\) (v36 already has an explicit bound),
- and a δ‑uniform residual envelope bound \(\mathrm{Res}(m)\ll \log m\) (v36 Lemma 7.2 style).

**Critical point:** in the current architecture forcing is O(1), so **the envelope RHS must become < c_force/2 uniformly in m** after we set δ=δ0(m,α) and choose η small.

---

### 1.2 The closure theorem

> **Theorem (S5′ closure from a forceable phase endpoint + budget‑eligible upper control).**  
> Assume the v36 setup (entire completion E(v), κ‑admissible boxes, boundary quotient W, forcing constant‑limited as in Lemma 8.2).  
> Assume there exists an S5′ endpoint \(\widetilde D_B\) such that (S5′‑FORCE) and (S5′‑UE+SPLIT) hold with δ‑uniform constants and with a growth model
> \[
> G(n,\kappa)\ \le\ C_G\,\kappa^{-u}n^q
> \quad (u,q\ge 0,\ C_G\ge 1\ \text{absolute}).
> \]
> Suppose additionally that the exponents satisfy the **two** budget inequalities
> \[
> 2p\ \ge\ 1\qquad\text{and}\qquad 2(p-\theta)\ \ge\ q,
> \]
> and the strict shrink condition \(p-\theta>0\).
> Then there exists \(\eta_\star=\eta_\star(\kappa,C_{\mathrm{up}},C_{\mathrm{loc}},C_G,u,q,c_{\mathrm{force}})\in(0,1)\) such that for every \(\eta\in(0,\eta_\star]\) the following holds:
> for all \(m\ge 10\) and all \(\alpha\in(0,1]\), setting \(\delta=\delta_0(m,\alpha)\) forces
> \[
> C_{\mathrm{up}}\delta^{p}\Big(\mathrm{Res}(m)+C_{\mathrm{loc}}\delta^{-\theta}G(N_{\mathrm{loc}}(m),\kappa)\Big)
> \ <\ c_{\mathrm{force}}-\delta\,\Xi(m),
> \]
> and hence (by (S5′‑FORCE)) no off‑axis quartet at height m can exist.  
> Consequently, the tail criterion family holds (for all m≥10), and together with any finite‑height front‑end input, RH follows.

**Proof sketch (audit‑grade, no handwaving):**
1. Plug δ=δ0(m,α) into the envelope bound. Use \(\mathrm{Res}(m)\ll \log m\) and \(N_{\mathrm{loc}}(m)\ll \log m\).  
2. The residual term behaves like \(\delta_0^p \log m=\eta^p\alpha^p (\log m)^{1-2p}\), uniformly bounded in m iff 2p≥1.  
3. The local term behaves like
\(\delta_0^{p-\theta}G(N_{\mathrm{loc}},\kappa)\ll \kappa^{-u}\eta^{p-\theta}(\log m)^{q-2(p-\theta)}\),
uniformly bounded in m iff 2(p-θ)≥q, and η‑shrinkable iff p-θ>0.  
4. Forceability is constant‑limited (c_force is O(1)), and the forcing correction \(\delta\Xi(m)\) is δ‑small. Hence choosing η≤η_\star makes the envelope side < c_force/2 while the forcing side ≥ c_force/2 for all m≥10, contradiction.  
5. Therefore no off‑axis quartet exists at any height m≥10; combine with finite front‑end for m<10 to conclude RH.

**Why this is the correct “closure spine”:** it explicitly exposes the *only* way to beat constant‑limited forcing: a strict exponent gain \(p-\theta>0\) plus the uniformity inequalities \(2p\ge1\) and \(2(p-\theta)\ge q\). This is the non‑drifting, referee‑acceptable replacement for the older absorption narrative.

---

## 2) Budget extraction for boundary phase endpoints (what survives; what dies)

This section converts “phase endpoint vibes” into the exact budget parameters \((p,\theta,q)\). The goal is to prevent future drift into endpoints that *cannot* close under constant‑limited forcing.

### 2.1 NO‑GO: raw Δarg endpoints (no δ‑prefactor)

Consider the naive phase endpoint
\[
\widetilde D_B^{\Delta\arg}(W):=\left|\Delta_{I_+}\arg W\right|
\quad\text{or}\quad
\left|\int_{I_+}\Im\!\Big(\frac{W'}{W}\Big)\,ds\right|
\]
(or any comparable signed phase‑increment endpoint on a boundary segment of length ≍δ).

- **Forceability:** plausible (Z_pair produces a π/2 rotation on the near side; Lemma 8.1).  
- **But UE exponent:** the endpoint is scale‑invariant (dimensionless) and does not naturally supply a δ^p prefactor; the best one can hope for at the “black‑box” level is p=0.  
- **Local term:** each local zero contributes O(1) to the phase increment on a segment, so the local growth is at least q=1 with θ=0 (δ‑inert, ≍N_loc).  
- **Budget check:** fails immediately since 2p≥1 fails (p=0), and also 2(p-θ)≥q becomes 0≥1 (false).

> **Conclusion (NO‑GO):** **pure Δarg endpoints cannot yield uniform tail closure** under the current forcing architecture, unless one also proves a new forcing mechanism whose lower bound grows like log m (ruled out by Lemma 8.2) or proves a nontrivial short‑interval zero bound forcing q=0 (not available).

This is a useful elimination: S5′ cannot be “just take Δarg”. It must be a **phase endpoint with a true δ‑gain** in the envelope inequality *and* a reduced local singularity (θ smaller than p−1/2).

### 2.2 NO‑GO: Cauchy–Schwarz phase bounds that reduce to absolute L^2 collars

A common move is:
\[
|\Delta\arg|\ \le\ |I_+|^{1/2}\,\big\|\Im(W'/W)\big\|_{L^2(I_+)}\ \asymp\ \delta^{1/2}\,\|W'/W\|_{L^2(I_+)}.
\]
This produces a δ^{1/2} prefactor (so p=1/2), but the local kernels still have L^2 size ≍δ^{-1/2}, so θ=1/2 and the local term remains δ‑inert (p−θ=0). This is the exact same mechanism behind the v36 NO‑GO for absolute L^r endpoints, just in “phase clothing.”

> **Conclusion (NO‑GO):** any S5′ endpoint whose UE step is ultimately reduced to an **absolute L^2 collar estimate** inherits θ=p and cannot close.

### 2.3 What a viable S5′ phase endpoint must accomplish (the only surviving design target)

To pass the budget in §1.2 under the nominal scale δ0=ηα/(log m)^2 with N_loc(m)≍log m, an S5′ phase endpoint must achieve:

- **A real δ‑gain:** \(p\ge 1/2\) (to suppress the residual \(\log m\) term), and  
- **A local‑singularity improvement:** \(p-\theta\ge 1/2\) (to suppress local growth), i.e.
  \[
  \theta\ \le\ p-\tfrac12.
  \]

Given v36’s baseline collar bound has θ=1 pointwise and θ(r)=1−1/r for absolute L^r collars, the only plausible routes are exactly those noted in v36 Remark 12.8:

1. **Cancellation endpoints** (argument‑principle / signed / commutator structure) that reduce the effective θ below the absolute collar scaling; and/or  
2. **Less singular boundary objects** (BMO / Carleson / fractional Sobolev endpoints) for which each local Cauchy kernel has bounded endpoint norm (θ≈0) even though its pointwise size is δ^{-1}.

This is where S5′ legitimately lives: not in “Δarg as such,” but in a **phase endpoint class whose functional analysis lowers θ**.

---

## 3) Decision and the single missing analytic lever

### 3.1 Status

- The **logical closure criterion** is now explicit and proof‑grade (§1.2).  
- The **endpoint viability conditions** for phase‑type proposals are explicit (§2.3).

### 3.2 What is missing (one decisive lever)

To make S5′ a real closure route (not just a design note), the program still needs **one of** the following to be proved (and either one would be decisive):

**Missing Lever (preferred):** an S5′ endpoint class \(\Phi_B\) for which the *local term* satisfies a bound with θ ≤ p−1/2 (ideally θ=0) **without** sacrificing forceability (Lemma 12.4/Remark 12.5).  
Concretely, the missing lemma has the form:
\[
\Phi_B\!\left(\frac{Z'_{\mathrm{loc}}}{Z_{\mathrm{loc}}}\right)\ \le\ C\,\kappa^{-u}\,N_{\mathrm{loc}}(m)^q
\quad\text{with }\theta=0\text{ inside the S5′ split,}
\]
in an endpoint class that still admits an UE inequality \(DB(W)\le C_{\mathrm{up}}\delta^p\Phi_B(E'/E)\) with p≥1/2.

If ENVELOPE/LOCAL can supply this single lemma (together with the corresponding UE inequality in the same endpoint class), the closure theorem in §1.2 becomes *live*.

---

## 4) v37 “S5′ acceptance gate” remark (paste‑ready; prevents drift)

Below is a paste‑ready remark to insert near v36 Remark 12.1–12.8 (start of the S5 section). It hard‑codes the S5′ phase‑endpoint acceptance test.

---

## 5) S6 harness check: explicit formula interpretation

**Does S5′ correspond to an x^β amplitude leak?**  
Yes, but only indirectly: any successful S5′ closure proves **no off‑critical‑line zeros**, i.e. RH. Under RH, classical explicit‑formula consequences hold (e.g. \( \psi(x)=x+O(x^{1/2}\log^2 x)\)), and any β>1/2 would yield an \(x^\beta\) amplitude contribution in ψ(x) (the “amplitude leak”).

**Is that implication RH‑equivalent?**  
Yes: a bound of the form \( \psi(x)=x+O(x^{1/2+\varepsilon})\) for all ε>0 is RH‑equivalent. The S5′ endpoint is an *analytic detector* for off‑axis zeros rather than a direct prime‑counting estimate, but if it succeeds it collapses to the usual RH‑equivalent explicit‑formula regime.

---

# MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* Callsign: RH‑ABSORB
* Result classification: CONDITIONAL
* Target gaps closed (by ID):
  - **Closes the logical/formal “S5′ closure criterion” gap** (budget theorem instantiated for phase endpoints; drift‑proof closure statement).
* Target gaps still open (by ID):
  - **S5′‑UE** (new non‑pointwise UE inequality with p≥1/2 in a non‑NO‑GO endpoint class)
  - **S5′‑LOC** (local interface in the same endpoint class with θ≤p−1/2, ideally θ=0)
  - **S5′‑FORCE** (either domination \(\widetilde D_B\ge DB(W)\) or a new forcing lemma lower‑bounding \(\widetilde D_B\))
* Key conclusions (≤5 bullets):
  1. Constant‑limited forcing means any closure must shrink the envelope side below an O(1) constant uniformly in m.
  2. For nominal δ0=ηα/(log m)^2 and N_loc(m)≍log m, uniform closure requires **both** 2p≥1 (residual control) and 2(p−θ)≥q (local control), with p−θ>0 for η‑shrink.
  3. Pure phase‑increment endpoints (raw Δarg / ∫Im(log‑derivative)) have p=0 and cannot close (NO‑GO).
  4. Any phase endpoint that reduces to an **absolute** L^2 collar estimate also fails (p=θ, δ‑inert local term).
  5. The only plausible surviving S5′ route is a phase endpoint with genuine cancellation / less‑singular boundary object so that θ drops below p−1/2 while forceability is preserved.
* Paste‑ready manuscript edits (TeX blocks):

  (i) **Revised lemma/proposition statements**
  ```tex
  % --- Insert in Section 12 (S5 frontier), after Remark 12.5 ---
  \begin{theorem}[S5$'$ closure from a forceable phase endpoint]\label{thm:S5prime-closure}
  Fix $\kappa\in(0,1/10)$ and $\eta\in(0,1)$ and define $\delta_0(m,\alpha)=\eta\alpha/(\log m)^2$.
  Let $\widetilde D_B$ be a boundary phase endpoint functional assigned to each $\kappa$--admissible
  aligned box $B=B(\pm a,m,\delta)$ and its boundary quotient $W$.
  Assume:
  \begin{enumerate}
    \item[(S5$'$--FORCE)] Under an off-axis quartet at height $m$ with displacement $a>0$,
    there exists an aligned $\kappa$--admissible box $B$ (with $\alpha\approx a$) such that
    $\widetilde D_B(W)\ge c_{\rm force}-\delta\,\Xi(m)$ with $c_{\rm force}>0$ absolute and
    $\Xi(m)\ge 0$ explicit.
    \item[(S5$'$--UE+SPLIT)] For every $\kappa$--admissible aligned box,
    \[
      \widetilde D_B(W)\le C_{\rm up}\,\delta^p\Big(\mathrm{Res}(m)+C_{\rm loc}\,\delta^{-\theta}\,G(N_{\rm loc}(m),\kappa)\Big),
    \]
    where $p>0$, $\theta\ge 0$, and $C_{\rm up},C_{\rm loc}$ are $\delta$--uniform, and
    $G(n,\kappa)\le C_G\,\kappa^{-u}n^q$ for fixed $u,q\ge 0$.
  \end{enumerate}
  Suppose additionally that $2p\ge 1$, $2(p-\theta)\ge q$, and $p-\theta>0$.
  Then there exists $\eta_\star\in(0,1)$ (depending on the displayed constants and $\kappa$) such that
  for every $\eta\in(0,\eta_\star]$ the S5$'$ tail inequality holds at $\delta=\delta_0(m,\alpha)$
  for all $m\ge 10$ and all $\alpha\in(0,1]$, and hence no off-axis quartet exists at any height $m\ge 10$.
  Combined with any finite-height front-end, this implies RH.
  \end{theorem}
  ```

  (ii) **Revised definitions/remarks**
  ```tex
  % --- Insert near Remark 12.1 (acceptance criterion) ---
  \begin{remark}[S5$'$ acceptance gate for phase endpoints (no drift)]\label{rem:S5prime-gate}
  Any proposed S5$'$ endpoint built from boundary phase data (e.g.\ $\Delta\arg$ or an integral of
  $\Im(\log\text{-derivative})$) must declare its exponent budget data $(p,\theta,q)$ in the
  schematic bound
  \[
    \widetilde D_B(W)\le C_{\rm up}\,\delta^p\Big(\mathrm{Res}(m)+C_{\rm loc}\,\delta^{-\theta}\,G(N_{\rm loc}(m),\kappa)\Big),
  \]
  and must satisfy the uniformity/shrink conditions of Theorem~\ref{thm:S5prime-closure}:
  $2p\ge 1$, $2(p-\theta)\ge q$, and $p-\theta>0$.
  Pure $\Delta\arg$ endpoints have $p=0$ and are rejected. Any phase endpoint whose proof reduces
  to an absolute $L^r(\partial B)$ estimate for $E'/E$ is also rejected by Lemma~12.6 and
  Proposition~12.7.
  \end{remark}
  ```

  (iii) **Revised theorem/inequality lines**
  ```tex
  % --- Optional insertion in the S5 introduction paragraph ---
  % (This line forces any S5' proposal to carry explicit budget metadata.)
  \noindent\textbf{S5$'$ truth spine.}\;
  Under constant-limited forcing (Lemma~8.2), a uniform tail closure can occur only if the redesigned
  endpoint achieves an exponent budget gain $p-\theta\ge 1/2$ (and $p\ge 1/2$ for the residual term)
  at the nominal scale $\delta_0=\eta\alpha/(\log m)^2$.
  ```
* Dependencies on other branches:
  - **RH‑FORCE:** either (i) domination proof \(\widetilde D_B\ge DB(W)\) or (ii) a new forcing lemma that lower‑bounds \(\widetilde D_B\) directly (per v36 Remark 12.5).
  - **RH‑ENVELOPE:** an S5′‑UE inequality in the proposed endpoint class with explicit p≥1/2 and δ‑uniform constants.
  - **RH‑LOCAL:** a local interface bound in the *same endpoint class* with θ≤p−1/2 (ideally θ=0) and explicit dependence on κ and N_loc.
  - **CR / integration:** confirm lemma numbering/placement in v37; ensure the repro‑pack schema records endpoint metadata (already started in v36 patchlog).
* Referee risk notes (anticipated objections + how addressed):
  - **“Where did 2p≥1 come from?”** It is the residual log‑growth budget: \(\delta_0^p\log m\) is uniformly bounded only if 1−2p≤0. Theorem statement makes it explicit (no hidden steps).
  - **“This seems to assume cancellation.”** It does not assume it; it isolates the *only* viable path: lowering θ below the absolute collar exponent. Without that lemma, result remains CONDITIONAL.
  - **“Forceability might break.”** Explicitly gated: S5′ endpoints are invalid unless domination or a new forcing lemma is proved (v36 Remark 12.5). The patch preserves that gate.
  - **“Endpoint class ambiguity.”** The patch forces every proposal to declare (p,θ,q) and thus becomes machine‑auditable under the v36 repro‑pack schema (prevents drift).
