# Integration Notes — v41 PRE-BUILD (v40 locked → geometry pivot)

Date: 2026-01-28  
Base: `manuscript_v40.tex` (locked) + `v40_next_build_plan_diff.md` + post‑v40 audit proving ML‑Δa(Forcing) is false on aligned boxes.

## 0) Executive: what changed since v40 locked

v40 installed a single active open statement (Box `box:missing-lever-v40`, ML‑Δa). A line‑by‑line audit now shows:

> **ML‑Δa(1) Forcing is false as stated** when the witness family is restricted to **aligned boxes** `B(±a,m,δ)` and nominal coupling `h=δ`.

Therefore v41 must be a **geometry‑pivot prebuild**:

1. **Lock** the new NO‑GO lemma (“Aligned‑box Δa forcing NO‑GO”).
2. **Sanity‑check** existing v40 NO‑GO latches for scope correctness.
3. **Replace** the ML‑Δa box with an explicit **Geometry Change Requirement** box (GEO), giving criteria for any viable closure lever.

This is not drift; it is convergence: we removed a false target and reduced the search space.

---

## 1) New proof-grade finding (must be inserted in v41)

### NG‑Δa‑A (Aligned‑box forcing NO‑GO)

Let `E(v)` be even and entire (as in v40). Define

- `L_t(v) := (E'/E)(v+t) − (E'/E)(v−t)`
- `D_{a,h}(v) := L_{a+h}(v) − L_{a−h}(v)`
- endpoint `Φ_B^{(2s)}(a;h) := max_{I⊂∂B_{κ/2}} | Im ∫_I D_{a,h}(v) dv |`.

**Claim (NO‑GO):** For aligned boxes `B(a,m,δ)` with `δ,h ≤ a/4`, in the toy even-quartet model

`E0(v)=((v−a)^2+m^2)((v+a)^2+m^2)`

one has the uniform bound

`Φ_{B(a,m,δ)}^{(2s)}(a;h) ≤ C · δ h / a^2`.

In particular at nominal coupling `h=δ=η a/(log m)^2` the endpoint is `O((log m)^{-4}) → 0`, contradicting the v40 ML‑Δa forcing requirement of an absolute lower bound `c0>0`.

**Interpretation:** On aligned boxes, the shift evaluations `v±(a±h)` stay a distance `≈a` away from the quartet points `±a±im`, so no topological/near‑pole forcing can occur.

**Immediate consequence:** v41 must remove/repair the forcing bullet in `box:missing-lever-v40`.

---

## 2) Sanity check of v40 NO‑GO latches (scope audit)

The goal is to ensure we are not “shooting ourselves in the foot” by overblocking.

### (i) `lem:ML1-samebox-nogo` (centered transfer)
**Correct scope:** blocks only **transfer** of aligned forcing to the **centered defect endpoint** at the *same* δ.  
**Does NOT block:** using centered/hinge boxes for a *new* endpoint that is forced directly (no transfer).

### (ii) `lem:defect-p-ceiling` (δ¹ ceiling)
**Correct scope:** applies to pointwise UE derived from δ‑uniform pointwise control of `|L_a|` (or similar) on a contour of length `~δ`.  
**Does NOT block:** non‑pointwise endpoints that introduce an extra small factor (e.g., an `a`‑difference / smoothing / 2D averaging) before applying triangle inequality.

### (iii) `lem:defect-resonance-nogo`
**Correct scope:** warns that **δ‑inert resonance** exists for pointwise‑in‑a endpoints built from `Q_a`/`L_a`.  
**Does NOT block:** δ‑aware resonance objects or endpoints where near‑resonant quartets cancel by design.

### (iv) `lem:defectbox-nogo-ML1` (pole-box forcing)
**Correct scope:** “pole winding is δ‑inert, therefore cannot yield δ‑gain UE contradictions.”  
**Does NOT block:** using pole‑box forcing as a **harness/diagnostic** or as one side of a larger 2D mechanism where the gain comes from the other dimension.

### (v) `lem:phase-UE-theta0-nogo`
**Correct scope:** forbids δ‑gain inequalities of the form `Db(W) ≤ C δ^p Φ(E'/E)` when `Φ` has per‑pole θ=0 behavior.  
**Does NOT block:** endpoint classes whose per‑pole response scales with an extra small parameter (e.g. a finite‑difference in `a` that contributes a factor `h`).

### (vi) Legacy “Φ^E_B on E'/E” endpoint
**Sanity outcome:** still NO‑GO as a *δ‑shrinking closure lever* on contours enclosing a zero, because the per‑pole contribution to `∫|E'/E|` is scale‑invariant (δ‑inert).  
However: v41 should clarify that it may remain useful as a **forcing certificate** and as an expository bridge to the argument principle; it is not a closure endpoint.

---

## 3) Cross-version convergence check (v38 → v39 → v40 → v41)

- **v38:** “Missing Lever” framed as repairing pointwise UE / local window / resonance for a phase endpoint.  
- **v39:** defect primitives (`Q_a`, `L_a`) made explicit; δ‑inert resonance is latched as a true obstruction.
- **v40:** drift was closed by retiring S5^def; active frontier became ML‑Δa.
- **v41 (prebuild):** ML‑Δa forcing bullet is shown false on aligned boxes, yielding a clean pivot: **the frontier is now a geometry/coupling redesign**, not an exponent chase.

This is monotone convergence: every pivot is justified by an explicit NO‑GO, not aesthetic preference.

---

## 4) The v41 “Geometry Change Requirement” (what we must lock in)

### GEO (single active frontier after v41)
A viable closure lever must specify:

1. **A witness family** of admissible contours/boxes `\mathfrak B(m,a,δ,…)`.
2. **An endpoint functional** `Φ^*(m,a,δ,…)` built from `E` (or controlled factors) that is:
   - **Forceable** from an off-axis quartet (gives an absolute lower bound independent of δ),
   - **UE‑controllable** with a bound that passes the exponent-budget gate under the nominal δ‑policy (or a revised, explicitly stated policy),
   - **Resonance‑robust** (either monotone-safe or cancellation-safe under near-resonant quartets).
3. **A coupling policy** specifying how δ and the auxiliary non‑pointwise parameter(s) scale (e.g. `h=h(δ)`), with explicit κ‑admissibility conditions.

**What we have proved:** the specific combination

`(witness family = aligned boxes B(±a,m,δ), endpoint = Φ^{(2s)}(a;h), coupling h=δ)`

fails forcing (NG‑Δa‑A). So the witness family and/or coupling must change.

### Candidate geometry directions (non-committal; for batch 11)
- **GEO‑C1:** Centered/hinge box `B(0,m,δ)` with a max‑over‑sides endpoint for `D_{a,h}` (requires careful κ‑buffering so shifted evaluations do not land on zeros).
- **GEO‑C2:** Decouple `h` from δ (e.g. `h=δ^α`, `α>1`) to trade forcing vs UE size.
- **GEO‑C3:** 2D “(a,v) rectangle” mechanism: treat `a` as an orthogonal axis (echoing your 2D→3D input-space transfiguration) and design an endpoint as a flux/averaged winding over an `(a,v)` region so that gain comes from the extra dimension.

---

## 5) v41 prebuild deliverables (what the next artifact pack will implement)

- Insert lemma NG‑Δa‑A (aligned-box forcing NO‑GO) + proof.
- Fix the sign/expansion typo in the definition of `D_{a,h}` if present.
- Replace Box `box:missing-lever-v40` with a new Box `box:geometry-change-v41` stating GEO requirements and explicitly recording NG‑Δa‑A.
- Add a short “NO‑GO scope remark” so no old latch is misread as blocking geometry/coupling redesign.

