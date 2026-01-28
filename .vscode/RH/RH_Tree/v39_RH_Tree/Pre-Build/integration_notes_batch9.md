# Integration Notes — Batch‑9 (conflict‑resolution + delta digest → v39 pre‑build)

**Date:** 2026-01-26  
**Baseline locked:** v38  
**Objective of Batch‑9:** de‑risk the “Missing Lever” by finding a *proof‑grade local redesign mechanism* that can plausibly deliver a **gate‑passing phase‑class UE** (or a domination link that makes one usable).

---

## 1) Executive synthesis (what Batch‑9 actually tells us)

### 1.1 The convergent signal
Batch‑9 converges on a single plausible analytic lever that does *not* violate the v38 NO‑GO constraints:

> **Use a cancellative “defect” log‑derivative difference**
> \[
> \mathcal Q_a(v):=\frac{E(v+a)}{E(v-a)},\qquad
> \mathcal L_a(v):=\frac{\mathcal Q_a'(v)}{\mathcal Q_a(v)}=
> \frac{E'}{E}(v+a)-\frac{E'}{E}(v-a),
> \]
> to turn the “local blow‑up” problem into a **horizontal‑resonance accounting problem**.

Why this matters: the local‑window singularities that killed earlier UE attempts are *pair‑cancelled* in `\mathcal L_a` near the aligned hinge, leaving only a **δ/a‑scale pair term** plus “resonance‑type” remainder terms.

### 1.2 The sharp new obstruction
Batch‑9 also isolates the *real* reason S5′ stalled:

- A **single quartet** does **not** force a defect endpoint on the aligned box (removable singularity / cancellation).
- But **two near‑resonant quartets** *can* make defect endpoints **δ‑inert** (O(1) as δ→0), defeating any η‑shrinking UE unless that resonance is controlled/excluded.

So the Missing Lever is now crisply:  
**Domination + Defect UE + Resonance control.**

### 1.3 What we will do in v39
We will **install the defect primitives as tooling** and **re‑box the Missing Lever** to make the remaining frontier explicit and fail‑closed:

- `\Phi^{\rm def}_B(a)` (defect phase endpoint) is introduced **as the candidate UE‑friendly quantity**.
- v39 will *not* claim RH closure; it will make it mechanically obvious what remains open.

---

## 2) Branch results (PASS/FAIL/CONDITIONAL) + conflict resolution

### RH‑ABSORB — **CONDITIONAL (good framing patch)**
- Correctly flags the central issue: the defect endpoint is **not automatically forceable** on the symmetric/aligned contour because of cancellation (removable singularity).
- Supplies a clean **Missing‑Lever box rewrite** and a conditional closure theorem skeleton keyed to gate exponents.
- **Integration decision:** accept ABSORB’s *box rewrite* and make forcing explicit as an OPEN dependency.

### RH‑BRIDGE — **PASS (tooling is proof‑grade)**
- Provides collar safety and difference‑kernel bounds for `\mathcal L_a` on buffered contours.
- Gives the structural identity: defect endpoint equals *difference of* phase increments of `E` on shifted contours.
- **Integration decision:** include as the analytic backbone for the defect UE proof.

### RH‑ENVELOPE — **CONDITIONAL (UE skeleton + new NO‑GO)**
- Proposes the correct phase endpoint:
  `\Phi_B^{\rm def}(a)=\max_{\rm sides}|\Im\int \mathcal L_a|`.
- Produces the key UE skeleton:
  `\Phi_B^{\rm def}(a) \lesssim \delta\log m + \delta a\,R_a(m)`.
- Supplies an explicit **δ‑inert resonance countermodel** (must be latched in‑text as NO‑GO).
- **Integration decision:** adopt the UE skeleton **and** install the resonance NO‑GO lemma.

### RH‑LOCAL — **CONDITIONAL (pair cancellation + scaling, but resonance remains open)**
- Gives the local factorization near the aligned hinge, proving:
  - `\mathcal Q_a` has a removable singularity at `v=i m`,
  - `\mathcal L_a` is holomorphic there,
  - the pure‑pair contribution is `O(\delta/a)` and vanishes under the standard `\delta_0\sim a/(\log m)^2` policy.
- **Integration decision:** install as the *official explanation* of why “forced‑quartet ⇒ forced‑defect endpoint” is false in general.

### RH‑FORCE — **PASS (but not directly usable for phase‑class UE)**
- Proves a forcing lower bound for a defect endpoint on a **defect‑pole box** centered at `2a+i m` via argument principle (pole winding ⇒ ≥π/2 on some side).
- **Conflict resolution:** this does **not** contradict LOCAL/ENVELOPE, because it forces a *different contour* (one enclosing a pole), while the UE‑friendly defect endpoint must live on an **analytic/no‑singularity contour**.
- **Integration decision:** keep this lemma as a **harness/diagnostic** (S6 cross‑check), not as the main S5^def closure route.

---

## 3) Canonical decisions locked for v39 pre‑build

1. **Defect endpoint is UE‑tooling, not a forced endpoint** (unless a domination/transfer lemma is proven).
2. **Horizontal resonance is now the named adversary**.
3. **v39 will carry two explicit NO‑GOs in‑text:**
   - one‑pole endpoint NO‑GO (v38),
   - near‑resonant δ‑inert NO‑GO (new).
4. **S6 explicit‑formula mapping remains mandatory**:
   displacement `a = 2\beta-1` corresponds to a potential `x^\beta` amplitude leak in the classical explicit formula.

---

## 4) What v39 must contain (high‑signal manuscript deltas)

- Definitions: `\mathcal Q_a`, `\mathcal L_a`, `\Phi_B^{\rm def}(a)`, resonance sum `R_a(m)` and/or `N_{\rm near}`.
- Lemma: local cancellation / removable singularity / `O(\delta/a)` pair term.
- Lemma(s): collar safety for shifted boxes; difference‑kernel bound.
- Lemma: resonance countermodel (δ‑inert) → **NO‑GO latch**.
- Boxed open statement: **Missing Lever = {Domination, Defect UE, Resonance control}**.

---

## 5) Readiness call

✅ **Proceed to v39 pre‑build artifacts** (this step)  
⛔ **Do not build v39 yet** until the pre‑build patch queue + protocol are locked (this output provides them).

