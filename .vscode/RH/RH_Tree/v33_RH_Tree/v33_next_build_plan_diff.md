# v33 → next build plan (diff-only)

Now that **v33 is locked**, the next build iteration should be *targeted* and short.
This file lists only the next deltas to pursue.

## Δ‑NEXT‑1 (CRITICAL): Close G‑1 / G‑12 (constant ledger provenance)

Deliverable: a Patch Packet that replaces the *assumed* residual envelope lemma with a complete proof and explicit constant bookkeeping, including:
- exact hypotheses on E, frame, and box scale,
- where C1,C2 come from,
- proof that C1,C2 are δ‑independent (or explicit δ dependence tracked and shown harmless),
- consequences for C_up and C_h''.

## Δ‑NEXT‑2 (CRITICAL): Close G‑4 δ‑uniformity for absorption

Deliverable: a single “δ‑uniformity audit” lemma bundle:
- constants used in tail inequality do not smuggle dependence on unknown zeros,
- κ‑policy and δ‑shrink do not change any constant provenance,
- any remaining parameter dependencies are explicit and monotone-safe.

## Δ‑NEXT‑3 (HIGH): Close G‑2 scaling audit (upper‑envelope chain)

Deliverable: a referee-grade “exponent ledger” from:
Bridge‑1 → upper envelope → log-derivative split → residual+local bounds → tail inequality

Must include:
- which quantity is bounded (W vs residual vs E),
- no unjustified √δ or limit swaps,
- explicit use of Corollary UE-residual-local (no proxying).

## Δ‑NEXT‑4 (MED): Close G‑7 quantifier hygiene

Deliverable: a global sweep:
- “m” free height variable vs “m/2” etc,
- off-axis vs on-axis language,
- remove any RH-equivalent phrases from definitions.

