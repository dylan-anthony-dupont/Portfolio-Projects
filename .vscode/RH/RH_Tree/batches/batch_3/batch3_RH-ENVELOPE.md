# batch3_RH-ENVELOPE.md  
**UE‑Gate Decision (v33 ground truth)**  
**Callsign:** RH‑ENVELOPE  
**Primary target:** **G‑2 (Upper‑envelope δ‑exponent gate)**  
**Secondary:** G‑1 integration consistency only where it touches UE→tail bookkeeping.

---

## 0) UE‑Gate verdict (explicit answers required by Batch‑3 protocol)

### 0.1 Best UE exponent actually supported by a proof
- **Best proven exponent:** **\(p=1\)** for the *pointwise* dial‑deviation bound currently stated in v33 Lemma `\ref{lem:upper-envelope}`.
- The currently written statement **\(\delta^{3/2}\)** is **not supported** by the proof as written; correcting the proof arithmetic yields **\(\delta^{1}\)**.

### 0.2 Does S1′ (η‑absorption tail closure) survive under this \(p\)?
- **Answer:** **NO.**  
  Under \(p=1\), the split+collar insertion forces a **δ⁰ local term** (non‑shrinkable in η), which breaks the η‑absorption mechanism as used in v33 Sections `\ref{sec:eta-absorption}`–`\ref{sec:global}`.

### 0.3 Minimal v34 edits implied by this conclusion
- v34 must choose **one** of two truth‑preserving directions:

  **(S1′‑break / truthful downgrade):**  
  Downgrade UE from \(\delta^{3/2}\) to \(\delta\) everywhere it feeds the tail chain, and explicitly mark that η‑absorption closure is no longer proven (retain only a conditional “criterion” form).

  **(S1′‑keep / requires new technology):**  
  Keep \(\delta^{3/2}\) **only by changing the mechanism** (e.g., replace pointwise dial deviation by an \(L^2(\partial B)\) deviation that genuinely carries \(\delta^{3/2}\)), and add a new forcing‑to‑\(L^2\) lower‑bound lemma. This is a redesign, not a proof‑fix.

---

## 1) Referee audit of v33 UE lemma: where the exponent comes from

### 1.1 Ground truth object
v33 Lemma `\ref{lem:upper-envelope}` (Upper envelope bound, outer‑aligned form) is a **pointwise** bound on dial centers:
\[
\sum_{\pm}\bigl|W(v_\pm)-e^{i\varphi_0^\pm}\bigr|
\ \le\ 2\,C_{\rm up}\,\delta^{3/2}\,
\sup_{\partial B}\Bigl|\frac{E'}{E}\Bigr|.
\tag{UE‑stmt in v33}
\]

### 1.2 The proof’s scale factors (as written in v33)
In the proof of Lemma `\ref{lem:upper-envelope}`, v33 explicitly enumerates the scaling contributions:

1. **Boundary→point evaluation via harmonic measure:** contributes  
   \(\|P_B(v_0,\cdot)\|_\infty^{1/2}\sim \delta^{-1/2}\).

2. **Poincaré/Wirtinger on \(\partial B\):** contributes  
   \(|\partial B|/(2\pi)\sim \delta\).

3. **Outer factor control (Hilbert/Cauchy operator):** no δ power.

4. **\(L^2(\partial B)\)→sup conversion for \(E'/E\):** contributes  
   \(\sqrt{|\partial B|}\sim \delta^{1/2}\).

Multiplying the δ‑powers that the proof itself lists gives:
\[
\delta^{-1/2}\cdot \delta \cdot \delta^{1/2}=\delta^{1}.
\]

### 1.3 UE‑Gate conclusion (proved inequality)
Therefore the *proved* pointwise bound supported by the proof chain is:

\[
\sum_{\pm}\bigl|W(v_\pm)-e^{i\varphi_0^\pm}\bigr|
\ \le\ 2\,C_{\rm up}\,\delta\,
\sup_{\partial B}\Bigl|\frac{E'}{E}\Bigr|.
\tag{UE‑proved; \(p=1\)}
\]

### 1.4 “Why \(p>1\) is not recoverable by a local proof tweak” (scaling sanity check)
Independently of the bookkeeping, \(p=1\) is the scale‑consistent exponent when:
- the constant \(C_{\rm up}\) is **shape‑only** (scale‑invariant), and
- the right side uses \(\sup_{\partial B}|E'/E|\), which has units \(1/\text{length}\).

Under the similarity \(v=v_0+\delta z\), one has \((E'/E)(v)=\delta^{-1}(f'/f)(z)\). To combine a scale‑invariant constant with a dimensionless dial deviation on the left, the δ factor must be **exactly δ¹**. Any claimed \(p>1\) in a pointwise inequality of this form would contradict scaling unless additional smallness structure is introduced (different norms, different functional, or extra hypotheses).

---

## 2) Consequence for UE→split→collar→tail: why η‑absorption breaks for \(p=1\)

### 2.1 Generic exponent ledger with a UE exponent \(p\)
Assume a pointwise UE of the form:
\[
\text{dial‑dev} \ \le\ 2C_{\rm up}\,\delta^{p}\,\sup_{\partial B}\Bigl|\frac{E'}{E}\Bigr|.
\]

With the v33 split and collar majorant:
\[
\sup_{\partial B}\Bigl|\frac{E'}{E}\Bigr|\le L(m)+\frac{N_{\rm loc}(m)}{\kappa\delta},
\]
one obtains:
\[
\text{dial‑dev}\ \le\ 2C_{\rm up}\Bigl(\delta^{p}L(m)+\delta^{p-1}\frac{N_{\rm loc}(m)}{\kappa}\Bigr).
\]

**Key:** the local term shrinks with δ only if \(p>1\).

### 2.2 Plugging in the proved \(p=1\)
With \(p=1\):
\[
\text{dial‑dev}\ \le\ 2C_{\rm up}\Bigl(\delta\,L(m)+\frac{N_{\rm loc}(m)}{\kappa}\Bigr).
\]

The local term is now **δ⁰** and is **not shrinkable** by choosing η small (since δ scales linearly with η).

### 2.3 Why this breaks S1′ in v33
v33 Theorem `\ref{thm:tail-inequality}` has a fixed positive constant
\[
c=\frac{3\log 2}{16}\approx 0.13
\]
on the right side, while the local majorant satisfies (Lemma `\ref{lem:Nloc-logm}`):
\[
N_{\rm loc}(m)\le 1.01\log m+17.
\]

Even at the low anchor \(m=10\), the v33 majorant gives \(N_{\rm up}(10)\approx 19.3\). With \(\kappa\le 0.1\), the constant term \(N_{\rm up}(10)/\kappa\) is \(\gtrsim 190\), and multiplying by \(2C_{\rm up}\) makes the left side astronomically larger than \(c\). Thus the η‑absorption section (which relies on a shrinkable \(\eta^{1/2}\) local term) cannot survive under \(p=1\).

**Conclusion:** **S1′ does not survive** under the proved UE exponent \(p=1\).

---

## 3) Minimal redesign candidates if Control Room wants S1′ back (ranked)

This section is intentionally short (max 2–3 candidates), as requested.

### Candidate R1 (highest viability): Replace pointwise dial deviation by an \(L^2(\partial B)\) deviation
**Idea:** The proof already yields an \(L^2\) upper‑envelope with a genuine **\(\delta^{3/2}\)** factor before the point‑evaluation step is applied.

Specifically, from v33 proof Steps (2)–(4) (dropping Step (1)), one can prove:
\[
\|W-e^{i\varphi_0}\|_{L^2(\partial B)}\ \lesssim\ \delta^{3/2}\sup_{\partial B}|E'/E|.
\]
Then split+collar gives exactly the shrinkable local term \(\delta^{1/2}N_{\rm loc}(m)/\kappa\) again.

**New required lemma (outside this branch’s proof scope):**  
A forcing/budget inequality that lower‑bounds an \(L^2(\partial B)\) deviation (or an \(L^2\) phase‑variation functional) by the short‑side forcing constant.

**Pros:** Keeps the tail inequality’s \(\eta^{1/2}\) absorption structure intact.  
**Cons:** Requires a forcing‑to‑\(L^2\) bridge (new lemma).

### Candidate R2 (medium viability): Redesign the local factor/window so the collar blow‑up is weaker than \(1/\delta\)
**Idea:** If the collar step could be replaced by a bound of the form
\[
\sup_{\partial B}\Bigl|\frac{Z'_{\rm loc}}{Z_{\rm loc}}\Bigr|\ \lesssim\ \frac{N_{\rm loc}(m)}{\kappa\,\delta^\theta}
\quad\text{with}\quad \theta<1,
\]
then even a \(p=1\) UE would produce a shrinkable \(\delta^{1-\theta}\) local contribution.

**New required lemma:** A genuinely stronger “local log‑derivative on the boundary” estimate (not the standard sum of \(1/\dist\) terms).  
**Pros:** Keeps pointwise dial deviation.  
**Cons:** Looks technically harder than R1; likely needs substantial new analytic technology.

### Candidate R3 (fallback): Abandon η‑absorption; revert to S2‑style certified criterion
**Idea:** Accept \(p=1\), keep the corrected chain as a criterion, and use a computational/certified scaffold to close what absorption no longer closes.  
**Pros:** Truthful and auditable.  
**Cons:** It is not S1′; it’s a strategic retreat to the harness.

---

## 4) v34 patch sets (as requested)

### Patch Set S1′‑keep (ONLY if \(p>1\)) — not available under pointwise UE
**Verdict:** Under the current pointwise architecture, **there is no honest “proof patch” that upgrades \(p\) above 1**.  
Therefore a “keep δ^{3/2} in the pointwise UE” patch set is **not applicable**.

**If Control Room adopts redesign Candidate R1**, then a different S1′‑keep patch becomes viable:
- Replace the *pointwise* UE lemma with an *\(L^2(\partial B)\)* UE lemma carrying \(\delta^{3/2}\).
- Rewrite the tail inequality to use the \(L^2\) deviation functional instead of pointwise dial deviation.
- Add the new forcing‑to‑\(L^2\) lower‑bound lemma as an explicit open gate (or prove it).

(I do **not** supply that forcing lemma here; it is outside RH‑ENVELOPE scope.)

### Patch Set S1′‑break (if \(p\le1\)) — **recommended for v34 truthfulness**
This is the minimal set of edits that makes the manuscript internally consistent and audit‑grade under the proven \(p=1\).

---

# MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* **Callsign:** RH‑ENVELOPE

* **Result classification:** **FAIL** (for S1′ under current pointwise UE); **PASS** (for UE exponent audit itself).

* **Target gaps closed (by ID):**
  - **G‑2 (UE δ‑exponent gate):** closed — best proven \(p\) is identified and enforced.

* **Target gaps still open (by ID):**
  - **S1′ tail closure (η‑absorption):** open/broken under \(p=1\) (not a numbered gap, but the program’s closure step).  
  - **G‑4 / G‑5:** remain relevant only if an absorption‑style closure is pursued.  
  - **G‑1:** residual envelope ledger is still a hard gate for any tail inequality criterion (not re‑audited here unless redesigned per R1).

* **Key conclusions (5 bullets max):**
  1. v33’s pointwise UE proof supports **\(\delta^1\)**, not \(\delta^{3/2}\); the δ‑arithmetic is explicit and unambiguous.
  2. The exponent **\(p=1\)** is also forced by scaling for a shape‑only constant multiplying \(\sup|E'/E|\).
  3. With \(p=1\), the split+collar step produces a **δ⁰ local term** \(N_{\rm loc}(m)/\kappa\), which destroys η‑absorption.
  4. Therefore **S1′ does not survive** under the proved pointwise UE exponent.
  5. The smallest route to recover \(\delta^{3/2}\) shrinkability is **R1**: switch from pointwise dial deviation to an \(L^2(\partial B)\) deviation functional and add a forcing‑to‑\(L^2\) lower bound.

* **Paste-ready manuscript edits:**
  (i) **revised lemma/proposition statements**
  - **Lemma `\ref{lem:upper-envelope}` (UE, outer‑aligned form):** replace \(\delta^{3/2}\) by \(\delta\) in the statement:
```tex
% In Lemma \ref{lem:upper-envelope}, Eq. \eqref{eq:UE-EoverE}:
\sum_{\pm}\bigl|W(v_\pm)-e^{i\varphi_0^\pm}\bigr|
\ \le\ 2\,C_{\rm up}\,\delta\,
\sup_{v\in\partial B}\Bigl|\frac{E'(v)}{E(v)}\Bigr|.
```

  - **Corollary `\ref{cor:UE-residual-local}`:** replace the UE‑driven powers accordingly:
```tex
\sum_{\pm}|W(v_\pm)-e^{i\varphi_0^\pm}|
\le 2C_{\rm up}\left(\delta\,L(m) + \frac{N_{\rm loc}(m)}{\kappa}\right)
\le 2C_{\rm up}\left(\delta\,L(m) + \frac{1.01\log m + 17}{\kappa}\right).
```

  - **Theorem `\ref{thm:tail-inequality}`:** update the LHS to match the corrected UE chain:
```tex
2C_{\mathrm{up}}\Bigl(\delta\,L(m)\; +\; \frac{N_{\rm up}(m)}{\kappa}\Bigr)
\ <\
 c\ -\ \delta\Bigl(K_{\rm alloc}\,c_0\,L(m)+C_h''\,(\log m+1)\Bigr).
```
(Keep the theorem as a **conditional criterion**; do not claim it is satisfiable by η‑absorption.)

  (ii) **revised definitions/remarks**
  - **Section `\ref{sec:eta-absorption}` header paragraph:** replace the absorption claim with a truthful status note:
```tex
\begin{remark}[UE exponent gate and status]
The pointwise upper-envelope Lemma~\ref{lem:upper-envelope} yields a $\delta^1$ scaling (not $\delta^{3/2}$)
under the current hypotheses.  Consequently, after the split and collar bound, the local contribution becomes
$\delta^0$ and is not shrinkable by choosing $\eta$ small.  The $\eta$--absorption closure in v33 therefore
requires either (i) a strengthened UE mechanism with exponent $p>1$, or (ii) a redesigned forcing-vs-envelope
comparison (e.g.\ an $L^2(\partial B)$ deviation functional).  Until such a lemma is supplied, global closure
by absorption is not established.
\end{remark}
```

  - **Disable/retire Proposition `\ref{prop:eta-absorption}`** by converting it into a conditional statement:
```tex
% Rename proposition as conditional/open, or comment it out and replace by an "Open Lemma" placeholder.
```

  (iii) **revised theorem/inequality lines**
  - In the proof sketch of Theorem `\ref{thm:tail-inequality}`, replace any reference to the \(\delta^{1/2}\) local term with the corrected δ⁰ term and explicitly state that η‑absorption no longer follows.

* **Dependencies on other branches:**
  - If Control Room pursues **R1 (L2‑deviation redesign)**: requires a new **forcing‑to‑\(L^2\)** lower bound (forcing branch) and likely a matching “horizontal budget” reformulation in \(L^2\).
  - If Control Room pursues **R2 (weaker collar blow‑up)**: requires new local log‑derivative technology (local term branch).
  - Residual envelope ledger (G‑1) remains a prerequisite for any tail inequality criterion, regardless of exponent.

* **Referee risk notes (anticipated objections + how addressed)**
  1. **Objection:** “Your UE exponent mismatch is subjective.”  
     **Addressed:** the proof explicitly lists δ‑factors; multiplying them yields δ¹. This also matches scaling invariance.
  2. **Objection:** “You are breaking the claimed RH proof.”  
     **Addressed:** v34 must be truthful. The patch set S1′‑break preserves correctness by downgrading claims and marking absorption as open.
  3. **Objection:** “Maybe δ^{3/2} can be recovered by a better estimate.”  
     **Addressed:** not for a pointwise UE with shape‑only constant and \(\sup|E'/E|\); scaling forces \(p=1\) unless the mechanism changes (R1/R2).  
