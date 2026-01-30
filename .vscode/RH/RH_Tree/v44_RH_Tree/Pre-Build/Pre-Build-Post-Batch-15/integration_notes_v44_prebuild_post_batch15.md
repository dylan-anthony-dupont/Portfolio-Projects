# v44 PRE‑BUILD (post‑Batch‑15) — Integration Notes (CONTROL ROOM)

**Date:** 2026-01-30  
**Decision:** ✅ Upgrade to **v44‑pre‑build‑post‑Batch‑15 artifacts** (no Batch‑16 required *before* v44 post‑build).  
**Reason:** Batch‑15 cleanly resolves the *interface question*: the v43 UE‑INPUT(L1/H¹) box is **strictly stronger than needed** and **phase‑losing** for the GEO‑C4 endpoint. We should **promote a signed k=2 interface** that is (i) endpoint‑native, (ii) weaker than L1, and (iii) the right shape for a Weil/Li bridge attempt later.

---

## 0) Snapshot of what Batch‑15 delivered

### ABSORB (PASS: Archimedean piece is not the bottleneck)
**Latch:** Decompose the log‑derivative into “zeta part + archimedean part,” and show the **archimedean contribution** to any k=2 boundary pairing is **uniformly tame** (no δ‑pathology), so the *only* hard work is the **zeta/zero kernel** contribution.  
**Consequence:** UE‑INPUT should be stated in a way that isolates the zeta kernel.

### ENVELOPE (PASS: NO‑GO for L1‑style UE interface)
**Latch:** Any UE interface that tries to control **\(\int |{\mathcal D_{a,h}}|\)** (or worse \(\sup_\theta\)) is **RH‑strength** and/or structurally mis‑matched: off‑axis quartets generate δ‑scale spikes that make L1 control “too expensive,” and it discards exactly the signed information harmonic extraction was meant to keep.

### FORCE (PASS: Geometry + carrier mode is right; interface must be signed/channel‑compatible)
**Latch:** The forced singular model on the hinge circle produces a **clean k=2 carrier** (\(\sin 2\theta\)/\(\cos 2\theta\)), and the right “unit” object to control is the **k=2 Fourier coefficient** (equivalently \(\|P_2\psi\|_{L^2}\)).  
**Consequence:** Replace UE‑INPUT(L1) by **UE‑INPUT(k=2)** (signed pairing / Fourier coefficient).

### LOCAL (PASS: finalize the minimal closure interface + patch map)
**Latch:** We can and should make the UE interface **exactly match the endpoint**. Because \(P_2\) is two‑dimensional, controlling **one complex Fourier coefficient** is equivalent (up to constants) to controlling \(\|P_2\psi\|_{L^2}\).  
Also latches the reader‑guide linkage: k=2 harmonic is the **π/2‑carrier** analogue of the **mod‑4 projector** in the lattice calculus intuition.

### BRIDGE (FAIL as a closure claim; PASS as a “future‑route harness”)
**Latch:** A direct “\(\Phi^\star\) *equals* a Weil functional” identification is **not** established.  
**However:** The *shape* of the k=2 signed pairing is exactly what a Weil test functional wants (kernel‑evaluation at zeros). So: **retain Weil/Li as a harness**, not as the current closure route.

---

## 1) Conflict resolution (what gets promoted / demoted)

### What gets demoted
**Demote:** v43’s active box  
\[
\int_0^{2\pi}\big|\mathcal D_{a,h}(v(\theta))\big|\,d\theta \ \le\ C\,h\,\frac{\log(m)^{C'}}{a^2}
\]
as the **single active statement**.

**Why:** It is (i) stronger than necessary for GEO‑C4, (ii) loses the signed phase information, and (iii) invites δ‑scale spike pathology. Batch‑15 provides multiple NO‑GO arguments that this is the wrong “interface layer” to pin as the lone frontier.

### What gets promoted
**Promote:** a *signed*, k=2‑native interface:

> **UE‑INPUT(k=2) — new single active box for v44.**  
> With \(v(\theta)=i m+\delta e^{i\theta}\), \(h=\kappa\delta\),  
> \(\mathcal L_t(v)=\frac{E'}{E}(v+t)-\frac{E'}{E}(v-t)\),  
> \(\mathcal D_{a,h}(v)=\mathcal L_{a+h}(v)-\mathcal L_{a-h}(v)\),  
> \(\psi(\theta)=\Im(\mathcal D_{a,h}(v(\theta)))\),  
> prove a bound of the form
> \[
> \boxed{\ 
> \Big|\int_0^{2\pi}\psi(\theta)\,e^{-2i\theta}\,d\theta\Big|
> \ \le\ C\,h\,\frac{(\log(m+3))^{C'}}{a^2}.
> \ }
> \]
> (Here \(C'<4\) is the “exponent budget” target; \(C'=4\) is still usable with a small \(\eta\) policy.)

**Key:** This is strictly weaker than the old L1 box because
\[
\Big|\int \psi e^{-2i\theta}\Big| \le \int |\psi| \le \int |\mathcal D|.
\]

---

## 2) New truth‑latching identity (endpoint ↔ Fourier coefficient)

Because \(\psi\) is real and \(P_2\) is the orthogonal projection onto \(\mathrm{span}\{\cos 2\theta,\sin 2\theta\}\), we have the exact identity
\[
\|P_2\psi\|_{L^2([0,2\pi])}=\frac{1}{\sqrt{\pi}}\Big|\int_0^{2\pi}\psi(\theta)e^{-2i\theta}\,d\theta\Big|.
\]
Therefore the endpoint is **exactly**
\[
\Phi^\star(m,a,\delta,h)
=\frac{\delta^2}{h}\,\|P_2\psi\|_{L^2}
=\frac{\delta^2}{h\sqrt{\pi}}\Big|\int_0^{2\pi}\psi(\theta)e^{-2i\theta}\,d\theta\Big|.
\]

So UE‑INPUT(k=2) yields
\[
\Phi^\star \ \le\ \frac{\delta^2}{h\sqrt{\pi}}\cdot C h\frac{(\log(m+3))^{C'}}{a^2}
=\frac{C}{\sqrt{\pi}}\,(\log(m+3))^{C'}\Big(\frac{\delta}{a}\Big)^2.
\]
Under the nominal policy \(\delta=\eta a/(\log(m+3))^2\),
\[
\Phi^\star \le \frac{C}{\sqrt{\pi}}\eta^2(\log(m+3))^{C'-4}=o(1)
\quad\text{if }C'<4.
\]

This is the clean v44 UE chain.

---

## 3) Updated single‑active dependency map (truth‑latched)

**Goal:** exclude off‑axis quartets ⇒ PHU ⇒ RH.

### FORCE chain (already locked)
1. Assume an off‑axis quartet at height \(m\): zeros at \(\pm a\pm i m\) with \(a>0\).
2. Under hinge‑circle witness \(v(\theta)=im+\delta e^{i\theta}\) and coupling \(h=\kappa\delta\), the singular model produces a k=2 carrier.
3. Therefore **FORCE:** \(\Phi^\star(m,a,\delta,h)\ge c_0(\kappa)>0\) (δ‑independent).

### UE chain (new single active box)
4. Identity: \(\Phi^\star=\frac{\delta^2}{h\sqrt\pi}|\int \psi e^{-2i\theta}|\).
5. **UE‑INPUT(k=2)** bounds the coefficient by \(C h(\log m)^{C'}/a^2\).
6. Hence \(\Phi^\star\le (C/\sqrt\pi)\eta^2(\log m)^{C'-4}\), which is \(<c_0\) for large \(m\) (or small \(\eta\)).

### Contradiction and collapse
7. Contradiction ⇒ no off‑axis quartet at height \(m\).
8. Since \(m\) arbitrary ⇒ PHU holds for all heights ⇒ RH.

**Single active statement:** UE‑INPUT(k=2). Everything else is locked.

---

## 4) What the Weil/Li bridge is (and is not) after Batch‑15

**Not locked:** an equality identifying the k=2 functional with Weil’s quadratic form for a compactly supported test function \(g\).

**Locked as a harness:** the k=2 coefficient is a **signed zero‑kernel functional**, i.e., after writing \(E'/E=\sum_\rho \frac{1}{v-\rho} + \text{arch}\),
the coefficient becomes a sum of evaluations of an explicit kernel \(K_{m,a,\delta,h}(\rho)\) at zeros \(\rho\).  
This is *structurally* in the same family as Weil functionals (kernel‑sum over zeros).  

**v44 posture:** keep Weil/Li as a **future bridge attempt**, but do not make the paper depend on it for closure.

---

## 5) Reader‑guide Part III linkage (why k=2 is the right carrier)

Batch‑15 LOCAL latches the conceptual correspondence:

* The hinge circle parameter \(e^{i\theta}\) is the continuous analogue of the discrete \(\pi/2\) “carrier lattice” sampling.
* The k=2 mode (\(e^{\pm 2i\theta}\)) is the contour analogue of the **mod‑4 projector** / parity gating (because \(e^{i\pi n/2}\) has period 4, and squaring corresponds to \((-1)^n\)).

This is not load‑bearing for the proof, but it is a clean post‑theorem *interpretive bridge* that makes the manuscript easier to read for anyone following the lane‑decomposition intuition.

---

## 6) Patch map summary for v44 (what changes in the manuscript)

1. **Replace** UE‑REDUCE lemma: remove the L1 bound reduction; replace with the *exact Fourier‑coefficient identity* for \(\|P_2\psi\|_{L^2}\).
2. **Replace** Box UE‑INPUT(v43) with **Box UE‑INPUT(k=2)** (single active statement).
3. **Archive** the old L1 box as a “too‑strong/phase‑loss interface” remark (optional NO‑GO subsection).
4. **Keep** FORCE section unchanged (already best‑in‑class).
5. **Add** a short “Weil/Li harness note” section: why this endpoint is compatible, and what lemma would be required for an actual identification (but explicitly label it as non‑essential).
6. **Add** the one‑page UE playbook appendix (definitions → target coefficient → decomposition → analytic routes).

---

## 7) Open work (what remains genuinely unsolved)

UE‑INPUT(k=2) still needs proof for the **true** completed object. Batch‑15 isolates the likely viable analytic routes:

1. **Archimedean part:** already essentially bounded (ABSORB).  
2. **Zero kernel part:** must bound the k=2 coefficient. Candidate techniques:
   * Hardy/Carleson measure bounds for boundary traces of meromorphic functions with controlled pole structure,
   * convert to a signed explicit‑formula kernel sum and attempt a Weil‑type positivity constraint,
   * or bound the coefficient via Cauchy estimates + zero density controls (if available), respecting the exponent budget \(C'<4\).

---

## 8) Action: write v44 pre‑build‑post‑Batch‑15 artifacts (this pass)

Files generated:
* `integration_notes_v44_prebuild_post_batch15.md`
* `CR_master_dashboard_v44_prebuild_post_batch15.md`
* `v44_next_build_plan_diff_post_batch15.md`
* `v44_patch_queue_post_batch15.md`
* `v44_build_protocol_post_batch15.md`
