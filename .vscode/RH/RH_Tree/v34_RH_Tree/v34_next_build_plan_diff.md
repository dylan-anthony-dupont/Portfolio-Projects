# v34 → v35 next build plan (diff-only)

This is a *diff-only* forward plan from the v34 locked baseline.

## 1) Clear the UE–Gate (primary analytic frontier)
Goal: replace the pointwise UE endpoint (p=1) with a mechanism that yields **effective p>1 against the local term**,
or redesign the envelope/local-window interface so the collar penalty does not appear as `N_loc/(κδ)` in the same way.

Concrete candidate directions:
- **L2/energy envelope**: replace the pointwise `sup_{∂B}|E'/E|` endpoint by an `L^2(∂B)` (or Carleson measure) control and
  pair it with the sharp evaluation lemma (`δ^{-1/2}`) to extract additional δ-power.
- **Avoid the collar blow-up**: local term currently enters as `sup |Z_loc'/Z_loc| ≤ N_loc/(κδ)`. Seek a *boundary integral*
  estimate that yields `δ^{-1+ε}` or a bound involving a smaller moment of the local counting measure.
- **Re-tune δ0 scaling**: if `p` is improved but still <3/2, consider changing the nominal `δ0(m,α)` scaling to keep the local term
  m-uniform (tradeoff with other steps must be checked).

Deliverable: a revised upper-envelope lemma with explicit exponent `p` and a proof that the *local contribution* decays with δ.

## 2) Make the residual envelope lemma referee-grade
- Replace imported bound (⋆) with a fully internal proof or a hard citation (Titchmarsh/Ivić + exact statement).
- Ensure constants are explicitly tracked and uniform for all `0<δ≤δ0`.

## 3) Reintroduce a uniform tail closure (only after UE–Gate cleared)
- If an m-reduction is possible (monotonic band, verified band, or new inequality), re-add a “tail closure theorem”.
- Otherwise, specify an explicit computational band strategy and its required inputs (without claiming unconditional proof).

## 4) Hygiene
- Quantifier audit: ensure every “for all m” / “for all δ” statement is explicit and matches lemmas.
- Cross-reference pass; remove legacy mentions of v33 tail closure.

