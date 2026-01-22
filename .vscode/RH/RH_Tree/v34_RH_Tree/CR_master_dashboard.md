# CR Master Dashboard (v34 locked)

Date: 2026-01-22  
Primary spine: **S4 (criterion-first + UE–Gate diagnostics)** — **CONDITIONAL**  
Audit harness: **v34_repro_pack/** — exponent-tracking + tail-inequality evaluator

## Snapshot

- **v34 is built**: `manuscript_v34.tex` / `manuscript_v34.pdf` + `v34_repro_pack.zip`.
- **Batch‑3 UE–Gate audit merged** (dominant change):
  - **G‑2 RESOLVED (negative for absorption):** Lemma `upper-envelope` supports **δ¹** (not δ^{3/2}).  
    This removes η‑absorption tail closure under the current collar/local-window mechanism.
  - New **UE–Gate remark + obstruction lemma** added to prevent silent reintroduction of exponent drift.
- **Batch‑2 residual envelope upgrade merged (proof-sketch level):**
  - Lemma `residual-envelope` rewritten as **δ‑uniform** with explicit dependency control and a clear “constant gate”.
- **Tail posture changed:**
  - v33’s **one‑height reduction + η‑absorption closure** removed.
  - Replaced by a **tail criterion family** (Theorem `tail-inequality`) + a **criterion-first global theorem**.

## Blocker queue (ranked)

1) **CRITICAL — UE–Gate redesign (formerly G‑4/G‑5 frontier)**  
   Need an analytic mechanism that yields an effective exponent **p>1** against the *local* term  
   (or redesigns the envelope endpoint to avoid the sup-based collar blow-up).  
   Without this, uniform tail closure is not obtained from η‑shrinking.

2) **CRITICAL — G‑1 / G‑12 (Residual envelope constant provenance)**  
   v34 contains a δ‑uniform proof sketch, but it still imports a standard RH‑free bound for `ζ'/ζ`
   with local-zero subtraction; this must be fully proved in-text or cited in a referee-acceptable way.

3) **HIGH — G‑4 (δ‑uniformity obligations, globally)**  
   Ensure every constant used in the tail inequality is δ‑independent and does not smuggle RH‑equivalents.

4) **MED/HIGH — G‑11 (front‑end dependence)**  
   External finite-height verification remains an input; acceptable for a conditional theorem, but must be clearly labeled.

5) **MED — G‑7 / G‑10 (global hygiene)**  
   Cross-reference integrity, quantifier hygiene, and removal of legacy “proof by proxying”.

## Live status board (G‑1…G‑12)

| Gap ID | Name | Status (v34) | Notes |
|---|---|---:|---|
| G‑1 | Residual envelope constant chain | **IN PROGRESS** | δ‑uniform proof sketch added; still needs fully certifiable source/proof for (⋆) |
| G‑2 | W‑control chain alignment / δ‑exponents | **CLOSED** | Exponent mismatch fixed; p=1 pointwise UE recorded as gate |
| G‑3 | K_alloc provenance | **CLOSED** | Carried from v33 |
| G‑4 | δ‑uniformity for tail criterion | **IN PROGRESS** | Must ensure *all* constants are δ‑independent and RH‑free |
| G‑5 | κ‑admissibility / collar interface | **IN PROGRESS** | δ‑shrink safety proved; interface still blocks absorption under p=1 |
| G‑6 | Bridge‑1 hypotheses | **CLOSED** | Carried from v33 |
| G‑7 | Free‑m / quantifier hygiene | **OPEN** | Needs a global hygiene pass |
| G‑8 | Local zero term bounds | **CLOSED** | Explicit bound inserted in v33, retained |
| G‑9 | Citation / external dependency labeling | **IN PROGRESS** | Residual bound (⋆) needs citation/proof; front-end labeled |
| G‑10 | Placeholder elimination / labeling integrity | **IN PROGRESS** | Continue hunting legacy “proof sketch” placeholders |
| G‑11 | External computation reliance | **DEFERRED** | Conditional statement acceptable; internal replacement optional |
| G‑12 | Constant provenance discipline | **OPEN** | Ledger needs proof/citations + audit trails |

## Minimal dependency DAG (v34 canonical)

(Dirichlet outer factor) → (Bridge‑1 collapse when zero‑free)  
→ (Upper‑envelope lemma, pointwise p=1)  
→ (Log‑derivative split: E'/E = F'/F + Z_loc'/Z_loc)  
→ (Residual envelope bound on F'/F) + (κ‑collar bound on Z_loc'/Z_loc)  
→ (Explicit dial deviation bound)  
→ (Forcing lemma lower bound on phase jump)  
→ (Tail criterion: deviation < forcing contradiction, at each m)  
→ (Front‑end verified band) + (Tail criterion family for all m≥10) ⇒ RH (conditional)
