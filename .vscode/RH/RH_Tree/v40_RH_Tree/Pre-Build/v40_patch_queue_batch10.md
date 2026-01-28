# v40 Patch Queue — Batch 10 + legacy synthesis (paste-ready TeX)

**Date:** 2026-01-28  
**Integrator:** RH‑CR  
**Base:** `manuscript_v39.tex` (locked)

> **Protocol:** Apply patches in order. Each patch is designed to be minimal and truth‑latching. If a label already exists, keep the existing label and adjust only the statement text.

---

## Patch 40.1 — NO‑GO latch: centered/same‑box transfer fails (ML‑1 in v39 form is impossible)

**Insert near** the S5′ “Missing Lever” frontier (right before Box `box:missing-lever-v39`), or in the “Discarded closure routes” appendix with a forward reference.

```tex
\begin{lemma}[NO--GO: no $\delta$--uniform transfer to the centered defect box]
  \label{lem:ML1-samebox-nogo}
  Fix $\kappa\in(0,1/10)$. There do not exist constants $C_{\rm tr}>0$ and an absorbable error
  ${\rm Err}(m,a,\delta)=o_{m\to\infty}(1)$ (uniform for $\delta=\delta_0(m,a)=\eta a/(\log m)^2$)
  such that for every $\kappa$--admissible forcing box $B=B(\pm a,m,\delta)$ and the centered box
  $\widehat B=B(0,m,\delta)$ one has
  \[
  \widetilde D_{B}(W)\ \le\ C_{\rm tr}\,\Phi^{\rm def}_{\widehat B}(a)\ +\ {\rm Err}(m,a,\delta).
  \]
  In particular, ML--1 cannot be discharged with $\widehat B=B(0,m,\delta)$ under the current hypotheses.
  \end{lemma}

  \begin{proof}
  Consider the even entire model
  $E(v)=\prod_{\sigma,\tau\in\{\pm1\}}\bigl(v-\sigma(a+i\tau m)\bigr)$.
  Choose $\delta\le a/4$ so that $B(\pm a,m,\delta)$ and $B(0,m,\delta)$ are $\kappa$--admissible.
  Then $E$ (hence $W$) has a zero in $B(a,m,\delta)_{\kappa/2}^\circ$, so
  $\widetilde D_{B(a,m,\delta)}(W)\ge \pi/2$ by Lemma~\ref{lem:phase-forcing-argprinciple}.
  On the centered box $\widehat B=B(0,m,\delta)$, Lemma~\ref{lem:defect-cancellation} gives
  $\Phi^{\rm def}_{\widehat B}(a)\le C\,\delta/a+\delta\|H(\cdot+a)-H(\cdot-a)\|_\infty=O(\delta/a)$.
  Under $\delta=\delta_0(m,a)=\eta a/(\log m)^2$ the RHS is $O(1/(\log m)^2)\to0$ as $m\to\infty$,
  contradicting any transfer inequality with $\delta$--uniform $C_{\rm tr}$ and absorbable ${\rm Err}$.
  \end{proof}
```

---

## Patch 40.2 — Missing Lever box item update: remove “centered box transfer” from OPEN list

**Replace** the ML‑1 bullet in Box `box:missing-lever-v39` with the following “NO‑GO latched” wording:

```tex
% In Box~\ref{box:missing-lever-v39}, item (Transfer / domination):
  % replace D_B(W) by \widetilde D_B(W) and record the centered-box NO--GO.

  \item \textbf{(Transfer / domination)} Prove a domination link that connects the forced phase endpoint
  $\widetilde D_B(W)$ to the UE--friendly \emph{defect} endpoint class:
  \[
  \widetilde D_B(W)\ \le\ C_{\rm tr}\,\Phi^{\rm def}_{\widehat B}(a)\ +\ {\rm Err}(m,a,\delta),
  \]
  for every $\kappa$--admissible aligned box $B=B(\pm a,m,\delta)$ at the nominal scale
  $0<\delta\le \delta_0(m,a)=\eta\,a/(\log m)^2$.
  \emph{NO--GO:} choosing $\widehat B=B(0,m,\delta)$ (or any $O(\delta)$ shift away from the defect singularities
  $v=\pm(2a+i m)$) cannot yield a $\delta$--uniform transfer; see Lemma~\ref{lem:ML1-samebox-nogo}.
```

---

## Patch 40.3 — Editorial remark: why \widehat{B}=B(0,m,\delta) fails (bridge rationale)

```tex
\begin{remark}
  Lemma~\ref{lem:ML1-samebox-nogo} shows $\Phi^{\rm def}_{B(0,m,\delta)}(a)$ does not dominate the forced endpoint
  $\widetilde D_B(W)$; any forcing transfer to defect endpoints must therefore use different geometry (a box enclosing
  a genuine zero/pole of $\mathcal Q_a$) or add new hypotheses beyond $\kappa$--admissibility.
  \end{remark}
```

---

## Patch 40.4 — NO‑GO latch: defect endpoint has a side-length ceiling (no p>1 from pointwise UE)

**Insert near** Lemma `lem:UE-scaling-nogo` or immediately after it.

```tex
% New lemma (NO-GO for p>1 in the current defect endpoint class)
  \begin{lemma}[Side-length ceiling for the defect phase endpoint]\label{lem:defect-p-ceiling}
  Fix $a\in(0,1]$ and let $B=B(0,m,\delta)$ be a $\kappa$-admissible aligned box with buffered contour $\partial B_{\kappa/2}$.
  Assume $\mathcal L_a$ is holomorphic on an open neighborhood of $\partial B_{\kappa/2}$.
  Then
  \[
    \Phi_B^{\rm def}(a)\ \le\ C_{\rm geom}\,\delta\cdot \sup_{v\in\partial B_{\kappa/2}}|\mathcal L_a(v)|,
  \]
  where $C_{\rm geom}>0$ is an absolute rectangle-shape constant.
  In particular, any proof of $\Phi_B^{\rm def}(a)\ll \delta^p(\cdots)$ obtained solely from $\delta$-uniform pointwise bounds on
  $\sup_{\partial B_{\kappa/2}}|\mathcal L_a|$ cannot have $p>1$.
  \end{lemma}
```

---

## Patch 40.5 — δ-aware resonance primitive (replace δ-blind proxy)

**Insert after** Def. `def:defect-endpoint` (or in the same subsection).

```tex
% Replace Def. 12.5 by a delta-aware resonance sum (or add as Def. 12.5*)
  \begin{definition}[$\delta$-aware horizontal resonance sum (local window)]\label{def:resonance-sum-delta}
  For $a\in(0,1]$, $m\ge 10$, and $0<\delta\le a/4$, define
  \[
    \mathcal R_{a,\delta}(m)
    \ :=\
    \sum_{\rho:\,E(\rho)=0,\ |\Im(\rho)-m|\le 1}
    \frac{1}{|\Re(\rho)-a|+\delta},
  \]
  where zeros are counted with multiplicity.
  Then $\mathcal R_{a,\delta}(m)\le \delta^{-1}N_{\rm loc}(m)$.
  \end{definition}

  % Replace Remark 12.6 by a delta-aware target bound
  \begin{remark}[Target defect UE bound (OPEN; $\delta$-aware)]\label{rem:defect-UE-target-delta}
  A defect upper-envelope bound consistent with the resonance NO--GO (Lemma~\ref{lem:defect-resonance-nogo})
  should have the schematic form
  \[
    \Phi_B^{\rm def}(a)\ \le\ C_0\,\delta\log m\ +\ C_1\,\delta\,\mathcal R_{a,\delta}(m),
  \]
  uniformly for $0<\delta\le \delta_0(m,a)=\eta a/(\log m)^2$, with $C_0,C_1$ independent of $(m,a,\delta)$.
  In the toy-model configuration behind Lemma~\ref{lem:defect-resonance-nogo}, one has $\mathcal R_{a,\delta}(m)\gg 1/\delta$,
  so the right-hand side is $\gg 1$ and the bound does not contradict $\delta$-inertness.
  \end{remark}
```

---

## Patch 40.6 — Missing Lever box: remove the “p>1 / δ^{3/2}” slogan (envelope hygiene)

```tex
% Patch Box 12.1: reconcile the p>1 phrase with the actual target scaling of Def. 12.2
  % (Minimal edit: remove the p>1 numeric claim and instead refer to "gate passing" via Theorem 12.12.)
  % Replace:
  %   "If (Transfer) and (Defect UE) are proven in a regime with effective p>1 (gate passing), ..."
  % By:
  %   "If (Transfer) and (Defect UE) are proven in a gate-passing regime (in the sense of Theorem~12.12),
  %    and (Resonance control) supplies the needed $\delta$-uniformity, ..."
```

---

## Patch 40.7 — δ-awareness diagnosis (LOCAL): current \mathcal R_a is δ-blind; add near-resonance count

**Insert near** the resonance NO‑GO lemma and/or immediately after the current definition of \(\mathcal R_a(m)\).

```tex
\begin{definition}[Near-resonance count at scale $\delta$]\label{def:near-resonance-count}
  Fix $a\in(0,1)$, $m\ge 10$, and $0<\delta\le a/4$. Define
  \[
    N_{\rm res}(a,m,\delta)
    :=\#\Bigl\{\rho:\ E(\rho)=0,\ |\Im\rho-m|\le 1,\ 0<\bigl||\Re\rho|-a\bigr|\le 2\delta\Bigr\},
  \]
  counting zeros with multiplicity. We say the local window is \emph{$\delta$-nonresonant at $(a,m)$}
  if $N_{\rm res}(a,m,\delta)=0$.
  \end{definition}
```

```tex
\begin{remark}[Why $\mathcal R_a(m)$ is $\delta$-blind for resonance]\label{rem:Ra-deltablind}
  Lemma~\ref{lem:defect-resonance-nogo} exhibits an even entire $E_\varepsilon$ with a second quartet at
  real part $a-\varepsilon$ (with $\varepsilon\asymp \delta$) such that $\Phi^{\rm def}_{B(0,m,\delta)}(a)\ge c_0>0$
  uniformly in $\delta,\varepsilon$. In that example, however, $\mathcal R_a(m)$ remains $O(1/a)$
  (independent of $\varepsilon$), so the term $\delta a\,\mathcal R_a(m)$ is $O(\delta)\to 0$.
  Therefore any defect-UE inequality of the schematic form in Remark~\ref{rem:defect-UE-target}
  must incorporate a $\delta$-aware resonance control term/hypothesis (e.g.\ $N_{\rm res}(a,m,\delta)$).
  \end{remark}
```

```tex
\item[(ML-3) Resonance control.] Provide a $\delta$-aware resonance control that rules out the
  $\delta$-inert configuration of Lemma~\ref{lem:defect-resonance-nogo}. For example, prove that
  the local window is $\delta_0(m,a)$-nonresonant at every $(a,m)$ (Definition~\ref{def:near-resonance-count}),
  or else replace the defect-UE target by a bound that explicitly depends on the near-resonance count.
```

---

## Patch 40.8 — NO‑GO latch: defect-box pole-winding cannot replace ML‑1

**Insert near** the forcing lemmas (end of S5 forcing subsection) and reference it from the Missing Lever box.

```tex
\begin{lemma}[NO--GO: defect-box pole-winding cannot replace ML--1]\label{lem:defectbox-nogo-ML1}
Fix $\kappa\in(0,1/10)$ and let $a\in(0,1)$, $m>0$.
Assume $E$ is the even entire width--2 completion and that $E$ has a quartet at
$\pm a\pm i m$ (so $E(a+i m)=E(-a+i m)=0$ with multiplicities $\ge 1$).
Define $\mathcal Q_a(v)=E(v+a)/E(v-a)$ and let $\Phi^{\rm def}_{B}(a)$ be the defect phase endpoint
(Definition~\ref{def:defect-endpoint}).

Let $\widehat B=B(2a,m,\delta)$ be any $\kappa$--admissible aligned box with
$0<\delta\le a/4$ such that:
(i) $\partial \widehat B_{\kappa/2}$ contains no zeros or poles of $\mathcal Q_a$, and
(ii) $\widehat B_{\kappa/2}$ contains the point $v_0:=2a+i m$ but contains no other zero/pole of $\mathcal Q_a$.

Then $\mathcal Q_a$ has a pole in $\widehat B_{\kappa/2}$ and the argument principle yields
\[
\Big|\Delta_{\partial\widehat B_{\kappa/2}}\arg \mathcal Q_a\Big|=2\pi.
\]
Consequently,
\[
\Phi^{\rm def}_{\widehat B}(a)\ \ge\ \frac{\pi}{2},
\]
independently of $\delta$.

In particular, \emph{no} inequality of the form
$\Phi^{\rm def}_{\widehat B}(a)\le C\,\delta^p(\log m)^q$ with $p>0$ and $C$ independent of $\delta$
can hold uniformly as $\delta\to 0$ on this defect-box family. Hence defect-box pole-winding forcing
cannot be used as a $\delta$--shrinkable UE mechanism and therefore cannot replace ML--1 in the v39
architecture.
\end{lemma}

\begin{proof}
Since $E(a+i m)=0$, the denominator $E(v-a)$ vanishes at $v_0=2a+i m$, so $\mathcal Q_a$ has a pole at $v_0$.
Under (i)--(ii), $\mathcal Q_a$ is meromorphic in a neighborhood of $\partial\widehat B_{\kappa/2}$ with exactly one
pole and no zeros/poles on the contour. The argument principle gives total phase change $2\pi$ in magnitude around
$\partial\widehat B_{\kappa/2}$. Since $\partial\widehat B_{\kappa/2}$ is the concatenation of four oriented sides,
at least one side has phase increment magnitude at least $\pi/2$. By definition of $\Phi^{\rm def}_{\widehat B}(a)$
as the max side increment, $\Phi^{\rm def}_{\widehat B}(a)\ge\pi/2$. The final incompatibility with any $p>0$
$\delta$--gain is immediate.
\end{proof}
```

---

# Patch 40.9 — NEW endpoint class: two‑sided shift‑difference operator (S5Δa)

**Insert** in the S5 section immediately after Def. `def:defect-quotient` and Def. `def:defect-endpoint`.

```tex
\begin{definition}[Two-sided shift-difference defect operator]\label{def:two-sided-shift-diff}
Let \(E\) be the even entire completion in the \(v\)-plane, and define the defect quotient and defect log-derivative
\[
\mathcal Q_a(v):=\frac{E(v+a)}{E(v-a)},\qquad
\mathcal L_a(v):=\frac{\mathcal Q_a'(v)}{\mathcal Q_a(v)}
=\frac{E'}{E}(v+a)-\frac{E'}{E}(v-a).
\]
For a shift step \(h>0\), define the two-sided shift-difference operator
\[
\mathcal D_{a,h}(v):=\mathcal L_{a+h}(v)-\mathcal L_{a-h}(v).
\]
Equivalently,
\[
\mathcal D_{a,h}(v)=\frac{E'}{E}(v+a+h)-\frac{E'}{E}(v+a-h)-\frac{E'}{E}(v-a+h)+\frac{E'}{E}(v-a-h).
\]
\end{definition}
```

---

## Patch 40.10 — NEW endpoint: two‑sided shift‑difference phase endpoint

**Insert** right after Def. `def:two-sided-shift-diff`.

```tex
\begin{definition}[Two-sided shift-difference phase endpoint]\label{def:two-sided-endpoint}
Fix \(\kappa\in(0,1/10)\). For a \(\kappa\)-admissible aligned box \(B=B(\alpha,m,\delta)\) and parameters \((a,h)\), define
\[
\Phi^{(2\mathrm{s})}_B(a;h)
:=\max_{I\in\mathrm{Sides}(\partial B_{\kappa/2})}
\left|\Im\int_I \mathcal D_{a,h}(v)\,dv\right|.
\]
In the nominal coupling used in this program we take \(h=\delta\) and \(\delta=\delta_0(m,a):=\eta a/(\log m)^2\).
\end{definition}
```

---

## Patch 40.11 — NEW boxed open statement: replace v39 Missing Lever triad with ML‑Δa

**Replace** Box `box:missing-lever-v39` by the following v40 box.

```tex
\begin{tcolorbox}[title=Missing Lever (v40): non-pointwise shift-difference closure, colback=white]\label{box:missing-lever-v40}
\textbf{Goal.} Replace the v39 transfer/defect-UE/resonance triad by a single redesigned endpoint obligation.

\medskip
\textbf{Setup.} Let \(\mathcal D_{a,h}\) and \(\Phi^{(2\mathrm{s})}_B(a;h)\) be as in Defs.~\ref{def:two-sided-shift-diff}--\ref{def:two-sided-endpoint}, and take the nominal coupling
\[
h=\delta,\qquad \delta=\delta_0(m,a):=\eta \frac{a}{(\log m)^2}.
\]

\medskip
\textbf{(ML-\(\Delta a\)) Required statements (OPEN).}
\begin{enumerate}
\item \textbf{Forcing.} If \(E\) has an off-axis quartet at height \(m\) with tilt \(a>0\), then there exists a \(\kappa\)-admissible aligned box \(B\) at that height such that
\[
\Phi^{(2\mathrm{s})}_B(a;h)\ge c_0
\]
for an absolute constant \(c_0>0\) (toy model suggests \(c_0\approx\pi/2\)).

\item \textbf{UE upper bound (gate passing).} For all such admissible \(B\),
\[
\Phi^{(2\mathrm{s})}_B(a;h)\le \mathrm{UE}(m,a,\delta,h),
\]
where \(\mathrm{UE}\) is \(\delta\)-uniform at the nominal scale and passes the exponent-budget gate (cf. Thm.~\ref{thm:exponent-budget} / Gate Calculator).

\item \textbf{Resonance robustness.} Near-resonant quartets at tilts \(a-\varepsilon\sim a-h\) cannot make \(\Phi^{(2\mathrm{s})}\) \(\delta\)-inert in a way that violates (2).
\end{enumerate}

\medskip
\textbf{NO-GO reminders.} Centered transfer to \(B(0,m,\delta)\) is impossible (Lemma~\ref{lem:ML1-samebox-nogo}); defect-box pole-winding forcing cannot substitute for transfer (Lemma~\ref{lem:defectbox-nogo-ML1}); and the pointwise defect endpoint \(\Phi^{\rm def}\) has a side-length ceiling (Lemma~\ref{lem:defect-p-ceiling}).
\end{tcolorbox}
```

---

## Patch 40.12 — S6 harness upgrade: interpret \mathcal D_{a,h} as an amplitude-leak derivative

**Insert** at the end of the S6 harness section (or add a short paragraph).

```tex
\paragraph{S6 cross-check for the two-sided endpoint.}
Recall that \(a=2\beta-1\) so that \(\beta=\tfrac12+\tfrac a2\). The operator \(\mathcal D_{a,h}=\mathcal L_{a+h}-\mathcal L_{a-h}\) is a finite difference in the tilt parameter, hence a finite difference in \(\beta\).
In explicit-formula language, this tests sensitivity to an \(x^\beta\) amplitude leak by comparing nearby \(\beta\)-values.
Accordingly, a successful ML-\(\Delta a\) closure can be interpreted as forbidding any persistent \(x^\beta\) leak with \(\beta>\tfrac12\).
```

---

## Patch 40.13 — (Optional) Discarded closure route: forceable endpoint \Phi^E_B (record as NO‑GO under current envelopes)

**Insert** in the “Discarded closure routes” appendix as a cautionary note.

```tex
\paragraph{Discarded route (current NO-GO): endpoint on \(E\) itself.}
One may consider \(\Phi^E_B:=\max_I|\Im\int_I (E'/E)\,dv|\), which is forceable by the argument principle (\(\ge\pi/2\) if \(B\) encloses a zero).
However, under the current local envelope for \(E'/E\), side integrals are \(\delta^0\)-scale and do not admit a shrinking UE bound \(<\pi/2\) without new local cancellation/isolation. We therefore treat this route as NO-GO in the present architecture.
```

---
