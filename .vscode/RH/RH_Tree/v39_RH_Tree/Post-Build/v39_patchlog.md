# v39 patchlog (relative to v38)

**Build date:** 2026-01-26 (Europe/London)  
**Baseline:** `manuscript_v38.tex` / `manuscript_v38.pdf`  
**Output:** `manuscript_v39.tex` / `manuscript_v39.pdf`

## Intent (v39)

v39 is a **frontier re-aim** build: it installs the *defect endpoint* primitives (S5^{\rm def}), proves the
**local cancellation** mechanism that destroys aligned-box forcing for defect endpoints, and hardens the
frontier statement as a three-part “Missing Lever” (Transfer + Defect-UE + Resonance control).

No RH claim is made.

---

## Patch Queue executed

### PQ39.1 — Defect endpoint primitives (new)
- Added **Defect quotient** and **defect log-derivative**:
  \(\mathcal Q_a(v)=E(v+a)/E(v-a)\), \(\mathcal L_a=(\log\mathcal Q_a)'\).  
- Added **Defect phase endpoint** functional \(\Phi_B^{\rm def}(a)\) on buffered contours.

**Location:** Section `S5′ frontier` (new Subsection “Defect quotient primitives and cancellation mechanism (v39)”).  
**Refs:** Defs. `def:defect-quotient`, `def:defect-endpoint`.

### PQ39.2 — Local cancellation lemma (new, proof-grade)
- Proved that if a quartet exists at \(\pm a\pm i m\), then \(\mathcal Q_a\) has a *removable singularity* at \(v=i m\),
  and the pure-pair contribution to \(\Phi^{\rm def}_{B(0,m,\delta)}(a)\) is only \(O(\delta/a)\) (shrinkable).

**Location:** same subsection.  
**Refs:** Lemma `lem:defect-cancellation` (+ proof).

### PQ39.3 — Resonance accounting + NO-GO (new)
- Added the **horizontal resonance sum** \(\mathcal R_a(m)\) (local-window accounting).  
- Added an **OPEN target** “defect UE” inequality (explicitly labeled OPEN).  
- Added a toy-model **NO–GO** lemma showing near-resonant quartets can make \(\Phi^{\rm def}\) **\(\delta\)-inert**.

**Location:** same subsection.  
**Refs:** Def. `def:resonance-sum`, Remark `rem:defect-UE-target`, Lemma `lem:defect-resonance-nogo`.

### PQ39.4 — Missing Lever statement rewritten (replacement)
- Replaced the v38 “Missing Lever” box with a v39 version that:
  1) demands a **Transfer/domination** link from \(D_B(W)\) to defect endpoints,  
  2) demands a **\(\delta\)-uniform defect UE**, and  
  3) demands **Resonance control** (explicitly latching the new NO–GO lemma).
- Explicitly latches the two decisive NO–GO constraints:
  one-pole endpoint no-gain, and resonance δ-inertia.

**Location:** Section `S5′ frontier` (Box `box:missing-lever-v39`).

### PQ39.5 — Reproducibility pack bump
- Forked `v38_repro_pack` → `v39_repro_pack` (rename + SHA refresh).  
- Updated manuscript reproducibility references to v39 pack.

---

## Known open obligations (carried forward)

- **Transfer/domination lemma** (defect endpoint ↔ forcing endpoint) — OPEN.
- **Defect UE with p>1** (δ-uniform constants) — OPEN.
- **Resonance control** (rule out / bound near-resonant quartets) — OPEN.

These are now the sole boxed frontier obligations (Box `box:missing-lever-v39`).
