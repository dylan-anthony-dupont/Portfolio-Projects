# RH‑LOCAL — Batch 3 (UE‑gate + local redesign viability if UE exponent drops to \(p\le 1\))
**Callsign:** RH‑LOCAL  
**Ground truth:** `manuscript_v33.tex/pdf` only  
**Primary target:** local mechanism redesign options if UE gives only a \(\delta^1\) prefactor (or worse)  
**Key dependency:** UE exponent \(p\) in Lemma `\ref{lem:upper-envelope}` and its downstream Corollary `\ref{cor:UE-residual-local}`.

---

## UE‑gate answers (required by Batch‑3 protocol)

### Q1. What UE \(\delta\)-exponent is actually supported by a proof? (best proven \(p\))
**Best proven (as written in v33’s proof chain):** \(p=1\), not \(p=3/2\).

- v33 Lemma `\ref{lem:upper-envelope}` *states* (UE):
  \[
  \sum_\pm |W(v_\pm)-e^{i\varphi_0^\pm}|\ \le\ 2C_{\rm up}\,\delta^{3/2}\,\sup_{\partial B}\Big|\frac{E'}{E}\Big|.
  \]
- But the **scale factors explicitly listed inside the proof** multiply to \(\delta^1\):
  - harmonic measure evaluation: \(\|P_B\|_\infty^{1/2}\sim \delta^{-1/2}\)  
  - Poincaré/Wirtinger on \(\partial B\): factor \(\sim\delta\)  
  - \(L^2\to\sup\) on \(\partial B\): factor \(\sim \delta^{1/2}\)  
  Multiplying: \(\delta^{-1/2}\cdot \delta \cdot \delta^{1/2}=\delta\).

**Conclusion:** as currently written, the lemma’s *proof* supports a \(\delta^1\) prefactor. Either:
- the lemma statement must be corrected to \(\delta^1\), **or**
- the proof must be modified to produce an additional \(\delta^{1/2}\) gain (this is an ENVELOPE-branch issue).

---

### Q2. Does S1′ (η‑absorption tail closure) survive under that \(p\)? (YES/NO/CONDITIONAL)
**Answer under best proven \(p=1\): NO.**  
Reason: the UE-multiplied local term becomes \(\sim N_{\rm loc}(m)/\kappa\), which grows like \(\log m\) under the best unconditional bound available in v33 (Lemma `\ref{lem:Nloc-logm}`), and therefore cannot be uniformly absorbed against a constant forcing term.

---

### Q3. What minimal v34 edits follow from the conclusion?
Minimal v34 edits (decision-grade):

1. **Add an explicit “UE exponent gate” remark** near Corollary `\ref{cor:UE-residual-local}` stating that:
   - the local contribution scales like \(\delta^{p-1}N_{\rm loc}(m)/\kappa\),
   - hence uniform tail closure requires \(p>1\) unless one proves a substantially sharper local-window bound than \(N_{\rm loc}(m)\ll\log m\).

2. If Control Room decides the proof truly only gives \(p=1\):  
   **S1′ must be retired or rebuilt** (local window redesign alone cannot salvage unconditionally with current N\(_{\rm loc}\) technology).

3. If Control Room can repair UE to restore \(p\ge 3/2\):  
   **no local redesign is needed**; the existing v33 local bound is sufficient (local term becomes \(\delta^{p-1}N_{\rm loc}/\kappa = \delta^{1/2}N_{\rm loc}/\kappa\), and with \(\delta=\eta\alpha/(\log m)^2\), this is \(O(\sqrt{\eta})\)).

---

# Task A (CRITICAL) — Growth obstruction under UE exponent \(p=1\)

Assume UE only yields (schematically)
\[
\sum_\pm |W(v_\pm)-e^{i\varphi_0^\pm}|\ \lesssim\ C_{\rm up}\,\delta\,\sup_{\partial B}\Big|\frac{E'}{E}\Big|.
\tag{UE\(_{p=1}\)}
\]

Using v33’s log-derivative split (Lemma `\ref{lem:logder-split}`) and collar bound (Lemma `\ref{lem:Zloc-logder-collar}`),
\[
\sup_{\partial B}\Big|\frac{E'}{E}\Big|
\le \sup_{\partial B}\Big|\frac{F'}{F}\Big|+\sup_{\partial B}\Big|\frac{Z'_{\rm loc}}{Z_{\rm loc}}\Big|
\le L(m)\ +\ \frac{N_{\rm loc}(m)}{\kappa\delta}.
\]

Multiplying by \(\delta\) gives the **local obstruction term**
\[
\delta\cdot \sup_{\partial B}\Big|\frac{Z'_{\rm loc}}{Z_{\rm loc}}\Big|
\le \delta\cdot \frac{N_{\rm loc}(m)}{\kappa\delta}
=\frac{N_{\rm loc}(m)}{\kappa}.
\]

Now insert v33’s unconditional explicit bound (Lemma `\ref{lem:Nloc-logm}`):
\[
N_{\rm loc}(m)\le 1.01\log m + 17\qquad(m\ge 10),
\]
so
\[
\frac{N_{\rm loc}(m)}{\kappa}\ \gtrsim\ \frac{\log m}{\kappa}\quad\to\infty\quad(m\to\infty).
\]

**Why this kills uniform tail closure:**  
In S1′, the forcing side of the tail inequality is \(m\)-uniform (a positive constant minus terms vanishing with \(\delta\)), while the UE-driven envelope side would contain a term \(\sim (C_{\rm up}/\kappa)\log m\). Thus for large \(m\), the inequality cannot hold.

This obstruction is **structural**: changing \(\delta=\eta\alpha/(\log m)^2\) does not help because the \(\delta\) cancels out of the local contribution when \(p=1\).

---

# Task B (PRIMARY) — Two redesigned local window policies (ranked), with explicit bounds

## Option 1 (Rank #1, but CONDITIONAL): Shrinking vertical window \(H(m)\) to force \(N_{\rm loc}\) bounded
### Definition change
Replace the fixed window \(|\Im\rho-m|\le 1\) by a shrinking half-width \(H(m)\in(0,1]\):
\[
Z_H(m):=\{\rho:\ E(\rho)=0,\ |\Im\rho-m|\le H(m)\},
\]
and define
\[
Z_{{\rm loc},H}(v):=\prod_{\rho\in Z_H(m)}(v-\rho)^{m_\rho},\qquad
F_H(v):=\frac{E(v)}{Z_{{\rm loc},H}(v)}.
\]

### What bound we would need (to salvage under \(p=1\))
To make UE\(_{p=1}\) absorbable, we would need a **genuinely short-interval** unconditional bound of the form
\[
N(T+H)-N(T-H)\ \le\ A_H\cdot H\log T\ +\ B_H,
\]
with explicit absolute constants \(A_H,B_H\) valid for all large \(T\) and for \(H=H(m)/2\) as small as \(\asymp 1/\log m\) (or smaller).
Then choosing \(H(m)\asymp 1/\log m\) would yield \(N_{\rm loc,H}(m)=O(1)\), and the local UE term \(\sim N_{\rm loc,H}/\kappa\) would be uniformly bounded.

### What we can prove unconditionally **with the current v33 technology**
Using only monotonicity and Lemma `\ref{lem:Nloc-logm}`, for any \(0<H(m)\le 1\) and \(m\ge 10\),
\[
N_{\rm loc,H}(m)
= N\!\left(\frac m2+\frac{H(m)}{2}\right)-N\!\left(\frac m2-\frac{H(m)}{2}\right)
\le N\!\left(\frac m2+1\right)-N\!\left(\frac m2-1\right)
\le 1.01\log m + 17.
\]
This bound **does not improve with shrinking \(H(m)\)**, and therefore does **not** salvage UE\(_{p=1}\).

### Compatibility note
This option would force a re-audit of:
- the residual envelope lemma (since \(F\) becomes \(F_H\) and inherits additional nearby zeros),
- any step that uses the window’s fixed width (e.g., any “difference-of-windows” bookkeeping).

**Status:** **CONDITIONAL** (requires new analytic input beyond v33’s current explicit N(T) technology).

---

## Option 2 (Rank #2, CONDITIONAL and more invasive): δ‑coupled window \(H(m,\delta)\) + δ‑shrinking isolation
### Definition change
Tie the window to the box scale, e.g.
\[
Z_{\delta}(m):=\{\rho:\ E(\rho)=0,\ |\Im\rho-m|\le c\,\delta\},
\]
for a fixed shape-only constant \(c\ge 1\) (say \(c=10\) to cover a buffered collar band).
Define \(Z_{{\rm loc},\delta}\) and \(F_\delta\) analogously.

### Intended mechanism under UE\(_{p=1}\)
Because \(Z_\delta(m)\) shrinks when \(\delta\) shrinks, one hopes to reduce \(N_{{\rm loc},\delta}(m)\) by taking a smaller admissible \(\delta\), using Lemma `\ref{lem:collar-existence}` + δ‑shrinking monotonic safety.

### Explicit unconditional bound available now
Again, monotonicity + Lemma `\ref{lem:Nloc-logm}` yields only
\[
N_{{\rm loc},\delta}(m)\le 1.01\log m + 17\qquad(m\ge 10),
\]
independent of \(\delta\), so this does **not** yield a uniform bound under UE\(_{p=1}\) without new short-interval technology.

### Compatibility note
This is more invasive than Option 1:
- the residual envelope lemma would need to be rederived for \(F_\delta\),
- any step using a fixed “±1 window” would need rewriting,
- the certificate scaffolding would have to track the \(\delta\)-dependent window.

**Status:** **CONDITIONAL** (and higher integration cost than Option 1).

---

## Viability ranking (local-only conclusion)
1. **Option 1 (shrinking \(H(m)\sim 1/\log m\))** — best conceptual fit, but still **conditional** on a new short-interval zero-count bound with explicit constants.  
2. **Option 2 (δ-coupled \(H\))** — conditional and substantially more invasive; not recommended unless the program accepts a major rework.

**Local branch conclusion:** With only the explicit N(T) technology currently in v33, **no window policy change can make the UE\(_{p=1}\) local contribution uniformly absorbable.**

---

# Task C — v34‑ready patch set (surgical edits)

## C1) Add an explicit “UE exponent gate” remark (recommended regardless of decision)
**Paste-ready remark** (place immediately after Corollary `\ref{cor:UE-residual-local}`):

```tex
\begin{remark}[UE exponent gate and the local term]
Let Lemma~\ref{lem:upper-envelope} hold with a prefactor $\delta^{p}$, i.e.
$\sum_\pm |W(v_\pm)-e^{i\varphi_0^\pm}|\ll \delta^{p}\sup_{\partial B}|E'/E|$.
Routing through the split $E'/E=F'/F+Z'_{\rm loc}/Z_{\rm loc}$ and the collar bound
$\sup_{\partial B}|Z'_{\rm loc}/Z_{\rm loc}|\le N_{\rm loc}(m)/(\kappa\delta)$ yields a local contribution
of size $\delta^{p-1}\,N_{\rm loc}(m)/\kappa$.
With only the unconditional bound $N_{\rm loc}(m)\ll \log m$, uniform tail closure requires $p>1$.
In particular, if $p=1$ then the local term is $\asymp N_{\rm loc}(m)/\kappa$, which grows like $\log m$
and cannot be absorbed uniformly in $m$ by a constant forcing margin.
\end{remark}
```

## C2) If Control Room insists on a window redesign despite UE\(_{p=1}\) (conditional patches)
I do **not** recommend integrating these unless the program explicitly accepts new analytic assumptions,
but here are minimal paste-ready definitions/lemmas for Option 1 to “make the dependence explicit”.

### Revised definition (Option 1: shrinking \(H(m)\))
```tex
\begin{definition}[Shrinking local window]\label{def:Zloc-H}
Fix a window half-width function $H:[m_\star,\infty)\to(0,1]$.
Define
\[
Z_H(m):=\{\rho:\ E(\rho)=0,\ |\ImPart\rho-m|\le H(m)\},
\qquad
Z_{{\rm loc},H}(v):=\prod_{\rho\in Z_H(m)}(v-\rho)^{m_\rho},
\qquad
F_H(v):=\frac{E(v)}{Z_{{\rm loc},H}(v)}.
\]
Let $N_{{\rm loc},H}(m)$ denote the cardinality of $Z_H(m)$ with multiplicity.
\end{definition}
```

### Trivial explicit bound available without new theory (not sufficient for closure)
```tex
\begin{lemma}[Trivial bound for $N_{{\rm loc},H}$]\label{lem:NlocH-trivial}
For $m\ge 10$ and any $0<H(m)\le 1$,
\[
N_{{\rm loc},H}(m)\le 1.01\log m + 17.
\]
\end{lemma}
```

### Conditional lemma you would *need* to salvage UE\(_{p=1}\) (DO NOT CLAIM without proof)
```tex
\begin{lemma}[Short-interval zero bound (needed for UE$_{p=1}$)]\label{lem:NlocH-short}
Assume there exist explicit constants $A,B,T_0$ such that for all $T\ge T_0$ and all $0<H\le 1$,
\[
N(T+H)-N(T-H)\le A\,H\log T + B.
\]
Then choosing $H(m)=c/\log m$ yields $N_{{\rm loc},H}(m)\le (A c)+B$ for all sufficiently large $m$,
and the UE$_{p=1}$ local contribution is uniformly bounded.
\end{lemma}
```

---

# MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* **Callsign:** RH‑LOCAL
* **Result classification:** **FAIL** (under best proven \(p=1\), no unconditional local window redesign salvages S1′ with current v33 local technology)
* **Target gaps closed (by ID):**
  - None newly closed in Batch‑3. (G‑8 remains “formally closed” as an explicit inequality, but is insufficient if UE drops to \(p=1\).)
* **Target gaps still open (by ID):**
  - UE exponent gate (ENVELOPE branch; local consequence documented here)
  - S1′ viability under UE\(_{p=1}\) (global mechanism)
* **Key conclusions (5 bullets max):**
  1. v33’s UE proof chain (as written) supports a \(\delta^1\) prefactor, not \(\delta^{3/2}\); this re-opens the UE gate.  
  2. Under \(p=1\), the UE‑multiplied local term becomes \(N_{\rm loc}(m)/\kappa\), and with v33’s unconditional bound \(N_{\rm loc}(m)\asymp\log m\), uniform tail closure fails.  
  3. Shrinking the local window (either \(H(m)\) or \(H(m,\delta)\)) does not help unless one has a *true* short-interval zero-count bound with explicit constants depending on \(H\).  
  4. No such short-interval bound is available from the current v33 input (which only bounds \(N(T)\) in magnitude, not its short-interval variation).  
  5. Minimal v34 action is to add an explicit “UE exponent gate” remark and decide: repair UE to \(p>1\) or retire/rebuild S1′.

* **Paste-ready manuscript edits:**
  (i) **revised lemma/proposition statements**  
  - None (local). UE lemma exponent issue is upstream; see remark gate below.

  (ii) **revised definitions/remarks**  
  - Add the “UE exponent gate” remark (snippet C1 above) after Corollary `\ref{cor:UE-residual-local}`.

  (iii) **revised theorem/inequality lines**  
  - None locally unless the program accepts a redesigned window (then use Option‑1 definition/lemmas above, marked conditional).

* **Dependencies on other branches:**
  - **RH‑ENVELOPE:** must resolve whether UE exponent is truly \(p=3/2\) or only \(p=1\); local consequences are decisive.  
  - **RH‑ABSORB / Control Room:** if UE is \(p=1\), must decide to retire S1′ or introduce new analytic input; local redesign alone is insufficient.

* **Referee risk notes (anticipated objections + how addressed):**
  - **Objection:** “Your conclusion depends on an internal scaling arithmetic.”  
    **Response:** The proof steps in Lemma `\ref{lem:upper-envelope}` explicitly list the three scale factors; their product is \(\delta\). If ENVELOPE supplies the missing \(\delta^{1/2}\) gain, this FAIL becomes a PASS.  
  - **Objection:** “Can’t we just shrink the window?”  
    **Response:** With the current unconditional N(T) input (magnitude bound only), shrinking \(H\) does not improve the bound; it stays \(O(\log m)\). A genuine short-interval bound is required.  
  - **Objection:** “Couldn’t the zeros be well-spaced in practice?”  
    **Response:** The manuscript is required to be unconditional/audit-grade; spacing is not available as a theorem with explicit constants in the required generality, so it cannot be assumed.
