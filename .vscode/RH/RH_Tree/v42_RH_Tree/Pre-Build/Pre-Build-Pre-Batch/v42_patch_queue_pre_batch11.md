# v42 Patch Queue — pre–Batch 12
*(Paste-ready targets; ordered by dependency. Labels are stable and should be referenced in Batch‑12 prompts.)*

---

## Q42.1 — Insert GEO‑C4 geometry + endpoint (definitions)
**Location:** After the Geometry Change Requirement box (early Part II / local analysis section).  
**Add:**
1. Define hinge circle \(C_{m,\delta}: v(\theta)=i m+\delta e^{i\theta}\).  
2. Define \(F=E'/E\), \(\mathcal L_t\), \(\mathcal D_{a,h}\).  
3. Define \(\psi_{a,h}(\theta)=\Im(\mathcal D_{a,h}(v(\theta)))\).  
4. Define projection \(P_2\) onto \(\{\cos 2\theta,\sin 2\theta\}\).  
5. Define \(\Phi^*=\frac{\delta^2}{h}\|P_2\psi\|_{L^2}\).

**Dependencies:** none (pure definitions).

---

## Q42.2 — Coupling & δ-policy (truth-latching)
**Location:** Immediately after Q42.1.  
**Add (canonical policy):**
- \(h=\kappa\delta\), \(\kappa\in(0,1)\) fixed.
- \(\delta=\eta\,a/\log^2(m+3)\), \(\eta\in(0,1)\) fixed.

**Note:** Explicitly state: FORCE is δ‑independent once κ fixed; UE improves as δ shrinks.

---

## Q42.3 — Toy forcing lemma (LOCKED)
**Location:** New lemma “FORCE (toy)” in GEO‑C4 subsection.  
**Statement:** In the single‑quartet toy model,
\[
\mathcal D^{\mathrm{sing}}(i m+u)=-\frac{4h}{u^2-h^2},\quad u=\delta e^{i\theta},
\]
\(\psi(\theta)\) is a \(k=2\) carrier, and
\[
\Phi^*(m,a,\delta,h)=4\pi\ \text{(up to endpoint normalization), independent of }\delta.
\]
**Include full computation** (already available from legacy 1a/1b).

---

## Q42.4 — UE reduction via IBP (LOCKED)
**Location:** Immediately after Q42.3.  
**Add lemma chain:**
1. \( \widehat\psi(2)=\int \psi e^{-2i\theta}\), IBP twice ⇒ \(|\widehat\psi(2)|\le \frac14\int|\psi''|\).  
2. Chain rule: \(|\psi''|\lesssim \delta^2|\partial_v^2\mathcal D|+\delta|\partial_v\mathcal D|\).  
3. Mean-value in shift: \(\partial_v^j\mathcal D = 2h\,\partial_t\partial_v^j\mathcal L_t|_{t=t_*}\).

---

## Q42.5 — ACTIVE BRICK: UE‑INPUT field bound (OPEN)
**Location:** Boxed “Only Open Brick” right after Q42.4.  
**Statement template:**
For \(j=0,1,2\),
\[
\sup_{t\in[a-h,a+h]}\sup_{\theta\in[0,2\pi]}
\big|\partial_t\partial_v^j\mathcal L_t(v(\theta))\big|
\le C\,\frac{(\log(m+3))^{C_1}}{a^{2+j}}.
\]
**Goal:** combine with Q42.4 to get \(\Phi^*=o(1)\) under δ-policy.

---

## Q42.6 — FORCE‑robustness lemma (OPEN)
**Location:** After Q42.5.  
**Statement template:**
Decompose
\[
\psi=\psi_{\mathrm{forced}}+\psi_{\mathrm{rem}},
\]
where \(\psi_{\mathrm{forced}}\) is the contribution from the quartet \(\pm a+i m\) to \(\mathcal D_{a,h}\).
Show:
- \(\|P_2\psi_{\mathrm{forced}}\|_{L^2}\ge c_0(\kappa)\cdot h/\delta^2\),
- \(\|P_2\psi_{\mathrm{rem}}\|_{L^2}\le \tfrac12 c_0(\kappa)\cdot h/\delta^2\)
under explicit hypotheses (shift‑admissibility + remainder bound from local zero counts/separation),
⇒ \(\Phi^*\ge c_0/2\).

---

## Q42.7 — Shift‑admissibility definition + δ‑shrink lemma (OPEN)
**Location:** Before using Q42.1–Q42.6 in the contradiction proof.  
**Add:**
- Definition of “shift‑admissible” (all four traces \(v(\theta)\pm(a\pm h)\) avoid zeros).  
- A δ‑shrink lemma: if admissibility fails, shrink δ until it holds; FORCE unaffected, UE improves.

---

## Q42.8 — Resonance / multi‑quartet remark (OPEN)
**Location:** End of GEO‑C4 subsection (before global RH conclusion).  
**Add remark/lemma template:**
- Define an “effective multiplicity” \(N_{\mathrm{eff}}(m,\delta)\) capturing number of poles within \(O(\delta)\) of shifted traces.
- State sufficient condition (e.g. \(N_{\mathrm{eff}}\le C\log m\)) under which Q42.6 + Q42.5 remain valid.

---

## Q42.9 — Demote obsolete endpoints to NO‑GO Appendix (EDIT)
**Location:** Appendix “Discarded closure routes / NO‑GO archive”.  
**Action:** Move S5′ centered defect endpoints and sidewise-max endpoints here with:
- explicit O(δ/a) cancellation,
- δ‑inert resonance example,
- statement: “kept as cautionary; not used in closure spine.”

---

## Q42.10 — NO‑GO sanity audit patch (EDIT)
**Location:** NO‑GO Appendix front matter.  
**Action:** Add a 1‑page table:
- NO‑GO lemma name,
- what it forbids,
- whether GEO‑C4 needs it to be modified/retired,
- justification.

---

## Q42.11 — S6 harness remark update (EDIT)
**Location:** Cross-check / interpretation section.  
**Add:** off‑axis \(a\) corresponds to explicit-formula amplitude leak \(x^{a/2}\); GEO‑C4 endpoint is a local tilt‑derivative detector.

