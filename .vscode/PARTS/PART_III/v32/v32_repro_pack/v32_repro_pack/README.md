# v32 reproducibility pack

This bundle contains **optional** computer-checkable certificates used as sanity
checks in `manuscript_v32.tex`.

The v32 manuscript's *logical* tail closure is formulated as an **η-absorption**
argument (Section `sec:eta-absorption`): once the analytic constants are defined
and known to be finite and δ-uniform, one may choose η small enough so that the
tail inequality holds at the anchor height `m = 10`. The scripts here simply
verify the inequality for a particular conservative constants enclosure.

Contents
- `v32_generate_tail_certificate.py`: generates `v32_tail_certificate_m10.json`
  from `v32_constants_m10.json`.
- `v32_verify_tail_certificate.py`: recomputes the same bounds and checks the
  certificate matches (strict stringwise equality).
- `v32_generate_frontend_certificate.py` / `v32_verify_frontend_certificate.py`:
  a JSON wrapper recording the finite-height front-end claim (Platt--Trudgian
  height and the chosen low-height cutoff `H0`).
- `verify_all.sh`: one-shot generation + verification.

Reproduce
```bash
cd v32_repro_pack
./verify_all.sh
```
