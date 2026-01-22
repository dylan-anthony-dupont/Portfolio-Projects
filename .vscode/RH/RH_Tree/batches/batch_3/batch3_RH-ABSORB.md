# Batch 3 — RH-ABSORB (UE‑Gate Decision)  
**Callsign:** RH-ABSORB  
**Ground truth:** v33 only (`manuscript_v33.tex/pdf`).  
**Primary target:** Re‑evaluate **G‑4 (δ‑uniform absorption)** under the **UE‑Gate** and issue an **S1′ viability** decision.  
**Secondary:** If S1′ fails, propose a successor posture (**S4**) and v34‑ready status edits.

---

## 1) UE‑Gate: what δ‑exponent is actually supported by a proof?

### 1.1 v33 states UE exponent \(p=3/2\) (claimed)
v33 Lemma **“Upper envelope bound (outer‑aligned form)”** states
\[
\sum_{\pm}|W(v_\pm)-e^{i\varphi_0^\pm}|
\ \le\ 2C_{\rm up}\,\delta^{3/2}\,\sup_{\partial B}\Big|\frac{E'}{E}\Big|.
\tag{UE-claimed}
\]

### 1.2 The v33 proof as written only supports \(p=1\) (δ, not δ^{3/2})
In the proof, the δ‑tracking steps are explicitly enumerated:

- boundary evaluation via Poisson kernel: factor \(\delta^{-1/2}\),
- Poincaré/Wirtinger on \(\partial B\): factor \(\delta\),
- \(L^2\to\sup\) on \(\partial B\): factor \(\delta^{1/2}\).

Multiplying the stated scale factors gives:
\[
\delta^{-1/2}\cdot\delta\cdot\delta^{1/2}=\delta^1.
\]

Therefore, the proof chain supports at best
\[
\sum_{\pm}|W(v_\pm)-e^{i\varphi_0^\pm}|
\ \lesssim\ 2C_{\rm up}\,\delta\;\sup_{\partial B}\Big|\frac{E'}{E}\Big|
\tag{UE-proven}
\]
with the same shape‑only constant package (up to harmless absolute factors).

### 1.3 UE‑Gate answer
- **Best proven exponent:** \(\boxed{p=1}\).
- **Status of \(p=3/2\):** **not proven** as currently written (a δ‑power mismatch between lemma statement and the recorded δ bookkeeping).

---

## 2) Task A — S1′ viability under both UE regimes

Let the UE bound be of the form
\[
\text{dial deviation}\ \le\ C_{\rm up}\,\delta^{p}\,\sup_{\partial B}\Big|\frac{E'}{E}\Big|,
\]
and recall the post‑pivot collar split gives
\[
\sup_{\partial B}\Big|\frac{E'}{E}\Big|
\ \le\ L(m)\ +\ \frac{N_{\rm up}(m)}{\kappa\delta},
\]
with \(N_{\rm up}(m)\asymp \log m\) (v33 gives an explicit \(N_{\rm up}(m)=1.01\log m+17\)).

Then the UE contribution to the tail inequality has the structure
\[
C_{\rm up}\Big(\delta^{p}L(m)\ +\ \delta^{p-1}\frac{N_{\rm up}(m)}{\kappa}\Big).
\tag{UE→TAIL(p)}
\]

### Case 1: UE \(p>1\) (e.g. \(p=3/2\) survives)
**Absorption requirements from ENVELOPE:** exactly as in Batch‑2: Lemma “residual envelope” must supply δ‑uniform constants \(C_1,C_2\) for \(L(m)=C_1\log m+C_2\), valid for all \(0<\delta\le\delta_0\) (κ‑admissible shrink included). Then all coefficients in the absorption inequality are η‑independent.

**Proof‑grade absorption closure theorem (final form):**

> **Theorem (S1′ Tail Closure under UE \(p>1\)).**  
> Assume:  
> (i) UE bound holds with exponent \(p>1\) and shape‑only \(C_{\rm up}\);  
> (ii) residual envelope lemma holds with absolute \(C_1,C_2\) uniformly for all \(m\ge 10\), \(\alpha\in(0,1]\), and all κ‑admissible \(0<\delta\le\delta_0(m,\alpha)=\eta\alpha/(\log m)^2\);  
> (iii) local window majorant \(N_{\rm up}(m)\) is explicit and δ‑independent;  
> (iv) forcing constants \(c,c_0,K_{\rm alloc}\) are absolute.  
> Then there exists \(\eta_\star>0\) such that for all \(\eta\in(0,\eta_\star]\) the tail inequality holds for all \(m\ge 10\) and all \(\alpha\in(0,1]\), hence no off‑axis quartets occur at any height \(m\ge 10\).

**S1′ viability under Case 1:** **YES (conditional on ENVELOPE δ‑uniformity)**.

---

### Case 2: UE \(p\le 1\) (δ¹ or worse)
This case is decisive because the **local term becomes δ‑inert** (or worse):

- If \(p=1\): \(\delta^{p-1}=\delta^0=1\), so UE→TAIL contributes a term \(\asymp \frac{C_{\rm up}}{\kappa}\,N_{\rm up}(m)\sim \frac{C_{\rm up}}{\kappa}\log m\) independent of η.
- If \(p<1\): \(\delta^{p-1}=(\eta\alpha/(\log m)^2)^{p-1}\) blows up as \(m\to\infty\).

**Referee‑grade obstruction lemma (clean consequence check):**

> **Lemma (Obstruction: no uniform tail closure when \(p\le 1\)).**  
> Suppose \(N_{\rm up}(m)\ge c_3\log m\) for all sufficiently large \(m\), and \(\delta_0(m,\alpha)=\eta\alpha/(\log m)^2\) with fixed \(\eta>0\).  
> If the UE contribution to the tail inequality contains a term of size  
> \[
> \ge \ C\,\delta^{p-1}\,N_{\rm up}(m)
> \]
> with \(p\le 1\) and \(C>0\) independent of \(m\), then for any fixed forcing constant \(c>0\) the tail inequality cannot hold for all large \(m\) (even after δ‑shrinking), because the LHS grows at least like a positive power of \(\log m\) while the RHS tends to \(c\) as \(m\to\infty\).

**Conclusion:** Under \(p\le 1\), **η‑absorption cannot close** the tail: the local penalty term cannot be made small by shrinking η.

**S1′ viability under Case 2:** **NO**.

---

## 3) UE‑Gate verdict for v33 as it stands
From §1, the **best proven** UE exponent is \(\boxed{p=1}\).  
Therefore, applying Case 2, the η‑absorption tail closure **does not survive** under the UE exponent actually supported by the proof.

**Required truth posture:** v33’s S1′ absorption closure is **conditional on proving a UE exponent strictly greater than 1** (or otherwise eliminating the δ‑inert local penalty).

---

## 4) Task B — Successor posture if S1′ fails (S4)

### S4 (recommended): “Criterion‑first spine; absorption demoted to conditional corollary”
**Description (1–2 paragraphs):**  
Adopt the **S2/v30–v31 criterion posture** as the primary closure mechanism: the manuscript proves a certified, fully auditable criterion (finite set of inequalities + verified front‑end), and the RH conclusion is conditioned on either (i) certified constant provenance or (ii) explicit computation/verification. v33’s post‑pivot improvements (correct object \(E'/E\), collar policy lemmas, explicit \(N_{\rm loc}\) bound, restored \(K_{\rm alloc}\)) remain reusable, but η‑absorption is treated as a *future improvement* contingent on passing the UE‑Gate.

**New gaps created (if promoted to main spine):**
- **G‑S4‑1:** explicit computational verification scope definition (what finite band / what certificate conditions).
- **G‑S4‑2:** certificate ↔ theorem alignment (strict parsing; already tracked as G‑12 in Phase‑2 language).
- **G‑S4‑3:** constants provenance ledger completeness (G‑1).

**Reusable v33 packages:**
- forcing package (with restored \(K_{\rm alloc}\)),
- local split + κ‑admissibility lemmas (non‑circular shrink + monotonicity),
- explicit local zero counting bound \(N_{\rm up}(m)\),
- the post‑pivot alignment “no residual proxying” architecture (keeps the spine honest).

### Alternative mechanisms (max 2; viability ranking)
1) **(Highest)** Prove UE exponent \(p>1\) (restore \(p=3/2\)) by a new analytic argument (this re‑enables S1′).  
2) **(Lower)** Replace absorption by a computation‑assisted closure (S4/S2), keeping the analytic structure but removing dependence on UE \(p>1\).

---

## 5) Task C — v34‑ready “Status posture” remark (truthful, audit‑grade)

A v34 status remark must explicitly name the UE‑Gate as decisive and prevent “proof tone” drift.

Suggested paste‑ready remark is in the Patch Packet.

---

# MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* **Callsign:** RH-ABSORB

* **Result classification:** **FAIL** *(for S1′ under the UE exponent actually supported by the current proof; conditional salvage exists if UE is upgraded to \(p>1\)).*

* **Target gaps closed (by ID):**
  - None closed in this batch; this is a decision batch establishing the UE‑Gate obstruction.

* **Target gaps still open (by ID):**
  - **G‑4** remains open **because the UE exponent required for absorption (p>1) is not currently proved.**  
  - *(G‑5 was previously handled by the κ‑policy lemmas; not re‑audited here.)*

* **Key conclusions (5 bullets max):**
  1. v33’s UE proof chain supports at best \(p=1\), not the stated \(p=3/2\).  
  2. If \(p\le 1\), the local collar penalty becomes δ‑inert (\(\sim \log m\)) and η‑absorption cannot close the tail uniformly.  
  3. Therefore S1′ (η‑absorption tail closure) is **not viable** under the currently proved UE exponent.  
  4. S1′ becomes viable again if and only if UE is upgraded to \(p>1\) (e.g., a valid proof of δ^{3/2}).  
  5. v34 should adopt a criterion‑first posture (S4/S2) unless the UE‑Gate is cleared.

* **Paste-ready manuscript edits:**
  (i) revised lemma/proposition statements  
  (ii) revised definitions/remarks  
  (iii) revised theorem/inequality lines

  **(i) Add an explicit “UE‑Gate” note immediately after Lemma (Upper envelope):**
  ```tex
  \begin{remark}[UE--Gate (δ-exponent)]
  The tail closure by $\eta$--absorption requires an upper-envelope exponent $p>1$ so that the local
  collar term contributes $\delta^{p-1}N_{\rm up}(m)$ with a positive δ-power.
  The present proof of Lemma~\ref{lem:upper-envelope} yields a δ-exponent $p=1$ under the recorded
  bookkeeping, while the statement claims $p=3/2$. Clearing this UE--Gate (establishing $p>1$) is the
  decisive open item for the absorption closure.
  \end{remark}
  ```

  **(ii) Add a v34 “Status posture” remark (e.g., in the Executive Proof Status section):**
  ```tex
  \begin{remark}[Status posture (v34)]
  The manuscript presently establishes a certified criterion for tail closure. The $\eta$--absorption
  closure is conditional on clearing the UE--Gate: a proof of an upper-envelope δ-exponent $p>1$.
  Under the exponent $p\le 1$ supported by the current upper-envelope derivation, the local collar
  penalty is δ-inert and uniform tail closure by absorption is impossible.
  \end{remark}
  ```

  **(iii) (Optional, if you want to make the obstruction explicit) add a lemma in the tail section:**
  ```tex
  \begin{lemma}[Obstruction to absorption if $p\le 1$]
  If the upper-envelope contribution contains a term $\gtrsim \delta^{p-1}N_{\rm up}(m)$ with
  $N_{\rm up}(m)\ge c_3\log m$ for large $m$ and $p\le 1$, then for fixed forcing constant $c>0$
  the tail inequality cannot hold for all sufficiently large $m$ at $\delta_0=\eta\alpha/(\log m)^2$.
  \end{lemma}
  ```

* **Dependencies on other branches:**
  - A dedicated **UE branch** (or RH‑ENVELOPE if owning UE) must either:
    1) prove a genuine UE exponent \(p>1\) (restore δ^{3/2}), **or**
    2) propose a replacement tail closure mechanism that eliminates the δ‑inert local penalty.
  - If S4/S2 becomes primary, certificate/provenance branches own the closure (G‑1 / G‑12).

* **Referee risk notes (anticipated objections + how addressed):**
  1. **Objection:** “Your proof claims δ^{3/2}, but the bookkeeping yields δ.”  
     **Answer:** the UE‑Gate remark surfaces this explicitly; the manuscript must not claim absorption closure until \(p>1\) is proved.
  2. **Objection:** “If UE exponent is only δ, absorption cannot work.”  
     **Answer:** the obstruction lemma formalizes this: the local penalty becomes δ‑inert and grows like \(\log m\), defeating fixed forcing \(c\).
  3. **Objection:** “You still sound like you proved RH.”  
     **Answer:** the v34 status posture remark prevents proof‑tone drift and correctly classifies absorption as conditional.
