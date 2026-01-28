# CR Master Dashboard — v40 (LOCKED)

Lock date: 2026-01-28  
Current manuscript: `manuscript_v40.tex` / `manuscript_v40.pdf`  
Repro pack: `v40_repro_pack.zip`

---

## 0) One-sentence status

v40 permanently **retires** the centered defect endpoint closure route (S5^{def}) and installs **one** active open frontier:

> **Missing Lever = ML‑Δa** (Box `box:missing-lever-v40`): prove forcing/UE/resonance for the two‑sided shift‑difference endpoint Φ^{(2s)}.

---

## 1) The single boxed open statement (the frontier)

### ML‑Δa (v40)
**Box:** `box:missing-lever-v40`

**Endpoint family:**
- Two‑sided shift‑difference operator: `def:two-sided-shift-diff`  
  D_{a,h}(v) := L_{a+h}(v) − L_{a−h}(v)
- Two‑sided phase endpoint: `def:two-sided-endpoint`  
  Φ^{(2s)}_B(a;h) := max_{side I} | Im ∫_I D_{a,h}(v) dv |
- Nominal coupling: h = δ, δ = η a/(log m)^2

**Required closure bullets (all OPEN):**
1) Forcing: Φ^{(2s)} ≥ c0 on an admissible aligned box containing a quartet.
2) UE: Φ^{(2s)} ≤ UE(m,a,δ,h) with δ‑uniform control that **passes the exponent-budget gate**.
3) Resonance robustness: near‑resonant quartets cannot make the endpoint δ‑inert in a way that breaks (2).

---

## 2) Installed truth-latching NO‑GO borders (cannot be violated)

These are now treated as **non-negotiable** in downstream reasoning.

### A. No centered transfer at the same δ
- `lem:ML1-samebox-nogo`  
  **No δ‑uniform transfer** from aligned forcing to Φ^{def} on the centered box at the same δ.

### B. Pointwise → endpoint has a δ¹ ceiling (for Φ^{def})
- `lem:defect-p-ceiling`  
  Any bound derived solely from δ‑uniform pointwise control of |L_a| cannot achieve δ^p with p>1.

### C. Defect-box pole winding cannot “replace” transfer
- `lem:defectbox-nogo-ML1`  
  On a defect box containing the pole, Φ^{def} ≥ π/2 (δ‑independent), so δ‑gain cannot hold uniformly.

### D. Near-resonance can be δ-inert for Φ^{def}
- `lem:defect-resonance-nogo`  
  A second quartet at tilt a−ε ~ a−δ can keep Φ^{def} bounded below even as δ→0.

---

## 3) What is archived (kept only as cautionary context)

- S5^{def} “centered defect endpoint” closure route is **retired** (Appendix `app:discarded`, item D0).
- Any “transfer-to-centered-box” strategy at the same δ is disallowed by `lem:ML1-samebox-nogo`.
- Any attempt to salvage Φ^{def} by claiming δ^p with p>1 is disallowed by `lem:defect-p-ceiling`.

---

## 4) Explicit-formula cross-check (S6 harness)

v40 explicitly records the S6 interpretation:

- off-axis (β = 1/2 + a/2) corresponds to an **x^β amplitude leak** in the explicit formula;
- ML‑Δa is a local **tilt-sensitivity** functional meant to detect (and rule out) such leaks via boundary phase constraints.

(See Appendix `app:S6-harness`.)

---

## 5) v41 tactical plan (minimal, no drift)

### Must-do (in order)
1) **Forcing lemma for Φ^{(2s)}**  
   Show that if a quartet lies in an admissible aligned box, at least one side phase integral of D_{a,h} has |Im| ≥ c0.

2) **UE bound for D_{a,h} at nominal coupling**  
   Derive a δ‑uniform envelope for |E'/E| at the four shifted arguments (v±a±h) that yields a bound on Φ^{(2s)} passing the gate.

3) **Resonance robustness lemma**  
   Prove that extra quartets cannot make (2) fail at the nominal δ; i.e. near-resonant contributions are controlled (δ-aware).

### Must-not-do (guardrails)
- Do not reintroduce centered defect endpoint closure attempts as “primary”.
- Do not loosen the gate calculator / exponent budget.
- Do not reopen v33 absorption narratives (already killed by v36 constraints).

---

## 6) Repro pack status

The v40 repro pack certifies:
- the finite-height front-end certificate, and
- the m=10 tail-check certificate.

It does **not** certify ML‑Δa (still open).

