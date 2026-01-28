# v40 next build plan (diff-only) — v39 → v40

**Date:** 2026-01-26 (Europe/London)  
**Baseline:** v39 locked (`manuscript_v39.*`)  
**Target:** v40 PRE-BUILD plan (do not claim closure; close ML-1..ML-3 or prove impossibility)

---

## A) Hard requirement: pick one “Missing Lever closure story” and lock it

v39’s boxed frontier (Box `box:missing-lever-v39`) is now the single source of truth.

v40 must either:

1. **Close ML-1..ML-3** (even partially, with explicit constants + audit trail), or  
2. **Prove a clean impossibility / obstruction** for at least one of ML-1..ML-3 inside the current architecture.

No new endpoint class is permitted in v40 unless it replaces one of ML-1..ML-3 with a strictly stronger/cleaner obligation.

---

## B) ML-1 Transfer/domination (highest priority)

**Goal:** a proof-grade domination link transporting forcing from the W-endpoint to a defect endpoint.

Candidate targets (choose exactly one and pursue it):

- **(T1) Same-box transfer:** \(D_{B(\pm a,m,\delta)}(W)\le C\,\Phi^{\rm def}_{B(0,m,\delta)}(a)+\mathrm{Err}\).  
- **(T2) Shifted-box transfer:** compare \(B(\pm a,m,\delta)\) to a controlled shift \(\widehat B\) where \(\mathcal Q_a\) is natural.  
- **(T3) Product-factor transfer:** an identity showing \(W\) is (up to a controlled outer factor) a multiplicative functional of \(\mathcal Q_a\).

**Deliverable:** a lemma with a complete proof (or a theorem-style reduction to one explicit analytic estimate).

---

## C) ML-2 Defect UE with p>1 (δ-uniform)

**Goal:** upgrade the OPEN target (Remark `rem:defect-UE-target`) into a proved bound, or replace it with a proved bound
of the same type with an effective exponent \(p>1\).

Required properties:

- constants independent of \((m,a,\delta)\) in the nominal regime \(0<\delta\le \delta_0(m,a)=\eta a/(\log m)^2\),
- explicit dependence on \(\mathcal R_a(m)\) (or a stronger resonance-control object),
- audit-friendly decomposition: “local window” + “residual envelope ledger”.

---

## D) ML-3 Resonance control (make δ-inert NO–GO impossible)

**Goal:** show \(\mathcal R_a(m)\) is uniformly bounded (or bounded by \(O(\log m)\) with enough slack),
or else add a provable “resonance exclusion” hypothesis and propagate it to a contradiction.

Two acceptable outcomes:

- **(R1) Bound:** \(\mathcal R_a(m)\le C\) (or \(\le C\log m\)) in the regimes needed by ML-2.  
- **(R2) Exclusion:** show that the near-resonant configuration behind Lemma `lem:defect-resonance-nogo`
cannot occur for the actual completed \(E\) (using functional equation / Jensen / local density constraints).

---

## E) Harness: keep S6 explicit-formula leak mapping pinned

v40 must keep the S6 cross-check mandatory:

- \(s=\beta+i\gamma\), \(u=2s\), \(v=u-1\) ⇒ \(a=2\beta-1\), \(m=2\gamma\).
- Any off-line zero (\(\beta>1/2\)) corresponds to an explicit-formula term amplitude \(x^\beta\)
(i.e., an “amplitude leak”).

If any new endpoint is proposed, it must explicitly answer:
“does this endpoint correspond to an \(x^\beta\) leak or not?”

---

## F) Repro pack deltas (v40)

- Add a tiny “Missing Lever tracker” JSON with fields `{ML1_status, ML2_status, ML3_status}`.
- Add a harness script that numerically evaluates \(\Phi^{\rm def}\) for toy models (including the δ-inert NO–GO construction),
to prevent accidental drift back into resonance-blind UE claims.

