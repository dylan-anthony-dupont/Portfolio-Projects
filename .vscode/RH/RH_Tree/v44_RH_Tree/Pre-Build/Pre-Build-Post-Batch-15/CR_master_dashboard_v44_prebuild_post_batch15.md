# CR MASTER DASHBOARD — v44 pre‑build (post‑Batch‑15)

**Date:** 2026-01-30  
**Single active statement:** **UE‑INPUT(k=2)** (signed Fourier coefficient control)

---

## A) Locked components (do not change)

| Module | Status | Notes |
|---|---:|---|
| GEO‑C1 hinge‑centered witness \(v(\theta)=im+\delta e^{i\theta}\) | ✅ LOCKED | Canonical geometry (breaks aligned‑box NG‑Δa‑A). |
| GEO‑C2 decouple \(\delta\) and \(h\) with \(h=\kappa\delta\) | ✅ LOCKED | Keeps forced poles buffered from boundary. |
| GEO‑C3 forcing (toy model → constant lower bound) | ✅ LOCKED | Off‑axis quartet ⇒ \(\Phi^\star\ge c_0(\kappa)\). |
| Endpoint definition \(\Phi^\star=\frac{\delta^2}{h}\|P_2\psi\|_{L^2}\) | ✅ LOCKED | k=2 “π/2 carrier” endpoint. |

---

## B) UE layer (what changed in Batch‑15)

### UE‑REDUCE (v44): exact identity (LOCK)
\[
\|P_2\psi\|_{L^2}=\frac{1}{\sqrt{\pi}}\Big|\int_0^{2\pi}\psi(\theta)e^{-2i\theta}\,d\theta\Big|,
\qquad
\Phi^\star=\frac{\delta^2}{h\sqrt{\pi}}\Big|\int_0^{2\pi}\psi(\theta)e^{-2i\theta}\,d\theta\Big|.
\]

| UE item | Status | Notes |
|---|---:|---|
| UE‑REDUCE(L1) from v43 (\(\int|\mathcal D|\)) | 🟡 ARCHIVED | Phase‑loss + too strong; keep as optional remark/NO‑GO. |
| UE‑REDUCE(k=2) identity | ✅ LOCKED | Endpoint‑native; preserves sign/channel. |

---

## C) Single active box (OPEN)

### **UE‑INPUT(k=2) (v44)**
For the true completed even entire object \(E\), with  
\(\mathcal L_t(v)=E'/E(v+t)-E'/E(v-t)\), \(\mathcal D_{a,h}=\mathcal L_{a+h}-\mathcal L_{a-h}\),  
\(v(\theta)=im+\delta e^{i\theta}\), \(h=\kappa\delta\), \(\psi(\theta)=\Im(\mathcal D_{a,h}(v(\theta)))\), prove
\[
\boxed{\ 
\Big|\int_0^{2\pi}\psi(\theta)e^{-2i\theta}\,d\theta\Big|
\ \le\ C\,h\,\frac{(\log(m+3))^{C'}}{a^2}
\ }
\qquad(\text{target }C'<4).
\]

**Why this is the right frontier:** it is the *minimal* statement that makes \(\Phi^\star=o(1)\) under \(\delta=\eta a/\log^2 m\), and it is the only statement the manuscript needs to close.

---

## D) Sub‑decompositions feeding UE‑INPUT(k=2)

| Sub‑task | Status | Deliverable |
|---|---:|---|
| Split \(E'/E\) into **archimedean** + **zeta/zero kernel** parts | ✅ PARTIALLY LOCKED | ABSORB shows archimedean contribution is tame. |
| Prove archimedean contribution satisfies UE‑INPUT(k=2) bound | ✅ LIKELY CLOSED | Should be an easy bound (digamma/Stirling). |
| Reduce the remaining bound to a **zero‑kernel pairing** | 🟡 IN PROGRESS | Write coefficient as \(\sum_{\rho} K_{m,a,\delta,h}(\rho)\). |
| Attempt Weil/Li identification \(K(\rho)=\widehat g(\rho)\widehat g(1-\rho)\) | 🟥 NOT CLOSED | Treat as harness only (BRIDGE warns not to assume). |

---

## E) Decision gate

✅ **Proceed to v44 post‑build** with:
1) UE‑INPUT(k=2) as the single active box,  
2) old L1 interface archived (optional NO‑GO note),  
3) UE playbook appendix added.

No Batch‑16 required *before* the v44 post‑build.

