# RH-CR Master Dashboard — Batch 5 (pre‑v36)

Date: 2026-01-24  
Baseline locked: **v35** (2026-01-23)  
Primary frontier: **S5′ = forceable cancellation endpoint redesign** (non‑absolute, non‑projection)  
Audit scaffold: **S2-style certified criterion/harness** (unchanged)

---

## (1) What Batch‑5 changed (decision-grade)

### New hard guardrails (drift‑prevention)
- **S5 acceptance criterion + general budget calculus** (must specify \(\Phi_B\), exponents \((p,	heta,q)\), δ‑uniform constants, and forceability mode).  
- **NO‑GO: absolute \(L^r(\partial B)\) endpoints of \(|E'/E|\)** ⇒ local term is δ‑inert (forces \(p(r)=	heta(r)=1-1/r\)).  
- **NO‑GO: projection endpoints that annihilate the local kernel span** cannot control forced dial deviation \(D_B(W)\) without changing forcing/contradiction endpoint.
- **Forceability gate hardened:** if S5 endpoint changes away from forced \(D_B(W)\), you must prove \(\Phi_B\ge D_B(W)\) or a new forcing lemma.

### What remains open (the *actual* frontier)
- A **positive** S5 design: cancellation / less singular boundary data that
  1) still upper-bounds \(D_B(W)\) with a gain \(\delta^{p}\),  
  2) has a local interface \(\Phi_B(Z'_{m loc}/Z_{m loc})\lesssim \delta^{-	heta}G(N_{m loc})\), and  
  3) clears the budget \(2(p-	heta)\ge q\) with \(p-	heta>0\), all δ‑uniform.

---

## (2) Ranked blocker queue (post‑Batch‑5)

1. **S5–UE (CRITICAL):** invent a *cancellation* (non‑absolute) endpoint \(\Phi_B\) and prove a UE inequality with explicit \(p\) and δ‑uniform constants.  
2. **S5–RES (CRITICAL):** residual envelope bound in the *same* endpoint class (constant provenance!).  
3. **S5–LOC (HIGH):** local/collar bound in the *same* endpoint class with explicit \(	heta\) and growth model \(G\).  
4. **S5–FORCE (HIGH):** show forceability: either \(\Phi_B\ge D_B(W)\) or prove forcing transfer lemma.  
5. **G‑1/G‑12 (HIGH):** residual-envelope constants ledger + citations must be proof-grade and δ‑uniform.

---

## (3) Live Gap Register (canonical IDs + S5 subitems)

| Gap ID | Status (v35) | Status after Batch‑5 | Notes |
|---|---:|---:|---|
| **G-1** constant provenance ledger | OPEN | **OPEN** | still the residual-envelope bottleneck |
| **G-2** what is bounded (W vs residual) | MUTATED→S5 | **MUTATED→S5′** | now explicitly “cancellation endpoint” required |
| **G-3** K_alloc provenance | CLOSED | CLOSED | stable |
| **G-4** δ‑uniformity for absorption | CLOSED‑AS‑NOGO | **CLOSED‑AS‑BUDGET** | generalized S5 budget theorem/acceptance test ready to encode |
| **G-5** κ‑admissibility interactions | OPEN (S5‑dep.) | **OPEN (S5‑dep.)** | budget theorem adds monotonicity condition \(p-	heta\ge 0\) |
| **G-6** Bridge‑1 hypotheses | CLOSED (one‑way) | CLOSED | stable |
| **G-7** free‑m hygiene | IN PROGRESS | IN PROGRESS | keep auditing with each new S5 attempt |
| **G-8** local window bound | CLOSED | CLOSED | local toolkit extended (L^2 collar bounds; projection facts recorded as closed routes) |
| **G-11** external computation reliance | DEFERRED | DEFERRED | unchanged (front-end certificate still quarantined) |
| **G-12** verification discipline | OPEN | **OPEN (hardened)** | forceability gate + S5 metadata latch ready to encode |

**S5 subitems (search-space status):**
- **S5‑ABS‑Lp endpoints:** CLOSED (NO‑GO; do not revisit).  
- **S5‑PROJ endpoints:** CLOSED (NO‑GO under current forcing target).  
- **S5‑CANCEL endpoints:** OPEN (only viable remaining class).

---

## (4) Minimal S5 dependency DAG (unchanged skeleton; updated constraints)

**Forcing (closed, constant‑limited):** off‑axis quartet ⇒ lower bound on \(D_B(W)\).  
**S5 UE (OPEN):** \(D_B(W)\) ≤ \(\delta^{p}\Phi_B\) (must be *cancellation / non‑absolute*).  
**S5 split (OPEN):** \(\Phi_B(E'/E)\) ≤ Residual(m) + Local(m,δ).  
**Budget (closed as theorem):** accept S5 only if \(2(p-	heta)\ge q\) + forceability + δ‑uniform constants.  
**Tail closure:** if S5 passes budget uniformly + residual ledger closed ⇒ global RH (with front‑end certificate).

---

## (5) v36 pre‑build intent

**v36 is a guardrail build**: codify S5 acceptance criterion + NO‑GO results in-text (and Appendix),
so future versions cannot drift back into dead endpoint classes.
