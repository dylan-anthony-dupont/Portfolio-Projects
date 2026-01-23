# v35 patchlog (relative to v34)

Date locked: 2026-01-23  
Build intent: **truth-latch** (codify NO-GO constraints; prevent drift back to v33 absorption narrative)

## High-level posture change

- **S1 / pointwise η-absorption closure is formally discarded** under current proved inputs.
- The manuscript’s main deliverable is now the **tail criterion family** (per-height, per-α) + finite-height front-end.
- The analytic frontier is reframed as **S5: non-pointwise upper-envelope redesign** (endpoint + collar interface).

## Proof-spine changes (patch IDs)

### P35-ENT-1 — Completion / holomorphy hygiene (CRITICAL)
- Replaced the working function `E(v)=Λ₂(1+v)` with the **entire** completion
  \(\Xi_2(u):=\xi(u/2) = \frac{u(u-2)}{8}\Lambda_2(u)\), and recentered
  \(E(v):=\Xi_2(1+v)\).
- Updated the residual log-derivative identity accordingly:
  \(E'/E\) now includes the bounded completion terms \(1/u+1/(u-2)\).
- Quartet symmetry statements now explicitly refer to zeros of \(\Xi_2\).

### P35-UE-BUDGET — Exponent budget obstruction (CRITICAL)
- Added **Theorem `exponent-budget`**: under the nominal scaling
  \(\delta_0(m,\alpha)=\eta\alpha/(\log m)^2\) and growth \(N_{\rm loc}(m)\ll\log m\),
  uniform η-shrinking requires **\(p-\theta\ge 1/2\)**.
- Strengthened the “UE gate” remark to encode the budget condition explicitly.

### P35-UE-NOGO — Pointwise endpoint scaling NO-GO (CRITICAL)
- Added **Lemma `UE-scaling-nogo`**: with pointwise/sup endpoint \(\sup_{\partial B}|E'/E|\) and shape-only constants,
  **no UE exponent \(p>1\)** is possible. This prevents “recover δ^{3/2}” drift inside the same endpoint class.

### P35-FORCE-NOGO — Forcing cannot grow with height (HIGH)
- Added **Lemma `force-constant-limited`**: in the single-box forcing architecture,
  \(\Delta_{I_+}\arg Z_{\rm pair}\le 2\pi\) uniformly, so the forcing constant is **O(1)** and cannot scale like \(\log m\).

### P35-BRIDGE-NOCONVERSE — Boundary-modulus converse forbidden (HIGH)
- Added **Remark `no-converse`**: \(|W|=1\) on \(\partial B\) does not imply interior zero-freeness; Bridge-1 is strictly one-directional.

### P35-S5-FRONTIER — Replace absorption section with S5 template (CRITICAL)
- Removed the main-text “conditional absorption closure” section.
- Inserted **Section `S5 frontier`**: open redesign checklist + forcing-compatibility condition (forceability remark).
- Added **Appendix `Discarded closure routes`** with concise NO-GO reasons and a historical record proposition (explicitly marked “not used”).

### P35-HARNESS — Repro pack metadata latch (MED)
- Updated the repro pack schema to record:
  - `UE_endpoint_class`, `endpoint_functional`
  - `forcing_architecture`, `forcing_constants` (expression strings)
- Updated generator/verifier scripts to assert metadata consistency.

## Files produced

- `manuscript_v35.tex`, `manuscript_v35.pdf`
- `v35_repro_pack.zip` (contains `v35_repro_pack/`)
- `v35_patchlog.md` (this file)
- `integration_notes_v35.md` (integration digest)
- `CR_master_dashboard_v35_locked.md` + updated `CR_master_dashboard.md`
- `v35_next_build_plan_diff.md`
