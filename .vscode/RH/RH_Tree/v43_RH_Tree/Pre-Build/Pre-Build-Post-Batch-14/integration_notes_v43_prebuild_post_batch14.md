# v43 pre-build (post Batch 14) — Canonical ingestion + closure map
**Date:** 2026-01-30  
**Input ingested:** Batch 14 (ABSORB/BRIDGE/ENVELOPE/FORCE/LOCAL) + legacy translation.  
**Locked baseline:** v42 post-build + v43 pre-build-post-batch-13 artifacts (GEO‑C4 endpoint + reduced UE interface).

---

## 0) Snapshot: where v43 stands right now

We are now in the **GEO‑C4 regime**:

- **Geometry witness:** hinge‑centered circle  
  \[
  C_{m,\delta}: v(\theta)= i m + \delta e^{i\theta},\quad \theta\in[0,2\pi].
  \]
- **Operator:** two‑sided shift difference (finite difference in tilt)  
  \[
  \mathcal L_t(v):=\frac{E'}{E}(v+t)-\frac{E'}{E}(v-t),\qquad
  \mathcal D_{a,h}(v):=\mathcal L_{a+h}(v)-\mathcal L_{a-h}(v).
  \]
- **Endpoint:** *single orthogonal harmonic channel* (k=2)  
  \[
  \psi(\theta):=\Im\big(\mathcal D_{a,h}(v(\theta))\,v'(\theta)\big),\qquad
  \Phi^\star:=\frac{\delta^2}{h}\,\|P_2\psi\|_{L^2([0,2\pi])}.
  \]
  (Here \(P_2\) projects onto \(\mathrm{span}\{\cos 2\theta,\sin 2\theta\}\).)

**Forceability:** In the even‑quartet toy model, an off‑axis quartet forces a nonzero k=2 harmonic *with constant forcing after the \(\delta^2/h\) normalization* (the “π/2‑carrier on a circle” effect).

**Single active frontier (still):** a **non‑pointwise UE input** controlling the size of \(\mathcal D_{a,h}\) on the hinge circle at the nominal scale.

---

## 1) Batch 14 ingestion — what is new / what is now latched

### 1.1 ABSORB (hygiene latches)

**ENT hygiene must be explicit and enforced everywhere:**

1) **Even entire completion** in the v‑frame:  
\[
E(v)\ \text{entire},\quad E(-v)=E(v),\quad E(\overline v)=\overline{E(v)}.
\]

2) **Shift‑admissibility (buffering)** must be stated as part of every lemma that uses \(E'/E\):  
\[
\min_\theta\min_{\pm,\pm}\mathrm{dist}\big(v(\theta)\pm(a\pm h),\ Z(E)\big)\ \ge\ \mathrm{buf}\,\delta
\]
for a fixed \(\mathrm{buf}\in(0,1)\).  
(*And we allow shrinking \(\delta\) to enforce admissibility, with \(h\) shrinking proportionally.*)

3) **Coupling policy:** always tie coupling to geometry scale  
\[
h=\kappa\delta,\qquad \kappa\in(0,1)\ \text{fixed}.
\]

These are now “non‑negotiable” latches.

---

### 1.2 BRIDGE (clean UE reduction constant)

A TeX‑ready reduction (now latched as the canonical UE reduction):

> \[
> \boxed{
> \|P_2\psi\|_{L^2}\ \le\ \|\psi\|_{L^2}\ \le\ \frac{1}{\sqrt\pi}\int_0^{2\pi}\big|\mathcal D_{a,h}(v(\theta))\big|\,d\theta
> }
> \]
> hence
> \[
> \boxed{
> \Phi^\star
> \le
> \frac{\delta^2}{\sqrt\pi\,h}\int_0^{2\pi}\big|\mathcal D_{a,h}(v(\theta))\big|\,d\theta.
> }
> \]

This pins down the **exact place** the UE input is used: a single \(H^1\)-type boundary norm of \(\mathcal D_{a,h}\).

---

### 1.3 ENVELOPE + FORCE (new NO‑GO latch about UE‑strength)

**Truth latch:** if an off‑axis quartet is present at \((a,m)\), then the k=2 forcing implies that the boundary \(L^1\) norm of \(\mathcal D_{a,h}\) on the hinge circle cannot be small. Concretely (under the usual coupling \(h=\kappa\delta\)):

\[
\Phi^\star\ge c_0\ \Rightarrow\ 
\int_0^{2\pi}\big|\mathcal D_{a,h}(v(\theta))\big|\,d\theta
\ \gtrsim\ \frac{h}{\delta^2}
\ =\ \frac{\kappa}{\delta}.
\]

So any UE input that “beats” \(\kappa/\delta\) at the nominal \(\delta\)-policy **is itself an RH‑closing statement** (not a routine estimate).

**This is not a problem — it is clarity.** It means the paper’s last remaining box is genuinely “the last lever”.

---

### 1.4 LOCAL + LEGACY (interpretation + resonance stance)

- The **k=2 harmonic** on the hinge circle is the contour analogue of the **π/2‑carrier / mod‑4 projector** intuition from the lattice calculus: you are not “maxing a side”, you are **extracting an orthogonal mode** (a channel).
- **Resonance / extra quartets:** because the endpoint is an \(L^2\) *energy* in a single Fourier band, additional quartets cannot cancel by sign; they can only (i) add energy in k=2 or (ii) live largely outside that band. This is qualitatively safer than side‑max endpoints.
- Practically: the UE step must still be formulated in a way that does not assume “one zero per height”, but allows clustering while keeping the UE input statement explicit.

---

## 2) Decision: keep R2 (and tighten it), do NOT reopen R1/R0

### R1 vs R2 recap (from post‑Batch‑13)

- **R1 (discarded):** v42 UE‑INPUT (pointwise + high derivatives) — over‑strong, effectively RH-strength with unnecessary derivative stack.
- **R2 (kept):** \(H^1\) boundary control of \(\mathcal D_{a,h}\) on the hinge circle — *minimal sufficient interface* for the GEO‑C4 endpoint.

### Batch 14 verdict

We **keep R2** as the single active statement, but we add two key clarifications:

1) **R2 is expected to be RH‑strength** (ENVELOPE/FORCE NO‑GO latch).  
   That is OK: it is the final closure brick.

2) We should explicitly allow a **barrier form** \(m\ge M\) (already in v43‑post‑13).  
   This matches the usual “finite verification below M” posture and avoids muddy quantifiers.

---

## 3) The single active statement (optimized + truth‑latched)

### 3.1 Nominal policy (locked)

\[
\delta=\eta\,\frac{a}{(\log(m+3))^2},\qquad h=\kappa\delta,
\]
with fixed \(\eta\in(0,1)\), \(\kappa\in(0,1)\).

### 3.2 Active UE closure statement (v43)

> **UE‑INPUT\(^{H^1}(\mathcal D;M)\) (single active box for v43).**  
> There exist absolute constants \(C>0\), \(C'\ge 0\), and \(M\ge 1\) such that for all \(m\ge M\), all \(a\in(0,1)\), for all shift‑admissible hinge circles \(C_{m,\delta}\) at the nominal policy,
> \[
> \boxed{
> \int_0^{2\pi}\big|\mathcal D_{a,h}(v(\theta))\big|\,d\theta
> \ \le\ 
> C\,h\,\frac{(\log(m+3))^{C'}}{a^2}.
> }
> \]
> Exponent‑budget target: \(C'\le 4\) (or \(C'=4\) with \(\eta\) chosen small enough).

### 3.3 Closure chain (dependency map)

**(D0) Definitions + hygiene:** ENT + shift‑admissible + \(h=\kappa\delta\).  
↓  
**(D1) FORCE:** if an off‑axis quartet exists at \((a,m)\), then  
\[
\Phi^\star(m,a,\delta,h)\ \ge\ c_0(\kappa)>0.
\]
↓  
**(D2) UE reduction (BRIDGE):**  
\[
\Phi^\star \le \frac{\delta^2}{\sqrt\pi\,h}\int_0^{2\pi}|\mathcal D_{a,h}(v(\theta))|\,d\theta.
\]
↓  
**(D3) UE‑INPUT\(^{H^1}(\mathcal D;M)\):** gives  
\[
\Phi^\star \le \frac{\delta^2}{\sqrt\pi\,h}\cdot
C h\frac{(\log(m+3))^{C'}}{a^2}
=
\frac{C}{\sqrt\pi}\,(\log(m+3))^{C'}\left(\frac{\delta}{a}\right)^2.
\]
With \(\delta/a=\eta/(\log(m+3))^2\),  
\[
\Phi^\star \le \frac{C}{\sqrt\pi}\,\eta^2\,(\log(m+3))^{C'-4}.
\]
Choose \(M\) (large) and/or \(\eta\) (small) so that RHS \(<c_0\), contradiction.  
↓  
**(D4) Conclusion:** no off‑axis quartet at any \(m\ge M\); combine with finite verification below \(M\) (if desired) to conclude RH.

---

## 4) New NO‑GO statements to freeze (to prevent self‑sabotage)

These are not “discouraging”; they are *frontier markers*.

1) **NO‑GO(δ⁻¹) upper bounds:** any UE input allowing a factor \(h/\delta\) (or worse) is too weak: it cannot drive \(\Phi^\star\to 0\) and is compatible with the forced toy model.

2) **NO‑GO (soft‑method expectation):** UE‑INPUT\(^{H^1}(\mathcal D;M)\) is genuinely RH‑strength (ENVELOPE/FORCE). Treat it as the *final analytic brick*, not a routine corollary.

3) **NO‑GO (missing admissibility):** any proof step using \(E'/E\) without shift‑admissibility/buffering is invalid.

---

## 5) Patch map: how to upgrade the manuscript in the v43 build

### Patch A — insert “ENT hygiene + admissibility” once, then reuse everywhere
Place early in GEO‑C4 section: define shift‑admissible hinge circle and explicitly bind \(h=\kappa\delta\).

### Patch B — replace UE‑reduction lemma with BRIDGE’s sharp constant
Insert the TeX‑ready lemma from BRIDGE (Section 1.2 above).

### Patch C — add the ENVELOPE/FORCE “RH‑strength” remark as a boxed NO‑GO lemma
Place immediately after the FORCE lemma, as:
- “FORCE ⇒ \(\|\mathcal D\|_{L^1}\gtrsim h/\delta^2\)”  
- therefore UE‑INPUT\(^{H^1}(\mathcal D)\) is exactly an RH‑closing statement.

This prevents future confusion (“why is this so hard?”).

### Patch D — rewrite the active UE box in v43 form
Swap v42’s UE‑INPUT with UE‑INPUT\(^{H^1}(\mathcal D;M)\), and explicitly list exponent budget.

---

## 6) What we need from Batch 15+ (if required)

If UE‑INPUT\(^{H^1}(\mathcal D;M)\) is not closed in‑house, the next prompt batch must target only:

- Bounding \(\int_0^{2\pi}|\mathcal D_{a,h}(v(\theta))|\,d\theta\) using:
  - Hadamard/log‑derivative decompositions,
  - “far zeros” contribution control,
  - and any available unconditional local zero density bounds on shifted circles.

No other frontiers should be opened.

---

**End state:** After Batch 14, the story is tighter: *everything is locked except a single, explicit boundary norm inequality that is known to be RH‑strength and is now stated in the minimal interface compatible with GEO‑C4.*
