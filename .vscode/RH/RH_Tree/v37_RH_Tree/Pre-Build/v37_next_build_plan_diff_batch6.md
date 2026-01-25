# v37 pre-build plan (diff-only) — post Batch 6

Date: 2026-01-25  
Baseline: **v36 locked**  
Purpose of v37: an **S5′ architecture build**: integrate phase/winding endpoints + forcing lemma + acceptance gates, and isolate the *single Missing Lever* with zero drift.

---

## 0) What stays locked (non-negotiable carryover from v36)

1. **Truth-latching NO–GO archive** remains binding:
   - no pointwise UE / disc/Poisson evaluation endpoints,
   - no absolute \(L^r(\partial B)\) endpoints on \(|E'/E|\),
   - no projection-kill tricks unless forcing is redesigned.
2. **Forceability gate** remains binding:
   - any endpoint must either dominate the forced object or come with its own forcing lemma.
3. Repro-pack schema remains **fail-closed** on endpoint metadata.

---

## 1) New content to be merged into v37 (additive patches)

### (A) S5′ Phase Toolkit subsection (new, early in Section `sec:S5-frontier`)
Insert a compact toolkit:

- Definition: phase increment on a boundary arc  
  \(\Delta_\Gamma\arg f := \Im\int_\Gamma (f'/f)\,dv\) (collar nonvanishing required).
- Lemma: vertical specialization on \(I_+\): becomes \(\int \Re(f'/f)\,dy\).
- Lemma: additive split under \(E=F\cdot Z_{\rm loc}\).
- Lemma: local phase δ–inert bound \(|\Delta\arg Z_{\rm loc}|\le \pi N_{\rm loc}(m)\).
- **Notation hygiene remark:** parenthesis discipline (Im outside integral).

### (B) FORCE endpoint candidate: buffered boundary max-side phase
Insert:
- Definition \(\widetilde D_B(W)\) on the buffered contour \(\partial B_{\kappa/2}\).
- Lemma: interior zero ⇒ \(\widetilde D_B(W)\ge \pi/2\) (argument principle).
- Remark: **tail rewrite vs transfer inequality** (forceability gate concretized).

### (C) ENVELOPE residual phase budget
Insert:
- Definition of shifted segment \(I_{+,\lambda}\) and its phase increment.
- Lemma: phase split on \(I_{+,\lambda}\).
- Corollary: residual phase budget \(|\Delta\arg F|\le 2\delta(C_1\log m+C_2)\).

### (D) ABSORB: S5′ closure criterion + acceptance gate
Insert:
- Theorem `thm:S5prime-closure` (budget-eligible closure spine for phase endpoints).
- Remark `rem:S5prime-gate` (explicitly rejects raw Δarg and L^2-in-disguise endpoints).

### (E) S6 harness appendix (short, explicitly non-closure)
Add a one-page appendix:
- map v-frame off-axis \(\Re v\neq 0\) to s-frame \(\beta\neq 1/2\),
- interpret: such zeros produce \(x^\beta\) amplitude terms in the classical explicit formula,
- label as **interpretation harness only** (no prime-error bounds claimed).

---

## 2) Repro pack / schema deltas (v37 pre-build)

Update the certificate schema to include:

- `endpoint_family`: `"phase"` / `"winding"` / `"tbd-cancellation"`,
- `endpoint_definition`: label (LaTeX ref),
- `forcing_target`: `"DB"` or `"Dtilde"` and a boolean `forceability_gate_passed`,
- exponent budget fields: `(p, theta, q)` + model string for `G(n,kappa)`,
- `missing_lever_open`: true/false (must be **true** in v37 unless a new endpoint closes it).

Fail-closed rule:
- if any of these fields are missing, the certificate is invalid.

(No new computations; schema-only.)

---

## 3) PASS/FAIL criteria for the v37 build

### PASS if all are true
- All Batch‑6 toolkit lemmas and the \(\widetilde D_B\) forcing lemma are integrated with correct hypotheses (collar nonvanishing stated).
- The S5′ acceptance gate is present and rejects raw Δarg + L^2-in-disguise endpoints.
- The manuscript contains an explicit boxed statement of the **Missing Lever** and labels it OPEN.
- No new RH-claiming text appears (v37 is architecture only).

### FAIL if any occur
- Any phase endpoint is written using \(\int \Im(f'/f)\,dv\) instead of \(\Im\int (f'/f)\,dv\) (notation bug).
- Any text implies S5′ closure without supplying explicit \((p,\theta,q)\) in the acceptance gate.
- Any point evaluation or absolute \(L^r\) endpoint re-enters the S5 section without being flagged as NO–GO.

---

## 4) What v37 sets up for the next batch (v37 → v38 prebuild)

Batch 7 should target exactly one thing:

> Construct (or kill) a **cancellation / less-singular endpoint class** that is forceable and budget-eligible:  
> provide a UE inequality with p≥1/2 and a local bound with θ≤p−1/2 (ideally θ=0), or else prove a new NO‑GO that narrows the search space further.

