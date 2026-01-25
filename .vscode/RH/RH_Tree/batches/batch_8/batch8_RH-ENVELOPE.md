# batch8_RH-ENVELOPE.md

## RH Convergence Program — Batch 8  
**Callsign:** RH-ENVELOPE  
**Ground truth:** v38 locked build  
**Mission:** Close or decisively reframe the “Missing Lever” for S5′.

---

## Mechanism choice (mandatory)

**Chosen mechanism:** **(M1) Pair isolation / cancellation.**

Rationale: v38 already codifies that endpoint-only, per-pole δ-inert controls (θ=0 per pole) cannot yield any UE gain p>0 for the buffered phase endpoint (Lemma `lem:phase-UE-theta0-nogo`).【860:10†manuscript_v38.pdf†L28-L68】  
Therefore, the only plausible way M1 could “defeat the one-pole model” is to isolate the forced local contribution and show the remainder is δ-small (or cancels) in the *same* phase endpoint class. The question is whether that can possibly clear the **budget gate** in the *forceable* endpoint class \(\widetilde D_B\) without delusion.【860:4†manuscript_v38.pdf†L14-L49】

---

## Executive decision (one page)

### Verdict: **FAIL (NO-GO for M1 in the current S5′ architecture)**

Even granting *perfect* pair isolation—i.e., the “rest” local factor contributes \(O(\delta\log m)\) to the phase endpoint—the **forced zero(s)** inside \(B_{\kappa/2}^\circ\) already force a δ‑inert phase increment of size \(\ge \pi/2\) in the **same endpoint class** \(\widetilde D_B\) by the argument principle.【860:1†manuscript_v38.pdf†L54-L107】

Consequently, **any** ENVELOPE inequality of the S5′ target form
\[
\widetilde D_B(W)\ \le\ C_{\rm up}\,\delta^{p}\Bigl(\mathrm{Res}(m)+C_{\rm loc}\,\delta^{-\theta}G(N_{\rm eff},\kappa)\Bigr)
\]
with **δ‑uniform constants** and **shrinkable local exponent budget** \(p-\theta>0\) is **incompatible** with the existence of even a single interior zero—independently of how well one isolates the remainder cluster. This is the forced-zero obstruction.

This is stronger than “we don’t yet have the technology”: it is a structural incompatibility between:

- the *forceable* endpoint class \(\widetilde D_B\), where a single interior zero already forces an \(O(1)\) lower bound,【860:1†manuscript_v38.pdf†L54-L107】
- and the *required* δ‑shrinking upper-bound architecture demanded by the S5′ acceptance gate \(p-\theta>0\).【860:4†manuscript_v38.pdf†L41-L44】

---

## Ground truth recap (v38 anchors; minimal)

### A. Forced endpoint definition (v38)

- Aligned box \(B(\alpha,m,\delta)=\{v: |\Re v-\alpha|\le\delta,\ |\Im v-m|\le\delta\}\) (square of half-side δ).【864:2†manuscript_v34.pdf†L41-L43】  
- Buffered inner box \(B_{\kappa/2}=\{v\in B: \mathrm{dist}(v,\partial B)\ge \kappa\delta/2\}\).【860:2†manuscript_v38.pdf†L3-L8】

- Buffered boundary phase endpoint:
\[
\Delta_{S_j}\arg W := \Im\int_{S_j}\frac{W'(v)}{W(v)}\,dv,\qquad
\widetilde D_B(W):=\max_{1\le j\le 4}\bigl|\Delta_{S_j}\arg W\bigr|.
\]
(Definition 12.19).【860:2†manuscript_v38.pdf†L9-L31】

### B. FORCE is automatic for \(\widetilde D_B\)

If \(W\) has at least one zero in \(B_{\kappa/2}^\circ\), then \(\widetilde D_B(W)\ge \pi/2\). (Lemma 12.23).【860:1†manuscript_v38.pdf†L54-L107】

### C. The Missing Lever target inequality + gate

The OPEN “Missing Lever” box in §12 demands an ENVELOPE inequality with exponents \((p,\theta,q)\) satisfying the budget gate
\[
2p\ge 1,\quad 2(p-\theta)\ge q,\quad p-\theta>0,
\]
uniformly for all \(m\ge 10\), \(\alpha\in(0,1]\), and all κ‑admissible \(0<\delta\le\delta_0(m,\alpha)=\eta\alpha/(\log m)^2\).【860:4†manuscript_v38.pdf†L14-L44】

---

## Why M1 fails: the forced-zero obstruction

### Statement (NO-GO lemma; v39-ready)

> **Lemma (Forced-zero obstruction to δ‑shrinking phase UE in \(\widetilde D_B\)).**  
> Fix \(\kappa\in(0,1/10)\). Let \(p>0\) and \(\theta\ge 0\) satisfy \(p-\theta>0\).  
> Suppose there exist constants \(C_{\rm up}>0\), \(C_{\rm loc}>0\), \(C_G>0\), \(u\ge 0\), \(q\ge 0\), independent of \(\delta\), such that the following holds:
> 
> For every \(m\ge 10\), every \(\alpha\in(0,1]\), and every κ‑admissible aligned box \(B=B(\alpha,m,\delta)\) with \(0<\delta\le\delta_0(m,\alpha)\), for every holomorphic function \(E\) on a neighborhood of \(B\), letting \(G_{\rm out}\) be the Dirichlet outer factor of \(E\) on \(B^\circ\), \(W:=E/G_{\rm out}\), and letting \(N_{\rm eff}(B)\) denote the number of zeros of \(W\) in \(B_{\kappa/2}^\circ\) (counted with multiplicity), one has
> \[
> \widetilde D_B(W)\ \le\ C_{\rm up}\,\delta^{p}\Bigl(\mathrm{Res}(m)\ +\ C_{\rm loc}\,\delta^{-\theta}\,C_G\,\kappa^{-u}\,N_{\rm eff}(B)^q\Bigr),
> \tag{UE\(_{\widetilde D}\)}
> \]
> where \(\mathrm{Res}(m)\) is any nonnegative quantity independent of \(\delta\) (e.g. \(C_1\log m+C_2\)).
> 
> Then (UE\(_{\widetilde D}\)) cannot hold uniformly in \(\delta\). In fact, it already fails for a one-zero model \(E(v)=v-\rho\) with \(\rho\in B_{\kappa/2}^\circ\).

### Proof (referee-grade; short)

Fix any \(m\ge 10\), \(\alpha\in(0,1]\), and any \(\delta>0\) with \(0<\delta\le\delta_0(m,\alpha)\). Let \(B=B(\alpha,m,\delta)\) and choose \(\rho:=\alpha+im\), the box center. Then \(\rho\in B_{\kappa/2}^\circ\) for every \(\kappa\in(0,1)\) (the buffered box is strictly inside \(B\)). Moreover, \(B\) is κ‑admissible for \(E(v)=v-\rho\), since the unique zero is at distance \(\ge \delta\) from \(\partial B\), hence \(\mathrm{dist}(\partial B,Z(E))=\delta\ge \kappa\delta\).

Let \(E_\rho(v):=v-\rho\) and let \(G_{\rm out}\) be its Dirichlet outer factor on \(B^\circ\); set \(W:=E_\rho/G_{\rm out}\). Then \(W\) has at least one zero in \(B_{\kappa/2}^\circ\) (indeed at \(v=\rho\)), so by Lemma 12.23,
\[
\widetilde D_B(W)\ \ge\ \frac{\pi}{2}. \tag{1}
\]
【860:1†manuscript_v38.pdf†L54-L107】

In (UE\(_{\widetilde D}\)), we have \(N_{\rm eff}(B)=1\). Also \(\mathrm{Res}(m)\) is δ‑independent by hypothesis, hence bounded as \(\delta\to 0\). Therefore (UE\(_{\widetilde D}\)) implies, for some constant \(C^\star(\kappa,m,\alpha)\) independent of \(\delta\),
\[
\frac{\pi}{2}\ \le\ \widetilde D_B(W)\ \le\ C^\star\,\delta^{p-\theta}.
\]
Since \(p-\theta>0\), the right-hand side tends to \(0\) as \(\delta\to 0\), contradicting \(\pi/2>0\). This contradiction is uniform: it uses only the forced endpoint lower bound (1) and δ‑uniformity, not any subtle zeta input. ∎

### Consequence for M1 (pair isolation / cancellation)

The advertised M1 pathway (“only the forced pair contributes \(O(1)\) phase while the remainder contributes \(O(\delta\log m)\)”) does **not** address the obstruction above. Even if the “remainder” were \(0\), the forced factor alone leaves \(\widetilde D_B(W)\ge \pi/2\). Thus M1 cannot yield any δ‑shrinking UE upper bound with \(p-\theta>0\) in the endpoint class \(\widetilde D_B\).

This is consistent with the v38 endpoint-only NO‑GO latch: δ‑inert per-pole phase contributions preclude UE gain in \(\widetilde D_B\).【860:10†manuscript_v38.pdf†L28-L68】【860:5†v38_patchlog.md†L1-L6】

---

## What this means for the Missing Lever (decision-grade reframing)

### 1) The “pair-isolation” bullet in the §12 OPEN box is not decisive as written

The OPEN box currently lists “pair isolation” as a decisive LOCAL redesign option.【860:4†manuscript_v38.pdf†L45-L49】  
Under the forced-zero obstruction, **pair isolation cannot by itself lead to an ENVELOPE inequality with \(p-\theta>0\)** *in the forceable endpoint class* \(\widetilde D_B\).

### 2) What would be required instead

To make progress beyond v38, one must change at least one of the following:

1. **Endpoint class:** Replace \(\widetilde D_B\) by a different endpoint \(\Phi_B\) for which forcing does *not* produce a δ‑independent \(O(1)\) lower bound from a single interior zero, while still being forceable/transferable (Remark 12.25).【860:1†manuscript_v38.pdf†L114-L121】
2. **Forcing architecture:** Replace single-box forcing by a multi-box or global forcing mechanism whose lower bound scales compatibly with any δ‑normalized endpoint.
3. **Restriction to zeta-specific structure:** Any claim that “zeta’s \(E\)” avoids the one-zero obstruction must introduce explicit additional hypotheses not satisfied by the model \(E(v)=v-\rho\). In other words: the Missing Lever, if real, cannot be proved by “local holomorphicity + collar nonvanishing” arguments alone; it must use genuine global/arithmetic structure of \(\Xi_2\) not shared by generic holomorphic functions.

Under current program rules (forceability gate + δ‑uniformity + NO‑GO filters), none of these replacements is presently in v38.

---

## S6 check: explicit-formula amplitude leak (mandatory)

### Frame mapping (correct scaling)

A nontrivial zero \(\rho=\beta+i\gamma\) in s-frame corresponds to:

- u-frame: \(u_\rho=2\rho=(1+a)+im\), where \(a=2\beta-1\in(-1,1)\), \(m=2\gamma>0\).【792:1†manuscript_v35.pdf†L10-L16】
- v-frame: \(v_\rho=u_\rho-1=a+im\).

Thus “off critical line” means \(\beta\neq 1/2\iff a\neq 0\iff \Re(v_\rho)\neq 0\).

### Does failure of the phase-class UE correspond to an \(x^\beta\) amplitude leak?

**Not directly.** The endpoint \(\widetilde D_B(W)\) is a **local winding/argument** witness: it detects the presence of a zero in \(B_{\kappa/2}^\circ\) via the argument principle (total winding \(2\pi N\)).【860:1†manuscript_v38.pdf†L54-L107】  
This is not, by itself, a quantitative control on the amplitude of explicit-formula correction terms.

**Indirectly (trivial direction):** If an off-axis zero exists with \(\beta>1/2\), the explicit formula for \(\psi(x)\) contains a term \(x^\rho/\rho\) of magnitude \(\asymp x^\beta/|\rho|\), i.e. an \(x^\beta\) amplitude leak relative to \(x^{1/2}\). The phase endpoint does not measure this amplitude; it only witnesses that such a zero would exist locally.

Therefore, under the current architecture, the S6 harness interpretation is:

- \(\widetilde D_B\) is consistent with being a **zero-presence witness**, not an amplitude-leak controller.
- Any future lever that claims to close RH via \(\widetilde D_B\) must explain an additional bridge from local winding to explicit-formula amplitude control (or explicitly state the analogy is inapt).

---

## Paste-ready TeX edits for v39 (decision-grade latch)

These edits are designed to be **truth-latching**: they prevent silent drift by recording that M1 is a dead end for the \(\widetilde D_B\) endpoint in the current δ‑shrinking budget architecture.

### (i) New lemma insertion (place in §12.2 after Lemma `lem:phase-UE-theta0-nogo`)

```tex
\begin{lemma}[Forced-zero obstruction to $\delta$-shrinking UE in $\widetilde D_B$]
\label{lem:forced_zero_obstruction_phaseUE}
Fix $\kappa\in(0,1/10)$. Let $p>0$ and $\theta\ge 0$ satisfy $p-\theta>0$.
Assume there exist constants $C_{\rm up}>0$, $C_{\rm loc}>0$, $C_G>0$, $u\ge 0$, $q\ge 0$,
independent of $\delta$, such that for every $m\ge 10$, every $\alpha\in(0,1]$, and every
$\kappa$--admissible aligned box $B=B(\alpha,m,\delta)$ with $0<\delta\le \delta_0(m,\alpha)$,
for every holomorphic $E$ on a neighborhood of $B$, letting $G_{\rm out}$ be the Dirichlet outer factor of $E$
on $B^\circ$ and $W:=E/G_{\rm out}$, one has
\[
\widetilde D_B(W)\ \le\ C_{\rm up}\,\delta^{p}\Bigl(\mathrm{Res}(m)\ +\
C_{\rm loc}\,\delta^{-\theta}\,C_G\,\kappa^{-u}\,N_{\rm eff}(B)^q\Bigr),
\]
where $\mathrm{Res}(m)\ge 0$ is independent of $\delta$ and $N_{\rm eff}(B)$ counts zeros of $W$
in $B_{\kappa/2}^\circ$ with multiplicity.
Then no such inequality can hold uniformly in $\delta$.
\end{lemma}

\begin{proof}
Fix $m\ge 10$, $\alpha\in(0,1]$, and choose any $0<\delta\le \delta_0(m,\alpha)$.
Let $B=B(\alpha,m,\delta)$ and set $\rho:=\alpha+i m$.
Then $\rho\in B_{\kappa/2}^\circ$, and for $E_\rho(v)=v-\rho$ the box is $\kappa$--admissible.
Let $G_{\rm out}$ be the outer factor for $E_\rho$ and $W:=E_\rho/G_{\rm out}$.
Since $W$ has a zero in $B_{\kappa/2}^\circ$, Lemma~\ref{lem:phase-forcing-argprinciple} gives
$\widetilde D_B(W)\ge \pi/2$.
But $N_{\rm eff}(B)=1$ and $\mathrm{Res}(m)$ is $\delta$--independent, so the assumed inequality implies
$\pi/2\le C^\star\,\delta^{p-\theta}$ for some $C^\star$ independent of $\delta$.
This fails as $\delta\to 0$ because $p-\theta>0$.
\end{proof}
```

### (ii) Edit the §12 OPEN “Missing Lever” box (remove false decisiveness of M1)

Replace the current LOCAL REDESIGN bullet list in the OPEN box (Section 12) with:

```tex
\noindent
\textbf{LOCAL REDESIGN (one decisive route is required).}
Because $\widetilde D_B$ is forced at size $\ge \pi/2$ by a single interior zero
(Lemma~\ref{lem:phase-forcing-argprinciple}),
any $\delta$--shrinking ENVELOPE inequality of the form \eqref{eq:S5prime-envelope-template}
must \emph{defeat the one-zero model} in a way not covered by mere “pair isolation.”
In particular, Lemma~\ref{lem:forced_zero_obstruction_phaseUE} shows that
isolating the remainder local cluster while leaving an $O(1)$ forced local contribution
cannot yield an exponent budget with $p-\theta>0$ in the endpoint class $\widetilde D_B$.
Accordingly, the only viable next steps must change at least one of:
(i) the contradiction endpoint class (while maintaining forceability),
(ii) the forcing architecture, or
(iii) introduce a genuinely zeta-specific structural hypothesis that rules out the one-zero model.
\textbf{NO CLAIM POLICY:} no tail closure and no RH claim are made until such a lever is proved/cited.
```

### (iii) Add a short S6 harness remark (optional, but consistent with v38 posture)

```tex
\begin{remark}[S6 check: $\widetilde D_B$ is a zero-presence witness, not an amplitude controller]
The endpoint $\widetilde D_B$ is forced via the argument principle and therefore primarily detects
local zero presence/winding on $\partial B_{\kappa/2}$.
It does not, by itself, give a quantitative bound on explicit-formula amplitudes $x^\beta$.
Any proposed closure lever in this endpoint class should state explicitly whether (and how)
it connects to explicit-formula amplitude leaks, or why the analogy is inapt.
\end{remark}
```

---

## Mandatory Patch Packet

* Callsign: RH-ENVELOPE  
* Result classification: **FAIL (NO-GO for M1 / pair isolation in the current S5′ endpoint \(\widetilde D_B\))**  
* Target gaps closed (by ID):  
  - None fully closed.  
  - **G‑4′ (Missing Lever)** is **reframed/tightened**: M1 is eliminated as a viable closure mechanism for \(\widetilde D_B\) under the δ‑shrinking budget gate.
* Target gaps still open (by ID):  
  - **G‑4′ (Missing Lever)** remains OPEN (requires an endpoint/forcing redesign or genuinely zeta-specific structural lever).  
* Key conclusions (≤5 bullets):  
  1. In the forceable buffered phase endpoint \(\widetilde D_B\), a single interior zero forces \(\widetilde D_B(W)\ge\pi/2\) (argument principle).【860:1†manuscript_v38.pdf†L54-L107】  
  2. Therefore any ENVELOPE inequality with δ‑uniform constants and **shrinkable budget** \(p-\theta>0\) is incompatible with the one-zero model \(E(v)=v-\rho\).  
  3. Hence **pair isolation/cancellation (M1)**, even if perfect for the “rest” cluster, cannot clear the UE gate for \(\widetilde D_B\) without changing endpoint/forcing.  
  4. Any viable continuation must change endpoint class, forcing architecture, or add zeta-specific structure that invalidates the one-zero obstruction.  
  5. \(\widetilde D_B\) is a **local zero-presence witness**; it does not directly control explicit-formula amplitude leaks.  
* Paste-ready manuscript edits (TeX blocks):  
  - Included above: Lemma `lem:forced_zero_obstruction_phaseUE`; edits to the OPEN box; optional S6 remark.  
* Dependencies on other branches:  
  - Uses only v38 locked facts: Definition 12.19 and Lemma 12.23 (FORCE).【860:2†manuscript_v38.pdf†L9-L31】【860:1†manuscript_v38.pdf†L54-L107】  
  - No dependency on ABSORB/LOCAL computations beyond the already-installed budget gate framework.【860:4†manuscript_v38.pdf†L41-L44】  
* Referee risk notes (anticipated objections + how addressed):  
  - **Objection:** “But we only need ENVELOPE for \(E=\Xi_2(1+v)\), not for arbitrary holomorphic \(E\).”  
    **Response:** Correct; the lemma shows that **any** proof of ENVELOPE that relies only on local holomorphicity + collar nonvanishing cannot succeed. A viable route must use explicit global properties of \(\Xi_2\) that exclude the one-zero model, and those properties must be stated as hypotheses and proved/cited.  
  - **Objection:** “Pair isolation could remove the forced contribution.”  
    **Response:** Removing the forced contribution requires changing the contradiction endpoint or redesigning forcing; otherwise \(\widetilde D_B\) remains forced at \(\ge\pi/2\) whenever any interior zero exists.  
  - **Objection:** “Maybe constants depend on \(\delta\).”  
    **Response:** The entire S5′ gate is explicitly a δ‑uniform program; allowing δ‑dependent constants defeats the purpose and violates the v38 acceptance gate posture.【860:4†manuscript_v38.pdf†L14-L44】  
