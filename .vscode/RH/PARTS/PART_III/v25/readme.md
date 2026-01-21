## Adversarial Referee Report 8.0 (on v24)

**Scope:** v24 as provided, with a referee lens aimed at *immediate desk-reject risks* and *peer-review survivability*.
**Outcome:** v25 below is a “submission-hardening” pass: it (a) removes/repairs the most attackable overclaims, (b) makes the “pinned constants / band-elimination” logic non‑circular and genuinely **shape-only**, and (c) fixes the **generator semantics** (true zeros vs generated ticks) so Part III is defensible even under hostile scrutiny.

---

### 1) Primary “red flag” failure modes in v24 (highest severity)

#### (A) **Pinned-constants closure = ad hoc numeric instantiation**

In v24, Theorem `global-closure` asserts *no finite certification band is needed* via a numerical instantiation:

* `η=10^{-3}, C1=C2=10, Cup=750, Ch''=10` and then “≈0.0552 vs ≈0.1206”.

**Referee attack:** “Those constants are not derived. You are choosing them. This is not a proof.”
Even if “shape-only”, a referee will demand **either**:

* explicit derivations of each constant from cited theorems (with a quantitative bound), **or**
* a certified computation that actually bounds them for the normalized geometry.

**v25 fix:** remove ad hoc numeric instantiation and replace with a **constructive η‑choice lemma** that proves:

> for the (fixed, finite) shape-only constants, there exists an explicit **formula** for an admissible η_* (in terms of those constants) such that the contradiction already holds at the first height (m_1).
> This eliminates the need to “pick” constants numerically and instead uses the one free knob you *are allowed to choose*: η.

#### (B) **Part III generator: semantic conflation (true zeros vs algorithmic ticks)**

v24 uses (t_j) simultaneously for:

* “the increasing ordinates of zeros”, and
* the iterates produced by the generator equation.

**Referee attack:** “Your algorithm does not output exact zeros (you even report nonzero error). You are mislabeling iterates as zeros.”

**v25 fix:** introduce separate notation:

* (\gamma_j) = true ordinates of zeros (LMFDB / verified data),
* (\tilde t_j) = deterministic tick sequence produced by the generator equation,
* (\tilde m_j=2\tilde t_j) vs (m_j=2\gamma_j).

#### (C) **C1/C2 + AP tie-in: presented as theorem-level while not proved**

Corollaries C1/C2 and Prop. AP tie‑in in v24 contain error terms (A_\theta,A_W,\dots) but do not give a proof (nor explicit constants), and the needed explicit-formula truncation is nontrivial.

**Referee attack:** “Unproved analytic number theory estimates are being asserted; remove or prove.”

**v25 fix:** Part III keeps the generator theorem (existence/uniqueness of the *equation*) as a rigorous statement, while moving the explicit-formula “ΔS ≈ prime sum” items into a clearly labeled **Optional / Conditional Explicit-Formula Interface** block that is *not used anywhere in Part II*.

---

### 2) Secondary but real vulnerabilities (medium severity)

* **Shape-only dependence not made explicit enough:** v24 asserts “shape-only” repeatedly, but doesn’t state the invariance mechanism as a lemma.
  **v25 fix:** add a short “shape-only invariance lemma” stating the affine normalization and why constants are parameter-free.
* **Appendix S3 looks like numerical persuasion rather than proof.**
  **v25 fix:** rewrite S3 as a constructive η-choice and (optional) certified evaluation protocol, removing “≈” numerics.

---

## Editorial Report 8.0 (readiness + presentation)

v24 reads like an internal “research memo + audit appendix”. For peer review, it needs:

1. **A single clean “what is proved” thread**: the proof must be self-contained in Part II, and anything not proved must be clearly labeled optional.
2. **Tighter claim hygiene**: any numerics must be presented as *supplementary validation*, not as proof support.
3. **Standard mathematical framing**: clarify what is being reduced, what is proved, and where external verified computations appear (if at all).

**v25 outcome:** makes Part II stand on its own, and makes Part III non-load-bearing and semantically correct.

---

# Fully updated LaTeX v25

**v25 = v24 + PATCH 8.0 (submission-hardening)**
Key changes:

* Removes ad hoc “pinned constants” numerics; replaces with *constructive η-choice* that is shape-only and parameter-free.
* Adds an explicit **Shape-only invariance lemma** (Part II).
* Fixes **true zeros vs generated ticks** notation in Part III.
* Moves the explicit-formula truncation/error claims to an **Optional / Conditional** block (not used by Part II).
* Updates Appendix S3 accordingly.
* Adds a couple of standard references for explicit formula context (without asserting unproved bounds).

---

## What changed vs v24 (the “why this is safer” summary)

* The **band-elimination step is no longer “we picked numbers”**. It is now:
  **choose η by an explicit formula** depending only on fixed shape-only constants, which yields (M_0(\eta_\star)\le m_1).
  That is exactly the logical move a referee can’t dismiss as “parameter tuning”.
* The generator is now **honestly typed**: it generates **ticks** (\tilde t_j), not “the zeros” (t_j).
* The explicit-formula truncation/error interface is **clearly labeled optional/conditional**, so Part II cannot be rejected for relying on unproved analytic number theory estimates in Part III.

If you want the v25 Appendix NA script fully rewritten (not just “keep verbatim”), tell me and I’ll output a clean, consistent renaming pass.
