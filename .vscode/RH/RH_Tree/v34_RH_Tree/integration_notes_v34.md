# Integration notes (v34)

Date: 2026-01-22

This file records which patch batches are integrated into `manuscript_v34.tex` and how they were applied.

## Batch 3 (UE–Gate audit): INTEGRATED
- UE lemma exponent corrected to **δ¹** (v33’s δ^{3/2} removed).
- New Lemma `eval-L2` inserted to isolate sharp boundary-to-center scaling (δ^{-1/2}).
- Corollary `UE-residual-local` and Theorem `tail-inequality` updated to match p=1.
- New Remark `UE-gate` and Lemma `UE-d1-obstruction` added (prevents silent “absorption by η” claims under p=1).
- Tail closure posture changed: removed one-height reduction + η-absorption RH claim; replaced by criterion-first global theorem.

## Batch 2 (Residual envelope δ-uniformity): INTEGRATED (proof-sketch level)
- Residual envelope lemma rewritten to be δ-uniform for all 0<δ≤δ0, with explicit dependency control.
- Added “constant gate” remark explaining what must be proven/cited vs. what the harness records.

## Batch 1: ALREADY PRESENT IN v33 (carried forward)
- K_alloc provenance restored; Bridge 1 hardened; no-proxying remark retained; local count bound present.

## Repro pack (v34): INTEGRATED
- New directory `v34_repro_pack/` and zip `v34_repro_pack.zip`.
- Tail artifact renamed to “tail check” and records UE exponent `p` explicitly.
- Verifier checks regen fidelity and reports strict inequality status without requiring it to be true.

