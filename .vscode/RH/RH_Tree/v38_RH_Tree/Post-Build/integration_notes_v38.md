# Integration Notes — v38 (post-build)

**Build:** v38 (from v37 + Batch‑7 queue)  
**Date:** 2026-01-25  
**Integrator posture:** v38 is a *truth‑latching* narrowing build: it seals drift, codifies NO‑GO constraints, and latches the frontier to the single boxed OPEN statement (“Missing Lever”).

---

## 1) What is now hard‑locked (new in v38)

### (i) Endpoint alignment is now explicit (G‑2b CLOSED)
- The forced contradiction endpoint is now unambiguously the **buffered phase endpoint** `\widetilde D_B` (Def. `def:Db-tilde-phase`).
- Any alternative endpoint `\Phi_B` is admissible only if it provably dominates `\widetilde D_B` or has its own forcing lemma (Remark `rem:forceability-phase-gate`).

### (ii) Bridge/collar safety is now in-text (G‑6 CLOSED)
- κ‑admissibility implies **collar nonvanishing** on `\partial B_{\kappa/2}` (Lemma `lem:phase_collar_nonvanishing`), so the argument increments defining `\widetilde D_B` are well‑posed and branch‑safe.

### (iii) Local phase control is now endpoint‑class explicit (G‑8θ CLOSED)
- Local term is δ‑inert per zero on *any line segment* (Lemma `lem:local_phase_delta_inert`).
- Consequently the buffered boundary local contribution is bounded by `\pi N_loc(m)` per side (Cor. `cor:local_phase_on_buffered_boundary`).

### (iv) Endpoint‑only NO‑GO constraint installed (new latch; frontier narrowing)
- Lemma `lem:phase-UE-theta0-nogo` proves: **θ=0 per pole (δ‑inert endpoint‑only control) forbids any UE gain p>0** for the phase endpoint.
- This converts the vague “recover p>1” folklore into a hard structural filter: S5′ must defeat the one‑pole model (pair isolation/cancellation or truly new UE tech).

### (v) Missing Lever is now non‑silent and budget‑gated
- The OPEN box in Section 12 has been rewritten as a **hard latch**:
  - FORCE is proved (`\widetilde D_B \ge \pi/2`),
  - ENVELOPE is missing,
  - the acceptance gate (`2p≥1`, `2(p-θ)≥q`, `p-θ>0`) is mandatory,
  - a LOCAL redesign item must be supplied,
  - **no RH claim** until these are proved/cited.

---

## 2) What remains open (and is now sharper)

### Primary frontier: **G‑4′ (Missing Lever) — OPEN**
We still lack a referee‑grade **phase‑class UE + split inequality** of the form required by Theorem `thm:S5prime-closure`, with an exponent tuple that passes the gate.

**Newly sharpened choices:**
1. **Local isolation / pair‑dominance**: show the “rest” local factor contributes δ‑small in the chosen endpoint class (Lemma `lem:local-isolation-needed`).
2. **Non‑pointwise UE redesign**: a mechanism that defeats the one‑pole obstruction without hidden RH‑equivalent assumptions.
3. **Micro‑window clustering bound**: `N_eff(m,δ0)=O(1)` at the nominal scale, so the local growth exponent effectively drops to `q=0`.

---

## 3) Canonical posture update (post‑v38)

- **Primary frontier:** S5′ (phase/winding endpoint redesign) — still *conditional*; now hard‑latched with explicit NO‑GO filters.
- **Secondary harness:** finite band / certificate harness remains as an audit scaffold (repro pack latches remain fail‑closed).

**No drift rule (reinforced):** v38 is explicit that RH closure is not claimed until the ENVELOPE inequality and a decisive LOCAL redesign are proved.

