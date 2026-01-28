# Control Room Master Dashboard (LOCKED) — v41

**Purpose.** This dashboard is the “truth‑latching control panel” for the current manuscript version.
It records what is CLOSED, what is OPEN, and what is explicitly NO‑GO.

---

## Current version
- **Manuscript:** v41 (`manuscript_v41.tex` / `manuscript_v41.pdf`)
- **Single boxed OPEN statement:** Box `box:geometry-change-v41` (Geometry Change Requirement)

---

## What v41 locks in

### 1) NO‑GO latches (hard constraints)

**NG‑BUDGET (v36).** Exponent‑budget gate (Theorem `thm:exponent-budget`) remains binding.  
**NG‑UE‑POINTWISE / NG‑UE‑SUP (v36).** Pointwise or sup‑type UE endpoints cannot close at the nominal scale.  
**NG‑FORCE‑CONST (v36).** Forcing must come from a genuine winding / pole count; no “fake forcing”.

**NG‑Δa‑ALIGNED (v41).** *New latch.*  
Lemma `lem:deltaa-alignedbox-nogo` rules out **aligned‑box micro‑step forcing** for the two‑sided ML‑Δa endpoint
\(\Phi^{(2s)}_B(a;h)\) at \(h\asymp\delta\asymp \eta a/(\log m)^2\) (toy quartet model).

> Translation: **stop** trying to force \(\Phi^{(2s)}\) on the aligned witness family at nominal coupling.

### 2) Hygiene locks
- Completion hygiene: work with entire width‑2 completion \(\Xi_2(u)=\xi(u/2)\) and recenter \(E(v)=\Xi_2(1+v)\).
- FE quartet symmetry only (no RH assumptions).

---

## What remains open (single active frontier)

### OPEN‑GEO (v41)
**Box `box:geometry-change-v41`: Geometry Change Requirement.**

Find a new witness family \(\mathfrak B(a,m)\) and endpoint \(\Phi_{\mathfrak B}(a,m)\) such that for any off‑axis quartet at height \(m\) and tilt \(a>0\):

1) **FORCE:** \(\Phi_{\mathfrak B}\ge c_0\) (argument principle / winding / pole count).  
2) **UE / gate passing:** \(\Phi_{\mathfrak B}\le\) bound that passes the exponent‑budget gate at \(\delta=\eta a/(\log m)^2\).  
3) **Resonance robustness:** remains valid with multiple quartets at the same height.

---

## Candidate geometry directions (recorded, not yet promoted)

These are **allowed** by v41 latches and were repeatedly suggested in Batch‑11 as plausible “geometry change” moves:

- **GEO‑C1 (hinge‑centered):** witness boxes centered at \(v=im\) (hinge) with shift‑aware admissibility and an endpoint that remains forceable.
- **GEO‑C2 (pole‑centered):** witness boxes centered at poles of \(\mathcal Q_a\) (e.g. \(v=2a+im\)) so forcing comes from a pole count.
- **GEO‑C3 (two‑parameter / averaged):** a two‑dimensional endpoint (e.g. averaging over \(h\) or over \((a,v)\)) to bypass per‑pole ceilings.

**Important:** v41 does not claim any of these closes the program; they are just the leading candidates consistent with current locks.

---

## Next build pointer
- **v42 goal:** pick one candidate geometry (or a short shortlist), formalize the witness family and admissibility rules,
  and prove a first “FORCE vs UE” contradiction at the nominal scale *without* violating NG‑BUDGET and *without* assuming “one quartet per height”.

---

## Audit harness
- `v41_repro_pack.zip` (and folder `v41_repro_pack/`) — certificate/verifier harness for finite‑height and low‑anchor checks.

