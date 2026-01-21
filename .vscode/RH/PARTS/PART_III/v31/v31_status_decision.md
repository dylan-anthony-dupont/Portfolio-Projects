# v31 status decision (2026-01-17)

## Decision

**Unconditional proof closure is NOT achieved in v31.**

v31 is an **improved certified-criterion manuscript**. The computational part of the **tail certificate** is
now verified at the **minimal admissible anchor** `m_* = 10` (width–2 height), so the analytic tail
covers all `m >= 10` *conditional on* the correctness of the constants-ledger enclosures
`(C1,C2,C_up,C_hpp,eta)`.

However, the constants ledger is **not independently certified** (no complete provenance chain), so the
core hard gate remains.

## What is now genuinely verified (executed computations)

All computations below were executed in the sandbox and are pinned in `v31_repro_pack/`.

### 1) Tail certificate (historical v29 anchor)

- Constants: `v31_repro_pack/v29_constants.json`
- Certificate: `v31_repro_pack/v29_tail_certificate.json`
- Verifier: `v31_repro_pack/v31_verify_tail_certificate.py`

Result:
- Regeneration check: **PASS**
- Strict interval inequality: `CHECK: lhs.hi < rhs.lo : True`

Verbatim stdout: `v31_repro_pack/v31_verifier_output_m6e12.txt`.

### 2) Tail certificate (new low anchor)

- Constants: `v31_repro_pack/v31_constants_m10.json` (same ledger intervals as v29; `m_band=10`)
- Certificate: `v31_repro_pack/v31_tail_certificate_m10.json`
- Verifier: `v31_repro_pack/v31_verify_tail_certificate.py`

Result:
- Regeneration check: **PASS**
- Strict interval inequality: `CHECK: lhs.hi < rhs.lo : True`

Verbatim stdout: `v31_repro_pack/v31_verifier_output_m10.txt`.

### 3) Front-end (finite-height remainder)

With `m_* = 10`, the tail covers all width–2 heights `m >= 10`, leaving only `0 < m < 10`, i.e.
`0 < Im(s) < 5`.

v31 discharges this by citation to:

- **Platt–Trudgian (2021)**: *The Riemann hypothesis is true up to 3*10^12* (interval arithmetic).

A pinned JSON record of the exact finite-height statement used and the reference is in:

- `v31_repro_pack/v31_frontend_certificate.json`

The accompanying verifier only checks the internal logical implication `H0 <= H_cited` and prints PASS:

- `v31_repro_pack/v31_frontend_verifier_output.txt`

## What the tail certificate does and does not prove

**It proves:** Given the ledger intervals in the constants JSON, the one-height tail inequality holds
with strict interval separation at the anchor, hence (by the manuscript’s monotonicity lemma) holds
for all larger heights.

**It does NOT prove:** That the ledger constants are correct bounds for the mathematical quantities
asserted in the residual envelope and shape-only lemmas.

## Remaining hard gate for an unconditional RH claim

To promote v31 to an unconditional proof, one must provide an **independent certification** of each
ledger constant interval:

- `C1, C2`: residual envelope for `sup_{∂B} |F'/F| <= C1 log m + C2` (uniform in `m >= 10` and
  admissible `α` with `δ = ηα/(log m)^2`).
- `C_up`: upper-envelope constant in the boundary-program inequality.
- `C_hpp`: horizontal-budget constant in the boundary-program inequality.

No such end-to-end certification is currently present in the artifact bundle.

## Recommended next steps

1) **Lock down mathematical specifications** for each ledger constant (exact supremum/operator norm,
   domain geometry, and hypotheses).
2) Choose certification route:
   - analytic derivation with explicit constants, or
   - hybrid analytic reduction + **ball/interval arithmetic** computation (recommended: Arb/Acb), or
   - fully computational enclosure.
3) Provide a deterministic repro pipeline:
   - pinned code + pinned environment (Docker digest),
   - pinned intermediate outputs,
   - `sha256sum -c SHA256SUMS.txt` integrity checks,
   - and verifiers that output `PASS/FAIL`.

The manuscript v31 includes a concrete certification plan outline in Section “Ledger certification
hard gate” and Appendix “Ledger certification plan.”

## Artifacts produced

- `manuscript_v31.tex`
- `manuscript_v31.pdf`
- `v31_repro_pack.zip` (contains `v31_repro_pack/`)
- `v31_status_decision.md` (this file)
