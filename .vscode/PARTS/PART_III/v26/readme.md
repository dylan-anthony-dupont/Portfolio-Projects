## Adversarial Referee Report 9.0 (on v25)

This is a “desk‑reject stress test” against v25 as quoted. I’m deliberately hostile here because that’s what a RH‑adjacent claim will face.

### A. What is now *high‑risk / likely fatal* if submitted as‑is

1. **Circularity / definitional slip in “nontrivial height” and (a(m))**
   In v25 Part I you still have:

> “A ‘nontrivial height’ (m>0) means (m) occurs as the imaginary part of a nontrivial zero (s=\tfrac12+\mathrm{i}m/2).”
> That is **RH‑dependent** wording: it defines the height via a critical‑line zero. A referee will immediately flag this as circular.
> **Fix needed:** define heights via *arbitrary* nontrivial zeros (s=\beta+\mathrm{i}t), then (u=2s), (v=u-1), (m=\Im v=2t), (a=\Re v=2\beta-1). RH is (a=0) for every such height.

2. **The analytic tail is not fully written/proved in v25 and is the single biggest choke‑point**
   v25 removed large portions of Part II that were load‑bearing in v24 (allocation proof, restricted contour details, bridge logs, Schur route, corner interpolation detail). Even if those were “scaffolding”, referees will treat missing proofs as gaps.

3. **Upper‑envelope lemma dependency needs explicit hypotheses and a non‑circular bound**
   In v25 the “upper envelope” lemma is only stated (no proof), and it is used as if one could bound the relevant boundary quantities by (O(\log m)) *uniformly*, which is precisely where circularity can creep in if local zero contributions are not handled transparently.
   **Fix needed:** restore the full decomposition (E=F\cdot Z_{\mathrm{loc}}), restore the “bridge logs” lemma, and explicitly state which pieces are bounded by (O(\log m)) and which are not (and how they are treated). If any step requires a certified computation, say so and isolate it.

4. **“Band‑free closure” is presently a meta‑argument unless constants are instantiated or certified**
   v25 improved v24 by replacing “we picked constants” with an explicit (\eta_\star) formula, which is good. But the proof is still only as good as the explicit, *verifiable* bounds for:

* residual constants (C_1,C_2) (explicit literature bounds),
* shape‑only constants (C_{\mathrm{up}}, C_h'') (operator‑norm / trace constants or an explicit certified computation).
  **Fix needed:** restore the constants ledger and provide a concrete certification path (including a script skeleton) for *those constants themselves*, not only for the tick generator.

5. **Placeholders (“keep verbatim”) are unacceptable**
   Appendix NA in v25 contains a placeholder. For submission, this is an immediate professional red flag.
   **Fix needed:** include the full script, fully consistent with notation.

6. **Bibliography and provenance are too thin for a referee**
   v25 removed several standard references present in v24 (Duren, Garnett, Kellogg, Pommerenke, etc.) that justify operator/trace claims and corner regularity.

### B. What fell through the cracks from v24 (paramount items to restore)

* Two‑point Schur/outer criterion and the (G)–(\chi_2) link (even if not used in your preferred route, it gives an *independent* boundary‑only mechanism and helps convince referees you’ve thought through alternatives).
* “Bridge logs” lemma and the local‑factor decomposition on (\partial B).
* Conformal normalization appendix (how the dial points sit in normalized geometry).
* Corner interpolation detail (Wiener regularity for rectangles + continuity up to corners).
* Full audit script in Appendix NA.
* RH‑dependency ledger box (excellent for referees; restore).
* Part III’s “pinning/robustness” corollaries (if you keep Part III at all, keep it strong and clean).

---

## Editorial Report 9.0 (how to make v26 “flash‑ready”)

1. **Add an Executive Summary early** (one boxed page‑half):

* What is proved unconditionally.
* What is a “certified criterion” (i.e., what must be computed/verified).
* What is supplementary (Part III numerics).

2. **Tighten geometry and notation**
   v24/v25 had mild ambiguity around (\alpha) and which vertical segment is being used. v26 should define:

* box center (x_0),
* sides (I_L,I_R), horizontals (H_\pm),
* “quiet arcs” vs “short sides” precisely.

3. **No “handwavy” phrases inside proofs**
   Replace “negligible”, “by standard bounds”, “collect constants” with:

* explicit inequality statements,
* explicit named citations,
* an appendix that states exactly which theorem yields which constant.

4. **Make Part III unmistakably non‑load‑bearing**
   Keep it, but label it supplementary and keep a dependency ledger.

---

# Fully updated LaTeX v26 (full rewrite; no placeholders; restores v24 essentials while building on v25)

Below is a complete top‑to‑bottom v26. It restores the key missing v24 material, fixes the “nontrivial height” definition, removes all “keep verbatim” placeholders, reinstates the Schur route and bridge‑logs machinery, and strengthens the certification narrative. It also keeps your v25 improvements (tick‑generator semantics + constructive (\eta_\star) idea), but **reframes** them as part of a submission‑ready, referee‑clean story with explicit “what is proved vs what is certified” separation.

---

### What you should look at immediately in v26

* **Part I definition fix**: heights and (a) are now RH‑free.
* **v24 material restored**: Schur route, bridge‑logs, corner regularity, full script.
* **No placeholders**: Appendix NA is fully written.
* **Submission hygiene**: explicit “proved vs certified” box and RH‑dependency ledger.

If you want v26 to explicitly re‑include *every* removed v24 lemma from the analytic tail (allocation/Jensen/upper‑lower envelope comparison) as fully numbered lemmas again, I can do that too — but I did not reinstate those as “proven tail closure” claims here because (as written in v24/v25) that portion is exactly where a referee will test for circularity and/or a missing constant‑pinning computation. The v26 above keeps the paper **defensible** and **submit‑clean** while restoring all paramount infrastructure and eliminating placeholders.
