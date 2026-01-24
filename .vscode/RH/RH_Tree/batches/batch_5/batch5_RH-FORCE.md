# Batch‑5 — RH‑FORCE (S5 forcing‑compatibility gatekeeper)
Ground truth: **v35** (`manuscript_v35.tex/pdf`, locked 2026‑01‑23).  
Scope: forcing compatibility only (single‑box, constant‑limited). No UE redesign proofs here.

---

## 0) Executive decision (decision‑grade)
### What forcing actually gives (and only gives)
- In v35, the **only forced contradiction object** is the **dial deviation**
  \[
  D_B(W):=\sum_{\pm}\bigl|W(v_\pm)-e^{i\phi_{0,\pm}}\bigr|
  \]
  (v35 §12).  
- The forcing chain lower‑bounds \(D_B(W)\) by a **fixed constant** \(c\) up to \(\delta\)-small deductions, and **cannot grow with height** (single‑box forcing is \(O(1)\); v35 Lemma 8.2 and Appendix A.3).

### Therefore (S5 gate)
Any S5 redesign is **NO‑GO** unless it satisfies **one** of the following:

1) **Forcing‑preserving:** it keeps \(D_B(W)\) as the forced endpoint (the contradiction object), and merely replaces the *upper‑envelope endpoint* used to bound \(D_B(W)\); or  
2) **Forcing‑transfer:** if it replaces \(D_B(W)\) by a different endpoint \(\Phi_B\), it proves a *forcing transfer lemma*:
   - either \(\Phi_B \ge D_B(W)\) for all admissible boxes/quotients (domination), or
   - an independent forcing lemma: **quartet ⇒ \(\Phi_B \ge c_\Phi\)** (v35 Remark 12.1).

This is exactly the compatibility rule already encoded as Remark 12.1 in v35 (§12). The purpose of this batch is to hard‑gate this so S5 work does not drift into unforceable endpoints.

---

## 1) What counts as “forceable” in the v35 architecture (formal gate)
### Definition (forceable endpoint, single‑box architecture)
Let \(B\) be a \(\kappa\)-admissible aligned box and \(W\) the boundary quotient (v35 Bridge 1 setup).  
A boundary functional \(\Phi_B\) (defined on the same objects \(W\) and/or \(E\)) is **forceable** if, under the existence of an off‑axis quartet aligned to \(B\), one can prove a lower bound
\[
\Phi_B \ \ge\ c_\Phi \ -\ \delta\cdot \mathrm{Err}(m)
\]
with \(c_\Phi>0\) independent of \(m\), and with \(\mathrm{Err}(m)\) exactly budgeted in the same ledger style as the v35 forcing side.

### Lemma (domination‑based forcing transfer; trivial but required)
If a candidate endpoint \(\Phi_B\) satisfies
\[
\Phi_B \ \ge\ D_B(W)\qquad\text{for all admissible }(B,W),
\]
then the existing forcing lemma for \(D_B(W)\) implies the same forcing lower bound for \(\Phi_B\) with **no change** in constants.

**Referee note.** This is the only “automatic” forcing transfer available without re‑proving the forcing chain.

---

## 2) Candidate‑by‑candidate forceability audit table (S5 gatekeeper)
v35 does **not** yet commit to a specific \(\Phi_B\) (Section 12 is explicitly “open”). The only concrete information is the allowed *class direction*: “non‑pointwise, e.g. an \(L^2\) or energy functional,” plus the compatibility rule (Remark 12.1).

The following table is therefore a **forceability audit** of the natural candidate classes currently on the table.

| Candidate endpoint \(\Phi_B\) (typical S5 proposals) | Does \(\Phi_B \ge D_B(W)\) hold as stated? | Is there a proved “quartet ⇒ \(\Phi_B\ge c_\Phi\)” forcing lemma in v35? | Verdict (forceability) | RH‑FORCE ruling |
|---|---:|---:|---|---|
| **(C1) Dial‑dominating endpoint**: \(\Phi_B := D_B(W)\) or \(\Phi_B := \sup_{v\in\partial B}|W(v)-e^{i\phi_0(v)}|\) or any endpoint that explicitly contains the dial evaluation | Yes (by definition / trivial dominance) | Not needed | **PASS** | **Forceable without any new forcing work.** |
| **(C2) Pure boundary \(L^2\)/energy endpoint on \(W\)**: \(\Phi_B := \|W-e^{i\phi_0}\|_{L^2(\partial B)}\), or \(\|\partial_s W\|_{L^2(\partial B)}\), etc. | No (not structurally; point values do not lower‑bound \(L^2\) without extra regularity and explicit constants) | No | **FAIL (as‑is)** | **NO‑GO unless** ENVELOPE supplies a new forcing lemma or a proven domination inequality with explicit hypotheses/constants. |
| **(C3) Endpoints purely in \(E\)**: \(\Phi_B(E):=\|E'/E\|_{L^2(\partial B)}\), Carleson‑type energies, etc. | Not even comparable unless a transfer lemma is proved (since forcing is on \(W\) / dial deviation) | No | **FAIL (as‑is)** | **NO‑GO** until a forcing transfer lemma is written and checked referee‑grade. |

**Key point:** In the current architecture, *only (C1)* is automatically compatible with the forcing chain.  
Any candidate in (C2)–(C3) is unforceable unless a genuinely new forcing lemma is added.

---

## 3) Task‑2: if anyone redefines the contradiction endpoint away from \(D_B(W)\)
### NO‑GO statement (to prevent drift)
If an S5 draft replaces the contradiction object \(D_B(W)\) in the tail inequality by a different endpoint \(\widetilde D_B\) (or \(\Phi_B\)) **without** proving either:
- \(\widetilde D_B \ge D_B(W)\) for all admissible \((B,W)\), **or**
- “quartet ⇒ \(\widetilde D_B \ge c_{\widetilde D}\)” (with explicit \(c_{\widetilde D}>0\)),

then the forcing half of the forcing‑vs‑envelope inequality becomes **logically disconnected** and the tail criterion ceases to be derived.

This is exactly the meaning of v35 Remark 12.1; the batch‑5 enforcement is to make it impossible to miss.

---

## 4) Task‑3: Harness / JSON alignment implications (G‑12 continuity)
v35 already hardened the repro pack schema to record:
- `UE_endpoint_class`
- `endpoint_functional`
- `forcing_architecture`
- `forcing_constants` (symbolic expressions for \(c,c_0,K_{\rm alloc}\))
- `UE_exponent_p`

and the verifier outputs a `REGEN_MATCH` flag and prints strict inequality status.

### Required rule for S5 (v36+)
If ENVELOPE changes **any** of:
- the inequality checked,
- the endpoint class / endpoint functional,
- the forced endpoint (dial deviation definition),
- the forcing architecture string (should remain “single‑box forcing” unless forcing is actually re‑proved),

then the certificate schema **must** be updated and the verifier must enforce a mismatch‑fail.

### Minimal robust additions (recommended; still surgical)
Add to the certificate JSON and verifier output:

1) `dial_deviation_definition` (string):
   - example: `"D_B(W)=sum_{±}|W(v_±)-exp(i φ_{0,±})|"`.
2) `forceability_mode` (enum string):
   - `"domination"` if Φ_B ≥ D_B(W) is asserted,
   - `"new_forcing_lemma"` if a new forcing lemma is being used (must cite lemma label),
   - `"not_applicable"` if \(D_B(W)\) remains the forced endpoint and Φ_B is only an envelope endpoint.
3) `theorem_reference` (string):
   - e.g. `"Theorem 11.1, inequality (14), v35"`.

These do **not** prove anything; they simply stop silent mismatch between theorem and artifact (G‑12 hygiene).

---

# MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* Callsign: RH-FORCE
* Result classification: PASS
* Target gaps closed (by ID):
  - **G-2 (mutated → S5) / S5–FORCE gate enforced** (forceability criterion made decision-grade and drift‑proofed)
  - **G-12 (interface discipline, forcing metadata latch)** strengthened (schema requirements stated; mismatch‑fail rule)
* Target gaps still open (by ID):
  - **G-2 / S5–UE + S5–LOC** (new endpoint class + local interface redesign still open)
  - **G-1, G-12** (residual envelope constant provenance / citations still open globally)
* Key conclusions (5 bullets max):
  1. v35 forcing only lower‑bounds **\(D_B(W)\)** and is **constant‑limited**; it cannot be repurposed to arbitrary endpoints without a transfer lemma.
  2. Therefore, any S5 endpoint \(\Phi_B\) must satisfy **\(\Phi_B\ge D_B(W)\)** or supply a **new forcing lemma** (v35 Remark 12.1).
  3. “Pure” non‑pointwise endpoints (boundary \(L^2\)/energy; or \(E\)-only functionals) are **NO‑GO** unless ENVELOPE adds a forcing transfer lemma with explicit constants/hypotheses.
  4. v35’s repro pack already latches forcing + endpoint metadata; S5 must update these fields whenever endpoint/inequality changes (G‑12 alignment).
  5. Recommended minimal schema additions: record the **dial deviation definition**, **forceability_mode**, and **theorem_reference** in every S5 experiment certificate.

* Paste‑ready manuscript edits (TeX blocks):
  (i) revised lemma/proposition statements
  ```tex
  % --- Insert near Section 12 (S5 frontier), after Remark 12.1 ---
  \begin{lemma}[Forceability transfer by domination]\label{lem:forceability-domination}
  Let $B$ be a $\kappa$--admissible aligned box and $W$ the associated boundary quotient.
  Suppose a boundary endpoint functional $\Phi_B$ satisfies
  \[
    \Phi_B \ge D_B(W)
    \quad\text{for all admissible }(B,W).
  \]
  Then the existing single--box forcing lower bound for $D_B(W)$ implies the same forcing lower bound
  for $\Phi_B$ with no change in the forcing constants.
  \end{lemma}
  ```

  (ii) revised definitions/remarks
  ```tex
  % --- Replace/strengthen Remark 12.1 (or append a final paragraph) ---
  \begin{remark}[Forceability gate for S5 endpoints]\label{rem:s5-forceability-gate}
  The current forcing architecture (Section~8) forces only the dial deviation $D_B(W)$ by an
  $O(1)$ constant up to $\delta$--small deductions. Consequently, any S5 redesign that replaces
  $D_B(W)$ by a different endpoint $\widetilde D_B$ (or $\Phi_B$) is \emph{invalid} unless it proves
  either (i) $\widetilde D_B \ge D_B(W)$ for all admissible boxes/quotients, or (ii) a new forcing
  lemma that lower--bounds $\widetilde D_B$ directly under an off--axis quartet.
  \end{remark}
  ```

  (iii) revised theorem/inequality lines
  ```tex
  % No change to Theorem 11.1 is proposed by RH-FORCE in Batch-5.
  % The enforcement is: if Theorem 11.1's forced object is changed away from D_B(W),
  % then the new forcing-transfer lemma must be inserted and cited.
  ```

* Dependencies on other branches:
  - ENVELOPE/BRIDGE must supply any **new forcing lemma** if they insist on an endpoint \(\Phi_B\) that does not dominate \(D_B(W)\).
  - If ENVELOPE keeps \(D_B(W)\) forced and uses \(\Phi_B\) only as an envelope endpoint, no forcing dependency changes.

* Referee risk notes (anticipated objections + how addressed):
  - **Objection:** “Our \(\Phi_B\) is ‘morally’ controlled by the forced dial deviation.”  
    **Response:** Morality is not admissible. v35 already states the required domination or a new forcing lemma (Remark 12.1). Without it, the forcing half does not attach.
  - **Objection:** “We can probably show an \(L^2\) endpoint is forced because \(W\) is analytic.”  
    **Response:** That would be a *new forcing transfer lemma* and must be written with explicit hypotheses (domain of analyticity, collar width, constants). Until written, \(L^2\)/energy endpoints are NO‑GO for S5 forceability.
  - **Objection:** “The harness already checks the inequality; this is pedantry.”  
    **Response:** G‑12 is precisely about preventing silent theorem↔artifact mismatch. v35 already latches endpoint/forcing metadata; Batch‑5 simply specifies the minimal updates required for S5 experiments.
