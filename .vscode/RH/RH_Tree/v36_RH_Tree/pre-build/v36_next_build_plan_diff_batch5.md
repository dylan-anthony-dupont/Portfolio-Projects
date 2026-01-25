# v35 → v36 build plan (diff‑only; Batch‑5 driven)

Date: 2026-01-24  
Locked baseline: **v35** (2026-01-23)  
Next build: **v36 (guardrail + S5 narrowing)** — *no new claimed closure*

---

## 0) Non‑negotiables carried forward from v35 (do not regress)

- ENT hygiene stays: \(E(v)=\Xi_2(1+v)\), \(\Xi_2(u)=\xi(u/2)\) entire.
- Forcing is single‑box and constant‑limited: forced object is \(D_B(W)\).
- Bridge‑1 remains one‑way only (no converse).
- S1/S1′ (pointwise η‑absorption) is retired; do not resurrect.

---

## 1) The point of v36

v36 will **prevent drift** by codifying:
1) the **S5 acceptance criterion** (explicit endpoint + exponents + forceability),
2) a **general S5 budget theorem** (the only test that matters),
3) **baseline NO‑GO lemmas** eliminating dead endpoint classes, and
4) Appendix “discarded routes” entries documenting why they are dead.

This makes S5 research *auditable*: future endpoint proposals must pass explicit gates or they are invalid.

---

## 2) Planned manuscript edits (grouped)

### (A) Section 12 (S5 frontier) — acceptance, budget, and forceability gate
1. Insert Remark `rem:S5-accept` near the start of the S5 section (post‑Remark 12.1 or at the top of §12).  
2. Insert Theorem `thm:S5-budget` immediately after the existing exponent budget discussion (or right after v35 Theorem 10.12 / the S5 checklist).  
3. Strengthen forceability: add Lemma `lem:forceability-domination` + Remark `rem:s5-forceability-gate` near v35 Remark 12.1.

### (B) Section 12 — baseline NO‑GO subsection (new)
Add a new subsection (e.g. `subsec:S5-nogo-baseline`) containing:
- Bridge package: `lem:S5_Lp_collapse`, `prop:S5_Lp_nogo`, `rem:S5_endpoint_implication`  
  (rules out absolute \(L^r(\partial B)\) endpoints on \(|E'/E|\)).
- Envelope NO‑GO: `lem:S5-projection-nogo` + `rem:S5-nogo-consequence`  
  (rules out local‑kernel projection endpoints under forced \(D_B(W)\)).

### (C) Local toolbox (optional, but recommended as *documentation*)
- Insert `lem:Zloc-L2-collar` near the collar section (after Lemma 10.8) as a recorded fact about \(L^2\) local scaling.
- Move projection definition/lemma (`def:KB-projection`, `lem:proj-kills-Zloc`, `rem:proj-conditioning`) to Appendix D6 as supporting material (since the endpoint class is now NO‑GO).

### (D) Appendix A — discarded closure routes (expand)
Add two short discarded routes (as per RH‑ENVELOPE patch):
- D5: naive non‑pointwise \(L^2\) endpoint (subsumed by Bridge absolute \(L^r\) NO‑GO)
- D6: local‑kernel projection endpoint (explicit NO‑GO; documented)

---

## 3) Repro pack / harness (minor schema hygiene)

- Add/require explicit S5 metadata fields (if S5 experiments are run in future builds):
  - `endpoint_definition`, `p`, `theta`, `q`, `forceability_mode`, `theorem_reference`
- Fail closed: an S5 certificate is invalid if these fields are missing.

(No computational reruns required for v36; this is schema + documentation.)

---

## 4) Expected output artifacts for v36 lock

- `manuscript_v36.tex`, `manuscript_v36.pdf`
- `v36_repro_pack.zip` (schema-updated; no new computational claims)
- `v36_patchlog.md`
- `integration_notes_v36.md` (one-page)
- `CR_master_dashboard_v36_locked.md` (one-page)
- `v36_next_build_plan_diff.md` (forward-looking; cancellation endpoint search plan)

