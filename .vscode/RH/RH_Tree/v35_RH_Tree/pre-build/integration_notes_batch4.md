# Integration Notes — Batch 4 (Decision Batch, v34 ground truth)

These notes ingest Batch‑4 branch packets and convert them into **decision‑grade** outcomes for the v35 build.

## 0) Executive synthesis (what Batch‑4 actually decided)

Batch‑4 did **not** “advance the proof” by adding new closure. It did something more important for convergence: it **proved three structural NO‑GO constraints** that eliminate entire classes of patch‑level fixes.

### The NO‑GO set (now canonical)

1) **UE‑gate NO‑GO (scaling):** Within the current *pointwise* upper envelope architecture using the endpoint \(\sup_{\partial B}|E'/E|\) and shape‑only constants, one cannot obtain any exponent \(p>1\).  
   → Therefore η‑absorption cannot be revived by “fixing the proof” to recover δ^{3/2}; δ¹ is not a mistake, it’s the only scale‑consistent exponent in that endpoint class. fileciteturn47file2

2) **LOCAL NO‑GO:** Under κ‑admissibility, the collar blow‑up exponent \(\theta=1\) is sharp for \(\sup_{\partial B}\) bounds, and no explicit short‑interval improvement \(N(T+H)-N(T-H)\ll H\log T\) at \(H\ll 1\) can be obtained from the current explicit \(N(T)\) technology.  
   → So “shrink the window” is not a rescue mechanism for the δ‑inert local term. fileciteturn47file4

3) **FORCING NO‑GO:** In the single‑box/single‑height pair‑factor forcing architecture, forcing is constant‑limited; it cannot grow like \(\log m\).  
   → Forcing cannot be strengthened to beat the local \(\log m\) term without a wholly new forcing architecture (multi‑box or multi‑height stacking), which brings new circularity risks. fileciteturn47file3

### What this implies (posture update)

- The program’s “absorption closure” spine is **closed (negative)** under the v34 endpoint chain; it is not an execution error, it is a structural limitation. fileciteturn47file0  
- The correct next step is to **truth‑latch v35** (codify the NO‑GO constraints + patch ENT hygiene) and then pursue an explicit **UE redesign** that avoids pointwise sup/collar blow‑up while remaining compatible with the existing forcing endpoint \(D_B(W)\). fileciteturn47file1 fileciteturn47file3

---

## 1) Branch digest (PASS/FAIL/CONDITIONAL)

### RH‑ABSORB — **PASS**
- Delivers an **Exponent Budget Theorem**: under \(\delta_0=\eta/(\log m)^2\), local term scaling requires \(p-\theta\ge 1/2\) for uniform η‑absorption.  
- Specializes to v34: with \(p=1\) and \(\theta=1\), absorption is impossible; with \(\theta=1\), one would need \(p\ge 3/2\). fileciteturn47file0

### RH‑ENVELOPE — **FAIL (for “p>1” in current endpoint class), PASS (for hygiene patch package)**
- Proves the **scaling obstruction**: \(p>1\) cannot hold for the pointwise/sup endpoint class with shape‑only constants.  
- Provides **ENT patch (ENT‑1)**: redefine \(E\) via an entire completion (e.g. \(\xi_2\)), and patch the downstream log‑derivative identity in the residual envelope lemma. fileciteturn47file2

### RH‑LOCAL — **CONDITIONAL**
- Confirms the local rescue routes are NO‑GO:
  - no short‑interval explicit bounds at \(H\asymp 1/\log T\) from current \(N(T)\) inputs,  
  - θ=1 sharp for sup collar bounds.  
- Supports ENT patch to make “E entire” literally correct. fileciteturn47file4

### RH‑FORCE — **PASS**
- Delivers a forcing NO‑GO lemma (constant‑limited).  
- Delivers a **forceability criterion**: if ENVELOPE changes the endpoint functional, forcing compatibility requires a dominance link back to the dial deviation \(D_B(W)\) or a new forcing lemma.  
- Provides harness hardening: record forcing constants explicitly in JSON to prevent drift. fileciteturn47file3

### RH‑BRIDGE — **CONDITIONAL**
- Clarifies what the collar actually fixes: boundary‑contact / pointwise boundary modulus meaning; it does not remove interior zeros.  
- Provides a **NO‑CONVERSE guard**: boundary modulus \(|W|=1\) does not constrain interior zeros; Proposition 9.2 is one‑directional and needs its hypothesis highlighted.  
- Flags and patches ENT/meromorphic misuse (“Λ₂ entire”). fileciteturn47file1

---

## 2) v35 build intent (what we will actually change)

v35 should be a *truth‑latching* build with three objectives:

1) **Codify the NO‑GO constraints inside the manuscript** (so no future version can “wish” \(p>1\) back into existence under the same endpoint, or speculate about forcing growth, or window‑shrink miracles). fileciteturn47file2 fileciteturn47file3 fileciteturn47file4

2) **Fix ENT / holomorphy hygiene globally** (adopt an actually‑entire completion; patch every “E is entire” usage + residual identity). fileciteturn47file2 fileciteturn47file4

3) **Write the frontier correctly:** the remaining analytic unknown is an UE redesign (S5) that avoids pointwise sup + collar blow‑up **without changing the forced endpoint** \(D_B(W)\), or else redesign forcing architecture (high risk). fileciteturn47file1 fileciteturn47file3

---

## 3) Control‑Room decision statement (paste‑ready)

> **Batch‑4 conclusion:** The v34 absorption narrative is not “unfinished”; it is structurally blocked by a scaling obstruction (UE) and by sharp local/forcing limitations.  
> v35 will therefore (i) harden these NO‑GO facts in‑text, (ii) fix ENT hygiene, and (iii) reframe the paper’s open frontier as the design of a non‑pointwise upper‑envelope mechanism compatible with the existing forcing endpoint.

