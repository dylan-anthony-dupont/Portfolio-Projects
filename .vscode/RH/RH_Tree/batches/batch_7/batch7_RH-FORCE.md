# Batch 7 — RH-FORCE (v37 locked)

*Side note (access check): the legacy PDF manuscripts v10–v14 are still present and readable in this run (`/mnt/data/manuscript_v10.pdf` … `/mnt/data/manuscript_v14.pdf`).*

## 0) Scope reminder (what this branch is solving)

Batch‑7 asks RH‑FORCE to make the “Missing Lever” usable by **ensuring forceability attaches** to the S5′ endpoint class. Concretely:

* either show **domination transfer** from a proposed endpoint \(\Phi_B\) to a forced endpoint, or
* supply a **direct forcing lemma** targeting \(\Phi_B\), or
* issue a **NO‑GO** classification if neither is possible.

Ground truth is **v37** (locked build). The relevant installed objects are:

* **Buffered boundary phase endpoint** \(\widetilde D_B(W)\) (Definition 12.16)【681:2†manuscript_v37.pdf†L106-L112】.
* **Direct \(\pi/2\) forcing lemma** for \(\widetilde D_B(W)\) via argument principle (Lemma 12.17)【655:0†manuscript_v37.pdf†L1-L10】.
* **Forceability gate warning**: \(\widetilde D_B\) does **not** dominate the legacy dial deviation \(D_B(W)\) (Remark 12.18)【655:1†manuscript_v37.pdf†L1-L19】.

## 1) Task A — Forcing transfer or direct forcing for the S5′ endpoint

### A1. The clean PASS route: take ENVELOPE’s endpoint \(\Phi_B\) to be \(\widetilde D_B(W)\)

v37 already provides a proof‑grade direct forcing lemma at this endpoint:

*Definition (v37).* For a \(\kappa\)-admissible aligned box \(B\), define \(\widetilde D_B(W)\) as the maximum of the absolute phase increments of \(W\) along the four sides of the **buffered inner boundary** \(\partial B_{\kappa/2}\)【681:2†manuscript_v37.pdf†L106-L112】【655:0†manuscript_v37.pdf†L1-L7】.

*Lemma (v37).* If \(W\) has a zero in \(B_{\kappa/2}^\circ\), then \(\widetilde D_B(W)\ge \pi/2\)【655:0†manuscript_v37.pdf†L1-L10】.

This is already exactly the “off‑axis quartet ⇒ endpoint ≥ constant” forcing shape required by Batch‑7 Task A (with \(c_\Phi=\pi/2\) and \(\mathrm{Err}\equiv 0\)).

### A2. Making the (S5′–FORCE) hypothesis of the budget theorem **non‑conditional**

The S5′ budget theorem (Theorem 12.3) is formulated for an abstract “boundary phase endpoint functional” \(\widetilde D_B\) and assumes a forcing hypothesis (S5′–FORCE) of the form
\(\widetilde D_B(W)\ge c_{\mathrm{force}}-\delta\,\Xi(m)\).

**Patchable conclusion:** once we set \(\widetilde D_B\equiv\widetilde D_B(W)\) as in Definition 12.16, the forcing hypothesis can be declared **discharged** by Lemma 12.17.

The only remaining “interface” obligation is to ensure the off‑axis quartet produces (equivalently) a zero of \(W\) in \(B_{\kappa/2}^\circ\). Under the manuscript’s aligned‑box setup, this is the intended mapping: nontrivial zeros of \(E\) in the box correspond to zeros of \(W=E/G_{\mathrm{out}}\) (since \(G_{\mathrm{out}}\) is zero‑free on the admissible collar). Lemma 12.17 explicitly states “equivalently, \(E\) has a zero there”【655:0†manuscript_v37.pdf†L1-L4】.

Moreover, the manuscript already includes the general existence of a \(\kappa\)-admissible shrink around any center (Lemma 10.6)【681:8†manuscript_v37.pdf†L96-L113】, which is the mechanism used whenever admissibility is needed.

### A3. Domination transfer lemma for *alternative* endpoints \(\Phi_B\)

If ENVELOPE proposes a different endpoint \(\Phi_B\) (still in the “phase/winding” class), forcing can transfer **only** under an explicit domination hypothesis.

**Transfer criterion (referee-grade):**

> If an S5′ endpoint \(\Phi_B\) satisfies
> \[
> \Phi_B(W)\ \ge\ \widetilde D_B(W)\qquad\text{for every \(\kappa\)-admissible aligned box \(B\)},
> \]
> then Lemma 12.17 immediately implies the forcing bound
> \(
> \Phi_B(W)\ge \pi/2
> \)
> whenever \(W\) has a zero in \(B_{\kappa/2}^\circ\).

This is the **only** safe way to “replace the contradiction endpoint” without changing forcing architecture.

### A4. NO‑GO classification when neither (direct forcing) nor (domination) is available

If \(\Phi_B\) does **not** dominate \(\widetilde D_B\) and no new forcing lemma targets \(\Phi_B\), then the architecture fails the forceability gate:

* forcing produces a lower bound on one quantity (\(\widetilde D_B\) or legacy \(D_B\)),
* the envelope upper bound controls a different quantity (\(\Phi_B\)),
* and **no implication links them**.

This is exactly the “logical disconnect” warning already recorded in v37 (Remark 12.18)【655:1†manuscript_v37.pdf†L1-L19】.

**Verdict:** such a \(\Phi_B\) is **NO‑GO as a contradiction endpoint** unless it is used purely as an *upper‑bound helper* while the forced endpoint remains \(\widetilde D_B(W)\) (or the legacy \(D_B(W)\)).

## 2) Task B — Collar nonvanishing and \(\lambda\)-shift policy

### B1. Collar nonvanishing for the phase endpoint (buffered boundary)

The buffered endpoint is designed precisely to avoid branch/zero issues.

* v37 defines \(\widetilde D_B(W)\) only under \(\kappa\)-admissibility: \(\mathrm{dist}(\partial B,Z(E))\ge \kappa\delta\)【681:8†manuscript_v37.pdf†L77-L85】.
* Under this condition, \(E\) has no zeros in a collar neighborhood of the boundary, hence \(W\) is holomorphic and nonzero on a neighborhood of \(\partial B_{\kappa/2}\) and phase increments are well‑defined by Definition 12.8 (\(\Delta_\Gamma\arg f := \Im\int_\Gamma f'/f\,dv\))【681:10†manuscript_v37.pdf†L4-L16】.

This makes the phase endpoint branch‑safe: the integral definition is independent of the choice of continuous branch of \(\log f\) on the curve.

### B2. \(\lambda\)-shift policy (interior vertical segments)

v37 introduces a shifted segment \(I_{+,\lambda}\) (Definition 12.11)【681:2†manuscript_v37.pdf†L3-L6】 to support phase‑split estimates (Lemma 12.12)【681:2†manuscript_v37.pdf†L7-L43】.

However, the parenthetical sentence in Definition 12.11 is geometrically misleading under the manuscript’s box convention \(B(\alpha,m,\delta)=\{\|v-(\alpha+im)\|_\infty\le\delta\}\)【681:8†manuscript_v37.pdf†L99-L112】:

* \(I_{+,\lambda}\) is at horizontal distance \(\lambda\delta\) from the central vertical line \(I_+\),
* but its distance to \(\partial B\) is controlled by \((1-\lambda)\delta\), not \(\lambda\delta\).

**Policy recommendation (minimal, proof-grade):**

1. Keep Definition 12.11 but correct the parenthetical to avoid confusion.
2. Treat \(\lambda\in(0,1)\) as a *shift parameter to avoid singularities on the unshifted line*, not as a collar parameter.
3. When Lemma 12.12 requires “\(E,Z_{\mathrm{loc}},F\) holomorphic and nonvanishing on a neighborhood of \(I_{+,\lambda}\),” explicitly note that this is satisfied whenever \(I_{+,\lambda}\) avoids the **finite** set of zeros/poles in the box; hence a valid choice of \(\lambda\) always exists (and the bounds in Corollary 12.13 are uniform in \(\lambda\))【681:2†manuscript_v37.pdf†L44-L52】.

This avoids any illicit “principal value” argument across zeros.

## 3) Task C — Explicit compatibility note (forcing ↔ envelope)

The v37 forcing lemma is now cleanly pinned to a specific object:

\[
\text{(off-axis quartet)}\ \Rightarrow\ \exists\ \kappa\text{-admissible aligned }B\text{ with }W\text{ zero in }B_{\kappa/2}^\circ\ \Rightarrow\ \widetilde D_B(W)\ge \pi/2.
\]

Therefore, the only forceable S5′ route is:

* **Envelope must upper bound** this same \(\widetilde D_B(W)\) (or a dominating endpoint \(\Phi_B\ge\widetilde D_B\)).
* The S5′ tail/budget theorem must be read with \(\widetilde D_B\equiv\widetilde D_B(W)\) and with (S5′–FORCE) treated as **discharged**.

This is consistent with v37’s own warning: if you redefine the contradiction endpoint away from the forced quantity without a transfer lemma, the proof chain breaks (Remark 12.18)【655:1†manuscript_v37.pdf†L1-L19】.

## 4) S6 harness check — explicit formula interpretation (phase endpoints)

v37 already includes an explicit‑formula interpretation appendix framing off‑axis zeros as “amplitude leaks,” with the correct frame mapping \(v_\rho=(2\beta-1)+i2\gamma\) and displacement \(a=2\beta-1\)【681:5†manuscript_v37.pdf†L62-L70】.

**Interpretation:** the forced endpoint \(\widetilde D_B(W)\) is a *winding/argument* diagnostic. It detects the presence of an interior zero topologically (via argument principle), not by measuring the explicit‑formula amplitude \(x^\beta\) directly. Any “amplitude leak” link is therefore **indirect**: the off‑axis quartet that creates an \(x^\beta\) term also creates an interior \(v\)-zero, which forces winding.

## 5) Paste‑ready TeX edits for v38 insertion (surgical)

### (i) Corollary: discharge (S5′–FORCE) for the buffered endpoint

```tex
% --- Insert immediately after Lemma 12.17 ---
\begin{corollary}[S5$'$ forcing is automatic for the buffered phase endpoint]
\label{cor:S5prime-force-automatic}
Let $B=B(\alpha,m,\delta)$ be a $\kappa$--admissible aligned box and let $W$ be its boundary quotient.
Define $\widetilde D_B(W)$ as in Definition~\ref{def:buffered-phase-endpoint}.
If $W$ has at least one zero in $B_{\kappa/2}^\circ$ (equivalently, $E$ has at least one zero there), then
\[
\widetilde D_B(W)\ge \pi/2.
\]
In particular, in Theorem~\ref{thm:S5prime-budget}, the hypothesis \textup{(S5$'$--FORCE)}
may be taken with $c_{\mathrm{force}}:=\pi/2$ and $\Xi(m)\equiv 0$ when
$\mathcal D_B\equiv \widetilde D_B$.
\end{corollary}
```

### (ii) Definition 12.11 parenthetical correction (\(\lambda\)-shift hygiene)

```tex
% --- Replace the parenthetical sentence in Definition 12.11 ---
(\emph{This lies strictly inside $B$. It is separated from the unshifted vertical line
$I_+=\{\alpha+iy:|y-m|\le\delta\}$ by horizontal distance $\lambda\delta$, and its distance to $\partial B$
 is at least $(1-\lambda)\delta$.})
```

### (iii) Forceability gate remark (phase endpoint variant)

```tex
% --- Add near Remark 12.18 (or in the S5' frontier gate list) ---
\begin{remark}[Forceability gate for phase endpoints]
\label{rem:forceability-gate-phase}
The single-box forcing chain in this manuscript supplies a lower bound only for a \emph{forced endpoint}.
For S5$'$ we have a direct forcing lemma for the buffered phase endpoint
$\widetilde D_B(W)$ (Lemma~\ref{lem:phase-forcing-argprinciple}).
Consequently, any proposed S5$'$ contradiction endpoint $\Phi_B$ is admissible only if either
\begin{enumerate}
\item $\Phi_B(W)\ge \widetilde D_B(W)$ on every $\kappa$--admissible aligned box (so forcing transfers), or
\item a new forcing lemma is proved that targets $\Phi_B$ directly.
\end{enumerate}
Without such a link, the forcing half and envelope half of the S5$'$ budget theorem are logically
 disconnected.
\end{remark}
```

## Mandatory final section — Patch Packet

* Callsign: RH-FORCE
* Result classification: **PASS** (for S5′ phase endpoint forceability), with a **NO‑GO gate** for any endpoint not dominating \(\widetilde D_B\)
* Target gaps closed (by ID): **(forceability attachment for S5′ phase endpoints / “missing lever usability” gate)**
* Target gaps still open (by ID): **ENVELOPE-side endpoint upper control** (not in RH‑FORCE scope); any transfer beyond domination is open
* Key conclusions (≤5 bullets):
  1. v37 already contains a proof‑grade direct forcing lemma: interior zero in \(B_{\kappa/2}^\circ\) forces \(\widetilde D_B(W)\ge \pi/2\) (Lemma 12.17).
  2. Therefore, if ENVELOPE uses \(\Phi_B\equiv\widetilde D_B\), the S5′ forcing hypothesis is discharged with \(c_\Phi=\pi/2\), \(\mathrm{Err}\equiv 0\).
  3. Any alternative endpoint \(\Phi_B\) is **invalid as a contradiction endpoint** unless it dominates \(\widetilde D_B\) or comes with a new forcing lemma.
  4. \(\kappa\)-admissibility provides the collar nonvanishing needed for branch‑safe phase integrals; \(\lambda\)-shifts should be treated as singularity‑avoidance, not collar control.
  5. Phase/winding endpoints do not directly encode an explicit‑formula \(x^\beta\) amplitude leak; they detect interior zeros topologically.
* Paste-ready manuscript edits (TeX blocks):
  (i) revised lemma/proposition statements: **Corollary `cor:S5prime-force-automatic`** (above)
  (ii) revised definitions/remarks: **Definition 12.11 parenthetical correction** + **Remark `rem:forceability-gate-phase`** (above)
  (iii) revised theorem/inequality lines: none in this branch (budget theorem remains conditional on envelope side)
* Dependencies on other branches:
  - RH-ENVELOPE must upper bound \(\widetilde D_B(W)\) (or an endpoint \(\Phi_B\ge\widetilde D_B\)) with δ‑uniform constants compatible with the acceptance gate.
  - RH-ABSORB/BUDGET must confirm the acceptance gate remains correctly parameterized for a phase endpoint (no hidden δ‑loss).
* Referee risk notes (anticipated objections + how addressed):
  - **Objection:** “You replaced the contradiction endpoint; forcing no longer applies.”
    *Answer:* forcing applies directly to \(\widetilde D_B\) via Lemma 12.17; the new remark gates any endpoint swap without domination/forcing.
  - **Objection:** “Phase increments are branch‑dependent / cross zeros.”
    *Answer:* \(\kappa\)-admissibility + buffered contour ensure nonvanishing on the integration curve; Definition 12.11 comment is corrected and the \(\lambda\) shift is treated as a zero‑avoidance parameter.
  - **Objection:** “Where do you get a \(\kappa\)-admissible box?”
    *Answer:* Lemma 10.6 provides existence of a \(\kappa\)-admissible shrink around any center, and the program explicitly shrinks when needed.
