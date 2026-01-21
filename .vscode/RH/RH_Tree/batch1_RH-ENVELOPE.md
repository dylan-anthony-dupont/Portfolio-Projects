## RH-ENVELOPE — G‑2 Closeout (W-control chain alignment)

This branch is correctly scoped: **G‑2 / E‑5** is the “object mismatch” problem: pre‑v32, parts of the manuscript attempted to control the **inner quotient** \(W:=E/G_{\rm out}\) using **residual-only** bounds (typically \(\sup|F'/F|\)), even though the *actual* upper-envelope lemma for dial deviation must depend on \(\sup_{\partial B}|E'/E|\). v32 explicitly identifies and corrects this by (i) restating UE in “outer-aligned form” with \(E'/E\), then (ii) splitting \(E'/E = F'/F + Z_{\rm loc}'/Z_{\rm loc}\) and collar-bounding the local term. This is the right repair direction. citeturn11file14

Below is the requested **invocation inventory**, **mismatch report**, and a **v33-ready canonical lemma chain** plus **paste-ready patch edits**.

---

# 1) Invocation inventory: every place W-control is claimed/needed

I list each **invocation site** with (i) *object controlled*, (ii) *hypotheses / domain*, and (iii) *downstream dependency*.

### I.1 Bridge 1 inner quotient definition + constancy criterion (certification path)
- **Where:** v32 defines \(G_{\rm out}\) by the Dirichlet problem with boundary data \(\log|E|\), defines \(W:=E/G_{\rm out}\), and states “\(|W|=1\) on \(\partial B\)”. Then **Bridge 1**: if \(W\) is analytic and **zero-free** on \(B\), continuous on \(\overline B\), and \(|W|=1\) on \(\partial B\), then \(W\) is constant. citeturn7file0
- **Object controlled:** *Not a quantitative bound*; it is a **rigidity implication** (“unimodular + zero-free ⇒ constant”).
- **Domain/hypotheses:** box \(B(\alpha,m,\delta)\), boundary-contact (“\(E\) has no zeros on \(\partial B\)”), plus the stronger **zero-free** hypothesis for \(W\) in Bridge 1.
- **Downstream dependency:** certification logic and “boundary modulus program”; *not* the quantitative tail contradiction itself.

**Branch scope note:** Bridge‑1 hypotheses tracking is **G‑6**, not owned here, but it is part of the W‑spine vocabulary.

---

### I.2 Upper envelope (UE) dial deviation — quantitative W-control core
- **Where (v32):** **Lemma 10.2 “Upper envelope bound (outer-aligned form)”**: for an aligned box \(B=B(\pm a,m,\delta)\), with boundary-contact (no zeros of \(E\) on \(\partial B\)), define dial centers \(v_\pm=\pm a+im\) and best constant phases \(e^{i\varphi_0^\pm}\). Then
\[
\sum_{\pm}\bigl|W(v_\pm)-e^{i\varphi_0^\pm}\bigr|
\le 2C_{\rm up}\,\delta^{3/2}\,\sup_{v\in\partial B}\Bigl|\frac{E'(v)}{E(v)}\Bigr|.
\]
citeturn7file0turn11file0
- **Object controlled:** **Dial deviation of \(W\)** at the dial centers, *in terms of* \(\sup_{\partial B}|E'/E|\).  
  This is exactly the object alignment required to close G‑2.
- **Domain/hypotheses:** aligned box \(B(\pm a,m,\delta)\); boundary-contact so \(E'/E\) is defined on \(\partial B\); shape-only constant \(C_{\rm up}\).
- **Downstream dependency:** this is the left-hand “upper envelope” input used in the **tail inequality** assembly.

---

### I.3 UE conversion to “residual+local” form — the v32 repair move
- **Where (v32):** Definition 10.3 **\(\kappa\)-admissibility** (collar policy), Lemma 10.4 **log-derivative split**, Lemma 10.5 **buffered local factor bound**, Lemma 10.6 **\(N_{\rm loc}(m)\ll\log m\)**, then **Corollary 10.7**:
\[
\sum_{\pm}|W(v_\pm)-e^{i\varphi_0^\pm}|
\le 2C_{\rm up}\left(\delta^{3/2}L(m) + \delta^{1/2}\frac{N_{\rm loc}(m)}{\kappa}\right)
\]
assuming the residual envelope bound \(\sup_{\partial B}|F'/F|\le L(m)\). citeturn7file0turn11file0
- **Object controlled:** still **dial deviation of \(W\)**, but now expressed as **residual + local** contributions.
- **Domain/hypotheses:** must have:
  - **boundary-contact** (so log-derivatives on \(\partial B\) are legal),
  - **\(\kappa\)-admissible** collar: \(\operatorname{dist}(\partial B,\mathcal Z(E))\ge\kappa\delta\),
  - the residual lemma \(\sup|F'/F|\le C_1\log m+C_2\),
  - the local window bound \(N_{\rm loc}(m)\le A_N\log m+B_N\).
- **Downstream dependency:** this is the **only valid interface** between (residual) log-derivative technology and (W) dial deviation.

---

### I.4 Tail inequality assembly — where W-control is actually consumed
- **Where (v32):** **Theorem 11.1 (Tail inequality, post-pivot)** uses the UE bound in residual+local form on the left-hand side:
\[
2C_{\mathrm{up}}\Bigl(\delta^{3/2}L(m)\; +\; \delta^{1/2}\,\frac{N_{\rm up}(m)}{\kappa}\Bigr)
< c - \delta(\cdots)
\]
and its proof sketch explicitly says: UE is in terms of \(\sup|E'/E|\), then split and bound the local term to recover the LHS. citeturn11file0turn7file0turn11file14
- **Object controlled:** the exact **dial deviation** quantity that the forcing inequality competes against.
- **Domain/hypotheses:** \(m\ge10\), \(\eta\in(0,1)\), \(\alpha\in(0,1]\), aligned box \(B(\pm\alpha,m,\delta)\) that is \(\kappa\)-admissible.
- **Downstream dependency:** contradiction “forcing > budget+UE” ⇒ no off-axis quartet at height \(m\); then tail closure/global closure.

---

# 2) Mismatch report (residual-only proxy bounds) — what remains, and how to patch

## M.1 Structurally fatal proxy (v30/v31): UE stated in residual form
- **Where (v31):** Lemma 10.2 “Upper envelope bound (residual form)” states dial deviation of \(W\) is bounded by \(\sup_{\partial B}|F'/F|\):
\[
\sum_\pm |W(v_\pm)-e^{i\phi_0^\pm}| \le 2C_{\rm up}\delta^{3/2}\sup_{\partial B}\left|\frac{F'}{F}\right|.
\]
citeturn11file10turn11file12
- **Why this is a mismatch:** \(W=E/G_{\rm out}\) is built from \(E\), and the UE proof structure controls **\(\partial_s\log E\)** (equivalently \(\sup|E'/E|\)) on \(\partial B\). Replacing \(E'/E\) by \(F'/F\) *silently deletes* the local term \(Z_{\rm loc}'/Z_{\rm loc}\), which can be large near \(\partial B\) without a collar buffer.
- **Classification:** **structurally fatal** (this is precisely G‑2/E‑5). It breaks the tail inequality’s left-hand control because the object being bounded is the wrong log-derivative.

**Exact replacement:** v33 must not contain any lemma of the form “dial deviation of \(W\) \(\lesssim \sup|F'/F|\)” unless it is explicitly routed through the **split + collar** producing a residual+local term (Cor. 10.7 in v32).

---

## M.2 Harmless residual control (v32): Horizontal budget is intentionally residual
- **Where (v32):** the “Horizontal non-forcing phase budget” \(\Delta_{\rm nonforce}\) is explicitly defined using the **residual factor \(F\)** and bounded by \(\sup|F'/F|\). citeturn11file15
- **Why harmless:** this is **not** attempting to control \(W\). It is controlling the residual phase variation after removing local zeros. This is a distinct object with distinct role.
- **Classification:** **harmless**, but must be clearly signposted as “HB is residual; UE is inner-quotient; do not mix.”

---

## M.3 Remaining “proxy risk” in v32 text: interface clarity (not math, but audit fragility)
Even though v32’s *math interface* is corrected, it still benefits from an explicit “no proxying” remark so that future revisions don’t reintroduce the v31 error by shortcutting “residual envelope ⇒ UE”.

- **Patch recommendation:** add an explicit remark immediately after Lemma 10.2 or before Corollary 10.7:
  - UE controls \(W\) via \(E'/E\),
  - residual lemma controls \(F'/F\),
  - any substitution **must** use the split plus collar bound.

---

# 3) Canonical v33-ready W-control chain (minimal lemmas + precise hypotheses)

Below is the **minimal chain** that closes G‑2 in a referee-auditable way. I’m stating it in “module form” so you can paste it into a v33 plan/DAG.

### (W0) Outer/inner factorization on a box
**Hypotheses:** \(B=B(\alpha,m,\delta)\) simply connected with Lipschitz boundary; **boundary-contact**: \(E\neq0\) on \(\partial B\).  
**Conclusion:** define \(G_{\rm out}=\exp(U+iV)\) from \(\log|E|\) on \(\partial B\); then \(G_{\rm out}\) analytic and zero-free on \(B\), \(|G_{\rm out}|=|E|\) on \(\partial B\); define \(W=E/G_{\rm out}\) analytic on \(B\) and \(|W|=1\) a.e. on \(\partial B\). citeturn7file0

### (W1) Upper envelope bound is outer-aligned and uses \(\sup|E'/E|\)
**Hypotheses:** aligned box \(B=B(\pm\alpha,m,\delta)\); boundary-contact.  
**Conclusion (dial deviation):**
\[
\sum_{\pm}|W(v_\pm)-e^{i\varphi_0^\pm}|
\le 2C_{\rm up}\,\delta^{3/2}\sup_{\partial B}\left|\frac{E'}{E}\right|.
\]
(UE must *never* be stated in terms of \(F'/F\) alone.) citeturn7file0turn11file0

### (W2) Collar policy for local poles (κ-admissibility)
**Hypotheses:** fixed \(\kappa\in(0,1/10)\).  
**Definition:** \(B\) is \(\kappa\)-admissible if \(\operatorname{dist}(\partial B,\mathcal Z(E))\ge\kappa\delta\).  
**Convention:** if not, shrink \(\delta\) until it holds. citeturn7file0turn11file0

### (W3) Log-derivative split
**Hypotheses:** \(E\) and \(Z_{\rm loc}\) holomorphic and nonvanishing on \(\partial B\) (ensured by boundary-contact and collar).  
**Conclusion:**
\[
\frac{E'}{E}=\frac{F'}{F}+\frac{Z_{\rm loc}'}{Z_{\rm loc}}.
\]
citeturn7file0turn11file0

### (W4) Collar bound for the local term
**Hypotheses:** \(\kappa\)-admissible.  
**Conclusion:**
\[
\sup_{\partial B}\left|\frac{Z_{\rm loc}'}{Z_{\rm loc}}\right|\le \frac{N_{\rm loc}(m)}{\kappa\delta}.
\]
citeturn7file0turn11file0

### (W5) Residual bound (external / other branch)
**Hypotheses:** RH-free classical input after deleting local zeros.  
**Conclusion:** \(\sup_{\partial B}|F'/F|\le C_1\log m+C_2\) uniformly in \(\alpha,\delta\). (Not proven in this branch.)

### (W6) Combine (W1)+(W3)+(W4)+(W5)
**Conclusion (the only valid residual interface):**
\[
\sum_{\pm}|W(v_\pm)-e^{i\varphi_0^\pm}|
\le 2C_{\rm up}\left(\delta^{3/2}L(m)+\delta^{1/2}\frac{N_{\rm loc}(m)}{\kappa}\right),
\]
with \(L(m)=C_1\log m+C_2\). citeturn7file0turn11file14

That closes G‑2 at the object level: **W-control is always via \(E'/E\)**, and residual technology is attached only via the explicit split.

---

# 4) Patch-ready edits (v33) to eliminate proxying and lock the correct object

These edits are designed to be “paste-ready” into `manuscript_v32.tex` as a v33 delta.

## 4.1 Add an explicit “no proxying” remark (prevents v31 regression)

**Insert immediately after Lemma `lem:upper-envelope` (Lemma 10.2):**
```tex
\begin{remark}[No residual proxying in UE]
Lemma~\ref{lem:upper-envelope} controls the \emph{inner quotient} $W=E/G_{\rm out}$ and therefore
depends on $\sup_{\partial B}|E'/E|$.  Bounds on the \emph{residual factor} $F=E/Z_{\rm loc}$ control
$\sup_{\partial B}|F'/F|$ and do \emph{not} by themselves bound $\sup_{\partial B}|E'/E$.
Whenever the residual envelope lemma is used to control dial deviation, it \emph{must} be routed through
the log-derivative split
\[
E'/E = F'/F + Z'_{\rm loc}/Z_{\rm loc}
\]
(Lemma~\ref{lem:logder-split}) together with the collar bound on $Z'_{\rm loc}/Z_{\rm loc}$
(Lemma~\ref{lem:Zloc-logder-collar}), yielding Corollary~\ref{cor:UE-residual-local}.
\end{remark}
```

## 4.2 Tighten the UE→tail interface language (make the dependency explicit)

**Replace the first two sentences of the Proof sketch of Theorem `thm:tail-inequality` with:**
```tex
The forcing side is unchanged from v31.  The post-pivot point is that dial deviation is controlled
\emph{only} via Lemma~\ref{lem:upper-envelope}, which is an $E'/E$ bound for the inner quotient $W$.
To connect this to the residual envelope lemma for $F'/F$, we invoke the split
$E'/E=F'/F+Z'_{\rm loc}/Z_{\rm loc}$ (Lemma~\ref{lem:logder-split}) and the collar bound
(Lemma~\ref{lem:Zloc-logder-collar}), i.e. Corollary~\ref{cor:UE-residual-local}.
```

## 4.3 Quantifier hygiene for \(\delta\) under collar shrink (interface-level patch)

This is not “new math” but removes a common audit failure mode: Theorem 11.1 currently *sets* \(\delta=\eta\alpha/(\log m)^2\) while Definition 10.3 permits shrinking \(\delta\). Make it explicit that \(\delta\) is at most the nominal scale and the worst case is the maximum \(\delta\).

**In Section `sec:tail`, replace:**
```tex
\delta:=\delta(m,\alpha):=\frac{\eta\alpha}{(\log m)^2}.
```
**with:**
```tex
\delta_0:=\delta_0(m,\alpha):=\frac{\eta\alpha}{(\log m)^2},\qquad
\delta\in(0,\delta_0]\ \text{chosen so that $B(\pm\alpha,m,\delta)$ is $\kappa$--admissible.}
```

**And in Theorem `thm:tail-inequality` statement, change “$B=B(\pm\alpha,m,\delta)$” to “$B=B(\pm\alpha,m,\delta)$ with $\delta\le\delta_0(m,\alpha)$”.**

(You already have the collar policy; this patch just prevents a referee from flagging “\(\delta\) is both fixed and variable”.)

## 4.4 (Optional but strongly recommended within W-control scope) Flag UE scaling proof discrepancy

Your own deep-research note explicitly identifies a \(\delta^{3/2}\) scaling issue in the Lemma 10.2 proof sketch, with a proposed fix via a quadratic/RMS combination step. citeturn11file1turn11file5

I am **not** rewriting the full proof here (that’s a separate dedicated patch), but for audit safety add a one-line note inside the Lemma 10.2 proof:

```tex
% NOTE (audit): the $\delta^{3/2}$ scaling requires an $L^2$ (RMS) combination step; see Deliverable C
% in v32_status_decision_Deep_Research for the patch outline.
```

---

# 5) Conclusion: does this close G‑2?

**Yes at the “object alignment” level**: v32 already has the right architecture:
- UE depends on \(\sup|E'/E|\) (correct object),
- residual lemma bounds \(\sup|F'/F|\) (different object),
- collar + split converts residual into an \(E'/E\) bound with an explicit local term. citeturn7file0turn11file14

**Remaining fragility is not G‑2 itself**, but:
- the UE proof scaling patch (still within W-control spine as a rigor issue),
- the collar-policy monotonicity bookkeeping (interface-level),
- the residual envelope lemma completeness (other branch).

---

## MANDATORY PATCH PACKET FORMAT

- **Prompt Batch Number:** 1

- **Callsign:** RH-ENVELOPE

- **Result classification:** CONDITIONAL

- **Target gaps closed (by ID):**  
  - G‑2 (W-control object mismatch) — **closed at architecture/interface level** via v32’s UE(\(E'/E\)) + split + collar.

- **Target gaps still open (by ID):**  
  - G‑4 (δ‑uniformity / collar monotonicity) — interface quantifiers still need explicit tightening (patch suggested above).  
  - G‑6 (Bridge‑1 hypotheses formalization) — referenced but not owned here.  
  - G‑1 / G‑12 (residual envelope completeness + constant provenance) — required to *numerically* instantiate UE-residual-local bound.  
  - (W-control rigor note) UE scaling proof patch (Lemma 10.2) — flagged in deep research; recommended insert.

- **Key conclusions (≤5 bullets):**
  1. v30/v31’s “UE residual form” is a **structurally fatal proxy**: it bounds \(W\) using \(\sup|F'/F|\) without the missing local term. citeturn11file10turn11file12  
  2. v32 repairs the mismatch correctly: UE is stated in terms of \(\sup|E'/E|\) and only converted to residual form via \(E'/E=F'/F+Z'_{\rm loc}/Z_{\rm loc}\) plus collar control. citeturn7file0turn11file14  
  3. Horizontal budget remaining in residual form is **not a mismatch** (it controls \(\Delta_{\rm nonforce}\) for \(F\), not \(W\)). citeturn11file15  
  4. The manuscript should explicitly prohibit “residual proxying” to prevent regression back to the v31 error.  
  5. Lemma 10.2’s \(\delta^{3/2}\) proof scaling remains an **audit-grade rigor risk** (deep research patch exists). citeturn11file1turn11file5

- **Paste-ready manuscript edits:**
  - **(i) Revised lemma/proposition statements**
    - *No change required to Lemma 10.2 statement* (already \(E'/E\)). Add “No residual proxying” remark (below).
    - *Theorem 11.1 quantifier hygiene:* change \(\delta\) definition to \(\delta\le\delta_0\) (see §4.3 edits).
  - **(ii) Revised definitions/remarks**
    - Insert the **Remark [No residual proxying in UE]** exactly as in §4.1.
    - Update the \(\delta\) setup paragraph in `sec:tail` to use \(\delta_0\) and choose \(\delta\le\delta_0\) for \(\kappa\)-admissibility (see §4.3).
  - **(iii) Revised theorem/inequality lines**
    - Replace the opening sentences of the Proof sketch of `thm:tail-inequality` with the text in §4.2 to lock the interface UE(\(E'/E\)) → split → corollary.

- **Dependencies on other branches:**
  - Residual envelope lemma completeness and \((\alpha,\delta)\)-uniformity (G‑1/G‑12).  
  - Collar-policy monotonicity bookkeeping (G‑4/G‑5).  
  - Bridge‑1 hypotheses formalization if certification path is used (G‑6).  
  - Tail assembly constants derivation (G‑3) is not owned here, but is needed for global closure.

- **Referee risk notes: anticipated objections + how addressed**
  1. **Objection:** “You bound the wrong object: \(F'/F\) does not control \(W\).”  
     **Addressed:** v33 must enforce the v32 architecture: UE uses \(E'/E\) and residual enters only via split + collar; add “No residual proxying” remark to prevent drift.
  2. **Objection:** “Your log-derivatives require nonvanishing on the contour.”  
     **Addressed:** boundary-contact convention + \(\kappa\)-admissibility is explicitly invoked; tightening \(\delta\le\delta_0\) resolves collar shrink ambiguity.
  3. **Objection:** “The UE proof scaling is inconsistent.”  
     **Addressed:** flag as conditional; deep research patch exists and should be integrated explicitly into Lemma 10.2 proof before external submission.
