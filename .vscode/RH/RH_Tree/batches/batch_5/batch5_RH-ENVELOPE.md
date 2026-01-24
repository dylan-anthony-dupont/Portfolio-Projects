# Batch 5 — RH-ENVELOPE (v35 ground truth)
**Decision target:** S5 non-pointwise UE redesign (or decisive NO‑GO) under the locked v35 constraints.

## Executive decision (one page)

**Result:** **FAIL** (for delivering a proof‑grade, forcing‑compatible S5 redesign in this batch).

**What I can certify instead (decision‑grade NO‑GO):**
1. **Any “plain boundary \(L^p\) endpoint”** (non-pointwise but not cancelling the local kernels) **cannot make the local term subcritical.** The UE gain and the local kernel blow‑up scale in lockstep, so the local contribution to the UE side remains **\(\delta\)-inert** after the split \(E'/E=F'/F+Z'_{\rm loc}/Z_{\rm loc}\). This generalizes the already‑recorded v35 obstruction for the pointwise/sup endpoint \(p=\infty\) (where \(p=1,\theta=1\)) to the non-pointwise \(L^2\) endpoint (where the best is \(p=1/2,\theta=1/2\)).
2. **Any endpoint that “projects out / annihilates the local kernel span”** (e.g. \(\Phi_B(E):=\|(I-\Pi_B)(E'/E)\|_X\) with \(\Pi_B(Z'_{\rm loc}/Z_{\rm loc})=Z'_{\rm loc}/Z_{\rm loc}\)) **cannot control the forced dial deviation \(D_B(W)\)** without changing the contradiction endpoint or proving a new forcing link. Counterexample: if \(E=Z_{\rm loc}\), then the projected endpoint is \(0\) while \(W=E/G_{\rm out}\) has interior zeros and therefore \(D_B(W)\not=0\) on forcing-aligned boxes.

**Implication for Control Room / v36 planning:** an S5 redesign that clears the UE‑Gate must introduce **genuine cancellation or new analytic input** at the local interface (or a new forcing architecture), not merely replace \(\sup\) by \(L^p\) norms or project out local kernels while still targeting \(D_B(W)\). This batch provides paste‑ready “do‑not‑reopen” lemmas to prevent further drift into these two dead ends.

Key v35 facts used (for traceability):
- Dial deviation endpoint and pointwise UE: Lemma 10.3 (upper envelope) and definition of \(D_B(W)\) via L2-best constant phases.  
- Split and collar: Lemma 10.7 (\(E'/E=F'/F+Z'_{\rm loc}/Z_{\rm loc}\)) and Lemma 10.8 (collar bound \(\sup_{\partial B}|Z'_{\rm loc}/Z_{\rm loc}|\le N_{\rm loc}(m)/(\kappa\delta)\)).  
- Exponent budget: Theorem 10.12 and the “local term is \(\delta\)-inert” conclusion (Remark 10.11 + Lemma 10.13).  
- S5 design constraint: any new endpoint must still control the same \(D_B(W)\) used by forcing, unless a forceability link is supplied (§12, Remark 12.1).

---

## Task 1 — Candidate endpoint functionals (≤2), ranked, and verdicts

### Candidate 1 (rank 1): **Local-kernel projection endpoint** (cancellation attempt)
**Definition (prototype):**
- Space: \(X=L^2(\partial B,ds)\).
- Local-kernel span: \(K_B:=\mathrm{span}\{(v-\rho)^{-1}:\rho\in Z_{\rm loc}(B)\}\subset L^2(\partial B)\).
- Projection: \(\Pi_B\) = the \(L^2\)-orthogonal projection onto \(K_B\) (so \(\|\Pi_B\|_{L^2\to L^2}=1\), dimension-free).
- Endpoint: \(\Phi_B(E):=\|(I-\Pi_B)(E'/E)\|_{L^2(\partial B)}\).

**Why it looks attractive:** under the split \(E'/E=F'/F+Z'_{\rm loc}/Z_{\rm loc}\), the local term lies in \(K_B\), hence \((I-\Pi_B)(E'/E)=(I-\Pi_B)(F'/F)\); the local blow‑up would be annihilated “for free”.

**Fatal issue (forceability / correctness):** This endpoint cannot upper-bound the *forced* dial deviation \(D_B(W)\) uniformly, because it can vanish even when \(W\) is highly nonconstant (indeed has zeros) inside \(B\). See **NO‑GO Lemma P** below. Therefore this candidate is **NOT forcing‑compatible** unless the contradiction endpoint is changed (and a new forcing lemma supplied), which is disallowed by the Batch‑5 hard constraints.

**Verdict:** **FAIL** as an S5 endpoint controlling \(D_B(W)\).

---

### Candidate 2 (rank 2): **Boundary \(L^2\) endpoint**
**Endpoint:** \(\Phi_{B,2}(E):=\|E'/E\|_{L^2(\partial B,ds)}\).

**Best UE form supported by the v35 chain:** from the same evaluation + Poincaré + outer-factor control used in Lemma 10.3, but *without* the final \(L^2\to L^\infty\) step, one gets
\[
D_B(W)\ \lesssim\ \delta^{1/2}\,\|E'/E\|_{L^2(\partial B)}.
\]
(Scaling: Poisson evaluation contributes \(\delta^{-1/2}\), Poincaré contributes \(\delta\), outer-factor control contributes no \(\delta\).)

**Local term under κ-admissibility:** from Lemma 10.8 and \(|\partial B|\asymp \delta\),
\[
\left\|\frac{Z'_{\rm loc}}{Z_{\rm loc}}\right\|_{L^2(\partial B)}
\le |\partial B|^{1/2}\,\sup_{\partial B}\left|\frac{Z'_{\rm loc}}{Z_{\rm loc}}\right|
\lesssim \delta^{1/2}\cdot \frac{N_{\rm loc}(m)}{\kappa\delta}
= \frac{N_{\rm loc}(m)}{\kappa\,\delta^{1/2}}.
\]
Thus the local contribution to the UE bound is
\[
\delta^{1/2}\cdot \left\|\frac{Z'_{\rm loc}}{Z_{\rm loc}}\right\|_{2}\ \lesssim\ \frac{N_{\rm loc}(m)}{\kappa},
\]
again **δ-inert** and (since \(N_{\rm loc}(m)\ll\log m\)) unbounded with \(m\).

**Verdict:** **FAIL** (cannot clear UE‑Gate / exponent budget). See **NO‑GO Lemma L2** below.

---

## Task 2 — Proof‑grade NO‑GO lemmas (paste‑ready)

### NO‑GO Lemma L2 (non-pointwise \(L^2\) endpoint still δ‑inert at the local interface)

**Core claim:** Switching from \(\sup_{\partial B}\) to \(\|\,\cdot\,\|_{L^2(\partial B)}\) does **not** improve the exponent budget \(p-\theta\) in Theorem 10.12; one merely changes \((p,\theta)\) from \((1,1)\) to \((1/2,1/2)\), keeping \(p-\theta=0\).

### NO‑GO Lemma P (kernel‑projection endpoints cannot control \(D_B(W)\) under forcing)

**Core claim:** Any endpoint that annihilates the local log-derivative term cannot upper bound \(D_B(W)\) uniformly, because \(D_B(W)\) is *driven by the inner/local factor*.

---

## Task 3 — δ‑uniformity obligations checklist (for the NO‑GO statements)

The constants in the NO‑GO lemmas are:
- **shape‑only** (depend only on the normalized square \(Q=[-1,1]^2\) and on the v35 Poisson/Hilbert operator norms already used in Lemma 10.3),
- and **independent of** \(\delta\) and \(m\), except through the explicit appearance of \(N_{\rm loc}(m)\) and \(\kappa\) (exactly as in Lemma 10.8 / Corollary 10.10).

No hidden \(\delta\to0\) losses are used; everything is scale‑tracked.

---

## Task 4 — Interface with the S4 harness

No harness modification is required for these NO‑GO patches. The intended control-room effect is *negative*: prevent time spent on endpoint classes that cannot affect the δ‑ledger.

---

# MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* Callsign: RH-ENVELOPE
* Result classification: **FAIL**
* Target gaps closed (by ID):
  * **None** (no S5 closure delivered).  
  * **But**: two *drift-prevention* NO‑GO lemmas are supplied to permanently retire large endpoint classes that cannot work under v35’s forcing-compatible \(D_B(W)\) target.
* Target gaps still open (by ID):
  * **S5 UE redesign frontier** (v35 “Open blockers” item 1; prior register G‑4/G‑5).
  * Residual envelope ledger closure (prior G‑1/G‑12) — not addressed here.
  * Front-end dependence (prior G‑11) — not addressed here.
* Key conclusions (≤5 bullets):
  1. Replacing \(\sup_{\partial B}|E'/E|\) by \(\|E'/E\|_{L^2(\partial B)}\) yields UE gain \(\delta^{1/2}\) but local blow‑up \(\delta^{-1/2}\); their product is δ‑inert (\(p-\theta=0\)).
  2. More generally, any “plain \(L^p\)” endpoint (no cancellation) inherits the same lockstep scaling: local contribution remains δ‑inert.
  3. Endpoints that **project out** the local kernel span cannot control the forced \(D_B(W)\) without changing the contradiction endpoint / forcing architecture.
  4. Therefore S5 must introduce **new analytic input** at the local interface (e.g. provable window‑shrinking, multi‑box forcing, or a forceable cancellation endpoint), not merely a norm change.
  5. Two paste‑ready NO‑GO insertions are provided to prevent drift into these dead ends.
* Paste‑ready manuscript edits (TeX blocks):
  (i) revised lemma/proposition statements
  (ii) revised definitions/remarks
  (iii) revised theorem/inequality lines

```tex
% =========================
% v36 PATCH: Section 12 (S5 frontier) — record two baseline NO-GO results
% =========================

\subsection{Baseline NO--GO results for naive non-pointwise endpoints}
\label{subsec:S5-nogo-baseline}

The S5 goal (Section~\ref{sec:S5}) is to replace the pointwise/sup endpoint in Lemma~\ref{lem:upper-envelope}
by a non-pointwise functional that still controls the same dial deviation $D_B(W)$ appearing in the forcing chain.
Remark~\ref{rem:S5-forceability} records the forcing-compatibility requirement.

The next two lemmas prevent drift into two large endpoint classes that cannot work under the present $D_B(W)$
target and the v35 local split/collar interface.

\begin{lemma}[NO--GO: $L^2(\partial B)$ endpoint remains $\delta$--inert at the local interface]
\label{lem:S5-L2-nogo}
Let $B=B(\pm a,m,\delta)$ be an aligned box and define $W=E/G_{\rm out}$ and the best phases $e^{i\phi_0^\pm}$
as in Lemma~\ref{lem:upper-envelope}. Assume boundary contact and $\kappa$--admissibility.
Then there is a shape-only constant $C_{2}>0$ such that
\begin{equation}
  D_B(W):=\sum_{\pm}\bigl|W(v_\pm)-e^{i\phi_0^\pm}\bigr|
  \ \le\ C_{2}\,\delta^{1/2}\,\left\|\frac{E'}{E}\right\|_{L^2(\partial B,ds)}.
  \tag{S5-$L^2$-UE}
\end{equation}
Moreover, using the split $E'/E=F'/F+Z'_{\rm loc}/Z_{\rm loc}$ (Lemma~\ref{lem:log-derivative-split})
and the collar bound (Lemma~\ref{lem:collar-bound}), the local contribution satisfies
\begin{equation}
  \delta^{1/2}\left\|\frac{Z'_{\rm loc}}{Z_{\rm loc}}\right\|_{L^2(\partial B)}
  \ \le\ C_{2}'\,\frac{N_{\rm loc}(m)}{\kappa},
  \tag{S5-$L^2$-local}
\end{equation}
hence is $\delta$--inert. In particular, $L^2$ endpoints do not improve the exponent budget condition
$p-\theta\ge \tfrac12$ of Theorem~\ref{thm:exponent-budget}.
\end{lemma}

\begin{proof}
Repeat the proof of Lemma~\ref{lem:upper-envelope} but stop after Step~3 (outer factor control), i.e. do not
apply the final $L^2\to L^\infty$ bound on $E'/E$.
This yields \eqref{S5-$L^2$-UE} with the same Poisson and boundary-conjugation constants.
For \eqref{S5-$L^2$-local}, combine $|\partial B|^{1/2}\asymp \delta^{1/2}$ with the collar estimate
$\sup_{\partial B}|Z'_{\rm loc}/Z_{\rm loc}|\le N_{\rm loc}(m)/(\kappa\delta)$ (Lemma~\ref{lem:collar-bound}).
\end{proof}

\begin{lemma}[NO--GO: local-kernel projection endpoints cannot control $D_B(W)$]
\label{lem:S5-projection-nogo}
Fix an aligned box $B$ and suppose an endpoint functional has the form
\begin{equation}
  \Phi_B(E)\ :=\ \|(I-\Pi_B)(E'/E)\|_{X(\partial B)}
\end{equation}
for some normed boundary space $X(\partial B)$ and a bounded projection $\Pi_B$ satisfying
$\Pi_B(Z'_{\rm loc}/Z_{\rm loc})=Z'_{\rm loc}/Z_{\rm loc}$ whenever $Z_{\rm loc}$ is the local factor
associated to $B$ (so that the local term is annihilated).
Then there is no uniform inequality of the form
\begin{equation}
  D_B(W)\ \le\ C\,\delta^{p}\,\Phi_B(E)
\end{equation}
(valid for all forcing-aligned boxes and all $E$ obeying the boundary-contact convention), for any fixed
$p>0$ and any fixed constant $C$.
\end{lemma}

\begin{proof}
Take $E=Z_{\rm loc}$ on a forcing-aligned box for which $Z_{\rm loc}$ has at least one zero at one of the dial
points $v_\pm$ (this is the forcing scenario). Then $F\equiv 1$ and $E'/E=Z'_{\rm loc}/Z_{\rm loc}$, so by
assumption $(I-\Pi_B)(E'/E)=0$ and hence $\Phi_B(E)=0$.
However $W=E/G_{\rm out}$ shares the same interior zeros as $E$ (since $G_{\rm out}$ is zero-free), so
$W(v_\pm)=0$ for at least one sign. Because $|e^{i\phi_0^\pm}|=1$, the corresponding term in $D_B(W)$ equals
$|0-e^{i\phi_0^\pm}|=1$, so $D_B(W)\ge 1$. This contradicts any inequality $D_B(W)\le C\delta^{p}\Phi_B(E)$.
\end{proof}

\begin{remark}[Consequence for S5 searches]
\label{rem:S5-nogo-consequence}
Lemmas~\ref{lem:S5-L2-nogo} and \ref{lem:S5-projection-nogo} rule out two large endpoint classes:
(i) replacing $\sup_{\partial B}$ by an $L^2$ boundary norm without cancellation, and
(ii) annihilating the local kernel span while still targeting the forced dial deviation $D_B(W)$.
Any viable S5 redesign must introduce a genuinely new local-interface input or a new forcing-compatible endpoint.
\end{remark}
```

```tex
% =========================
% v36 PATCH: Appendix A — add two new discarded closure routes
% =========================

\subsection*{A.5 D5: Naive non-pointwise $L^2$ endpoint (NO--GO)}
Under the v35 split/collar interface (Lemmas~\ref{lem:log-derivative-split} and \ref{lem:collar-bound}),
switching the UE endpoint from $\sup_{\partial B}|E'/E|$ to $\|E'/E\|_{L^2(\partial B)}$ does not improve
the local exponent budget: Lemma~\ref{lem:S5-L2-nogo} shows the local contribution remains $\delta$--inert.

\subsection*{A.6 D6: Projecting out the local kernel span (NO--GO)}
A tempting idea is to define an endpoint by projecting $E'/E$ off the span of local Cauchy kernels so the local
term vanishes. Lemma~\ref{lem:S5-projection-nogo} shows this cannot control the forced dial deviation $D_B(W)$
without changing the contradiction endpoint or supplying a new forcing link. Therefore this route is closed
in the v35 forcing-compatible architecture.
```

* Dependencies on other branches:
  * Any *positive* S5 closure will likely require either:
    - a new forcing architecture / forceability link for a different endpoint, or
    - new local-interface analytic input (e.g. provable short-interval zero counts enabling window shrink), or
    - a new mechanism that couples the local term to a subcritical norm **without** projecting away the component that forces \(D_B(W)\).
* Referee risk notes (anticipated objections + how addressed):
  * **Objection:** “Your \(L^2\) UE inequality isn’t in v35.”  
    **Answer:** It is literally Lemma 10.3’s proof with the final \(L^2\to L^\infty\) step removed; constants are the same shape-only Poisson/Hilbert bounds already used in v35.
  * **Objection:** “Projection endpoints might work with a different forcing target.”  
    **Answer:** Agreed; the NO‑GO is specifically for endpoints that still aim to upper bound the existing forced \(D_B(W)\), per Batch‑5 constraints and v35 §12 (forceability requirement). Changing the endpoint requires a new forcing link and is outside this batch.
  * **Objection:** “You didn’t rule out all possible non-pointwise endpoints.”  
    **Answer:** Correct. This patch is *decision-grade negative triage* only: it retires two broad classes that are otherwise tempting and repeatedly re-enter the design space.
