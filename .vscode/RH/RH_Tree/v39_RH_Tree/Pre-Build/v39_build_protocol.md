# v39 Build Protocol (pre‑build) — Batch‑9 locked

**Date:** 2026-01-26  
**Baseline:** v38 locked (`manuscript_v38.tex`, repro pack)  
**Objective:** produce v39 as a *truth‑latching* build that installs defect tooling + resonance NO‑GO + Missing Lever reframing, without drifting the spine.

---

## 0) Non‑negotiable guardrails (do not violate)

1. **ENT hygiene:** keep `E` as the even entire completion (xi/Λ object) fixed in v38.
2. **Endpoint class hygiene:** do **not** silently swap endpoints:
   - If we keep `\widetilde D_B(W)` as the forced endpoint, say so.
   - If we introduce `\Phi_B^{\rm def}(a)`, label it as tooling unless a forcing/transfer lemma is proven.
3. **NO‑GO latches must remain in‑text**:
   - one‑pole phase endpoint NO‑GO (v38),
   - resonance δ‑inert NO‑GO (new in v39).
4. **Fail‑closed posture:** Missing Lever box stays OPEN.

---

## 1) Patch application order (deterministic)

Apply patches exactly in this order (see `v39_patch_queue_batch9.md`):

1. Patch 1 — Defect primitives definitions (`\mathcal Q_a`, `\mathcal L_a`, `\Phi_B^{\rm def}(a)`).
2. Patch 2 — Local cancellation lemma (removable singularity + `O(\delta/a)` pair term).
3. Patch 3 — Bridge tooling (collar safety under shifts + difference kernel estimate).
4. Patch 4 — Defect UE skeleton + resonance definition (`R_a(m)` or `N_{\rm near}`).
5. Patch 5 — Resonance NO‑GO lemma (δ‑inert countermodel).
6. Patch 6 — Replace Missing Lever box (Domination + Defect UE + Resonance control).
7. Patch 7 (optional) — Harness-only pole‑winding forcing lemma, labeled as diagnostic.

---

## 2) Integration checks (must pass before calling v39 “pre‑build ready”)

### 2.1 Terminology and scope checks
- Verify every instance of “entire” refers to `E` (completed object), not to `\zeta(s)` itself.
- Verify `\mathcal Q_a`/`\mathcal L_a` definitions use the same `E(v)` as v38 (no silent redefinition).

### 2.2 s→u→v frame mapping checks (S6 mandatory)
Add (or confirm) a small subsection:

- `u=2s`, `v=u-1`.
- Off-axis zero `s=\beta+i\gamma` corresponds to `v=a+i m` with `a=2\beta-1`, `m=2\gamma`.
- Explicit formula amplitude contribution is `x^{\beta}` → leak corresponds to `a>0`.

### 2.3 Labeling / cross-reference checks
- New lemmas must not renumber existing v38 lemmas incorrectly.
- The Missing Lever box must reference the correct endpoint symbols.

### 2.4 “Drift prevention” checks
- Ensure no claim of RH closure is added.
- Ensure no step reintroduces forbidden “residual proxying” or pointwise UE.

---

## 3) Repro pack updates (pre‑build only)

Add a tiny markdown checklist file inside the repro pack:

- `defect_tooling_installed = true`
- `horizontal_resonance_nogo_installed = true`
- `missing_lever_open = true`

(Optional) Add a notebook/script stub that numerically illustrates the δ‑inert countermodel
for the toy factor (clearly labeled “toy”).

---

## 4) Output artifacts to generate once v39 is built (post‑GO)

When you later give “GO v39 build”, we will produce:

- `manuscript_v39.tex` and `manuscript_v39.pdf`
- `v39_patchlog.md` (diff vs v38)
- `integration_notes_v39.md`
- `CR_master_dashboard_v39_locked.md` (+ update canonical `CR_master_dashboard.md`)
- `v39_repro_pack.zip` updated to include the new latches

---

## 5) Definition of “v39 success” (truth‑latching)

v39 is successful if, after reading only v39:

- the Missing Lever is uniquely identified as **Domination + Defect UE + Resonance control**, and
- the resonance NO‑GO makes it impossible to “handwave δ^{p>0}” without confronting horizontal resonance.

