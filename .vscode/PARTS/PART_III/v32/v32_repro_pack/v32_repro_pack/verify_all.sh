#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

echo "[1/2] Tail certificate"
python3 v32_generate_tail_certificate.py --constants v32_constants_m10.json --out v32_tail_certificate_m10.json
python3 v32_verify_tail_certificate.py v32_constants_m10.json v32_tail_certificate_m10.json | tee v32_verifier_output_m10.txt

echo "[2/2] Front-end certificate"
python3 v32_generate_frontend_certificate.py --H0 5 --out v32_frontend_certificate.json
python3 v32_verify_frontend_certificate.py --certificate v32_frontend_certificate.json | tee v32_frontend_verifier_output.txt
