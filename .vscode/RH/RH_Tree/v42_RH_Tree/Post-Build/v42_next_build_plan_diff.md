# v42 next build plan — diff-only update (post Batch 12)

This diff updates the **v42 pre-build plan** in light of Batch 12.

---

## ✅ Items now considered CLOSED (upgrade from pre-batch plan)

### (A) Forcing robustness (Q42.6)
**Was:** Open: forcing constant might cancel / require strict assumptions.  
**Now:** **Closed** once we adopt:
- a k=2 harmonic endpoint on the hinge circle, and
- LOCAL’s pair isolation + remainder-energy lemma ensuring the forced k=2 channel cannot be erased by analytic remainder terms.

### (B) Shift-admissibility (Q42.7)
**Was:** Open: need δ-shrink lemma ensuring admissibility without breaking scaling.  
**Now:** **Closed** via LOCAL + ABSORB monotone-shrink contract:
- If a shifted trace hits a zero, shrink δ by a fixed factor until admissible.
- This is monotone-safe for UE (smaller δ makes UE easier), while forcing is δ-independent once coupling is fixed.

### (C) Resonance (Q42.8) — lower-bound side
**Was:** Open: near-resonant quartets could neutralize endpoints.  
**Now:** **Closed** on the forcing side:
- Energy endpoint + k=2 projection is cancellation-safe.
- Additional quartets tend to add energy; remainder bounds prevent hiding.

---

## ❗ Single remaining open item (must be the only frontier)

### (D) UE-INPUT (Q42.5) — harmonic channel bound
**Still OPEN.**  
Batch 12 clarifies the right framing:

- UE must be proved for the **projection endpoint**, not via any global sup-norm of |E'/E|.
- The analytic brick can be reduced to a bound on v- and t-derivatives of L_t (ENVELOPE reduction), then turned into an o(1) endpoint via integration-by-parts in θ (harmonic extraction gain).

**New canonical UE target (replace vague UE wording):**
Prove explicit bounds for `∂_t ∂_v^j L_t(v)` on the shifted hinge-circle traces for j=0,1,2 (or an equivalent Hardy/Hilbert transform bound), strong enough to yield:
`Φ*(m,a,δ,h) ≤ C·(δ/a)^p (log m)^C` with p>0 large enough that δ=η a/log²m gives o(1).

---

## Manuscript integration priorities for v42 build

1) Promote GEO-C4 definitions (circle witness, D_{a,h}, k=2 endpoint Φ*).  
2) Insert forcing lemma as “CLOSED” (cite toy-model computation + remainder control).  
3) Insert admissibility-by-shrink lemma (CLOSED).  
4) Replace the “Missing Lever” box with the single UE-INPUT statement in harmonic/projection form.  
5) Move all earlier defect endpoints into NO-GO appendix (already earned), to prevent drift.

---

## Next-batch prompt scope (if needed)

Batch 13 must target only UE-INPUT. Everything else is frozen.
