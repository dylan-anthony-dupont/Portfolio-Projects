# Batch 11 — RH-LOCAL (v41 geometry pivot support)
**Callsign:** RH-LOCAL  
**Choice (mandatory):** **(B) \(N_{\rm eff}=O(1)\)** via a *shift-aware isolation rule* (works even if multiple quartets exist at the same height).

---

## 1) Resonance model being neutralized (explicit)

**Model (danger configuration):** two off-axis quartets at the same v-frame height \(m\),
with tilts \(a\) and \(a-\varepsilon\) (same \(m\), small \(\varepsilon>0\)).  
This is the configuration that produces **\(\delta\)-inert behavior** for defect-type endpoints when \(\delta\asymp\varepsilon\), i.e. a positive lower bound independent of \(\delta\) as \(\delta\to 0\). In v40 this is latched as a proof-grade NO‑GO for the defect class (Lemma 12.14).【turn8file13†L25-L48】

**Why it matters for OPEN‑GEO:** OPEN‑GEO requires that any proposed new endpoint/witness family be **resonance robust** (no \(\delta\)-inert violation of UE). This is explicitly part of the v41 prebuild GEO box requirements.【turn8file4†L51-L53】【turn8file0†L18-L23】

---

## 2) Mechanism (B): define \(N_{\rm eff}\) for shifted evaluations + prove \(N_{\rm eff}\le C\) under a selection rule

### 2.1 Geometry family (LOCAL’s compatible choice)

I adopt **GEO‑C1** as the geometry backbone (hinge-centered witness box), since aligned-box forcing for \(\Phi^{(2s)}\) is now latched false (NG‑\(\Delta a\)‑A).【turn8file7†L10-L12】【turn8file6†L7-L10】

Define the **hinge-centered** box
```tex
\[
B_0(m,\delta):=B(0,m,\delta)=[-\delta,\delta]\times[m-\delta,m+\delta],
\qquad 
\partial B_{0,\kappa/2}:=\partial\bigl(B_0(m,\delta)_{\kappa/2}\bigr).
\]
```

This family is “not restricted to aligned boxes,” as required by OPEN‑GEO.【turn8file4†L37-L44】

### 2.2 Shift set and effective local count \(N_{\rm eff}\)

We are in the v40/v41 two-sided shift framework:
\[
\mathcal L_t(v):=\frac{E'}{E}(v+t)-\frac{E'}{E}(v-t),\qquad 
\mathcal D_{a,h}(v):=\mathcal L_{a+h}(v)-\mathcal L_{a-h}(v),
\]
with the corrected expanded form (Patch‑queue hygiene)【turn8file12†L20-L26】.

For a fixed witness box \(B_0(m,\delta)\), the poles of \(v\mapsto (E'/E)(v+t)\) arise from zeros \(\rho\) of \(E\) lying in the **shifted box** \(t+B_0(m,\delta)\) (equivalently \(\rho-t\in B_0(m,\delta)\)).

Define the **shift-relevant near-zero set**
```tex
\[
\mathcal Z_{\rm shift}(m;a,h,\delta)
:=\Bigl\{\rho:\ E(\rho)=0,\ \exists\, t\in\{\pm(a+h),\pm(a-h)\}\ \text{s.t.}\ \rho\in t+B_0(m,\delta)\Bigr\},
\]
counted with multiplicity,
and \(N_{\rm eff}(m;a,h,\delta):=\#\mathcal Z_{\rm shift}(m;a,h,\delta)\).
```

Interpretation: \(N_{\rm eff}\) counts exactly those zeros whose poles can enter \(\mathcal D_{a,h}(v)\) when \(v\) runs on \(\partial B_{0,\kappa/2}\).

### 2.3 Isolation / selection rule that forces \(N_{\rm eff}=O(1)\) even under resonance

Let \(\{\pm a\pm i m\}\subset Z(E)\) be an off-axis quartet (v-frame), with multiplicity \(r\) (usually \(r=1\)). Consider the **finite** set of zeros of \(E\) in the compact region
\[
\bigcup_{t\in\{\pm(a+h),\pm(a-h)\}}(t+\overline{B_0(m,\delta_0)}),
\quad \delta_0=\eta a/(\log m)^2.
\]
(Compactness gives finiteness; no number theory needed.)

Define a *separation radius*:
```tex
\[
d_*(m;a):=\min\bigl\{|\rho-\rho_*|:\ E(\rho)=0,\ \rho\notin\{\pm a\pm i m\},\ \rho_* \in\{\pm a\pm i m\}\bigr\}>0,
\]
where the minimum is over zeros in the above compact region.
```

Because zeros are isolated, \(d_*(m;a)>0\) unless there is an additional zero *exactly coincident* with the quartet (absorbed into multiplicity \(r\)).

**Selection rule (monotone-safe):**
```tex
\[
\delta:=\min\Bigl(\delta_0,\ \frac{d_*(m;a)}{100}\Bigr),\qquad h\le \delta.
\]
```
Then **no other zeros** can lie inside any shifted box \(t+B_0(m,\delta)\) besides the quartet points themselves. In particular,
\[
N_{\rm eff}(m;a,h,\delta)=4r \quad\text{(hence \(O(1)\))}.
\]

**What this neutralizes:** if there is a near-resonant quartet at tilt \(a-\varepsilon\) with \(\varepsilon\asymp\delta_0\), then \(d_*(m;a)\lesssim \varepsilon\) and the rule shrinks \(\delta\ll \varepsilon\), *automatically excluding* the near-resonant quartet from the shift-relevant set. This is the correct “δ-aware resonance bookkeeping” demanded by OPEN‑GEO.【turn8file0†L18-L23】

> This is not a new theorem about zeta zeros; it is a **witness-box selection rule** based only on discreteness of zeros and admissible δ‑shrinking (already monotone‑safe in the program hygiene).

---

## 3) Plug-in inequality enabled (local contribution bound for the endpoint)

We need a LOCAL bound that FORCE/ENVELOPE can cite in OPEN‑GEO’s “Resonance robustness” clause.

### 3.1 Phase-class local bound (θ=0 form)

For a single pole term \((v-\rho)^{-1}\), any contour segment \(I\) satisfies
\[
\Bigl|\Im\int_I \frac{dv}{v-\rho}\Bigr|
\le \operatorname{Var}_I(\arg(v-\rho))\le 2\pi,
\]
assuming \(I\) does not pass through \(\rho\). Thus each pole contributes \(O(1)\) to phase endpoints (θ=0).

Since \(\mathcal D_{a,h}\) is a linear combination of four \((E'/E)(v\pm t)\) traces, and since each zero in \(\mathcal Z_{\rm shift}\) induces at most **one** pole in each shifted trace, we get the uniform local-phase bound:

```tex
\begin{lemma}[LOCAL: phase-class bound in terms of \(N_{\rm eff}\)]
\label{lem:local-Neff-phase}
Fix \(\kappa\in(0,1/10)\). Let \(B_0(m,\delta)\) be hinge-centered and assume shift-admissibility
(i.e. \(E\) is zero-free on a neighborhood of each shifted contour \(\partial B_{0,\kappa/2}\pm(a\pm h)\)).
Then for the v41 endpoint
\[
\Phi^{(2\mathrm{s})}_{B_0}(a;h)
:=\max_{I\subset \partial B_{0,\kappa/2}}
\Bigl|\Im\int_I \mathcal D_{a,h}(v)\,dv\Bigr|,
\]
the contribution of the shift-relevant poles satisfies
\[
\Phi^{(2\mathrm{s})}_{B_0}(a;h)\Big|_{\rm local}
\ \le\ 8\pi\, N_{\rm eff}(m;a,h,\delta).
\]
In particular, under the isolation rule of \S2.3 one has \(\Phi^{(2\mathrm{s})}_{B_0}(a;h)|_{\rm local}\le 32\pi r\).
\end{lemma}
```

This gives the desired **θ=0** local control but now in terms of a **δ-aware** count \(N_{\rm eff}\), not the δ-blind \(R_a(m)\) (which v40 already warns is insufficient).【turn8file13†L19-L24】

### 3.2 Scale-sensitive (non-phase) bound if ENVELOPE wants an \(h\)-gain term

If an absolute-value bound is needed (not the phase endpoint), then using
\[
\frac{1}{v-\rho+h}-\frac{1}{v-\rho-h}=\frac{2h}{(v-\rho)^2-h^2},
\]
and collar separation \(|v-\rho|\gtrsim \kappa\delta\) on \(\partial B_{0,\kappa/2}\), one gets schematically
\[
|\mathcal D_{a,h}(v)|_{\rm local}\ \lesssim\ \frac{h}{(\kappa\delta)^2}\,N_{\rm eff},
\qquad 
\int_{\partial B_{0,\kappa/2}}|\mathcal D_{a,h}|\,|dv|\ \lesssim\ \frac{h}{\kappa^2\delta}\,N_{\rm eff}.
\]
Thus if v41 chooses a coupling \(h\ll \delta\) (candidate GEO‑C2), LOCAL contributes an **explicit shrink factor** \(h/\delta\) to the local term (while the phase bound remains θ=0).【turn8file6†L7-L10】

I am **not** claiming forcing survives for \(h\ll\delta\) (FORCE must decide); I am only isolating what the local bound becomes in that regime.

---

## 4) Compatibility with v41 geometry requirement (what \(\mathfrak B\) needs from LOCAL)

To make the above lemmas usable, v41 should add a short “shift-admissibility” line to the witness family definition:

* The contour \(\partial B_{0,\kappa/2}\) itself must avoid zeros of \(E\) (standard κ-admissibility).
* **Additionally:** for each shift \(t\in\{\pm(a+h),\pm(a-h)\}\), the shifted contour \(\partial B_{0,\kappa/2}+t\) must also avoid zeros, so that \((E'/E)(v+t)\) is well-defined on the trace.

This is explicitly flagged in the v41 prebuild as “requires careful κ-buffering so shifted evaluations do not land on zeros.”【turn8file6†L7-L10】

Because zeros are discrete, this condition can always be met by shrinking \(\delta\) slightly (monotone-safe).

---

## 5) NO-GO sanity checks (required)

* **Pointwise δ^{3/2} resurrection:** **PASS** — not used; everything above is non-pointwise phase / contour logic (consistent with v35–v37 latches).
* **Centered defect cancellation \(O(\delta/a)\)** (if relevant): **PASS** — not modified; resonance model is acknowledged as in v40 (Lemma 12.14).【turn8file13†L25-L48】
* **δ-inert resonance obstruction:** **CONDITIONAL PASS** — neutralized **only** by making resonance δ-aware via \(N_{\rm eff}\) and by allowing admissible δ‑shrinking until the shift-relevant neighborhood isolates a single quartet (Sections 2.3–3.1). This is exactly the OPEN‑GEO “resonance robustness” requirement.【turn8file4†L51-L53】
* **NG-(Δa)-A aligned-box failure:** **PASS (acknowledged)** — we do not use aligned boxes; hinge-centered geometry is used precisely because aligned-box forcing is false.【turn8file7†L10-L12】【turn8file6†L7-L10】

---

## 6) S6 harness (explicit-formula / amplitude leak interpretation)

**Frame mapping (mandatory):**
\[
u=2s,\qquad v=u-1,\qquad s=\frac{1+v}{2}.
\]
An s-frame zero \(\rho=\beta+i\gamma\) corresponds to \(v_\rho=(2\beta-1)+i(2\gamma)\).  
Thus \(a=2\beta-1\) and \(m=2\gamma\). Off-axis means \(a\neq 0\).

**Explicit-formula interpretation:** an off-axis quartet corresponds to terms \(x^\rho/\rho\) and \(x^{1-\rho}/(1-\rho)\) in explicit formulae; the “amplitude leak” is driven by \(x^\beta\) with \(\beta>1/2\) (equivalently \(a>0\)).  

LOCAL’s mechanism here **does not block the amplitude leak directly**; it ensures that the *analytic endpoint mechanism* does not become δ-inert due to near-resonant additional quartets, by shrinking the witness scale until only the target quartet contributes. In other words: it is a **robustness / bookkeeping device**, not a direct amplitude-leak detector.

---

## MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* **Callsign:** RH-LOCAL
* **Result classification:** **CONDITIONAL**
* **Target gaps closed (by ID):**
  - **OPEN-GEO (Resonance robustness clause)** — provides a proof-grade, δ-aware local bookkeeping mechanism via \(N_{\rm eff}\) + isolation rule.
* **Target gaps still open (by ID):**
  - **OPEN-GEO (Forceability + gate-passing UE)** — FORCE/ENVELOPE/ABSORB must determine whether hinge geometry (and/or \(h\ll\delta\)) yields a forceable lower bound while still passing the exponent-budget gate.
* **Key conclusions (≤5 bullets):**
  1. Resonance is neutralized **structurally** by replacing δ-blind counts with a **shift-aware** \(N_{\rm eff}(m;a,h,\delta)\) and allowing admissible δ-shrinking.
  2. Under the isolation rule, \(N_{\rm eff}=4r=O(1)\) even if multiple quartets exist at the same height (resonance clusters).
  3. For phase endpoints, local poles contribute **θ=0** with an explicit constant: \(\Phi^{(2s)}_{\rm local}\le 8\pi N_{\rm eff}\).
  4. If an absolute-value bound is needed, the local contribution carries a scale factor \(h/(\kappa^2\delta)\) (hence shrinks if \(h\ll\delta\)).
  5. This is compatible with GEO‑C1 hinge-centered geometry and directly addresses OPEN‑GEO’s resonance clause, without any RH smuggling.
* **Paste-ready manuscript edits (TeX blocks):**
  1. **(Definition/Remark)** add just after the OPEN‑GEO box (or inside it) to define \(N_{\rm eff}\):
     ```tex
     \begin{definition}[Shift-effective near-zero count]
     For a hinge-centered witness box \(B_0(m,\delta)=B(0,m,\delta)\) and parameters \(a>0\), \(h>0\),
     define
     \[
     \mathcal Z_{\rm shift}(m;a,h,\delta)
     :=\Bigl\{\rho:\ E(\rho)=0,\ \exists\, t\in\{\pm(a+h),\pm(a-h)\}\ \text{s.t.}\ \rho\in t+B_0(m,\delta)\Bigr\},
     \]
     counted with multiplicity, and \(N_{\rm eff}(m;a,h,\delta):=\#\mathcal Z_{\rm shift}(m;a,h,\delta)\).
     \end{definition}
     ```
  2. **(Lemma)** local bound in terms of \(N_{\rm eff}\) (θ=0):
     ```tex
     \begin{lemma}[LOCAL: phase-class bound in terms of \(N_{\rm eff}\)]
     \label{lem:local-Neff-phase}
     Fix \(\kappa\in(0,1/10)\) and let \(B_0(m,\delta)=B(0,m,\delta)\).
     Assume shift-admissibility: \(E\) is zero-free on a neighborhood of each shifted contour
     \(\partial(B_0(m,\delta)_{\kappa/2})+t\) for \(t\in\{\pm(a+h),\pm(a-h)\}\).
     Then for
     \[
     \Phi^{(2\mathrm{s})}_{B_0}(a;h)
     :=\max_{I\subset \partial(B_0(m,\delta)_{\kappa/2})}
     \Bigl|\Im\int_I \mathcal D_{a,h}(v)\,dv\Bigr|,
     \]
     the contribution of the shift-relevant poles satisfies
     \[
     \Phi^{(2\mathrm{s})}_{B_0}(a;h)\Big|_{\rm local}
     \ \le\ 8\pi\, N_{\rm eff}(m;a,h,\delta).
     \]
     \end{lemma}
     ```
  3. **(Remark)** isolation rule / resonance robustness for the OPEN‑GEO box:
     ```tex
     \begin{remark}[Resonance robustness via admissible shrinking]
     Let \(\delta_0=\eta a/(\log m)^2\) be the nominal scale. Because zeros of \(E\) are isolated,
     for any fixed quartet \(\{\pm a\pm i m\}\subset Z(E)\) there exists a separation radius \(d_*(m;a)>0\)
     to the nearest other zero in the shift-relevant neighborhood.
     Choosing any admissible \(\delta\le \min(\delta_0,d_*(m;a)/100)\) and \(h\le\delta\) isolates the quartet
     in the shifted boxes and yields \(N_{\rm eff}(m;a,h,\delta)=4r\) (multiplicity \(r\)).
     Hence near-resonant quartets with tilt \(a-\varepsilon\) do not create a \(\delta\)-inert obstruction once
     \(N_{\rm eff}\) is used as the bookkeeping object.
     \end{remark}
     ```
* **Dependencies on other branches:**
  - **RH-FORCE / RH-ENVELOPE:** must decide whether GEO‑C1 (or GEO‑C2) yields a forceable lower bound and a gate-passing UE upper bound on the *same* family \(\mathfrak B\).
  - **RH-ABSORB:** must confirm δ-shrinking is monotone-safe in the new geometry/coupling regime (already a program hygiene theme).
* **Referee risk notes (anticipated objections + how addressed):**
  1. *Objection:* “\(d_*\) is non-explicit; you are hiding dependence on unknown zeros.”  
     *Answer:* \(d_*\) is used only to justify **existence** of a resonance-free admissible witness scale (allowed in forceability/existential steps); the resulting bounds are explicit once \(N_{\rm eff}\) is defined.
  2. *Objection:* “Shrinking δ may break forcing.”  
     *Answer:* This is explicitly flagged as a dependency on FORCE; LOCAL supplies the resonance-robust local bound and leaves forcing-vs-coupling viability to the FORCE/ENVELOPE gate analysis.
  3. *Objection:* “Shift-admissibility is extra baggage.”  
     *Answer:* It is unavoidable for \(v\mapsto (E'/E)(v\pm(a\pm h))\) traces; v41 prebuild already requires careful κ-buffering for this reason.【turn8file6†L7-L10】
