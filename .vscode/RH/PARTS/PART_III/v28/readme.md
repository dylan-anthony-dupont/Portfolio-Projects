## Adversarial Referee Report 11.0 (run on v27 → demands for v28)

### A. Stop‑ship issues in v27 (auditor/referee blockers)

1. **The “ledger criterion” is still not a proof artifact**
   v27 cleanly *defines* what must be certified, but it **does not include** any certified constant enclosures nor a deterministic one‑height inequality printout. A referee cannot audit “Ledger” without external files that are not cryptographically pinned.

2. **Part I circularity is still structurally present**
   v27 explicitly states that the definition of “nontrivial height” is RH‑dependent. Even if this is acknowledged, it is a formal **circularity smell** in the exposition. The paper must treat (m) as a free real parameter and only *associate* (m=2t) when a zero (s=\beta+it) is assumed.

3. **Bridge 1 uses an a.e. boundary‑trace argument where pointwise continuity is required**
   If the conclusion is “(W) is constant,” the proof must route through:

   * continuity up to (\partial B),
   * pointwise unimodularity (|W|=1) on (\partial B),
   * and **zero‑freeness** (so (1/W) is holomorphic) + maximum modulus applied to both (W) and (1/W).
     The “a.e.” boundary trace pathway is not audit‑grade here.

4. **(t_1) conflates two different roles**
   v27 uses “(t_1) = first zero height” as a threshold for the digamma–cotangent comparison in hinge monotonicity. That is not the right object. A proof needs a **hinge threshold** (t_{\mathrm{hinge}}) that comes from a monotonicity estimate, and separately the **first zero ordinate** (t_{\mathrm{first}}) (an external certified constant).

5. **(\mathcal Z_{\mathrm{loc}}) finiteness is used but not stated**
   A referee will flag the local product (\Zloc) unless a short lemma states: in each finite vertical window, only finitely many zeros occur, hence (\Zloc) is a finite product and (F=E/\Zloc) is well‑defined.

6. **(W) is used as a main‑line object while outer factorization is described as “optional”**
   If the analytic core uses (W) to express the boundary‑phase budget, then (G_{\mathrm{out}}) and (W) must be **defined unconditionally** (whenever (E\neq0) on (\partial B)), and their properties must be declared in the main line.

7. **Monotonicity and worst‑(\alpha) reductions need explicit derivatives**
   “Routine derivative check” is not submission‑grade. The paper must show the derivative signs in-line, at least for the final tail inequality functions.

### B. What v28 must do

* **Bake the certificate**: explicit numeric enclosures for all constants used in the tail inequality, a deterministic one‑height check with printed interval bounds, and cryptographic pinning (SHA‑256) of the certificate files.
* **Repair the exposition**: remove RH‑dependent definitions, strengthen Bridge 1, separate (t_{\mathrm{hinge}}) and (t_{\mathrm{first}}), and add (\Zloc) finiteness lemma.
* **Make “audit path” single‑shot**: a referee should be able to hash two files, run one verifier script, and see the printed interval inequality.

---

## Editorial Report 11.0 (what changed from v27 → v28)

* **Certificate baked in** (Appendix D):

  * A single **Certificate Table** with explicit numeric intervals for (C_1,C_2,C_{\mathrm{up}},C_h'').
  * A deterministic **one-height inequality check** at (m=6\cdot 10^{12}), (\alpha=1), printed as interval bounds with strict separation ( \mathrm{LHS}*{\max}<\mathrm{RHS}*{\min}).
  * Two certificate files **pinned by SHA‑256** and embedded inline; a deterministic verifier script (also hashed) is embedded and referenced.
* **Part I circularity removed**: “height parameter” (m) is RH‑free; only when assuming a zero (s=\beta+it) do we set (m=2t) and (a=2\beta-1).
* **Bridge 1 fixed**: replaced “a.e.” trace with a continuity + zero‑free maximum‑principle argument (apply to (W) and (1/W)).
* **(t_{\mathrm{hinge}}) separated from (t_{\mathrm{first}})**: hinge monotonicity uses an explicit analytic threshold (t_{\mathrm{hinge}}); the first zero ordinate remains an external certified datum.
* **(\Zloc) finiteness lemma added**.
* **(W) definition moved to main line**: outer factorization is no longer described as optional where (W) is used.
* **Worst‑(\alpha) and monotonicity lemmas strengthened**: explicit derivative computations are included (no “routine check” handwave).

---

## Certificate files

The exact certificate artifacts/files used in Appendix D (matching the in-paper SHA-256) can be found in the v28 folder on VS code in your projects repo.