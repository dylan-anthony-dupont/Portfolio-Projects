# v37 Patch Queue — Batch 6 (S5′ phase endpoint integration)

Date: 2026-01-25  
Baseline: **v36 locked** (`manuscript_v36.tex`)  
Scope: integrate Batch‑6 patch packets into v37 as an **architecture build** (no closure claims).

---

## Patch order (apply sequentially)

### P37.1 — Insert “S5′ phase endpoint toolkit” subsection (BRIDGE + LOCAL + ENVELOPE)

**Placement:** in Section `sec:S5-frontier`, immediately after Remark `rem:s5-forceability-gate` and before Subsection `subsec:S5-nogo-baseline`.

**Edits (TeX blocks):**

```tex
% ============================================================
% S5' phase endpoint toolkit (no point evaluation)
% Insert after Remark~ef{rem:s5-forceability-gate}.
% ============================================================

\subsection{S5$'$ phase endpoints: winding / argument-increment toolkit}\label{subsec:S5prime-phase-toolkit}

egin{definition}[Phase increment on a boundary arc]\label{def:phase_increment}
Let $\Gamma\subset\C$ be a piecewise $C^1$ curve with a chosen orientation.
Let $f$ be holomorphic and nonvanishing on an open neighborhood of $\Gamma$.
Define the phase increment of $f$ along $\Gamma$ by
\[
\Delta_\Gammarg f \ :=\ \Im\int_\Gamma rac{f'(v)}{f(v)}\,dv,
\]
which equals the net change of a continuous argument of $f$ along $\Gamma$ (well-defined modulo $2\pi$).
\end{definition}

egin{lemma}[Phase increment identity and vertical specialization]\label{lem:phase_increment_identity}
In the setting of Definition~ef{def:phase_increment}, the phase increment satisfies
\[
\Delta_\Gammarg f \ =\ \Im\int_\Gamma rac{f'(v)}{f(v)}\,dv.
\]
In particular, on the near-vertical side $I_+:=\{lpha+i y:\ |y-m|\le \delta\}$ (parametrized by $v(y)=lpha+i y$),
\[
\Delta_{I_+}rg f
=\Im\int_{m-\delta}^{m+\delta}rac{f'(lpha+i y)}{f(lpha+i y)}\, i\,dy
=\int_{m-\delta}^{m+\delta}\Re\!\left(rac{f'(lpha+i y)}{f(lpha+i y)}ight)\,dy,
\]
and hence
\[
|\Delta_{I_+}rg f|
\le \int_{m-\delta}^{m+\delta}\left|rac{f'(lpha+i y)}{f(lpha+i y)}ight|\,dy
\le 2\delta\cdot \sup_{I_+}\left|rac{f'}{f}ight|.
\]
\end{lemma}

egin{remark}[Parentheses hygiene for phase endpoints]\label{rem:phase_parentheses_hygiene}
For a complex-valued integrand $h(v)$ and a complex line element $dv$, the phase functional is
$\Im\!\int_\Gamma h(v)\,dv$, not $\int_\Gamma \Im(h(v))\,dv$.
This distinction matters on vertical segments (where $dv=i\,dy$) and prevents notation-level errors.
\end{remark}

% --- optional shifted segment (ENVELOPE) ---
egin{definition}[Shifted near-vertical segment]\label{def:Iplus_lambda}
Let $B=B(lpha,m,\delta)$ be an aligned box and let $\lambda\in[0,1]$.
Define the shifted near-vertical segment
\[
I_{+,\lambda}:=\{lpha+\lambda\delta+i y:\ |y-m|\le\delta\}.
\]
\end{definition}

egin{lemma}[Phase split on $I_{+,\lambda}$]\label{lem:phase_split_Iplus_lambda}
Assume $I_{+,\lambda}$ contains no zero of $Z_{m loc}$, and that $E$, $Z_{m loc}$, and $F:=E/Z_{m loc}$
are holomorphic and nonvanishing on a neighborhood of $I_{+,\lambda}$.
Then
\[
\Delta_{I_{+,\lambda}}rg E
=\Delta_{I_{+,\lambda}}rg F + \Delta_{I_{+,\lambda}}rg Z_{m loc}.
\]
Moreover,
\[
ig|\Delta_{I_{+,\lambda}}rg Fig|
\le 2\delta\cdot \sup_{\partial B}\left|rac{F'}{F}ight|.
\]
\end{lemma}

egin{corollary}[Residual phase budget (δ-uniform)]\label{cor:residual_phase_budget}
Under the hypotheses of Lemma~ef{lem:phase_split_Iplus_lambda},
\[
ig|\Delta_{I_{+,\lambda}}rg Fig|
\le 2\delta\,(C_1\log m + C_2),
\]
where $(C_1,C_2)$ are the constants from Lemma~ef{lem:residual-envelope}.
\end{corollary}

egin{lemma}[Local phase is δ--inert: per-zero contribution is $O(1)$]\label{lem:local_phase_delta_inert}
Let $I_+$ be the near-vertical side and let $ho
otin I_+$.
Then
\[
\Im\int_{I_+}rac{dv}{v-ho}
= rg(lpha+i(m+\delta)-ho)-rg(lpha+i(m-\delta)-ho),
\]
and hence
\[
\left|\Im\int_{I_+}rac{dv}{v-ho}ight|\le \pi.
\]
Consequently, for $Z_{m loc}(v)=\prod_{ho\in Z(m)}(v-ho)^{m_ho}$ one has
\[
\left|\Delta_{I_+}rg Z_{m loc}ight|
=\left|\Im\int_{I_+}rac{Z'_{m loc}}{Z_{m loc}}\,dvight|
\le \pi\,N_{m loc}(m).
\]
\end{lemma}

egin{corollary}[Prototype phase upper bound]\label{cor:prototype_phase_upper}
If additionally $\sup_{I_+}|F'/F|\le L(m)$, then
\[
ig|\Delta_{I_+}rg Eig|
\le 2\delta\,L(m) + \pi N_{m loc}(m).
\]
\end{corollary}
```

---

### P37.2 — Add FORCE endpoint \(\widetilde D_B(W)\) on a buffered contour + forcing lemma

**Placement:** immediately after Subsection `subsec:S5prime-phase-toolkit` (still inside Section `sec:S5-frontier`).

**Edits (TeX blocks):**

```tex
% ============================================================
% FORCE: buffered boundary max-side phase endpoint and forcing lemma
% ============================================================

egin{definition}[Buffered boundary phase endpoint]\label{def:Db-tilde-phase}
Let $B=B(lpha,m,\delta)$ be an aligned box and assume $\kappa$--admissibility:
$\dist(\partial B, Z(E))\ge \kappa\delta$.
Let $G_{m out}$ be the Dirichlet outer factor on $B^\circ$ and $W:=E/G_{m out}$ the inner quotient.
Define the buffered inner rectangle
\[
B_{\kappa/2}:=\{v\in B:\dist(v,\partial B)\ge 	frac{\kappa\delta}{2}\},
\]
and write its oriented boundary as $\partial B_{\kappa/2}=igcup_{j=1}^4 S_j$ (counterclockwise).
Define the sidewise phase increment
\[
\Delta_{S_j}rg W := \Im\int_{S_j}rac{W'(v)}{W(v)}\,dv,
\]
and the phase endpoint
\[
\widetilde D_B(W):=\max_{1\le j\le 4}\Bigl|\Delta_{S_j}rg W\Bigr|.
\]
\end{definition}

egin{lemma}[Phase forcing from an interior zero]\label{lem:phase-forcing-argprinciple}
Assume the setup of Definition~ef{def:Db-tilde-phase}.
If $W$ has at least one zero in $B_{\kappa/2}^\circ$ (equivalently $E$ has at least one zero there), then
\[
\widetilde D_B(W)\ge rac{\pi}{2}.
\]
\end{lemma}

egin{proof}
Since $W$ is holomorphic and nonvanishing on a neighborhood of $\partial B_{\kappa/2}$,
the argument principle gives
\[
\oint_{\partial B_{\kappa/2}} rac{W'(v)}{W(v)}\,dv = 2\pi i\,N,
\]
where $N\ge 1$ is the number of zeros of $W$ in $B_{\kappa/2}^\circ$, counted with multiplicity.
Taking imaginary parts and decomposing $\partial B_{\kappa/2}$ into four sides yields
\[
\sum_{j=1}^4 \Delta_{S_j}rg W = 2\pi N \ge 2\pi.
\]
Hence at least one side satisfies $\Delta_{S_j}rg W\ge \pi/2$, so
$\max_j|\Delta_{S_j}rg W|\ge \pi/2$, i.e. $\widetilde D_B(W)\ge \pi/2$.
\end{proof}

egin{remark}[Forceability gate for phase endpoints]\label{rem:forceability-phase-gate}
The v36 forcing chain lower-bounds the dial deviation $D_B(W)$.
The phase endpoint $\widetilde D_B(W)$ above is not known to dominate $D_B(W)$ or vice-versa.
Therefore any redesign that adopts $\widetilde D_B$ must either:
(i) rewrite the tail inequality so that $\widetilde D_B$ is the forced object (using
Lemma~ef{lem:phase-forcing-argprinciple}), or
(ii) prove a transfer inequality relating $\widetilde D_B$ and $D_B(W)$ on all admissible boxes.
Without (i) or (ii), forcing and envelope are logically disconnected.
\end{remark}
```

---

### P37.3 — Add ABSORB’s S5′ closure theorem + acceptance gate remark (drift-proof)

**Placement:** in Section `sec:S5-frontier`, immediately after Theorem `thm:S5-budget` (companion/specialization).

**Edits (TeX blocks):**

```tex
% ============================================================
% ABSORB: S5' closure spine (budget-eligible phase endpoints)
% ============================================================

egin{theorem}[S5$'$ closure from a forceable phase endpoint]\label{thm:S5prime-closure}
Fix $\kappa\in(0,1/10)$ and $\eta\in(0,1)$ and define $\delta_0(m,lpha)=\etalpha/(\log m)^2$.
Let $\widetilde D_B$ be a boundary phase endpoint functional assigned to each $\kappa$--admissible
aligned box $B=B(\pm a,m,\delta)$ and its boundary quotient $W$.
Assume:
egin{enumerate}[leftmargin=1.5em]
  \item[(S5$'$--FORCE)] Under an off-axis quartet at height $m$ with displacement $a>0$,
  there exists an aligned $\kappa$--admissible box $B$ (with $lphapprox a$) such that
  $\widetilde D_B(W)\ge c_{m force}-\delta\,\Xi(m)$ with $c_{m force}>0$ absolute and
  $\Xi(m)\ge 0$ explicit.
  \item[(S5$'$--UE+SPLIT)] For every $\kappa$--admissible aligned box,
  \[
    \widetilde D_B(W)\le C_{m up}\,\delta^p\Big(\mathrm{Res}(m)+C_{m loc}\,\delta^{-	heta}\,G(N_{m loc}(m),\kappa)\Big),
  \]
  where $p>0$, $	heta\ge 0$, and $C_{m up},C_{m loc}$ are $\delta$--uniform, and
  $G(n,\kappa)\le C_G\,\kappa^{-u}n^q$ for fixed $u,q\ge 0$.
\end{enumerate}
Suppose additionally that $2p\ge 1$, $2(p-	heta)\ge q$, and $p-	heta>0$.
Then there exists $\eta_\star\in(0,1)$ (depending on the displayed constants and $\kappa$) such that
for every $\eta\in(0,\eta_\star]$ the S5$'$ tail inequality holds at $\delta=\delta_0(m,lpha)$
for all $m\ge 10$ and all $lpha\in(0,1]$, and hence no off-axis quartet exists at any height $m\ge 10$.
Combined with any finite-height front-end, this implies RH.
\end{theorem}

egin{remark}[S5$'$ acceptance gate for phase endpoints (no drift)]\label{rem:S5prime-gate}
Any proposed S5$'$ endpoint built from boundary phase data (e.g.\ $\Deltarg$ or an integral of
$\Im(\log	ext{-derivative})$) must declare its exponent budget data $(p,	heta,q)$ in the
schematic bound
\[
  \widetilde D_B(W)\le C_{m up}\,\delta^p\Big(\mathrm{Res}(m)+C_{m loc}\,\delta^{-	heta}\,G(N_{m loc}(m),\kappa)\Big),
\]
and must satisfy the uniformity/shrink conditions of Theorem~ef{thm:S5prime-closure}:
$2p\ge 1$, $2(p-	heta)\ge q$, and $p-	heta>0$.
Pure $\Deltarg$ endpoints have $p=0$ and are rejected. Any phase endpoint whose proof reduces
to an absolute $L^r(\partial B)$ estimate for $E'/E$ is also rejected by Lemma~ef{lem:S5_Lp_collapse}
and Proposition~ef{prop:S5_Lp_nogo}.
\end{remark}
```

---

### P37.4 — Add S6 harness appendix (optional, 1 page)

**Placement:** Appendix (new short appendix after existing NO–GO appendix).

**Edits (outline only):**
- Define “amplitude leak” in explicit formula: off-axis zero β>1/2 gives a term of size ≍ x^β.
- Map: v-frame displacement a = 2β−1.
- State explicitly: S6 is interpretive unless a new lemma connects the phase endpoint to a prime-error bound.

(Write this appendix in prose, with one displayed explicit-formula identity.)

---

## Build-time audit checklist (v37)

1. Every phase endpoint uses **Im outside the integral**.
2. Collar nonvanishing hypotheses are explicit wherever phase increments are defined.
3. v37 makes **no closure claim**; it only installs S5′ infrastructure + missing lever as OPEN.

