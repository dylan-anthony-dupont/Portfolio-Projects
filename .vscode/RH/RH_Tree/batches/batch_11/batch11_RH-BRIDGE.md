# Batch 11 — RH-BRIDGE  
**Mechanism selected (required): (A) Pair isolation.**  
Goal: convert the v40→v41 geometry pivot **OPEN-GEO** into a manuscript-ready closure spine:  
**forcing + UE + resonance-handling ⇒ a(m)=0 ⇒ PHU ⇒ RH**.

---

## (1) One-page dependency map (strict order; each lemma stated in one line)

**Pre-gate (why OPEN-GEO is needed):**

- **NO–GO-Δa-Aligned (v41 patch queue / v41 prebuild):** On aligned boxes \(B(a,m,\delta)\) with nominal coupling \(h=\delta\), the two-sided endpoint \(\Phi^{(2\mathrm{s})}_B(a;h)\) cannot have an \(m\)-independent forcing lower bound; in the quartet toy model it is \(\ll \delta h/a^2\), hence \(o(1)\) at \(\delta=\eta a/(\log m)^2\).  
  *(This is the “aligned forcing bullet is false” latch that necessitates OPEN-GEO.)*

**OPEN-GEO spine (pair-isolation route):**

1. **GEO-1 (Witness family / open geometry):** For each off-axis quartet parameter pair \((a,m)\) with \(a>0\), there exists an admissible witness contour/box \(\mathscr B=\mathscr B(a,m,\delta,h)\) (not necessarily aligned) such that all phase integrals defining the endpoint are well-defined on its buffered boundary.

2. **GEO-2 (Pair isolation on the witness contour):** The witness \(\mathscr B\) can be chosen so that, after the required shifts \((v\mapsto v\pm(a\pm h))\), the induced contours have controlled winding around **exactly the forced pair** \(\{\pm a+im\}\) at distance \(\asymp \delta\), while staying a definite distance \(\gg \delta\) from every other zero in the local window (in particular, excluding a near-resonant “tilt-\(a-\varepsilon\)” quartet from the same winding geometry).

3. **FORCE-1 (Phase forcing on \(\Phi^{(2\mathrm{s})}\) via winding):** Under GEO-1–GEO-2 and \(\kappa\)-admissibility, an off-axis quartet at \(\{\pm a\pm im\}\) forces a **constant-limited** lower bound
   \[
   \Phi^{(2\mathrm{s})}_{\mathscr B}(a;h)\ \ge\ c_0,
   \]
   with \(c_0\) absolute (e.g. \(\pi/2\)-type), independent of \((m,a,\delta)\).

4. **UE-1 (Upper envelope bound on \(\Phi^{(2\mathrm{s})}\)):** For all admissible witnesses \(\mathscr B\) at scales \(0<\delta\le\delta_0=\eta a/(\log m)^2\) and couplings \(h\) in the declared policy,
   \[
   \Phi^{(2\mathrm{s})}_{\mathscr B}(a;h)\ \le\ C_{\mathrm{UE}}\;\delta^{p}\,\Phi_B\!\left(\frac{E'}{E}\right)\ +\ \mathrm{Loc}_{a,m}(\delta,h)\ +\ \mathrm{Err}_{a,m}(\delta,h),
   \]
   with \(C_{\mathrm{UE}}\) \(\delta\)-uniform, and **no point-evaluation losses**.

5. **RES-1 (Resonance handling / pair-isolation payoff):** Under the pair-isolation geometry, the “local term” satisfies
   \[
   \mathrm{Loc}_{a,m}(\delta,h)\ \le\ C_{\mathrm{res}}\;\delta\cdot \mathcal R_{a}(m)
   \]
   (or stronger), where \(\mathcal R_{a}(m)\) only counts zeros in a **near-tube** (distance \(\lesssim a\) to the shifted contour). In particular, if \((a,m)\) is chosen as a **minimal tilt** at height \(m\), the near-tube contains only the forced pair, so \(\mathrm{Loc}_{a,m}(\delta,h)=o(1)\) at nominal \(\delta\).

6. **CONTR-1 (Budget contradiction):** Choose \(\delta=\delta_0(m,a)\) and \(h=h(m,a,\delta)\) per policy. Then UE-1+RES-1 gives
   \[
   \Phi^{(2\mathrm{s})}_{\mathscr B}(a;h) \le c_0/2
   \]
   for all sufficiently large \(m\), contradicting FORCE-1. Hence **no off-axis quartet exists at that height**, i.e. \(a(m)=0\).

7. **PHU (height-local reduction):** The width–2 bookkeeping gives: for any nontrivial zero \(\rho=\beta+i\gamma\), \(a=2\beta-1\), \(m=2\gamma\), and **RH is equivalent to \(a=0\) for every nontrivial zero** (Reader’s Guide “Heights and horizontal displacement”). Therefore \(a(m)=0\ \forall m\) implies RH.

8. **RH (global):** Combine the tail-height collapse (for all \(m\ge m_\star\)) with the finite-height front-end statement (already isolated in the manuscript) to cover all heights.

---

## (2) Geometry Change Requirement — manuscript-ready boxed theorem schema (OPEN-GEO)

> **Mechanism fixed:** (A) pair isolation.  
> The box below is the **one-page “closure spine schema”**: it is not a new proof, it is the contract that OPEN-GEO must satisfy.

```tex
\fbox{\begin{minipage}{0.97\linewidth}
\textbf{Theorem (OPEN--GEO closure schema; pair-isolation version).}
Fix parameters $\eta\in(0,1)$ and $\kappa\in(0,1/10)$. Let $E(v)=\Xi_2(1+v)$ be the even entire completion
(Reader's Guide, \S1). Assume $\kappa$--admissibility conventions and buffered contours are in force.

Let $\rho=\beta+i\gamma$ be a nontrivial zero of $\zeta(s)$ with $\beta>1/2$, and set
\[
a:=2\beta-1\in(0,1),\qquad m:=2\gamma>0,\qquad v_\rho=a+im\in\{E=0\}.
\]
Let $\delta_0=\delta_0(m,a):=\eta a/(\log m)^2$ and fix $0<\delta\le \delta_0$.
Let $h=h(m,a,\delta)$ be the coupling parameter in the $\Delta a$ endpoint family.

\medskip
\textbf{(OPEN--GEO witness family).}
There exists a family of admissible witness boxes/contours $\mathscr B=\mathscr B(a,m,\delta,h)$
(not necessarily aligned at $\Re v=a$) with buffered boundary $\partial\mathscr B_{\kappa/2}$ such that
$\mathcal D_{a,h}$ is holomorphic on a neighborhood of $\partial\mathscr B_{\kappa/2}$ and the endpoint
$\Phi^{(2\mathrm{s})}_{\mathscr B}(a;h)$ is well-defined.

\medskip
\textbf{(Pair isolation property).}
The witness $\mathscr B$ can be chosen so that the shifted contours induced by $v\mapsto v\pm(a\pm h)$
wind around the forced pair $\{\pm a+im\}$ in a controlled way, while remaining at distance $\gg \delta$
from every other zero in the local window $\{|\Im(\rho)-m|\le 1\}$.

\medskip
\textbf{(FORCING).}
Under the above hypotheses, the off-axis quartet forces a constant-limited lower bound
\[
\Phi^{(2\mathrm{s})}_{\mathscr B}(a;h)\ \ge\ c_0,
\]
where $c_0>0$ is an absolute constant, independent of $(m,a,\delta)$.

\medskip
\textbf{(UE upper control + resonance handling).}
For all such witnesses $\mathscr B$ one has
\[
\Phi^{(2\mathrm{s})}_{\mathscr B}(a;h)
\ \le\ C_{\mathrm{UE}}\,\delta^{p}\,\Phi_B\!\left(\frac{E'}{E}\right)
\ +\ C_{\mathrm{res}}\,\delta\cdot \mathcal R_a(m)\ +\ \mathrm{Err}(m,a,\delta,h),
\]
with constants $C_{\mathrm{UE}},C_{\mathrm{res}}$ independent of $\delta$, and with $\mathrm{Err}$ absorbable
under $\delta\le\delta_0$.
Moreover, under the pair-isolation hypothesis (e.g.\ choosing $(a,m)$ minimal at height $m$),
$\mathcal R_a(m)=O(1)$ and the right-hand side is $o(1)$ as $m\to\infty$ at nominal scale.

\medskip
\textbf{(CONTRADICTION and collapse).}
For all sufficiently large $m$ this upper bound contradicts the forcing lower bound, hence no such off-axis
zero exists. Therefore $a(m)=0$ for every nontrivial height $m$, and by the RH--free reduction in the Reader's Guide
(\S2), RH holds.
\end{minipage}}
```

---

## (3) Explicit linkage to PHU + “canonical collapse” toolbox

### 3.1 Frames and columns (manuscript language)

- **s-frame:** \(\rho=\beta+i\gamma\) (no assumption on \(\beta\)).  
- **u-frame (width–2):** \(u_\rho=2\rho=(1+a)+im\) with \(a=2\beta-1\), \(m=2\gamma\).  
- **v-frame (centered):** \(v_\rho=u_\rho-1=a+im\).

Define the “two columns” at height \(m\) in u-frame:
\[
U_R(m;a):=1+a+im,\qquad U_L(m;a):=1-a+im.
\]
Then the quartet symmetry produces \(\{U_R,U_L,\overline{U_R},\overline{U_L}\}\), and in v-frame the dial centers are \(\pm a\pm im\).

### 3.2 Collapse logic

- The Reader’s Guide records the RH-free equivalence: **RH \(\Longleftrightarrow\) \(a=0\) for every nontrivial zero** (width–2 bookkeeping).  
- OPEN-GEO (boxed schema above) is precisely the mechanism that turns a hypothetical \(a>0\) quartet into a forced endpoint contradiction, yielding \(a(m)=0\) (per-height collapse).
- Once \(a(m)=0\), the columns coincide: \(U_R(m;0)=U_L(m;0)=1+im\). This is the “column collapse”/PHU posture.
- The “canonical collapse” corollary language (“left/right RH-free forms collapse to a canonical object under PHU”) becomes post-theorem: it is downstream of \(a=0\), not an input.

---

## (4) Sanity check: one v40 NO-GO label that may be mis-classified

**Candidate mis-classification:** the program sometimes treats the legacy endpoint “\(\Phi^E_B\)” (a boundary-size functional built directly from \(E'/E\), i.e. pole-sum magnitude) as “dead” in an absolute sense.

**Referee-grade correction:**
- It *is* correctly **NO-GO as a δ-shrinking closure lever**: per-pole magnitude bounds on \(|E'/E|\) (or absolute \(L^r\) norms of it) have a built-in δ-inertia and cannot deliver the exponent budget needed for one-height collapse at \(\delta_0=\eta a/(\log m)^2\).
- But it should be downgraded from “impossible endpoint” to “not used for closure”: it can still function as a **forcing certificate / audit harness quantity** (constant-limited, topological, or numerically checkable) even if it cannot provide the δ-gain needed for contradiction.  
  *(This aligns with the v41 prebuild guidance: “Legacy \(\Phi^E_B\) remains NO-GO as δ-shrinking closure lever, but may remain useful as forcing certificate”.)*

So: keep the NO-GO latch as stated (closure), but soften the rhetorical label “dead endpoint” to “not a closure lever.”

---

## (5) S6 harness integration paragraph (explicit formula amplitude-leak mapping)

Under the explicit formula for \(\psi(x)\), an off-critical-line zero \(\rho=\beta+i\gamma\) contributes oscillatory terms of size comparable to \(x^\beta\) (modulated by \(1/\rho\) and phase), i.e. an **amplitude leak** when \(\beta>1/2\). In the program’s coordinates, this is exactly \(a=2\beta-1>0\) and \(m=2\gamma\), i.e. a v-frame quartet \(\{\pm a\pm im\}\). The OPEN-GEO closure spine is designed to rule out \(a>0\) by converting that quartet into a forced boundary phase witness on a tailored contour, and then showing the same witness must be \(o(1)\) under δ-uniform envelope control + resonance handling. Thus, discharging OPEN-GEO is tantamount to banning \(x^\beta\) leaks: it proves there are no zeros with \(\beta>1/2\), hence restores RH-level cancellation in the prime explicit formula.

---

# Patch Packet (manuscript-facing; ready to hand to Control Room)

* Callsign: RH-BRIDGE  
* Result classification: **CONDITIONAL** (depends on discharging OPEN-GEO witness existence + pair-isolation + UE bound)  
* Target gaps closed (by ID):  
  - **OPEN-GEO documentation gap** (turn the geometry pivot into an explicit proof spine contract)  
  - **NO-GO label hygiene** (clarify “dead for closure” vs “dead absolutely”)  
* Target gaps still open (by ID):  
  - **OPEN-GEO itself** (existence of witness family + forcing lemma + UE lemma + resonance lemma)  
  - Any downstream ENVELOPE/LOCAL obligations needed to upper-bound \(\Phi_B(E'/E)\) δ-uniformly  
* Key conclusions (≤5 bullets):  
  1. Aligned-box forcing for the \(\Delta a\) endpoint is provably impossible at nominal coupling; OPEN-GEO is necessary.  
  2. The pair-isolation mechanism is the cleanest way to make OPEN-GEO imply \(a(m)=0\) without reviving forbidden pointwise UE.  
  3. The manuscript needs an explicit “OPEN-GEO closure schema” box to prevent drift and make dependencies audit-visible.  
  4. “Legacy \(\Phi^E_B\)” should remain NO-GO for δ-shrinking closure but not be labeled “impossible” in absolute terms.  
  5. The geometric contradiction forbids \(a>0\) quartets, matching the explicit-formula “amplitude leak” narrative.

* Paste-ready manuscript edits:  
  (i) revised lemma/proposition statements  
  - **Insert** the boxed theorem schema (Section (2) TeX block) as the new “OPEN-GEO” theorem-style box immediately after the geometry-pivot section header.  

  (ii) revised definitions/remarks  
  - **Add** a short remark near the NO-GO constraints: “NO-GO means ‘not a δ-shrinking closure lever’ unless explicitly stated otherwise.”  

  (iii) revised theorem/inequality lines  
  - None (this batch is the closure-chain dependency map + OPEN-GEO contract, not a new inequality proof).

* Dependencies on other branches:  
  - **RH-LOCAL:** must supply the geometric/local decomposition estimates compatible with pair-isolation (near-tube vs far).  
  - **RH-ENVELOPE:** must supply δ-uniform upper control of the envelope functional on the OPEN-GEO witness.  
  - **RH-FORCE:** must confirm the forcing lemma on the OPEN-GEO witness is constant-limited (no hidden \(m\)-growth).  

* Referee risk notes (anticipated objections + how addressed):  
  - “You have not proven OPEN-GEO”: correct; this batch turns it into an explicit, audit-grade contract so it is clear what remains open.  
  - “Pair isolation is a strong geometric requirement”: yes; it is stated as an explicit hypothesis/lemma obligation (GEO-2), not assumed implicitly.  
  - “NO-GO label softened”: we preserve the closure NO-GO; we only prevent overclaiming impossibility outside closure use-cases.
