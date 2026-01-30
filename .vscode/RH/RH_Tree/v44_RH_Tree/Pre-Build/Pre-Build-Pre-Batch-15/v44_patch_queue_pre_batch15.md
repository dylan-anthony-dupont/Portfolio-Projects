# v44 Patch Queue — Pre‑Batch‑15

This queue enumerates **edits we can safely make in v44 without claiming new mathematics**.
All items are documentation/hygiene improvements which make Batch‑15 responses easier to integrate.

## P0 (Documentation): Appendix UE Playbook
**Goal:** one-page attack surface for UE‑INPUT.

**Insert location:** end of manuscript (appendix).  
**Contents:**
1. Exact definitions (E, f, L_t, D_{a,h}, hinge circle, coupling policy, admissibility).
2. Single active UE‑INPUT box.
3. Allowed decompositions (D as finite differences; log-derivative of Q_{a,h}; FTC in t; zero-kernel sum + archimedean term).
4. Candidate routes A–D.

## P1 (Documentation): Weil/Li bridge harness subsection
**Goal:** record a concrete, RH-equivalent criterion and state the precise “Bridge Lemma” target.

**Insert location:** Appendix after UE Playbook.

**Add:**
- Weil criterion statement (RH iff positivity for all test functions).
- Li criterion statement (RH iff Li coefficients nonnegative).
- Bridge target: identify GEO‑C4 k=2 channel functional with a Weil test (or a controlled linear combination) for some explicit family g_{m,a,δ}.
- “Phase-loss caution”: absolute value UE interfaces control magnitudes but may destroy sign information required by Weil negativity witnesses.

## P2 (Hygiene): Explicit quantifier contract for δ-shrink
**Goal:** make “allow smaller δ for buffering” proof-grade.

**Add remark/definition:**
- Fix η, κ.
- δ₀(m,a)=η a/(log(m+3))^2.
- Actual δ is any 0<δ≤δ₀ such that all shift traces avoid zeros by buf·δ.
- All claims must quantify over this δ choice explicitly (no hidden monotonicity).

## P3 (Optional, only if Batch‑15 supports): Signed k=2 interface box
Do **not** activate before Batch‑15.

Candidate (inactive) box:
\[
\Big|\int_0^{2\pi}\mathcal D_{a,h}(v(\theta))\,e^{-2i\theta}\,d\theta\Big|\le C\,h\,\frac{(\log(m+3))^{C'}}{a^2}.
\]

This would preserve phase and is bridge-compatible.
