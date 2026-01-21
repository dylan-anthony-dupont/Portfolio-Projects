## RH‑BRIDGE Batch 1 — Bridge‑1 hypothesis discharge (G‑6)

### 1) What Bridge‑1 currently is (and why G‑6 exists)

Across v29–v32, Bridge‑1 is stated in the **maximum‑modulus** form:

> If \(W\) is analytic and zero‑free on \(B\), continuous on \(B\), and \(|W|=1\) on \(\partial B\), then \(W\) is constant.  
> Proof: apply maximum modulus to \(W\) and to \(1/W\).  
(Explicitly in v30/v31/v32 as Proposition 9.1.)【3:9†manuscript_v30.pdf†L34-L59】【2:6†manuscript_v32.pdf†L23-L39】

The **issue (G‑6 / E‑9)** is not that the proposition is false; it’s that the manuscript does not cleanly discharge the hypotheses in the *way it actually constructs \(W\)*:

- In the outer‑factor section, \(G_{\rm out}\) is constructed from a Dirichlet solution \(U\) and a harmonic conjugate \(V\), and \(W:=E/G_{\rm out}\) is declared analytic with \(|W|=1\) on \(\partial B\).【3:9†manuscript_v30.pdf†L34-L50】  
  But continuity of \(W\) on \(\overline{B}\) (needed for the max‑modulus proof as written) is not proved there, and the phrase “continuous on \(B\)” is ambiguous (open vs closed box).

- Later, v32’s envelope machinery treats boundary values **a.e. / \(L^2(\partial B)\)** (best constant phase in \(L^2\)), which is logically consistent with “boundary traces” but does not match a pointwise continuity‑to‑boundary assumption without additional lemmas.【2:13†manuscript_v32.pdf†L18-L37】

- Earlier lineage (e.g. v13, v24, v26) *already had* a more robust “log‑harmonic / boundary‑trace” style Bridge‑1 that does not rely on pointwise continuity of \(W\) as an analytic function on \(\overline{B}\).【3:4†manuscript_v13.pdf†L34-L57】【2:11†manuscript_v24.pdf†L37-L50】【2:12†manuscript_v26.pdf†L45-L49】

So G‑6 is: **Bridge‑1’s hypotheses are not aligned with what the manuscript actually guarantees about \(G_{\rm out}\) and \(W\)**, especially the continuity/trace meaning and the “\(|W|=1\) on \(\partial B\)” sense.

---

## 2) Proof‑grade Bridge‑1 package with minimum hypotheses

I recommend **replacing** the max‑modulus Bridge‑1 (current v29–v32 Proposition 9.1) with a strictly cleaner lemma that uses **Dirichlet uniqueness** + **zero‑freeness**. This closes G‑6 with fewer boundary regularity assumptions and matches both the older v13/v24/v26 logic and the v32 “boundary trace / \(L^2\)” environment.

### 2.1 Outer factor construction lemma (what \(G_{\rm out}\) actually needs)

**Lemma (Outer factor on a box; boundary modulus is pointwise in modulus).**  
Let \(B=B(\alpha,m,\delta)\) be the closed rectangle and \(B^\circ\) its interior. Assume:

1. \(E\) is holomorphic on a neighborhood of \(\overline{B}\) (true in your program since \(E\) is built from \(\Lambda_2\) and is holomorphic on the height‑\(m\) boxes under consideration), and  
2. (**Boundary‑contact**) \(E(v)\neq 0\) for all \(v\in\partial B\).

Then \(\log|E|\in C(\partial B)\). Let \(U\in C(\overline{B})\cap {\rm Harm}(B^\circ)\) be the unique Dirichlet solution with boundary data
\[
U|_{\partial B}=\log|E|.
\]
Because \(B^\circ\) is simply connected, there exists a harmonic conjugate \(V\) on \(B^\circ\) (unique up to an additive real constant). Define
\[
G_{\rm out}(v):=\exp(U(v)+iV(v)),\qquad v\in B^\circ.
\]
Then \(G_{\rm out}\) is holomorphic and zero‑free on \(B^\circ\), and its modulus satisfies
\[
|G_{\rm out}(v)|=e^{U(v)}\quad (v\in B^\circ),\qquad \lim_{z\to \xi,\,z\in B^\circ}|G_{\rm out}(z)|=|E(\xi)|\quad(\xi\in\partial B).
\]
Equivalently, the boundary modulus identity \(|G_{\rm out}|=|E|\) holds **pointwise in modulus** on \(\partial B\) (as an interior limit), and hence \(|W|=1\) on \(\partial B\) in the same sense for \(W:=E/G_{\rm out}\).

**Where this is already “declared” in the manuscript (but not formalized):**  
The construction is stated in v30/v31/v32 Section “Outer factorization and the inner quotient (Bridge 1)”.【3:9†manuscript_v30.pdf†L34-L50】【2:6†manuscript_v32.pdf†L23-L32】  
v28 goes further and asserts continuity and “pointwise on \(\partial B\)” directly, but without a supporting lemma.【3:1†manuscript_v28.pdf†L53-L73】

**Key audit point:** this lemma does **not** need \(V\) to extend continuously to \(\partial B\). It only uses that \(U\) extends continuously, hence the **modulus** boundary matching is pointwise (as a limit).

---

### 2.2 Final Bridge‑1 statement (minimum hypotheses; proof‑grade)

**Proposition (Bridge‑1: zero‑free inner collapse; proof‑grade).**  
Work under the outer factor setup above: \(E\) holomorphic near \(\overline{B}\), \(E\neq 0\) on \(\partial B\), \(U\) the Dirichlet solution with \(U|_{\partial B}=\log|E|\), and \(G_{\rm out}:=\exp(U+iV)\) with \(V\) a harmonic conjugate on \(B^\circ\). Define
\[
W(v):=\frac{E(v)}{G_{\rm out}(v)}\qquad (v\in B^\circ).
\]

Assume additionally:

3. (**Zero‑free hypothesis**) \(W\) is zero‑free on \(B^\circ\).  
   (Equivalently, \(E\) is zero‑free on \(B^\circ\), since \(G_{\rm out}\) is zero‑free.)

**Conclusion:** \(W\) is constant on \(B^\circ\); in fact \(W\equiv e^{i\theta_B}\) for some \(\theta_B\in\mathbb{R}\).

**Meaning of the boundary modulus:** Under the construction, \(|W|=1\) on \(\partial B\) holds as a **pointwise modulus statement** (interior limits), and therefore also holds **a.e.** on \(\partial B\) for any boundary‑integral usage (e.g., \(L^2(\partial B)\) phases in v32).【2:13†manuscript_v32.pdf†L18-L37】

#### Proof (referee‑grade; no max‑modulus on \(1/W\) required)

- Because \(W\) is zero‑free on \(B^\circ\) and \(G_{\rm out}\) is zero‑free on \(B^\circ\), we have \(E\) zero‑free on \(B^\circ\).  
  Since \(B^\circ\) is simply connected, there exists a holomorphic logarithm \(\Log E\) on \(B^\circ\), and therefore \(\log|E|=\Re(\Log E)\) is harmonic on \(B^\circ\).

- By construction, \(U\) is harmonic on \(B^\circ\), continuous on \(\overline{B}\), and satisfies \(U=\log|E|\) on \(\partial B\).  
  The function \(h:=U-\log|E|\) is harmonic on \(B^\circ\), extends continuously to \(\partial B\), and satisfies \(h|_{\partial B}=0\).  
  By uniqueness of the Dirichlet problem on a rectangle, \(h\equiv 0\) on \(B^\circ\), i.e. \(U\equiv\log|E|\) on \(B^\circ\).

- Hence for all \(v\in B^\circ\),
  \[
  |W(v)|=\frac{|E(v)|}{|G_{\rm out}(v)|}
        =\frac{|E(v)|}{e^{U(v)}}
        =\frac{|E(v)|}{e^{\log|E(v)|}}=1.
  \]
  An analytic function with constant modulus on a connected open set is constant (open mapping theorem). Therefore \(W\equiv e^{i\theta_B}\) on \(B^\circ\).

This proposition is the clean formal version of the earlier “log‑harmonic + open mapping” Bridge‑1 that appears explicitly in v13 (and similar in v24/v26), but rewritten to match the v30+ \(G_{\rm out}\)/\(W\) definitions.【3:4†manuscript_v13.pdf†L34-L57】

---

### 2.3 Optional: keep the max‑modulus version as a corollary (if you want)

If you prefer to keep the existing Proposition 9.1 proof style (max modulus on \(W\) and \(1/W\)), you must strengthen and clarify the hypotheses:

**Corollary (Max‑modulus Bridge‑1; continuity form).**  
If \(W\) extends continuously to \(\overline{B}\), is zero‑free on \(\overline{B}\), and satisfies \(|W|=1\) pointwise on \(\partial B\), then \(W\) is constant.

This matches the current v29/v30/v31/v32 proof verbatim but fixes the closure ambiguity (“continuous on \(B\)” should be “continuous on \(\overline{B}\)”, and zero‑freeness should include boundary if you want \(1/W\) continuous).【3:5†manuscript_v29.pdf†L51-L57】【3:9†manuscript_v30.pdf†L52-L59】

**However:** the outer‑factor construction in v30–v32 does not currently prove \(W\in C(\overline{B})\), and v32 elsewhere defaults to a.e./\(L^2\) traces, so I recommend the harmonic‑uniqueness Bridge‑1 as the mainline fix.

---

## 3) Outer factor construction requirements (minimum, explicit)

To make Bridge‑1 referee‑proof, the manuscript should state (or cite) the following minimal facts as lemmas/remarks:

1. **Boundary‑contact ⇒ \(\log|E|\in C(\partial B)\)**  
   If \(E\) is continuous on \(\partial B\) and has no zeros there, \(\log|E|\) is continuous and bounded on \(\partial B\). (This is immediate.)

2. **Dirichlet solvability/uniqueness on \(B\)**  
   Because \(B\) is a rectangle (bounded Lipschitz/Jordan domain), the Dirichlet problem with continuous boundary data has a unique solution \(U\in C(\overline{B})\cap{\rm Harm}(B^\circ)\).  
   This is the sole PDE input Bridge‑1 needs.

3. **Harmonic conjugate exists on \(B^\circ\)**  
   Since \(B^\circ\) is simply connected, \(U\) has a harmonic conjugate \(V\) and \(U+iV\) is holomorphic. \(V\) is unique up to an additive constant (hence \(G_{\rm out}\) unique up to unimodular factor).

4. **Zero‑free condition needed for “collapse”**  
   Bridge‑1 requires \(W\) zero‑free on \(B^\circ\) (equivalently \(E\) zero‑free on \(B^\circ\)).  
   This is exactly the “certified Rouché” purpose in earlier versions (v13/v24/v26) and the “Rouché ratio” path in v28.【3:4†manuscript_v13.pdf†L39-L57】【3:1†manuscript_v28.pdf†L78-L90】

---

## 4) Patch‑ready manuscript edits

Below are paste‑ready edits that you can drop into v33 (or retro‑patch v32) to close G‑6 cleanly.

### (i) Insert immediately after the definition of \(B(\alpha,m,\delta)\) or at the start of “Outer factorization and the inner quotient (Bridge 1)”

```tex
\begin{lemma}[Dirichlet outer factor on a box]\label{lem:outer_dirichlet_box}
Let $B=B(\alpha,m,\delta)$ be the closed rectangle and $B^\circ$ its interior.
Assume $E$ is holomorphic on a neighborhood of $\overline{B}$ and $E\neq 0$ on $\partial B$
(\emph{boundary-contact convention}). Then $\log|E|\in C(\partial B)$.
Let $U\in C(\overline{B})\cap \mathrm{Harm}(B^\circ)$ be the unique solution of the Dirichlet
problem with boundary data $U|_{\partial B}=\log|E|$.

Since $B^\circ$ is simply connected, there exists a harmonic conjugate $V$ on $B^\circ$
(unique up to an additive constant) such that $U+iV$ is holomorphic on $B^\circ$.
Define
\[
G_{\rm out}(v):=\exp\!\big(U(v)+iV(v)\big),\qquad v\in B^\circ.
\]
Then $G_{\rm out}$ is holomorphic and zero-free on $B^\circ$, and $|G_{\rm out}(v)|=e^{U(v)}$ for all
$v\in B^\circ$. In particular, as $z\to \xi\in\partial B$ from within $B^\circ$,
\[
|G_{\rm out}(z)|\to e^{U(\xi)} = e^{\log|E(\xi)|}=|E(\xi)|.
\]
\end{lemma}
```

### (ii) Replace Proposition 9.1 (v29–v32) with the proof‑grade Bridge‑1

This replaces the current maximum‑modulus continuity‑sensitive statement【3:9†manuscript_v30.pdf†L52-L59】【2:6†manuscript_v32.pdf†L33-L39】.

```tex
\begin{proposition}[Bridge 1: zero-free inner collapse]\label{prop:bridge1}
Assume the setup of Lemma~\ref{lem:outer_dirichlet_box}, and define on $B^\circ$
\[
W(v):=\frac{E(v)}{G_{\rm out}(v)}.
\]
Then $W$ is holomorphic on $B^\circ$ and satisfies $|W|=1$ on $\partial B$ in the sense of interior
limits in modulus. If moreover $W$ is zero-free on $B^\circ$ (equivalently, $E$ is zero-free on $B^\circ$),
then $W$ is constant on $B^\circ$; in fact $W\equiv e^{i\theta_B}$ for some $\theta_B\in\mathbb{R}$.
\end{proposition}

\begin{proof}
Since $W$ is zero-free on $B^\circ$ and $G_{\rm out}$ is zero-free on $B^\circ$,
the function $E$ is zero-free on $B^\circ$. Because $B^\circ$ is simply connected, $E$ admits a holomorphic
logarithm on $B^\circ$, hence $\log|E|$ is harmonic on $B^\circ$ and continuous on $\overline{B}$.

By construction, $U$ is harmonic on $B^\circ$, continuous on $\overline{B}$, and equals $\log|E|$ on $\partial B$.
Therefore $U-\log|E|$ is harmonic on $B^\circ$ with zero boundary values; by uniqueness of the Dirichlet problem,
$U\equiv \log|E|$ on $B^\circ$. It follows that for all $v\in B^\circ$,
\[
|W(v)|=\frac{|E(v)|}{|G_{\rm out}(v)|}=\frac{|E(v)|}{e^{U(v)}}=\frac{|E(v)|}{e^{\log|E(v)|}}=1.
\]
An analytic function of constant modulus on a connected open set is constant (open mapping theorem),
so $W\equiv e^{i\theta_B}$ on $B^\circ$.
\end{proof}
```

### (iii) Patch the “a.e.” language to be unambiguous (optional but recommended for coherence with v32 Lemma 10.2)

v32 currently says boundary‑contact “hence \(W\) has unimodular boundary values a.e.”【2:13†manuscript_v32.pdf†L24-L25】. Replace/add:

```tex
\begin{remark}[Boundary modulus convention]\label{rem:boundary_modulus}
Under boundary-contact ($E\neq 0$ on $\partial B$), the Dirichlet solution $U$ is continuous on $\overline{B}$
with $U|_{\partial B}=\log|E|$. Hence the modulus identity $|G_{\rm out}|=|E| holds pointwise on $\partial B$
(as interior limits in modulus), and therefore $|W|=1$ holds pointwise in modulus on $\partial B$.
In any boundary-integral estimate, this may be used in the a.e.\ sense without change.
\end{remark}
```

### (iv) If you keep any max‑modulus form anywhere, fix “continuous on \(B\)” ⇒ “continuous on \(\overline{B}\)”

This addresses the ambiguity in current v29–v32 statements.【3:5†manuscript_v29.pdf†L51-L57】【3:9†manuscript_v30.pdf†L52-L59】

---

## 5) What remains “hard gate” vs now closed

- With the replacement Bridge‑1 above, the only substantive “gate” is: **you must actually establish (or certify) that \(W\) is zero‑free on \(B^\circ\)** in the contexts where you invoke Bridge‑1. This is consistent with the program’s own framing: Bridge‑1 is the “collapse once zero‑free is known,” whether the zero‑free fact comes from Rouché, a verified band, or another step.

- This patch does **not** assume away boundary regularity; it makes the minimal regularity explicit and pins it to the **Dirichlet problem on a rectangle with continuous boundary data**.

---

# MANDATORY FINAL SECTION — PATCH PACKET FORMAT

- **Prompt Batch Number:** 1  
- **Callsign:** RH-BRIDGE  
- **Result classification:** **CONDITIONAL**  
- **Target gaps closed (by ID):** **G-6** (Bridge‑1 hypotheses) — closed **provided** the manuscript adopts the patched Bridge‑1 statement + adds the Dirichlet outer‑factor lemma.  
- **Target gaps still open (by ID):**  
  - **(Outside my scope, but directly adjacent as a dependency):** “Zero‑free in \(B\)” sourcing (e.g., Rouché ratio certification, verified band propagation, etc.). Bridge‑1 consumes it; it does not produce it.

- **Key conclusions (≤5 bullets):**
  1. The current v29–v32 Bridge‑1 (max‑modulus) is mathematically correct but hypothesis‑fragile due to continuity/trace ambiguity.  
  2. A proof‑grade Bridge‑1 with **strictly weaker boundary regularity assumptions** exists: Dirichlet uniqueness + zero‑free ⇒ \(W\) unimodular in \(B\) ⇒ constant.  
  3. This patch aligns v30+ with the earlier v13/v24/v26 “log‑harmonic collapse” approach while remaining compatible with v32’s \(L^2(\partial B)\) boundary‑trace usage.  
  4. Pointwise vs a.e. is resolved cleanly: modulus identities are pointwise (via continuous Dirichlet data) and therefore also valid a.e. for integrals.  
  5. The only essential Bridge‑1 “gate” is the **zero‑free** hypothesis for \(W\) (equivalently \(E\)) on the box interior.

- **Paste-ready manuscript edits:**  
  - **(i) lemma statements:** Lemma `outer_dirichlet_box` as given above.  
  - **(ii) definitions/remarks:** Remark `boundary_modulus` as given above; clarify \(B^\circ,\overline{B},\partial B\).  
  - **(iii) inequality lines:** None required for Bridge‑1 itself.

- **Dependencies on other branches:**  
  - Requires whichever mechanism supplies “\(W\) is zero‑free on \(B^\circ\)” in the intended invocation points (e.g., certified Rouché, verified band, or other zero‑exclusion step). Bridge‑1 is downstream of that.

- **Referee risk notes:**  
  - **Primary risk if unpatched:** the manuscript mixes “pointwise on \(\partial B\)” and “a.e. boundary trace” regimes while using a continuity‑dependent max‑modulus argument, leaving Bridge‑1 vulnerable (exactly G‑6 / E‑9).  
  - **Residual risk after patch:** ensure Dirichlet uniqueness on the rectangle is either cited explicitly or briefly justified; otherwise a referee may object that \(U\) is assumed rather than constructed.  
  - The patched proof is intentionally designed to avoid any need for continuity of the harmonic conjugate \(V\) to the boundary, which is where polygon/corner pathologies typically enter.
