# v30 Status Decision (RH closure claim posture)

Date: 2026-01-17

## A. What was verified in this chat

### A1) Tail certificate code executes and verifies

Using the uploaded v29 bundle files and a v30 canonical verifier entrypoint, the tail certificate
verification **passes**:

- Command:
  ```bash
  cd v30_repro_pack
  python3 v30_verify_tail_certificate.py \
    --constants v29_constants.json \
    --certificate v29_tail_certificate.json
  ```
- The verifier prints the strict interval check
  `CHECK: lhs.hi < rhs.lo : True`
  and returns `RESULT: PASS`.

The exact stdout used for the manuscript is stored verbatim in:
`v30_repro_pack/v30_verifier_output.txt`.

### A2) Code ↔ manuscript alignment (tail inequality object)

The v29→v30 tail inequality is stated in **residual form** in terms of
`sup_{∂B} |F'/F|` (not `E'/E`), and the certificate generator/verifier uses the same residual
quantity via `L(m) = C1 log m + C2`. This eliminates the v28 “E'/E vs F'/F” mismatch.

## B. What the tail certificate does and does not prove

### It DOES prove

Given the constant intervals in `v29_constants.json`, the generator produces a deterministic
interval enclosure of `lhs_interval` and `rhs_interval` at `(m,α)=(6·10^12, 1)` and the verifier
checks the strict inequality `lhs.hi < rhs.lo`.

This is a genuine *interval* proof of the one-height inequality **conditional on the constants
file**.

### It DOES NOT prove

The certificate **does not** (by itself) establish that the constants in `v29_constants.json`
are valid bounds for the analytic quantities claimed in the manuscript. In particular, the bundle
does not include an independent certified derivation or computation for:

- residual envelope constants `(C1, C2)` controlling `sup_{∂B} |F'/F|`, and
- shape-only constants `(C_up, C_h'')` (called `C_up` and `C_hpp` in JSON).

## C. Claim posture for v30

**Conclusion:** With the materials currently provided (v14, v25–v29 PDFs + v29 tail bundle),
I cannot honestly label the result an *unconditional proof of RH* in the usual mathematical sense,
because the constants ledger used by the tail certificate is not itself independently certified.

Therefore, v30 must be framed as a **conditional certified criterion**:

> RH follows provided (i) the published verified band up to height `3·10^12` holds, and
> (ii) the constants ledger enclosures in `v29_constants.json` are certified by an auditable
> derivation/computation matching the manuscript hypotheses.

## D. Minimum checklist to upgrade v30 from “criterion” to “unconditional (computer-assisted)”

To allow v30 to claim unconditional closure (in the computer-assisted sense), the following must
be added and hashed, with a one-command verifier for each item:

1) **Certification of (C1, C2)**
   - Either: explicit quantitative analytic derivation with fully explicit constants, OR
   - certified computation that upper-bounds `sup_{∂B} |F'/F|` on the required geometry.

2) **Certification of (C_up, C_h'')**
   - Either: explicit numeric bounds for the required operator norms/trace constants on the square
     boundary (shape-only), OR
   - a certified computation (interval arithmetic) that bounds the relevant kernels/norms.

3) **Pinning and reproducibility**
   - Each new certification artifact must be SHA-256 pinned, with exact commands and expected output,
     analogous to the existing tail certificate.

Once (1)–(3) exist, the *only remaining external input* is the published verified band result,
which is standard for computer-assisted proofs.

## E. Tick audit (supplementary numerics)

The tick generator audit is not proof-load-bearing in v30. Without an externally verified truth
zero dataset (or a certified enclosure method), it should be labeled *illustrative floating-point
numerics* even if it is reproducible.
