# batch3_RH-BRIDGE — UE Gate Decision Support (v33 ground truth)

**Callsign:** RH-BRIDGE  
**Scope:** UE-gate decision support from the boundary/outer-factor/harmonic analysis side.  
**Ground truth:** `manuscript_v33.tex/pdf` only.

---

## Required UE-gate answers (explicit)

### Q1) What UE \(\delta\)-exponent is actually supported by a proof?
**Best proven exponent:** \(\boxed{p=1}\) (i.e., UE gives \(\;\sim \delta^1\;\) against \(\sup_{\partial B}|E'/E|\)).  

> The currently stated v33 exponent \(\delta^{3/2}\) in Lemma `\ref{lem:upper-envelope}` is **not** supported by the proof as written, because the point-evaluation operator from \(L^2(\partial B,ds)\) necessarily contributes a sharp \(\delta^{-1/2}\) factor (Task A below).

### Q2) Does S1′ (η‑absorption tail closure) survive under that \(p\)?
**Answer:** \(\boxed{\text{NO}}\) (not in its current v33 form).

Reason: with \(p=1\), plugging the collar split
\[
\sup_{\partial B}\Big|\frac{E'}{E}\Big| \le L(m)+\frac{N_{\rm up}(m)}{\kappa\delta}
\]
into UE yields an \(O(\delta^0)\) local term \(N_{\rm up}(m)/\kappa\) that **does not decay** as \(\delta\to 0\). The v33 tail inequality crucially needs the **decaying** \(\delta^{1/2}\) local term that comes from \(p>1\) (specifically \(p=3/2\)).

### Q3) What minimal v34 edits follow?
**Minimal audit-honest v34 edits:**
1. **Correct Lemma `\ref{lem:upper-envelope}` to the proven scaling \(p=1\)** (i.e., \(\delta^{3/2}\mapsto \delta\)).  
2. **Insert an explicit evaluation-operator lemma** (Task A) documenting the sharp \(\delta^{-1/2}\) scaling.  
3. **Downgrade the v33 tail closure posture** to explicitly require a *new* UE-gate mechanism achieving \(p>1\), or otherwise mark η‑absorption closure as **blocked** under the proven UE bound.

(Concrete patch text is provided below.)

---

## Task A (CRITICAL): audit the “point evaluation from boundary trace” scaling

### A.1 The sharp evaluation operator norm (L\(^2(\partial B,ds)\) \(\to\) interior point)

Let \(B=B(v_0,\delta)\) be the closed rectangle in the \(v\)-plane
\[
B(v_0,\delta)=\{\,v\in\mathbb C:\ \|v-v_0\|_\infty\le \delta\,\},
\qquad B^\circ=\mathrm{int}(B).
\]

#### Lemma A (evaluation from boundary \(L^2(ds)\); sharp \(\delta^{-1/2}\))
Let \(u\in C(\overline B)\cap \mathrm{Harm}(B^\circ)\). Then
\[
|u(v_0)|\le \|P_B(v_0,\cdot)\|_{L^2(\partial B,ds)}\ \|u\|_{L^2(\partial B,ds)}.
\]
Moreover, under the similarity map \(T(\xi)=(\xi-v_0)/\delta\) sending \(\partial B\) to \(\partial Q\) with \(Q=[-1,1]^2\),
\[
\|P_B(v_0,\cdot)\|_{L^2(\partial B,ds)}=\delta^{-1/2}\ \|P_Q(0,\cdot)\|_{L^2(\partial Q,ds)}.
\]
Hence there is a shape-only constant \(C_{\rm eval}:=\|P_Q(0,\cdot)\|_{L^2(\partial Q)}\) such that
\[
\boxed{\quad |u(v_0)|\ \le\ C_{\rm eval}\ \delta^{-1/2}\ \|u\|_{L^2(\partial B,ds)}.\quad}
\]

**Proof (sketch, referee-grade):**
- Harmonic measure representation: \(u(v_0)=\int_{\partial B} u(\xi)\,d\omega^B_{v_0}(\xi)=\int_{\partial B} u(\xi)\,P_B(v_0,\xi)\,ds(\xi)\).
- Cauchy–Schwarz: \(|u(v_0)|\le \|P_B(v_0,\cdot)\|_2\,\|u\|_2\).
- Scaling: \(ds_B=\delta\,ds_Q\) and \(P_B(v_0,v_0+\delta\xi)=\delta^{-1}P_Q(0,\xi)\), so
  \[
  \int_{\partial B}P_B(v_0,\xi)^2\,ds_B(\xi)
  =\int_{\partial Q}(\delta^{-1}P_Q(0,\xi))^2\,(\delta\,ds_Q(\xi))
  =\delta^{-1}\int_{\partial Q}P_Q(0,\xi)^2\,ds_Q(\xi).
  \]

#### Sharpness (cannot improve \(\delta^{-1/2}\) under \(L^2(ds)\))
Take \(u\equiv 1\) on \(\overline B\). Then \(u(v_0)=1\) while \(\|u\|_{L^2(\partial B)}=\sqrt{|\partial B|}=\sqrt{8\delta}\).
Any inequality of the form \(|u(v_0)|\le C\,\delta^{-\gamma}\|u\|_{L^2(\partial B)}\) forces
\(1\le C\,\delta^{-\gamma}\sqrt{8\delta}\), hence \(\gamma\ge 1/2\).
So \(\delta^{-1/2}\) is **unavoidable** in this norming.

---

### A.2 Consequence for UE: the v33 \(\delta^{3/2}\) factor cannot be obtained from \(L^2(ds)\) point evaluation

In v33 Lemma `\ref{lem:upper-envelope}`, Step 1 explicitly notes that boundary evaluation “produces \(\delta^{-1/2}\)”.
That already fixes the exponent arithmetic:

- evaluation from boundary \(L^2(ds)\): \(\delta^{-1/2}\) (sharp; Lemma A above),
- Poincaré/Wirtinger on \(\partial B\): \(\delta^{+1}\),
- \(L^2\to \sup\) on \(\partial B\): \(\delta^{+1/2}\),

so the total scaling against \(\sup_{\partial B}|E'/E|\) is
\[
(-1/2)+1+(1/2)=1,
\]
not \(3/2\).

**Therefore:** the strongest \(\delta\)-power supported by this route is \(\boxed{p=1}\).

---

## Task B: if \(\delta^{3/2}\) is not possible via this route, best alternatives (≤2)

The conclusion above is not a “small tweak” issue; it is structural. To achieve \(p>1\) you must **change the UE architecture**, not merely renormalize constants.

### Alternative 1 (rank 1): redesign UE to avoid \(\sup_{\partial B}|E'/E|\) (sup-based collar blow-up)
**Idea:** Replace the UE endpoint bound in terms of \(\sup_{\partial B}|E'/E|\) by a bound in terms of a *bulk norm* or a *Carleson-type boundary norm* in which the local log-derivative contribution does not scale like \(1/\delta\) at the boundary.  
**Viability:** Medium (requires new harmonic/Hardy machinery; but plausibly the only way to recover a decaying local term without \(p>1\) from point evaluation).

### Alternative 2 (rank 2): redefine the outer/inner quotient so the “local factor” is absorbed before UE
**Idea:** Modify the definition of the quotient controlled by UE so that the factor responsible for the collar blow-up (the local zero factor) is removed *before* applying the boundary envelope. Conceptually, this is a controlled return toward a “residual-based” UE, but it must be made compatible with the forcing/dial object.  
**Viability:** Low–Medium (touches the v31→v32/v33 “no residual proxying” stance; would require careful re-audit of what the forcing lemma actually needs).

---

## Task C: v34-ready edits (audit-honest patch set)

Below are minimal edits that (i) correct the proven scaling, and (ii) explicitly mark the UE-gate required for η-absorption tail closure.

### C.1 Patch: add the evaluation lemma (near the UE proof, before Lemma `\ref{lem:upper-envelope}` proof)

```tex
\begin{lemma}[Point evaluation from boundary $L^2$]\label{lem:eval-L2}
Let $B=B(v_0,\delta)$ be a closed rectangle and $u\in C(\overline B)\cap \mathrm{Harm}(B^\circ)$.
Then
\[
|u(v_0)|\le \|P_B(v_0,\cdot)\|_{L^2(\partial B,ds)}\,\|u\|_{L^2(\partial B,ds)}.
\]
Under the similarity map $T(\xi)=(\xi-v_0)/\delta$ sending $\partial B$ to $\partial Q$ with $Q=[-1,1]^2$,
\[
\|P_B(v_0,\cdot)\|_{L^2(\partial B,ds)}=\delta^{-1/2}\,\|P_Q(0,\cdot)\|_{L^2(\partial Q,ds)}.
\]
In particular, there is a shape-only constant $C_{\rm eval}:=\|P_Q(0,\cdot)\|_{L^2(\partial Q)}$ such that
\[
|u(v_0)|\le C_{\rm eval}\,\delta^{-1/2}\,\|u\|_{L^2(\partial B,ds)}.
\]
Moreover the exponent $\delta^{-1/2}$ is sharp under $L^2(\partial B,ds)$ norming.
\end{lemma}
```

### C.2 Patch: correct the proven UE exponent in Lemma `\ref{lem:upper-envelope}`

**Change in the lemma statement:** replace \(\delta^{3/2}\) by \(\delta\) in `\eqref{eq:UE-EoverE}`.

```diff
- \sum_{\pm}\bigl|W(v_\pm)-e^{i\varphi_0^\pm}\bigr|
- \ \le\ 2\,C_{\rm up}\,\delta^{3/2}\,\sup_{v\in\partial B}\Bigl|\frac{E'(v)}{E(v)}\Bigr|.
+ \sum_{\pm}\bigl|W(v_\pm)-e^{i\varphi_0^\pm}\bigr|
+ \ \le\ 2\,C_{\rm up}\,\delta\,\sup_{v\in\partial B}\Bigl|\frac{E'(v)}{E(v)}\Bigr|.
```

**Change in the proof (final combined line):** replace \(\delta^{3/2}\) by \(\delta\).

```diff
- \cdot \delta^{3/2}\sup_{\partial B}\Big|\frac{E'}{E}\Big|,
+ \cdot \delta\sup_{\partial B}\Big|\frac{E'}{E}\Big|,
```

*(No other proof steps need to change; the exponent correction is the arithmetic consequence of Step 1’s unavoidable \(\delta^{-1/2}\).)*

### C.3 Patch: add an explicit “UE-gate” remark near tail closure (audit honesty)

Insert immediately after Lemma `\ref{lem:upper-envelope}` or at the start of the tail-inequality section:

```tex
\begin{remark}[UE-gate and $\eta$--absorption]\label{rem:UE-gate}
The point-evaluation step from $L^2(\partial B,ds)$ necessarily incurs a sharp factor $\delta^{-1/2}$
(Lemma~\ref{lem:eval-L2}). Consequently, the upper-envelope bound against $\sup_{\partial B}|E'/E|$
has proven scaling $O(\delta)$, not $O(\delta^{3/2})$.
Under the collar bound $\sup_{\partial B}|Z'_{\rm loc}/Z_{\rm loc}|\lesssim (\kappa\delta)^{-1}$,
an $O(\delta)$ UE bound yields a non-decaying local contribution $O(N_{\rm up}(m)/\kappa)$, which blocks
$\eta$--absorption tail closure in its current form. Any $\eta$--absorption closure therefore requires
a strengthened UE mechanism (``UE-gate'') that yields an effective $\delta$--power $p>1$ against the local term,
or a redesign of the envelope architecture that avoids the sup-based collar blow-up.
\end{remark}
```

---

# MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* Callsign: RH-BRIDGE
* Result classification: **FAIL** (UE \(p>1\) is not supported by boundary \(L^2(ds)\) point-evaluation; therefore S1′ η‑absorption does not survive as currently structured)
* Target gaps closed (by ID): **G-2 (UE scaling audit sub-issue)** — the v33 “Upper-envelope scaling audit” blocker is resolved (with a negative result); **G-6** remains stable (no changes needed).
* Target gaps still open (by ID): **G-4 (δ‑uniformity for absorption)** and tail-closure viability are now contingent on a *new* UE-gate mechanism achieving \(p>1\) (not provided by boundary \(L^2\) evaluation).
* Key conclusions (5 bullets max):
  1. Point evaluation from boundary \(L^2(\partial B,ds)\) has sharp operator blow-up \(\sim \delta^{-1/2}\); it cannot be improved within this norming.
  2. Therefore the proven UE scaling against \(\sup_{\partial B}|E'/E|\) is \(\delta^1\) (i.e., \(p=1\)), not \(\delta^{3/2}\).
  3. With \(p=1\), the collar local term becomes \(O(N_{\rm up}(m)/\kappa)\) (non-decaying), so η‑absorption tail closure (S1′) fails in its present v33 architecture.
  4. Any recovery of η‑absorption requires a structurally different UE-gate: either avoid sup-based collar blow-up or change the object/norm so the local contribution decays with \(\delta\).
  5. Minimal v34 honesty requires correcting Lemma UE and explicitly marking the UE-gate as open.
* Paste-ready manuscript edits:
  (i) revised lemma/proposition statements:
    - Add Lemma `\ref{lem:eval-L2}` (point evaluation from boundary \(L^2\); sharp \(\delta^{-1/2}\)).
    - Revise Lemma `\ref{lem:upper-envelope}`: replace \(\delta^{3/2}\) by \(\delta\) in `\eqref{eq:UE-EoverE}` and in the final combined bound.
  (ii) revised definitions/remarks:
    - Add Remark `\ref{rem:UE-gate}` explicitly stating the UE-gate obstruction for η‑absorption under the proven scaling.
  (iii) revised theorem/inequality lines:
    - None directly here (but tail inequality statements that currently rely on \(\delta^{3/2}\) become conditional on an unproved UE-gate and must be reclassified accordingly by the control room).
* Dependencies on other branches:
  - Any attempt to preserve S1′ must produce a **new UE-gate mechanism** achieving an effective \(\delta\)-power \(p>1\) against the *local* term, or redesign the envelope so the collar blow-up is avoided.
* Referee risk notes (anticipated objections + how addressed):
  - **Objection:** “Why must evaluation blow up like \(\delta^{-1/2}\)?”  
    **Addressed:** Lemma `\ref{lem:eval-L2}` + sharpness via the constant function example.
  - **Objection:** “Maybe different constants hide the \(\delta^{-1/2}\)?”  
    **Addressed:** It is a scaling/lower-bound phenomenon independent of constants.
  - **Objection:** “Then your η‑absorption closure is invalid.”  
    **Addressed:** Yes; this batch explicitly reports that S1′ fails unless UE-gate is rebuilt.
