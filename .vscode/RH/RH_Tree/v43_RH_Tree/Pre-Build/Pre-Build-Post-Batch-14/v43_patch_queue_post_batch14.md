# v43 patch queue — post Batch 14

This queue is **only** what must be applied in the v43 build.  
Everything else is locked.

---

## P0 (must land cleanly)

### P0.1 — Centralize GEO‑C4 hygiene + admissibility
- Add a dedicated subsection “GEO‑C4 setup: \(E\) even entire, shift‑admissible hinge circles”.
- Define \(C_{m,\delta}\), nominal \(\delta\)-policy, and coupling \(h=\kappa\delta\).
- State shift‑admissibility/buffer condition explicitly and allow shrinking \(\delta\) (with proportional \(h\)) to enforce it.

### P0.2 — Replace UE reduction lemma with BRIDGE version (sharp constants)
- Insert the TeX block:
  \[
  \|P_2\psi\|_{L^2}\le \|\psi\|_{L^2}\le \frac{1}{\sqrt\pi}\int_0^{2\pi}|\mathcal D_{a,h}(v(\theta))|\,d\theta,
  \]
  hence
  \[
  \Phi^\star \le \frac{\delta^2}{\sqrt\pi\,h}\int_0^{2\pi}|\mathcal D_{a,h}(v(\theta))|\,d\theta.
  \]

### P0.3 — Swap the active UE box (v42 → v43)
- Remove the pointwise/derivative-stack UE‑INPUT box.
- Insert **UE‑INPUT\(^{{H^1}}(\mathcal D;M)\)**:
  \[
  \int_0^{2\pi}|\mathcal D_{a,h}(v(\theta))|\,d\theta \le C\,h\,(\log(m+3))^{C'}/a^2 \quad (m\ge M).
  \]
- Add the exponent‑budget note: \(C'\le 4\) (or \(C'=4\) with small \(\eta\)).

---

## P1 (strongly recommended for truth-latching)

### P1.1 — Add NO‑GO lemma/remark: “FORCE ⇒ \(\|\mathcal D\|_{L^1}\gtrsim h/\delta^2\)”
- Place immediately after the FORCE lemma.
- Purpose: make explicit that the UE box is RH‑strength (final closure brick), not a routine estimate.

### P1.2 — Add a one-paragraph legacy translation remark (optional)
- “k=2 harmonic = π/2-carrier / mod‑4 projector analogue”.
- Strictly expository, not used in the proof.

---

## P2 (only if time permits)

### P2.1 — FORCE stability under clutter (clean writeup)
- Keep the toy forcing exact, then state a robust version under a separation/buffer condition.
- Ensure no hidden “one zero per height” assumption.

---

## Stop condition
Do **not** introduce any new endpoint, any new geometry family, or any new global bridge in v43.  
The only open brick must remain UE‑INPUT\(^{{H^1}}(\mathcal D;M)\).

