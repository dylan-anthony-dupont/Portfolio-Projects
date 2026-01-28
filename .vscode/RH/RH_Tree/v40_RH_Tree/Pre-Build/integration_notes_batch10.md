# Integration Notes — Batch 10 (v39 locked → v40 pre-build)

**Program state:** v39 is the current locked manuscript. Batch 10 resolves several *boxed* ambiguities in the v39 S5′ frontier and provides multiple proof-grade **NO‑GO latches**. In parallel, two legacy “Missing Lever” candidate mechanisms were ingested; only one survives contact with the v39 NO‑GO borders.

**Date:** 2026-01-28  
**Integrator:** RH‑CR (Control Room)

---

## 0) Executive summary (what changed since v39)

### Truth-latching outcomes (now treated as *canonical constraints*)

1. **ML‑1 (Transfer / domination to the centered defect box) is impossible** in the v39 geometry: forced phase on the *forcing box* is \(\Omega(1)\), while the centered defect endpoint on \(B(0,m,\delta)\) can be \(O(\delta/a)\).  
   → We must not keep “same‑box / centered‑box transfer” as an open item; it is a **NO‑GO latch**.

2. **The slogan “prove \(p>1\) for \(\Phi_B^{{\rm def}}(a)\)” is mis-specified** for the current endpoint class: any UE estimate derived only from pointwise bounds on \(\sup_{\partial B}|\mathcal L_a|\) has a **side-length ceiling** and cannot yield \(p>1\).  
   → Replace “\(p>1\)” with the **Gate Calculator** language: we need a *gate‑passing* regime in terms of \((p_{\rm eff},\theta_{\rm eff})\), or else a new endpoint class.

3. **Resonance control must be \(\delta\)-aware**: the v39 resonance proxy \(\mathcal R_a(m)\) is \(\delta\)-blind and cannot see the near‑resonance configuration that makes \(\Phi_B^{{\rm def}}(a)\) \(\delta\)-inert.  
   → Any surviving “defect‑UE” bound must involve a \(\delta\)-aware resonance term or hypothesis.

4. **Defect-box pole-winding forcing cannot replace ML‑1**: any attempt to force via a defect pole/zero inside an aligned box yields a \(\pi/2\) lower bound independent of \(\delta\), contradicting any \(\delta^p\) shrinkable UE target.  
   → Another **NO‑GO latch**: “force via defect poles” cannot be used for a shrink‑with‑\(\delta\) UE mechanism.

### Surviving candidate for the “Missing Lever”

- The only legacy mechanism consistent with the v39 NO‑GO borders is a **non-pointwise (in shift \(a\)) endpoint redesign**: a **two‑sided shift-difference** (finite difference in \(a\)) which:
  * breaks the quartet cancellation that kills \(\Phi_B^{{\rm def}}(a)\) on centered boxes, and
  * is designed to be \(\delta\)-aware and resonance‑robust.

This becomes the v40 frontier: **S5″ / S5Δa (two-sided shift‑difference UE)**.

---

## 1) Batch 10 branch ingestion (PASS/FAIL + what becomes canonical)

### RH‑BRIDGE — **PASS (as a NO‑GO latch package)**
- Delivers proof-grade lemma: **NO‑GO: no \(\delta\)-uniform transfer to the centered defect box** (proposed label `lem:ML1-samebox-nogo`).  
- Patch guidance: update the v39 Missing Lever box to explicitly record that \(\widehat B=B(0,m,\delta)\) (and nearby \(O(\delta)\) shifts away from defect singularities) cannot work.

**Impact:** ML‑1 as written in v39 must be **reframed**: “transfer” is not forbidden in principle, but *centered/same‑box transfer is*.

---

### RH‑ENVELOPE — **PASS (as endpoint-class ceiling + δ-aware resonance proposal)**
- Proof-grade lemma: **Side-length ceiling** for \(\Phi_B^{\rm def}(a)\) (proposed label `lem:defect-p-ceiling`): from \( |\Im\int|\le \int|\cdot| \) and side length \(\asymp \delta\), no \(p>1\) can be obtained *solely* from pointwise UE on \(\mathcal L_a\).  
- Proposes upgrading resonance term to a **\(\delta\)-aware resonance sum** \(\mathcal R_{a,\delta}(m)\) and updating the *target* defect-UE inequality accordingly.

**Impact:** “Recover \(\delta^{3/2}\)” is formally dead for the current endpoint class; the manuscript must speak in gate-calculator terms and/or change endpoint class.

---

### RH‑LOCAL — **PASS (as δ-blindness diagnosis + δ-aware counting primitive)**
- Adds a proof-grade remark: \(\mathcal R_a(m)\) is \(\delta\)-blind in the near-resonance example; therefore v39’s resonance proxy cannot justify any defect‑UE statement that claims \(\delta\)-uniformity.  
- Adds \(\delta\)-aware primitive: **near-resonance count** \(N_{\rm res}(a,m,\delta)\) (proposed label `def:near-resonance-count`).

**Impact:** any remaining defect‑UE path must explicitly condition on / control \(N_{\rm res}\) or use an endpoint that intrinsically cancels near-resonance.

---

### RH‑FORCE — **PASS (as forcing mismatch / NO‑GO latch)**
- Provides proof-grade lemma: **NO‑GO: defect-box pole‑winding cannot replace ML‑1** (label suggestion `lem:defectbox-nogo-ML1`).

**Impact:** eliminates an entire class of “replace transfer with defect forcing” attempts.

---

### RH‑ABSORB — **PASS (gate calculator + stop-loss clause)**
- Provides a “Gate Calculator” restatement of the exponent budget: what matters is a **gate-passing inequality** of the form  
  \(p_{\rm eff}-\theta_{\rm eff}\ge \tfrac12\) (or equivalent), not “\(p>1\)” in isolation.
- Provides a **stop-loss clause**: if the endpoint class is provably capped at \(p_{\rm eff}\le 1\) and resonance terms are \(\delta^{-1}\)-singular, then S5′ cannot close without new analytic input.

**Impact:** v40 must explicitly articulate the gate variables for any endpoint it proposes.

---

## 2) Legacy “Missing Lever” candidates (two responses) — conflict resolution

### Legacy candidate A ("perfected" response): **forceable endpoint on \(E\) itself**
Defines  
\[
\Phi^E_B := \max_{I\in\mathrm{Sides}(\partial B_{\kappa/2})}\left|\Im\int_I \frac{E'}{E}(v)\,dv\right|\ge \pi/2
\]
by the argument principle.

**Why this is not viable under v39 constraints (NO‑GO):**
- Any admissible box that encloses a zero forces total winding \(2\pi\), hence side increment \(\ge \pi/2\) **independent of \(\delta\)**.
- The v39 analytic envelope for \(\sup|E'/E|\) contains a **local** \(\sim N_{\rm loc}/(\kappa\delta)\) term, so \(\int |E'/E|\) on a side of length \(\asymp\delta\) is typically **\(\delta^0\)** (not shrinking).  
- Therefore, obtaining an upper bound like \(\Phi^E_B<\pi/2\) would require *new local cancellation/isolation* beyond anything currently in v39 (and beyond what Batch 10 certifies).

**Verdict:** keep as an *interpretive* idea but treat as **NO‑GO for v40** unless accompanied by a genuinely new local mechanism.

---

### Legacy candidate B (initial response): **two‑sided shift‑difference endpoint (finite difference in \(a\))**
Defines the shift quotient and log‑derivative
\[
\mathcal Q_a(v)=\frac{E(v+a)}{E(v-a)},\qquad
\mathcal L_a(v)=\frac{E'}{E}(v+a)-\frac{E'}{E}(v-a),
\]
then defines a **non-pointwise in \(a\)** object
\[
\mathcal D_{a,h}(v):=\mathcal L_{a+h}(v)-\mathcal L_{a-h}(v),
\]
and an endpoint (taken as a **max over sides** to be forceable/robust):
\[
\Phi^{(2\mathrm{s})}_B(a;h):=
\max_{I\in\mathrm{Sides}(\partial B_{\kappa/2})}
\left|\Im\int_I \mathcal D_{a,h}(v)\,dv\right|.
\]

**Why this survives v39 NO‑GO borders (provisionally):**
- It is not a one-pole endpoint; it is a **finite-difference in the shift parameter**, designed to defeat the centered quartet cancellation.
- UE upper bounds naturally take the form  
  \(\Phi^{(2\mathrm{s})}\le C\,\delta\sup |\mathcal D_{a,h}|\), and \(\mathcal D_{a,h}\) can plausibly gain an extra \(h\)-smallness or resonance cancellation compared to \(\mathcal L_a\).

**Verdict:** this is the best current candidate for the “Missing Lever” to be embedded in v40 as the **single boxed open statement**, replacing ML‑1/ML‑2/ML‑3 in their v39 form.

---

## 3) Canonical “Missing Lever” statement for v40 (what must be proved)

> **(ML‑Δa) Two‑sided shift‑difference UE closure (OPEN).**  
> Define \(\mathcal D_{a,h}=\mathcal L_{a+h}-\mathcal L_{a-h}\) and \(\Phi^{(2\mathrm{s})}_B(a;h)\) as above.  
> Choose the nominal box scale \(\delta=\delta_0(m,a)=\eta a/(\log m)^2\) and couple the shift step \(h\) to \(\delta\) (e.g. \(h=\delta\)).  
> Prove:
> 1. (**Forcing**) If an off-axis quartet exists at height \(m\) with tilt \(a>0\), then there exists a \(\kappa\)-admissible aligned box \(B\) at that height such that  
>    \(\Phi^{(2\mathrm{s})}_B(a;h)\ge c_0\) with an absolute constant \(c_0>0\) (toy model suggests \(c_0\approx \pi/2\)).
> 2. (**UE upper bound, gate-passing**) For all such admissible \(B\),  
>    \(\Phi^{(2\mathrm{s})}_B(a;h)\le \mathrm{UE}(m,a,\delta,h)\) where \(\mathrm{UE}\) is \(\delta\)-uniform and satisfies the Gate Calculator (e.g. \(\mathrm{UE}=o(1)\) as \(m\to\infty\) for the nominal \(\delta\)).
> 3. (**Resonance robustness**) Near-resonant quartets at \(a-\varepsilon\sim a-h\) cannot make \(\Phi^{(2\mathrm{s})}\) \(\delta\)-inert in a way that violates (2).

This replaces v39’s “Transfer + Defect‑UE + Resonance control” triad by a *single* redesigned endpoint obligation.

---

## 4) The “something” (holistic read) + confidence

### What the Missing Lever is most likely to be
In manuscript language: **a \(\delta\)-aware endpoint that is non-pointwise in the shift/tilt parameter** \(a\), i.e. a *tilt-derivative / finite-difference* endpoint, because:

- every pointwise-in-\(a\) defect endpoint inherits either
  * quartet cancellation at the centered box, or
  * \(\delta\)-inertness under near-resonance, or
  * a side-length ceiling that blocks \(p>1\) gains.

### Confidence
- **High (~0.8)** that *some* “tilt-derivative / shift-difference” device is necessary, because Batch 10 gives multiple independent NO‑GO latches eliminating the entire prior endpoint class family.  
- **Medium (~0.6)** that the specific choice \(\mathcal D_{a,h}=\mathcal L_{a+h}-\mathcal L_{a-h}\) closes the loop, because the analytic UE for \(\mathcal D_{a,h}\) is not yet proven and may still face hidden resonance phenomena.

---

## 5) Immediate v40 edits implied by this ingestion (diff-only)

1. **Demote** the current v39 “centered defect endpoint” attempt as a *NO‑GO cautionary route* (keep lemma/remark artifacts).
2. **Insert** Batch 10 NO‑GO lemmas/remarks (transfer NO‑GO, defect-box forcing NO‑GO, p>1 ceiling).
3. **Replace** Box `box:missing-lever-v39` by Box `box:missing-lever-v40` containing **ML‑Δa**.
4. **Add** the new endpoint definitions \(\mathcal D_{a,h}\) and \(\Phi^{(2\mathrm{s})}_B(a;h)\) and a toy-model calculation subsection.
5. **Update** the S6 harness subsection to interpret \(\mathcal D_{a,h}\) as a “β-derivative / amplitude-leak detector” (finite-difference in \(\beta=\tfrac12+\tfrac a2\)).

---

## Patch Packet (integrator summary)
- **Callsign:** RH‑CR  
- **Result classification:** CONDITIONAL (pre-build ready; analytic closure still OPEN)  
- **Key conclusions (≤5):**
  1. Centered transfer ML‑1 is a hard NO‑GO.
  2. “Recover \(p>1\)” is dead for the current defect endpoint class.
  3. Resonance control must be \(\delta\)-aware (current proxy is δ-blind).
  4. Defect-box pole‑winding forcing cannot replace ML‑1.
  5. The only viable frontier candidate is a **tilt-difference / non-pointwise in \(a\)** endpoint redesign (ML‑Δa).
- **Dependencies:** None required to *state* ML‑Δa; closure depends on future analytic UE bounds for \(\mathcal D_{a,h}\).
