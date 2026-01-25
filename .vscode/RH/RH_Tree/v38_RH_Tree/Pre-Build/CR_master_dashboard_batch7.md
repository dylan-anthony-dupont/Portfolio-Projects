# CR master dashboard — Batch 7 (post v37 locked) — 2026-01-25

## Posture (unchanged, now sharpened)
- **Primary spine:** **S5′** (phase / winding endpoint redesign) — **CONDITIONAL**.
- **Audit harness:** legacy D1 tail check (expected FAIL; kept for drift detection).
- **Interpretation harness:** S6 explicit‑formula translation (appendix only; no logical dependencies).

## Batch‑7 headline: “Missing Lever” search space is now sharply narrowed
- **FORCE side:** forcing attaches cleanly to the buffered phase endpoint \(\widetilde D_B(W)\) (π/2 lemma already in v37; Batch‑7 supplies a corollary to discharge the budget theorem hypothesis once we commit to \(\mathcal D_B\equiv \widetilde D_B\)).  
- **LOCAL side:** local phase bound in the *actual buffered boundary geometry* is proof‑grade with **θ=0** (δ‑inert per zero), but still has **q≈1** unless we prove clustering / pair‑isolation.  
- **ENVELOPE side:** decisive **NO‑GO filter**: endpoint‑only “θ=0 per pole” designs cannot yield any \(\delta^p\) UE gain with \(p>0\) via purely local analytic arguments (single‑pole obstruction).  
  ⇒ Any viable UE mechanism must incorporate **additional structure** (pair‑isolation/cancellation, forcing redesign, or arithmetic exclusions of the one‑pole model).

## Ranked blocker queue (v37 → v38)
1. **G‑4′ (PHASE‑CLASS UE / ENVELOPE):** still **OPEN**. Now explicitly constrained by the single‑pole NO‑GO.
2. **G‑8 (LOCAL MICRO‑WINDOW / PAIR‑ISOLATION):** **OPEN (q‑reduction component)**. θ‑component is now CLOSED‑READY (Batch‑7 LOCAL).
3. **G‑2b (FORCING ↔ ENDPOINT ALIGNMENT, S5′):** **CLOSE‑READY** once tail/budget is rewritten to target \(\widetilde D_B\) (Batch‑7 FORCE corollary).
4. **G‑6 (BRIDGE‑1 for phase endpoints):** **CLOSE‑READY** (collar nonvanishing hypotheses + shifted‑segment parenthetical fix).
5. **S6 (optional harness):** keep interpretive only (no new logical dependencies).

## Minimal S5′ dependency DAG (v37 + batch‑7)
**Bridge / collar nonvanishing (G‑6)**  
→ outer factor regularity on buffered contour  
→ define \(W := E/G_{\rm out}\) and the forced endpoint \(\widetilde D_B(W)\)  
→ **Forcing**: interior zero ⇒ \(\widetilde D_B(W)\ge \pi/2\) (Lemma 12.17)  
→ **Envelope (Missing Lever)**: \(\widetilde D_B(W)\le C\,\delta^p(\mathrm{Res}+\text{local})\) with \(p\ge 1/2\) and δ‑uniform constants (**G‑4′**)  
→ **Local interface**: θ=0, growth model \(G(n,\kappa)\) and effective count \(N_{\rm eff}\) (**G‑8**)  
→ **Budget closure**: Theorem `thm:S5prime-closure`  
→ contradiction ⇒ no off‑axis quartet ⇒ RH (with front‑end certificate).

## Gap status board (G‑1 … G‑12) — delta view
| Gap ID | Status after Batch‑7 ingestion | Notes |
|---|---|---|
| **G‑2b** Forced object alignment (S5′) | **IN PROGRESS → CLOSE‑READY** | Apply FORCE corollary + set \(\mathcal D_B\equiv \widetilde D_B\). |
| **G‑4′** δ‑uniform phase envelope (S5′) | **OPEN (now NO‑GO‑filtered)** | UE must defeat single‑pole model; endpoint‑only proofs ruled out. |
| **G‑6** Bridge‑1 hypotheses (phase endpoints) | **IN PROGRESS → CLOSE‑READY** | Insert collar nonvanishing lemma + shifted‑segment parenthetical fix. |
| **G‑8** Local window growth | **PARTIAL** | θ=0 lemma is PASS (CLOSE‑READY); q‑reduction still open. |
| **G‑10** Label / wording integrity | **CLOSE‑READY** | Parenthetical fix in Definition 12.11. |
| *(all other G‑IDs)* | **No change from v37 dashboard** | Remain CLOSED / DEPRECATED as in v37. |

## v38 “no drift” latch (must persist)
- Keep `missing_lever_open = true` in‑text **and** in repro‑pack schema until G‑4′ and the decisive LOCAL redesign item are actually proved.
