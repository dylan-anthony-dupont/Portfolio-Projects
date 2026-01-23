# v35 → next build plan (diff-only)

Locked baseline: v35 (2026-01-23)  
Next target: **S5 implementation draft** (endpoint redesign), without claiming closure

---

## 0. Non-negotiable constraints carried forward from v35 (do not regress)

- ENT hygiene stays: **E(v)=Xi₂(1+v)** with Xi₂(u)=xi(u/2) entire.
- Pointwise/sup UE endpoint is *not* a closure candidate:
  - UE exponent **p>1 is forbidden** (UE scaling NO-GO).
  - Exponent budget under δ₀ requires **p−θ ≥ 1/2**.
- Single-box forcing is constant-limited: do not assume forcing grows with m.
- No Bridge converse: |W|=1 on ∂B gives no interior zero-freeness.

---

## 1. S5 endpoint proposal (new work)

### S5-1: Choose a forceable non-pointwise endpoint Φ_B
Goal: replace sup_{∂B}|E'/E| with Φ_B(E) that still controls dial deviation D_B(W) in a UE inequality.

Deliverable in next version:
- A **definition** of Φ_B (clearly scoped: boundary functional; δ-normalized; invariant under shape normalization).
- A **forceability statement**:
  - either Φ_B ≥ D_B(W), or
  - a new forcing lemma lower-bounding Φ_B directly.

### S5-2: Prove UE inequality in Φ_B
Deliverable:
- A lemma of the form  
  D_B(W) ≤ C_up · δ^p · Φ_B(E)  
  with a proved exponent p and a δ-uniform constant ledger.

### S5-3: Local/residual split in Φ_B (avoid θ=1 pointwise blow-up)
Deliverable:
- Replace the pointwise collar bound by a Φ_B-local interface:
  Φ_B(E) ≤ Residual(m) + Local(m,δ)
- Track the **effective θ** in the new endpoint class.
- Must meet the budget p−θ > 1/2 under δ₀.

---

## 2. Residual envelope ledger (still required)

- Convert Lemma residual-envelope into referee-grade form:
  - cite or derive an RH-free bound for ζ'/ζ with explicit constants and parameter dependence
  - include how local-zero subtraction interacts with the chosen S5 endpoint.

---

## 3. Harness updates (to prevent silent mismatch)

- Extend repro pack schema to support:
  - endpoint_functional = "Φ_B(...)" (string + parameter list)
  - forcing_architecture (string)
  - any new constants introduced by Φ_B.
- Add verifier checks that the manuscript’s endpoint and the repro pack’s endpoint match.

---

## 4. Manuscript structure (diff-only edits)

- Keep v35’s Appendix “Discarded closure routes” (update with any newly ruled-out S5 variants).
- Replace Section S5 frontier (template) with:
  - Φ_B definition
  - forceability lemma
  - UE inequality lemma
  - new local/residual split lemma

No RH claim is permitted until:
- S5 meets exponent budget uniformly, AND
- residual ledger + front-end provenance are closed.

---
