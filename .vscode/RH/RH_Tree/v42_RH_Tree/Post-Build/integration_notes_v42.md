# Integration notes (v42 post-build)

Date: 2026-01-29 (Europe/London)

## 0) Objective of v42

Lock the **GEO–C4** geometry/endpoint redesign and produce the cleanest manuscript-to-date scaffold in which:

- **FORCE is closed**: an off-axis quartet forces a nonzero **k=2 boundary harmonic** on a hinge-centered witness circle.
- **Only one statement remains open**: **UE-INPUT** (a derivative field bound on shifted hinge circles), explicitly boxed.

## 1) Dependencies (truth-latched)

To ensure canonical synthesis across prebuild + Batch 12:

1. **E even entire** in the v-plane (xi-type completion) and standard quartet symmetry.
2. **Two-sided field definitions**:
   - `\mathcal L_t(v)=E'/E(v+t)-E'/E(v-t)`
   - `\mathcal D_{a,h}(v)=\mathcal L_{a+h}(v)-\mathcal L_{a-h}(v)`
3. **Witness geometry**: hinge-centered circle `C_{m,\delta}: v(\theta)=im+\delta e^{i\theta}`.
4. **Coupling**: `h=\kappa\delta` with fixed `\kappa\in(0,1)`.
5. **Monotone admissibility shrink**: shrinking `\delta` is always allowed (zeros are isolated), and UE must be stated in a form monotone in `\delta`.

These are the minimal dependencies needed to merge the prebuild plan with Batch 12’s forcing/UE reductions without accidental circularity.

## 2) Batch 12 synthesis outcome

Batch 12 converged on a single canonical endpoint choice:

- **Endpoint (GEO–C4)**: the normalized L^2 magnitude of the **k=2 Fourier projection** of
  `\psi(\theta)=\Im(\mathcal D_{a,h}(v(\theta)))` on `C_{m,\delta}`:
  `\Phi^\star=(\delta^2/h)\,\|P_2\psi\|_{L^2([0,2\pi])}`.

Key syntheses incorporated:

- **Toy forcing is exact** and survives shrink (`h<\delta`): the k=2 coefficient is computed by a geometric-series expansion.
- **Stability under analytic remainders**: decomposing `\mathcal D=\mathcal D^{\rm sing}+\mathcal R` gives normalized remainder `O(\delta)`.
- **UE reduction**: harmonic extraction + 2× integration-by-parts trades θ-oscillation for **v-derivatives**, yielding a `(\delta/a)^3` gain.
- **NO-GO scope audit**: projection endpoints are only “dead” when they annihilate the forced kernel or collapse to pointwise UE; GEO–C4 avoids that.

## 3) What changed in the manuscript (v41 → v42)

- Replaced the v41 “Geometry Change Requirement” blocker with the **GEO–C4 closure schema** box.
- Inserted a self-contained GEO–C4 section containing:
  - shift-admissibility definition + monotone shrink remark,
  - toy forcing lemma (explicit constant),
  - forcing stability lemma for the true E,
  - UE reduction lemma,
  - boxed UE-INPUT (single open statement),
  - dependency summary and NO-GO vs GEO–C4 table.
- Updated the executive status, NO-GO list, and S6 cross-check language to match GEO–C4.

## 4) Current frontier (v42)

### Sole open statement

**UE-INPUT (Box `box:ue-input-v42`)**:
A uniform bound on `\partial_t\partial_v^j\mathcal L_t` (j=0,1,2) on shifted hinge circles at the nominal policy
`\delta=\eta a/(\log(m+3))^2` (allowing smaller `\delta` for admissibility), sufficient to force
`\Phi^\star=o(1)`.

### Everything else

All other items are either:

- **closed** (FORCE, stability, admissibility shrink conventions), or
- **archived** as NO-GO diagnostics (S5′ defect endpoints / aligned-box micro-coupling routes), or
- **supporting infrastructure** (tail + front-end certificate harness).

## 5) Build outputs produced in this pass

- `manuscript_v42.tex`
- `manuscript_v42.pdf`
- `v42_patchlog.md`
- `v42_repro_pack/` and `v42_repro_pack.zip`
- `CR_master_dashboard_v42_locked.md`

