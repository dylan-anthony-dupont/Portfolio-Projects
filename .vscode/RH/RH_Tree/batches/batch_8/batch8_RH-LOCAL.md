# batch8_RH-LOCAL.md

**PROGRAM:** RH Convergence Program  
**CALLSIGN:** RH-LOCAL  
**GROUND TRUTH:** v38 locked build (`manuscript_v38.pdf`, `CR_master_dashboard_v38_locked.md`, `integration_notes_v38.md`).

## Mechanism choice (mandatory): **(M2) `N_eff(m,δ0)=O(1)` via micro-window clustering**

**Intent:** Defeat the phase-class “single-pole test” obstruction by ensuring the *effective* local growth exponent is **q = 0** at the nominal scale `δ0(m,α) = ηα/(log m)^2`. Under S5′’s budget gate, this would allow a phase-class UE exponent as small as `p = 1/2` (with `θ = 0`) to pass uniformly, since the local term would be constant-limited.

**Why this would defeat the one-pole model:** If `N_eff(m,δ0) ≤ C0` uniformly, then the local phase contribution on the buffered contour can be bounded by `O(C0)` (θ=0), and any UE mechanism yielding `p ≥ 1/2` would force `\widetilde D_B(W) = O(δ0^{p})` at the nominal scale; since `δ0→0` with `m→∞`, this can contradict the constant forcing `\widetilde D_B(W) ≥ π/2` under an interior zero.

**Decision outcome (this batch):** **NO-GO / FAIL** under the current v38 toolchain and known unconditional inputs, unless a *new, genuinely short-interval zero-count theorem* is imported (with explicit constants).

---

## A) Why micro-window clustering is not currently derivable (proof-grade NO-GO)

### A.1 What v38 would need, precisely

In v38, the nominal box scale is
\[
\delta_0(m,\alpha)=\frac{\eta\alpha}{(\log m)^2},\qquad m\ge 10,\ \alpha\in(0,1].
\]
A “micro-window clustering” lever requires an **unconditional** bound of the schematic form
\[
N_{\mathrm{eff}}(m,\delta_0)\ :=\ \#\{\rho\in Z(E): |\Im(\rho)-m|\le c\,\delta_0\ \text{and}\ \rho\ \text{is relevant to the endpoint}\}\ \le C_0
\]
with constants **independent of** `m,α,δ0` (and compatible with κ-shrinking). See the v38 OPEN-box list of decisive LOCAL redesign options. fileciteturn5file4

Even in the *weakest* interpretation “count zeros in a vertical window”, one would need something like
\[
N_v(m+\delta_0)-N_v(m-\delta_0)\ \le\ C_0
\]
for the v-frame counting function `N_v` of `E(v)=\Xi_2(1+v)`.

### A.2 Reduction to classical short-interval zero counts

Let `ρ_s = β+iγ` be a nontrivial zero of ζ in s-frame. In the program’s mapping:
- `u = 2s`, `v = u-1`, so `v_ρ = (2β-1) + i(2γ)`.
- Therefore `\Im(v_ρ)=2γ` and the “classical height” is `T := γ = \Im(v)/2`.

Thus, a v-window of half-width `H_v` corresponds to an s-window of half-width `H_s := H_v/2`.

So a micro-window of half-width `H_v = δ0(m,α)` corresponds to
\[
H_s = \frac{\delta_0(m,\alpha)}{2} \asymp \frac{1}{(\log m)^2} \asymp \frac{1}{(\log T)^2}
\]
(up to harmless constants, since `m=2T`).

### A.3 The toolchain obstruction: explicit RvM error is too large

The strongest unconditional “plug-and-play” input currently integrated in the lineage (and used earlier for G‑8 closure) is a *global* zero-counting bound of the type
\[
N(T) = \frac{T}{2\pi}\log\!\Big(\frac{T}{2\pi}\Big)-\frac{T}{2\pi} + O(\log T),
\]
often with explicit constants in the `O(\log T)` term.

**Key point:** an `O(\log T)` error term is far too large to control **short intervals** with half-width `H \ll 1`, and certainly with `H \asymp 1/(\log T)^2`.

#### Lemma (NO-GO: explicit RvM with `O(log T)` error does not imply micro-window `O(1)` bounds)
Assume an explicit bound of the form
\[
N(T)=M(T)+E(T), \qquad |E(T)| \le C\log T \ \ (T\ge T_0),
\]
where `M(T)` is the usual main term and `C>0` is explicit.

Then for any `H\in(0,1]`,
\[
N(T+H)-N(T-H)\ \le\ \big(M(T+H)-M(T-H)\big)\ +\ 2C\log(T+H).
\]
For `H = c/(\log T)^2`, the main-term difference is `\ll H\log T \asymp 1/\log T`, but the error contribution is still `\asymp \log T` in general. Hence this method cannot yield `N(T+H)-N(T-H)=O(1)` uniformly.

**Proof sketch:** subtract the decomposition at `T±H` and use the triangle inequality on `E(T±H)`.

**Interpretation:** to get an `O(1)` bound for `H\asymp 1/(\log T)^2`, one would need error control that is essentially **Lipschitz on scale H**, i.e. `E(T+H)-E(T-H)=O(1)` (or better), which is far stronger than any explicit unconditional `O(\log T)` error bound presently available/used.

### A.4 Consequence for v38: M2 is not currently a proof-grade lever

Given v38’s reliance on explicit but *global* zero-count bounds and the absence (in the current integrated inputs) of any **short-interval** theorem with explicit constants at scales `H \asymp 1/(\log T)^2` (or even `H\asymp 1/\log T`), **RH-LOCAL cannot certify** `N_eff(m,δ0)=O(1)` at the nominal scale.

Therefore mechanism **(M2) is a NO-GO under current inputs**.

---

## B) What would be needed to make M2 viable (requirements for a future import)

To revive (M2) honestly, v39+ would need to import (and cite) a theorem of the following type, with explicit constants:

> **Short-interval zero count (explicit):** for all `T ≥ T0` and all `H` in a specified regime (at least down to `H \asymp 1/(\log T)^2`),
> \[
> N(T+H)-N(T-H) \le A\,H\log T + B
> \]
> (or any bound implying `O(1)` at `H=\delta_0/2`).

As of the v38 integrated toolchain, we do not have such an input available in-text, and the earlier “global N(T) bound” route cannot supply it (Lemma above).

---

## C) v39-facing manuscript edits (labeling + narrowing)

Since M2 cannot currently be justified, the responsible action in v39 is to **tighten the OPEN box** so that M2 is explicitly flagged as requiring *new* external analytic-number-theory input (short-interval counting), and is not treated as “available from N(T) technology.”

### Paste-ready TeX edits (surgical)

#### (i) Add a remark immediately after Lemma `lem:local-isolation-needed` (v38 Lemma 12.3)

```tex
\begin{remark}[LOCAL redesign option (ii) requires short-interval zero counts (currently not available)]
The micro-window clustering lever (option (ii) in the OPEN box) requires an \emph{explicit short-interval}
zero-count theorem at the nominal scale $\delta_0(m,\alpha)=\eta\alpha/(\log m)^2$.
In $s$-height variables $T=\Im(s)=m/2$, this corresponds to a window half-width
$H=\delta_0/2 \asymp 1/(\log T)^2$.
Global explicit bounds for $N(T)$ with $O(\log T)$ error (Riemann--von Mangoldt type) do \emph{not}
control $N(T+H)-N(T-H)$ at such $H$; the error term dominates and one cannot deduce $O(1)$ micro-window
bounds without a genuinely short-interval input.
Accordingly, option (ii) should be treated as \textbf{NEW INPUT REQUIRED} until such a theorem
(with explicit constants and a stated $H$-regime) is imported and cited.
\end{remark}
```

#### (ii) Tighten the OPEN-box bullet (ii) in Section 12 (S5′ frontier)

```tex
(ii) a micro-window clustering bound $N_{\mathrm{eff}}(m,\delta_0)=O(1)$
\emph{(NEW INPUT REQUIRED: explicit short-interval zero counts at }$H\asymp \delta_0/2\emph{)};
```

---

## D) Handoff block to ENVELOPE / ABSORB (what LOCAL can certify post-v38)

- **Certified (already in v38):** phase-local per-zero δ-inertness on line segments (Lemma 12.17) and the prototype split showing residual phase is `O(δ log m)` while local phase is δ-inert. fileciteturn4file10  
- **Not certified / decisive missing lever:** any reduction `N_eff(m,δ0)=O(1)` at `δ0=\eta\alpha/(\log m)^2`.

**Implication for budgets:** unless a true short-interval theorem is imported, LOCAL can only support the default `q=1` growth model (`N_loc(m)\asymp \log m`) and cannot supply an “effective q=0” path. In that case, S5′ can only survive if ENVELOPE supplies a phase-class UE+split inequality with **p ≥ 1/2** while keeping **θ = 0** (as already noted in the OPEN-box decisive list). fileciteturn5file4

---

## E) S6 explicit-formula amplitude-leak mapping (mandatory)

A micro-window clustering statement is primarily about **zero distribution in height** (control of `γ` in `ρ=β+iγ`) on very short scales. This does **not** directly correspond to an `x^\beta` amplitude leak in the explicit formula: the amplitude leak is governed by `β` (real part), whereas micro-window clustering is a statement about how many `γ`’s fall into a tiny interval.

At best, micro-window clustering would be an *auxiliary analytic lever* to keep the boundary-phase local term subcritical; it would not, by itself, certify that an off-axis `β>1/2` contribution is absent in an explicit-formula sense.

Mapping reminder (program hygiene): `v = (2β-1) + i(2γ)`, so controlling micro-windows in `\Im v` is controlling micro-windows in `γ` (frequency `e^{i\gamma\log x}`), not amplitudes `x^\beta`.

---

# MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* **Callsign:** RH-LOCAL
* **Result classification:** **FAIL / NO-GO (for M2 at v38 inputs)**
* **Target gaps closed (by ID):** none newly closed in this batch
* **Target gaps still open (by ID):**
  - **G‑4′ (Missing Lever / phase-class UE+split): OPEN**
  - **G‑8 (Local technology): PARTIAL (θ=0 per-zero phase is closed; “decisive LOCAL redesign” remains open)**
* **Key conclusions (≤5 bullets):**
  1. Micro-window clustering at the nominal scale `δ0(m,α)=ηα/(log m)^2` requires **short-interval zero counting** with explicit constants at `H\asymp 1/(\log T)^2`.
  2. The current toolchain’s explicit `N(T)` bounds with `O(\log T)` error cannot yield `N(T+H)-N(T-H)=O(1)` at such `H` (error dominates).
  3. Therefore mechanism **(M2) is not presently proof-grade**; treat it as **NEW INPUT REQUIRED**.
  4. In absence of (M2), S5′ must rely on **ENVELOPE delivering `p ≥ 1/2` with `θ=0`**, or on a different decisive LOCAL mechanism (M1/M3).
* **Paste-ready manuscript edits (TeX blocks):**
  - (i) remark after Lemma 12.3 (LOCAL isolation needed) flagging “short-interval zero counts required”
  - (ii) tightened OPEN-box bullet labeling option (ii) as “NEW INPUT REQUIRED”
* **Dependencies on other branches:**
  - ENVELOPE: must decide whether a phase-class UE mechanism with `p ≥ 1/2` and `θ=0` is plausible without importing new number theory.
  - ABSORB: budget gate evaluation once ENVELOPE proposes `(p,θ,q)`; LOCAL contributes no new positive lever here.
* **Referee risk notes (anticipated objections + how addressed):**
  - *Objection:* “But average zero spacing is ~`1/\log T`, so micro-window should have O(1) zeros.”  
    *Response:* average spacing is not a uniform upper bound; without a short-interval theorem, clustering on smaller scales is not ruled out.
  - *Objection:* “Can’t we just use the explicit RvM formula?”  
    *Response:* explicit RvM provides only `O(\log T)` error, which is too coarse to control `N(T+H)-N(T-H)` for `H\ll 1`.
  - *Objection:* “This is too pessimistic.”  
    *Response:* the manuscript is audit-grade; without a citable theorem with constants and regime, M2 must remain labeled as new input.
