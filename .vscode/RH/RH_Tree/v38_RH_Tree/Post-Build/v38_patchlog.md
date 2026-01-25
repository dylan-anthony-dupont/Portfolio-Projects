# v38 patchlog (relative to v37)

**Build date:** 2026-01-25  
**Build intent:** *truth‑latching / drift‑preventing* narrowing build focused on the S5′ frontier (“Missing Lever”), with explicit NO‑GO constraints installed in‑text and schema‑latched in the repro pack.

---

## A. Manuscript deltas (proof‑spine significant)

### PQ38.1 — Forcing assumption discharge for the buffered phase endpoint
- Added **Corollary `cor:S5prime-force-automatic`**: when the contradiction endpoint is the buffered phase endpoint `\widetilde D_B` (Def. `def:Db-tilde-phase`), the S5′ forcing hypothesis can be taken with **`c_force=\pi/2`** and **`\Xi\equiv 0`**, by Lemma `lem:phase-forcing-argprinciple`.

### PQ38.2 — λ‑shift hygiene (Definition `def:Iplus_lambda`)
- Tightened the parenthetical geometry statement to clarify:
  - separation from the unshifted vertical line `I_+` is **`\lambda\delta`**
  - distance to the box boundary is at least **`(1-\lambda)\delta`**.

### PQ38.4 — Local phase δ‑inertness generalized
- Replaced Lemma `lem:local_phase_delta_inert` with the **segment‑general** argument‑increment bound:
  `|Im \int_S (v-\rho)^{-1} dv| \le \pi`, hence `|\Delta_S \arg Z_{loc}| \le \pi N_{loc}(m)` for any segment `S` avoiding zeros.

### PQ38.5 — Collar safety + refined per‑zero phase bound
- Added:
  - **Lemma `lem:phase_collar_nonvanishing`**: κ‑admissibility on `\partial B` implies a **nonvanishing collar** on `\partial B_{\kappa/2}`.
  - **Corollary `cor:local_phase_on_buffered_boundary`**: local factor phase on each buffered side satisfies `\le \pi N_{loc}(m)`.
  - **Lemma `lem:phase_kernel_refined`**: refined bound `\min\{\pi, |S|/d\}` based on horizontal separation.

### PQ38.7–PQ38.9 — Endpoint‑only NO‑GO installed + “local isolation” obligation
- Added:
  - **Lemma `lem:phase-UE-theta0-nogo`**: any endpoint class with **θ=0 per pole** (δ‑inert on `1/(v-\rho)`) cannot yield **any `p>0`** UE gain for `\widetilde D_B`.
  - Consequence remark: forces S5′ to defeat the **one‑pole model** (pair‑isolation/cancellation or truly new UE mechanism).
  - **Lemma `lem:local-isolation-needed`**: explicit structural obligation template for beating the one‑pole obstruction.

### PQ38.10 — Missing Lever box rewritten (hard latch)
- Replaced the Section‑12 OPEN box with a **non‑silent latch**:
  - FORCE is proved (`\widetilde D_B \ge \pi/2` under an interior zero),
  - ENVELOPE is missing (phase‑class UE+split must be proven),
  - budget gate (`2p\ge 1`, `2(p-\theta)\ge q`, `p-\theta>0`) is non‑negotiable,
  - local redesign options enumerated,
  - explicit **NO CLAIM POLICY** until ENVELOPE + decisive LOCAL redesign exist.

---

## B. Repro pack deltas (v38 format)

- Created **`v38_repro_pack.zip`** by version‑bumping the v37 pack:
  - directory renamed to `v38_repro_pack/`
  - all filenames version‑bumped `v37_* → v38_*`
  - verifier scripts updated to enforce:
    - `missing_lever_open == true`
    - `phase_endpoint_only_nogo_installed == true` (**new in v38**)
- Updated checksums (`SHA256SUMS.txt`) to match.

**Note:** The “D1 tail check” remains an **audit harness** (expected FAIL); it is retained to prevent narrative drift and to keep certificate logic honest.

---

## C. What v38 explicitly does *not* do
- Does **not** claim tail closure.
- Does **not** claim RH.
- Does **not** claim any phase‑class UE exponent `p>0` beyond the open S5′ frontier.
