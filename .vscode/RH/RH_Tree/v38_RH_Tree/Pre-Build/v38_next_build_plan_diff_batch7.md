# v38 next build plan (diff‑only) — Batch 7 — 2026-01-25
*(Target: v37 → v38 pre‑build artifacts; no proof‑tone drift.)*

## Build intent for v38
**v38 is a “truth‑latching narrowing build”:** close all *plumbing* gaps that are ready, and install the Batch‑7 NO‑GO filter + Missing Lever latch so only the genuine frontier remains.

---

## P38.1 — Force/end‑point alignment (close G‑2b by design)
**Goal:** make the forced object and contradiction endpoint the *same* object.

1) **Commit** throughout Section 12 / S5′ to:  
\[
\mathcal D_B(\cdot)\equiv \widetilde D_B(\cdot)
\]
as the contradiction endpoint.

2) **Insert** FORCE’s corollary immediately after Lemma 12.17:  
`cor:S5prime-force-automatic` (discharges (S5′‑FORCE) with \(c_{\rm force}=\pi/2\), \(\Xi\equiv0\)).

3) **Update references** in:
- The S5′ budget theorem statement (where (S5′‑FORCE) appears), and
- Any later “budget closure criterion” wording,
so that it is explicit that (S5′‑FORCE) is now a **proved lemma**, not a hypothesis.

**GO/NO‑GO check:** after patch, no theorem may list (S5′‑FORCE) as an assumption when \(\mathcal D_B\equiv\widetilde D_B\).

---

## P38.2 — Definition 12.11 λ‑shift hygiene (close G‑10 wording bug)
Apply FORCE’s parenthetical correction in Definition 12.11 so the distance statements are mathematically correct.

---

## P38.3 — Bridge‑1 for phase endpoints (close G‑6)
1) **Insert** BRIDGE’s collar nonvanishing lemma near the start of the phase endpoint toolkit (before local phase lemmas are invoked).  
This ensures phase increments along shifted segments / buffered boundary are branch‑safe.

2) **(Optional, but recommended)** add BRIDGE’s refined per‑zero phase bound remark (horizontal separation \(d\) gives bound \(\min\{\pi, O(\delta/d)\}\)).  
This will be referenced as motivation for the remaining frontier (pair‑isolation).

---

## P38.4 — Local phase interface (close G‑8 θ component)
1) **Replace** Lemma `lem:local_phase_delta_inert` with LOCAL’s strengthened line‑segment lemma.  
2) **Insert** corollary `cor:local_phase_on_buffered_boundary` for the actual buffered sides \(S_j\subset\partial B_{\kappa/2}\).

**GO/NO‑GO check:** local phase lemma must explicitly cover the geometry used by Definition `def:Db-tilde-phase`.

---

## P38.5 — Install Batch‑7 NO‑GO filter (reframe G‑4′)
1) **Insert** ENVELOPE’s lemma `lem:phase-UE-theta0-nogo` + proof.
2) **Insert** ENVELOPE’s consequence remark:
- endpoint‑only θ=0 per‑pole cannot yield any \(p>0\) UE gain;
- therefore \(p\ge 1/2\) UE must use extra structure defeating the one‑pole model.

**GO/NO‑GO check:** the text must clearly label this as “endpoint‑only / local analytic NO‑GO” (not “impossible for ζ”).

---

## P38.6 — Missing Lever latch (prevent silent closure)
1) **Insert** ABSORB’s “Missing Lever box (S5′)” near `thm:S5prime-closure` / `rem:S5prime-gate`.
2) **Optional sentence**: append to `rem:S5prime-gate` that `missing_lever_open=true` is the only analytic completion item.

---

## P38.7 — Repro‑pack / schema (fail‑closed continuation)
Carry forward the v37 fail‑closed rules:
- `missing_lever_open = true`
- `endpoint_family`, `forcing_target`, and declared `(p,θ,q)` tuple present

**Optional v38 latch extension:** add a boolean `phase_endpoint_only_nogo_installed=true` to the schema to prevent future drift (purely documentary).

---

## After‑build deliverables (v38)
- `manuscript_v38.tex` / `manuscript_v38.pdf`
- `v38_patchlog.md` (must cite P38.1–P38.7 edits)
- Updated `CR_master_dashboard_v38_locked.md`
- Updated repro pack (if schema latch extended)
