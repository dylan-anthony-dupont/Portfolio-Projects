# CR Master Dashboard — v39 locked → v40 PRE‑BUILD (Batch 10 + legacy synthesis)

**Date:** 2026-01-28  
**Callsign:** RH‑CR (Control Room / Integrator)

---

## 1) Canonical posture (now)

- **Locked manuscript:** v39  
- **Primary frontier spine:** **S5Δa (two‑sided shift‑difference endpoint)** — **CONDITIONAL**  
- **Secondary harness:** **S6 explicit‑formula amplitude‑leak mapping** (mandatory cross‑check)  
- **Deprecated / NO‑GO route:** S5^def “centered defect endpoint transfer + p>1 + δ‑blind resonance”

---

## 2) Ranked blocker queue (v40 must reduce these)

### CRITICAL
1. **ML‑Δa forcing**: prove a constant lower bound \(c_0>0\) for the new endpoint under an off‑axis quartet (toy model suggests \(c_0\approx\pi/2\)).  
2. **ML‑Δa UE**: derive a \(\delta\)-uniform upper bound for the new endpoint on \(\kappa\)-admissible aligned boxes at the nominal scale \(\delta=\eta a/\log^2 m\), passing the Gate Calculator.

### HIGH
3. **Resonance robustness**: show near‑resonant quartets at \(a-\varepsilon\sim a-h\) cannot keep the new endpoint \(\delta\)-inert (i.e., no hidden “resonance constant” obstruction remains).  
4. **κ‑admissibility + δ‑shrinking compatibility**: ensure the chosen \(B(\alpha,m,\delta)\) can be shrunk without crossing zeros, and that the endpoint bound improves under shrinking.

### MED
5. **S6 mapping upgrade**: interpret \(\mathcal D_{a,h}\) as a finite‑difference in \(\beta=\tfrac12+\tfrac a2\), i.e. “amplitude‑leak derivative”.

---

## 3) Truth‑latching NO‑GO borders (locked into manuscript in v40)

**(NG‑1) No centered/same‑box transfer (ML‑1 fails).**  
Forced phase on the forcing box is \(\Omega(1)\), while the centered defect endpoint can be \(O(\delta/a)\).

**(NG‑2) Endpoint-class ceiling: no \(p>1\) from pointwise UE.**  
For \(\Phi_B^{\rm def}(a)\), \(|\Im\int|\le\int|\cdot|\) and side length \(\asymp\delta\) caps the gain at \(p\le1\) absent new non-pointwise structure.

**(NG‑3) δ‑blind resonance proxy is insufficient.**  
\(\mathcal R_a(m)\) does not see near‑resonant quartets and cannot certify \(\delta\)-uniformity.

**(NG‑4) Defect-box pole forcing cannot replace ML‑1.**  
Any forcing via defect poles yields \(\pi/2\) lower bounds independent of \(\delta\), incompatible with \(\delta^p\) shrink strategies.

**(NG‑5) One‑pole endpoints on \(E'/E\) are not currently closable.**  
Argument-principle forcing is δ‑independent; current analytic envelopes for \(E'/E\) produce \(\delta^0\) bounds on side integrals.

---

## 4) Minimal S5Δa dependency DAG (v40 target)

**Off-axis quartet exists at height \(m\) with tilt \(a>0\)**  
→ choose \(h\sim\delta=\eta a/\log^2 m\) and an admissible aligned box \(B\)  
→ **(Forcing)** \(\Phi^{(2s)}_B(a;h)\ge c_0\)  
→ **(UE)** \(\Phi^{(2s)}_B(a;h)\le \mathrm{UE}(m,a,\delta,h)=o(1)\) as \(m\to\infty\)  
→ contradiction for all sufficiently large \(m\)  
→ finite-height front-end (verified band / computation) closes remaining range  
→ \(a(m)=0\) for all nontrivial heights → RH → structural corollaries become corollaries (post‑theorem).

---

## 5) Live status board (what is OPEN / CLOSED)

### Boxed open statement(s)
- **OPEN:** **ML‑Δa** (two‑sided shift‑difference endpoint closure) — replaces v39’s ML‑1/ML‑2/ML‑3 as written.

### Closed as NO‑GO latches (do not revisit without new math)
- **CLOSED (NO‑GO):** ML‑1 centered transfer  
- **CLOSED (NO‑GO):** “recover \(p>1\)” for \(\Phi^{\rm def}\) via pointwise UE  
- **CLOSED (NO‑GO):** defect-box pole forcing as substitute for transfer  
- **CLOSED (NO‑GO, conditional):** \(\Phi^E_B\) (one‑pole endpoint on \(E'/E\)) under current analytic envelopes

---

## 6) Immediate v40 patch intent (one line)

**v40 will**: (i) lock in NG‑1…NG‑5, (ii) demote S5^def attempt, (iii) introduce S5Δa definitions + toy model, and (iv) replace the Missing Lever box by ML‑Δa.

