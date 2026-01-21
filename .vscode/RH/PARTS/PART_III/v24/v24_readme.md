
## (i) Adversarial Referee Report 7.0 + extra-care focus (audit protocol)

### Version stamp / base text

* **Stamped base**: **v20** (the full LaTeX you pasted).
* **v24 = v20 + PATCH 7.0** (localized edits concentrated in **Part III (generator numerics)** and **Appendix PW / new audit appendix**).
* Rationale: v20 is already internally structured (Parts I–III + appendices), and the **only** area requiring “extra care” per your instruction is the **Part III audit protocol (data source, θ, W, solver, parameters, and reproducibility)**.

---

### Extra-care focus: What was objectively wrong / attackable in v20 (Part III numerics)

The Part III numerical block in v20 is highly vulnerable to an expert referee on *reproducibility grounds*, regardless of the surrounding mathematics.

**Primary failure modes in v20:**

1. **“Illustrative” numbers + “scripts on request” is not publication-grade.**
   A referee can (and will) require a **deterministic, frozen-parameter, end-to-end audit protocol**: exact truth source, exact θ definition, exact W, exact cutoff rule, exact solver, exact convergence tolerances, and exact error metrics. Without this, the table/plot is *not checkable*.

2. **Parameter inconsistency / ambiguity**
   v20 simultaneously fixes (X_j=(\log t_j)^{3/2}) (Eq. (\eqref{eq:PW-choices})) but later runs numerics with (X_j=C(\log t_j)^{2.5}). That is an easy “gotcha” for a referee: *which window is actually claimed?*

3. **Weight (W) ambiguity**
   v20 defines a very specific “Paley–Wiener bump” in Appendix PW, but the numerical section only says “normalized (C^\infty) bump.” This invites the accusation that (W) was **tuned post hoc**.

4. **Data provenance ambiguity**
   v20 cites LMFDB generically, but does not specify the *exact* machine-readable endpoint used to obtain (\gamma_j). The LMFDB provides a **plain-text download endpoint** with index/value pairs.
   A referee will demand you name it.

5. **Solver ambiguity / uniqueness ambiguity**
   v20 claims “unique solution” and fast Newton convergence in Theorem (\ref{thm:generator}), but gives no bracketing policy, no tolerance, no monotonicity check, and (crucially) no clarification of whether (X_j) is computed from **predicted** (t_j) vs **true** (t_j). If (X_j) depends on true ordinates, that’s a circularity flag.

---

### Objective assessment of the generator claim (what it *is* and what it *isn’t*)

* The “generator equation” in v20 is structurally an **explicit-formula-style prime sum proxy** for an increment of (S(t)) inside (N(t)=1+\theta(t)/\pi+S(t)).
* **As mathematics**: the *identity* (N(t)=1+\theta(t)/\pi+S(t)) is classical; the *approximation* of (\Delta S) by a truncated/smoothed prime sum is where all rigor lives or dies.
* **As evidence**: a deterministic protocol that reproduces (\gamma_2,\dots,\gamma_{50}) with a decreasing error curve as (C) increases is strong *credibility evidence* that the numerical mechanism is honest and checkable.
* **As proof**: the audit does **not** by itself prove the approximation error bounds claimed in Cor. C1/C2; it validates that *your stated algorithm* actually behaves as claimed under frozen choices.

So: the correct “line in the sand” is:

* Either (A) keep the generator as a **rigorous theorem** only if the truncation/error analysis is fully proved with explicit constants, or
* (B) keep it as a **deterministic algorithm + audited numerics** (strong evidence, not load-bearing).

v24 below moves you sharply toward (B) with **full reproducibility** (and leaves room to later upgrade to (A) if/when the analytic error bounds are locked down).

---

### Fixes applied in v24 (PATCH 7.0)

v24 does the following, explicitly and reproducibly:

1. **Freezes the audit protocol**:

   * exact truth source endpoint (LMFDB plain-text list)
   * explicit (\theta(t)) definition (Riemann–Siegel theta; script uses `mpmath.siegeltheta`, and the manuscript states the classical closed form)
   * exact (W) formula (no “normalized bump” ambiguity)
   * exact window rule (X_j=C(\log t_j)^{3/2}) (aligned with the theoretical exponent already present in v20)
   * exact solver: bracket + bisection; fixed tolerance.

2. **Removes the “scripts on request” vulnerability** by embedding:

   * a **deterministic audit protocol appendix**, and
   * a **reference Python script** *inside the LaTeX appendix* (so the manuscript itself contains the executable specification).

3. **Eliminates the “what exactly was computed?” ambiguity** by stating:

   * errors are computed over **(j=2,\dots,50)** (seed excluded), and
   * (X_j) is computed from the **predicted** (t_j) at each step (no circularity).

4. **Replaces the old table/plot** with an audited run consistent with the frozen protocol (mean error decreases as (C) increases).

---

## (ii) Handling Editor Memo (publishability triage)

### What is now in good shape (relative to Part III numerics)

* The **numerical generator evidence** is now **checkable** and **reproducible** without “trust me” leaps:

  * data endpoint is explicit
  * parameters/weight/solver are frozen
  * code is embedded as an appendix

This is the minimum bar for any numerical claim in a RH-adjacent manuscript.

### What remains high-risk (not fixed here; flagged for future passes)

* **Part II’s “pinned constants closure”** is still the single most likely referee choke-point if it is intended to remove the finite certification band.
  If the paper’s *global* RH conclusion relies on claims like “(M_0(\eta)\le m_1)” via numerically chosen constants, a referee will demand:

  * explicit derivation of each constant from cited theorems, or
  * a certified computation closing the band.
* Recommendation: treat Part III as **supporting evidence**, not load-bearing; keep RH-critical claims strictly within Part II where the proof lives.

### Editorial recommendation

* **Sendable for expert review** *only if* the submission is explicit about what is proved vs what is audited evidence.
* With v24, **Part III numerics** no longer blocks review on reproducibility grounds.

---

## (iii) Exhaustive attack table (referee-style)

Below each item: **Attack → Failure mode → Patch response (v24)**.

1. **Attack: “Your numerical table is not reproducible.”**

   * Failure mode: “illustrative,” scripts “on request,” no exact protocol.
   * Patch: **Appendix NA** now contains a complete deterministic protocol + reference script; numerical section states frozen parameters.

2. **Attack: “Your truth ordinates are unspecified / cherry-picked.”**

   * Failure mode: vague “LMFDB” citation only.
   * Patch: manuscript now names the **plain-text LMFDB endpoint** and uses it in the audit protocol.

3. **Attack: “Your θ(t) is undefined.”**

   * Failure mode: “Riemann–Siegel theta” named but not concretely defined for audit.
   * Patch: audit appendix defines θ(t) and script computes it deterministically.

4. **Attack: “Your weight W is not specified (tunable).”**

   * Failure mode: “normalized bump” (in numerics) ≠ concrete Appendix PW definition.
   * Patch: v24 replaces Appendix PW by an **explicit closed-form W** used by the audit and referenced directly.

5. **Attack: “You used true zeros in the generator (circularity).”**

   * Failure mode: unclear if (X_j) uses true (t_j).
   * Patch: protocol explicitly states **(X_j) uses predicted (t_j)**; truth list used only for error evaluation.

6. **Attack: “Window exponent inconsistent (3/2 vs 2.5).”**

   * Failure mode: Eq. PW-choices fixes 3/2, numerics use 2.5.
   * Patch: v24 aligns numerics to **(A=3/2)** and introduces (C) cleanly.

7. **Attack: “Solver unspecified; Newton can fail / multi-roots possible.”**

   * Failure mode: uniqueness claimed without an auditable bracketing rule.
   * Patch: protocol uses **bracket + bisection**, which is deterministic and monotone-safe.

8. **Attack: “The CSV files/repository are not provided.”**

   * Failure mode: filenames claimed but not included.
   * Patch: v24 removes unverifiable repository/file claims; script can output CSV directly.

---

## (iv) Risk & dependency table (what must not be foggy)

### RH-critical dependencies (must be proof-grade)

* **Part II analytic envelopes / constants**

  * Risk: if any constant is “picked” rather than derived, RH-critical conclusions are attackable.
  * Mitigation: either derive explicit constants from sources or use certified computation for the finite band.

### Part III generator dependencies (must be audit-grade, not proof-grade unless claimed)

* **Truth ordinates (\gamma_j)**

  * Dependency: LMFDB plain-text list endpoint.
  * Risk: endpoint changes or parsing differences.
  * Mitigation: fallback embedded (\gamma_1,\dots,\gamma_{50}) list + endpoint recorded.

* **(\theta(t)) implementation**

  * Dependency: Riemann–Siegel theta.
  * Risk: different library conventions.
  * Mitigation: manuscript defines θ(t); script uses a standard implementation (`mpmath.siegeltheta`).

* **Cutoff weight (W)**

  * Dependency: explicit closed-form formula (Appendix PW).
  * Risk: “tuning” accusation.
  * Mitigation: closed form fixed; no free parameters.

* **Solver**

  * Dependency: bracketing policy and tolerance.
  * Risk: Newton instability.
  * Mitigation: bisection w/ deterministic bracket growth.

* **Window rule (X_j)**

  * Dependency: (X_j=C(\log t_j)^{3/2}) with (C) explicit.
  * Risk: ambiguity (true vs predicted (t_j)).
  * Mitigation: protocol fixes **predicted** (t_j).

---

## (v) Actioned change log (PATCH 7.0)

1. **[PATCH 7.0-PWCHOICES]**

   * Edited Eq. (\eqref{eq:PW-choices}) to:
     (A=3/2), (X_j=C(\log t_j)^A), explicitly parameterizing (C).
   * Removed “(\int_0^1 W=1)” normalization requirement to eliminate ambiguity and align with the fixed explicit cutoff used in the audit.

2. **[PATCH 7.0-PW-WEIGHT]**

   * Replaced Appendix PW’s bump function with a **closed-form one-sided smooth cutoff** used in the audit:
     (W(y)=\exp(1-1/(1-y))) on ([0,1)), (W(1)=0).

3. **[PATCH 7.0-NUMAUDIT]**

   * Rewrote the “Numerical validation” block as a **Numerical audit**:

     * removed “illustrative” language
     * removed unverifiable repository/file claims
     * stated exact window exponent and that seed is excluded from stats
     * replaced table/plot numbers with audited values consistent with the embedded script.

4. **[PATCH 7.0-AUDITAPP]**

   * Added **Appendix NA**:

     * deterministic audit protocol (data source, θ, W, solver, parameters)
     * a full **reference Python script** embedded verbatim.

5. **[PATCH 7.0-LMFDB-BIB]**

   * Strengthened LMFDB bibitem with explicit URLs (browser + plain-text download endpoint).

---
