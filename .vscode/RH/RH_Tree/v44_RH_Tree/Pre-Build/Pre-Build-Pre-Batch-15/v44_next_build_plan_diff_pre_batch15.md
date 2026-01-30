# v44 Next Build Plan (Diff‑Only) — Pre‑Batch‑15

Pre-build plan: changes intended for v44 relative to v43 **before** Batch-15 ingestion.

## 1) Documentation upgrades (safe, non-frontier)

1. Add Appendix "UE Playbook" (one page):
   - Restate the single active UE-INPUT.
   - List allowed decompositions of D_{a,h}.
   - Give candidate analytic routes (kernel-sum split; Hardy/Carleson; signed k=2).

2. Add Appendix "Weil/Li Bridge Harness":
   - State Weil positivity criterion (RH-equivalent) and Li criterion.
   - State Bridge Lemma target: identify the GEO-C4 k=2 channel with a Weil functional for a test family.
   - Add a caution box: L1 absolute-value interfaces lose phase; Weil is phase-sensitive.

## 2) No changes to the active closure box yet

- Keep UE-INPUT(v43) as the single active box until Batch-15 provides either:
  (i) a proof, or
  (ii) a proof-grade NO-GO, or
  (iii) a strictly better replacement interface with a proof-grade reduction.

## 3) Batch-15 decision gates (what v44 will do post-ingestion)

Gate G1: UE-INPUT(v43) proved RH-free -> keep; proceed to v44 build as a closure build.

Gate G2: UE-INPUT(v43) shown RH-strength/false -> demote; promote a signed/k=2 interface if available.

Gate G3: Weil/Li bridge lemma becomes concrete -> add as secondary harness; do not replace primary chain unless it closes.
