# CR Master Dashboard — v42 pre-build (pre–Batch 12)
*(One-page control-room view: status board + blocker queue + DAG.)*

**Current locked manuscript:** v41  
**Next target:** v42 (pre-build, before Batch 12) — install GEO‑C4 as canonical endpoint; isolate the single UE brick.

---

## A) Canonical posture
**Primary closure spine (now):** **GEO‑C4 harmonic endpoint closure** (hinge‑circle + \(k=2\) projection).  
**Interpretive harness:** S6 explicit-formula “amplitude leak” mapping (cross-check only).

**One-line objective:** Replace sidewise/pointwise UE with orthogonal harmonic extraction so that δ‑shrink produces an unconditional contradiction.

---

## B) Minimal dependency DAG (Schematic)
1. **Setup:** completed even entire \(E(v)\), \(F=E'/E\), quartet symmetry.  
2. **Operators:** \(\mathcal L_t(v)=F(v+t)-F(v-t)\), \(\mathcal D_{a,h}=\mathcal L_{a+h}-\mathcal L_{a-h}\).  
3. **Geometry:** hinge‑circle \(C_{m,\delta}: v=i m+\delta e^{i\theta}\) + coupling \(h=\kappa\delta\).  
4. **Endpoint:** \(\psi(\theta)=\Im(\mathcal D_{a,h}(v(\theta)))\), \(\Phi^*=\frac{\delta^2}{h}\|P_2\psi\|_{L^2}\).  
5. **FORCE:** off‑axis quartet ⇒ forced \(k=2\) harmonic ⇒ \(\Phi^*\ge c_0\).  
6. **UE:** UE‑INPUT field bound ⇒ IBP ⇒ \(\Phi^*\le o(1)\) under δ‑policy.  
7. **Contradiction:** \(c_0 \le \Phi^* \le o(1)\) ⇒ no off‑axis quartets ⇒ RH.

**If any of (5)–(6) fails, closure stalls.**

---

## C) Blocker queue (ranked)
### CRITICAL
**B1 — UE‑INPUT (ACTIVE BRICK):** prove explicit bounds for  
\(\sup_{t\in[a-h,a+h]}\sup_{\theta}\big|\partial_t\partial_v^j\mathcal L_t(v(\theta))\big|\) (j=0,1,2)  
on shift‑admissible hinge circles, with \(a\)-power decay and polylog(m) loss only.

**B2 — FORCE robustness:** show forced quartet contribution to \(P_2\psi\) cannot be cancelled below \(c_0\) by remainder terms (other zeros + archimedean), under explicit isolation/separation or controllable remainder hypotheses.

**B3 — Shift‑admissibility protocol:** a clean δ‑shrink / buffer lemma ensuring all shifted traces avoid zeros, stated non‑circularly.

### HIGH
**B4 — Resonance bookkeeping:** quantify how multiple tilts at same height affect \(P_2\psi\); specify an “N_eff” control condition sufficient for FORCE robustness + UE.

**B5 — NO‑GO sanity audit:** re-check v40–v41 NO‑GO archive for any statement that *incorrectly forbids* harmonic/projection endpoints, circular witnesses, or \(h\asymp\delta\) coupling.

---

## D) Gap/status board (v42 pre-build)
| Item | Meaning | Status | Notes |
|---|---|---:|---|
| GEO‑C1 | Hinge‑centered witness (circle) | LOCKED | Canonical geometry |
| GEO‑C2 | Coupling \(h=\kappa\delta\) | LOCKED | No micro‑coupling |
| GEO‑C3 | Non‑pointwise endpoint | LOCKED | via \(L^2\) projection |
| GEO‑C4 | Trig contour + harmonic extraction | LOCKED | \(k=2\) projection |
| FORCE‑toy | constant forcing in toy quartet | LOCKED | exact computation |
| FORCE‑robust | forcing survives remainders | OPEN | B2 |
| UE‑INPUT | derivative/field bounds | OPEN | B1 |
| SHIFT‑ADMISS | avoid poles on shifted traces | OPEN | B3 |
| Resonance (multi‑quartet) | N_eff control | OPEN | B4 |
| S6 map | amplitude leak interpretation | LOCKED | cross-check only |

---

## E) Work orders for Batch 12 (who should close what)
*(Prompts will be engineered in part 1e, but these are the target payloads.)*

- **RH‑ENVELOPE:** close **B1 UE‑INPUT** with explicit constants (digamma/Gamma + zero-sum control on shifted hinge circles; bounds for \(j=0,1,2\)).
- **RH‑BRIDGE:** close **B3 SHIFT‑ADMISS** (buffer construction on circle + shifted traces; δ‑shrink lemma; noncircular).
- **RH‑FORCE:** close **B2 FORCE‑robust** (dominance of forced \(k=2\) harmonic; remainder bound via separation/local count).
- **RH‑LOCAL:** close **B4 Resonance/N_eff** (multi‑quartet scenario; prevent cancellation; or provide conditions under which it cannot sabotage forcing).
- **RH‑ABSORB:** integrate GEO‑C4 into global manuscript spine; verify δ‑policy compatibility; ensure no absorption/tail stage reintroduces pointwise UE.

---

## F) “What is the Missing Lever now?”
**Answer:** a *provable*, *δ‑aware*, *shift‑admissible* **UE‑INPUT field bound** for \(\mathcal L_t\) (and thus \(\mathcal D_{a,h}\)) on hinge‑centered circles, plus a robustness lemma that the forced \(k=2\) harmonic cannot be canceled by the remainder.  

That is the boxed frontier. Everything else is scaffolding.
