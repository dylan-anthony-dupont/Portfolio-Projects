# CR Master Dashboard — v43 pre-build (post Batch 14)

**Locked manuscript baseline:** v42 post-build (GEO‑C4 endpoint is in place).  
**Goal of this pre-build:** produce a v43 build that is *strictly simpler* than v42 by:
1) locking GEO‑C4 definitions + hygiene,  
2) freezing all NO‑GO constraints, and  
3) reducing the whole closure to **one** explicit UE statement.

---

## A. One-screen dependency map (the only chain that matters)

### Definitions (locked)
- \(E(v)\) even entire completion in the \(v\)-frame.
- Hinge circle \(C_{m,\delta}: v(\theta)=im+\delta e^{i\theta}\).
- \(\mathcal L_t(v)=E'/E(v+t)-E'/E(v-t)\).
- \(\mathcal D_{a,h}(v)=\mathcal L_{a+h}(v)-\mathcal L_{a-h}(v)\).
- \(h=\kappa\delta\), \(\delta=\eta a/(\log(m+3))^2\).
- \(\psi(\theta)=\Im(\mathcal D_{a,h}(v(\theta))v'(\theta))\).
- \(\Phi^\star=(\delta^2/h)\|P_2\psi\|_{L^2}\).

### Closure chain
1) **FORCE:** off-axis quartet at \((a,m)\) ⇒ \(\Phi^\star\ge c_0(\kappa)\).
2) **UE-REDUCE (BRIDGE):** \(\displaystyle \Phi^\star\le \frac{\delta^2}{\sqrt\pi\,h}\int_0^{2\pi}|\mathcal D_{a,h}(v(\theta))|\,d\theta\).
3) **ACTIVE (UE‑INPUT\(^{{H^1}}(\mathcal D;M)\)):** \(\displaystyle \int_0^{2\pi}|\mathcal D_{a,h}(v(\theta))|\,d\theta\le C\,h\,(\log(m+3))^{C'}/a^2\).
4) Plugging the nominal \(\delta\)-policy yields \(\Phi^\star=o(1)\), contradicting FORCE.

✅ Therefore the entire proof reduces to **one** UE statement.

---

## B. Status table (truth‑latching)

| ID | Object | Status | Notes |
|---:|---|---|---|
| GEO‑C4‑DEF | Hinge circle + \(k=2\) harmonic endpoint \(\Phi^\star\) | **LOCKED** | k=2 is the contour analogue of π/2-carrier/mod-4 projector (legacy) |
| HYGIENE | Even entire + shift‑admissibility + \(h=\kappa\delta\) | **LOCKED** | must appear before any \(E'/E\) integral |
| FORCE | Quartet ⇒ \(\Phi^\star\ge c_0(\kappa)\) | **LOCKED** | toy model exact; stability under clutter is “supported” (needs clean writeup) |
| UE‑REDUCE | \(\Phi^\star \le (\delta^2/(\sqrt\pi h))\int|\mathcal D|\) | **LOCKED** | sharp constant from Batch‑14 BRIDGE |
| NO‑GO‑δ | Any UE bound with \(h/\delta\) (or worse) is useless | **LOCKED** | compatible with the toy forcing; cannot yield \(\Phi^\star\to 0\) |
| NO‑GO‑RH | Off-axis quartet forces \(\int|\mathcal D|\gtrsim h/\delta^2\) | **LOCKED** | makes clear UE‑INPUT is RH‑strength |
| UE‑INPUT\(^{{H^1}}(\mathcal D;M)\) | \(\int|\mathcal D|\le C h(\log m)^{C'}/a^2\) | **ACTIVE** | the *only* open statement after Batch‑14 |

---

## C. What changed from post‑Batch‑13 → post‑Batch‑14 (net progress)

1) **Sharper UE reduction lemma** (BRIDGE) with correct \(\sqrt\pi\) normalization.
2) **Explicit NO‑GO latch**: FORCE already implies \(\|\mathcal D\|_{L^1}\) is large under an off-axis quartet, so UE‑INPUT is the true closure brick.
3) Hygiene constraints (ENT + admissibility) are now mandatory and should be stated once and reused.

---

## D. What v43 build must do (patch queue pointer)

v43 must:
- (P0) Insert/centralize **shift‑admissibility** definition and “\(h=\kappa\delta\)” coupling policy.
- (P0) Replace UE reduction lemma with BRIDGE TeX block.
- (P1) Insert NO‑GO remark/lemma: “FORCE ⇒ \(\|\mathcal D\|_{L^1}\gtrsim h/\delta^2\)”.
- (P1) Replace the active UE box with UE‑INPUT\(^{{H^1}}(\mathcal D;M)\).

Everything else is locked.

