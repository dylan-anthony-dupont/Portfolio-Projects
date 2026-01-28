# CR Master Dashboard — v41 PRE‑BUILD (post‑v40 audit)

Date: 2026‑01‑28 (Europe/London)  
Locked base: v40 (`manuscript_v40.tex/pdf`)  
This dashboard is the **single page** Control‑Room view: statuses + blocker queue + minimal DAG.

---

## 1) Canonical posture (truth‑latched)

- **Primary spine:** S5 (post‑v40) = *single‑frontier* program.
- **Active frontier (v41):** **GEO‑pivot** (geometry / coupling redesign) after proving ML‑Δa forcing on aligned boxes is NO‑GO.
- **Goal:** keep builds getting **easier** by maintaining one boxed OPEN statement and one boxed NO‑GO boundary.

---

## 2) Status board (OPEN / IN‑PROGRESS / CLOSED)

### Core latches (CLOSED)
- NG‑1: `lem:ML1-samebox-nogo` (no δ‑uniform transfer to centered defect endpoint at same δ).  
- NG‑2: `lem:defect-p-ceiling` (side‑length ceiling for pointwise defect UE).  
- NG‑3: `lem:defectbox-nogo-ML1` (defect‑box pole winding is δ‑inert; cannot serve δ‑gain closure).  
- NG‑4: `lem:defect-resonance-nogo` (δ‑inert resonance counterexample exists for pointwise defect endpoint).  
- NG‑5: `lem:phase-UE-theta0-nogo` (per‑pole θ=0 blocks any δ^p gain in phase‑class inequalities).

### New latch (must be installed in v41)
- **NG‑Δa‑A (NEW, to add in v41):** aligned‑box forcing for `Φ^{(2s)}(a;h)` is NO‑GO at nominal coupling.

### Single boxed OPEN target (v41)
- **OPEN‑GEO:** find a **geometry/coupling** (box family + endpoint + coupling of parameters) that achieves:
  1) **Forceability** from an off‑axis quartet,
  2) **UE bound** that **passes the Gate Calculator**, and
  3) **Resonance robustness** (no δ‑inert obstruction in the chosen endpoint class).

---

## 3) Blocker queue (ranked)

1. **GEO‑1 (definition‑level):** specify the new witness family `𝔅(a,m,δ,h)` (not restricted to aligned boxes) and the endpoint class precisely.
2. **GEO‑2 (forcing):** prove a lower bound `Φ_{B}^{new} ≥ c0` from a single quartet for some `B∈𝔅`.
3. **GEO‑3 (UE):** prove `Φ_{B}^{new} ≤ UE(m,a,δ,h)` with δ‑uniform constants and show the Gate Calculator passes.
4. **GEO‑4 (resonance):** show near‑resonant quartets cannot make the endpoint δ‑inert in a way that breaks GEO‑3.

---

## 4) Minimal dependency DAG (S5 after v40)

`off‑axis quartet (a>0 at height m)`
 → choose witness geometry `B∈𝔅(a,m,δ,h)`
 → **FORCE:** `Φ_B^{new} ≥ c0` (truth‑latching)
 → **UE:** `Φ_B^{new} ≤ UE(m,a,δ,h)` (boundary envelope)
 → Gate Calculator: `UE < c0` at nominal scale (or small‑η / large‑m)
 → contradiction ⇒ `a(m)=0` (PHU at height m)
 → for all m ⇒ RH.

**Key pivot:** v40 assumed `𝔅 = {aligned boxes B(±a,m,δ)}` for `Φ^{(2s)}` forcing. Audit shows this is impossible (NG‑Δa‑A), hence **𝔅 must change**.

---

## 5) Sanity check reminders (scope of NO‑GO latches)

- NG‑1 is **about transfer** to centered defect endpoints, not a ban on using centered boxes for other endpoints.
- NG‑3 bans defect‑box pole winding as a **δ‑gain closure** route; it may remain a harness/diagnostic.
- NG‑5 forbids δ^p gain when the UE inequality reduces to “bounded per pole”; it does **not** forbid endpoints that incorporate additional cancellation/derivative structure.

---

## 6) v41 build intent (pre‑build contract)

v41 must be a **truth‑latching geometry pivot build**:
- insert NG‑Δa‑A as a numbered lemma,
- replace Box `box:missing-lever-v40` with Box `box:geometry-change-v41` defining OPEN‑GEO,
- tighten the scope statements on existing NO‑GO lemmas to prevent accidental over‑blocking.

(After v41 is locked, Batch‑11 prompts will be designed to attack OPEN‑GEO directly.)
