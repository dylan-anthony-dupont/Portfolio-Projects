# v41 → v42 next build plan diff (post‑v41)

v41 is a **geometry‑pivot** build. It installs an explicit NO‑GO latch ruling out the v40 aligned‑box ML‑Δa forcing configuration,
and reframes the single frontier as: **Geometry Change Requirement** (Box `box:geometry-change-v41`).

This diff lists the minimal deltas required for v42 to be a meaningful “closure attempt” (as opposed to more bookkeeping).

---

## 0) Non‑negotiable constraints to keep (do not regress)
- Keep v36 exponent‑budget gate (Theorem `thm:exponent-budget`) as the primary budget filter.
- Keep v41 NO‑GO latch `lem:deltaa-alignedbox-nogo` (do not try to re‑enable aligned‑box micro‑step forcing by rhetoric).
- Keep strict “no RH assumptions” posture; only FE quartet symmetry is allowed.

---

## 1) Choose a geometry candidate (one of three) and formalize it

### Option GEO‑C2 (pole‑centered, pair isolation) — *Batch‑11 FORC/BRDG consensus*
**Witness family:**
- Define boxes centered at the relevant poles/zeros of the defect quotient \(\mathcal Q_a(v)=E(v+a)/E(v-a)\),
  e.g. \(B^{\mathrm{pole}}(a,m,\delta)\) around \(v=2a+im\) (and symmetric mates).
**Endpoint:**
- Use a forceable phase/winding endpoint on \(\mathcal Q_a\) or \(\log\mathcal Q_a\) along \(\partial B^{\mathrm{pole}}\):
  \(\widetilde D_{B^{\mathrm{pole}}}(\mathcal Q_a) := \max_I |\Im \int_I (\mathcal Q_a'/\mathcal Q_a)\,dv|\).
**Target lemmas:**
1. FORCE: pole/zero count gives \(\ge \pi/2\) on at least one side.
2. UE: bound \(\int_I |\mathcal Q_a'/\mathcal Q_a|\) using shifted admissibility + existing Gamma/\(\zeta'/\zeta\) envelopes.
3. Resonance: show additional quartets cannot destroy forcing (they may add poles/zeros; forcing survives).

### Option GEO‑C1 (hinge‑centered with shift‑aware admissibility) — *LOCAL direction*
**Witness family:**
- Boxes centered at \(v=im\) (hinge), but admissibility is defined **after shifts** \(v\mapsto v\pm(a\pm h)\)
  so that the endpoint “sees” the correct poles/zeros.
**Endpoint:**
- Either keep \(\Phi^{(2s)}\) but on a *new* witness family, or use a hinge‑anchored endpoint \(\widetilde D_{B_0}(E)\).
**Key extra obligation:**
- Formalize an “effective local count” \(N_{\mathrm{eff}}=O(1)\) on the witness family (pair isolation).

### Option GEO‑C3 (two‑parameter / averaged endpoint) — *ENVEL direction*
**Witness family + endpoint:**
- Define a 2D endpoint that averages over the shift parameter (or over a small \((a,v)\) rectangle),
  so that near‑resonant contributions cannot stay δ‑inert while the averaged UE bound shrinks.
**Key risk:**
- Must remain compatible with v36 exponent budget (avoid introducing an averaged endpoint that costs too much).

---

## 2) Add a “shifted admissibility” definition (needed for any non‑aligned geometry)
Add a definition along the lines of:

- A box \(B\) is **(a,h)-shift admissible** if \(E(v\pm(a\pm h))\neq 0\) on the relevant shifted buffered boundaries.
- This is the minimal formal object needed to justify bounding \(E'/E\) and \(\mathcal Q_a'/\mathcal Q_a\) uniformly.

---

## 3) Mandatory S6 harness cross‑check (keep it as a guardrail)
For any chosen endpoint \(\Phi_{\mathfrak B}(a,m)\), include a short subsection:

- “Interpretation via explicit formula: does this endpoint correspond to an \(x^\beta\) amplitude leak?”
- Map correctly: s‑frame → u‑frame → v‑frame so that \(a=2\beta-1\).

This remains interpretive, but it is a strong “sanity filter” for endpoint relevance.

---

## 4) Deliverables for v42
- One new *formal* witness family definition (pick GEO‑C1/C2/C3).
- One new FORCE lemma on that family.
- One budget‑eligible UE bound statement (even if constants are deferred), with a clearly marked proof plan that does not violate NG‑BUDGET.
- One resonance note (explicitly: no “one quartet per height” assumption).

If v42 cannot discharge at least FORCE + a credible UE plan on the new geometry, then we should stop iterating and re‑plan prompts (cost discipline).

