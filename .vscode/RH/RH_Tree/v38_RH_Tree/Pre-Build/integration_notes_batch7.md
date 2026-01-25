# Integration Notes — Batch 7 (post v37 locked) — 2026-01-25

## 0) Executive digest (what changed)
Batch‑7 was targeted at the **Missing Lever** (S5′ phase endpoint closure). Net outcome:

- **Strong progress on “plumbing”:** forcing attaches cleanly to \(\widetilde D_B\); local θ=0 is proof‑grade on the buffered boundary geometry; Bridge hygiene patches are ready.
- **Decisive narrowing on “math frontier”:** ENVELOPE supplies an **endpoint‑only NO‑GO lemma** showing that any UE bound with a \(\delta^p\) prefactor (any \(p>0\)) is impossible by local analytic arguments if the endpoint class is δ‑inert per pole (single‑pole obstruction).  
  ⇒ The Missing Lever must now be formulated as: *find extra structure that defeats the one‑pole model* (pair‑isolation / cancellation / arithmetic forcing).

## 1) Branch payloads (Batch‑7)

### RH‑FORCE — PASS (forceability attachment + gate)
- Confirms v37’s Lemma 12.17 already provides **π/2 forcing** for \(\widetilde D_B(W)\).
- Provides a drop‑in corollary to **discharge (S5′‑FORCE)** in the budget theorem once \(\mathcal D_B\equiv \widetilde D_B\) is adopted.
- Adds a **forceability gate**: any alternative endpoint \(\Phi_B\) must dominate \(\widetilde D_B\) or come with a new forcing lemma.
- Also supplies a small parenthetical correction in Definition 12.11 (λ‑shift distance statement).

**Patch blocks:** `cor:S5prime-force-automatic`, Def 12.11 parenthetical correction, `rem:forceability-gate-phase`.

### RH‑LOCAL — PASS (G‑8 θ closed in phase class)
- Strengthens Lemma `lem:local_phase_delta_inert` to a fully general **line‑segment phase bound** (per zero ≤ π), and adds a corollary applying it to the buffered sides \(S_j\subset \partial B_{\kappa/2}\).
- Records exponent data in acceptance‑gate notation: **θ=0, q=1, u=0** for the phase‑increment class (growth still \(N_{\rm loc}(m)\)).

**Patch blocks:** replacement Lemma `lem:local_phase_delta_inert` + `cor:local_phase_on_buffered_boundary`.

### RH‑ENVELOPE — NO‑GO (endpoint‑only route), plus a new design filter
- Provides a decisive new lemma `lem:phase-UE-theta0-nogo`: if the endpoint class treats each Cauchy kernel \((v-\rho)^{-1}\) as \(O(1)\) uniformly in δ (strong “θ=0 per pole”), then **no UE inequality with any \(p>0\)** can hold by purely local analytic arguments (single‑pole test \(E(v)=v-\rho\)).
- Clarifies S6 harness is **interpretive only** (phase endpoints are zero‑presence witnesses, not amplitude‑leak observables, absent an extra transfer lemma).
- Supplies a “consequence remark” to insert near the Missing Lever box: any successful \(p\ge 1/2\) UE bound must incorporate **additional structure** (pair‑isolation / cancellation / forcing redesign / arithmetic).

**Patch blocks:** lemma `lem:phase-UE-theta0-nogo` + consequence remark.

### RH‑BRIDGE — CONDITIONAL (ready-to-close hygiene patches)
- Supplies a collar‑nonvanishing lemma ensuring phase increments are branch‑safe on \(\partial B_{\kappa/2}\) (Bridge‑1 strengthening for the phase endpoint toolkit).
- Fixes a wording/notation bug in Definition 12.11’s parenthetical (distance to boundary / λ‑shift hygiene).
- Adds an optional refined per‑zero phase bound depending on horizontal separation (helps motivate pair‑isolation).

**Patch blocks:** collar nonvanishing lemma + optional refined kernel bound remark.

### RH‑ABSORB — CONDITIONAL (referee/integrator latch)
- Provides a paste‑ready **“Missing Lever box (S5′)”** that latches quantifiers + acceptance gate and forbids silent closure tone.
- Re‑states the non‑negotiable acceptance gate: \(2p\ge 1\), \(2(p-\theta)\ge q\), \(p-\theta>0\).
- Emphasizes S6 explicit‑formula language stays interpretive only.

**Patch blocks:** Missing Lever box + optional one‑sentence latch in `rem:S5prime-gate`.

## 2) What becomes v38’s purpose (truth‑latching build)
v38 should:
1. **Close the ready-to-close plumbing gaps**: G‑2b (rewrite target), G‑6 (collar nonvanishing), G‑10 (wording fix), and the θ‑component of G‑8.
2. **Install the new NO‑GO filter in‑text** (so future work does not drift back into endpoint‑only attempts).
3. **Reframe the remaining frontier cleanly** as: *defeat the single‑pole model via extra structure* (pair isolation / cancellation / arithmetic).

## 3) Carry-forward reminders
- Keep `missing_lever_open = true` fail‑closed until the UE+local redesign is genuinely proved.
- Do not allow any UE proof path that collapses to absolute \(|E'/E|\) \(L^r(\partial B)\) controls (already codified NO‑GO in v37).
