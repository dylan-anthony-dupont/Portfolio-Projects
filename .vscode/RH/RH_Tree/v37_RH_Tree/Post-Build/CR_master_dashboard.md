# CR master dashboard — v37 LOCKED (2026-01-25)

## Posture
- **Primary spine:** **S5′** (phase/winding endpoint redesign). v37 installs the *phase endpoint toolkit* + *π/2 forcing lemma*.
- **Audit harness:** legacy D1 tail check (low-anchor, expected FAIL; kept for honesty + drift detection).
- **Interpretation harness:** S6 explicit-formula translation (appendix only; no logical dependencies).

## Ranked blocker queue (v37 → v38)
1. **G-2b (FORCING ↔ ENDPOINT ALIGNMENT, S5′):** either rewrite tail inequality to target `\widetilde D_B(W)` (forced by Lemma `lem:phase-forcing-argprinciple`) **or** prove a transfer inequality `\widetilde D_B(W) ↔ D_B(W)`.  
2. **G-4′ (PHASE-CLASS UE / ENVELOPE):** prove an upper-envelope inequality in the **phase** class with **p ≥ 1/2** and δ-uniform constants (must not collapse to absolute `L^r` endpoints).  
3. **G-8 (LOCAL MICRO-WINDOW):** reduce effective local growth `q` (micro-window clustering or pair-isolation) so budget `2(p−θ) ≥ q` becomes feasible.  
4. **G-6 (BRIDGE-1 for phase endpoints):** precise nonvanishing neighborhoods + outer-factor regularity along *shifted segments* and *buffered contours*.  
5. **S6 (optional harness):** if any S5′ endpoint corresponds to an explicit-formula amplitude leak, state it cleanly (interpretation only).

## Minimal S5′ dependency DAG (v37)
**Outer factor / regularity**  
→ `W := E / G_out` well-defined on admissible boxes (**Bridge-1 / G-6**)  
→ **Forcing:** interior zero ⇒ `\widetilde D_B(W) ≥ π/2` (**Lemma `lem:phase-forcing-argprinciple`**)  
→ **Envelope:** `\widetilde D_B(W) ≤ C δ^p (Res + local)` with *phase-class split* (**G-4′**)  
→ **Local control:** phase is δ-inert per zero; need `q` small enough (**G-8**)  
→ **Budget closure:** apply Theorem `thm:S5prime-closure`  
→ contradiction ⇒ no off-axis quartet ⇒ RH with front-end.

## Gap status board (G-1 … G-12)
| Gap ID | Status (v37) | Notes |
|---|---|---|
| **G-1** Constant ledger | **CLOSED** | v35+ pinned `C_up, C1, C2, C_h''`; no hidden reuse. |
| **G-2a** W-control chain (legacy D_B) | **CLOSED** | v35+ forbids residual proxying; W-control alignment OK. |
| **G-2b** Forced object alignment (S5′) | **OPEN** | New: forcing targets `\widetilde D_B(W)`; tail/envelope still targets `D_B(W)` unless rewritten/transfer proved. |
| **G-3** K_alloc provenance | **CLOSED** | Locked earlier (FORCE). |
| **G-4** δ-uniform absorption (old S4) | **DEPRECATED** | v35 demoted absorption closure routes. |
| **G-4′** δ-uniform phase envelope (S5′) | **OPEN** | Need phase-class UE with `p ≥ 1/2` and uniform constants. |
| **G-5** κ-admissibility / shrink policy | **CLOSED** | v35+ monotone-safe; reused by S5′ tooling. |
| **G-6** Bridge-1 hypotheses | **IN PROGRESS** | Must be sharpened for phase endpoints (shifted segments + buffered contour). |
| **G-7** Free-m hygiene | **CLOSED** | v35 fixed. |
| **G-8** Local window growth | **OPEN** | Need micro-window clustering or pair-isolation to reduce `q`. |
| **G-9** External computation reliance | **CLOSED** | Front-end pinned as explicit assumption/certificate. |
| **G-10** Label / placeholder hygiene | **CLOSED** | v35+ “NO-GO constraints codified in-text.” |
| **G-11** Verified band/front-end | **CLOSED** | Certificate pinned. |
| **G-12** Provenance discipline | **CLOSED** | No silent constant drift. |

## v37 “no drift” latch (hard rule)
`missing_lever_open = true` is enforced both **in-text** (OPEN box in Section 12) and **in repro pack schema** (fail-closed verifier).
