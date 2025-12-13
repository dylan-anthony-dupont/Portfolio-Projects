Here are the v29 deliverables (LaTeX + updated, self-consistent certificate bundle + hardened generator/verifier):

# Adversarial Referee Report 12.0 (v28 → v29)

## A. Stop‑ship logical crack fixed

**Issue (v28):** the paper *stated* an upper-envelope bound in terms of (\sup_{\partial B}|E'/E|), but *then* substituted the residual envelope (C_1\log m+C_2) (which is a bound for (F'/F), not for (E'/E)) when forming the tail inequality and the certificate computation. That is an audit-failing mismatch: a referee can point out the chain “Lemma uses (E'/E) → certificate uses (F'/F)” is not justified.

**Fix (v29):** Lemma “Upper envelope” is rewritten explicitly in **residual form**, i.e. it is stated in terms of (\sup_{\partial B}|F'/F|). The tail inequality and the certificate now match the lemma as stated. This removes the most damaging “fell through the cracks” inconsistency.

## B. Certificate bundle was not self-consistent; now it is

**Issue (v28):**

* `tail_certificate.json` could drift from what the verifier actually recomputes; the verifier did not validate that the printed/embedded certificate fields were truly *generated from* the hashed constants by a deterministic procedure.
* The verifier used ordinary floating point and did not implement a strict, directed-rounding interval check.

**Fix (v29):**

* Added **two-stage architecture**:

  1. `generate_tail_certificate.py` deterministically generates `tail_certificate.json` from `constants.json` using directed-rounding **Decimal** interval arithmetic and a fixed (\pi) enclosure.
  2. `verify_tail_certificate.py` regenerates a fresh certificate in a temp file and checks that key fields match exactly, and checks the strict inequality `lhs.hi < rhs.lo`.
* All files are **SHA-256 pinned** in Appendix D, and the verifier output is printed verbatim in the paper.

This closes the “certificate is cosmetic” loophole: now the certificate is a *checked output* of the generator.

## C. “Interval arithmetic” was not actually interval arithmetic; now it is (in the verifier)

**Issue (v28):** numeric “intervals” were produced with float arithmetic; a referee can (rightly) object that outward rounding is not guaranteed.

**Fix (v29):** generator uses Python’s `decimal` module with `ROUND_FLOOR / ROUND_CEILING` context switching for every operation, plus an explicit two-sided enclosure for (\pi). The resulting enclosures are stored as decimal strings in JSON to avoid any JSON-float ambiguity.

## D. “Omitted for brevity / as in” sections removed

**Issue (v28):** the tick-generator appendix was explicitly “omitted”; user’s requirement forbids that.

**Fix (v29):** tick-generator audit script is fully embedded (and hashed) in Appendix D.6, and the supplementary section is fully written.

## E. Audit protocol hardened

**Issue (v28):** audit steps were described but the bundle did not prove that the *embedded* results were exactly what the verifier checks.

**Fix (v29):**

* Appendix D includes:

  * certificate table,
  * recorded inequality in “LHS ≤ … < … ≤ RHS” form,
  * file hashes,
  * verifier output,
  * full embedded contents of all bundle files.

A referee can reproduce in a single command and compare directly to the printed output.

---

# Editorial Report 12.0 (v28 → v29)

## 1) Proof narrative tightened where referees attack first

* Explicit “Executive Proof Status” now states precisely what is proved where and what must be audited (and how).
* The proof’s “tail” is explicitly a *one-height certified inequality check* plus monotonicity and worst-(\alpha) reductions.

## 2) Definitions moved to “before first use”

* (m=2t) conversion box and (m_{\mathrm{band}}) definition appear before the first tail statement.
* (F=E/Z_{\mathrm{loc}}) appears before any residual bounds are used.

## 3) Certificate embedded and internally consistent

* The paper prints the exact inequalities and embeds all files.
* SHA-256 values updated to match the updated files.

## 4) No remaining “verbatim as / see v27” placeholders

* Everything needed for audit is in-text or embedded in appendices.

---
