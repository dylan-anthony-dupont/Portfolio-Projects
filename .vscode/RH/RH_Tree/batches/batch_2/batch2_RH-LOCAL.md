# RH‑LOCAL — Batch 2 (v33 base)
**Deliverable:** `batch2_RH-LOCAL.md`  
**Primary targets:** G‑8 integration audit (HIGH), G‑11 front‑end packaging (MED), citation hygiene supporting G‑12 (MED)  
**Ground truth:** `manuscript_v33.tex` (checked directly).

---

## Task A (HIGH) — Audit v33’s `N_{\rm loc}` mapping (definition ↔ bound ↔ plug‑in)

### A1) Local window definition in v33
v33 defines the **local window** (zeros of \(E\) in the centered \(v\)-plane) as:
\[
Z(m):=\{\rho:\ E(\rho)=0,\ |\Im\rho - m|\le 1\},
\]
with multiplicity, and defines:
\[
Z_{\rm loc}(v)=\prod_{\rho\in Z(m)}(v-\rho)^{m_\rho},\qquad F(v):=\frac{E(v)}{Z_{\rm loc}(v)}.
\]
**Location:** v33 §“Local factor and finiteness”, eqs. `\eqref{eq:Z-window}`–`\eqref{eq:F-def}`.

✅ **Match to Batch‑1 bound:** This is exactly the window assumed in the Batch‑1 RH‑LOCAL derivation: width \(=2\) in the \(v\)-imaginary direction (i.e., \(\pm 1\) around \(m\)).

---

### A2) Height conversion (classical \(s\)-height \(T\) ↔ manuscript \(m\))
v33 uses width–2 normalization:
\[
u:=2s,\qquad v:=u-1=2s-1,
\]
so
\[
\Im(v)=2\,\Im(s).
\]
Hence if the classical ordinate is \(T:=\Im(s)\), then \(m=\Im(v)=2T\), i.e. \(T=m/2\).

**Location:** v33 §“Width–2 normalization” and the proof of Lemma `\ref{lem:Nloc-logm}` (final mapping lines).

✅ **Mapping consistency:** The \(T=m/2\) conversion used in the N\(_{\rm loc}\) proof is consistent with the manuscript’s width–2 coordinate convention.

---

### A3) Zero‑window bound and the plug‑in
v33 Lemma `\ref{lem:Nloc-logm}` states:
\[
N(T+1)-N(T-1)\le 1.01\log T + 17\qquad(T\ge 5),
\]
and concludes:
\[
N_{\rm loc}(m)\le 1.01\log m + 17\qquad(m\ge 10).
\]

v33’s proof explicitly justifies the window mapping:
- local window \(|\Im\rho-m|\le 1\) in \(v\) corresponds to \(|\gamma-T|\le \tfrac12\) in the \(s\)-plane (since \(m=2T\)),
- hence \(N_{\rm loc}(m)=N(T+\tfrac12)-N(T-\tfrac12)\le N(T+1)-N(T-1)\).

v33 then defines the explicit majorant:
\[
N_{\rm up}(m):=1.01\log m+17,\quad\text{so }N_{\rm loc}(m)\le N_{\rm up}(m)\ (m\ge 10),
\]
and uses it inside the tail inequality as the local term
\(\delta^{1/2}\,N_{\rm up}(m)/\kappa\).

**Location:**  
- Lemma `\ref{lem:Nloc-logm}` and its proof,  
- Corollary `\ref{cor:UE-residual-local}`,  
- §“The explicit tail inequality (post-pivot)”, and eq. `\eqref{eq:tail-ineq}`.

✅ **Acceptance test:** PASS. The window definition, height conversion, and the local term plug‑in are dimensionally and parametrically consistent in v33.

**One surgical hygiene note (recommended, not mathematically required):**  
In Lemma `\ref{lem:Nloc-logm}` the symbol \(\rho\) is used both for (i) zeros of \(E\) in the \(v\)-plane (via \(Z(m)\)) and (ii) zeros of \(\zeta\) in the \(s\)-plane (via \(N(T)\)). This is a potential referee confusion point. A one‑line notation clarification removes ambiguity and supports G‑12 (alignment/hygiene).

---

## Task B (MED) — Front‑end assumption packaging (G‑11 labeling)

v33 already contains a clean front‑end package:

- It defines \(H_0:=m_\star/2\) and fixes \(m_\star=10\Rightarrow H_0=5\).  
- It defines “RH holds up to height \(H_0\)” (Definition `\ref{def:frontend}`).
- It cites Platt–Trudgian’s rigorous verification to \(3\cdot 10^{12}\) as a sufficient literature discharge (Remark + Appendix `\ref{app:frontend}`).
- Global Theorem `\ref{thm:global}` assumes the front‑end only up to \(\Im(s)\le 5\).

✅ **Task‑B objective is already met in substance.**  
**However**, the front‑end remark currently says “How v31 discharges the front‑end” and “required statement for v31…”. In v33, this should be updated to “v33” / “this paper” for clarity and to avoid a reviewer thinking the argument depends on an older version.

**Recommended minimal edit:** rename the remark and add the explicit width–2 conversion sentence (“equivalently, \(0<m\le 10\)”).

---

## Task C (MED) — Bibliography / citation hygiene for the zero‑counting bound

### C1) Issue found
v33 cites `\cite[Theorem~1.1]{BellottiWongZeta2024}` inside Lemma `\ref{lem:Nloc-logm}`, but the bibliography entry currently reads (verbatim from v33):
- “A. Bellotti and T. Wong, *An improved explicit bound on the argument…*, arXiv:2412.15470v2 (2024).”

This is **not** the correct author/title metadata for arXiv:2412.15470v2.

### C2) Correct bib metadata (unambiguous)
arXiv:2412.15470v2 (dated 7 Jul 2025) is:
- **Chiara Bellotti and Peng‑Jie Wong**,  
- “**Improved estimates for the argument and zero‑counting function of the Riemann zeta-function** (with an appendix by Andrew Fiori).”

This is the paper whose Theorem 1.1 contains the explicit \(N(T)\) bound used in Lemma `\ref{lem:Nloc-logm}`.

✅ **Action:** patch the `\bibitem{BellottiWongZeta2024}` text only (no key renaming required).

---

# MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* **Callsign:** RH‑LOCAL  
* **Result classification:** **PASS** (G‑8 mapping is correctly integrated in v33; only hygiene edits are recommended.)  
* **Target gaps closed (by ID):**  
  - **G‑8** (integration audit PASS; local window ↔ bound ↔ plug‑in is consistent in v33)  
  - **G‑11 (front‑end packaging / labeling)** — **minor clarity patch** (rename “v31”→“v33”, add width–2 conversion sentence)  
* **Target gaps still open (by ID):**  
  - **G‑12** (overall certificate/theorem alignment risk remains multi-branch; this patch only improves notation + bib hygiene)  
  - **G‑4, G‑5, G‑6, G‑3** (out of scope for RH‑LOCAL)  
* **Key conclusions (5 bullets max):**
  1. v33 defines the local window as \(|\Im\rho-m|\le 1\) for zeros of \(E\), matching the Batch‑1 bound.  
  2. v33’s width–2 normalization gives \(m=2T\), so the local window corresponds to \(|\gamma-T|\le 1/2\) in the \(s\)-plane; the plug‑in is correct.  
  3. v33 uses \(N_{\rm up}(m)=1.01\log m+17\) (for \(m\ge 10\)) consistently in Corollary `\ref{cor:UE-residual-local}` and the tail inequality.  
  4. Front‑end packaging is present and correctly scoped to \(\Im(s)\le 5\), but two “v31” labels should be updated to “v33/this paper.”  
  5. The Bellotti–Wong bibliography entry metadata is currently incorrect and should be corrected for unambiguous citation hygiene.

* **Paste-ready manuscript edits:**
  (i) **revised lemma/proposition statements**  
  - **None required** (mathematical content is correct).  
  - **Optional notation micro‑patch (proof only):** clarify the two uses of \(\rho\) in Lemma `\ref{lem:Nloc-logm}`.

  **Replace the final mapping paragraph in the proof of Lemma `\ref{lem:Nloc-logm}` with:**
  ```tex
  Finally, in width--2 one has $v=2s-1$, so $\Im(v)=2\,\Im(s)$.
  Thus if $E(\rho_v)=0$ with $\Im(\rho_v)=m$, the corresponding zeta zero has ordinate $T=m/2$.
  The local window $|\Im\rho_v-m|\le 1$ corresponds to $|\gamma-T|\le 1/2$ in the $s$--plane, so
  $N_{\rm loc}(m)=N(T+\tfrac12)-N(T-\tfrac12)\le N(T+1)-N(T-1)$, yielding \eqref{eq:Nloc-explicit}.
  ```

  (ii) **revised definitions/remarks**  
  **In §`\ref{sec:frontend}` (“Finite-height front-end…”), change the two “v31” references to “v33/this paper” and add the width–2 conversion sentence.**

  Replace:
  ```tex
  In v31 we take $m_\star=10$, hence $H_0=5$.
  ```
  with:
  ```tex
  In this paper we take $m_\star=10$, hence $H_0=5$.
  ```

  Replace the remark heading/body:
  ```tex
  \begin{remark}[How v31 discharges the front-end]
  The required statement for v31 is RH up to height $H_0=5$.
  ...
  \end{remark}
  ```
  with:
  ```tex
  \begin{remark}[How v33 discharges the front-end]
  The required statement for this paper is RH up to height $H_0=5$.
  Equivalently, in the width--2 variable $v=2s-1$ this covers $0<\Im(v)\le 10$.
  This is a tiny special case of published rigorous verifications of RH to enormous heights.
  For example, Platt--Trudgian prove RH for all zeros with $0<\gamma\le 3\cdot 10^{12}$ using interval arithmetic,
  which immediately implies RH up to $H_0=5$.
  Appendix~\ref{app:frontend} records this discharge in a pinned JSON file.
  \end{remark}
  ```

  (iii) **revised theorem/inequality lines**  
  **Optional clarity edit (not required for correctness):** In Theorem `\ref{thm:global}`, replace the hard-coded statement with a reference to Definition `\ref{def:frontend}`:
  ```tex
  \item (Front-end) RH holds up to height $H_0=5$ in the sense of Definition~\ref{def:frontend}.
  ```

  (iv) **bibliography fix (Task C)**  
  Replace the current (incorrect) bibitem:
  ```tex
  \bibitem{BellottiWongZeta2024}
  A.~Bellotti and T.~Wong,
  \emph{An improved explicit bound on the argument of the Riemann zeta function on the critical line},
  arXiv:2412.15470v2 (2024).
  ```
  with:
  ```tex
  \bibitem{BellottiWongZeta2024}
  C.~Bellotti and P.-J.~Wong,
  \emph{Improved estimates for the argument and zero-counting function of the Riemann zeta-function}
  (with an appendix by A.~Fiori),
  arXiv:2412.15470v2 (2025).
  ```

* **Dependencies on other branches:**
  - **RH‑ABSORB:** none beyond consuming the already-correct local term majorant \(N_{\rm up}(m)=1.01\log m+17\).  
  - **RH‑CERT / G‑12 owners:** may want to ensure verifier scripts mirror \(N_{\rm up}(m)\) exactly; RH‑LOCAL cannot audit scripts absent the repro pack files.

* **Referee risk notes (anticipated objections + how addressed):**
  - **“Your local window bound doesn’t match your window definition.”** Addressed: v33 uses \(|\Im\rho-m|\le 1\), and explicitly maps it to \(|\gamma-m/2|\le 1/2\) (proof of Lemma `\ref{lem:Nloc-logm}`).  
  - **“You are mixing notations for zeros of \(E\) and zeros of \(\zeta\).”** Addressed by the optional \(\rho_v\) notation micro‑patch in the lemma proof.  
  - **“Your citation is incorrect / ambiguous.”** Addressed by correcting the Bellotti–Wong bibitem to match arXiv:2412.15470v2 metadata.
