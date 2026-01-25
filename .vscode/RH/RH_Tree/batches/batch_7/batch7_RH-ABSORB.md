# batch7_RH-ABSORB.md — v37 UE‑Gate / S5′ acceptance‑gate instantiation (referee + integrator)

**Callsign:** RH‑ABSORB  
**Ground truth:** v37 locked build (dashboard + manuscript).  
**Scope:** instantiate and enforce the S5′ acceptance gate for the *current* concrete phase endpoint (`\widetilde D_B`) and provide a v38‑ready “Missing Lever” latch so closure cannot drift.

---

## 0) What v37 already locks (anchors)

1. **S5′ posture and blocker queue.** v37’s CR dashboard explicitly sets the primary spine to **S5′** (phase/winding endpoint redesign), and ranks the live blockers as **G‑2b**, **G‑4′**, **G‑8**, **G‑6** in that order. 【717:0†CR_master_dashboard_v37_locked.md†L1-L23】

2. **Conditional S5′ closure theorem + acceptance gate.** v37’s Theorem `thm:S5prime-closure` states: if a forceable phase endpoint `De_B` satisfies a schematic envelope bound with **declared** exponent tuple `(p,θ,q)` and δ‑uniform constants, and if **2p≥1**, **2(p−θ)≥q**, **p−θ>0**, then there exists `η⋆` making the S5′ tail inequality hold at `δ=δ0(m,α)` for all `m≥10`, `α∈(0,1]`. 【717:15†manuscript_v37.pdf†L1-L22】【717:15†manuscript_v37.pdf†L23-L39】

3. **Concrete forceable phase endpoint exists (but only forcing is proven).** v37 defines the **buffered boundary phase endpoint** `\widetilde D_B(W)` on the buffered contour `∂B_{κ/2}` and proves the **π/2 forcing lemma**: if `W` has an interior zero then `\widetilde D_B(W) ≥ π/2` via the argument principle. 【721:10†manuscript_v37.pdf†L55-L110】  
   Patchlog confirms this was added explicitly as the Batch‑6 integration. 【721:2†v37_patchlog.md†L1-L10】

4. **Prototype phase split confirms the *local phase term is δ‑inert per zero*.** Along the vertical segment `I+`, Lemma 12.14 gives the per‑zero phase increment bound ≤π, hence `|Δ arg Z_loc| ≤ π N_loc(m)`; Corollary 12.15 records residual phase `O(δ log m)` but local phase is δ‑inert. 【721:10†manuscript_v37.pdf†L1-L54】

5. **“Missing lever” is explicitly acknowledged as still OPEN.** v37’s integration notes state that the residual phase budget `O(δ log m)` is integrated, while the *phase‑class UE inequality with p≥1/2* remains open, and the local term’s growth remains the obstacle absent micro‑window clustering / pair isolation. 【717:12†integration_notes_v37.md†L1-L9】

---

## 1) Task A — Instantiate the S5′ acceptance gate for the *current* phase endpoint (v37)

### A.1 Candidate endpoint and forcing hypothesis

- **Candidate endpoint (v37 concrete):**  
  \[
    \widetilde D_B(W):=\max_{1\le j\le 4}\bigl|\Delta_{S_j}\arg W\bigr|
  \]
  on the buffered contour `∂B_{κ/2}` (Definition 12.16). 【721:10†manuscript_v37.pdf†L55-L85】

- **Forcing (already proven):**  
  If `W` has at least one zero in `B^\circ_{κ/2}`, then  
  \[
  \widetilde D_B(W)\ge \frac{\pi}{2}.
  \]
  (Lemma 12.17) 【721:10†manuscript_v37.pdf†L86-L110】

This satisfies the *S5′–FORCE* half **in the phase class** (direct forcing of the phase endpoint, not via `D_B`). 【721:2†v37_patchlog.md†L1-L6】

### A.2 Best available upper control in v37 (what we can actually justify right now)

What v37 actually proves in the phase toolkit is a **prototype split** on shifted segments:

- residual phase contribution on a vertical segment is `O(δ log m)` (Cor. 12.15);  
- local phase contribution is **δ‑inert** and bounded by `π N_loc(m)` (Lemma 12.14). 【721:10†manuscript_v37.pdf†L1-L54】

Crucially: this is **not yet** a proof of the required S5′ “UE+SPLIT” bound for `\widetilde D_B(W)` with a **common prefactor** `δ^p` and δ‑uniform constants; v37 records that as the missing lever. 【717:12†integration_notes_v37.md†L1-L9】

### A.3 Extracting the exponent tuple implied by the *available* phase split (referee check)

If one tries to shoehorn the currently available prototype bound into the gate template
\[
\widetilde D_B(W)\ \le\ C_{\rm up}\,\delta^{p}\Bigl(\mathrm{Res}(m)+C_{\rm loc}\,\delta^{-\theta}G(N_{\rm loc}(m),\kappa)\Bigr),
\]
the local term’s δ‑inert behavior forces **p=θ** (or equivalently `p−θ=0`), because each local zero contributes `O(1)` to the phase and there are `N_loc(m)` of them. 【721:10†manuscript_v37.pdf†L1-L54】

A concrete instantiation looks like:

- choose `p=1` so the residual term can be written as `δ^1·Res(m)` with `Res(m) ~ log m`;
- then the local term must be written as `δ^1·δ^{-1}·G(N_loc,κ)`, i.e. `θ=1` and `G(n,κ)≍n`.

This yields:
- `p−θ = 0` (δ‑inert local leakage),
- which **violates** the S5′ shrink condition `p−θ>0` and hence violates the acceptance gate. 【717:15†manuscript_v37.pdf†L18-L22】【717:15†manuscript_v37.pdf†L23-L39】

This is consistent with the manuscript’s own rejection of “pure Δarg endpoints” as having `p=0` and being unable to close under constant forcing. 【717:15†manuscript_v37.pdf†L33-L39】

### A.4 Referee‑grade decision paragraph for Task A

**Decision (as of v37): CONDITIONAL, with a baseline FAIL for the raw/prototype phase endpoint.**  
v37 provides a forceable phase endpoint `\widetilde D_B(W)` and a prototype residual+local phase split, but the only rigorously supported local phase control is δ‑inert per zero (Lemma 12.14), which forces `p=θ` in any attempted UE+SPLIT encoding and therefore violates the acceptance gate condition `p−θ>0` in Theorem `thm:S5prime-closure`. 【721:10†manuscript_v37.pdf†L1-L54】【717:15†manuscript_v37.pdf†L18-L22】  
Accordingly, **S5′ is not yet “live”**: it becomes live **iff** the batch‑7 candidate supplies the missing lever in one of the explicitly permitted forms (phase‑class UE with `p≥1/2` *and* compatible local exponent; or micro‑window / pair‑isolation reducing effective `q`) while keeping δ‑uniform constants. 【717:13†manuscript_v37.pdf†L1-L23】【717:0†CR_master_dashboard_v37_locked.md†L8-L22】

---

## 2) Task B — v38‑ready “Missing Lever box” (no silent closure policy)

Below is a paste‑ready TeX block designed to replace (or sit immediately under) the current OPEN box in Section 12.

### B.1 Paste‑ready TeX: “Missing Lever (S5′) — statement + branch ownership + latch”

```tex
% === BEGIN: Missing Lever box (S5') ===
\begin{center}
\fbox{\begin{minipage}{0.96\linewidth}
\textbf{OPEN (Missing Lever for S5$'$ tail closure; no silent closure).}
\vspace{2mm}

Fix $\eta\in(0,1]$, $\kappa\in(0,1/10)$, and the nominal scale
$\delta_0(m,\alpha)=\eta\alpha/(\log m)^2$.
Let $B=B(\pm \alpha,m,\delta)$ be any $\kappa$--admissible aligned box with $0<\delta\le \delta_0(m,\alpha)$.
Let $G_{\rm out}$ be the Dirichlet outer factor on $B^\circ$ and $W:=E/G_{\rm out}$ the corresponding quotient.
Let $\widetilde D_B(W)$ be the buffered boundary phase endpoint (Def.~\ref{def:Db-tilde-phase}).

\medskip
\textbf{FORCE (already proved).}
If $W$ has a zero in $B^\circ_{\kappa/2}$ then $\widetilde D_B(W)\ge \pi/2$
(Lemma~\ref{lem:phase-forcing-argprinciple}).

\medskip
\textbf{ENVELOPE (missing).}
To activate Theorem~\ref{thm:S5prime-closure}, it remains to prove a phase-class UE+split bound of the form
\[
\widetilde D_B(W)\ \le\ C_{\rm up}\,\delta^{p}\Bigl(\mathrm{Res}(m)+C_{\rm loc}\,\delta^{-\theta}\,G(N_{\rm eff}(m,\delta),\kappa)\Bigr),
\]
uniformly for all $m\ge 10$, all $\alpha\in(0,1]$, and all $\kappa$--admissible $0<\delta\le\delta_0(m,\alpha)$,
with $C_{\rm up},C_{\rm loc}$ independent of $\delta$ and with an explicit growth model
$G(n,\kappa)\le C_G\,\kappa^{-u}\,n^{q}$.

\medskip
\textbf{BUDGET GATE (non-negotiable).}
The declared exponent tuple $(p,\theta,q)$ must satisfy the acceptance gate:
\[
2p\ge 1,\qquad 2(p-\theta)\ge q,\qquad p-\theta>0,
\]
otherwise uniform $\eta$--shrinking at $\delta=\delta_0(m,\alpha)$ is impossible under constant-limited forcing.

\medskip
\textbf{LOCAL REDESIGN (one of these is decisive).}
Because phase is $\delta$--inert per zero (Lemma~\ref{lem:local-phase-delta-inert}),
the default choice $N_{\rm eff}(m,\delta)=N_{\rm loc}(m)\sim \log m$ forces $q=1$.
Any one of the following would be decisive:
(i) a phase-class UE mechanism achieving $p\ge 1/2$ while keeping $\theta=0$ in the same endpoint class;
(ii) a micro-window clustering bound $N_{\rm eff}(m,\delta_0)=O(1)$ (so $q=0$ effectively);
(iii) a pair-isolation mechanism: only the forced pair contributes $O(1)$ to $\widetilde D_B$ while the remainder contributes $O(\delta\log m)$.

\medskip
\textbf{NO CLAIM POLICY.}
Until the ENVELOPE bound and one decisive LOCAL redesign item are proved in-text (or cited referee-grade),
the manuscript makes \emph{no} claim of tail closure and \emph{no} claim of RH from S5$'$.
\end{minipage}}
\end{center}
% === END: Missing Lever box (S5') ===
```

**Notes (referee intent):**
- This box latches the precise acceptance gate already stated in v37 (Theorem `thm:S5prime-closure` + Remark gate). 【717:15†manuscript_v37.pdf†L18-L39】
- It explicitly prevents “closure tone” unless the UE+split inequality and one LOCAL redesign route are actually proved.

---

## 3) Task C — CR dashboard delta (minimal, no drift)

### C.1 What becomes CLOSED if “Missing Lever” is proved

If the ENVELOPE inequality in the box is proved with δ‑uniform constants and an exponent tuple passing the budget gate, then:

- **G‑4′ (PHASE‑CLASS UE / ENVELOPE)** becomes **CLOSED**. 【717:0†CR_master_dashboard_v37_locked.md†L8-L22】

If, in addition, either `N_eff(m,δ0)=O(1)` (micro-window) or the pair-isolation statement is proved:

- **G‑8 (LOCAL MICRO‑WINDOW)** becomes **CLOSED** (or CLOSED‑BY‑ROUTE with a note of which route). 【717:0†CR_master_dashboard_v37_locked.md†L10-L22】

Separately, the program still must close:

- **G‑2b** (alignment): rewrite tail to target `\widetilde D_B` or prove transfer `\widetilde D_B ↔ D_B`. 【717:0†CR_master_dashboard_v37_locked.md†L8-L12】

### C.2 New gap IDs?

**Recommendation: no new canonical gap IDs.**  
The existing trio **G‑2b / G‑4′ / G‑8** already partitions the “Missing Lever” into the correct three closure obligations (alignment, phase‑UE, local growth). The v37 next build plan already reflects this partition in GO‑criteria form. 【717:1†v37_next_build_plan_diff.md†L8-L13】

If CR wants finer tracking, add *subtasks* under each gap (non-canonical), e.g.:

- G‑4′a: “phase‑UE inequality proves p≥1/2 (not absolute‑L^r)”
- G‑4′b: “δ‑uniformity of C_up and any endpoint constants”
- G‑8a: “micro-window clustering at δ0”
- G‑8b: “pair-isolation remainder phase budget O(δ log m)”

But keep canonical IDs stable.

---

## 4) S6 harness check (explicit‑formula interpretation)

v37’s Appendix “S6 harness” is explicitly marked as **interpretive only** (no logical dependencies). 【721:3†manuscript_v37.pdf†L59-L62】

- **Direct amplitude‑leak consequence from S5′ endpoint chain:** none established. The endpoint `\widetilde D_B(W)` is a localized boundary phase/winding functional; by itself it is not an explicit‑formula quantity.

- **Indirect consequence if S5′ closure succeeds:** the chain would eliminate off‑critical‑line zeros (RH, with front‑end). RH is well known to be equivalent to eliminating the `x^\beta` amplitude leaks in the explicit formula, and v37’s harness records the mapping `a=2\beta-1` (v‑displacement) for interpretive consistency. 【721:3†manuscript_v37.pdf†L63-L70】

Referee posture: keep S6 as “interpretation only” until a separate, fully cited implication is written.

---

# MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* **Callsign:** RH-ABSORB
* **Result classification:** **CONDITIONAL**
* **Target gaps closed (by ID):**
  - None closed by this branch in batch‑7; this is a referee/integration latch.
* **Target gaps still open (by ID):**
  - **G‑2b** (forcing ↔ endpoint alignment for S5′)
  - **G‑4′** (phase‑class UE/envelope inequality with p≥1/2 and δ‑uniform constants)
  - **G‑8** (micro‑window clustering / pair‑isolation reducing effective local growth q)
  - **G‑6** (Bridge‑1 sharpened for phase endpoints: neighborhoods along shifted segments + buffered contour)
* **Key conclusions (≤5 bullets):**
  1. v37’s concrete phase endpoint `\widetilde D_B(W)` is **forceable** (π/2 lemma), but **not yet shrinkable** because the proven local phase control is δ‑inert per zero.
  2. Without a new phase‑class UE mechanism giving `p−θ>0` (and budget `2(p−θ)≥q`), S5′ cannot become live.
  3. The v38 “Missing Lever box” above is the minimal no‑drift latch that prevents accidental proof tone.
  4. No new canonical gap IDs are needed; G‑2b/G‑4′/G‑8 already cover the full missing‑lever surface.
  5. S6 explicit‑formula language remains **interpretive only**; do not treat it as a derived corollary from endpoint closure.
* **Paste-ready manuscript edits (TeX blocks):**
  1. Insert the “Missing Lever box (S5′)” block in Section 12 near Theorem `thm:S5prime-closure` / Remark gate (see §2 above).
  2. (Optional) Add one sentence at the end of Remark `rem:S5prime-gate`: “The OPEN box ‘Missing Lever for S5′’ is the sole analytic completion item; until closed, `missing_lever_open=true`.”
* **Dependencies on other branches:**
  - **RH-ENVELOPE:** must supply the phase‑class UE inequality (non‑pointwise, non‑absolute‑L^r) with explicit p≥1/2 and δ‑uniform constants.
  - **RH-LOCAL:** must supply micro‑window clustering at δ0 *or* a pair‑isolation mechanism, and phrase it in the phase endpoint class.
  - **RH-BRIDGE:** must sharpen Bridge‑1 for the buffered contour and shifted segments (nonvanishing neighborhoods).
  - **RH-FORCE:** already supplies the π/2 forcing lemma for `\widetilde D_B(W)`; may be needed if endpoint changes.
* **Referee risk notes (anticipated objections + how addressed):**
  1. **Hidden δ‑dependence:** the box forces explicit δ‑uniformity quantifiers and prohibits “C(δ)” constants.
  2. **Budget drift:** acceptance gate inequalities are latched explicitly; any candidate must declare (p,θ,q) and pass them.
  3. **Endpoint‑class cheating:** explicitly rejects proofs that reduce to absolute `L^r(∂B)` collar estimates (already NO‑GO in v37).
  4. **Forcing disconnect:** G‑2b remains open unless tail is rewritten to target `\widetilde D_B` or a transfer lemma is proved.
