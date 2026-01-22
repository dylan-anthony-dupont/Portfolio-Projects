# v33 reproducibility pack (audit scaffold)

This directory contains **optional sanity-check certificates** referenced by `manuscript_v33.tex`.

## What this pack is
- A deterministic set of scripts and JSON files that verify **strict separation** in the tail inequality
  at the low anchor `m=10, α=1` for a chosen small `η` and collar parameter `κ`.
- A pinned front-end certificate encoding the **finite-height verification input** (Platt–Trudgian 2021).

## What this pack is NOT
- It does **not** prove the analytic constants (`C_up, C1, C2, C_h''`); these remain manuscript obligations.
- It does **not** compute zeta zeros; the front-end certificate is a logic wrapper around the cited result.

## How to run
From this directory:

```bash
python3 v33_verify_tail_certificate.py --constants v33_constants_m10.json --certificate v33_tail_certificate_m10.json
python3 v33_verify_frontend_certificate.py --certificate v33_frontend_certificate.json
```

## Files
- `v33_constants_m10.json`: constants + parameters for the low-anchor tail check
- `v33_generate_tail_certificate.py`: deterministic generator (directed-rounding intervals)
- `v33_tail_certificate_m10.json`: pinned generated certificate
- `v33_verify_tail_certificate.py`: verifier (regen + strict separation)
- `v33_verifier_output_m10.txt`: verifier console output
- `v33_frontend_certificate.json`: pinned finite-height assumption statement
- `v33_verify_frontend_certificate.py`: logic-only verifier
- `v33_frontend_verifier_output.txt`: verifier console output
- `SHA256SUMS.txt`: SHA-256 hashes of the pack files (integrity check)
