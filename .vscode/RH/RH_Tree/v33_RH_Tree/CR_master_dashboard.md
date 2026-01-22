# CR Master Dashboard (v33 locked)

Date: 2026-01-21  
Primary spine: **S1 (v33 post‑pivot + η‑absorption)** — **CONDITIONAL**  
Secondary harness: **S2 (v30/v31 certified criterion)** — maintained as audit/test scaffold

## Snapshot

- **v33 is built**: `manuscript_v33.tex` / `manuscript_v33.pdf` + rebuilt `v33_repro_pack/`.
- **Batch‑1 merges completed at manuscript level**:
  - **G‑3 CLOSED**: `K_alloc` restored to `3+8√3` throughout tail inequality and absorption.
  - **G‑6 CLOSED**: Bridge‑1 rewritten via Dirichlet outer factor + Dirichlet uniqueness (no boundary ambiguity).
  - **G‑8 CLOSED**: explicit local window bound `N_loc(m) ≤ 1.01 log m + 17` for `m≥10`.
  - **G‑4/G‑5 PARTIAL**: δ0 vs δ separation + admissibility‑shrink lemma + δ‑shrink monotonicity lemma inserted.
- **Still conditional** because the **analytic constant ledger** is not yet independently certified.

## Blocker queue (ranked)

1) **CRITICAL — G‑1 (Residual envelope proof)**  
   Need a complete unconditional derivation of Lemma `residual-envelope` with explicit constant provenance.

2) **CRITICAL — G‑4 (δ‑uniformity obligations)**  
   Show `C1,C2,C_up,C_h''` (and any hidden constants) are δ‑independent and do not smuggle RH‑equivalents.

3) **HIGH — G‑2 (W‑control chain alignment / δ‑exponents)**  
   Upper‑envelope scaling + dial‑deviation bounds must be audited end‑to‑end (no “proxying”, no exponent drift).

4) **HIGH — G‑5 (κ‑admissibility interactions)**  
   Now partially formalized; remaining task is to ensure κ‑policy is compatible with every bound used in the spine.

5) **MED/HIGH — G‑11 (front‑end dependence)**  
   External finite‑height verification remains an input; acceptable for conditional theorem, but must be labeled.

## Live status board (G‑1…G‑12)

| Gap ID | Name | Status (v33) | Notes / owner |
|---|---|---:|---|
| G‑1 | Residual envelope constant chain | **OPEN** | Needs full proof (RH‑ENVELOPE) |
| G‑2 | W‑control chain alignment | **OPEN** | Scaling audit + interface (CR + RH‑ENVELOPE) |
| G‑3 | K_alloc provenance | **CLOSED** | Restored in v33 |
| G‑4 | δ‑uniformity for absorption | **IN PROGRESS** | δ‑shrink monotonicity added; still need δ‑independent constants |
| G‑5 | κ‑admissibility / shrink policy | **IN PROGRESS** | Existence lemma added; still need compatibility proof across spine |
| G‑6 | Bridge‑1 hypotheses | **CLOSED** | Dirichlet outer factor + uniqueness collapse in v33 |
| G‑7 | Free‑m / quantifier hygiene | **OPEN** | Needs global hygiene pass (CR) |
| G‑8 | Local zero term bounds | **CLOSED** | Explicit bound inserted in v33 |
| G‑9 | Citation / external dependency labeling | **IN PROGRESS** | v33 labels front‑end; continue |
| G‑10 | Placeholder elimination / labeling integrity | **IN PROGRESS** | One broken ref fixed; keep hunting |
| G‑11 | External computation reliance | **DEFERRED** | Conditional statement acceptable; internal replacement optional |
| G‑12 | Constant provenance discipline | **OPEN** | Audit ledger + provenance proofs (CR + RH‑ENVELOPE) |

## Minimal S1 dependency DAG (current canonical)

(Dirichlet outer factor) → (Bridge‑1 collapse when zero‑free)  
→ (Upper‑envelope lemma: boundary log‑derivative controls |W(v±)-e^{iφ±}|)  
→ (Log‑derivative split: E'/E = F'/F + Z_loc'/Z_loc)  
→ (Residual envelope bound on F'/F) + (κ‑collar bound on Z_loc'/Z_loc)  
→ (Explicit dial deviation bound)  
→ (Forcing lemma lower bound on phase jump)  
→ (Tail inequality: deviation < forcing contradiction)  
→ (η‑absorption + one‑height reduction)  
→ (Tail quartet exclusion for m≥10)  
→ (Front‑end verified band for m≤10) ⇒ RH (conditional on front‑end)

