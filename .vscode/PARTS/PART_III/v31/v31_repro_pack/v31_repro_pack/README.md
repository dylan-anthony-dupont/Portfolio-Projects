# v31 Repro Pack

This folder contains the computational artifacts referenced by `manuscript_v31.pdf`.

## Quick verification

You can also run:

```bash
./verify_all.sh
```

## Quick verification (3 commands)

From this directory:

1. Verify file integrity:

```bash
sha256sum -c SHA256SUMS.txt
```

2. Verify the historical (v29) tail certificate at `m_band = 6e12`:

```bash
python3 v31_verify_tail_certificate.py \
  --constants v29_constants.json \
  --certificate v29_tail_certificate.json
```

3. Verify the low-anchor (v31) tail certificate at `m_star = 10`:

```bash
python3 v31_verify_tail_certificate.py \
  --constants v31_constants_m10.json \
  --certificate v31_tail_certificate_m10.json
```

## Front-end certificate (literature-based)

The manuscript's low-height "front-end" requirement is encoded in:

- `v31_frontend_certificate.json`

Generate and verify its internal logic:

```bash
python3 v31_generate_frontend_certificate.py --H0 5 --out v31_frontend_certificate.json
python3 v31_verify_frontend_certificate.py --certificate v31_frontend_certificate.json
```

**Note:** these scripts do not re-run Platt--Trudgian's computation; they only record the exact
height statement required by v31 and check that it is within the cited verification height.

## Ledger self-check

To check internal formatting consistency (not mathematical correctness) of a constants ledger:

```bash
python3 v31_check_ledger_format.py --constants v29_constants.json
```
