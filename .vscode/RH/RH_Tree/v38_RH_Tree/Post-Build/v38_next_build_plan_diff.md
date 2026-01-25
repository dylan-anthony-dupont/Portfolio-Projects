# v38 → next build plan (diff‑only)

**Scope:** This is a forward plan from locked v38. It is *diff‑only* (what changes in the next build), and is designed to preserve the v38 “line in the sand” (no drift).

---

## 0) Non‑negotiables carried forward (no drift)

- The Section‑12 OPEN box (“Missing Lever”) remains **non‑silent**:
  - FORCE is proved,
  - ENVELOPE is missing,
  - the budget gate is mandatory,
  - **no RH claim** until ENVELOPE + decisive LOCAL redesign exist.
- Repro pack must remain **fail‑closed** with:
  - `missing_lever_open = true`
  - `phase_endpoint_only_nogo_installed = true`

---

## 1) Primary target (must move): close G‑4′ (Missing Lever)

### 1.1 Deliverable A — Phase‑class ENVELOPE inequality in the endpoint class `\widetilde D_B`
Produce (or cite referee‑grade) an inequality of the form required by Theorem `thm:S5prime-closure`:

\[
\widetilde D_B(W)\ \le\ C_{\rm up}\,\delta^{p}\Bigl(\mathrm{Res}(m)+C_{\rm loc}\,\delta^{-\theta}\,G(N_{\rm eff}(m,\delta),\kappa)\Bigr),
\]

with explicit `(p,θ,q,u)` and constants independent of δ, valid for all κ‑admissible boxes at `δ≤δ0(m,α)`.

**Hard acceptance gate:**  
`2p≥1`, `2(p−θ)≥q`, `p−θ>0`.

### 1.2 Deliverable B — Defeat the one‑pole obstruction (LOCAL redesign)
v38 installed the endpoint‑only NO‑GO (Lemma `lem:phase-UE-theta0-nogo`).  
Therefore the next build must supply *structure* that invalidates the one‑pole test input.

Minimum viable options (any one is decisive):
1. **Pair isolation/cancellation:** factor `Z_loc = Z_forced · Z_rest` with endpoint‑class control on `Z_rest'/Z_rest` that is δ‑small at `δ0`.
2. **Micro‑window clustering:** prove `N_eff(m,δ0)=O(1)` (effective `q=0`).
3. **Non‑pointwise UE redesign:** a mechanism not reducible to kernelwise bounds on `(v−ρ)^{-1}`.

---

## 2) Secondary target: S6 harness (explicit formula interpretation)

For any proposed endpoint / ENVELOPE inequality, add a short “interpretation lemma”:

- Map the endpoint inequality through the s‑frame → u‑frame → v‑frame scalings.
- State explicitly whether it corresponds to an **\(x^\beta\) amplitude leak** in the explicit formula sense (β>1/2), or why not.
- If it *does* correspond to an \(x^\beta\) leak, record the implied β and the contradiction route.

This is intended as a cross‑check harness: any “new lever” must either control amplitude leaks or explain why the analogy is inapt.

---

## 3) Hygiene / documentation diffs (only if needed)

- If the next build introduces a new endpoint class `\Phi_B`, it must include:
  - a domination lemma `\Phi_B ≥ \widetilde D_B` **or**
  - a dedicated forcing lemma for `\Phi_B`
  (to satisfy Remark `rem:forceability-phase-gate`).
- Extend the “discarded routes” appendix only when a candidate lever fails *for a new reason*, not merely by restating v38 NO‑GO.

---

## 4) Repro pack diffs

- Add an optional “S5′ lever sandbox” certificate stub (metadata only) if new computational experiments are introduced.
- Preserve existing v38 latches and verifier behavior (fail‑closed).

