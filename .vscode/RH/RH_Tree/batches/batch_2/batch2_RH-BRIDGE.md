# RH-BRIDGE — Batch 2 (v33 base)
**Scope:** G-6 merge audit (Bridge-1 / outer-factor integration) + G-10 label integrity around Bridge.

This is a **v33-only** audit. All findings and edits below are keyed to the current v33 objects/labels:
- `\section{Outer factorization and the inner quotient (Bridge 1)}\label{sec:bridge1}`
- `\lemma{Dirichlet outer factor on a box}\label{lem:outer_dirichlet_box}`
- `\proposition{Bridge 1: zero-free inner collapse}\label{prop:bridge1}`
- `\remark{Boundary modulus convention}\label{rem:boundary_modulus}`
- `\lemma{Upper envelope bound (outer-aligned form)}\label{lem:upper-envelope}`
- `\definition{Collar-admissible aligned boxes}\label{def:collar-admissible}`
- `\lemma{Existence of a \kappa--admissible shrink}\label{lem:collar-existence}`


---

## Task A (HIGH): Bridge-1 integration audit (v33 correctness sweep)

### A1) Residual max-modulus Bridge-1 check (old Prop 9.1 style)
**Result: PASS.**

A text-level sweep of `manuscript_v33.tex` finds **no remaining** instances of the old max-modulus Bridge-1 posture:
- No occurrences of “maximum modulus”, “apply maximum modulus to \(W\) and \(1/W\)”
- No occurrences of “\(1/W\)” / “\(W^{-1}\)” in the Bridge context
- No references to “Proposition 9.1” (or any earlier numbering)

Bridge-1 appears only as the **Dirichlet outer factor + Dirichlet-uniqueness collapse** package in Section `\ref{sec:bridge1}`.

---

### A2) Bridge-1 statement hygiene (domain, hypotheses, boundary modulus meaning)
**Result: PASS (already referee-stable).**

v33’s Bridge-1 package is now hypothesis-clean:

1. **Domain control (open vs closed):**
   - v33 explicitly distinguishes **closed box** \(B\) vs **interior** \(B^\circ\).
   - Outer factor \(G_{\mathrm{out}}\) is constructed on \(B^\circ\) with boundary modulus stated as **interior limits** on \(\partial B\) (`\ref{lem:outer_dirichlet_box}`).
   - Bridge collapse is proved on \(B^\circ\) (`\ref{prop:bridge1}`).

2. **Boundary-contact / log-continuity:**
   - The outer-factor lemma assumes: \(E\) holomorphic near \(\overline B\) and \(E\neq 0\) on \(\partial B\). This is the exact minimal condition needed to assert \(\log|E|\in C(\partial B)\).

3. **Meaning of “\(|W|=1\) on \(\partial B\)” and compatibility with traces:**
   - v33 includes a dedicated remark (`\ref{rem:boundary_modulus}`) that makes the bridge unattackable on pointwise-vs-a.e. ambiguity:
     - pointwise **in modulus** as interior limits on \(\partial B\);
     - usable **a.e.** for boundary integrals without changing meaning.

**Acceptance test check:** A referee cannot reasonably attack Bridge-1 on:
- “you need \(W\in C(\overline B)\)” (you do not; you use Dirichlet uniqueness + open mapping),
- “you only know a.e. boundary modulus” (you explicitly state interior-limit modulus and then a.e. as a corollary for integrals).

---

### A3) Boundary-contact alignment with \(\kappa\)-admissibility policy (\(\delta\)-shrinking)
**Result: PASS mathematically; MINOR merge-hardening recommended.**

- v33 has a **global** admissibility policy:
  - `\ref{def:collar-admissible}` defines \(\kappa\)-admissible boxes by a positive collar distance between \(\partial B\) and zeros of \(E\),
  - `\ref{lem:collar-existence}` guarantees existence of a \(\kappa\)-admissible shrink \(0<\delta\le\delta_0\),
  - and the text explicitly states the program shrinks \(\delta\) until \(\kappa\)-admissibility holds.

This implies boundary-contact (no zeros on \(\partial B\)) whenever \(B\) is \(\kappa\)-admissible.

**Merge-hardening issue:** Section `\ref{sec:bridge1}` currently states boundary-contact as a convention but does not explicitly point to the \(\kappa\)-admissibility mechanism that enforces it. This is not a logical gap, but it is an avoidable referee “where do you guarantee this?” objection.

**Action:** add a one-line cross-reference at the start of Section `\ref{sec:bridge1}` (see edits below).

---

### A4) Consistency with Upper Envelope (UE) boundary-trace usage
**Result: PASS; MINOR wording/linking recommended.**

`\ref{lem:upper-envelope}` and its proof use \(L^2(\partial B)\) and explicitly invoke “\(|W|=1\) a.e. on \(\partial B\)” in the boundary-operator chain.

This is consistent with Bridge-1:
- Bridge-1 gives interior-limit modulus identity pointwise (in modulus),
- `\ref{rem:boundary_modulus}` explicitly licenses using that identity “in the a.e. sense” for boundary integrals.

**Merge-hardening issue:** UE currently uses mixed notation (`G_{\rm out}` vs `G_{\mathrm{out}}`) and cites Section `\ref{sec:bridge1}` but not the boundary-modulus remark explicitly. This is not a logical gap, but it is easy to tighten.

**Action:** (i) standardize the `G_{\mathrm{out}}` notation in UE lines, and (ii) add an explicit pointer to `\ref{rem:boundary_modulus}` where UE assumes unimodularity (see edits below).

---

## Task B (MED): G-10 cleanup near Bridge (labels + wording standardization)

### B1) Broken cross-references / placeholder scan near Bridge
**Result: PASS.**

- No “??” placeholders detected.
- No duplicate labels.
- Existing forward/back references around Bridge compile cleanly (Section `\ref{sec:bridge1}` is referenced from UE; Bridge objects carry labels).

### B2) Recommended surgical edits (merge-hardening; no math changes)
Edits below are **purely** (i) cross-reference hardening, (ii) terminology standardization, and (iii) notation unification.

---

# Paste-ready manuscript edits (v33 only)

## Edit 1 — Bridge section intro: explicitly tie boundary-contact to \(\kappa\)-admissible shrinking

**Target location:** Immediately after:
```tex
We work on a fixed box $B=B(\alpha,m,\delta)$ and write $B^\circ$ for its interior.
Assume the boundary-contact convention: $E$ has no zeros on $\partial B$.
```

**Replace with:**
```tex
We work on a fixed closed box $B=B(\alpha,m,\delta)$ and write $B^\circ$ for its interior.
Assume the boundary-contact convention: $E$ has no zeros on $\partial B$.
(When needed, boundary-contact can always be enforced by shrinking $\delta$ until $B$ is $\kappa$--admissible;
see Definition~\ref{def:collar-admissible} and Lemma~\ref{lem:collar-existence}.)
```

---

## Edit 2 — Upper Envelope statement: unify \(G_{\mathrm{out}}\) notation and point directly to boundary-modulus convention

**Target location:** In Lemma `\ref{lem:upper-envelope}`, replace the block:
```tex
Let $B=B(\pm a,m,\delta)$ be an aligned box and let $G_{\rm out}$ be the outer factor on $B$
constructed from $\log|E|$ on $\partial B$ (Section~\ref{sec:bridge1}). Define the inner quotient
\[
W(v):=\frac{E(v)}{G_{\rm out}(v)}.
\]
Assume the boundary-contact convention: $E$ has no zeros on $\partial B$ (hence $W$ has unimodular
boundary values a.e.).
```

**Replace with:**
```tex
Let $B=B(\pm a,m,\delta)$ be an aligned box and let $G_{\mathrm{out}}$ be the outer factor on $B^\circ$
constructed from $\log|E|$ on $\partial B$ (Section~\ref{sec:bridge1}). Define the inner quotient
\[
W(v):=\frac{E(v)}{G_{\mathrm{out}}(v)}.
\]
Assume the boundary-contact convention: $E$ has no zeros on $\partial B$.
Then $|W|=1$ holds on $\partial B$ in the interior-limit sense, and the boundary trace is unimodular a.e.
(Remark~\ref{rem:boundary_modulus}).
```

---

## Edit 3 — UE remark/proof: unify \(G_{\mathrm{out}}\) notation (no semantic change)

**Target locations:** Replace the following occurrences:

1) Remark `\ref{rem:no-proxying}`:
```tex
W=E/G_{\rm out}
```
→
```tex
W=E/G_{\mathrm{out}}
```

2) UE proof step 3:
```tex
\log G_{\rm out}
```
→
```tex
\log G_{\mathrm{out}}
```

and similarly:
```tex
\partial_s\log G_{\rm out}
```
→
```tex
\partial_s\log G_{\mathrm{out}}
```

and:
```tex
\log W=\log E-\log G_{\rm out}
```
→
```tex
\log W=\log E-\log G_{\mathrm{out}}
```

These are strictly notational standardizations to prevent a referee from asking whether `G_{\rm out}` and `G_{\mathrm{out}}` are distinct objects.

---

# MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* Callsign: RH-BRIDGE
* Result classification: **PASS** (with recommended merge-hardening edits; no logical defects detected in v33 Bridge-1)
* Target gaps closed (by ID): **G-6** (confirmed integrated in v33), **G-10 (Bridge-local label integrity)** (no broken refs/placeholders in Bridge neighborhood)
* Target gaps still open (by ID): None within RH-BRIDGE scope. (Downstream dependency remains: wherever Bridge-1 is invoked, some other branch must supply the **zero-free-on-\(B^\circ\)** premise.)
* Key conclusions (5 bullets max):
  1. v33 contains **no residual** max-modulus Bridge-1 artifact; the only Bridge-1 is the Dirichlet-outer-factor + Dirichlet-uniqueness collapse package.
  2. Bridge-1 in v33 is domain-clean: closed \(B\), interior \(B^\circ\), boundary modulus via **interior limits**, and a.e. trace usage is explicitly licensed.
  3. Boundary-contact is globally enforceable via \(\kappa\)-admissible shrinking (`\ref{def:collar-admissible}`, `\ref{lem:collar-existence}`), but Bridge section should cross-reference this to preempt referee objections.
  4. UE’s boundary-trace usage is consistent with Bridge-1; adding an explicit pointer to `\ref{rem:boundary_modulus}` removes any pointwise/a.e. ambiguity.
  5. Unifying `G_{\rm out}` vs `G_{\mathrm{out}}` eliminates a trivial but real audit-risk: apparent “two different outer factors”.
* Paste-ready manuscript edits:
  (i) revised lemma/proposition statements: **None** (Bridge-1 statements are already correct); **Lemma `\ref{lem:upper-envelope}` statement receives wording/notation clarification only (Edit 2).**
  (ii) revised definitions/remarks: **Bridge section intro cross-reference (Edit 1); UE remark notation unification (Edit 3).**
  (iii) revised theorem/inequality lines: **None.**
* Dependencies on other branches:
  - Bridge-1 consumes (does not prove) the premise “\(W\) (equivalently \(E\)) is zero-free on \(B^\circ\)” at the invocation point.
* Referee risk notes (anticipated objections + how addressed):
  - **Objection:** “You assume boundary-contact; where do you ensure it?”  
    **Addressed:** explicit cross-reference to \(\kappa\)-admissible shrinking (`\ref{def:collar-admissible}`, `\ref{lem:collar-existence}`) added at Bridge entry point (Edit 1).
  - **Objection:** “You mix pointwise and a.e. boundary modulus.”  
    **Addressed:** `\ref{rem:boundary_modulus}` already resolves this; UE is pointed to it explicitly (Edit 2).
  - **Objection:** “Are `G_{\rm out}` and `G_{\mathrm{out}}` the same object?”  
    **Addressed:** notation standardized (Edit 2–3).
