# v41 Build Protocol (PRE‑BUILD)

Purpose: produce v41 as a **truth‑latching geometry pivot** build (v40 → v41) with zero drift.

**Inputs:**
- v40 manuscript: `manuscript_v40.tex`
- This patch queue: `v41_patch_queue_prebuild.md`
- Integration notes: `integration_notes_v41_prebuild.md`

---

## Step 0 — Guardrails (do not violate)

- Do **not** remove v40 NO‑GO lemmas. v41 only narrows their scope (if needed) and adds NG‑Δa‑A.
- Keep exactly **one** boxed open statement at the end of the S5 frontier (Box `box:geometry-change-v41`).
- Do not claim RH; v41 is a prebuild whose job is to **correct the frontier** and prevent future drift.

---

## Step 1 — Hygiene fix

Apply Patch 1: correct the displayed expansion of `\mathcal D_{a,h}` so it matches its defining equation.

**Check:** compile / scan that all occurrences of `\mathcal D_{a,h}` are consistent with
`\mathcal L_{a+h}-\mathcal L_{a-h}`.

---

## Step 2 — Insert NG‑Δa‑A lemma

Apply Patch 2.

**Proof audit checklist:**
- Uses only: quartet toy model + mean value theorem style bound (no hidden RH assumptions).
- Concludes: aligned boxes cannot support the v40 forcing clause (absolute `c0`) at nominal `h=δ`.
- Explicitly references Box `box:missing-lever-v40` bullet (1) so the contradiction is visible.

---

## Step 3 — Replace the active frontier box

Apply Patch 3.

**Check:**
- `box:missing-lever-v40` is removed or marked “superseded.”
- `box:geometry-change-v41` is the only OPEN box.
- The box explicitly records NG‑Δa‑A and lists the three criteria (forceability/UE/resonance) as the new open frontier.

---

## Step 4 — NO‑GO scope remark

Apply Patch 4.

**Check:** ensure this remark does not weaken any NO‑GO lemma; it only prevents over‑interpretation.

---

## Step 5 — Discarded routes appendix

Apply Patch 5.

**Check:** the appendix entry is short, factual, and points to the new lemma + new GEO box.

---

## Step 6 — Compile and mechanical checks

- Recompile PDF; confirm:
  - no broken references to the old box label,
  - lemma numbering is consistent,
  - no duplicated labels.

---

## Step 7 — Update reproducibility metadata (if needed)

v41 is proof-spine only; no new numerical certificates required.
If you edit any file list / README, regenerate `SHA256SUMS.txt`; otherwise keep v40 repro pack unchanged and rename to v41.

---

## Step 8 — Post-build artifacts checklist

When v41 build is executed, produce:
- `manuscript_v41.tex`, `manuscript_v41.pdf`
- `v41_patchlog.md`
- `integration_notes_v41.md` (delta digest)
- `CR_master_dashboard_v41_locked.md`
- `v41_next_build_plan_diff.md` (v41→next)

