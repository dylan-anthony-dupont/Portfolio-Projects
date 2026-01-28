# v39 Patch Queue — Batch‑9 (paste‑ready skeletons + insertion order)

**Date:** 2026-01-26  
**Baseline:** v38 locked manuscript  
**Goal:** install defect tooling + resonance NO‑GO + Missing Lever rewrite (no closure claims)

---

## Patch 1 — Defect primitives (Definitions)

**Insert near the S5′ “Missing Lever” region (same chapter as phase endpoint).**

```tex
% --- Defect primitives (v39) ---
\begin{definition}[Defect quotient and defect log-derivative]
Let $E$ be the even entire width--2 completion fixed in v38.
For $a\in(0,1)$ define
\[
\mathcal Q_a(v):=\frac{E(v+a)}{E(v-a)},\qquad
\mathcal L_a(v):=\frac{\mathcal Q_a'(v)}{\mathcal Q_a(v)}
=\frac{E'}{E}(v+a)-\frac{E'}{E}(v-a).
\]
\end{definition}

\begin{definition}[Defect phase endpoint on a box]
Let $B=B(\alpha,m,\delta)$ be a $\kappa$--admissible box and let $\partial B_{\kappa/2}$
denote its buffered contour.
Define
\[
\Phi_B^{\rm def}(a):=
\max_{I\in\mathrm{Sides}(\partial B_{\kappa/2})}
\left|\Im\int_I \mathcal L_a(v)\,dv\right|.
\]
\end{definition}
```

**Dependencies:** none (uses existing v38 `E`, `B`, `\partial B_{\kappa/2}`).

---

## Patch 2 — Local cancellation lemma (removable singularity + pair term)

**Insert immediately after Patch 1.**

```tex
\begin{lemma}[Local cancellation for the defect kernel]
Assume $E$ has a symmetric pair of zeros at $v=\pm a+i m$ (multiplicity $r$).
Then $\mathcal Q_a$ has a removable singularity at $v=i m$ and $\mathcal L_a$ is holomorphic
in a neighborhood of $v=i m$.
Moreover, on a vertical segment $I_0:=\{v=i y:|y-m|\le \delta\}$ one has the explicit pair bound
\[
\left|\Im\int_{I_0} \mathcal L_a^{\rm pair}(v)\,dv\right|
\le 2r\,\frac{\delta}{a}.
\]
\end{lemma}
```

**Remark (optional):** add “this is the forced‑zero obstruction: a single quartet does not force a defect endpoint on the aligned box.”

---

## Patch 3 — Collar safety for shifted boxes (Bridge tooling)

**Insert as the first lemma in the “Defect UE” subsection.**

```tex
\begin{lemma}[Collar safety under shifts]
If $\partial B_{\kappa/2}$ is $\kappa$--admissible for $E$, then the shifted contours
$\partial B_{\kappa/2}\pm a$ avoid zeros of $E$ by a quantitative margin.
In particular, $\mathcal L_a$ is analytic on $\partial B_{\kappa/2}$ and the integrals defining
$\Phi_B^{\rm def}(a)$ are well-defined.
\end{lemma}
```

```tex
\begin{lemma}[Difference-kernel bound]
For $v$ away from the local tube of zeros one has the representation
\[
\mathcal L_a(v)=\sum_{\rho}\left(\frac{1}{v+a-\rho}-\frac{1}{v-a-\rho}\right)+\text{(entire remainder)},
\]
and the coarse estimate
\[
\left|\frac{1}{v+a-\rho}-\frac{1}{v-a-\rho}\right|\lesssim \frac{a}{|v-\rho|^2}.
\]
\end{lemma}
```

---

## Patch 4 — Defect UE skeleton (Envelope)

**Insert after Patch 3.**

```tex
\begin{definition}[Horizontal resonance sum]
Fix $m$ and $a\in(0,1)$. Define
\[
R_a(m):=\sum_{\rho:\,|\Im\rho-m|\le 1}\frac{1}{|a-\Re\rho|+a}.
\]
\end{definition}

\begin{lemma}[Defect upper envelope skeleton]
There exist absolute constants $C_0,C_1$ such that for any $\kappa$--admissible $B=B(0,m,\delta)$,
\[
\Phi_B^{\rm def}(a)\le C_0\,\delta\,\log m + C_1\,\delta a\,R_a(m).
\]
\end{lemma}
```

**Note:** this is the “Missing Lever reducer” — it reduces the UE problem to bounding $R_a(m)$.

---

## Patch 5 — Resonance NO‑GO (δ‑inert countermodel)

**Insert as an explicit boxed remark or lemma immediately after Patch 4.**

```tex
\begin{lemma}[NO--GO: near-resonant quartets can make defect endpoints $\delta$--inert]
There exist entire even toy factors $E_{\varepsilon}$ with two quartets at displacements
$a$ and $a-\varepsilon$ (with $\varepsilon\asymp\delta$) such that for the aligned box $B(0,m,\delta)$,
\[
\Phi_B^{\rm def}(a)\ge c_0
\]
for an absolute constant $c_0>0$ independent of $\delta$.
Consequently, any proof of $\eta$--shrinking defect UE must control/exclude such near-resonant behavior.
\end{lemma}
```

---

## Patch 6 — Replace the “Missing Lever” box (ABSORB → CR rewrite)

**Replace the existing v38 boxed statement.**

```tex
\begin{mdframed}[style=OpenBox]
\textbf{OPEN (Missing Lever, v39).}
To close the phase-class route it suffices to prove:
\begin{enumerate}
\item \textbf{Domination:} a referee-grade bound
$\widetilde D_B(W)\le C_{\rm dom}\,\Phi_B^{\rm def}(a)+\mathrm{Err}(\delta,m,a)$.
\item \textbf{Defect UE:} an absolute-constant inequality
$\Phi_B^{\rm def}(a)\le C\,\delta\log m + C\,\delta a\,R_a(m)$, uniform for $0<\delta\le\delta_0(m,a)$.
\item \textbf{Resonance control:} show $R_a(m)$ (or $N_{\rm near}$) is bounded in the regime above so that the
gate constraints $2p\ge 1$, $2(p-\theta)\ge q$, $p-\theta>0$ pass with $(p,\theta,q)=(1,0,1)$.
\end{enumerate}
\emph{NO--GO latches:} (i) one-pole phase endpoints cannot yield $p>0$; (ii) near-resonant quartets can make defect endpoints $\delta$--inert.
\end{mdframed}
```

---

## Patch 7 (optional / harness) — Pole-winding forcing for defect quotient

**Only if included, label as “diagnostic/harness” (not used for UE shrinking).**

```tex
\begin{lemma}[Harness: pole-winding forcing for $\mathcal Q_a$]
If $E$ has a zero at $v=a+i m$, then $\mathcal Q_a$ has a pole at $v=2a+i m$.
Under collar admissibility on a defect box centered at $2a+i m$, the argument principle implies
a forced winding and hence a side with phase increment at least $\pi/2$.
\end{lemma}
```

