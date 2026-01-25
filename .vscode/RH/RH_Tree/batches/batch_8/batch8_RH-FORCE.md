# Batch 8 — RH-FORCE (v38 ground truth)
**Callsign:** RH-FORCE  
**Ground truth:** `manuscript_v38` (locked build)  
**Scope:** forceability under LOCAL redesign; attach forcing to the endpoint class used in S5′.

## A) Mechanism selection (mandatory)
I support **M1 = Local isolation / pair-dominance** (the “beat the one‑pole model” LOCAL option enumerated in the v38 Missing Lever latch).

*Reason for selection (forceability):* this LOCAL option does **not** require changing the contradiction endpoint away from the **forced** buffered phase endpoint `\widetilde D_B(W)`. It is therefore compatible with the only forcing we currently have, without needing a new forcing architecture.

## B) Forcing lemma / transfer lemma (decision-grade)

### B.1 Direct forcing is already attached in v38 (no redesign needed)
In v38, the contradiction endpoint is **explicitly** the buffered boundary phase endpoint `\widetilde D_B(W)` (Def. `def:Db-tilde-phase`). The forcing lemma is the argument‑principle pigeonhole bound (Lemma `lem:phase-forcing-argprinciple`) with constant `c_0 = \pi/2` and **no** error term (`\Xi \equiv 0`, Cor. `cor:S5prime-force-automatic`).

Concretely, with the v38 definitions:

* aligned box `B = B(\alpha,m,\delta)`,
* κ‑admissibility: `dist(\partial B, Z(E)) \ge \kappa\delta`,
* buffered inner rectangle `B_{\kappa/2}` and its oriented boundary decomposition `\partial B_{\kappa/2} = \cup_{j=1}^4 S_j`,
* Dirichlet outer factor `G_{\rm out}` on `B^\circ`,
* inner quotient `W := E/G_{\rm out}`,

the endpoint is
\[
\widetilde D_B(W):=\max_{1\le j\le 4}\Bigl|\Delta_{S_j}\arg W\Bigr|,
\qquad
\Delta_{S_j}\arg W := \Im \int_{S_j}\frac{W'(v)}{W(v)}\,dv.
\]

**Direct forcing statement (what Batch‑8 needs):**
If `W` has **at least one** zero in `B_{\kappa/2}^\circ`, then
\[
\widetilde D_B(W)\ \ge\ \pi/2,
\qquad \text{with Err}(\delta,m)\equiv 0.
\]
This is the strongest form: no δ‑loss, no height dependence.

**Proof (fully explicit, referee‑grade):**  
Since κ‑admissibility implies collar nonvanishing on `\partial B_{\kappa/2}` (Lemma `lem:phase_collar_nonvanishing`), the logarithmic derivative `W'/W` is holomorphic on a neighborhood of `\partial B_{\kappa/2}` and the argument increments are well‑defined. By the argument principle,
\[
\Im\oint_{\partial B_{\kappa/2}}\frac{W'(v)}{W(v)}\,dv
= 2\pi\,N_{B_{\kappa/2}}(W),
\]
where `N_{B_{\kappa/2}}(W)\in\mathbb{Z}_{\ge 0}` counts zeros of `W` in `B_{\kappa/2}^\circ` with multiplicity. Decomposing the contour into sides,
\[
2\pi\,N_{B_{\kappa/2}}(W)=\Im\sum_{j=1}^4\int_{S_j}\frac{W'}{W}\,dv
=\sum_{j=1}^4 \Delta_{S_j}\arg W.
\]
Hence, by triangle inequality,
\[
2\pi\,N_{B_{\kappa/2}}(W)=\Bigl|\sum_{j=1}^4 \Delta_{S_j}\arg W\Bigr|
\le \sum_{j=1}^4\bigl|\Delta_{S_j}\arg W\bigr|
\le 4\,\widetilde D_B(W).
\]
If `W` has at least one zero in `B_{\kappa/2}^\circ` then `N_{B_{\kappa/2}}(W)\ge 1`, so `\widetilde D_B(W)\ge \pi/2`.

This closes the Batch‑8 requirement **for the endpoint actually used in v38**.

### B.2 Transfer lemma if LOCAL/ENVELOPE proposes a different endpoint (Φ_B)
Batch‑8 asks for robustness “if the endpoint changes.” Here is the exact forceability transfer criterion in the **correct direction**.

**Lemma (Forceability transfer by domination; phase endpoint version).**  
Let `\Phi_B(W)\ge 0` be any endpoint functional defined for all κ‑admissible aligned boxes and associated inner quotients `W`. Assume the domination property
\[
\Phi_B(W)\ \ge\ \widetilde D_B(W)
\quad\text{for all κ‑admissible boxes.}
\]
Then the v38 forcing lemma transfers verbatim:
\[
\Bigl(W \text{ has a zero in } B_{\kappa/2}^\circ\Bigr)\ \Longrightarrow\ 
\Phi_B(W)\ \ge\ \pi/2.
\]
(Again `\mathrm{Err}\equiv 0`.)

*Proof:* Combine `\widetilde D_B(W)\ge \pi/2` with `\Phi_B(W)\ge \widetilde D_B(W)`.

**Interpretation:** This is the **only** direction that preserves forceability. If a redesign yields only `\Phi_B(W)\le \widetilde D_B(W)`, it is *not* usable as a contradiction endpoint without a separate forcing lemma.

### B.3 NO‑GO classification for non-dominating endpoint replacements (constructive)
If a proposed endpoint is not known (or is false) to dominate `\widetilde D_B`, forcing may simply not attach.

A common drift pattern is to replace `\widetilde D_B` with a **single-side** phase increment on a pre-selected side, e.g.
\[
\Phi_B^{(+)}(W) := \bigl|\Delta_{S_+}\arg W\bigr|,
\]
where `S_+` is (say) the right vertical side of `\partial B_{\kappa/2}`.

**NO‑GO lemma (single-side phase endpoint is not forceable δ‑uniformly).**  
Fix any aligned box geometry where the vertical side length is `O(\delta)` (as in the standard box family). Then there is no absolute constant `c_0>0` such that
\[
W \text{ has a zero in } B_{\kappa/2}^\circ \ \Rightarrow\ \Phi_B^{(+)}(W)\ge c_0
\quad\text{uniformly for all sufficiently small }\delta.
\]

*Model/counterexample:* Take `W(v)=v-\rho` with `\rho` placed inside `B_{\kappa/2}^\circ` but at horizontal separation `d\asymp 1` from the chosen side `S_+`. Then on the short vertical segment `S_+` of length `O(\delta)` one has
\[
\Bigl|\Delta_{S_+}\arg(v-\rho)\Bigr| \le \int_{S_+}\frac{|dv|}{|v-\rho|}
\le \frac{O(\delta)}{d}\xrightarrow[\delta\to 0]{}0,
\]
while `W` still has a zero in the interior. Thus no δ‑uniform forcing constant exists for `\Phi_B^{(+)}`.

**Least-intrusive fix:** replace any pre-selected-side endpoint by the **max-over-sides** endpoint `\widetilde D_B` (or prove a domination `\Phi_B\ge \widetilde D_B`).

## C) Quantifier discipline (mandatory)
All forcing and transfer statements above are quantified as:

*For every* aligned box `B=B(\alpha,m,\delta)` and every `\kappa\in(0,1)`,
*for every* `\delta>0` such that κ‑admissibility holds:
\[
\operatorname{dist}(\partial B, Z(E))\ge \kappa\delta,
\]
*define* `B_{\kappa/2}` and `W=E/G_{\rm out}` as in Def. `def:Db-tilde-phase`. Then:

1. `G_{\rm out}` and `W` are holomorphic and nonvanishing on a neighborhood of `\partial B_{\kappa/2}` (Lemma `lem:phase_collar_nonvanishing`).
2. If `Z(W)\cap B_{\kappa/2}^\circ \neq \varnothing`, then `\widetilde D_B(W)\ge \pi/2` (Lemma `lem:phase-forcing-argprinciple`, Cor. `cor:S5prime-force-automatic`).
3. If additionally `\Phi_B(W)\ge \widetilde D_B(W)` (domination hypothesis), then `\Phi_B(W)\ge \pi/2`.

No statement ties “height” to `\Re(v)=0`; height is always the RH‑free parameter `m=\Im(v)` (and in s‑frame `m=2\gamma`).

## D) S6 explicit-formula mapping (mandatory)
**Does phase forcing correspond to an explicit-formula amplitude leak (x^\beta)?**  
Not directly.

* The explicit formula “amplitude leak” mechanism is global-in-`x`: an off-line zero `\rho=\beta+i\gamma` introduces terms on the order of `x^\beta` in (e.g.) `\psi(x)=x-\sum_\rho x^\rho/\rho+\cdots`.
* The endpoint `\widetilde D_B(W)` is a **local, geometric** certificate of a zero in a specific v‑frame box via winding/argument principle. It detects the *existence* of a zero inside a contour, not the size of `x^\beta` oscillations.

**Correct frame mapping:** `u=2s`, `v=u-1`, so an off-axis zero `\rho=\beta+i\gamma` corresponds to `v_\rho=(2\beta-1)+i(2\gamma)`. “Off-axis” means `\Re(v_\rho)\ne 0`. Forcing uses a box `B(\alpha,m,\delta)` at height `m=2\gamma` and (after alignment) the existence of an interior zero implies `\widetilde D_B(W)\ge\pi/2`.

## Mandatory Patch Packet
*Callsign:* RH-FORCE  
*Result classification:* **PASS** (forceability remains attached for the v38 contradiction endpoint; robust transfer criterion supplied; non-dominating endpoint swaps classified NO‑GO)  
*Target gaps closed (by ID):* **(forceability interface latch; already tracked as G‑2b in the Control Room), plus “endpoint‑swap drift prevention” in S5′**  
*Target gaps still open (by ID):* **G‑4′ (Missing Lever / phase-class ENVELOPE), LOCAL redesign proof itself (pair isolation), and any new endpoint’s δ‑uniform domination proof if an endpoint swap is attempted**  
*Key conclusions (≤5 bullets):*
1. v38’s contradiction endpoint is `\widetilde D_B(W)` and is directly forceable: interior zero ⇒ `\widetilde D_B(W)\ge \pi/2` with `\mathrm{Err}\equiv 0`.
2. Any redesigned endpoint `\Phi_B` is admissible only if it satisfies the domination direction `\Phi_B\ge \widetilde D_B` (or has its own forcing lemma).
3. Single-side (pre-selected-side) phase endpoints are **not** δ‑uniformly forceable; max-over-sides (or another dominating functional) is the minimal repair.
4. Forceability is geometric (argument principle), not an explicit-formula amplitude-leak detector.

*Paste-ready manuscript edits (TeX blocks):*

(i) **Revised lemma/proposition statements**
```tex
\begin{lemma}[Forceability transfer by domination (phase endpoint)]
\label{lem:forceability-transfer-phase}
Let $B=B(\alpha,m,\delta)$ be an aligned box and assume $\kappa$--admissibility:
$\dist(\partial B,\mathcal Z(E))\ge \kappa\delta$.
Let $G_{\rm out}$ be the Dirichlet outer factor on $B^\circ$ and $W:=E/G_{\rm out}$.
Let $\widetilde D_B(W)$ be the buffered boundary phase endpoint from
Definition~\ref{def:Db-tilde-phase}.

Let $\Phi_B(W)\ge 0$ be any endpoint functional defined on all such admissible boxes,
and assume the domination property
\[
\Phi_B(W)\ \ge\ \widetilde D_B(W)
\qquad\text{for all admissible boxes.}
\]
Then, if $W$ has a zero in $B_{\kappa/2}^\circ$,
\[
\Phi_B(W)\ \ge\ \pi/2.
\]
\end{lemma}
\begin{proof}
By Lemma~\ref{lem:phase-forcing-argprinciple} one has $\widetilde D_B(W)\ge \pi/2$.
The domination hypothesis yields $\Phi_B(W)\ge \widetilde D_B(W)$, hence $\Phi_B(W)\ge\pi/2$.
\end{proof}
```

```tex
\begin{lemma}[NO--GO for pre-selected-side phase endpoints]
\label{lem:nogo-single-side-phase}
Fix an aligned box family where at least one boundary side has Euclidean length $O(\delta)$.
Let $S_+$ denote such a side and define $\Phi_B^{(+)}(W):=|\Delta_{S_+}\arg W|$.
There is no absolute constant $c_0>0$ such that, uniformly for all sufficiently small $\delta$,
\[
\Bigl(W \text{ has a zero in }B_{\kappa/2}^\circ\Bigr)\ \Rightarrow\ \Phi_B^{(+)}(W)\ge c_0.
\]
\end{lemma}
\begin{proof}
Take $W(v)=v-\rho$ with $\rho\in B_{\kappa/2}^\circ$ but with horizontal separation
$d:=\dist(\rho,S_+)\asymp 1$. Then on the segment $S_+$ (length $O(\delta)$),
\(
|\Delta_{S_+}\arg(v-\rho)|\le \int_{S_+}|dv|/|v-\rho|\le O(\delta)/d\to 0
\)
as $\delta\to 0$, while $W$ still has a zero in the interior.
\end{proof}
```

(ii) **Revised definitions/remarks**
```tex
\begin{remark}[Forceability gate (phase endpoints)]
\label{rem:forceability-phase-gate}
The forced contradiction endpoint in S5$'$ is $\widetilde D_B(W)$
(Definition~\ref{def:Db-tilde-phase}).
Any alternative endpoint $\Phi_B$ may replace $\widetilde D_B$ \emph{only if}
either:
\begin{enumerate}
\item (\emph{Domination}) $\Phi_B(W)\ge \widetilde D_B(W)$ holds on every admissible box, so forcing transfers
by Lemma~\ref{lem:forceability-transfer-phase}; or
\item (\emph{Direct forcing}) one proves a new forcing lemma with conclusion $\Phi_B(W)\ge c_\Phi>0$
under an interior zero.
\end{enumerate}
Endpoint swaps that fail both conditions break forceability and are invalid.
\end{remark}
```

(iii) **Revised theorem/inequality lines**
```tex
% No change required to the forcing line when the endpoint is \widetilde D_B(W):
% the forcing hypothesis is discharged with c_{\rm force}=\pi/2 and \Xi\equiv 0
% by Corollary~cor:S5prime-force-automatic.
```

*Dependencies on other branches:*  
- LOCAL branch must supply the **pair isolation / δ‑shrink** mechanism (the chosen M1) to close the Missing Lever.  
- ENVELOPE/ABSORB must provide a **phase-class UE + split** upper bound feeding Theorem `thm:S5prime-closure`.  

*Referee risk notes (anticipated objections + how addressed):*
- **Objection:** “Endpoint swaps might silently break forcing.”  
  **Addressed:** explicit forceability gate remark + transfer lemma + NO‑GO lemma.
- **Objection:** “Branch issues for arg/log.”  
  **Addressed:** collar nonvanishing on buffered boundary is the prerequisite; forcing proof uses only `W'/W` integral on a zero-free contour.
- **Objection:** “Is the forcing constant really δ‑uniform?”  
  **Addressed:** yes; proof is argument principle on a fixed contour; the lower bound `\pi/2` depends only on counting zeros, not on δ or m.
