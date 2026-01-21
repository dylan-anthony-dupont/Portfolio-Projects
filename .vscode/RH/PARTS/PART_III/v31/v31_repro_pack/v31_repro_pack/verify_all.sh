#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

echo "[1/4] sha256 integrity"
sha256sum -c SHA256SUMS.txt

echo "[2/4] tail certificate (v29 anchor m=6e12)"
python3 v31_verify_tail_certificate.py --constants v29_constants.json --certificate v29_tail_certificate.json

echo "[3/4] tail certificate (v31 low anchor m=10)"
python3 v31_verify_tail_certificate.py --constants v31_constants_m10.json --certificate v31_tail_certificate_m10.json

echo "[4/4] front-end logical discharge (H0 <= cited height)"
python3 v31_verify_frontend_certificate.py --certificate v31_frontend_certificate.json

echo "ALL CHECKS PASSED"
