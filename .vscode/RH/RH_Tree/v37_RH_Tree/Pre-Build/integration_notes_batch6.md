# Integration Notes — Batch 6 (v36 → v37 pre-build)

Date: 2026-01-25  
Baseline: **v36 locked**  
Objective: ingest Batch‑6 patch packets into a **v37 architecture build** that (i) introduces the S5′ *phase/winding endpoint* toolkit, (ii) preserves v36 truth‑latching (NO‑GO guardrails), and (iii) promotes the remaining frontier to one explicit “Missing Lever” with no drift.

---

## 1) Executive summary (what changed)

Batch‑6 delivered the *correct* next move for the program:  
**replace pointwise UE dreams with a forceable phase/winding endpoint family**, while also proving that **raw Δarg endpoints cannot close** under constant‑limited forcing unless a new analytic lever is invented.

This is progress because it narrows the frontier:  
we now know *exactly* what must be invented (δ‑gain + reduced local singularity / cancellation) and what is dead.

---

## 2) Branch digest (Patch Packet highlights)

### RH‑FORCE (CONDITIONAL)
**What it delivered**
- New endpoint candidate: \(\widetilde D_B(W)\) = max sidewise phase increment of the inner quotient \(W\) on a buffered contour \(\partial B_{\kappa/2}\).
- Proof‑grade forcing lemma: if \(W\) has ≥1 zero inside \(B_{\kappa/2}\), then \(\widetilde D_B(W)\ge \pi/2\) via argument principle.
- Explicit “forceability gate” reminder: adopting \(\widetilde D_B\) requires either tail rewrite (forced object replacement) or a transfer inequality to the existing forced dial deviation \(D_B(W)\).

**Integration decision for v37**
- Include definition + forcing lemma + gate remark.
- Correct notation: phase increment must be \(\Im\int (W'/W)\,dv\) (parentheses).

---

### RH‑BRIDGE (PASS)
**What it delivered**
- Phase increment calculus infrastructure:
  - \(\Delta_\Gamma \arg f = \Im\int_\Gamma (f'/f)\,dv\) under boundary‑collar nonvanishing.
  - Vertical specialization: on \(I_+\) it becomes an integral of \(\Re(f'/f)\,dy\).
- Additive split under \(E=F\cdot Z_{\rm loc}\).
- Local term bound in the phase class: per‑zero contribution \(\le \pi\) ⇒ local penalty is δ‑inert with θ=0 (contrast pointwise collar θ=1).

**Integration decision for v37**
- Drop these as “Phase Toolkit” lemmas early in the S5 section.

---

### RH‑ENVELOPE (CONDITIONAL)
**What it delivered**
- Shifted near‑vertical segment \(I_{+,\lambda}\) + phase increment definition (orientation correct).
- Phase split lemma on \(I_{+,\lambda}\) + residual phase budget:
  \(|\Delta\arg F|\le 2\delta(C_1\log m+C_2)\) using existing residual envelope lemma.
- Exact discrete representation of the local phase increment.
- Key blocker identified: missing micro‑window clustering control for zeros with \(|\Im\rho-m|\lesssim\delta\).

**Integration decision for v37**
- Include definition + split + residual budget lemmas.
- Promote “micro‑window clustering bound or pair‑isolation mechanism” as the explicit Missing Lever.

---

### RH‑LOCAL (PASS)
**What it delivered**
- Clean local phase budget lemma:
  \(\Delta_{I_+}\arg Z_{\rm loc}\le \pi N_{\rm loc}(m)\), i.e. θ=0 in the phase class.
- Parentheses warning: must distinguish \(\Im\int (\cdot)\) from \(\int\Im(\cdot)\).
- Confirmed: symmetry does not cancel in absolute bound; local term is δ‑inert unless endpoint uses cancellation.

**Integration decision for v37**
- Include lemma + the “parentheses hygiene” remark.

---

### RH‑ABSORB (CONDITIONAL)
**What it delivered**
- S5′ closure theorem template (budget spine) specialized to phase endpoints:
  exposes explicit exponents \((p,\theta,q)\) and **uniform closure conditions**.
- Two decisive NO‑GO eliminations:
  1) raw Δarg endpoints have p=0 ⇒ cannot close;
  2) any endpoint whose proof reduces to absolute \(L^2\) collars has p=θ ⇒ cannot close.
- Paste‑ready “S5′ acceptance gate” remark (prevents drift).

**Integration decision for v37**
- Insert theorem + gate remark as the canonical truth spine for S5′.
- Place adjacent to v36’s general S5 Budget Theorem; make clear it is a specialization/companion, not a new claim of closure.

---

## 3) Net posture update after Batch 6

**S5′ is still CONDITIONAL**.  
The v37 build should *not* claim RH or closure.

**What is now crystal clear**
- We have a forceable phase witness (\(\pi/2\) forcing).
- We have δ‑shrinkable residual control (O(δ log m)).
- The only obstruction is the **local phase pile‑up** (micro‑clustering / lack of cancellation).

So the program has converged to one frontier problem:
> **Invent an endpoint / mechanism that makes the local penalty shrinkable under δ0, without breaking forceability.**

---

## 4) v37 “Missing Lever” (should be boxed in-text)

One of the following must be produced (any one is decisive):
1. a cancellation endpoint class in which the local kernels have bounded endpoint norm (θ≈0) and the UE inequality has p≥1/2, or  
2. a micro-window zero bound N_micro(m,δ)=O(1) (or similar) that forces q=0 in the local growth model, or  
3. a pair-isolation lemma showing only the forced pair contributes O(1) and the rest contributes O(δ log m).

---

## 5) What v37 must NOT do (no-drift)

- Must not revert to “try to recover δ^{3/2}” as the target.
- Must not introduce point evaluation, absolute \(L^r\) endpoints, or projection endpoints without redesigning forcing.
- Must keep the acceptance gates fail‑closed: missing \((p,\theta,q)\) metadata ⇒ endpoint rejected.

