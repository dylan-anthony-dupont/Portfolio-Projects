# batch7_RH-ENVELOPE.md

According to a document from **2026-01-25**, v37’s **primary spine** is S5′ (phase/winding endpoint redesign), and the ENVELOPE-side blocker is **G-4′: a phase-class upper-envelope (UE) inequality with `p ≥ 1/2` and δ-uniform constants**, beyond the already-installed phase toolkit. 【turn10file1†CR_master_dashboard_v37_locked.md†L3-L21】【turn10file0†v37_next_build_plan_diff.md†L8-L12】

This Batch-7 ENVELOPE response is **decisive**: under the *current* S5′ architecture, any attempt to obtain a **δ-gain** `δ^p` with `p>0` **while keeping the local interface δ-inert (θ=0) by endpoint design alone** runs into a universal “single-pole” obstruction. Concretely:

- v37 already has:  
  (i) a **forceable phase witness** on the buffered contour (Definition 12.16 / Lemma 12.17),  
  (ii) a **residual phase budget** `O(δ log m)` (Corollary 12.13), and  
  (iii) a **local phase bound** that is δ-inert per zero in the phase class (Lemma 12.14). 【turn8file6†manuscript_v37.pdf†L36-L51】【turn8file3†manuscript_v37.pdf†L86-L93】【turn8file4†manuscript_v37.pdf†L15-L41】【turn8file8†manuscript_v37.pdf†L7-L63】  
- What is missing is exactly the v37 OPEN box: a phase-class UE bound with `p ≥ 1/2` and **local exponent** `θ ≤ p-1/2` (ideally `θ=0`). 【turn10file9†manuscript_v37.pdf†L16-L36】  
- This report shows: **if “θ=0” is achieved by endpoint choice in the strong sense “each Cauchy kernel is O(1) in Φ_B”**, then **no UE inequality with any `p>0` can hold by a local analytic argument**. This effectively marks **P38.2 / G-4′ as NO-GO unless additional structure is introduced** (e.g., a forcing redesign or an explicit cancellation/isolation mechanism that defeats the single-pole test). 【turn10file2†v37_next_build_plan_diff.md†L1-L9】

---

## Task A — Candidate endpoint class Φ_B (θ≈0 target) and why it cannot supply p>0 “by itself”

### A1. Natural phase endpoint family already in v37 (δ-inert local, but p=0)

The phase toolkit in v37 uses **phase increments** (log-derivative integrals) as endpoints, e.g. on shifted segments or the buffered contour. This yields δ-inert local control because each local Cauchy kernel contributes at most `π` in argument change (Lemma 12.14). 【turn8file4†manuscript_v37.pdf†L15-L41】

A canonical “endpoint functional” in this family is:

```tex
\begin{definition}[Raw phase endpoint on a side]
Let $S\subset \partial B_{\kappa/2}$ be a line segment with a fixed orientation.
For a holomorphic nonvanishing function $H$ on a neighborhood of $S$, define
\[
\Phi^{\mathrm{ph}}_{B,S}(H) \;:=\; \left|\Im \int_{S} \frac{H'(v)}{H(v)}\,dv \right|
\;=\; \bigl|\Delta_S \arg H\bigr|.
\]
Define the “max-side” phase endpoint
\[
\Phi^{\mathrm{ph}}_{B}(H) \;:=\; \max_{S\in \mathcal S(B_{\kappa/2})}\, \Phi^{\mathrm{ph}}_{B,S}(H),
\]
where $\mathcal S(B_{\kappa/2})$ denotes the four sides of the buffered rectangle $\partial B_{\kappa/2}$.
\end{definition}
```

This is **δ-inert per zero** but has **no δ-gain** (`p=0`). v37 explicitly notes raw phase endpoints cannot close under constant-limited forcing (OPEN box “No–GO reminders”). 【turn10file9†manuscript_v37.pdf†L37-L42】

### A2. Design-family endpoints with θ≈0 (BMO / fractional Sobolev / Carleson), still blocked at UE-step

Many standard “less singular boundary object” endpoints have the desired δ-inert per-pole behavior (θ≈0) on the primitive `log H` rather than on `H'/H`; examples include:

- `\| \arg H \|_{\mathrm{BMO}}` on an arc,  
- `[\arg H]_{\dot H^{1/2}}` on an arc (scale-invariant),  
- Carleson measure norms of `|\nabla \log|H||^2` in a collar.

These all treat the model primitive `\arg(v-\rho)` as **O(1)** on a length-`δ` arc (constant shifts like `\log \delta` drop out). So they are “θ=0–friendly” candidates for LOCAL.

**But** the next step (UE) needs a **δ^p prefactor** with `p ≥ 1/2` between the *forced object* and this endpoint. The universal obstruction below shows: as long as the endpoint remains δ-inert on the *single-pole model*, **no local analytic UE inequality with any `p>0` can hold**.

---

## Task B — UE inequality: best attempt + decisive obstruction (NO-GO)

### B1. Ground truth: what UE would need to look like in v37

v37’s acceptance gate (Remark 12.1) demands a forceable UE inequality of the form
`D_B(W) ≤ C_up δ^p Φ_B(E'/E)` with an explicit `p>0` and δ-uniform `C_up`. 【turn10file9†manuscript_v37.pdf†L43-L52】

The v38 build plan P38.2 makes this even more specific for the phase class: it requests **local exponent `θ=0` in the same endpoint class** and **`p ≥ 1/2`**. 【turn10file2†v37_next_build_plan_diff.md†L1-L9】

### B2. New NO-GO lemma (endpoint-only): δ-inert per-pole ⇒ no δ^p UE

What follows is an “endpoint-only” obstruction: **if the UE inequality is to be proved using only local analyticity + κ-geometry (i.e., it must hold for generic holomorphic inputs on boxes), then any endpoint class in which each Cauchy kernel is O(1) (θ=0) cannot admit any δ^p prefactor with p>0.**

This is not a statement about ζ specifically; it is a local analytic no-go analogous in spirit to the v36 “absolute L^r collapse” (which shows p=θ for absolute norms). 【turn10file16†manuscript_v37.pdf†L1-L10】

```tex
\begin{lemma}[Endpoint-only NO--GO: $\theta=0$ per pole forbids any $p>0$ UE gain]
\label{lem:phase-UE-theta0-nogo}
Fix $\kappa\in(0,1/10)$. Let $B=B(\alpha,m,\delta)$ be an aligned box and let
$E$ be holomorphic on a neighborhood of $\overline B$, with outer factorization
$E=G_{\rm out}\,W$ on $B$ (so $W$ is inner on $B$).

Assume $\Phi_B$ is a boundary functional acting on the trace of $E'/E$ and that
there exist constants $C_{\rm loc}=C_{\rm loc}(\kappa)$ and $u\ge 0$ such that,
for every $\rho\in B_{\kappa/2}$ and the test function $E_\rho(v):=v-\rho$, one has
the per-pole bound
\[
\Phi_B\!\left(\frac{E_\rho'}{E_\rho}\right)
=\Phi_B\!\left(\frac1{v-\rho}\right)
\le C_{\rm loc}\,\kappa^{-u},
\]
uniformly in $\delta$ (this is the strong form of ``$\theta=0$ per pole'').

Then there do not exist constants $C_{\rm up}>0$ and $p>0$ (independent of $\delta$)
such that the phase-class UE inequality
\[
\widetilde D_B(W) \;\le\; C_{\rm up}\,\delta^{p}\,\Phi_B\!\left(\frac{E'}{E}\right)
\]
holds for all such boxes $B$ and all such holomorphic $E$.
In fact, for $E=E_\rho(v)=v-\rho$ with $\rho\in B_{\kappa/2}$, the inequality forces
\[
\frac{\pi}{2} \;\le\; C_{\rm up}\,C_{\rm loc}\,\kappa^{-u}\,\delta^{p},
\]
which fails for sufficiently small $\delta$.
\end{lemma}

\begin{proof}
Fix $\rho\in B_{\kappa/2}$ and take $E(v)=E_\rho(v)=v-\rho$.
Then $E$ has a zero in $B_{\kappa/2}$, so its inner quotient $W$ has a zero in $B_{\kappa/2}$.
By Lemma~12.17 (phase forcing by the argument principle), this implies
$\widetilde D_B(W)\ge \pi/2$.
On the other hand $E'/E=1/(v-\rho)$, so by hypothesis
$\Phi_B(E'/E)\le C_{\rm loc}\kappa^{-u}$ uniformly in $\delta$.
Substituting into the claimed UE bound gives
$\pi/2 \le C_{\rm up}C_{\rm loc}\kappa^{-u}\delta^{p}$, contradicting $p>0$ as $\delta\to 0$.
\end{proof}
```

**Why this lemma is relevant to v37:** the left-hand side forcing input is exactly v37’s Lemma 12.17 (interior zero forces `\widetilde D_B(W) ≥ π/2`). 【turn8file3†manuscript_v37.pdf†L86-L93】 The per-pole “θ=0” hypothesis is exactly the kind of endpoint behavior the Missing Lever aspires to (local poles cost O(1) each). 【turn10file9†manuscript_v37.pdf†L24-L36】

### B3. Consequence (decision): P38.2 as stated cannot be achieved by endpoint choice alone

Lemma \ref{lem:phase-UE-theta0-nogo} implies:

- If we insist on **θ=0 “per pole”** (each Cauchy kernel has bounded Φ_B size), then **any UE inequality with `p>0` is NO-GO** unless one uses additional nonlocal structure that excludes the test case `E(v)=v-\rho`.  
- In particular, the v38 plan requirement “local exponent θ=0 in the same endpoint class + UE exponent p ≥ 1/2” (P38.2) cannot be satisfied by a UE mechanism that is stable under the minimal local hypotheses (holomorphicity + κ-geometry + outer factorization). 【turn10file2†v37_next_build_plan_diff.md†L1-L9】

This strongly suggests G-4′ should be treated as **“needs extra structure”**:
- either **a forcing redesign** (G-2b) plus a UE bound for a different forced object,  
- or **a pair-isolation / cancellation lemma** that breaks the “single-pole” model (G-8),  
- or importing **explicit-formula arithmetic** (S6-style) into the logical proof spine (currently disallowed by posture). 【turn10file1†CR_master_dashboard_v37_locked.md†L15-L23】

**Verdict for Task B:** Under the endpoint-only regime mandated by the NO-GO rules, a phase-class UE inequality with `p ≥ 1/2` and local exponent `θ=0` is **NO-GO**.

---

## Task C — Residual/local split in the phase class (v37-compatible)

Even though the δ^p upgrade is blocked as above, the **phase split itself** is clean and already integrated.

v37 OPEN box summarizes the three installed tools: forceable phase witness (Def 12.16/Lem 12.17), residual phase budget `O(δ log m)` (Cor 12.13), and local δ-inert phase bound (Lem 12.14). 【turn10file9†manuscript_v37.pdf†L16-L23】

A representative split statement in v37 is the “shifted segment” version: on `I_{+,\lambda}` one has
\|Δ arg E\| ≤ \|Δ arg F\| + \|Δ arg Z_loc\|, with the residual budget and the per-zero local bound. 【turn8file8†manuscript_v37.pdf†L7-L63】【turn8file4†manuscript_v37.pdf†L15-L41】

Paste-ready “generic” version:

```tex
\begin{lemma}[Phase split on shifted segments (template)]
\label{lem:phase-split-template}
Assume $E=F\cdot Z_{\rm loc}$ on a neighborhood of a line segment $I$ on which both $F$ and
$Z_{\rm loc}$ are holomorphic and nonvanishing on a collar.
Then
\[
\bigl|\Delta_I \arg E\bigr|
\;\le\;
\bigl|\Delta_I \arg F\bigr| + \bigl|\Delta_I \arg Z_{\rm loc}\bigr|.
\]
\end{lemma}
```

And the v37 bounds (already present) are:

- Residual phase budget: `|\Delta_I \arg F| ≤ 2δ(C_1 \log m + C_2)` (Corollary 12.13). 【turn8file8†manuscript_v37.pdf†L7-L63】  
- Local phase bound: `|\Delta_I \arg Z_{\rm loc}| ≤ π N_{\rm loc}(m)` (Lemma 12.14). 【turn8file4†manuscript_v37.pdf†L15-L41】

These are exactly the δ-inert local interface (θ=0 in the phase class) that makes the Missing Lever look tantalizing — but per Lemma \ref{lem:phase-UE-theta0-nogo}, it cannot coexist with a δ^p UE prefactor for generic holomorphic inputs.

---

## Task D — Dependency handshake: what LOCAL must prove (or what forcing must change) to finish the Missing Lever

Given the endpoint-only NO-GO above, the remaining viable routes are the ones already listed in v37’s OPEN box and the v38 plan:

1. **Change the forced object / forcing architecture (G-2b)**: rewrite tail to target `\widetilde D_B(W)` or prove a transfer `\widetilde D_B ↔ D_B` (P38.1). 【turn10file0†v37_next_build_plan_diff.md†L18-L30】  
   - This does **not** solve the UE-side by itself, but it may allow a different endpoint functional with a new UE mechanism.

2. **Break the single-pole obstruction via structure (G-8 / P38.3)**: prove a **pair-isolation** or “rest-of-cluster is δ-small” statement, so the relevant local contribution is *not* modeled by a single Cauchy pole at distance `≈ κδ`. 【turn10file2†v37_next_build_plan_diff.md†L11-L16】

A precise LOCAL deliverable (matching the Missing Lever format) that would circumvent Lemma \ref{lem:phase-UE-theta0-nogo} must explicitly *invalidate the one-pole test* by exhibiting cancellation/isolation:

```tex
\begin{lemma}[LOCAL isolation needed to beat the one-pole obstruction]
\label{lem:local-isolation-needed}
Fix $\kappa\in(0,1/10)$ and let $\Phi_B$ be the endpoint class targeted in S5′.
To obtain any UE gain $p>0$ with a local exponent $\theta<p$ in the S5′ budget theorem,
it is necessary to prove a structural statement of the following form:

Whenever $B=B(\alpha,m,\delta)$ is $\kappa$-admissible at the nominal scale
$\delta\le \delta_0(m,\alpha)$ and $Z_{\rm loc}$ is the local factor of $E$ on $B$,
there exists a factorization
\[
Z_{\rm loc} \;=\; Z_{\rm forced}\cdot Z_{\rm rest}
\]
such that (i) $Z_{\rm forced}$ contains only $O(1)$ zeros (the “forced pair”), and (ii)
\emph{in the chosen endpoint class} one has the δ-small bound
\[
\Phi_B\!\left(\frac{Z_{\rm rest}'}{Z_{\rm rest}}\right)
\;\le\;
C\,\kappa^{-u}\,(\log m)^{q_{\rm eff}}\,\delta^{-(\theta_{\rm eff})}
\qquad\text{with}\qquad \theta_{\rm eff}<p
\]
(and ideally $\theta_{\rm eff}=0$ with $q_{\rm eff}=0$ or with an extra $\delta$ factor).
\end{lemma}
```

This matches exactly the third item in the v37 OPEN box (“pair-isolation: only the forced pair contributes O(1) while the remaining cluster contributes O(δ log m)”). 【turn10file9†manuscript_v37.pdf†L33-L36】

**Interpretation:** Without such a lemma, the local behavior of `E'/E` in any box containing a zero is indistinguishable from the single-pole test `E(v)=v-\rho`, and any UE inequality with `p>0` must pay `\theta\ge p` (collapse), making the budget gate impossible.

---

## S6 harness check (mandatory add-on)

### Does a phase/BMO/fractional endpoint correspond to an explicit-formula “x^β amplitude leak”?

Not directly. The phase endpoints in v37 (Δarg / winding witnesses) are **zero-presence witnesses**: they detect interior zeros via winding / argument principle, and their failure does not by itself translate to a clean “amplitude leak” statement on the prime side.

This is consistent with the v37 posture: S6 is explicitly an *interpretation harness only* and is not a logical dependency of S5′. 【turn10file1†CR_master_dashboard_v37_locked.md†L5-L7】

If one wants an amplitude-leak link, it must be stated as an additional lemma with explicit hypotheses; nothing in Lemma \ref{lem:phase-UE-theta0-nogo} provides such a link.

### Frame map (s → u → v)

v37’s normalization is (width–2 completion)
\[
u = 2s,\qquad v = u-1,\qquad s = \frac{u}{2}=\frac{1+v}{2}.
\]
So if a zero of $\zeta(s)$ has real part $\beta$, then in the $v$-frame its real part is
\[
\alpha = \Re(v) = 2\beta-1,\qquad\text{equivalently}\qquad \beta = \frac{1+\alpha}{2}.
\]
And heights map as $\Im(v)=\Im(u)=2\Im(s)$, so a “height band” $m$ in $v$ corresponds to $\gamma=m/2$ in $s$. 【turn10file16†manuscript_v37.pdf†L34-L47】

---

## Patch-packet (required)

- **Callsign:** RH-ENVELOPE  
- **Verdict:** **NO-GO** (endpoint-only route for P38.2 / G-4′ under θ=0 per-pole design)

### What I close vs what remains open

**Closed (new):**
- A clear **endpoint-only obstruction**: if the desired local interface is “θ=0 per pole” (each Cauchy kernel bounded in Φ_B), then **no phase-class UE inequality with any `p>0` can hold by local analytic arguments** (Lemma \ref{lem:phase-UE-theta0-nogo}). This narrows the Missing Lever search space sharply.

**Still open (as in v37):**
- **G-2b:** forcing ↔ endpoint alignment (`\widetilde D_B` rewrite or transfer). 【turn10file1†CR_master_dashboard_v37_locked.md†L8-L12】  
- **G-4′:** a viable phase-class UE inequality with `p ≥ 1/2` that avoids absolute-L^r collapse **and** defeats the single-pole obstruction (will require extra structure, not endpoint choice alone). 【turn10file11†CR_master_dashboard_v37_locked.md†L6-L13】  
- **G-8:** micro-window clustering or pair-isolation reducing effective local growth / producing cancellation. 【turn10file2†v37_next_build_plan_diff.md†L11-L16】

### Paste-ready TeX blocks (v38 insertion)

1) **Lemma (endpoint-only NO-GO)**: Lemma \ref{lem:phase-UE-theta0-nogo} and proof above.  
2) **Remark (consequence for P38.2)**:

```tex
\begin{remark}[Consequence for P38.2: endpoint-only $\theta=0$ cannot yield any $p>0$ gain]
Any attempt to close G--4$'$ by choosing an endpoint class $\Phi_B$ that is $\delta$--inert on each
local Cauchy kernel $(v-\rho)^{-1}$ (``$\theta=0$ per pole'') cannot produce a $\delta^p$ UE gain with
$p>0$ via a purely local analytic argument: the test input $E(v)=v-\rho$ contradicts such a bound
(Lemma~\ref{lem:phase-UE-theta0-nogo}). Therefore any successful phase-class UE inequality with
$p\ge 1/2$ must incorporate additional structure that defeats the one-pole model (e.g.\ forcing redesign
or pair-isolation/cancellation in the local factor).
\end{remark}
```

### Referee-risk notes (1–4 bullets)

- The NO-GO lemma is **endpoint-only**: it rules out proofs that depend only on local analyticity + κ-geometry and that treat each Cauchy kernel as O(1) in Φ_B. A referee will want the assumptions spelled out (done explicitly via the `E(v)=v-\rho` test).  
- Make sure the manuscript labels this correctly as “no universal/local analytic UE mechanism,” not as “impossible for ζ.” (It is a design filter, consistent with the v36 NO-GO philosophy.)  
- If the program later imports explicit-formula arithmetic, the lemma should be quoted as “does not apply once arithmetic excludes the test case,” to avoid overclaiming.  
- If the forcing target is switched from `\widetilde D_B` back to `D_B`, re-check that the same one-pole test remains compatible with the new forced object (or adjust the statement accordingly).
