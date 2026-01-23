# v35 Build Protocol (from locked v34 baseline)

This protocol is what Control Room will execute **immediately** once you give “GO v35 build”.

## 0) Inputs (must be present)

- `manuscript_v34.tex` / `manuscript_v34.pdf`
- `v34_repro_pack.zip`
- Batch‑4 patch queue: `v35_patch_queue_batch4.md`
- Batch‑4 ingestion notes + dashboard:
  - `integration_notes_batch4.md`
  - `CR_master_dashboard_batch4.md`

---

## 1) Build philosophy (truth‑latch build)

v35 is not allowed to:
- claim η‑absorption tail closure under the pointwise/sup UE endpoint, or
- suggest forcing can be scaled to \(\log m\), or
- imply boundary modulus controls interior zeros.

v35 **must**:
- include the formal NO‑GO constraints (so drift cannot re-enter),
- fix ENT/holomorphy correctness,
- harden harness metadata for constant drift prevention.

---

## 2) Step-by-step execution

### Step 1 — Create v35 working copy
- Copy `manuscript_v34.tex` → `manuscript_v35.tex` (new file).
- Copy `v34_repro_pack.zip` → working folder `v35_repro_pack/` (unzip).

### Step 2 — Apply manuscript patches in queue order
Apply patches from `v35_patch_queue_batch4.md` in order:

1) `P35-ENT1` + `P35-ENT1b`  
2) `P35-BUDGET`  
3) `P35-UE-NOGO`  
4) `P35-FORCE-NOGO` + `P35-FORCE-COMPAT`  
5) `P35-BRIDGE-NOCONV`  
6) optional: `P35-LOCAL-NOGO-NOTE`  
7) `P35-FRONTIER-REWRITE`

### Step 3 — Cross-reference and hygiene checks (must-pass)
Run the following checks before compiling:

- `grep -n "Lambda_2 is entire" manuscript_v35.tex` → **no matches**
- `grep -n "E is entire" manuscript_v35.tex` → matches allowed only if ENT‑1 adopted (should be true)
- Search for any sentence implying: “|W|=1 on ∂B ⇒ W zero-free” → must be removed/guarded
- Verify that Theorem 11.1 / Eq (18) is unchanged unless explicitly intended

### Step 4 — Compile PDF
- Build `manuscript_v35.pdf` via LaTeX
- Fix any label shifts due to inserted lemmas/remarks

### Step 5 — Update repro pack (audit hardening)
Inside `v35_repro_pack/`:

- Apply `P35-HARNESS`:
  - update JSON schema fields (forcing constants, endpoint functional, forcing architecture)
  - update verifier scripts to print and assert alignment
- Re-run verifiers and save outputs:
  - `v35_tail_check_verifier_output_m10.txt`
  - `v35_frontend_verifier_output.txt` (if unchanged, still re-run to refresh hashes)
- Update `SHA256SUMS.txt`

### Step 6 — Create build artifacts
- `v35_patchlog.md` (diff vs v34, patch IDs + locations)
- `integration_notes_v35.md` (compact “what changed”)
- Update dashboard:
  - `CR_master_dashboard_v35_locked.md`
  - overwrite the canonical `CR_master_dashboard.md` with the v35 locked one

### Step 7 — Zip repro pack
- Zip `v35_repro_pack/` → `v35_repro_pack.zip`

---

## 3) Acceptance gates (GO/NO‑GO inside the build)

A v35 build is accepted only if:

1) ENT hygiene is correct (no false “Λ₂ entire” statements).
2) NO‑GO lemmas are present and referenced:
   - UE scaling obstruction
   - forcing constant‑limited
   - boundary modulus “no converse”
   - exponent budget theorem
3) Harness metadata prevents constant drift:
   - JSON includes explicit forcing constants and endpoint strings
   - verifier prints them

If any gate fails, v35 must not be “locked” and must be rebuilt.

---

## 4) Post-build deliverables (what you will receive)

- `manuscript_v35.tex`
- `manuscript_v35.pdf`
- `v35_repro_pack.zip`
- `v35_patchlog.md`
- `integration_notes_v35.md`
- `CR_master_dashboard_v35_locked.md`
- `v35_next_build_plan_diff.md` (forward plan, v35→v36)

