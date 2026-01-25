# Batch 6 — RH-BRIDGE

**Ground truth:** v36 (truth-latched; S5 frontier only)

**Scope for RH-BRIDGE (Batch 6):** supply the *rectangle boundary* identities/lemmas that justify using **phase increments / winding** as a non-pointwise endpoint. This package is intentionally “operator-theory light”: no Hardy/BMO/Carleson estimates are claimed here. The goal is to (i) state minimal hypotheses under which phase increments are well-defined and equal to a log-derivative integral, (ii) show where δ enters (only through arc length), and (iii) record a local/residual split for phase increments that avoids point-evaluation losses.

Throughout, use the v36 aligned box notation:
- \(B = B(\alpha,m,\delta) := \{v: |\Re v-\alpha|\le \delta,\ |\Im v-m|\le \delta\}\).
- Near vertical side: \(I_{+}:=\{\alpha + i y:\ |y-m|\le \delta\}\) (as in the forcing setup, Lemma 8.1 in v36; same notation as v35/v36).
- Tangential arclength parameter \(s\) on \(\partial B\), with \(dv = \tau\, ds\), \(|\tau|=1\) (unit tangent).

The “collar/boundary-contact” hypothesis below is exactly the one v36 already uses to ensure boundary traces and to avoid boundary zeros: the function(s) in question must be holomorphic and nonvanishing on an open neighborhood of the relevant boundary arc (or the full \(\partial B\)), not merely on \(B\).

---

## 1) Core identity: phase increment = log-derivative integral (no point evaluation)

### Lemma B6.1 (Phase increment identity on a boundary arc)

Let \(\Gamma\subset\mathbb C\) be a piecewise \(C^{1}\) curve with a chosen orientation, and let \(f\) be holomorphic and **nonvanishing on an open neighborhood** of \(\Gamma\).
Then:

1. There exists a continuous branch of \(\log f\) along \(\Gamma\).
2. The argument increment of \(f\) along \(\Gamma\) is well-defined (mod \(2\pi\)) and satisfies
\[
\Delta_{\Gamma}\arg f \;=\; \Im\int_{\Gamma}\frac{f'(v)}{f(v)}\,dv.
\]
Equivalently, if \(v=v(s)\) is an arclength parametrization with unit tangent \(\tau(s)=v'(s)\), then
\[
\frac{d}{ds}\arg f(v(s)) \;=\; \Im\!\left(\frac{f'(v(s))}{f(v(s))}\,\tau(s)\right)
\quad\text{a.e. on }\Gamma,
\]
and integrating yields the identity above.

**Proof (referee-grade sketch).** Since \(f\) is holomorphic and nonvanishing on a neighborhood of \(\Gamma\), it admits a holomorphic logarithm on that neighborhood (after restricting to a simply-connected collar if needed). Along \(\Gamma\),
\(\log f\circ v\) is differentiable and \(\frac{d}{ds}\log f(v(s)) = (f'/f)(v(s))\,v'(s)\).
Taking imaginary parts gives \(d(\arg f)/ds\), and integrating over \(\Gamma\) yields the formula.

**Audit note.** No interior zero-freeness on all of \(B\) is required—only nonvanishing in a collar of the boundary arc \(\Gamma\). This is compatible with v36’s “κ-admissibility / boundary-contact” policy.

---

### Lemma B6.2 (Vertical side specialization and δ-scaling)

Assume \(f\) is holomorphic and nonvanishing on a neighborhood of \(I_{+}\). Parametrize \(I_{+}\) by \(v(y)=\alpha + i y\), \(y\in[m-\delta,m+\delta]\).
Then
\[
\Delta_{I_+}\arg f
=\Im\int_{m-\delta}^{m+\delta}\frac{f'(\alpha+i y)}{f(\alpha+i y)}\, i\,dy
=\int_{m-\delta}^{m+\delta}\Re\!\left(\frac{f'(\alpha+i y)}{f(\alpha+i y)}\right)\,dy.
\]
Consequently,
\[
|\Delta_{I_+}\arg f|
\le \int_{m-\delta}^{m+\delta}\left|\frac{f'(\alpha+i y)}{f(\alpha+i y)}\right|\,dy
\le 2\delta\cdot \sup_{I_+}\left|\frac{f'}{f}\right|.
\]

**δ-scaling audit.** The only δ factor introduced here is the **length** \(|I_+|=2\delta\). There is no Poisson/evaluation kernel, hence no hidden \(\delta^{-1/2}\) (or worse) point-evaluation loss.

---

## 2) Log-derivative split for phase increments (residual + local)

v36 already uses the log-derivative decomposition \(E'/E = F'/F + Z'_{\mathrm{loc}}/Z_{\mathrm{loc}}\) on boundary collars (where all factors are holomorphic and nonzero). The next lemma records the *phase increment* analogue.

### Lemma B6.3 (Phase increment split under \(E=F\cdot Z_{\mathrm{loc}}\))

Let \(E\) be holomorphic and nonvanishing on a neighborhood of \(I_+\). Let \(Z_{\mathrm{loc}}\) be a finite product of linear factors corresponding to a chosen local multiset of zeros of \(E\) (counted with multiplicity), and define \(F := E/Z_{\mathrm{loc}}\).
Assume additionally that \(Z_{\mathrm{loc}}\) and \(F\) are holomorphic and nonvanishing on a neighborhood of \(I_+\).
Then
\[
\Delta_{I_+}\arg E
=\Delta_{I_+}\arg F \;+\; \Delta_{I_+}\arg Z_{\mathrm{loc}},
\]
and, equivalently,
\[
\Im\int_{I_+}\frac{E'}{E}\,dv
=
\Im\int_{I_+}\frac{F'}{F}\,dv
+
\Im\int_{I_+}\frac{Z_{\mathrm{loc}}'}{Z_{\mathrm{loc}}}\,dv.
\]

**Proof.** Apply Lemma B6.1 to \(E, F, Z_{\mathrm{loc}}\) and use \(\log E = \log F + \log Z_{\mathrm{loc}}\) on the collar of \(I_+\).

---

### Lemma B6.4 (Local term on a vertical side is δ–inert: per-zero contribution is \(O(1)\))

Let \(I_+\) be as above and let \(\rho\in\mathbb C\) satisfy \(\rho\notin I_+\). Define \(k_\rho(v) := (v-\rho)^{-1}\).
Then
\[
\Im\int_{I_+} k_\rho(v)\,dv
= \arg(\alpha+i(m+\delta)-\rho) - \arg(\alpha+i(m-\delta)-\rho),
\]
where the arguments are taken along any continuous branch on the segment (well-defined since \(v-\rho\neq 0\) on \(I_+\)).
In particular,
\[
\left|\Im\int_{I_+}\frac{dv}{v-\rho}\right|\le \pi.
\]
More sharply, if \(\operatorname{dist}(\rho,I_+)\ge \kappa\delta\) (collar separation), then
\[
\left|\Im\int_{I_+}\frac{dv}{v-\rho}\right|
\le 2\arctan\!\left(\frac{\delta}{\kappa\delta}\right)
= 2\arctan\!\left(\frac{1}{\kappa}\right)
\le \pi.
\]

Consequently, for a local product \(Z_{\mathrm{loc}}(v)=\prod_{\rho\in Z(m)}(v-\rho)^{m_\rho}\) with \(\operatorname{dist}(Z(m),I_+)\ge \kappa\delta\),
\[
\left|\Im\int_{I_+}\frac{Z'_{\mathrm{loc}}}{Z_{\mathrm{loc}}}\,dv\right|
\le \pi\sum_{\rho\in Z(m)} m_\rho
= \pi\,N_{\mathrm{loc}}(m).
\]

**Interpretation.** In this *phase-increment* endpoint class, the local contribution is **δ–inert with exponent θ = 0** (contrast the pointwise collar bound \(\sup_{\partial B}|Z'_{\mathrm{loc}}/Z_{\mathrm{loc}}|\lesssim N_{\mathrm{loc}}/( \kappa\delta)\), which has θ = 1).

---

### Corollary B6.5 (Prototype δ-uniform upper control for a vertical phase endpoint)

Assume the setting of Lemma B6.3 on \(I_+\), and assume a residual envelope bound \(\sup_{I_+}|F'/F|\le L(m)\).
Then
\[
|\Delta_{I_+}\arg E|
\le 2\delta\,L(m) \;+\; \pi\,N_{\mathrm{loc}}(m).
\]

**Risk note (expected objection).** This is *not* yet an S5 closure mechanism, because \(N_{\mathrm{loc}}(m)\) still grows like \(O(\log m)\) under RH-free majorants. The point of the lemma is narrower: it shows that a *phase* endpoint naturally avoids the \(\delta^{-1}\) collar blow-up, and thereby opens the door to budget-feasible designs if the local part can be handled with cancellation / signed structure (or if the forcing architecture is changed to target a local phase object directly).

---

## 3) How this interfaces with forcing (what BRIDGE provides vs what FORCE must do)

- v36 forcing uses **phase rotation of the pair factor** \(Z_{\mathrm{pair}}\) on \(I_+\), with
  \(\Delta_{I_+}\arg Z_{\mathrm{pair}}\ge \pi/2\) (short-side forcing; see Lemma 8.1 in v36, same as v35).
- Lemmas B6.1–B6.4 provide the “calculus” layer needed to make any *phase endpoint* proof-grade:
  it is a log-derivative integral on the boundary arc and splits additively across multiplicative factorization.
- What is not provided here (and must be supplied by FORCE/ENVELOPE in the S5′ design) is a forcing transfer statement of the form:
  “off-axis pair ⇒ \(\widetilde D_B\) is large,” where \(\widetilde D_B\) is the chosen phase endpoint (possibly a sub-arc / collar-restricted contour).

In other words: BRIDGE certifies the phase endpoint’s meaning and δ-scaling; FORCE must certify that the endpoint is actually forced (or dominates the already-forced \(D_B(W)\), per the v36 forceability gate).

---

## 4) If restricted contours are needed: Γλ sub-arcs (optional, but clean)

If corner/collar interactions at the endpoints of \(I_+\) are technically awkward, define the **central sub-arc**
\[
I_+^{(\lambda)} := \{\alpha + i y:\ |y-m|\le \lambda\delta\},\qquad 0<\lambda<1,
\]
or use any piecewise \(C^1\) curve \(\Gamma_\lambda\) contained in the collar of \(\partial B\) that connects the same vertical levels but stays a fixed fraction away from corners.

All lemmas above hold verbatim with \(I_+\) replaced by \(I_+^{(\lambda)}\) or \(\Gamma_\lambda\), with the only change that the length becomes \(2\lambda\delta\) (hence residual terms gain a factor \(\lambda\)).

---

## 5) S6 harness check: explicit-formula interpretation (requested)

A phase endpoint such as \(\Delta_{I_+}\arg E\) (or \(\Delta_{I_+}\arg Z_{\mathrm{pair}}\)) is, structurally, an **argument-principle witness**: it measures a component of the winding of \(E\) (or a factor of \(E\)) along a boundary segment.

- This is not *directly* the same object as an “\(x^\beta\) amplitude leak” in the explicit formula for primes; those leaks are governed by the real parts \(\beta\) of zeros.
- However, off-axis quartets in v-frame correspond to zeros of \(E(v)=\Xi_2(1+v)\) with \(\Re v\neq 0\), and the argument principle expresses zero counts inside contours via \(\int (E'/E)\,dv\). Thus a phase/winding endpoint is plausibly interpretable as a *geometric witness* of the same off-axis zeros that drive \(x^\beta\) terms.

**Truth-grade statement for v36/v37 design:** the phase endpoint is a “zero-presence witness” (argument principle / winding), not an amplitude functional. If S6 needs an explicit amplitude leak interpretation, an additional lemma must connect the proposed phase endpoint to a quantity that, under the explicit formula, forces a lower bound proportional to \(x^\beta\) for some \(x\). That link is not automatic and is not claimed here.

---

## 6) Paste-ready manuscript edits (v37 pre-build blocks)

> These edits do **not** claim an S5′ closure; they add the missing lemma infrastructure so that any future “Δarg endpoint” is meaningfully defined and δ-scaled without point evaluation.

### (i) Add a new definition (phase endpoint on the near side)

```tex
% --- add near the start of Section 12 (S5 frontier), after the forceability gate remark ---

\\begin{definition}[Vertical phase endpoint on the near side]
Let $B=B(\\alpha,m,\\delta)$ be a $\\kappa$--admissible aligned box and let $I_+:=\\{\\alpha+iy:\\ |y-m|\\le \\delta\\}$.
Let $f$ be holomorphic and nonvanishing on an open neighborhood of $I_+$.
Define the phase increment of $f$ on $I_+$ by
\\[
\\Delta_{I_+}\\arg f:=\\Im\\int_{I_+}\\frac{f'(v)}{f(v)}\\,dv,
\\]
which is well-defined (mod $2\\pi$) and equals the net change of a continuous argument of $f$ along $I_+$.
\\end{definition}
```

### (ii) Add the identity lemma (phase increment = log-derivative integral)

```tex
% --- immediately after the definition above ---

\\begin{lemma}[Phase increment identity on boundary arcs]\\label{lem:phase_increment_identity}
Let $\\Gamma$ be a piecewise $C^1$ curve and let $f$ be holomorphic and nonvanishing on a neighborhood of $\\Gamma$.
Then $\\Delta_\\Gamma\\arg f$ is well-defined and
\\[
\\Delta_\\Gamma\\arg f \\,=\\, \\Im\\int_\\Gamma \\frac{f'(v)}{f(v)}\\,dv.
\\]
In particular, for $I_+$ one has
\\[
\\Delta_{I_+}\\arg f
=\\Im\\int_{m-\\delta}^{m+\\delta}\\frac{f'(\\alpha+iy)}{f(\\alpha+iy)}\\, i\\,dy
=\\int_{m-\\delta}^{m+\\delta}\\Re\\!\\left(\\frac{f'(\\alpha+iy)}{f(\\alpha+iy)}\\right)dy.
\\]
\\end{lemma}

\\begin{proof}
Since $f$ is holomorphic and nonvanishing on a neighborhood of $\\Gamma$, it admits a holomorphic logarithm on a collar of $\\Gamma$.
Differentiate $\\log f(v(s))$ along an arclength parametrization $v(s)$ and take imaginary parts.
\\end{proof}
```

### (iii) Add the local/residual split and the δ–inert local bound

```tex
% --- add next; uses existing $Z_{\\rm loc}$ and $F=E/Z_{\\rm loc}$ notation ---

\\begin{lemma}[Phase increment split and local δ--inertness on $I_+$]\\label{lem:phase_increment_split_local}
Assume $E$, $Z_{\\rm loc}$ and $F:=E/Z_{\\rm loc}$ are holomorphic and nonvanishing on a neighborhood of $I_+$.
Then
\\[
\\Delta_{I_+}\\arg E = \\Delta_{I_+}\\arg F + \\Delta_{I_+}\\arg Z_{\\rm loc}.
\\]
Moreover,
\\[
\\left|\\Delta_{I_+}\\arg Z_{\\rm loc}\\right|
=\\left|\\Im\\int_{I_+}\\frac{Z'_{\\rm loc}}{Z_{\\rm loc}}\\,dv\\right|
\\le \\pi\\,N_{\\rm loc}(m),
\\]
where $N_{\\rm loc}(m)$ is the local-window zero count (with multiplicity).
\\end{lemma}

\\begin{proof}
The split follows from $\\log E = \\log F + \\log Z_{\\rm loc}$ on the collar of $I_+$.
For a single factor $(v-\\rho)$, $\\Im\\int_{I_+}\\frac{dv}{v-\\rho}$ equals the change of $\\arg(v-\\rho)$ between endpoints, hence has absolute value at most $\\pi$.
Summing with multiplicity gives the bound.
\\end{proof}
```

### (iv) Optional: record the prototype upper bound

```tex
\\begin{corollary}[Prototype upper bound for $\\Delta_{I_+}\\arg E$]\\label{cor:phase_increment_prototype_upper}
In the setting of Lemma~\\ref{lem:phase_increment_split_local}, if additionally $\\sup_{I_+}|F'/F|\\le L(m)$ then
\\[
\\left|\\Delta_{I_+}\\arg E\\right|
\\le 2\\delta\\,L(m)+\\pi N_{\\rm loc}(m).
\\]
\\end{corollary}
```

### (v) Add a short remark to prevent hidden point-evaluation reintroduction

```tex
\\begin{remark}[No point evaluation in phase endpoints]
The endpoint $\\Delta_{I_+}\\arg f$ is a boundary integral of a log-derivative and introduces no Poisson/evaluation kernel.
Hence it does not incur the $\\delta^{-1/2}$ point-evaluation loss present in disc/Poisson recovery of $f(v_0)$ from boundary data.
\\end{remark}
```

---

# MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* Callsign: RH-BRIDGE
* Result classification: **CONDITIONAL**
* Target gaps closed (by ID): *(Batch-6 scoped)* none fully closed; this is toolkit infrastructure for an S5′ phase endpoint class.
* Target gaps still open (by ID): forceability link for any redesigned endpoint; δ-uniform UE upper control beyond the prototype bound; explicit-formula amplitude interpretation lemma (if S6 demands it).
* Key conclusions (≤5 bullets):
  1. Phase increments on boundary arcs are well-defined under collar nonvanishing and equal \(\Im\int (f'/f)\,dv\) (Lemma B6.1).
  2. On the vertical near side \(I_+\), δ enters only via arc length; no point-evaluation losses occur (Lemma B6.2).
  3. Under \(E=F\cdot Z_{\rm loc}\), vertical phase increments split additively (Lemma B6.3).
  4. The local contribution to a vertical phase endpoint is δ–inert: per-zero contribution is \(O(1)\), hence \(|\Delta_{I_+}\arg Z_{\rm loc}|\le \pi N_{\rm loc}(m)\) (Lemma B6.4).
  5. This supports S5′ designs based on signed/winding endpoints, but does not itself provide closure.
* Paste-ready manuscript edits:
  (i) revised lemma/proposition statements: **Lemma `phase_increment_identity`**, **Lemma `phase_increment_split_local`**, **Corollary `phase_increment_prototype_upper`** (TeX blocks above)
  (ii) revised definitions/remarks: **Definition `Vertical phase endpoint on the near side`**, **Remark `No point evaluation in phase endpoints`** (TeX blocks above)
  (iii) revised theorem/inequality lines: none (toolkit only; no closure claimed)
* Dependencies on other branches:
  - **FORCE:** must decide the actual endpoint \(\widetilde D_B\) and prove forceability (domination transfer or new forcing lemma).
  - **ENVELOPE/LOCAL:** must propose δ-uniform upper control for the chosen phase endpoint that beats the budget (likely requiring cancellation / non-absolute structure).
* Referee risk notes (anticipated objections + how addressed):
  - *“Arg not well-defined / branch ambiguity.”* Addressed by requiring holomorphic nonvanishing on a collar of the arc; then a continuous log exists on the arc and the integral definition is unambiguous mod \(2\pi\).
  - *“Interior zeros invalidate log.”* Not relevant: only a collar of the boundary arc is needed, not interior zero-freeness.
  - *“Hidden δ^{-1/2} operator norm.”* Not present: endpoint is a boundary integral, not a point evaluation from boundary norms.
  - *“Local term might secretly scale like 1/δ.”* Explicitly ruled out for phase increments: \(\Im\int_{I_+} (v-\rho)^{-1}\,dv\) is an endpoint argument difference bounded by \(\pi\), independent of δ.
