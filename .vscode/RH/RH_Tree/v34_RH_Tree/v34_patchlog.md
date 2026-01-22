# v34 patchlog (relative to v33)

Date: 2026-01-22

This patchlog records *substantive* edits from v33 → v34. The guiding principle of v34 is **audit honesty** after the Batch 3 UE–Gate audit.

## A. Upper-envelope / UE–Gate corrections (Batch 3)

1. **Corrected UE exponent (critical fix).**
   - Lemma `upper-envelope` now yields a **δ¹** prefactor (not δ^{3/2}) against `sup_{∂B}|E'/E|`.
   - The proof’s four scaling steps already multiply to δ¹; v33’s δ^{3/2} was an arithmetic mismatch.

2. **Added a sharp boundary-to-center evaluation lemma.**
   - New Lemma `eval-L2` formalizes the Poisson-kernel scaling `||P_B||_{L^2} ~ δ^{-1/2}` and notes sharpness.

3. **Propagated corrected exponent to the residual+local corollary and the tail inequality.**
   - Corollary `UE-residual-local` now reads:
     `sum |W(v±)-e^{iφ±}| ≤ 2 C_up ( δ L(m) + N_loc(m)/κ )`.
   - Theorem `tail-inequality` LHS is updated consistently.

4. **UE–Gate diagnostics + obstruction to η-absorption.**
   - New Remark `UE-gate` isolates the local-term scaling `δ^{p-1} N_loc/κ` under a hypothetical UE exponent `p`.
   - New Lemma `UE-d1-obstruction` records the key fact: with the proved pointwise `p=1`, the local term is **δ-inert**, so η-shrinking cannot suppress it.

## B. Tail closure posture change (Batch 3)

5. **Removed v33’s one-height tail closure and unconditional RH claim.**
   - The monotonic-in-m reduction and the “tail closure from one-height check” theorem depended on the (unproved) stronger UE exponent.
   - v34 replaces these with:
     - Remark `no-one-height` (explaining why reduction fails under pointwise `p=1`);
     - A criterion-first global theorem (`thm:global`) that states RH follows from **front-end + tail criterion family**.

6. **Reintroduced η-absorption only as conditional.**
   - New Proposition `eta-absorption-conditional` shows: *if* a strengthened UE exponent `p>1` is obtained, then at a fixed anchor height the inequality can be satisfied for sufficiently small η.
   - A “uniformity caveat” remark flags that m-uniform closure still needs additional work.

## C. Residual envelope lemma upgrade (Batch 2 carried into v34)

7. **Residual envelope bound made δ-uniform (proof sketch with explicit dependencies).**
   - Lemma `residual-envelope` is rewritten to be uniform for all `0<δ≤δ0`.
   - Proof sketch explicitly reduces the bound to:
     - a standard RH-free local-zero decomposition for `ζ'/ζ` (imported as (⋆)),
     - Stirling-type control of `Γ'/Γ`,
     - and the manuscript’s explicit local-window count majorant.

8. **Added “constant gate” remark and updated certificate provenance note.**
   - Clarifies what is assumed/certified vs. what must be proven or cited.

## D. Repro pack (v34)

9. **Repro pack renamed/updated and UE exponent recorded.**
   - New pack: `v34_repro_pack.zip` with directory `v34_repro_pack/`.
   - `v34_constants_m10.json` now contains `UE_exponent_p`.

10. **Tail artifact is now a “tail check” (audit harness), not a proof certificate.**
   - The generator/verifier now support `p="1"` (proved) and `p="3/2"` (hypothetical).
   - Under `p=1`, the low-anchor check reports `"pass": false` (expected); the verifier still succeeds by checking regeneration fidelity.

## E. Front matter / editorial

11. **Title + abstract + Executive Proof Status updated** to reflect criterion-first posture and UE–Gate status.

---

If you need a machine-readable diff, the next build plan should treat the UE–Gate as the primary frontier: either obtain an effective exponent `p>1` against the *local* term, or redesign the envelope/local-window interface to avoid the collar blow-up.
