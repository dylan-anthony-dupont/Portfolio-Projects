# v35 Patch Queue — Batch‑4 (apply to v34 baseline)

This is the **ordered patch list** Control Room will apply when you give “GO v35 build”.

Conventions:
- **Patch IDs**: `P35-...`
- **Risk**: LOW/MED/HIGH (referee risk, not difficulty)
- **Owner**: which branch packet supplies the text
- **Target**: exact section/label in v34 TeX

---

## P35-ENT1 — Entire completion swap (Λ₂ → Ξ₂) + E definition (Risk: HIGH hygiene, low mathematical risk)
**Owner:** RH‑ENVELOPE + RH‑LOCAL (consistent) fileciteturn47file2 fileciteturn47file4  
**Target:** §`sec:width2` (Width‑2 normalization)

**Action:**
1) Replace the definition block:
   - Keep \(\Lambda_2\) as meromorphic completion (optional), but set the working entire object
     \[
     \Xi_2(u):=\xi(u/2)=\frac{u(u-2)}{8}\Lambda_2(u),
     \qquad E(v):=\Xi_2(1+v).
     \]
2) Update any downstream statement “Λ₂ is entire” → correct.
3) Search/replace “E is entire” arguments that are now literally true.

**Acceptance checks:**
- `grep -n "Lambda_2 is entire"` returns **0** matches.
- `grep -n "Since E is entire"` remains okay because E is now entire.

---

## P35-ENT1b — Patch residual log‑derivative identity (Risk: MED)
**Owner:** RH‑ENVELOPE fileciteturn47file2  
**Target:** Lemma `lem:residual-envelope` proof, step “Log-derivative identity in the s-frame”

**Action:**
Replace
\[
E'/E = -\tfrac14\log\pi + \tfrac14\Gamma'/\Gamma((1+v)/4) + \tfrac12\,\zeta'/\zeta(s)
\]
by the corrected identity including the rational completion terms:
\[
E'/E = \Bigl(\tfrac{1}{u}+\tfrac{1}{u-2}\Bigr) - \tfrac14\log\pi + \tfrac14\Gamma'/\Gamma(u/4) + \tfrac12\,\zeta'/\zeta(u/2),
\quad u=1+v.
\]

**Acceptance check:** Lemma statement unchanged; constants ledger updated only by an \(O(1)\) term.

---

## P35-BUDGET — Exponent Budget Theorem (Risk: HIGH, because it changes narrative constraints)
**Owner:** RH‑ABSORB fileciteturn47file0  
**Target:** Immediately after Remark `rem:UE-gate` (or in §12 “Status”)

**Action:**
- Insert `thm:exponent-budget`:
  - Inputs: nominal \(\delta_0=\eta/(\log m)^2\), local majorant \(N_{\rm loc}\ll \log m\), collar blow‑up exponent \(\theta\), UE prefactor exponent \(p\).
  - Conclusion: uniform η‑absorption requires \(p-\theta \ge 1/2\).
- Update Remark `rem:UE-gate` to cite this theorem and state the specialized condition \(p\ge 3/2\) if \(\theta=1\).

**Acceptance check:** Obstruction Lemma `lem:UE-d1-obstruction` becomes redundant or is explicitly labeled as a corollary.

---

## P35-UE-NOGO — Scaling obstruction lemma: “p>1 cannot hold with sup endpoint” (Risk: HIGH)
**Owner:** RH‑ENVELOPE fileciteturn47file2  
**Target:** After Lemma `lem:UE-d1-obstruction` (or after the budget theorem)

**Action:**
- Insert Lemma `lem:UE-scaling-nogo` exactly as provided.

**Acceptance check:** UE frontier text updated: “Need p>1” becomes “Need a non‑sup UE redesign”.

---

## P35-FORCE-NOGO — Single-box forcing is constant-limited (Risk: MED)
**Owner:** RH‑FORCE fileciteturn47file3  
**Target:** After Lemma 8.1 (Short‑side forcing)

**Action:** Insert new lemma + proof sketch bounding \(\Delta\arg Z_{\rm pair}\le 2\pi\) uniformly in \(m\).

---

## P35-FORCE-COMPAT — Forceability criterion remark (Risk: MED)
**Owner:** RH‑FORCE fileciteturn47file3  
**Target:** Near Theorem 11.1 (tail criterion)

**Action:** Insert remark: if endpoint functional changes, must prove \(\Phi_B\ge D_B\) or supply new forcing lemma.

---

## P35-HARNESS — JSON + verifier hardening for constants and endpoint metadata (Risk: LOW/MED, audit)
**Owner:** RH‑FORCE fileciteturn47file3  
**Target:** `v34_repro_pack/` scripts + JSON files (become v35 equivalents)

**Action:**
- Extend tail-check JSON schema to include:
  - forcing constants \(c_0,c,K_{\rm alloc}\) as explicit expressions,
  - `endpoint_functional` string,
  - `forcing_architecture` string.
- Modify `verify_tail_check.py` to print these and assert theorem alignment.

---

## P35-BRIDGE-NOCONV — “No converse” remark on boundary modulus (Risk: HIGH, directional correctness)
**Owner:** RH‑BRIDGE fileciteturn47file1  
**Target:** After Remark 9.3 (meaning of boundary modulus) or after Proposition 9.2

**Action:** Insert remark: \(|W|=1\) on \(\partial B\) does not constrain interior zeros (conformal transport of Blaschke products). Emphasize Prop 9.2 directionality.

---

## P35-BRIDGE-HYGIENE — Patch residual “entire” language if any remains (Risk: LOW)
**Owner:** RH‑BRIDGE fileciteturn47file1  
**Target:** Lemma `lem:zloc-finite` proof and Lemma 10.6 proof, if not already corrected by ENT‑1

**Action:** After ENT‑1, these become automatically correct; only patch if any “entire” usage remains inconsistent.

---

## P35-LOCAL-NOGO-NOTE — Optional short-interval NO‑GO sentence (Risk: LOW)
**Owner:** RH‑LOCAL fileciteturn47file4  
**Target:** Remark `rem:UE-gate` or the “Status” section

**Action:** Add a single explicit sentence: current inputs do not yield short-interval bounds at \(H\ll 1\); shrinking δ cannot force \(N_{\rm loc}\) to be \(o(\log m)\).

---

## P35-FRONTIER-REWRITE — S5 open problem rewrite (Risk: MED)
**Owner:** Control Room synthesis (based on Batch‑4 decisions)  
**Target:** Executive summary + any “next steps” section

**Action:** Rewrite “we need p>1” language to:
- p>1 is structurally impossible for the pointwise sup endpoint class;
- θ=1 is sharp for pointwise collar bounds;
- forcing is constant-limited;
- therefore the sole viable analytic frontier is a non‑pointwise UE redesign that bounds \(D_B(W)\) without δ^{-1} local blow-up.

---

## P35-PATCHLOG — Patchlog + artifact update (Risk: LOW)
**Owner:** Control Room  
**Target:** New `v35_patchlog.md`, update dashboard, zip new repro pack

**Action:** Record each patch ID, location, and resulting label map.

