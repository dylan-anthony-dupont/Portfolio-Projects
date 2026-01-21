## Adversarial Referee Report 10.0 (v26 → v27)

### A. “Stop‑the‑press” issues (must be fixed for peer review)

1. **Proof status is not machine‑checkable yet.**
   The analytic tail closes only once the paper supplies **explicit numeric enclosures** for the constants it invokes:

   * residual envelope constants (C_1,C_2) (from explicit, quantitative (\zeta'/\zeta) control after de‑singularization),
   * “shape‑only” constants (operator/geometry constants) (C_{\mathrm{up}},C_h'') (and any auxiliary norms).
     Without that, a referee can legitimately say: “the argument is a template, not a proof.”

2. **The tail must be presented as either (i) a complete proof with instantiated constants, or (ii) a formally stated *certified criterion* with a finite, auditable certificate list.**
   Anything in-between reads like “proof by assertion of bounded operator norms.” The paper needs a **single explicit ledger**: a numbered list of quantities + how to certify them + which theorem depends on which bound.

3. **Any “global RH” claim must be conditional unless the constants are pinned and the finite band is closed.**
   The text must not state “hence RH holds” unless you have actually instantiated the constants and performed the certified check (or provided a reproducible certificate).

4. **The “shape-only” step needs a concrete, bounded object.**
   “Boundedness of the Cauchy singular integral on Lipschitz curves” is not enough for a proof unless you:

   * either give explicit numerical upper bounds for the square (by a direct estimate or by a certified computation),
   * or reduce everything to explicit kernels on the square boundary and bound them yourself.

### B. Major technical vulnerabilities (referees will target these)

5. **Outer/Rouché path is correct in spirit, but the paper must be explicit about corner regularity and boundary traces.**
   On a rectangle, harmonic conjugates exist but corner behavior needs a short justification (or a reference with hypotheses that match exactly).

6. **Residual control needs explicit separation from local zero factors.**
   It must be totally clear where the local zero factors are removed and how the remaining terms are bounded. Referees will probe whether any hidden (1/\delta) or (1/\alpha) blow‑up slipped into “(O(\log m)).”

7. **Monotonicity claims (verify at a single height ⇒ all above) must be proved, not asserted.**
   The paper should isolate a lemma that (given the chosen (\delta(m)=\eta\alpha/(\log m)^2)) the upper envelope is non‑increasing in (m) while the lower envelope is non‑decreasing for (m\ge m_\star).

### C. Medium and minor issues

8. **Notation tightness:** (m) vs (t) vs (\gamma) vs (m_j=2\gamma_j) is easy to confuse. A single “conversion box” early in Part II helps.

9. **Tick generator section:** must stay clearly labeled “supplementary; not used in the analytic proof.” The audit script cannot contain “keep verbatim” placeholders if the manuscript is meant to be submission‑ready.

10. **Bibliography should include explicit‑bounds sources** for every quantitative inequality you invoke (even if only used for certification).

---

## Editorial Report 10.0 (what I changed in v27)

* Reframed the tail as a **Certified Closure Theorem**: RH follows from a **finite checklist** of certified inequalities + the (already published) Platt–Trudgian verification up to height (3\cdot 10^{12}).
* Added a **“Certification Ledger” appendix**: a literal list of constants/inequalities and how to certify each with interval arithmetic.
* Strengthened the narrative so every nontrivial step has either:

  * a written proof, or
  * a formally stated “Certification Lemma” with an explicit computational protocol.
* Removed “keep verbatim” placeholders by providing full scripts (audit + tail‑check script templates).
* Made the “global closure” statement conditional unless the certificate is actually instantiated.

---

If you want the next iteration to be a *true* v27 that **unconditionally** states RH (i.e., no “ledger” conditions), the only honest way is to actually *supply the certificate values* (or the Arb output files + hashes) for L1–L4 in Appendix `app:ledger` and then I can “bake them in” so the paper literally contains the numerical enclosures and the verified inequality check as a theorem-level step.
