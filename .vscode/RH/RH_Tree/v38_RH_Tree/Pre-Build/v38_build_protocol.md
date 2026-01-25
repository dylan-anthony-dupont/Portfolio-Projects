# v38 build protocol (pre‑build) — Batch 7 — 2026-01-25

## 0) Objective
v38 is not a “new closure attempt.” It is a **truth‑latching narrowing build** that:
- closes all ready-to-close plumbing gaps (G‑2b, G‑6, G‑10, G‑8θ), and
- installs the Batch‑7 **NO‑GO filter** + Missing Lever latch so the *only* remaining frontier is explicit.

## 1) Inputs
Base: `manuscript_v37.tex` + v37 repro pack.  
Patch sources: Batch‑7 branch packets:
- FORCE: forcing↔endpoint alignment + gate
- LOCAL: strengthened local phase lemma (geometry-correct)
- ENVELOPE: endpoint‑only NO‑GO + “local isolation needed” lemma (design constraint)
- BRIDGE: collar nonvanishing lemma + optional refined kernel lemma
- ABSORB: Missing Lever box latch

## 2) Edit sequence (must be followed in order)
### Step A — Forceability alignment (P38.1)
1. Replace any ambiguous “endpoint” symbols so that **the contradiction endpoint is \(\widetilde D_B\)**.
2. Paste `cor:S5prime-force-automatic` right after Lemma 12.17.
3. Ensure the S5′ budget theorem no longer lists (S5′‑FORCE) as an assumption when \(\mathcal D_B\equiv \widetilde D_B\).
4. Paste the forceability gate remark near the frontier list.

### Step B — Geometry/label hygiene (P38.2)
Apply the one-line parenthetical correction in Definition 12.11 (λ‑shift distance).

### Step C — Bridge collar nonvanishing (P38.3)
Insert the collar nonvanishing lemma before any use of “choose a continuous branch of \(\arg\)” on shifted/buffered segments.

*(Optional)* insert BRIDGE refined kernel lemma `lem:phase_kernel_refined` if not already present; otherwise just cite it in the pair-isolation remark.

### Step D — Local lemma upgrade (P38.4)
Replace Lemma `lem:local_phase_delta_inert` with LOCAL’s strengthened line‑segment lemma and add the corollary for buffered sides.

### Step E — Install NO‑GO filter + design constraint (P38.5)
1. Insert ENVELOPE’s lemma `lem:phase-UE-theta0-nogo` + proof.
2. Insert the consequence remark.  
3. (Recommended) insert `lem:local-isolation-needed` as an explicit boxed design constraint.

### Step F — Missing Lever latch (P38.6)
Insert ABSORB’s Missing Lever box near `thm:S5prime-closure` / `rem:S5prime-gate`.  
Confirm the prose tone is strictly “OPEN / not yet proved.”

### Step G — Repro‑pack metadata (P38.7)
- Keep `missing_lever_open=true`.
- Update any schema fields listing which gaps are open/closed.
- Optionally add `phase_endpoint_only_nogo_installed=true`.

## 3) Compilation / sanity checks
**C1 (Compilation):** TeX compiles without manual edits.  
**C2 (No drift):** “OPEN (Missing Lever)” appears in PDF and is referenced at least once in the S5′ closure theorem.  
**C3 (Forceability):** forcing is *proved*, not assumed, for the endpoint actually used.  
**C4 (Bridge safety):** collar nonvanishing lemma is cited before any argument-integral on buffered segments.  
**C5 (Endpoint-only NO‑GO):** lemma and consequence remark present; no later text contradicts it.

## 4) Output artifacts to lock v38
- `manuscript_v38.tex`, `manuscript_v38.pdf`
- `v38_patchlog.md` (must enumerate P38.1–P38.7)
- `CR_master_dashboard_v38_locked.md`
- `integration_notes_v38.md` (single-page delta digest from v37)
- updated repro pack zip

## 5) Success definition for v38
Even if the Missing Lever remains open, v38 is a success iff:
- G‑2b, G‑6, G‑10, and the θ‑component of G‑8 are **closed in-text**, and
- the remaining frontier is reduced to a single explicit design statement:  
  **defeat the one‑pole NO‑GO via extra structure (pair isolation / cancellation / arithmetic)**.
