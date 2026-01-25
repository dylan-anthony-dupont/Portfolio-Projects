# v37 Build Protocol (when GO is given)

Date: 2026-01-25  
Baseline: **v36 locked** (`manuscript_v36.tex/pdf`, repro pack v36)  
Build type: **Architecture build** (S5′ toolkit integration; no closure claims)

This protocol is designed to be fail-closed: if any NO–GO condition triggers, the build is rejected and must be repaired before locking v37.

---

## 0) Inputs required

From the Control Room pre-build artifacts (Batch 6):
- `v37_patch_queue_batch6.md` (patch IDs P37.1–P37.4)
- `v37_next_build_plan_diff_batch6.md`
- `CR_master_dashboard_batch6.md`
- `integration_notes_batch6.md`

Baseline manuscript:
- `manuscript_v36.tex` and compiled `manuscript_v36.pdf`

---

## 1) Build steps (deterministic)

### Step 1 — Create v37 working copy
- Copy `manuscript_v36.tex` → `manuscript_v37.tex`.
- Add header note in the TeX front-matter:
  - “v37 is an S5′ architecture build; no RH claim; installs phase endpoint toolkit.”

### Step 2 — Apply patch queue (strict order)
Apply patches from `v37_patch_queue_batch6.md`:

1. **P37.1**: insert `subsec:S5prime-phase-toolkit` after `rem:s5-forceability-gate`.
2. **P37.2**: insert FORCE’s `\widetilde D_B(W)` definition + forcing lemma + gate remark.
3. **P37.3**: insert ABSORB’s `thm:S5prime-closure` + acceptance gate remark after `thm:S5-budget`.
4. **P37.4** (optional but recommended): add 1-page S6 harness appendix.

### Step 3 — Add an explicit “Missing Lever” box (required)
Near the start of Section `sec:S5-frontier`, insert a boxed OPEN statement:

- Title: “OPEN (Missing Lever): budget-eligible phase endpoint”
- Content: must explicitly require:
  - forceability (domination or new forcing lemma),
  - UE inequality with p ≥ 1/2,
  - local bound with θ ≤ p − 1/2 (ideally θ=0),
  - δ-uniformity for all 0<δ≤δ0(m,α),
  - and must state that raw Δarg endpoints are NO–GO.

### Step 4 — Repro pack schema update (fail-closed)
Update the repro pack JSON schema and/or metadata tables to include:

- endpoint family string,
- forcing target (DB vs Dtilde),
- budget tuple (p,θ,q) + growth model fields,
- a boolean flag `missing_lever_open` (must be true in v37).

### Step 5 — Compile / cross-reference audit
- Compile `manuscript_v37.tex` → PDF.
- Ensure all references resolve and no duplicate labels were introduced.

### Step 6 — Produce v37 lock artifacts
On successful compile + audit, output:

- `manuscript_v37.tex`
- `manuscript_v37.pdf`
- `v37_patchlog.md` (diff narrative relative to v36)
- `v37_repro_pack.zip` (updated format)
- `integration_notes_v37.md` (post-build)
- `CR_master_dashboard_v37_locked.md`
- `v37_next_build_plan_diff.md` (diff-only forward plan after v37 lock)

---

## 2) Hard NO–GO conditions (build must be rejected)

1. **Notation bug:** any phase endpoint is written as `\int \Im(f'/f)\,dv` instead of `\Im\int (f'/f)\,dv`.
2. **Unstated hypotheses:** phase increment used without explicit collar nonvanishing.
3. **Drift:** any text implies RH is proved or S5′ is closed without an explicit endpoint satisfying the acceptance gate.
4. **Endpoint regressions:** point evaluation / absolute \(L^r\) endpoints re-enter S5 without being labeled NO–GO.
5. **Schema looseness:** repro pack permits missing endpoint metadata (must fail closed).

---

## 3) Lock criteria (what “v37 locked” means)

v37 is locked only if:

- All Batch‑6 phase toolkit lemmas and the \(\widetilde D_B\) forcing lemma are in-text, proof-grade.
- S5′ acceptance gate is in-text and rejects dead endpoint classes explicitly.
- The Missing Lever is boxed as OPEN and no alternative closure narrative is implied.
- Repro pack schema is updated and fail-closed.

---

## 4) Post-lock branch prompts (Batch 7 preview)

Once v37 is locked, all branches should be re-tasked to attack the Missing Lever:

- design a cancellation/less-singular endpoint with (p,θ,q) budget-eligible,
- or prove a new NO–GO that eliminates a tempting endpoint class,
- or supply a micro-window clustering bound strong enough to reduce the local term.

