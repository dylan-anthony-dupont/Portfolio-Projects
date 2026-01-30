# v42 Patchlog (from v41)

Date: 2026-01-29 (Europe/London)

This patchlog records the **manuscript-level** changes applied to produce **v42** from **v41**.

## 1) Frontier switch: GEO–C4 locked; S5′ defect endpoints archived

- **Replaced** the v41 “Geometry Change Requirement” blocker with a **locked geometry/endpoint choice**:
  - **Witness:** hinge-centered circle `C_{m,\delta} : v(\theta)=im+\delta e^{i\theta}`
  - **Field:** two-sided shift-difference log-derivative `\mathcal D_{a,h}`
  - **Endpoint:** the **k=2 harmonic projection** of `\psi(\theta)=\Im(\mathcal D_{a,h}(v(\theta)))`, normalized as
    `\Phi^\star = (\delta^2/h)\,\|P_2\psi\|_{L^2([0,2\pi])}`.
- **Demoted** all prior S5′ “centered defect” endpoints to **archived NO-GO diagnostics** (kept for audit/history).

## 2) Forcing chain: made proof-grade and δ-robust

- Added a **toy forcing lemma** for a single quartet showing an **explicit k=2 boundary carrier** and computing the
  k=2 coefficient by a geometric-series expansion (valid for `h<\delta`).
- Added a **stability lemma** (“forcing survives admissibility shrink”) that decomposes
  `\mathcal D_{a,h}=\mathcal D^{\rm sing}+\mathcal R` and shows the normalized remainder is `O(\delta)` while the
  normalized singular contribution is an **absolute constant**.

## 3) UE reduction: single open statement boxed

- Added an integration-by-parts / harmonic-extraction lemma reducing `\Phi^\star` control to
  **derivative bounds** for `\partial_v^j \mathcal D_{a,h}` (j=0,1,2), yielding the exponent-budget gain
  `\Phi^\star \ll (\delta/a)^3 A(m,a)`.
- Boxed the **only active open statement (UE-INPUT)** as a uniform field bound for
  `\partial_t\partial_v^j \mathcal L_t` on shifted hinge circles, sufficient to force `\Phi^\star=o(1)` at the
  nominal policy `\delta=\eta a/(\log(m+3))^2`.

## 4) NO-GO scope audit

- Updated the executive NO-GO list to clarify that “projection endpoints are dead” applies only when the projection
  **annihilates the forced local kernel** or collapses to pointwise/supremum UE.
- Added a compact **NO-GO vs GEO–C4** table and a one-line **dependency chain** summary.

## 5) S6 cross-check update

- Updated the S6 harness paragraph to explicitly align GEO–C4 with the explicit-formula interpretation:
  off-axis tilt `a>0` corresponds to `\beta=1/2+a/2` and an amplitude leak `x^{a/2}`.

## 6) Repro pack namespace bump

- Created `v42_repro_pack/` by copying the v41 certificate harness and updating the README + checksums.
- Updated manuscript listings to point at `v42_repro_pack/`.

## 7) Outputs

- `manuscript_v42.tex`, `manuscript_v42.pdf`
- `v42_repro_pack/` (directory) and `v42_repro_pack.zip`
- `integration_notes_v42.md`
- `CR_master_dashboard_v42_locked.md`

