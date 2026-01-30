# v42 patch queue (post Batch 12)

This is the **paste-ready** queue to build v42 from v41, updated after Batch 12.

---

## Q42.1 — Freeze posture + NO-GO archive
**Action:** Keep v41’s NO-GO / discarded endpoint routes, but mark them as **archived** (non-load-bearing).  
**Insert:** One paragraph at the start of the GEO section: “Only GEO-C4 endpoint remains active.”

---

## Q42.2 — GEO-C4 definition block (PROMOTE)
**Insert (definitions):**
1. Witness circle: `C_{m,δ}: v(θ)=im+δ e^{iθ}`.
2. Field: `L_t(v) = (E'/E)(v+t) - (E'/E)(v-t)`, `D_{a,h}(v) = L_{a+h}(v) - L_{a-h}(v)`.
3. Endpoint (k=2 harmonic projection):
   - `ψ(θ)=Im(D_{a,h}(v(θ)))`
   - `Φ*(m,a,δ,h)=(δ²/h)·||P_2 ψ||_{L²}` where `P_2` projects onto span{cos(2θ), sin(2θ)}.
4. Coupling: `h=κδ`, fixed κ∈(0,1/2] (or any fixed κ∈(0,1) away from collision).
5. Nominal δ-policy (kept abstract in v42): `δ=η a/log² m` (or comparable).

---

## Q42.3 — Shift-admissibility-by-shrink (CLOSED)
**Insert (lemma):**
> If any shifted trace `C_{m,δ} ± (a ± h)` intersects a zero of E, shrink δ ← δ/2 (and recompute h=κδ). Repeat.  
> Since zeros are discrete, this terminates, producing an admissible witness.  
> UE bounds are monotone-improving in δ, and forcing is scale-invariant once κ is fixed.

(Include a short “monotone-safe” remark referencing the δ-policy contract.)

---

## Q42.4 — Forcing lemma in the harmonic channel (CLOSED once LOCAL is adopted)
**Insert (proposition):**
> Under an off-axis quartet at height m and admissible witness, the k=2 harmonic endpoint satisfies `Φ* ≥ c₀(κ)>0`.

**Proof skeleton (paste-ready):**
1. Local pole model: E'/E has simple poles at zeros; D_{a,h} creates a dipole term near v=im.
2. On the hinge circle, the singular forced part equals `(-4h)/(u²-h²)` in the toy model (u=v-im).
3. Its imaginary part is exactly a k=2 carrier; compute the k=2 projection to get a constant ≍ 1 after normalization δ²/h (explicit constant from toy model).
4. LOCAL remainder lemma: analytic remainder contributes o(1) to the k=2 channel when δ is small relative to separation from other zeros; hence cannot cancel forced channel.

---

## Q42.5 — Resonance robustness (CLOSED on forcing side)
**Insert (remark/lemma):**
- Energy endpoint prevents sign cancellation.
- Extra quartets either add k=2 energy or are suppressed by orthogonality; remainder bounds keep the forced energy visible.

(Reference LOCAL’s “arc mass / N_eff control” as supporting lemma.)

---

## Q42.6 — UE-INPUT (ONLY OPEN STATEMENT)
**Replace the old open box with:**

> **UE-INPUT (Open):** Prove an RH-free inequality bounding the k=2 harmonic endpoint:
> `Φ*(m,a,δ,h) ≤ UE(m,a,δ)` with `UE(m,a,δ)=o(1)` under the nominal δ-policy, uniformly for admissible witnesses.

**Preferred reduction (from ENVELOPE):**
- Reduce to explicit bounds on `∂_t ∂_v^j L_t(v)` for j=0,1,2 along the shifted traces.
- Use harmonic extraction (integration by parts in θ) to gain δ-powers and close the exponent budget.

---

## Q42.7 — S6 harness mapping (optional but recommended)
**Insert:** One paragraph stating:
- off-axis tilt a corresponds to β=1/2+a/2 in the s-frame;
- the harmonic endpoint is a local “amplitude leak detector” (forbids x^β contributions via forced local phase energy vs UE bound).

---

## Q42.8 — Proof-spine tightening
**Action:** Ensure the PHU / “a(m)=0” implication is stated only after the GEO-C4 contradiction is complete, so no circular collapse assumptions appear earlier.

---

## Q42.9 — Editorial
- Add a small diagram of the hinge circle and shifted traces.
- Add a table of the GEO-C1..C4 requirements and which are closed/open.

---

### Patch packet dependencies
- Q42.4 depends on adopting LOCAL remainder lemma.
- Q42.6 is the single remaining analytic frontier.
