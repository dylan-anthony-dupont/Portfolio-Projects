# Batch 10 — RH-FORCE (v39 locked)  
**File:** `batch10_RH-FORCE.md`  
**Scope:** Decide whether *defect-box pole-winding forcing* can replace **ML‑1** (Transfer/domination) in the v39 architecture.

---

## 0) Ground-truth context (v39)

### Frame mapping (must remain explicit)
- **s-frame:** \(\rho=\beta+i\gamma\).
- **u-frame:** \(u=2s\).
- **v-frame:** \(v=u-1\).  
  Then an off-axis zero \(\beta\neq \tfrac12\) corresponds to \(a:=2\beta-1\neq 0\), and “height” is \(m:=2\gamma\).

### Defect primitives (v39)
v39 defines the defect quotient and log-derivative
\[
\mathcal Q_a(v)=\frac{E(v+a)}{E(v-a)},\qquad
\mathcal L_a(v)=\frac{\mathcal Q_a'(v)}{\mathcal Q_a(v)}=\frac{E'}{E}(v+a)-\frac{E'}{E}(v-a),
\]
and the defect phase endpoint \(\Phi_B^{\rm def}(a)\) as a *max side* phase increment on the buffered contour \(\partial B_{\kappa/2}\).【781:1†manuscript_v39.pdf†L17-L55】

### Why ML‑1 exists in v39
The v39 “Missing Lever” box makes ML‑1 explicit: the forcing object is still \(D_B(W)\), and to use defect endpoints one needs a domination/transfer \(D_B(W)\lesssim \Phi^{\rm def}\) on some comparison box. Without it, forcing is disconnected from the defect endpoint UE mechanism.【781:7†manuscript_v39.pdf†L9-L20】【789:2†CR_master_dashboard_v39_locked.md†L19-L23】

### Local obstruction: aligned defect forcing fails at \(v=i m\)
Lemma 12.3 (v39) proves: if \(E(\pm a\pm i m)=0\), then \(\mathcal Q_a\) has a *removable singularity* at \(v=i m\), and the pure-pair contribution to \(\Phi^{\rm def}_{B(0,m,\delta)}(a)\) is only \(O(\delta/a)\). Hence **no aligned-box defect forcing** exists on \(B(0,m,\delta)\).【781:1†manuscript_v39.pdf†L56-L64】

---

## 1) The proposed bypass: “defect-box forcing” at center \(2a+i m\)

The dashboard records the diagnostic harness idea:
> “defect-box pole-winding forcing (center \(2a+i m\))” — **DEFERRED** — “useful diagnostic, not UE mechanism.”【789:2†CR_master_dashboard_v39_locked.md†L29-L38】

Mechanism sketch (already acknowledged in integration notes):
- Under a quartet at \(\pm a\pm i m\), the denominator \(E(v-a)\) vanishes at \(v=2a+i m\), so \(\mathcal Q_a\) has a pole there.
- A small box \(\widehat B:=B(2a,m,\widehat\delta)\) enclosing that pole forces a nontrivial winding/phase increment (“\(\pi/2\)-type forcing”).  
But v39 explicitly classifies this as **harness-only**, *not used* for UE/closure.【789:1†integration_notes_v39.md†L22-L28】

The Batch‑10 question is: **can this defect-box forcing replace ML‑1?**

---

## 2) Decision: **F‑FAIL** (cannot replace ML‑1 in current architecture)

### Core reason (referee-grade)
**Defect-box pole-winding forcing is a one-pole/topological forcing.**  
On any contour enclosing a pole of \(\mathcal Q_a\) (or a zero), the phase increment is quantized by the argument principle. Therefore the endpoint is **\(\delta\)-inert** and cannot satisfy the δ‑shrinkable UE inequality class needed for S5 budget closure.

This is aligned with v39’s latched “NO–GO latches” in the Missing Lever box: “one-pole endpoint classes cannot win” (no UE gain \(p>0\)).【781:7†manuscript_v39.pdf†L33-L36】

### Formal NO‑GO lemma (paste-ready)
Below is the minimal statement that converts “diagnostic forcing” into a **decision instrument**: it proves the bypass cannot serve as ML‑1 replacement (because it cannot coexist with a \(p>0\) δ‑uniform UE bound).

```tex
\begin{lemma}[NO--GO: defect-box pole-winding cannot replace ML--1]\label{lem:defectbox-nogo-ML1}
Fix $\kappa\in(0,1/10)$ and let $a\in(0,1)$, $m>0$.
Assume $E$ is the even entire width--2 completion and that $E$ has a quartet at
$\pm a\pm i m$ (so $E(a+i m)=E(-a+i m)=0$ with multiplicities $\ge 1$).
Define $\mathcal Q_a(v)=E(v+a)/E(v-a)$ and let $\Phi^{\rm def}_{B}(a)$ be the defect phase endpoint
(Definition~\ref{def:defect-endpoint}).

Let $\widehat B=B(2a,m,\delta)$ be any $\kappa$--admissible aligned box with
$0<\delta\le a/4$ such that:
(i) $\partial \widehat B_{\kappa/2}$ contains no zeros or poles of $\mathcal Q_a$, and
(ii) $\widehat B_{\kappa/2}$ contains the point $v_0:=2a+i m$ but contains no other zero/pole of $\mathcal Q_a$.

Then $\mathcal Q_a$ has a pole in $\widehat B_{\kappa/2}$ and the argument principle yields
\[
\Big|\Delta_{\partial\widehat B_{\kappa/2}}\arg \mathcal Q_a\Big|=2\pi.
\]
Consequently,
\[
\Phi^{\rm def}_{\widehat B}(a)\ \ge\ \frac{\pi}{2},
\]
independently of $\delta$.

In particular, \emph{no} inequality of the form
$\Phi^{\rm def}_{\widehat B}(a)\le C\,\delta^p(\log m)^q$ with $p>0$ and $C$ independent of $\delta$
can hold uniformly as $\delta\to 0$ on this defect-box family. Hence defect-box pole-winding forcing
cannot be used as a $\delta$--shrinkable UE mechanism and therefore cannot replace ML--1 in the v39
architecture.
\end{lemma}

\begin{proof}
Since $E(a+i m)=0$, the denominator $E(v-a)$ vanishes at $v_0=2a+i m$, so $\mathcal Q_a$ has a pole at $v_0$.
Under (i)--(ii), $\mathcal Q_a$ is meromorphic in a neighborhood of $\partial\widehat B_{\kappa/2}$ with exactly one
pole and no zeros/poles on the contour. The argument principle gives total phase change $2\pi$ in magnitude around
$\partial\widehat B_{\kappa/2}$. Since $\partial\widehat B_{\kappa/2}$ is the concatenation of four oriented sides,
at least one side has phase increment magnitude at least $\pi/2$. By definition of $\Phi^{\rm def}_{\widehat B}(a)$
as the max side increment, $\Phi^{\rm def}_{\widehat B}(a)\ge\pi/2$. The final incompatibility with any $p>0$
$\delta$--gain is immediate.
\end{proof}
```

### Interpretation
- This lemma does **not** say defect-box forcing is false; it says it is **structurally incompatible** with the δ‑shrinkable UE program (and hence cannot replace ML‑1).
- It also cleanly addresses the “forced-zero obstruction”: on the *analytic/aligned* box \(B(0,m,\delta)\) the forced quartet **does not** force winding because \(\mathcal Q_a\) is removable at \(v=i m\) (Lemma 12.3).【781:1†manuscript_v39.pdf†L56-L64】

---

## 3) What this implies for v40 planning (surgical)

1. **ML‑1 remains mandatory.** v39’s dependency DAG stays correct: forcing produces \(D_B(W)\); defect UE must be connected by transfer/domination, not by defect-box pole winding.【789:2†CR_master_dashboard_v39_locked.md†L19-L23】【781:7†manuscript_v39.pdf†L9-L20】

2. Defect-box pole-winding forcing should stay explicitly labeled **harness-only** (diagnostic), as already recorded by CR.【789:2†CR_master_dashboard_v39_locked.md†L29-L38】

3. If anyone insists on using defect-box forcing for closure, it would require a **different closure paradigm** not based on δ‑shrinking (contradicting the current S5 budget architecture), i.e. it is “new architecture,” not an ML‑1 bypass.

---

## 4) S6 harness cross-check: explicit-formula meaning (amplitude leak)

- Under \(s\to u\to v\), an off-line zero \(\beta>1/2\) corresponds to \(a=2\beta-1>0\).  
- In the explicit formula, such a zero contributes an \(x^\beta\) term (“amplitude leak”) relative to the main \(x\) term (v39 keeps this as an interpretation harness).【789:15†manuscript_v39.pdf†L1-L2】

**Does defect-box pole-winding forcing “detect the leak”?**  
Only indirectly: it detects the *geometric tilt* \(a>0\) by exhibiting a pole of \(\mathcal Q_a\) at \(v=2a+i m\). This is not a quantitative \(x^\beta\) bound; it is a topological witness that “tilt exists.” Therefore it remains an internal diagnostic, not an explicit-formula amplitude control mechanism.

---

# MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* **Callsign:** RH-FORCE  
* **Result classification:** **FAIL** (as ML‑1 replacement)  
* **Target gaps closed (by ID):** closes the **“bypass hypothesis”**: defect-box pole-winding forcing **cannot** replace ML‑1 inside v39’s δ‑shrinking architecture.  
* **Target gaps still open (by ID):** **ML‑1, ML‑2, ML‑3** remain open (transfer, defect UE, resonance control).  
* **Key conclusions (≤5 bullets):**
  1. Aligned defect forcing at \(v=i m\) is impossible (removable singularity) — v39 Lemma 12.3 already pins this.  
  2. Defect-box forcing around \(2a+i m\) is **topological/δ‑inert** (one-pole class).  
  3. Any \(p>0\) δ‑gain UE bound is incompatible with one-pole defect boxes ⇒ cannot support S5 budget closure.  
  4. Therefore defect-box forcing is harness-only and **cannot** replace ML‑1.  
  5. v40 must focus on ML‑1 transfer + ML‑2 UE + ML‑3 resonance (no forcing bypass).

* **Paste-ready manuscript edits (TeX blocks):**
  (i) **New lemma** to insert in Section 12 (near the defect endpoint subsection or Missing Lever box):  
  *Use the lemma `lem:defectbox-nogo-ML1` exactly as written above.*

  (ii) **Remark for Box `box:missing-lever-v39` (add a “No bypass” sentence):**
  ```tex
  \begin{remark}[No bypass via defect-box pole winding]\label{rem:no-bypass-defectbox}
  Although $\mathcal Q_a$ has a pole at $v=2a+i m$ under an off-axis quartet, forcing the winding of $\mathcal Q_a$
  on a small box enclosing that pole is a one-pole/topological effect and is $\delta$--inert. By
  Lemma~\ref{lem:defectbox-nogo-ML1}, such defect-box forcing cannot yield any $\delta$--gain UE bound with $p>0$
  and therefore cannot replace the ML--1 transfer mechanism in the $\delta$--shrinking S5$^{\rm def}$ program.
  \end{remark}
  ```

  (iii) **Missing Lever box insertion (one line):**
  ```tex
  \item[\textbullet] (No bypass) Defect-box pole-winding forcing at $2a+i m$ is harness-only and cannot replace (ML--1)
  (Remark~\ref{rem:no-bypass-defectbox}).
  ```

* **Dependencies on other branches:** None for the NO‑GO lemma itself (uses only argument principle + existing defect definitions).  
* **Referee risk notes (anticipated objections + how addressed):**
  - *Objection:* “But forcing being constant is fine; why can’t we contradict with a small UE bound?”  
    *Answer:* because on a contour enclosing a pole/zero the phase increment is quantized; any correct UE upper bound must reflect that and cannot be \(o(1)\) in \(\delta\). The lemma isolates this incompatibility precisely.  
  - *Objection:* “Could we pick \(\widehat B\) so the pole is not enclosed?”  
    *Answer:* then there is no topological forcing; this reverts to ML‑1/ML‑2/ML‑3 (no bypass).  
  - *Objection:* “Does this smuggle RH?”  
    *Answer:* no; hypotheses are purely “quartet at \(\pm a\pm i m\)” in v-frame with \(a\neq 0\), with explicit s→u→v mapping stated up front.

