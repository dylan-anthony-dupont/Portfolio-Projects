# RH‑LOCAL — Batch 4 (Decision Batch, v34 ground truth)
**Callsign:** RH‑LOCAL  
**You own:** local term technology, window policies, zero counting inputs, collar exponent θ, and local reliance on “E entire”.

---

## Executive verdicts (requested PASS/FAIL)

### Primary Task 1 — Short‑interval zero count at \(H(T)=c/\log T\) or \(H(T)\asymp \delta_0(T)=\eta/(\log T)^2\)
**Verdict:** **FAIL / NO‑GO (unconditional, uniform in \(T\), explicit constants)**

- v34’s existing input gives only an **\(O(\log T)\)** upper bound on **unit** windows (Lemma 10.9):  
  \(N(T+1)-N(T-1)\le 1.01\log T + 17\) for \(T\ge 5\), hence \(N_{\rm loc}(m)\ll \log m\) (with \(m=2T\)).【302:10†manuscript_v34.pdf†L1-L51】
- There is **no mechanism in the current v34 toolchain** (explicit RvM-style bounds controlling \(|N(T)-M(T)|\)) that can upgrade this to
  \[
  N(T+H)-N(T-H)\ \le\ A\,H\log T + B
  \]
  **uniformly** for \(H\ll 1\), let alone \(H\asymp 1/\log T\) or \(H\asymp 1/(\log T)^2\). This would require a Lipschitz-type control on the *increment* of the error term (or on \(S(T)\)), which is not available from absolute error bounds.

**Interpretation:** You can have an explicit bound on \(N(T)\) with \(|N(T)-M(T)|\le C\log T + D\), yet still only deduce  
\(N(T+H)-N(T-H)\le M(T+H)-M(T-H)+2(C\log(T+H)+D)\), which is \(\asymp \log T\) when \(H\ll 1\). The error does not scale with \(H\).

---

### Primary Task 2 — Collar blow‑up exponent θ audit (can we get θ<1?)
**Verdict:** **FAIL / NO‑GO for pointwise \(\sup_{\partial B}\) bounds; θ=1 is sharp in proof-grade worst case**

- v34’s collar lemma is:
  \[
  \sup_{\partial B}\left|\frac{Z'_{\rm loc}}{Z_{\rm loc}}\right|
  \ \le\ \frac{N_{\rm loc}(m)}{\kappa\,\delta},
  \]
  i.e. θ=1 in \(\delta\).【302:10†manuscript_v34.pdf†L52-L68】
- Under only κ‑admissibility (distance \(\ge \kappa\delta\) from each zero), this exponent is essentially **optimal**: each term in the sum
  \(\sum_{\rho\in Z(m)} m_\rho/(v-\rho)\) can be as large as \(1/(\kappa\delta)\), and without additional spacing or cancellation hypotheses
  the triangle inequality gives \(N_{\rm loc}/(\kappa\delta)\). Configurations exist (zeros clustered near one side of the box with aligned arguments)
  making the bound saturate in order of magnitude.

**Only plausible way to “beat” θ=1:** change the **envelope endpoint** away from \(\sup_{\partial B}\) (e.g., to an \(L^2(\partial B)\) / energy endpoint),
so the local factor contributes as a lower moment (often \(\sqrt{N_{\rm loc}}/\delta\) in \(L^2\)), not as \(N_{\rm loc}/\delta\).
That is not a “local-only” change; it is a UE/ENVELOPE redesign (consistent with the v34 next-build plan).【507:1†v34_next_build_plan_diff.md†L1-L13】

---

### Primary Task 3 — “E entire” reliance (Λ2/E entireness issue)
**Verdict:** **CONDITIONAL PASS (patch needed for global correctness / hygiene, but local lemmas are salvageable once patched)**

- v34 defines
  \[
  \Lambda_2(u):=\pi^{-u/4}\Gamma(u/4)\zeta(u/2)
  \]
  and then states “\(\Lambda_2\) is entire”.【148:0†manuscript_v34.pdf†L66-L74】【148:0†manuscript_v34.pdf†L75-L83】
  As written, this \(\Lambda_2\) is **not entire**: it inherits poles at \(u=2\) (from \(\zeta(s)\) at \(s=1\)) and at \(u=0\) (from \(\Gamma(u/4)\)).
- The local lemmas (Z-window, collar, Nloc) only require \(E\) to be holomorphic on the boxes considered (far from \(u=0,2\)).
  However, v34 explicitly uses “zeros of the entire function \(E\) are isolated” in collar-admissibility existence logic (and global symmetry statements).
  For proof-grade hygiene, the manuscript should replace \(\Lambda_2\) with an actually-entire completed function.

---

## Detailed reasoning (decision-grade)

### 1) Why short-interval bounds at \(H\asymp 1/\log T\) are NO‑GO from v34’s current inputs

v34’s explicit local count lemma is derived from an explicit absolute error bound for \(N(T)\) (via [7, Thm 1.1]) and yields only a unit-window bound (Lemma 10.9).【302:10†manuscript_v34.pdf†L1-L51】

To obtain \(N(T+H)-N(T-H)\le A\,H\log T + B\) for \(H\ll 1\), you need error control that scales with \(H\), i.e. a bound on increments of the error term:
- Write the exact RvM form:
  \[
  N(T)=M(T)+S(T)+O(1/T),
  \]
  where \(M(T)\) is the smooth main term and \(S(T)\) is the argument term (a step-like oscillatory function).
- Then:
  \[
  N(T+H)-N(T-H)=\bigl(M(T+H)-M(T-H)\bigr)+\bigl(S(T+H)-S(T-H)\bigr)+O(1/T).
  \]
- The main term is \(\asymp H\log T\). But without a Lipschitz-type bound on \(S\), one only has \(|S|\ll\log T\) and therefore
  \(|S(T+H)-S(T-H)|\le 2\sup|S|\ll \log T\), independent of \(H\). This dominates when \(H\ll 1\).

So: **absolute** error bounds for \(N(T)\) (or \(S(T)\)) cannot yield a **short-interval Lipschitz** bound; the required bound is genuinely stronger than what v34 currently imports.

### 2) Why θ=1 is sharp for pointwise collar control

v34’s collar bound is exactly:
\[
\sup_{\partial B}\left|\frac{Z'_{\rm loc}}{Z_{\rm loc}}\right|
\le \frac{N_{\rm loc}(m)}{\kappa\,\delta}.【302:10†manuscript_v34.pdf†L52-L68】
\]

This follows from:
\[
\frac{Z'_{\rm loc}(v)}{Z_{\rm loc}(v)}=\sum_{\rho\in Z(m)}\frac{m_\rho}{v-\rho},\qquad |v-\rho|\ge \kappa\delta\ \text{ on }\partial B.
\]
Any attempt to force θ<1 for the **sup norm** would require either:
- additional cancellation (not available uniformly),
- additional spacing information that limits how many zeros can lie near the boundary with aligned phases (not known unconditionally with explicit constants at the required scale),
- or replacing \(\sup\) by an average / \(L^2\) endpoint (not a local-only change).

Hence, within the **pointwise UE architecture** (sup-based), θ=1 is the correct proof-grade exponent.

### 3) How this matches the v34 UE–Gate obstruction narrative

v34 already states the obstruction cleanly: with pointwise UE exponent \(p=1\), the envelope side contains the δ-inert term \((2C_{\rm up}/\kappa)N_{\rm up}(m)\), and with \(N_{\rm up}(m)=1.01\log m+17\), one-height reduction and absorption fail.【302:10†manuscript_v34.pdf†L65-L68】【302:10†manuscript_v34.pdf†L69-L84】【302:11†manuscript_v34.pdf†L18-L37】

This branch’s conclusion is consistent with that: **local technology cannot fix UE\(_{p=1}\)** by window shrinking alone unless a genuinely new short-interval theorem is introduced.

---

## Paste-ready v34 corrections (local scope)

### A) Fix the “Λ2 is entire” definition (Task 3 — required hygiene patch)

**Problem in v34:** \(\Lambda_2(u):=\pi^{-u/4}\Gamma(u/4)\zeta(u/2)\) is claimed entire but is not.【148:0†manuscript_v34.pdf†L66-L74】

**Minimal proof-grade patch:** redefine the completed width–2 object as the standard *entire* \(\xi\)-type completion.

**Replace v34 §1 (Width–2 normalization) equations (1)–(4) by:**
```tex
Define the width--2 objects
\[
u:=2s,\qquad \zeta_2(u):=\zeta(u/2),
\]
and define the entire completed function
\[
\Xi_2(u):=\xi(u/2)=\frac12\cdot \frac{u}{2}\left(\frac{u}{2}-1\right)\pi^{-u/4}\Gamma(u/4)\zeta(u/2)
=\frac{u(u-2)}{8}\,\pi^{-u/4}\Gamma(u/4)\zeta(u/2).
\tag{1}
\]
Then $\Xi_2$ is entire and satisfies the functional equation
\[
\Xi_2(u)=\Xi_2(2-u).
\tag{2}
\]
We recenter at $u=1$:
\[
v:=u-1,\qquad E(v):=\Xi_2(1+v).
\tag{3}
\]
The functional equation becomes the evenness relation
\[
E(v)=E(-v),
\tag{4}
\]
and complex conjugation gives $E(\bar v)=\overline{E(v)}$.
```

**Local impact:** none adverse. All “zeros of E are isolated” statements become literally correct, and poles at \(u=0,2\) disappear. κ‑admissibility and local factor lemmas become cleaner.

**Remark (optional):** add after (4):
```tex
\begin{remark}
The zeros of $\Xi_2(u)$ (and hence of $E(v)$) are exactly the zeros of $\zeta(s)$ (trivial and nontrivial), with multiplicity.
All boxes used in the tail program lie at heights $m\ge 10$, so only nontrivial zeros occur in the relevant local windows.
\end{remark}
```

### B) Short-interval redesign status (Task 1 — explicitly label NO‑GO)
v34 already has the UE–Gate remark and obstruction lemma. If you want the manuscript to record the “local branch verdict” explicitly, add one sentence to Remark 10.11:

```tex
In particular, no bound of the form $N(T+H)-N(T-H)\le A\,H\log T+B$ with $H\asymp 1/\log T$
is currently available from the explicit $N(T)$ technology used here; obtaining such a bound would require new input controlling
short-interval increments of the error term.
```

---

# MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* **Callsign:** RH‑LOCAL
* **Result classification:** **CONDITIONAL**
  - **FAIL** on (i) “window shrink can realistically reduce \(N_{\rm loc}\) below \(\asymp\log m\) at \(\delta_0\)” with current v34 toolchain,
  - **FAIL** on (ii) “θ<1 achievable in pointwise \(\sup_{\partial B}\) collar control,”
  - **PASS (with patch)** on (iii) “local lemmas remain valid once \(E\) is made genuinely entire.”
* **Target gaps closed (by ID):** none newly closed (this is a decision batch); G‑8 remains an explicit bound, but cannot clear UE‑Gate under \(p=1\).
* **Target gaps still open (by ID):**
  - UE–Gate redesign (effective exponent \(p>1\) or non‑sup envelope endpoint) — Control Room / RH‑ENVELOPE frontier
  - G‑4/G‑5 (global δ‑uniformity + collar interface) beyond local-only scope
* **Key conclusions (5 bullets max):**
  1. No unconditional, uniform, explicit short-interval bound \(N(T+H)-N(T-H)\le A H\log T+B\) at \(H\asymp 1/\log T\) follows from v34’s current explicit \(N(T)\) technology; the error term lacks Lipschitz control.
  2. Under pointwise UE exponent \(p=1\), the local penalty is δ‑inert: \(\delta\cdot (N_{\rm loc}/(\kappa\delta)) = N_{\rm loc}/\kappa\), and with \(N_{\rm loc}(m)\asymp \log m\) this blocks uniform tail closure exactly as v34 records.【302:10†manuscript_v34.pdf†L65-L68】【302:11†manuscript_v34.pdf†L18-L37】
  3. The collar blow-up exponent θ=1 is sharp for \(\sup_{\partial B}\) bounds under κ‑admissibility; θ<1 would require changing the envelope endpoint (e.g., \(L^2\)) rather than local factoring alone.【302:10†manuscript_v34.pdf†L52-L68】【507:1†v34_next_build_plan_diff.md†L1-L13】
  4. v34’s claim “\(\Lambda_2\) is entire” is incorrect as written; redefine the width–2 completion as \(\Xi_2(u)=\xi(u/2)\) to make \(E\) entire and keep the symmetry exact.【148:0†manuscript_v34.pdf†L66-L74】
  5. After the entireness patch, all local lemmas (Z-window, collar, Nloc) remain valid and cleaner, with no dependence on poles.

* **Paste-ready manuscript edits:**
  (i) **revised lemma/proposition statements**
  - None required locally (beyond the entireness patch in the definitions).

  (ii) **revised definitions/remarks**
  - Replace the “Λ2 is entire” definition block in §1 with the \(\Xi_2\) definition provided above (Patch A).
  - Optional one-line remark addition in Remark 10.11 documenting that short-interval bounds at \(H\asymp 1/\log T\) are not obtained from current inputs (Patch B).

  (iii) **revised theorem/inequality lines**
  - None.

* **Dependencies on other branches:**
  - **RH‑ENVELOPE / Control Room:** clearing UE–Gate requires either an effective exponent \(p>1\) or a non‑sup endpoint; local technology cannot supply this alone.
  - **RH‑ABSORB:** absorption remains conditional on UE redesign; local branch confirms no local-only rescue under \(p=1\).

* **Referee risk notes (anticipated objections + how addressed):**
  - **Objection:** “Maybe shrinking the local window makes \(N_{\rm loc}\) bounded.”  
    **Response:** Not provable from v34’s absolute \(N(T)\) bounds; would require new, uniform short-interval increment control. The best current explicit bound is the unit-window \(O(\log T)\) bound in Lemma 10.9.【302:10†manuscript_v34.pdf†L1-L51】
  - **Objection:** “Why can’t θ<1 be proved?”  
    **Response:** The collar estimate is a sum of principal parts; under only a distance lower bound, the worst-case alignment gives \(N/(\kappa\delta)\). Beating θ=1 needs cancellation or an averaged endpoint, neither available in the pointwise sup framework.【302:10†manuscript_v34.pdf†L52-L68】
  - **Objection:** “Your entireness correction is cosmetic.”  
    **Response:** v34 explicitly uses “zeros of the entire function E are isolated” in collar-admissibility arguments; making \(E\) genuinely entire removes a correctness attack vector and aligns the symmetry claims globally.【148:0†manuscript_v34.pdf†L66-L74】
