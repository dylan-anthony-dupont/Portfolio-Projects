# integration_notes_v41 (post‑build)

## Build objective
v41 is a **geometry‑pivot / drift‑prevention** build. The goal is not to “add more machinery”, but to:
1) **lock in** what is now *provably impossible* within the S5′ endpoint class, and  
2) re‑frame the single remaining frontier as an explicit **Geometry Change Requirement** (one boxed open statement).

## Inputs consumed
- `manuscript_v40.tex` (baseline)
- `v41_patch_queue.md` (pre‑build patch list)
- `v41_next_build_plan_diff.md` (pre‑build orientation)
- Batch‑11 responses (used to sanity‑check what is *still allowed*, but no branch‑specific mechanisms were promoted to theorem status in v41).

## What changed in the manuscript (v40 → v41)

### A) Single active open statement re‑framed
- The v40 open box “Missing Lever (ML‑Δa)” was **replaced** by:
  **OPEN (v41): Geometry Change Requirement** (Box `box:geometry-change-v41`).
- This box is now the **only** boxed open frontier claim, by design (anti‑drift posture).

### B) New NO‑GO latch installed (aligned boxes)
- Inserted **Lemma `lem:deltaa-alignedbox-nogo`** directly after the two‑sided endpoint definition:
  it shows, in the toy quartet model, that \(\Phi^{(2s)}_B(a;h)\) cannot be forced on the aligned witness family
  \(B(a,m,\delta)\) at the nominal micro‑step coupling \(h\asymp\delta\asymp \eta a/(\log m)^2\).
- Consequence: any closure route that requires an \(\Omega(1)\) lower bound for \(\Phi^{(2s)}\) on aligned boxes is invalid.
  This is now *explicitly* latching the “stop trying to recover δ^{3/2} / micro‑step forcing on aligned boxes” conclusion.

### C) Hygiene correction
- Corrected the expanded formula for \(\mathcal D_{a,h}\) into the grouped “difference‑of‑differences” form to prevent sign drift.

### D) Scope remark added (avoid over‑blocking)
- Added a scope remark immediately after the Geometry Change Requirement box:
  all NO‑GO latches are **endpoint‑ and witness‑family specific**.
  In particular, the new NO‑GO lemma does *not* rule out:
  - changing the witness family (hinge‑centered, pole‑centered, two‑parameter \((a,v)\) families),
  - changing the coupling \(h=h(\delta)\),
  - or abandoning the ML‑Δa endpoint class entirely.

### E) Archive updated
- Added a short new discarded‑routes entry documenting the aligned‑box ML‑Δa NO‑GO and pointing to the v41 open box.

## Sanity check: NO‑GO latches vs “shooting ourselves in the foot”
v41 explicitly clarifies that we have **not** banned entire categories of approaches—only *specific* endpoint/witness configurations.

- **Still banned (correctly):** “pointwise UE” and “sup UE” endpoint classes that cannot beat the exponent‑budget gate (v36 latches).
- **Newly banned (correctly):** aligned‑box forcing for \(\Phi^{(2s)}\) at nominal coupling (toy quartet NO‑GO).
- **Still allowed (explicitly):** any redesign that changes geometry (witness family) and still couples to S6 (explicit‑formula amplitude leak) for interpretive cross‑checks.

## Current frontier (what remains open)
Everything now reduces to the **Geometry Change Requirement** (Box `box:geometry-change-v41`):
produce a witness family + endpoint functional that is simultaneously:
1) **forceable** (truth‑latching lower bound),  
2) **budget‑eligible** (UE bound passes exponent gate at nominal scale), and  
3) **resonance‑robust** (no “one quartet per height” assumptions).

Batch‑11 suggests several plausible candidate geometries, but v41 intentionally does **not** promote any to a claimed closure mechanism.

## Build outputs (v41)
- `manuscript_v41.tex`
- `manuscript_v41.pdf`
- `v41_patchlog.md`
- `v41_repro_pack.zip` (and extracted folder `v41_repro_pack/`)
- `CR_master_dashboard_v41_locked.md` + updated `CR_master_dashboard.md`
- `v41_next_build_plan_diff.md` (post‑build: updated to point toward geometry candidates)

