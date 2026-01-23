# v34 → v35 next build plan (diff-only) — Batch‑4 updated

Locked baseline: **v34**  
Purpose of v35: **truth‑latch** the Batch‑4 decision set (NO‑GO constraints + ENT hygiene + harness hardening).

This is intentionally not an “advance the proof” build. It is a **convergence** build: it prevents future drift and makes the remaining frontier obligations explicit.

---

## 1) ENT‑1: Fix the “Λ₂ is entire” error by switching to an actually‑entire completion (HIGH priority)

**Why:** Multiple proofs rely on “E is entire”; in v34 \(E(v)=\Lambda_2(1+v)\) is meromorphic as written. This is a direct referee attack vector. fileciteturn47file2 fileciteturn47file4

**Patch:**
- In §`sec:width2`, replace \(\Lambda_2\) (meromorphic) as the working object by an entire completion:
  \[
  \Xi_2(u)=\xi(u/2)=\frac{u(u-2)}{8}\pi^{-u/4}\Gamma(u/4)\zeta(u/2),\qquad E(v):=\Xi_2(1+v).
  \]
- Patch the residual envelope log‑derivative identity accordingly by adding the rational terms \((1/u+1/(u-2))\) (ENVELOPE provides the exact TeX block). fileciteturn47file2

**Acceptance check:** `grep` for “Λ_2 is entire” and “E is entire” should become literally correct.

---

## 2) Insert “Exponent Budget Theorem” and replace slogan‑level UE‑gate text (HIGH priority)

**Why:** We need a single canonical inequality that states exactly when η‑shrinking can ever suppress the local term, and it must match the nominal scaling \(\delta_0=\eta/(\log m)^2\). fileciteturn47file0

**Patch:**
- Insert Theorem `thm:exponent-budget` (ABSORB) after Remark `rem:UE-gate` (or in §12 status section).
- Revise Remark `rem:UE-gate` so it references the budget theorem and states the correct condition \(p-\theta\ge 1/2\) (and hence \(p\ge 3/2\) when \(\theta=1\)). fileciteturn47file0

**Optional cleanup:** demote Lemma `lem:UE-d1-obstruction` to a corollary of the budget theorem.

---

## 3) Insert UE scaling NO‑GO lemma: “p>1 cannot happen with sup endpoint” (HIGH priority)

**Why:** Prevents future versions from re‑introducing δ^{3/2} claims inside the same endpoint class; makes the pivot to UE redesign (S5) logically mandatory rather than stylistic. fileciteturn47file2

**Patch:** add Lemma `lem:UE-scaling-nogo` immediately after the UE‑gate remark/obstruction lemma.

---

## 4) Insert forcing NO‑GO + forceability criterion and harden harness metadata (MED/HIGH priority)

**Why:** Forcing cannot be “scaled up” to beat a \(\log m\) local term. Also, any UE redesign that changes the endpoint functional must be explicitly linked back to the forced endpoint. fileciteturn47file3

**Patch:**
- After Lemma 8.1, insert Lemma “single‑box forcing is constant‑limited”.
- Near Theorem 11.1, insert Remark “forceability criterion for redesigned endpoints”.
- In Appendix A + repro pack JSON schema, record \((c_0,c,K_{\rm alloc})\) explicitly and record the endpoint functional string, so theorem↔artifact alignment is audit‑locked. fileciteturn47file3

---

## 5) Bridge guardrails: add “NO converse” remark and patch boundary/entire language (MED priority)

**Why:** Must prevent implication drift: boundary modulus \(|W|=1\) does not exclude interior zeros; Proposition 9.2 is strictly one‑directional. Also patch any residual “E entire” phrases that remain. fileciteturn47file1

**Patch:** insert remark after Bridge 1 remark 9.3 + patch “entire” → “holomorphic on neighborhood” only if ENT‑1 not adopted (but ENT‑1 is preferred).

---

## 6) Local note (optional): codify short‑interval NO‑GO (LOW/MED priority)

Add one sentence to the UE‑gate remark/status section: current explicit zero‑count inputs do not deliver \(H\ll 1\) short‑interval bounds.

---

## 7) v35 “Frontier section” (S5) — rewrite the open problem correctly (MED priority)

Replace any “we need p>1” language with the correct frontier statement:

- p>1 is impossible for the pointwise sup endpoint class (Lemma `lem:UE-scaling-nogo`).
- θ=1 is sharp for pointwise collar bounds (LOCAL).
- Therefore S5 must redesign the **upper bound** on the same forced dial deviation \(D_B(W)\) using a non‑pointwise boundary functional (energy / integral / averaged contour), while maintaining forcing compatibility (FORCE).

---

## Output artifacts to be built at GO‑time

- `manuscript_v35.tex` / `manuscript_v35.pdf`
- `v35_patchlog.md` (diff vs v34, with patch IDs)
- `v35_repro_pack.zip` (updated JSON schema + verifier prints)
- Updated `CR_master_dashboard.md` (v35 locked)

