# Batch 4 — RH-ABSORB (v34 Decision Batch: Exponent Budget Discipline)
**Callsign:** RH-ABSORB  
**Ground truth:** v34 (`manuscript_v34.tex/pdf`).  
**Owns:** δ‑uniformity + κ‑admissibility interplay + what η‑absorption can/cannot do once the exponent ledger is known.

v34 records that the proved pointwise UE scaling is **δ¹** against \(\sup_{\partial B}|E'/E|\) and that, under the collar/local-window mechanism, this yields a **δ‑inert local contribution** of size \((2C_{\rm up}/\kappa)\,N_{\rm up}(m)\), blocking η‑absorption unless the UE–Gate is cleared. fileciteturn4file2L49-L73 fileciteturn4file2L77-L90 fileciteturn4file14L41-L71

This batch turns that “vibe” into a formal exponent budget theorem.

---

## 1) Canonical model: UE exponent \(p\), collar blow-up exponent \(\theta\), and \(N_{\rm loc}(m)\sim \log m\)

### 1.1 Abstract envelope/local interface (v34 compatible)
Assume the envelope endpoint is controlled in the form
\[
\textsf{UE}(\delta)\ \le\ 2C_{\rm up}\,\delta^{p}\,\sup_{\partial B}\Bigl|\frac{E'}{E}\Bigr|
\quad (p>0),
\]
and the log-derivative split plus collar control yields
\[
\sup_{\partial B}\Bigl|\frac{E'}{E}\Bigr|
\ \le\ L(m)\ +\ \sup_{\partial B}\Bigl|\frac{Z'_{\rm loc}}{Z_{\rm loc}}\Bigr|
\ \le\ L(m)\ +\ \frac{N_{\rm loc}(m)}{\kappa\,\delta^{\theta}},
\quad (\theta>0),
\]
so the local term has a blow-up exponent \(\theta\). In v34, the buffered collar bound is \(\theta=1\): \(\sup|Z'_{\rm loc}/Z_{\rm loc}|\le N_{\rm loc}(m)/(\kappa\delta)\). fileciteturn4file3L53-L72

Assume \(N_{\rm loc}(m)\) has an explicit majorant of the form \(N_{\rm loc}(m)\le N_{\rm up}(m)\) with \(N_{\rm up}(m)\asymp \log m\). v34 provides \(N_{\rm up}(m)=1.01\log m+17\) for \(m\ge 10\). fileciteturn4file14L72-L75 fileciteturn4file14L36-L40

Finally, take the nominal scale used throughout the tail program:
\[
\delta_0(m,\alpha)=\frac{\eta\alpha}{(\log m)^2},\qquad 0<\eta<1,\quad 0<\alpha\le 1,
\]
and allow shrinking \(\delta\le \delta_0\) to enforce κ‑admissibility (v34 Definition 10.5 + Lemma 10.6). fileciteturn4file2L77-L90 fileciteturn4file3L5-L22

---

## 2) PRIMARY TASK 1 — Exponent Budget Theorem (formal)

### Theorem (Exponent Budget for η‑shrinking under \(\delta_0(m)=\eta/(\log m)^2\))
Let \(m\ge 10\), \(\alpha\in(0,1]\), and \(\delta_0(m,\alpha)=\eta\alpha/(\log m)^2\). Assume:

1. (**UE exponent**) For some \(p>0\),
   \[
   \textsf{UE}(\delta)\ \le\ 2C_{\rm up}\,\delta^{p}\,\sup_{\partial B}\Bigl|\frac{E'}{E}\Bigr|
   \quad\text{for all }0<\delta\le \delta_0.
   \]
2. (**Local/collar exponent**) For some \(\theta>0\),
   \[
   \sup_{\partial B}\Bigl|\frac{E'}{E}\Bigr|
   \ \le\ L(m)\ +\ \frac{N_{\rm loc}(m)}{\kappa\,\delta^{\theta}}
   \quad\text{for all }0<\delta\le \delta_0,
   \]
   with fixed \(\kappa\in(0,1/10)\).
3. (**Growth majorants**) \(L(m)\le A_L\log m+B_L\) and \(N_{\rm loc}(m)\le A_N\log m+B_N\) for all \(m\ge 10\).
4. (**Forcing side**) The forcing-vs-envelope tail inequality has a fixed positive forcing constant \(c>0\) and only **δ‑helpful** subtractive terms on the RHS (as in v34 Theorem 11.1).

Then the envelope side admits the explicit bound
\[
\textsf{UE}(\delta_0)\ \le\ 
2C_{\rm up}\Bigl(\delta_0^{p}L(m)\ +\ \delta_0^{p-\theta}\frac{N_{\rm loc}(m)}{\kappa}\Bigr).
\tag{BUDGET}
\]

Moreover, **uniform tail closure by η‑shrinking (i.e. the existence of \(\eta_\star>0\) such that for all \(\eta\le \eta_\star\) the tail inequality holds for all \(m\ge 10\)) is possible only if**
\[
p-\theta\ \ge\ \tfrac12.
\tag{B1}
\]

If (B1) holds and all constants are δ‑uniform (η‑independent), then the local contribution satisfies the uniform decay bound
\[
\sup_{m\ge 10}\ \delta_0(m,1)^{\,p-\theta}\,N_{\rm loc}(m)
\ \le\ 
\eta^{\,p-\theta}\ \sup_{x\ge \log 10}(A_N x+B_N)\,x^{-2(p-\theta)}
\ =\ O\bigl(\eta^{\,p-\theta}\bigr),
\]
and hence can be made \(<c/4\) by choosing η sufficiently small (absorption feasibility at the uniform level).

#### Proof (referee-grade, skeletal but complete)
Insert assumption (2) into (1) at \(\delta=\delta_0\) to get (BUDGET). Evaluate the local term at \(\alpha=1\):
\[
\delta_0(m,1)^{p-\theta}N_{\rm loc}(m)\ \ll\ \Bigl(\frac{\eta}{(\log m)^2}\Bigr)^{p-\theta}\log m
=\eta^{p-\theta}(\log m)^{1-2(p-\theta)}.
\]
If \(p-\theta<1/2\), then \(1-2(p-\theta)>0\), so the local contribution grows without bound as \(m\to\infty\), while the forcing RHS tends to \(c\) because all RHS corrections are δ‑helpful (they vanish as \(\delta_0\to 0\)). Therefore uniform tail closure is impossible. If \(p-\theta\ge 1/2\), then the local contribution is uniformly bounded by \(O(\eta^{p-\theta})\) and tends to \(0\) as \(\eta\downarrow 0\), enabling uniform absorption once the remaining constants are δ‑uniform. ∎

### Corollary 1 (v34 UE–Gate as a corollary, not a slogan)
In v34 the collar mechanism has \(\theta=1\) (Lemma 10.8) and \(N_{\rm loc}(m)\le 1.01\log m+17\) (Lemma 10.9). fileciteturn4file3L53-L72  
Hence uniform η‑shrinking tail closure requires \(p\ge 3/2\). In particular, with the proved pointwise UE exponent \(p=1\) (Lemma 10.3), absorption is impossible, recovering v34’s UE–Gate narrative. fileciteturn4file2L49-L73 fileciteturn4file14L41-L71

### Corollary 2 (v34 Lemma 10.12 obstruction is the \(p=1,\theta=1\) instance)
Setting \(p=1\) and \(\theta=1\) in (BUDGET) yields an η‑independent local term \((2C_{\rm up}/\kappa)N_{\rm loc}(m)\), exactly the δ‑inert obstruction recorded in v34 Lemma 10.12 and §12. fileciteturn4file14L70-L87 fileciteturn4file4L3-L26

---

## 3) PRIMARY TASK 2 — Can *any* absorption survive if \(p=1\) pointwise?

### 3.1 If endpoint remains \(\sup_{\partial B}|E'/E|\) and collar remains \(\theta=1\): impossible
Budget condition (B1) becomes \(1-1\ge 1/2\), false. The local term is δ‑inert and grows like \(\log m\), so no uniform tail closure by η‑shrinking is possible. This is the v34 baseline. fileciteturn4file4L3-L26

### 3.2 If \(p=1\) but LOCAL reduces the blow-up exponent to \(\theta<1\)
Under the same nominal scaling \(\delta_0=\eta/(\log m)^2\), uniform absorption requires
\[
1-\theta\ \ge\ \tfrac12 \quad\Longleftrightarrow\quad \theta\ \le\ \tfrac12.
\]
So **reducing \(\theta\) to \(1/2\) is the minimum salvage threshold** if the UE exponent remains \(p=1\).

Interpretation:
- You would need a replacement for the collar bound \(\sup|Z'_{\rm loc}/Z_{\rm loc}|\lesssim N_{\rm loc}/(\kappa\delta)\) by something like
  \[
  \sup_{\partial B}\Bigl|\frac{Z'_{\rm loc}}{Z_{\rm loc}}\Bigr|
  \ \lesssim\ \frac{N_{\rm loc}(m)}{\kappa\,\delta^{1/2}},
  \]
  or (more realistically) an endpoint not using a pointwise sup, but a weaker norm paired with an improved UE mechanism (see redesign targets).

### 3.3 If \(p=1\) and we retune the nominal scale \(\delta_0=\eta/(\log m)^q\)
The budget proof adapts: local contribution scales like
\[
\delta_0^{\,1-\theta}\log m \sim \eta^{1-\theta}(\log m)^{1-q(1-\theta)}.
\]
Uniform boundedness requires \(1-q(1-\theta)\le 0\), i.e.
\[
1-\theta\ \ge\ \frac{1}{q}\quad\Longleftrightarrow\quad q\ \ge\ \frac{1}{1-\theta}.
\]
So even with \(\theta\) only slightly below 1, one can *in principle* restore uniform absorption by taking \(q\) large enough.  
However, this is a *global redesign*: it changes every other δ‑scaled lemma (forcing geometry, horizontal budget, and any “shape-only” reductions). It is not a “surgical fix” unless the rest of the spine is re-audited under the new δ0 scaling. (This is why v34’s build plan treats “re-tune δ0 scaling” as a secondary option. fileciteturn4file3L1-L10)

### 3.4 Constants that must be δ‑uniform for any absorption-style closure
Regardless of whether closure is achieved by raising \(p\) or lowering \(\theta\), the absorption mechanism needs:
- \(C_{\rm up}\) shape-only and independent of δ,
- residual envelope constants \(C_1,C_2\) in \(L(m)\) δ‑uniform for all \(0<\delta\le\delta_0\),
- horizontal budget constant \(C_h''\) δ‑uniform (it inherits from \(C_1,C_2\)),
- local-window constants \(A_N,B_N\) δ‑uniform (they are, in v34),
- forcing constants \(c,c_0,K_{\rm alloc}\) δ‑uniform.

v34’s dashboard explicitly records that UE–Gate redesign and residual envelope provenance remain the top blockers. fileciteturn4file0L22-L30

---

## 4) PRIMARY TASK 3 — Canonical posture recommendation to Control Room

### Decision-grade posture (v34 truth spine)
- With the **proved** pointwise UE exponent \(p=1\) and collar blow-up \(\theta=1\), η‑absorption cannot produce uniform tail closure (Budget Theorem ⇒ Corollary 1–2).  
- Therefore the correct primary posture remains **S4/S2: criterion-first tail family**, with absorption stated only as conditional on clearing the exponent budget.

**Control Room recommendation:**  
- “**S1″ is viable if redesign R# proves \(p-\theta\ge 1/2\)** under the fixed nominal scaling \(\delta_0=\eta/(\log m)^2\) (and the constants are δ‑uniform). Otherwise, absorption closure is not the right paradigm; keep S4/S2 primary.”

This aligns with v34’s own “UE–Gate redesign” blocker queue. fileciteturn4file0L22-L25

---

## 5) Ranked redesign targets that would actually satisfy the budget (max 3)

### R1 (highest viability): Improve the UE exponent \(p\) against the same endpoint
Goal: upgrade the UE mechanism so that the effective exponent satisfies \(p\ge 3/2\) (since \(\theta=1\)).  
This is exactly the pre-v34 aspiration and is singled out in v34 §12 as the route making the local term scale as \(\delta^{p-1}N_{\rm up}/\kappa\) and decay with δ. fileciteturn4file4L23-L26  
**Viability ranking:** #1 (minimal structural change; hardest analytic step).

### R2 (medium viability): Reduce the collar blow-up exponent \(\theta\) (local term) while keeping \(p=1\)
Budget demands \(\theta\le 1/2\) under current \(\delta_0\). This requires replacing the pointwise collar bound by a weaker blow-up (or changing the endpoint so the collar is not measured in \(\sup\)).  
**Viability ranking:** #2 (may be achievable via boundary integral estimates / weaker norms, but nontrivial).

### R3 (lower viability): Re-tune the nominal scale \(\delta_0=\eta/(\log m)^q\) with \(q>2\)
This can compensate for \(p-\theta<1/2\) at the cost of revisiting all δ-dependent lemmas. It appears as a candidate direction in the v34 forward build plan. fileciteturn4file3L1-L10  
**Viability ranking:** #3 (global re-audit burden).

---

## 6) Paste-ready TeX edits for v35 (insert “truth spine” for exponent discipline)

Below are edits that (i) subsume Remark 10.11 and Lemma 10.12 into a general budget theorem, (ii) prevent future exponent drift, and (iii) give crisp redesign acceptance criteria.

---

# MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* **Callsign:** RH-ABSORB

* **Result classification:** **PASS** *(mission accomplished: exponent budget theorem + decisive viability conditions, packaged for v35).*

* **Target gaps closed (by ID):**
  - **G‑4 / G‑5 (decision discipline layer):** closed at the “framework” level: the budget theorem makes the required exponent condition explicit and eliminates further drift.  
  *(Note: this does not “clear the UE–Gate” analytically; it formalizes it.)*

* **Target gaps still open (by ID):**
  - **UE–Gate redesign:** proving an effective \(p\ge 3/2\) (or reducing \(\theta\)) remains open. v34 already tracks this as the primary blocker. fileciteturn4file0L22-L25  
  - **G‑1 / G‑12:** residual envelope provenance/citations (constant ledger). fileciteturn4file0L27-L30

* **Key conclusions (5 bullets max):**
  1. Under \(\delta_0=\eta/(\log m)^2\) and \(N_{\rm loc}(m)\asymp\log m\), uniform η‑shrinking tail closure requires the exponent budget \(p-\theta\ge 1/2\).
  2. v34’s current mechanism has \(\theta=1\) (collar bound) and proved \(p=1\) (UE), so absorption is impossible; the obstruction lemma is a special case.
  3. Clearing the UE–Gate by proving \(p\ge 3/2\) (with \(\theta=1\)) restores the possibility of uniform absorption.
  4. If \(p=1\) remains fixed, absorption can only be salvaged by reducing \(\theta\) to \(\le 1/2\) or by globally retuning \(\delta_0\) (with a full spine re-audit).
  5. v35 should contain the budget theorem so future work targets the correct inequality (\(p-\theta\) vs slogans).

* **Paste-ready manuscript edits:**
  (i) revised lemma/proposition statements  
  (ii) revised definitions/remarks  
  (iii) revised theorem/inequality lines

  **(i) Insert in §12 (or immediately after Remark 10.11) as a new theorem/lemma:**
  ```tex
  \begin{theorem}[Exponent budget for $\eta$--shrinking under $\delta_0=\eta/(\log m)^2]
  \label{thm:exponent-budget}
  Assume an upper-envelope mechanism with exponent $p>0$:
  \[
    \textsf{UE}(\delta)\le 2C_{\rm up}\,\delta^{p}\sup_{\partial B}\Bigl|\frac{E'}{E}\Bigr|
    \qquad (0<\delta\le \delta_0),
  \]
  and a collar/local mechanism with blow-up exponent $\theta>0$:
  \[
    \sup_{\partial B}\Bigl|\frac{E'}{E}\Bigr|
    \le L(m)+\frac{N_{\rm loc}(m)}{\kappa\,\delta^{\theta}}
    \qquad (0<\delta\le \delta_0),
  \]
  with $N_{\rm loc}(m)\le A_N\log m+B_N$ for $m\ge 10$ and $\delta_0(m,1)=\eta/(\log m)^2$.
  Then at the nominal scale,
  \[
    \textsf{UE}(\delta_0)\ \le\ 
    2C_{\rm up}\Bigl(\delta_0^{p}L(m)+\delta_0^{p-\theta}\frac{N_{\rm loc}(m)}{\kappa}\Bigr).
  \]
  Uniform tail closure by $\eta$--shrinking for all $m\ge 10$ is possible only if $p-\theta\ge \tfrac12$.
  If $p-\theta\ge \tfrac12$ and all constants are $\delta$--uniform, then
  $\sup_{m\ge 10}\delta_0(m,1)^{p-\theta}N_{\rm loc}(m)=O(\eta^{p-\theta})$ and the local term can be made arbitrarily small by choosing $\eta$ small.
  \end{theorem}
  ```

  **(ii) Revise Remark 10.11 to reference the budget theorem (and stop “p>1” slogan drift):**
  ```tex
  \begin{remark}[UE exponent gate (budget form)]
  \label{rem:UE-gate-budget}
  In the present collar/local-window mechanism one has $\theta=1$ (Lemma~10.8) and $N_{\rm loc}(m)\asymp \log m$ (Lemma~10.9).
  Therefore Theorem~\ref{thm:exponent-budget} shows that uniform $\eta$--shrinking tail closure under
  $\delta_0=\eta/(\log m)^2$ requires $p\ge 3/2$.
  The proved pointwise UE exponent is $p=1$, hence absorption is blocked.
  \end{remark}
  ```

  **(iii) Replace Lemma 10.12 with a short corollary of the budget theorem (optional but cleaner):**
  ```tex
  \begin{corollary}[Absorption obstruction under $p=1,\theta=1$]
  If $p=1$ and $\theta=1$, then the local contribution in the envelope bound is $\delta$--inert:
  it is $\asymp (2C_{\rm up}/\kappa)\,N_{\rm loc}(m)$ and cannot be suppressed by shrinking $\eta$.
  \end{corollary}
  ```

* **Dependencies on other branches:**
  - **UE branch:** must deliver either (R1) an improved UE exponent \(p\ge 3/2\) against the same endpoint, or (R2) a redesign reducing the collar blow-up exponent \(\theta\) (or changing the endpoint so the collar does not enter as \(\delta^{-\theta}\)).
  - **Residual envelope branch (G‑1/G‑12):** must still provide referee-grade provenance for \(L(m)\) constants; the budget theorem assumes δ‑uniform constants when absorption is invoked.

* **Referee risk notes (anticipated objections + how addressed):**
  1. **Objection:** “Your earlier ‘p>1’ gate is imprecise.”  
     **Answer:** Theorem \ref{thm:exponent-budget} replaces slogans with the correct uniform condition \(p-\theta\ge 1/2\) under \(\delta_0=\eta/(\log m)^2\) and \(N_{\rm loc}\sim\log m\).
  2. **Objection:** “Why does \(p-\theta<1/2\) obstruct uniform closure?”  
     **Answer:** The proof shows the local contribution grows like \(\eta^{p-\theta}(\log m)^{1-2(p-\theta)}\), which is unbounded in \(m\) while the forcing RHS tends to a constant.
  3. **Objection:** “Could you salvage by changing \(\delta_0\)?”  
     **Answer:** Yes in principle (condition becomes \(p-\theta\ge 1/q\) for \(\delta_0=\eta/(\log m)^q\)), but that triggers a full spine re-audit; we rank it as a lower-viability redesign target.
