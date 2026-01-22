# v33 Patchlog (relative to v32)

Date: 2026-01-21  
Base: `manuscript_v32.tex` → Output: `manuscript_v33.tex` / `manuscript_v33.pdf`

## High-level intent

Integrate **Batch 1 branch patch packets** into the v32 post-pivot spine so we can start the v32→v33 build
with (i) restored forcing provenance, (ii) hardened Bridge‑1 hypotheses, (iii) explicit local-window counts,
and (iv) admissibility/absorption hygiene improvements, while keeping the remaining proof-grade blockers
explicitly tracked.

## Manuscript changes (proof-spine significant)

### (G‑3) K_alloc provenance restored (FORCING)

- **Change:** In the tail inequality constant ledger, set  
  \(K_{\rm alloc} := 3 + 8\sqrt{3}\)  
  (replacing the incorrect placeholder \(1/4\)).
- **Where:** `Theorem (Tail inequality)` assumptions and downstream occurrences in the tail/absorption sections.
- **Reason:** Align manuscript with the forcing lemma’s actual constant, eliminating silent weakening of the forcing budget.

### (G‑6) Bridge‑1 hypotheses hardened (BRIDGE)

- **Change:** Replaced the earlier “outer factor = harmonic conjugate + max modulus” formulation with:
  - Dirichlet outer factor existence on a rectangle (`Lemma: Dirichlet outer factor on a box`).
  - Inner-collapse (`Prop: Bridge 1`) proved via **Dirichlet uniqueness** (no boundary-regularity loopholes).
- **Where:** Section “Outer factorization and the inner quotient (Bridge 1)”.
- **Reason:** Remove ambiguity about boundary values and make the logic referee-robust.

### (G‑8) Explicit local window zero bound inserted (LOCAL)

- **Change:** Replaced the qualitative `N_loc(m) << log m` lemma with the explicit unconditional bound  
  \(N_{\rm loc}(m) \le 1.01\log m + 17\) for \(m\ge 10\), derived from a literature explicit bound for `N(T)`.
- **Where:** Lemma `Nloc-logm` (retained label to minimize downstream edits), and the corollary feeding the tail.
- **Reason:** Make the local term *numerically controllable* in the tail inequality.

### (G‑4 / G‑5 partial) δ0 vs δ + admissibility shrink hygiene (ABSORB)

- **Change:** Introduced the nominal scale \(\delta_0=\eta\alpha/(\log m)^2\) and separated it from a chosen
  admissible \(\delta\le\delta_0\).
  Added:
  - `Lemma: collar-existence` (non-circular existence of κ-admissible shrink).
  - `Lemma: delta-shrink-monotone` (tail inequality monotone-safe under shrinking δ).
- **Where:** Section `Aligned boxes`, Definition `collar-admissible`, tail section.
- **Reason:** Prevent hidden dependence on unknown zeros and make “shrink δ if needed” formally safe in the inequality chain.

### (G‑10 hygiene) “No residual proxying” interface warning (ENVELOPE/CONTROL ROOM)

- **Change:** Added a remark right after the upper-envelope lemma clarifying that residual control `F'/F` does not directly
  control `E'/E`, and must be routed through the log-derivative split and collar bound.
- **Where:** Immediately after `Lemma: upper-envelope`.
- **Reason:** Prevent subtle interface misuse that can create circularity or hidden assumptions.

## Repro pack refresh (new format)

A new `v33_repro_pack/` is created from scratch (not inherited from earlier repro formats), containing:

- Tail certificate generator/verifier for the **full v33 tail inequality** (including the local term).
- Front-end certificate/verifier as a pinned logic wrapper around the cited finite-height verification.
- SHA256 hashes for integrity.

See: `v33_repro_pack.zip` for a single handoff artifact.

## Known OPEN items (unchanged from v32, explicitly tracked)

- Full analytic proof of the residual envelope lemma constants (`C1,C2`) and boundary/upper-envelope constants
  (`C_up, C_h''`) with explicit δ-uniformity discipline (G‑1, G‑4, G‑12).
- Upper-envelope scaling audit (the δ-exponent bookkeeping must be rechecked end-to-end).
- External front-end dependence remains (G‑11) unless replaced by an internal verified band procedure.

