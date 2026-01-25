# Integration Notes — v36 (post-build)

**Canonical posture (unchanged, clarified):**
- Primary spine is now **S5 (non-pointwise UE redesign)** as the *frontier*, not an “attempt to recover δ^{3/2}”.
- S2 remains an audit harness, but does not supply analytic closure.

## What v36 accomplished
1. **No-drift S5 acceptance gates are now in-text**:
   - every future endpoint proposal must declare `(p, θ, q)` and satisfy the S5 Budget Theorem (Theorem `thm:S5-budget`).
2. **Two broad endpoint classes are formally closed (NO–GO)**:
   - absolute `L^r(∂B)` norms of `E'/E` (incl. `L^2`) are δ-inert under the current collar split (Prop. `prop:S5_Lp_nogo`);
   - projection endpoints that annihilate the local kernel span cannot control the forced dial deviation without a new forcing link (Lemma `lem:S5-projection-nogo`).
3. **Forceability is now an explicit hard gate**:
   - if an endpoint does not dominate `D_B(W)`, it must be accompanied by a new forcing lemma (Remark `rem:s5-forceability-gate`).
4. **Repro pack now fails closed on metadata** (G-12 hygiene):
   - missing endpoint/exponent/forceability fields ⇒ certificate invalid.

## What v36 did NOT do (by design)
- It does **not** add any new analytic closure.
- It does **not** claim RH or any strengthened UE exponent.
- It does **not** change the local window bound; it only records its endpoint scaling cleanly.

## Updated frontier (what must be invented)
The only viable remaining route is an S5 endpoint that:
- **keeps forceability** (dominates `D_B(W)` or gets its own forcing lemma),
- **beats δ-inertness** (achieves `p−θ>0` with `2(p−θ)≥q`),
- and does **not** fall into the now-closed D5/D6 endpoint classes.

This strongly suggests the endpoint must involve **cancellation / signed structure** (argument-principle–type or Hilbert-transform–type objects) or a genuinely new boundary object (e.g. BMO / Carleson control of `log|E|`, not absolute norms of `E'/E`).

## Next work-order (v36 → v37 pre-build)
- Identify candidate S5 endpoints outside D5/D6:
  1. signed/oscillatory endpoints compatible with `D_B(W)` and forcing;
  2. endpoints based on `log|E|` / harmonic measure / BMO that can plausibly give `p>θ`.
- Any candidate must ship with a **Patch Packet** including:
  - precise endpoint definition + scaling under affine rescaling,
  - proof sketch of UE inequality + local term estimate in the same endpoint,
  - explicit declaration of `(p, θ, q)` and forceability mode.

