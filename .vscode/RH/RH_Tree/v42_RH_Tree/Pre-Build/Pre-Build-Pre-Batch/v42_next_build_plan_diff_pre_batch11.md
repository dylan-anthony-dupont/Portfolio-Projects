# v42 Next Build Plan (diff-only) — pre–Batch 12
**Baseline:** v41 locked  
**Goal of v42 (pre-build):** install GEO‑C4 endpoint + closure schema cleanly; demote obsolete endpoints; isolate the *single active UE brick* + supporting admissibility/robustness lemmas.

---

## 1) Structural edits (high level)
1. **Promote GEO‑C4 to canonical.**  
   Add a new subsection “GEO‑C4: hinge‑circle harmonic endpoint (k=2)” immediately after the existing Geometry Change Requirement box.
2. **Demote prior S5′ / defect-endpoint attempts.**  
   Move the centered defect endpoints and “sidewise max” endpoints into **Appendix: Discarded closure routes / NO‑GO archive**, with one paragraph explaining why (O(δ/a) cancellation, δ‑inert resonance, NG‑Δa‑A).
3. **Reframe the current frontier.**  
   Replace “Missing Lever” box with:
   - FORCE‑robust lemma (open),
   - SHIFT‑ADMISS lemma (open),
   - UE‑INPUT brick (open, single analytic brick).

---

## 2) New canonical definitions to add (paste-ready level)
- \(F(z)=E'(z)/E(z)\), \(\mathcal L_t(v)=F(v+t)-F(v-t)\), \(\mathcal D_{a,h}=\mathcal L_{a+h}-\mathcal L_{a-h}\).
- Hinge‑circle \(C_{m,\delta}: v(\theta)=i m+\delta e^{i\theta}\).
- Phase signal \(\psi(\theta)=\Im(\mathcal D_{a,h}(v(\theta)))\).
- Projection \(P_2\) onto \(\mathrm{span}\{\cos(2\theta),\sin(2\theta)\}\).
- Endpoint \(\Phi^*=\frac{\delta^2}{h}\|P_2\psi\|_{L^2}\).
- Coupling policy \(h=\kappa\delta\) (κ fixed) and nominal δ-policy \(\delta=\eta a/\log^2(m+3)\).

---

## 3) Lemmas/propositions to insert
### 3.1 FORCE (toy computation; lock it)
Insert a proof‑grade toy lemma showing:
- in a single‑quartet toy model, \(\mathcal D^{\mathrm{sing}}(i m+u)=-4h/(u^2-h^2)\),
- \(\psi(\theta)\) is a pure \(k=2\) carrier,
- \(\Phi^*\) equals an explicit constant (e.g. \(4\pi\) up to normalization), independent of δ.

### 3.2 UE reduction lemma (integration-by-parts)
Insert the lemma:
- \(k=2\) Fourier coefficient of \(\psi\) satisfies \(|\widehat\psi(2)|\le \frac14\int|\psi''|\),
- \(|\psi''|\) reduces to \(\delta^2|\partial_v^2\mathcal D|+\delta|\partial_v\mathcal D|\),
- mean value theorem gives \(\partial_v^j\mathcal D = 2h\,\partial_t\partial_v^j\mathcal L_t|_{t=t_*}\).

### 3.3 ACTIVE BRICK statement (open)
State UE‑INPUT as the single analytic obligation:
\[
\sup_{t\in[a-h,a+h]}\sup_{\theta}\big|\partial_t\partial_v^j\mathcal L_t(v(\theta))\big|
\le C\,(\log(m+3))^{C_1}/a^{2+j},\quad j=0,1,2.
\]
Make it explicit: “Everything now reduces to proving this field bound on shift‑admissible hinge circles.”

### 3.4 FORCE‑robustness statement (open)
Insert an explicit lemma template:
- decompose \(\psi = \psi_{\mathrm{forced}} + \psi_{\mathrm{rem}}\),
- show \(\|P_2\psi_{\mathrm{forced}}\| \ge c_0\),
- show \(\|P_2\psi_{\mathrm{rem}}\|\le c_0/2\) under explicit conditions (separation/local count),
- conclude \(\Phi^*\ge c_0/2\).

### 3.5 Shift‑admissibility / buffer lemma (open)
Add a lemma (or definition + remark):
- what “shift‑admissible” means for the four traces \(v(\theta)\pm(a\pm h)\),
- how δ‑shrink restores admissibility,
- ensure statement does not assume RH.

---

## 4) S6 explicit formula mapping update
Add a short remark: off‑axis \(a>0\) corresponds to amplitude leak \(x^{a/2}\) in explicit formula.  
Explain that \(\Phi^*\) is a local “tilt‑derivative field” probe that must be large if such a leak exists, but is shown small by UE‑INPUT.

---

## 5) NO‑GO sanity audit (required diff)
Add a **one‑page audit subsection**:
- list the current NO‑GO lemmas from v40–v41,
- explicitly mark which ones remain binding,
- explicitly mark any that must be weakened/retired because GEO‑C4 requires harmonic/projection endpoints.

---

## 6) Resulting “only open box” (v42 narrative clarity)
At the end of the GEO‑C4 subsection, include a boxed summary:

> **Only open obligations:** UE‑INPUT + FORCE‑robustness + SHIFT‑ADMISS (all explicit).  
> Everything else is now locked scaffolding.

