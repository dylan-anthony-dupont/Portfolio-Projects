# RH-CR Master Dashboard — v35 LOCKED (one-page)

Locked: 2026-01-23  
Primary frontier: **S5 (non-pointwise UE redesign)**  
Audit scaffold: **S2-style certified criterion/harness** (per-height tail-check + finite-height front-end certificate)  
Retired route: **S1/S1′ pointwise η-absorption** (now formally NO-GO; recorded in Appendix)

---

## (1) Posture + non-negotiables

### What v35 now proves (drift locks)
- **ENT hygiene:** working function is entire \(\Xi_2(u)=\xi(u/2)\); \(E(v)=\Xi_2(1+v)\).
- **Exponent budget:** uniform η-shrinking under \(\delta_0=\eta\alpha/(\log m)^2\) requires **\(p-\theta\ge 1/2\)**.
- **UE endpoint NO-GO:** with pointwise/sup endpoint \(\sup_{\partial B}|E'/E|\), **no \(p>1\)** is possible (shape-only constants).
- **Forcing NO-GO:** single-box forcing is **O(1)** in height (cannot grow like \(\log m\)).
- **Bridge NO-CONVERSE:** \(|W|=1\) on \(\partial B\) does **not** imply interior zero-freeness/constancy.

### What v35 does *not* claim
- No uniform tail closure.  
- No claim of RH from current UE architecture.

---

## (2) Ranked blocker queue (now the real frontier)

1. **S5–UE (CRITICAL):** design a forceable non-pointwise endpoint \(\Phi_B\) and prove a UE-type inequality  
   \(D_B(W)\le C\,\delta^{p}\,\Phi_B\) with effective gain meeting the budget (\(p-\theta>1/2\)).  
2. **S5–LOC (CRITICAL):** new local/collar interface in the same endpoint class (avoid pointwise \(\delta^{-1}\) blow-up).  
3. **S5–FORCE (HIGH):** either \(\Phi_B\ge D_B(W)\) or new forcing lemma that lower-bounds \(\Phi_B\) directly.  
4. **Residual envelope ledger (HIGH):** make Lemma residual-envelope referee-grade: cite/derive RH-free \(\zeta'/\zeta\) bound with explicit constants + parameter dependence.  
5. **Front-end certificate (MED):** keep as external input but tighten spec + provenance.

---

## (3) Live Gap Register (canonical IDs)

| Gap ID | Status v35 | Notes / where latched |
|---|---:|---|
| **G-1** constant provenance ledger | **OPEN** | residual-envelope constants + citations still need proof-grade sourcing |
| **G-2** what is bounded (W vs residual) | **MUTATED → S5** | now framed as endpoint redesign controlling dial deviation without pointwise sup |
| **G-3** K_alloc provenance | **CLOSED** | unchanged; recorded in constants + harness |
| **G-4** δ-uniformity for absorption | **CLOSED-AS-NOGO / REFRAMED** | budget theorem + UE NO-GO rule out absorption route; new work = S5 |
| **G-5** κ-admissibility interactions | **OPEN (S5-dependent)** | current κ policy safe; new endpoint may change requirements |
| **G-6** Bridge-1 hypotheses | **CLOSED (one-way)** | plus explicit “no converse” remark |
| **G-7** free-m / quantifier hygiene | **IN PROGRESS** | v35 improved; keep auditing as S5 is developed |
| **G-8** local window bound / N_loc | **CLOSED** | explicit unconditional N_loc majorant retained |
| **G-9** (reserved) | **DEFERRED** | keep slot available for S5-induced obligations |
| **G-10** placeholder elimination | **CLOSED** | v35 codifies NO-GO and removes “handwave closure” claims |
| **G-11** external computation reliance | **DEFERRED (quarantined)** | front-end remains explicit external certificate |
| **G-12** citation/verification discipline | **OPEN** | residual envelope + any future S5 endpoint must be fully sourced |

---

## (4) Minimal S5 dependency DAG (current + placeholders)

**Bridge/outer factor (closed)**  
`E (entire)` → `outer factor G_out` → `W = E/G_out`, `|W|=1 on ∂B` *(no converse)*

**Forcing (closed, constant-limited)**  
off-axis quartet ⇒ lower bound on dial deviation `D_B(W)` (constant forcing)

**S5 envelope (OPEN)**  
`D_B(W)` ≤ `δ^p * Φ_B(E)` with forceable Φ_B

**S5 residual/local interface (OPEN)**  
`Φ_B(E)` ≤ `Residual(m) + Local(m,δ)` with exponent budget gain (`p-θ > 1/2`)

**Closure**  
If S5 satisfies budget uniformly + constants/citations are closed ⇒ tail closure ⇒ RH (with front-end)

---

## (5) v35 artifact links

- `manuscript_v35.tex`, `manuscript_v35.pdf`
- `v35_repro_pack.zip` (audit harness; metadata-latched)
- `v35_patchlog.md`
- `integration_notes_v35.md`
- this dashboard: `CR_master_dashboard_v35_locked.md`
