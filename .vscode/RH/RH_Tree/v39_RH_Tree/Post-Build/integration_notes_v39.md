# Integration Notes — v39 (locked)

**Build:** v39  
**Date:** 2026-01-26 (Europe/London)  
**Baseline:** v38 locked  
**Result:** PASS (architecture hardening + new defect endpoint tooling installed)

## What v39 changes (high-signal only)

### 1) S5′ frontier is re-aimed to S5^{\rm def} (defect endpoint redesign)
v39 formalizes the defect endpoint class:

- Defect quotient: \(\mathcal Q_a(v)=E(v+a)/E(v-a)\)
- Defect log-derivative: \(\mathcal L_a(v)=(\log\mathcal Q_a)'=\frac{E'}{E}(v+a)-\frac{E'}{E}(v-a)\)
- Defect phase endpoint on buffered contours: \(\Phi^{\rm def}_B(a)\)

This is installed in the manuscript as Definitions `def:defect-quotient` and `def:defect-endpoint`.

### 2) Proof-grade local cancellation is now explicit (and decisive)
Lemma `lem:defect-cancellation` proves:

- If a quartet exists at \(\pm a\pm i m\), then \(\mathcal Q_a\) has a **removable singularity** at \(v=i m\).
- Therefore, **no aligned-box forcing** exists for \(\Phi^{\rm def}\) at \(v=i m\); the pure-pair contribution is only \(O(\delta/a)\).

This explains (referee-grade) why earlier “force → UE → absorption” attempts for *defect* endpoints cannot work without a transfer lemma.

### 3) Resonance is now the explicit enemy (and latched)
v39 installs:

- A local-window resonance accounting object \(\mathcal R_a(m)\) (Definition `def:resonance-sum`).
- An OPEN target defect-UE inequality (Remark `rem:defect-UE-target`).
- A toy-model NO–GO lemma showing **near-resonant quartets can make \(\Phi^{\rm def}\) δ-inert** (Lemma `lem:defect-resonance-nogo`).

This is the exact mechanism behind the “two branches disagreeing” risk: if one tries to prove UE without resonance control,
the NO–GO model shows it can fail even when the forced quartet cancels.

### 4) Missing Lever box rewritten (single source of truth)
The boxed frontier statement is replaced by Box `box:missing-lever-v39`:

- (ML-1) Transfer / domination: \(D_B(W)\) must be dominated by a defect endpoint class.
- (ML-2) Defect UE: δ-uniform UE bound with effective \(p>1\).
- (ML-3) Resonance control: bound/exclude horizontal resonance (else δ-inert obstruction).

Also latches the two NO–GO constraints: one-pole no-gain, resonance δ-inertia.

## Branch payload mapping (Batch 9)

- **RH-LOCAL:** provided the defect cancellation mechanism and removable-singularity explanation; integrated into Lemma `lem:defect-cancellation`.  
- **RH-BRIDGE:** shift-stability/collar-transfer framing; integrated as Lemma `lem:defect-shift-stability`.  
- **RH-ENVELOPE:** resonance accounting direction; integrated as \(\mathcal R_a(m)\) + the δ-inert NO–GO lemma.  
- **RH-FORCE:** (kept as harness-only) shows defect quotients can be forceable on *defect boxes* centered at \(2a+i m\) via pole-winding; **not used** for UE.  
- **RH-ABSORB:** confirms that if a UE with \(p>1\) exists, absorption closure is structurally correct; carried forward as conditional logic only.

## Net posture after v39

**Primary spine:** S5^{\rm def} (conditional)  
**Secondary harnesses:** S6 explicit-formula mapping + existing tail check scaffold.

v39 is a “truth-latching” build: it clarifies why aligned defect forcing fails, and it isolates the remaining analytic missing lever
into a finite checklist (Transfer + UE + Resonance control) with explicit NO–GO latches.

