# Batch 12 — RH-ABSORB
**Program:** RH Convergence Program  
**Callsign:** RH-ABSORB  
**Ground truth:** v41 (build) → v42 (target insertions)  
**Mission:** Program Hygiene Package for GEO‑C4 (δ‑uniform quantifiers + monotone‑shrink safety + NO‑GO scope audit)

This note is **not** an endpoint proposal. It is the *hygiene layer* required so GEO‑C4 (or any successor geometry/coupling redesign) can be audited without δ‑smuggling or shrink‑policy ambiguity.

---

## 1) Monotone shrink lemma (explicit, GEO‑C4 compatible)

### 1.1 What this lemma is for

The program repeatedly uses the pattern:

1. Fix a nominal scale \(\delta_0(m,a)\).
2. If the boundary is not \(\kappa\)-buffered away from zeros, **shrink** to some \(\delta\le \delta_0\) that is admissible.
3. Run forcing on that (possibly shrunk) witness contour.
4. Run an upper-envelope (UE) estimate and local/residual controls on that same contour.

To keep this non-circular, we need two things:

- **Forcing is not lost** by shrinking \(\delta\).
- **Upper bounds are not worsened** by shrinking \(\delta\) (or, if they can worsen, the lemma must say so explicitly and the architecture must not rely on such a shrink).

### 1.2 TeX-ready lemma

```tex
\begin{lemma}[Monotone shrink safety for GEO witness contours]\label{lem:geoC4-delta-shrink-monotone}
Fix \(\kappa\in(0,1/10)\). Let \((m,a)\) be parameters and set the nominal scale
\(\delta_0=\delta_0(m,a)\).
Assume we have a one-parameter witness family of contours/boxes
\(\{\mathscr B(\delta):0<\delta\le \delta_0\}\) in the \(v\)-plane and a coupling rule
\(h(\delta)=\kappa\delta\).

Let \(0<\delta'\le \delta\le \delta_0\) be two scales such that both \(\mathscr B(\delta)\) and
\(\mathscr B(\delta')\) are \(\kappa\)-admissible in the sense required by the GEO endpoint
(i.e. \(E\) is nonvanishing on the relevant boundary shifts so that the endpoint is well-defined).

Assume:

\begin{enumerate}[leftmargin=1.5em]
\item[\textnormal{(F)}] \textnormal{(Forcing is scale-independent).}
There exists \(c_0(\kappa)>0\) such that, whenever \(E\) has the off-axis quartet
\(\{\pm a\pm i m\}\), the forcing lemma applies on \(\mathscr B(\delta)\) and on \(\mathscr B(\delta')\),
yielding the same absolute lower bound
\(\widetilde D_{\mathscr B(\delta)}(W)\ge c_0(\kappa)\) and \(\widetilde D_{\mathscr B(\delta')}(W)\ge c_0(\kappa)\).

\item[\textnormal{(UE)}] \textnormal{(UE upper bound is an explicit \(\delta\)-power law).}
There exist exponents \(p\ge 0\), \(\theta\ge 0\) and \(\delta\)-uniform constants \(C_{\rm res},C_{\rm loc}\ge 0\)
(independent of \(\delta\)) and \(\delta\)-independent majorants \(A_{\rm res}(m,a)\), \(A_{\rm loc}(m,a)\ge 0\)
such that for all admissible \(\delta\le\delta_0\),
\begin{equation}\label{eq:UE-powerlaw}
\Phi_{\mathscr B(\delta)}^{\rm GEO}(E)\ \le\ C_{\rm res}\,\delta^{p}\,A_{\rm res}(m,a)\ +\ C_{\rm loc}\,\delta^{p-\theta}\,A_{\rm loc}(m,a).
\end{equation}
\end{enumerate}

Then:

\begin{enumerate}[leftmargin=1.5em]
\item If \(p-\theta>0\), the RHS of \eqref{eq:UE-powerlaw} is monotone non-increasing under \(\delta\mapsto \delta'\le\delta\).
In particular,
\(\Phi_{\mathscr B(\delta')}^{\rm GEO}(E)\le \Phi_{\mathscr B(\delta)}^{\rm GEO}(E)\) under the same majorants.

\item If \(p-\theta=0\), the local contribution is \(\delta\)-inert (shrinking does not help or hurt it).

\item If \(p-\theta<0\), shrinking \(\delta\) \emph{worsens} the local contribution; in this case any proof step that
relies on “shrink \(\delta\) if needed” must be rejected as invalid unless the architecture is redesigned.
\end{enumerate}
\end{lemma}

\begin{proof}
Item (F) is delegated to RH-FORCE: it is a statement that the lower bound is topological/structural and therefore
independent of the scale parameter \(\delta\) (as long as the endpoint is well-defined on the contour).

For (UE), compare powers. Since \(0<\delta'\le\delta\) and \(x\mapsto x^{\lambda}\) is nondecreasing for \(\lambda>0\),
we have \((\delta')^{p}\le \delta^{p}\). Moreover \((\delta')^{p-\theta}\le \delta^{p-\theta}\) iff \(p-\theta\ge 0\),
with strict monotone improvement if \(p-\theta>0\). Substituting these into \eqref{eq:UE-powerlaw} yields the claims.
\end{proof}
```

### 1.3 Implementation note (what this forces other branches to expose)

Lemma \(\ref{lem:geoC4-delta-shrink-monotone}\) is deliberately strict: it **forces** ENVELOPE/LOCAL to present their
bounds in a form where all \(\delta\)-dependence is explicit (no \(C(\delta)\) constants). If any step produces a term
like \(\delta^{-r}\) with \(r>p\) in the upper bound, then the lemma correctly flags “shrink \(\delta\)” as *unsafe*.

---

## 2) δ‑uniformity contract paragraph (paste into v42)

The program has repeatedly drifted via silent quantifier flips (e.g. “choose \(\delta\)” vs “for all \(\delta\le\delta_0\)”).
The following contract latches the correct quantifiers and uniformity obligations.

```tex
\begin{remark}[Quantifier contract for GEO-C4 (no \(\delta\)-smuggling)]\label{rem:delta-uniformity-contract}
Fix \(\kappa\in(0,1/10)\) and \(m_0\ge 10\).
For each parameter pair \((m,a)\) with \(m\ge m_0\) and \(0<a\le 1\), define the nominal scale
\(\delta_0(m,a)=\eta\,a/(\log m)^2\) with \(\eta\in(0,1)\) fixed globally.

All statements in the GEO closure chain must have one of the following explicit forms (no other form is permitted):

\begin{enumerate}[leftmargin=1.5em]
\item \textnormal{\textbf{Uniform-in-\(\delta\) bounds on admissible contours.}}
For all \(0<\delta\le \delta_0(m,a)\), if \(\mathscr B(\delta)\) is \(\kappa\)-admissible (so the endpoint is well-defined),
then the asserted inequality holds with constants independent of \(\delta\).

\item \textnormal{\textbf{Existence of an admissible shrink (non-circular).}}
For each \(\delta_0>0\) there exists some \(0<\delta\le \delta_0\) such that \(\mathscr B(\delta)\) is \(\kappa\)-admissible
(zeros of \(E\) are isolated). This existence claim may depend on \(E\), but not on any RH-equivalent hypothesis.

\item \textnormal{\textbf{Shrink is permitted only under monotone safety.}}
Any step that replaces \(\delta\) by a smaller \(\delta'\le\delta\) must invoke
Lemma~\ref{lem:geoC4-delta-shrink-monotone} (or a strictly stronger lemma) to certify that
(i) forcing is preserved and (ii) the UE upper bound does not worsen under the shrink.
\end{enumerate}
\end{remark}
```

---

## 3) NO‑GO sanity audit (v40/v41 latches: scope + GEO‑C4 compatibility)

The program already contains decisive NO‑GO items. The only risk here is **mis-scoping** them so they accidentally
block GEO‑C4 (or, conversely, letting GEO‑C4 drift back into a banned endpoint class).

### 3.1 Audit table (what still stands, and how it must be worded)

```tex
\begin{remark}[NO--GO scope audit (to prevent self-blocking)]\label{rem:nogo-scope-geoC4}
The following NO--GO items remain valid, but each must be read with its correct scope.
They do not forbid geometry/coupling redesigns unless the redesign falls back into the excluded endpoint class.

\begin{enumerate}[leftmargin=1.5em]
\item \textnormal{\textbf{(D1) Pointwise UE + collar + \(\eta\)-absorption.}}
The route using the pointwise endpoint \(\sup_{\partial B}|E'/E|\) with the standard \(\kappa\)-collar bound has local exponent
\(\theta=1\) and no effective \(\delta\)-gain under the nominal scaling. This blocks S1/S1', not GEO-C4.

\item \textnormal{\textbf{(D5) Absolute \(L^r(\partial B)\) endpoints on \(E'/E\).}}
Absolute \(L^r\) endpoints (including \(L^2\)) are \(\delta\)-inert under the current collar interface: the UE exponent collapses to
\(p(r)=1-1/r\) and the local exponent matches \(\theta(r)=1-1/r\), so \(p-\theta=0\).
This blocks “replace sup by \(L^r\)” fixes; it does not block signed/phase or energy endpoints outside this class.

\item \textnormal{\textbf{(D6) Projection-kill endpoints targeting the forced dial deviation.}}
Endpoints that explicitly annihilate the local kernel span and still attempt to control the \emph{forced object}
\(D_B(W)\) are impossible without a new forcing-transfer lemma (structural counterexample \(E=Z_{\rm loc}\)).
This does \emph{not} block GEO-C4 provided the GEO endpoint is itself forceable (or dominates the forced endpoint)
and is not used as a “kill local term then bound \(D_B(W)\)” shortcut.
\item \textnormal{\textbf{Defect \(\delta^1\) ceiling (pointwise-in-\(a\) class).}}
The lemma asserting a \(\delta^1\) ceiling applies to pointwise-in-\(a\) defect endpoints derived from uniform pointwise control of
\(|\mathcal L_a|\) on a contour of length \(\asymp \delta\). It must be stated explicitly as “NO--GO for the pointwise defect class,”
not as a global ban on non-pointwise endpoints.

\item \textnormal{\textbf{Defect resonance \(\delta\)-inertia (pointwise-in-\(a\) class).}}
The resonance NO--GO latches that near-resonant quartets can make pointwise defect endpoints \(\delta\)-inert.
This must be stated as “NO--GO for pointwise-in-\(a\) endpoints without \(\delta\)-aware resonance control,”
not as a global ban on all oscillatory/phase mechanisms.

\item \textnormal{\textbf{NG--\(\Delta a\)--A (aligned boxes).}}
The aligned-box forcing bullet for the \(\Delta a\) phase endpoint fails at the nominal coupling \(h=\delta\)
(in fact the toy model yields \(\Phi^{(2s)}_{B(a,m,\delta)}(a;h)\ll \delta h/a^2\), hence shrinking \(\delta\) only makes it smaller).
This is a forcing failure on that witness family/coupling, not an obstruction to GEO-C4.
\end{enumerate}
\end{remark}
```

### 3.2 What this audit explicitly *permits*

- **GEO-C4 is permitted** if it uses an endpoint outside D1/D5/D6 and ships with a forcing lemma in its own class (or a domination link).
- Any attempt to invoke a NO‑GO lemma against GEO-C4 must cite the matching endpoint class and show GEO-C4 lies in it.

These scoping corrections were already flagged as necessary in the v41 geometry-pivot plan and integration notes; the point of this package is to make them *in-text and enforceable*.  

---

## 4) Resonance interaction statement (energy/projection endpoint)

The resonance risk in the earlier defect/phase proposals was “endpoint can collapse to \(0\) by cancellation or near-resonant tilts,
making the UE bound \(\delta\)-inert.” GEO‑C4 changes the endpoint class.

### 4.1 TeX-ready remark/lemma

```tex
\begin{remark}[Resonance interaction for GEO-C4 endpoints]\label{rem:geoC4-resonance}
Assume the GEO-C4 endpoint is an \emph{energy/projection}-type functional, i.e.
\(\Phi^{\rm GEO}_{\mathscr B} \ge 0\) and is defined as a norm (or squared norm) of a projected boundary signal
(e.g. \(\Phi^{\rm GEO}_{\mathscr B}=\|P(\psi)\|_{L^2(\partial\mathscr B)}\) for a bounded projection \(P\)).
Then the earlier “sign-cancellation resonance” pathology for pointwise endpoints is eliminated: the endpoint cannot be made small by
pure sign cancellation in the integrand, only by the projected signal itself being small.

Accordingly, the only remaining resonance risk for GEO-C4 is \emph{geometric/packing} resonance:
too many zeros of \(E\) entering the \(\kappa\delta\)-collar or the \(\delta\)-window that defines the local factor, which enlarges
local contributions.
This risk is delegated to RH-LOCAL via explicit bounds on the appropriate local count (e.g. zeros in \(\delta\)-arcs / windows),
and must be recorded as such (no hidden “resonance is harmless” statements are permitted).
\end{remark}
```

---

## 5) Mandatory S6 harness cross-check (interpretive; not a proof step)

Under the program’s frame mapping, an off-axis zero \(\rho=\beta+i\gamma\) corresponds to the \(v\)-frame displacement
\(a=2\beta-1\neq 0\) at height \(m=2\gamma\). The S5/GEO closure logic is designed to show:

- off-axis quartet \(\Rightarrow\) a **scale-independent forced lower bound** (forcing lemma), but
- also \(\Rightarrow\) a **scale-dependent UE upper bound** that tends to \(0\) for \(\delta=\delta_0(m,a)=\eta a/(\log m)^2\) as \(m\to\infty\),
  provided the exponent budget passes and constants are \(\delta\)-uniform.

If this contradiction is achieved, it eliminates the possibility of any fixed \(a>0\), i.e. forbids \(\beta>1/2\) and hence removes the
explicit-formula amplitude leak term \(x^{\beta}\sim x^{1/2+a/2}\) at arbitrarily large heights. In that sense, the \(\delta\)-uniformity
contract and shrink-monotonicity lemma correspond to “uniform suppression of amplitude leaks across smoothing scales,” but this is
interpretive: the manuscript must not claim prime-error consequences until RH itself is proved.

---

## Mandatory Patch Packet

* **Callsign:** RH-ABSORB
* **Result classification:** **PASS** (hygiene package delivered; truth depends only on stated hypotheses)
* **Target gaps closed (by ID):**
  - **G‑4** (δ‑uniformity discipline) — for GEO‑C4 via Contract + explicit power-law requirement.
  - **G‑5** (κ‑admissible shrink policy safety) — via monotone-shrink lemma (now endpoint-class explicit).
* **Target gaps still open (by ID):**
  - Any GEO‑C4 **UE** inequality producing the explicit \((p,\theta)\) power-law form in \eqref{eq:UE-powerlaw} (owned by RH‑ENVELOPE/RH‑LOCAL).
  - Any GEO‑C4 **forcing** lemma establishing (F) for the new endpoint (owned by RH‑FORCE).
* **Key conclusions (≤5 bullets):**
  1. Shrink is only permitted if upper bounds are explicit \(\delta\)-power laws with \(\delta\)-uniform constants; otherwise “shrink \(\delta\)” is invalid.
  2. Under the gate \(p-\theta\ge 0\), shrinking cannot worsen the UE upper bound; if \(p-\theta<0\), shrink makes the architecture strictly worse (flagged).
  3. Forcing must be explicitly scale-independent (topological/structural) to be compatible with shrink policies.
  4. NO‑GO results remain valid but must be **scoped to endpoint classes**; they do not globally block GEO‑C4.
  5. GEO‑C4 energy/projection endpoints eliminate sign-cancellation resonance; remaining resonance is local zero packing, delegated to RH‑LOCAL.
* **Paste-ready manuscript edits:**
  (i) **revised lemma/proposition statements**
```tex
\begin{lemma}[Monotone shrink safety for GEO witness contours]\label{lem:geoC4-delta-shrink-monotone}
Fix \(\kappa\in(0,1/10)\). Let \((m,a)\) be parameters and set the nominal scale
\(\delta_0=\delta_0(m,a)\).
Assume we have a one-parameter witness family of contours/boxes
\(\{\mathscr B(\delta):0<\delta\le \delta_0\}\) in the \(v\)-plane and a coupling rule
\(h(\delta)=\kappa\delta\).

Let \(0<\delta'\le \delta\le \delta_0\) be two scales such that both \(\mathscr B(\delta)\) and
\(\mathscr B(\delta')\) are \(\kappa\)-admissible in the sense required by the GEO endpoint
(i.e. \(E\) is nonvanishing on the relevant boundary shifts so that the endpoint is well-defined).

Assume:

\begin{enumerate}[leftmargin=1.5em]
\item[\textnormal{(F)}] \textnormal{(Forcing is scale-independent).}
There exists \(c_0(\kappa)>0\) such that, whenever \(E\) has the off-axis quartet
\(\{\pm a\pm i m\}\), the forcing lemma applies on \(\mathscr B(\delta)\) and on \(\mathscr B(\delta')\),
yielding the same absolute lower bound
\(\widetilde D_{\mathscr B(\delta)}(W)\ge c_0(\kappa)\) and \(\widetilde D_{\mathscr B(\delta')}(W)\ge c_0(\kappa)\).

\item[\textnormal{(UE)}] \textnormal{(UE upper bound is an explicit \(\delta\)-power law).}
There exist exponents \(p\ge 0\), \(\theta\ge 0\) and \(\delta\)-uniform constants \(C_{\rm res},C_{\rm loc}\ge 0\)
(independent of \(\delta\)) and \(\delta\)-independent majorants \(A_{\rm res}(m,a)\), \(A_{\rm loc}(m,a)\ge 0\)
such that for all admissible \(\delta\le\delta_0\),
\begin{equation}\label{eq:UE-powerlaw}
\Phi_{\mathscr B(\delta)}^{\rm GEO}(E)\ \le\ C_{\rm res}\,\delta^{p}\,A_{\rm res}(m,a)\ +\ C_{\rm loc}\,\delta^{p-\theta}\,A_{\rm loc}(m,a).
\end{equation}
\end{enumerate}

Then:

\begin{enumerate}[leftmargin=1.5em]
\item If \(p-\theta>0\), the RHS of \eqref{eq:UE-powerlaw} is monotone non-increasing under \(\delta\mapsto \delta'\le\delta\).
In particular,
\(\Phi_{\mathscr B(\delta')}^{\rm GEO}(E)\le \Phi_{\mathscr B(\delta)}^{\rm GEO}(E)\) under the same majorants.

\item If \(p-\theta=0\), the local contribution is \(\delta\)-inert (shrinking does not help or hurt it).

\item If \(p-\theta<0\), shrinking \(\delta\) \emph{worsens} the local contribution; in this case any proof step that
relies on “shrink \(\delta\) if needed” must be rejected as invalid unless the architecture is redesigned.
\end{enumerate}
\end{lemma}

\begin{proof}
Item (F) is delegated to RH-FORCE: it is a statement that the lower bound is topological/structural and therefore
independent of the scale parameter \(\delta\) (as long as the endpoint is well-defined on the contour).

For (UE), compare powers. Since \(0<\delta'\le\delta\) and \(x\mapsto x^{\lambda}\) is nondecreasing for \(\lambda>0\),
we have \((\delta')^{p}\le \delta^{p}\). Moreover \((\delta')^{p-\theta}\le \delta^{p-\theta}\) iff \(p-\theta\ge 0\),
with strict monotone improvement if \(p-\theta>0\). Substituting these into \eqref{eq:UE-powerlaw} yields the claims.
\end{proof}
```
  (ii) **revised definitions/remarks**
  ```tex
  % Insert immediately after defining δ0 and κ-admissibility for the GEO witness family:
  \begin{remark}[Quantifier contract for GEO-C4 (no \(\delta\)-smuggling)]\label{rem:delta-uniformity-contract}
  % (paste Remark \ref{rem:delta-uniformity-contract} from above)
  \end{remark}

  % Insert in the NO–GO appendix or in the GEO front-matter (recommended: GEO front-matter):
  \begin{remark}[NO--GO scope audit (to prevent self-blocking)]\label{rem:nogo-scope-geoC4}
  % (paste Remark \ref{rem:nogo-scope-geoC4} from above)
  \end{remark}

  % Insert where resonance is discussed for GEO endpoints:
  \begin{remark}[Resonance interaction for GEO-C4 endpoints]\label{rem:geoC4-resonance}
  % (paste Remark \ref{rem:geoC4-resonance} from above)
  \end{remark}
  ```
  (iii) **revised theorem/inequality lines**
  ```tex
  % In any GEO-C4 UE inequality statement, force the explicit δ-power-law disclosure:
  \Phi^{\rm GEO}_{\mathscr B(\delta)}(E)\ \le\ C_{\rm res}\,\delta^{p}\,A_{\rm res}(m,a)\ +\ C_{\rm loc}\,\delta^{p-\theta}\,A_{\rm loc}(m,a),
  \qquad \text{with constants independent of \(\delta\).}
  ```
* **Dependencies on other branches:**
  - **RH‑FORCE:** must deliver the scale-independent forcing lower bound for the GEO endpoint (assumption (F)).
  - **RH‑ENVELOPE / RH‑LOCAL:** must deliver UE + local/residual controls in the explicit \(\delta\)-power-law form (assumption (UE)), with \(\delta\)-uniform constants.
* **Referee risk notes (anticipated objections + how addressed):**
  1. *“Your monotone lemma assumes a \(\delta\)-power law form; isn’t that the hard part?”* — Correct; the lemma is a **hygiene latch** that prevents hiding \(\delta\)-dependence inside constants. It does not claim ENVELOPE/LOCAL can achieve the form.
  2. *“Admissibility depends on unknown zeros; isn’t shrink circular?”* — No: existence of an admissible shrink uses only isolated zeros of an entire function; it is RH-free. The contract forces this to be stated explicitly.
  3. *“Does D6 projection NO‑GO block GEO‑C4 energy projections?”* — Only if the projection is used to annihilate the local kernel while still targeting a forced object without a forcing link. The scope remark forbids that misuse.
