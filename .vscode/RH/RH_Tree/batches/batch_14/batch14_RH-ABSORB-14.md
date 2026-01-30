# Batch 14 — RH-ABSORB-14  
## Program Hygiene Package for the UE-INPUTᴴ¹(D) interface (hinge-circle + harmonic endpoint)

**Scope of this package.** This is a *hygiene* deliverable: quantifiers, δ/h policy, and NO‑GO scope control for the **new** UE-INPUTᴴ¹(D) interface. It is not a proof of UE-INPUT itself.

---

## 1) Parameter map + nominal scale (what is fixed vs what varies)

### 1.1 Fixed parameters (global, chosen once)
- **κ** in \((0,1/10)\): buffering / hinge coupling constant.
- **η** in \((0,\eta_0]\): nominal shrink factor (height-independent).

### 1.2 Varying parameters (instance-by-instance)
- \(m \ge m_0\) (height parameter in the \(v\)-frame).
- \(a \in (0,1]\) (off-axis displacement; \(a=2\beta-1\) in \(v\)-frame conventions).

### 1.3 Nominal box/circle scale and coupling
Define the **nominal radius**
\[
\delta_0(m,a):=\frac{\eta a}{(\log(m+3))^2},
\]
and for any admissible choice \(0<\delta\le \delta_0(m,a)\) define the coupled step
\[
h:=\kappa\delta.
\]

**Hygiene rule (critical):** the program must never silently swap between \(\delta\) and \(\delta_0\). Any lemma that depends on \((\delta,h)\) must state which one is being used.

---

## 2) Hinge-circle geometry + admissibility (minimum hypotheses)

### 2.1 Hinge circle and shifted evaluation circles
For \(0<\delta\le \delta_0\), define the hinge circle
\[
v(\theta):=im+\delta e^{i\theta},\qquad \theta\in[0,2\pi].
\]

Recall the two-sided defect operators (notation consistent with the corrected expansion)
\[
\mathcal L_t(v)=\frac{E'}{E}(v+t)-\frac{E'}{E}(v-t),\qquad 
\mathcal D_{a,h}(v)=\mathcal L_{a+h}(v)-\mathcal L_{a-h}(v),
\]
so explicitly
\[
\mathcal D_{a,h}(v)
=\frac{E'}{E}(v+a+h)-\frac{E'}{E}(v-a-h)
-\frac{E'}{E}(v+a-h)+\frac{E'}{E}(v-a+h).
\]

Thus any boundary integral or \(L^1\) control of \(\mathcal D_{a,h}(v(\theta))\) requires \(E\neq 0\) on each of the four shifted hinge circles
\[
\theta\mapsto v(\theta)\pm(a\pm h).
\]

### 2.2 κ-admissibility (hinge-circle version)
A **minimal admissibility** condition sufficient to define all boundary traces used in UE-INPUTᴴ¹(D) is:

> **(κ-admᴴ¹)** For the chosen \((m,a,\delta)\) with \(h=\kappa\delta\), the function \(E\) is holomorphic on a neighborhood of the union  
> \(\{v(\theta)\pm(a\pm h):\theta\in[0,2\pi]\}\), and  
> \[
> E\bigl(v(\theta)\pm(a\pm h)\bigr)\neq 0\quad\text{for all }\theta\in[0,2\pi].
> \]
> (Optional stronger buffering variant, if the manuscript needs pointwise Cauchy bounds: assume a uniform distance-to-zeros lower bound \(\operatorname{dist}(\cdot,Z(E))\ge \kappa\delta\) on these curves.)

**Non-negotiable discipline:** any use of \(\frac{E'}{E}\) or \(\mathcal D_{a,h}\) on the boundary must explicitly cite (κ-admᴴ¹).

---

## 3) Monotone-shrink sanity (what is monotone, what is not)

This section exists to prevent a silent but fatal inference:
> “We can always shrink \(\delta\) for admissibility, and all bounds only improve.”

That statement is **not** valid for the new \(L^1\) hinge-circle UE input.

### 3.1 What *is* monotone under shrinking \(\delta\)
1. **Admissibility can be regained by shrinking** (topological fact):  
   because zeros are isolated, the set of “bad radii” for which any of the shifted circles hits a zero is discrete. If \(\delta_0\) is not admissible, one can choose a slightly smaller \(\delta\le \delta_0\) that is admissible.

2. **Coupling consistency is preserved**: if we shrink \(\delta\) we automatically shrink \(h=\kappa\delta\). All statements that require the nominal coupling remain within the same regime.

3. **Forcing lower bounds should be δ-stable (when proven in that form)**:  
   the program’s forcing lemmas are intended to produce a lower bound depending only on \(\kappa\) (and topology/argument principle), not one that deteriorates as \(\delta\downarrow 0\).  
   **Hygiene requirement:** forcing results must be stated as “for all \(0<\delta\le \delta_0\)” if they are used after a shrink step.

### 3.2 What is *not* monotone under shrinking \(\delta\)
The **analytic quantity**
\[
\theta\mapsto \left|\mathcal D_{a,h}(v(\theta))\right|
\quad\text{and hence}\quad
\int_0^{2\pi}\left|\mathcal D_{a,h}(v(\theta))\right|\,d\theta
\]
is **not** guaranteed to decrease as \(\delta\) decreases.

- Even in toy models, log-derivative traces can grow like \(1/\delta\) near a nearby zero, and discrete shift-differences typically do **not** remove that scaling without additional structure.
- Because the target UE-INPUTᴴ¹(D) inequality has an explicit prefactor \(h=\kappa\delta\) on the RHS, shrinking \(\delta\) actually makes the **RHS smaller**, and thus can make the inequality **harder** to satisfy.

> **Referee rule:** no argument may use “shrink \(\delta\)” to *strengthen* UE-INPUTᴴ¹(D). Shrinking \(\delta\) is allowed only to restore admissibility, and UE-INPUTᴴ¹(D) must be invoked at the *actual shrunk* \((\delta,h)\), not inferred from the nominal one.

---

## 4) Correct δ-policy contract (TeX-ready lemma)

### 4.1 Contract lemma (prevents circularity / false monotonicity)

```tex
\begin{lemma}[δ-policy contract for UE-INPUT$^{H^1}(\mathcal D)$]
\label{lem:delta-policy-contract-hinge}
Fix \(\kappa\in(0,1/10)\) and \(\eta\in(0,\eta_0]\). 
For each pair \((m,a)\) with \(m\ge m_0\) and \(a\in(0,1]\), define
\[
\delta_0(m,a):=\frac{\eta a}{(\log(m+3))^2}.
\]
Choose any radius \(0<\delta\le\delta_0(m,a)\) such that the hinge-circle admissibility condition
\emph{(κ-adm$^{H^1}$)} holds for \((m,a,\delta)\), and set \(h=\kappa\delta\).

Then every subsequent step in the UE-INPUT$^{H^1}(\mathcal D)$ pipeline (definition of the endpoint,
forcing lower bounds, and any envelope/upper bounds) is applied at this same pair \((\delta,h)\).
In particular, the program does \emph{not} use any monotonicity assertion of the form
“if the UE-INPUT bound holds at \(\delta_0\) then it holds for all \(\delta\le\delta_0\)”.
If the proof later replaces \(\delta\) by some \(\delta'\le\delta\), it must re-verify admissibility
at \(\delta'\) and re-invoke the UE-INPUT bound at \((\delta',h'=\kappa\delta')\).
\end{lemma}
```

### 4.2 Optional remark (if the manuscript wants a “maximal δ” convention)
If desired for streamlining, add:

- “When \(\delta_0\) is not admissible, we take \(\delta\) to be any admissible radius in \([\frac12\delta_0,\delta_0]\).”
- This requires a separate **existence-of-admissible-radius lemma** (likely delegated to RH‑LOCAL), because buffering excludes a neighborhood of each local zero radius.

---

## 5) NO-GO guardrails update (what still applies, and what no longer blocks)

The following v40/v41 NO‑GO results remain valid as *endpoint-class* exclusions and should stay latched, but they must not be misapplied to the new hinge-circle harmonic endpoint:

1. **Pointwise/sup UE scaling NO‑GO** remains valid: no \(p>1\) gain is possible in the sup/pointwise class.  
   **Status:** still true, but *irrelevant* if we are not using sup/pointwise endpoints.

2. **Absolute \(L^r(\partial B)\) endpoint NO‑GO** remains valid: \(p(r)=\theta(r)\) gives δ‑inert local terms.  
   **Status:** still true, but does not automatically block a harmonic/projection endpoint.

3. **Projection endpoints NO‑GO under old forcing** remains valid: any endpoint that annihilates the forced quantity is invalid unless a transfer/forcing lemma is supplied.  
   **Status:** still true, but the hinge-circle harmonic endpoint is explicitly designed to be **forceable**, so this NO‑GO is not applicable *if* the forcing lemma targets the harmonic endpoint directly.

4. **Aligned-box Δa forcing NO‑GO** remains valid (toy model shows forcing collapses at nominal coupling on aligned boxes).  
   **Status:** still true; it only forbids *aligned-box* forcing claims. It does **not** forbid hinge-circle forcing.

**Action item for v43/v44 builds:** every NO‑GO statement must be labeled “NO‑GO for endpoint class X / geometry Y” to prevent accidental global overreach that would falsely rule out GEO‑C4.

---

## 6) Paste-ready insertion blocks (minimal edits)

### 6.1 Insert near the UE-INPUT$^{H^1}(\mathcal D)$ statement

```tex
\begin{remark}[Shrink discipline for UE-INPUT$^{H^1}(\mathcal D)$]
Shrinking \(\delta\) is permitted solely to restore admissibility on the hinge-circle family
\(\theta\mapsto v(\theta)\pm(a\pm h)\) with \(h=\kappa\delta\).
One must not assume any monotonicity of \(\int|\mathcal D_{a,h}(v(\theta))|\,d\theta\) in \(\delta\).
Accordingly, every instance of UE-INPUT$^{H^1}(\mathcal D)$ is invoked at the \emph{actual} chosen
\((\delta,h)\), not inferred from the nominal \(\delta_0(m,a)\).
\end{remark}
```

### 6.2 Insert Lemma \ref{lem:delta-policy-contract-hinge} (from §4.1)

### 6.3 Update NO‑GO headings (Appendix / guardrail section)

```tex
\begin{remark}[Scope of NO--GO statements]
Each NO--GO result in this manuscript excludes a specific \emph{endpoint class} and/or \emph{geometry}.
For example, the pointwise/sup UE scaling obstruction excludes the sup endpoint class, and the
aligned-box \(\Delta a\) forcing obstruction excludes aligned-box forcing at nominal coupling.
These NO--GO statements do not automatically apply to hinge-circle harmonic endpoints unless their
hypotheses match the new endpoint/forcing architecture.
\end{remark}
```

---

## Mandatory Patch Packet

* Callsign: **RH-ABSORB-14**
* Result classification: **PASS (hygiene package complete; no analytic claims added)**
* Target gaps closed (by ID): **G-5 (κ/δ policy hygiene)**, **δ-quantifier discipline for UE-INPUTᴴ¹(D)** (program hygiene; new sub-gap if tracked)
* Target gaps still open (by ID): **UE-INPUTᴴ¹(D) proof itself (ENVELOPE)**; **admissible-radius existence in a thick band (LOCAL, if required)**; **forcing lemma for the harmonic endpoint (FORCE)**
* Key conclusions (≤5 bullets):
  1. Shrinking \(\delta\) restores admissibility but does **not** automatically improve the \(L^1\) UE input.
  2. The program must invoke UE-INPUTᴴ¹(D) at the *actual* \((\delta,h)\) used, not infer it from \(\delta_0\).
  3. Forcing lemmas must be stated δ-uniformly if used after a shrink step.
  4. NO‑GO results remain valid only as endpoint/geometry exclusions; they do not globally block GEO‑C4.
  5. A δ-policy contract lemma prevents silent circularity or false monotonicity.
* Paste-ready manuscript edits: **see §6 TeX blocks**
* Dependencies on other branches: **RH-ENVELOPE (UE-INPUTᴴ¹(D) proof), RH-LOCAL (thick admissible-radius lemma if needed), RH-FORCE (harmonic forcing lemma)**
* Referee risk notes (anticipated objections + how addressed):
  - *Objection:* “You shrank \(\delta\) so your UE bound got stronger.”  
    *Answer:* explicitly forbidden; contract lemma forces UE invocation at the shrunk scale.
  - *Objection:* “Your NO‑GO statements contradict the new endpoint.”  
    *Answer:* scope remark forces endpoint/geometry labeling; GEO‑C4 not blocked unless hypotheses match.
