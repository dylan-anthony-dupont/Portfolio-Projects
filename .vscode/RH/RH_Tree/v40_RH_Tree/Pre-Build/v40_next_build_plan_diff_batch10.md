# v40 next build plan (diff-only) — from v39 + Batch 10 + legacy synthesis

**Date:** 2026-01-28  
**Scope:** This is a *surgical* plan. v40 must reduce frontier ambiguity by (i) latching NO‑GO borders, and (ii) replacing the v39 Missing Lever triad (ML‑1/ML‑2/ML‑3) with a single redesigned endpoint obligation (ML‑Δa).

---

## A) Truth-latching inserts (NO‑GO borders)

1. **Insert NG‑1 lemma:** “No centered/same‑box transfer to \(B(0,m,\delta)\)”  
   - Source: RH‑BRIDGE code block (label suggestion `lem:ML1-samebox-nogo`).
2. **Insert NG‑2 lemma:** “Side-length ceiling: defect endpoint cannot yield \(p>1\) from pointwise UE”  
   - Source: RH‑ENVELOPE code block (label suggestion `lem:defect-p-ceiling`).
3. **Insert NG‑4 lemma:** “Defect-box pole-winding cannot replace transfer”  
   - Source: RH‑FORCE code block (label suggestion `lem:defectbox-nogo-ML1`).
4. **Latch δ-awareness requirement:** add RH‑LOCAL remarks/definitions that \(\mathcal R_a(m)\) is δ‑blind and must be replaced by δ‑aware counts/sums.

---

## B) Replace the boxed open statement (Missing Lever box)

**Replace** `box:missing-lever-v39` with a v40 box containing:

- **(ML‑Δa)** Two‑sided shift‑difference endpoint closure:
  - Define \( \mathcal D_{a,h}(v):=\mathcal L_{a+h}(v)-\mathcal L_{a-h}(v)\).
  - Define \( \Phi^{(2s)}_B(a;h)=\max_I\left|\Im\int_I \mathcal D_{a,h}\,dv\right|\).
  - Nominal coupling: \(h=\delta=\eta a/\log^2 m\).
  - Required: forcing lower bound \(c_0>0\), UE upper bound that passes the Gate Calculator, resonance robustness.

**Demote** the former ML‑1/ML‑2/ML‑3 triad to “discarded / known-failing” (appendix or NO‑GO list).

---

## C) New definitions + toy-model subsection (S5Δa)

1. **Add definition:** two‑sided shift‑difference operator \( \mathcal D_{a,h}\).  
2. **Add definition:** endpoint \( \Phi^{(2s)}_B(a;h)\) (max over sides; buffered contour).
3. **Add toy model block** (motivating computations):
   - single quartet cancellation for \(\Phi^{\rm def}\) on centered box is \(O(\delta/a)\) (already in v39),
   - two‑sided shift difference breaks cancellation (lower bound \(\Omega(1)\), arctan geometry),
   - near‑resonant quartet contributions are “finite-difference suppressed” (target statement; still OPEN).

---

## D) Gate Calculator integration (language hygiene)

- Keep Theorem `thm:exponent-budget` as the global closure constraint.  
- Add a short “Gate Calculator” remark table translating:
  - endpoint’s \(\delta\)-scaling exponent \(p_{\rm eff}\),
  - resonance exponent \( \theta_{\rm eff}\) (how resonance counts scale in \(\delta\)),
  - and the pass condition \(p_{\rm eff}-\theta_{\rm eff}\ge 1/2\) (or whatever form used in the text).

This replaces informal “\(p>1\)” phrasing.

---

## E) S6 harness upgrade (explicit formula cross-check)

- Extend the S6 subsection to interpret \(\mathcal D_{a,h}\) as a finite-difference in \(\beta=\tfrac12+\tfrac a2\):
  - “tilt derivative” \(a\mapsto\beta\) corresponds to sensitivity to \(x^\beta\) amplitude leak,
  - therefore a successful ML‑Δa closure is an “amplitude‑leak forbiddance” statement.

---

## F) Editorial truth-latching (drift prevention)

- Add an explicit “Do not attempt” checklist near the S5 frontier:
  1. no centered transfer (NG‑1),
  2. no p>1 recovery via pointwise UE for \(\Phi^{\rm def}\) (NG‑2),
  3. do not use δ‑blind resonance proxy (NG‑3),
  4. do not use defect pole-winding forcing as substitute (NG‑4),
  5. do not use \(\Phi^E_B\) endpoint on \(E'/E\) without a new local mechanism (NG‑5).

---

## v40 outcome target (non-claim)

v40 should make it **obvious** to a referee that:
- v39’s S5^def path is genuinely boxed-in by hard NO‑GO latches, and
- the only remaining boxed analytic gap is **ML‑Δa** for the redesigned endpoint.

