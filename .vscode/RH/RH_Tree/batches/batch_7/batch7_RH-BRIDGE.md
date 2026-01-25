# Batch 7 — RH-BRIDGE

**Ground truth:** v37 locked build.  
**Callsign:** RH-BRIDGE  
**Mission:** Bridge engineering for the *phase/winding endpoint class* so it is (i) mathematically clean, (ii) δ-scaled correctly, and (iii) composable with ENVELOPE’s endpoint functional without hidden point-evaluation leakage.

---

## 0) Executive verdict (what is solid vs what remains open)

### What is already *truth-grade* in v37 (Bridge-side)
1. **Forceability gate is explicit**: any endpoint redesign is invalid unless it either dominates the forced dial deviation \(D_B(W)\) or comes with a new forcing lemma. (v37 Remarks 12.5–12.7.)
2. **Phase increment toolkit is sound**: \(\Delta_\Gamma \arg f := \Im\int_\Gamma (f'/f)\,dv\) with correct “parentheses hygiene” on non-horizontal arcs. (v37 Def. 12.8, Lemma 12.9, Remark 12.10.)
3. **Buffered phase forcing exists**: if \(W\) has a zero in the buffered inner box \(B_{\kappa/2}\), then \(\widetilde D_B(W)\ge \pi/2\). (v37 Def. 12.16, Lemma 12.17.)  
   This is a *new forcing lemma* (forceability gate (ii)), so it can replace the “domination transfer” requirement for \(D_B\).

### What remains open (and is *not* Bridge-fixable alone)
- The **local phase δ-inertness** in Lemma 12.14 / Cor. 12.15 is still the core obstruction: without additional structure (e.g. micro-window / pair-isolation), local zeros can contribute \(O(1)\) phase per zero, so the “upper envelope” side cannot be made \(<\pi/2\) uniformly just by shrinking \(\delta\).

Bridge can, however, (i) ensure the endpoint class is *cleanly defined on a collar* (no hidden boundary regularity assumptions), and (ii) give a *refined per-zero phase bound* that exposes exactly what “pair-isolation” must prove.

---

## 1) Task A — Clean bridge chain from forcing to ENVELOPE’s \(\Phi_B(E'/E)\)

### 1.1 Mini-DAG (v-frame)

Below is the cleanest DAG that is faithful to v37 and makes the logic composable:

**Node 0 (setup):**
- Aligned square box  
  \(B = B(\alpha,m,\delta)=\{v:\ |\Re v-\alpha|\le \delta,\ |\Im v-m|\le \delta\}\).
- \(\kappa\)-admissibility / boundary-contact:  
  \(\operatorname{dist}(\partial B,\mathcal Z(E))\ge \kappa\delta\).
- Buffered inner square  
  \(B_{\kappa/2}:=\{v\in B:\ \operatorname{dist}(v,\partial B)\ge \kappa\delta/2\}\).
- Outer factor \(G_{\rm out}\) (Dirichlet) and inner quotient \(W:=E/G_{\rm out}\) are defined on \(B^\circ\).

**Node 1 (forced endpoint — pick one):**
- **Legacy forcing (S5)** forces the *dial deviation* \(D_B(W)\) by an \(O(1)\) constant (Section 8; v37 Remarks 12.5–12.7).  
  This is *not automatically usable* if ENVELOPE replaces \(D_B(W)\) by a new endpoint.
- **New forcing (S5′)** forces the *phase endpoint* directly:  
  If \(W\) has a zero in \(B_{\kappa/2}\), then  
  \[
  \widetilde D_B(W)\ :=\ \max_{S\subset\partial B_{\kappa/2}}\left|\Delta_S \arg W\right|\ \ge\ \frac{\pi}{2}.
  \]
  (v37 Def. 12.16, Lemma 12.17.)  
  This is the clean “forceability gate (ii)” route.

**Node 2 (endpoint-to-envelope identity):**
For each side \(S\subset\partial B_{\kappa/2}\),
\[
\Delta_S\arg W \;=\;\Im\int_S \frac{W'}{W}\,dv.
\]
This is purely *boundary integration* (no point evaluation).

**Node 3 (link to \(E'/E\) and the residual/local split):**
Since \(W=E/G_{\rm out}\),
\[
\frac{W'}{W}=\frac{E'}{E}-\frac{G_{\rm out}'}{G_{\rm out}}.
\]
Also, in the *height-local split* \(E = F\cdot Z_{\rm loc}\),
\[
\frac{E'}{E}=\frac{F'}{F}+\frac{Z_{\rm loc}'}{Z_{\rm loc}}.
\]
Thus any ENVELOPE functional \(\Phi_B(E'/E)\) that is built from log-derivative data should, at minimum, be compatible with the decomposition:
\[
\Delta_S\arg W
=\Im\int_S \frac{F'}{F}\,dv
+\Im\int_S \frac{Z_{\rm loc}'}{Z_{\rm loc}}\,dv
-\Im\int_S \frac{G_{\rm out}'}{G_{\rm out}}\,dv.
\]

**Node 4 (what is currently provable in v37 without new ideas):**
- **Residual phase budget (δ-uniform):** on short vertical segments inside \(B\),
  \[
  \left|\Delta_{I_{+,\lambda}}\arg F\right|\ \le\ 2\delta\,(C_1\log m+C_2)
  \]
  (v37 Cor. 12.13, from Lemma 12.12 + Lemma 7.2).
- **Local phase is δ-inert (current upper bound):**
  \[
  \left|\Delta_{I_+}\arg Z_{\rm loc}\right|\ \le\ \pi\,N_{\rm loc}(m)
  \]
  (v37 Lemma 12.14).
- **Prototype bound (residual + local):**
  \[
  |\Delta_{I_{+,\lambda}}\arg E|
  \ \le\ 2\delta(C_1\log m+C_2)+|\Delta_{I_{+,\lambda}}\arg Z_{\rm loc}|
  \]
  (v37 Cor. 12.15).

**Node 5 (what must be supplied by ENVELOPE/LOCAL for closure):**
To make S5′ composable with the “budget theorem”, one must bound the *local phase term* on the relevant boundary arc by something **with positive δ-power** (or prove a structure lemma that only \(O(1)\) local zeros contribute \(O(1)\) phase, the rest contributing \(O(\delta)\)). This is the micro-window / pair-isolation obligation.

---

## 2) Task B — Strict δ-scaling audit (no hidden losses)

### 2.1 Where δ enters (and where it does **not**)
- In the phase endpoint class, δ enters **only** through:
  - **arc length**: each side of \(\partial B_{\kappa/2}\) has length \(2\delta(1-\kappa/2)\sim \delta\),
  - **collar thickness**: \(\partial B_{\kappa/2}\) sits at distance \(\kappa\delta/2\) from \(\partial B\),
  - **shift offsets**: \(I_{+,\lambda}\) is an interior segment at a fixed horizontal offset of order \(\delta\).

There is **no** “evaluation operator norm” step of the form  
\(|h(v_0)|\le C\,\delta^{-1/2}\|h\|_{L^2(\partial B)}\), which is exactly the scaling loss that killed the old UE pointwise approach (cf. v37 Lemma 10.3 explicitly uses such a step).

### 2.2 “No absolute \(L^r\)” compliance
- The phase increments \(\Delta_S\arg(\cdot)\) are **signed integrals** \(\Im\int (f'/f)\,dv\), not absolute norms.
- Any step that upper bounds \(|\Im\int_S(\cdot)\,dv|\) by \(\int_S |(\cdot)|\,|dv|\) would *re-enter* an absolute endpoint class.  
  This is precisely the type of reduction v37 flags as a NO-GO class (Remark 12.4 / Lemma 12.19 / Prop. 12.20).

**Bridge-side rule (for v38):** every envelope inequality for the phase endpoint class must be written to avoid “\(|\int|\le\int|\cdot|\)” as the decisive bound, unless it is explicitly marked as falling into the rejected absolute-\(L^r\) class.

---

## 3) Task C — Legacy scan hook (optional, exploratory)

**Exploratory only (do not promote to core spine without a forcing transfer lemma):**

Early versions used “left/right column canonical objects”, e.g. FE-symmetric quotients like
\[
G(v):=\frac{E(1+v)}{E(1-v)}.
\]
A phase endpoint of argument-principle type applied to \(G\),
\[
\Phi_B^{(G)} := \max_{S\subset\partial B_{\kappa/2}}|\Delta_S\arg G|,
\]
would “collapse to the canonical object” if one can show \(G\) is nearly constant (or inner) on admissible boxes.

**Caution:** unless forcing is shown to lower-bound \(\Phi_B^{(G)}\) (either by domination of \(D_B\) or a fresh forcing lemma), it cannot replace the forced endpoint class.

---

## 4) S6 Harness check — explicit-formula interpretation

### Frame map (must be explicit)
- \(s\)-frame: \(s=\sigma+it\), nontrivial zero \(\rho=\beta+i\gamma\).
- \(u\)-frame (width–2): \(u=2s\), so \(u_\rho=2\beta+i\,2\gamma\).
- \(v\)-frame (centered): \(v=u-1\), so
  \[
  v_\rho = (2\beta-1) + i\,2\gamma.
  \]
Off-critical-line means \(\beta\neq \tfrac12 \iff \Re(v_\rho)\neq 0\).

### Does a phase endpoint correspond to an \(x^\beta\) “amplitude leak”?
**Not directly.** A boundary phase endpoint \(\widetilde D_B(\cdot)\) is a *local analytic witness* of a zero (via winding/argument principle), not an explicit-formula amplitude functional on primes.

Conceptual link (allowed): off-axis zeros create \(x^\beta\)-weighted oscillatory terms in explicit formulas (e.g., \(\psi(x)\)). The phase endpoint is “spectral presence” information about such zeros in the \(v\)-plane. But it is not, by itself, an amplitude observable on the prime side unless an additional transfer lemma is proved.

---

# MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* Prompt Batch Number: 7
* Callsign: RH-BRIDGE
* Result classification: CONDITIONAL
* Target gaps closed (by ID):
  - **G-6 (phase-endpoint Bridge hygiene)**: adding explicit “collar nonvanishing” hypotheses for phase increments on \(\partial B_{\kappa/2}\) and fixing a notation bug in Definition 12.11’s parenthetical.
  - **G-10 (label/wording integrity near phase toolkit)**: patching the “distance to boundary” parenthetical so it is mathematically correct.
* Target gaps still open (by ID):
  - **G-2b (forcing ↔ endpoint alignment)** if the program insists on keeping \(D_B(W)\) as the forced object. (If S5′ adopts Lemma 12.17 forcing of \(\widetilde D_B\), this is resolved by design.)
  - **G-4′ / G-8 (δ-exponent + local interface for phase class)**: the local phase term is δ-inert unless pair-isolation/micro-window structure is proven.
* Key conclusions (≤5 bullets):
  1. The phase endpoint class introduces **no point-evaluation loss**; δ enters only through arc-length and collar geometry.
  2. Any “upper envelope” proof that collapses to an **absolute** \(L^r\) control of \(|E'/E|\) is already a NO-GO class; phase endpoints must avoid that reduction.
  3. The clean forced endpoint for S5′ is \(\widetilde D_B(W)\) via **Lemma 12.17** (new forcing lemma), not by attempting to dominate legacy \(D_B(W)\).
  4. The only remaining mathematical obstruction is the **local phase term**: current truth-grade bounds are \(O(1)\) per local zero.
  5. A refined “per-zero phase bound” lemma makes the pair-isolation obligation explicit: zeros with horizontal separation \(\gg \delta\) contribute \(O(\delta)\) phase, while the near pair contributes \(O(1)\).

* Paste-ready manuscript edits (TeX blocks):

  **(i) revised lemma/proposition statements**

```tex
% Place immediately after Definition 12.16 (Buffered boundary phase endpoint).

\begin{lemma}[Collar nonvanishing for phase arcs]\label{lem:phase_collar_nonvanishing}
Let $B=B(\alpha,m,\delta)$ be an aligned box and assume $\kappa$--admissibility:
\[
\dist(\partial B,\mathcal Z(E))\ge \kappa\delta.
\]
Let $B_{\kappa/2}:=\{v\in B:\dist(v,\partial B)\ge \kappa\delta/2\}$.
Then there exists $r=r(\kappa,\delta)>0$ (e.g. $r=\kappa\delta/4$) such that
\[
\dist(\partial B_{\kappa/2},\mathcal Z(E))\ge r.
\]
In particular, $E$ is holomorphic and nonvanishing on an open $r$--neighborhood of
$\partial B_{\kappa/2}$, and for every side $S\subset \partial B_{\kappa/2}$ the phase
increment $\Delta_S \arg E$ (Definition~\ref{def:phase_increment}) is well-defined.

If $G_{\rm out}$ is the Dirichlet outer factor on $B$ and $W:=E/G_{\rm out}$, then $G_{\rm out}$
is holomorphic and zero-free on $B^\circ$, hence $W$ is holomorphic on $B^\circ$ and also
nonvanishing on an open neighborhood of $\partial B_{\kappa/2}$. Consequently
$\Delta_S\arg W$ is well-defined for every side $S\subset\partial B_{\kappa/2}$.
\end{lemma}

\begin{lemma}[Refined kernel phase bound on a vertical segment]\label{lem:phase_kernel_refined}
Let $x_0\in\mathbb R$, $\delta_*>0$, and let $I(x_0;\delta_*):=\{x_0+iy:\ |y-m|\le \delta_*\}$
be oriented upward. Let $\rho=x_\rho+i y_\rho\notin I(x_0;\delta_*)$ and set $d:=|x_0-x_\rho|$.
Then
\[
\left|\Im\int_{I(x_0;\delta_*)}\frac{dv}{v-\rho}\right|
= \Big|\arg(x_0+i(m+\delta_*)-\rho)-\arg(x_0+i(m-\delta_*)-\rho)\Big|
\le 2\arctan\!\Big(\frac{\delta_*}{d}\Big)
\le \min\!\Big(\pi,\frac{2\delta_*}{d}\Big),
\]
with the convention that the right-hand side is $\le \pi$ when $d=0$.
\end{lemma}
```

  **(ii) revised definitions/remarks**

```tex
% Fix Definition 12.11 parenthetical (current text says distance ~ lambda*delta, but the
% distance to the nearest vertical boundary is (1-lambda)*delta for B=[alpha-delta,alpha+delta].

\begin{definition}[Shifted near-vertical segment]\label{def:shifted_segment}
Let $B=B(\alpha,m,\delta)$ be an aligned box and let $\lambda\in(0,1)$.
Define the shifted segment
\[
I_{+,\lambda}:=\{\alpha+\lambda\delta+iy:\ |y-m|\le \delta\},
\]
oriented upward.  (This lies strictly inside $B$. Its distance to the right vertical side
$\{\alpha+\delta+iy\}$ is $(1-\lambda)\delta$.)
\end{definition}
```

  **(iii) revised theorem/inequality lines**

```tex
% Optional: insert after Corollary 12.15 to expose the pair-isolation obligation.

\begin{remark}[Phase-local contributions: what must be proved for closure]\label{rem:phase_pair_isolation}
Lemma~\ref{lem:phase_kernel_refined} shows that a zero $\rho$ contributes $O(\delta_*/d)$ to the
phase increment on a vertical segment at horizontal separation $d$.
Thus, to make a phase endpoint shrink with $\delta$ (and satisfy the budget condition
$p-\theta\ge 1/2$), it suffices to prove a structural lemma of the form:
all but $O(1)$ zeros in $\mathcal Z_{\rm loc}(m)$ have horizontal separation $d\gg \delta$ from the
endpoint contour, so their total phase contribution is $O(\delta\log m)$.
\end{remark}
```

* Dependencies on other branches:
  - **ENVELOPE / LOCAL** must decide (i) whether the forced endpoint is switched to \(\widetilde D_B\) (Lemma 12.17), and (ii) what structural lemma (pair-isolation / micro-window) will replace the δ-inert local phase bound.
  - **FORCE** must confirm the forcing lemma used in the contradiction is either the legacy \(D_B(W)\) chain or the new Lemma 12.17 chain; Bridge can support either but the manuscript must pick one.

* Referee risk notes (anticipated objections + how addressed):
  1. **“Phase increment requires a zero-free neighborhood, not just pointwise nonvanishing.”** Addressed by Lemma~\ref{lem:phase_collar_nonvanishing}, which provides an explicit collar radius.
  2. **Ambiguity in Definition 12.11 parenthetical (“distance ~ λδ”).** Patched to the correct distance \((1-\lambda)\delta\).
  3. **Hidden point-evaluation leakage.** The phase endpoint chain uses only path integrals of \(f'/f\), not boundary-to-point evaluation bounds.
  4. **Absolute-\(L^r\) reductions sneaking back in via \(|\int|\le\int|\cdot|\).** Explicitly flagged as a NO-GO reduction route per v37 Remark 12.4; Bridge recommends keeping all phase endpoints as signed integrals unless the manuscript declares it is entering the rejected class.
