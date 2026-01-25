# Integration Notes — Batch 5 (pre‑v36)

Date: 2026-01-24  
Baseline locked: **v35** (2026-01-23)  
Batch‑5 theme: **S5 endpoint redesign triage** (what is *viable*, what is *NO‑GO*, what must be proved next)

---

## 0) Control‑room posture update

Batch‑5 did **not** deliver a positive S5 closure.  
It did deliver **decision‑grade narrowing** of the S5 search space plus **drift‑prevention** inserts:

- Absolute \(L^r\) endpoints on \(|E'/E|\) are **provably NO‑GO** (δ‑inert at the local interface).
- Local‑kernel projection endpoints are **provably NO‑GO** under the current forcing target \(D_B(W)\).
- A generalized budget theorem + “S5 acceptance criterion” is ready to encode so future endpoints cannot be “vibes”.

Net effect: **we are not derailed**; we have *fewer degrees of freedom* and a clearer frontier:
> S5 must be a **forceable cancellation / less‑singular endpoint** (argument‑principle type, or log|E|/BMO‑type), not a norm swap.

---

## 1) Branch Patch Packets (Batch‑5)

### RH‑ABSORB — PASS (budget calculus + acceptance test)
**Delivered (TeX):**
- Theorem `thm:S5-budget` (general endpoint budget; explicit viability condition \(2(p-	heta)\ge q\)).  
- Remark `rem:S5-accept` (mandatory acceptance criterion; forces explicit \((p,	heta,q)\), δ‑uniform constants, and forceability mode).  
- Optional NO‑GO remark: if \(	heta=1\) and \(G(n)\gtrsim n\), then must prove \(p\ge 3/2\).

**Integration decision:** include theorem + acceptance criterion in v36 (mandatory), optional remark (recommended).

### RH‑BRIDGE — PASS (decision‑grade NO‑GO package)
**Delivered (TeX):**
- Lemma `lem:S5_Lp_collapse` + Proposition `prop:S5_Lp_nogo` + Remark `rem:S5_endpoint_implication`.  
Core: any absolute \(L^r(\partial B)\) endpoint forces \(p(r)=	heta(r)=1-1/r\) ⇒ \(p-	heta=0\) ⇒ no η‑shrinking leverage.

**Integration decision:** include as “S5‑NO‑GO: absolute \(L^r\) endpoints” in v36.

### RH‑ENVELOPE — FAIL (no positive endpoint), but supplies **drift‑prevention NO‑GO**
**Delivered (TeX):**
- Lemma `lem:S5-projection-nogo` + consequence remark + Appendix discarded routes D5/D6.  
Core: endpoints that annihilate local kernel span cannot upper bound forced \(D_B(W)\) without changing forcing/endpoint.

**Integration decision:** include projection NO‑GO + Appendix D6; do **not** duplicate \(L^2\) NO‑GO if Bridge package already present.

### RH‑FORCE — PASS (forceability gate hardened)
**Delivered (TeX):**
- Lemma `lem:forceability-domination`.  
- Remark `rem:s5-forceability-gate` (explicit “endpoint change is invalid unless domination or new forcing lemma”).

**Integration decision:** include both near v35 Remark 12.1 (v36 will hard‑gate S5 experimentation).

### RH‑LOCAL — CONDITIONAL (local interface tools; projection math)
**Delivered (TeX):**
- Lemma `lem:Zloc-L2-collar` (improves local blow‑up exponent for \(L^2\) norms: \(	heta=1/2\)).  
- Definition `def:KB-projection` + Lemma `lem:proj-kills-Zloc` + conditioning remark.

**Integration decision:** include lemma `lem:Zloc-L2-collar` (useful local toolkit), and move projection definition/lemma to Appendix D6 as *supporting documentation* (since projection endpoints are now NO‑GO under forcing).

---

## 2) Consolidated state of the S5 frontier (after Batch‑5)

What is now **ruled out** (don’t spend more cycles):
1) “Swap \(\sup_{\partial B}\) to absolute \(L^r(\partial B)\) on \(|E'/E|\).”  
2) “Project out local kernel span to kill the local term, while still targeting forced \(D_B(W)\).”

What remains **the only viable class**:
- Endpoints with **cancellation** (signed functionals, argument variation) and/or **less singular boundary objects** (e.g. \(\log|E|\), BMO‑type).

Hard requirement (forceability):
- S5 endpoint must be forceable by existing \(D_B(W)\) forcing (domination) or must come with a new forcing lemma.

---

## 3) v36 integration target

v36 should be a **guardrail build**:
- Encode S5 acceptance criterion + budget theorem.
- Encode “baseline NO‑GO” lemmas and add Appendix entries so these dead ends stay dead.
- Do **not** claim any new closure.

