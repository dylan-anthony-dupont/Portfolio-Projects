# v44 Build Protocol — Pre‑Batch‑15

## Objective
Prepare v44 as a **clarifying pre-build** that makes the single open frontier (UE‑INPUT) maximally explicit, and records the Weil/Li harness without changing the main closure chain.

## Inputs
1. v43 locked manuscript + artifacts.
2. Legacy Weil/Li bridge note (validated against Burnol 1998 expository paper).

## Steps

### Step 1 — Apply documentation patch queue (P0–P2)
Implement:
- Appendix UE Playbook (P0).
- Appendix Weil/Li bridge harness (P1).
- δ‑shrink quantifier contract (P2).

### Step 2 — Freeze the frontier
- Keep v43’s single active UE‑INPUT box unchanged.
- Mark signed k=2 interface as "inactive candidate" only.

### Step 3 — Batch‑15 prompt design (next pass)
Batch‑15 will be targeted to:
1) prove UE‑INPUT as stated, or
2) prove a NO‑GO lemma showing UE‑INPUT is RH-strength/false, or
3) produce a strictly better replacement interface plus a proof-grade reduction.

### Step 4 — Post Batch‑15 decision gates
- If proof: v44 becomes a closure build.
- If NO‑GO: v44 demotes UE‑INPUT and promotes the best replacement, updating FORCE/UE‑REDUCE only as needed.
- If Weil bridge becomes concrete: add it as a secondary harness; do not replace the main chain unless it closes.

## Mandatory output artifacts (after Batch‑15)
- Updated dashboard, integration notes, next build diff, patch queue.
- If closure achieved: v44 post-build manuscript + repro pack.