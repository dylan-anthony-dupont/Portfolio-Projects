# v41 Next Build Plan (Diff-Only) — v40 → v41

Build target: **v41**  
This plan is intentionally **minimal**: v40 installed a single active frontier (ML‑Δa). v41 must close it or decisively reduce it.

---

## 0) Non-negotiables carried from v40

- Do **not** revive S5^{def} centered defect endpoint closure attempts:
  - `lem:ML1-samebox-nogo` (no centered transfer at same δ),
  - `lem:defect-p-ceiling` (δ¹ ceiling from pointwise bounds),
  - `lem:defect-resonance-nogo` (δ-inert resonance).
- The only active open statement is Box `box:missing-lever-v40` (ML‑Δa).

---

## 1) v41 deliverables (must produce)

### D1. Forcing for Φ^{(2s)} on admissible aligned boxes (NEW, proof-grade)
Produce a lemma that replaces “π/2 forcing for W” with a forcing statement for the two‑sided endpoint:

- If an off-axis quartet exists at height m with tilt a,
- and B = B(±a,m,δ) is a κ-admissible aligned box with nominal δ and h=δ,
- then Φ^{(2s)}_B(a;δ) ≥ c0 for some absolute c0>0.

This should be proven by an argument-principle / pole-count mechanism applied to a meromorphic quotient that directly controls D_{a,h}.

### D2. UE envelope bound for D_{a,h} at nominal coupling (NEW, proof-grade)
Derive a δ-uniform bound for

|E'/E(v ± a ± h)| on the four shifted boundary segments

that yields:

Φ^{(2s)}_B(a;h) ≤ UE(m,a,δ,h)

and explicitly verify:

- UE passes the exponent-budget gate (Theorem `thm:exponent-budget`).

### D3. Resonance robustness lemma (NEW)
Prove a lemma that shows “near-resonant quartets cannot break D2 at nominal δ”, i.e.

- extra quartets at tilts a−ε with ε ~ δ do not create δ‑inert obstruction for Φ^{(2s)}.

The natural proof goal is a cancellation / Lipschitz-in-a effect built into the two-sided difference.

---

## 2) Manuscript patch targets

- In Section `sec:S5-frontier`, upgrade Box `box:missing-lever-v40` by:
  - replacing “OPEN” bullets with completed lemmas,
  - or splitting into (ML‑Δa‑1 forcing) + (ML‑Δa‑2 UE) + (ML‑Δa‑3 resonance).
- If D1–D3 succeed, add a short “PHU closure at height m” paragraph linking:
  (forcing) + (UE) ⇒ contradiction ⇒ a(m)=0.

---

## 3) Optional, strictly controlled fallback (ONLY if D1 fails cleanly)

If Φ^{(2s)} forcing (D1) cannot be proven without hidden RH assumptions, then introduce a clearly-labeled alternative endpoint
candidate (do not merge both into the mainline):

- forceable endpoint directly on E: Φ^E_B := max_I |Im ∫_I E'/E| (argument principle),
- plus a non-pointwise UE bound on ∫|E'/E|.

This fallback must be presented as “Option C2” and must not re-open drift in the mainline.

---

## 4) Repro pack

No new numerical certificates are required unless D2 introduces new explicit constants.
If constants change, bump the repro pack metadata and regenerate SHA256SUMS.

