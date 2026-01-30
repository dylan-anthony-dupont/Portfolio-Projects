# v42 build protocol (post Batch 12)

This protocol is designed to produce a **truth-latching v42** with zero drift: only GEO-C4 is active; only UE-INPUT remains open.

---

## Phase A — Pre-flight (freeze invariants)

1) **Freeze the frame map:** s → u → v and the meaning of (a,m,δ,h).  
2) **Freeze the object:** E(v) is even entire; quartets follow from FE symmetry; no RH assumed.  
3) **Freeze NO-GO archive:** sidewise-max / centered defect endpoints remain archived; they are not used in proofs.

---

## Phase B — Implement Batch-12-locked patches

### B1. GEO-C4 definition block (Q42.2)
- Insert the witness circle C_{m,δ}.
- Define L_t, D_{a,h}.
- Define endpoint Φ* using k=2 projection and normalization δ²/h.
- Fix coupling h=κδ and state nominal δ-policy (abstract).

### B2. Shift-admissibility-by-shrink lemma (Q42.3)
- Insert the δ-shrink admissibility lemma + monotone-safe remark.

### B3. Forcing lemma (Q42.4) + remainder robustness
- Insert the forcing proposition statement.
- Proof: toy-model computation + reduction to k=2 carrier + explicit projection constant.
- Append the LOCAL remainder lemma (or cite it) showing the analytic remainder cannot cancel the forced k=2 channel under isolation.

### B4. Resonance remark (Q42.5)
- Add short remark: energy endpoint prevents cancellation; additional quartets strengthen forcing.

---

## Phase C — Replace the “Missing Lever” box (only open item)

### C1. UE-INPUT box (Q42.6)
Replace any older “UE” claims with a single crisp open statement:
- prove Φ* ≤ o(1) under δ-policy, RH-free.

### C2. Preferred reduction target (ENVELOPE)
Add a short reduction paragraph:
- it suffices to bound ∂_t ∂_v^j L_t along shifted traces (j=0,1,2),
- then use harmonic extraction / integration by parts in θ to gain δ-powers.

No proof is claimed unless the inequality is fully derived.

---

## Phase D — Consistency checks (must pass before calling v42 “locked”)

1) **No circularity audit:** ensure no definition assumes “zeros on the hinge.”  
2) **Quantifier contract audit:** δ-policy and admissibility shrink are uniform and monotone-safe.  
3) **Endpoint normalization audit:** confirm δ²/h normalization is consistent with forcing computation constant.  
4) **Resonance audit:** show that adding zeros cannot reduce the endpoint lower bound (energy channel).  
5) **S6 mapping sanity:** verify a ↔ β mapping and interpret Φ* as local amplitude-leak detector (optional).

---

## Phase E — Output artifacts (when v42 build is executed later)
- manuscript_v42.tex / .pdf
- v42_patchlog.md
- integration_notes_v42.md
- CR_master_dashboard_v42_locked.md
- v42_next_build_plan_diff.md

---

## The only “GO / NO-GO” gate for v42 being proof-grade
- **GO** only if UE-INPUT is proven and explicitly written.
- Otherwise v42 is an honest “truth-latching scaffold” with one boxed open analytic statement.
