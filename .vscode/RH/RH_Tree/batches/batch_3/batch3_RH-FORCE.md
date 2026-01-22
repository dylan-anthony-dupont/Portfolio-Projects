# batch3_RH-FORCE.md

**Callsign:** RH-FORCE  
**Ground truth:** v33 (`manuscript_v33.pdf/tex`) only.  
**Batch:** 3 (UE-gate decision batch)

---

## 0) UE‑gate answers (required by Batch‑3 protocol)

### (i) What UE δ‑exponent is actually supported by a proof? (best proven p)

**Best proven (as written in v33):** **p = 1**.

* v33 **states** the UE lemma with a $\delta^{3/2}$ prefactor (Lemma 10.2, equation (16)), but its **proof chain records scale factors** “$\delta^{-1/2}$ (harmonic measure / Poisson), $\delta$ (Poincaré/Wirtinger), $\delta^{1/2}$ ($L^2\to\sup$)” which multiply to **$\delta^{1}$**, not $\delta^{3/2}$.  
* Until the missing $\sqrt{\delta}$ mechanism is inserted **in-text**, the strongest UE exponent that is actually *proved* is **$\delta^{1}$**.

This is exactly the UE‑gate risk: if only $p=1$ is available, the tail inequality cannot be made uniform in $m$ by $\eta$‑absorption (Task A below).

### (ii) Does S1′ (η‑absorption tail closure) survive under that p?

**NO** under **p = 1**, given the current local/collar mechanism (width‑1 local window majorant $N_{\rm up}(m)\sim \log m$ and collar bound $\sup_{\partial B}|Z'_{\rm loc}/Z_{\rm loc}|\lesssim N_{\rm up}(m)/(\kappa\delta)$).

Reason: under $p=1$ the envelope side contributes a term $\asymp N_{\rm up}(m)/\kappa$ **independent of $\delta$**, hence it grows like $\log m$ and eventually dominates the fixed forcing constant $c$.

### (iii) Minimal v34 edits implied by this conclusion

1. Insert an **honesty checkpoint**: an explicit lemma/remark stating the **UE‑$\delta^1$ obstruction** under the current collar/local-window setup (Task A).
2. Make the **repro/sanity harness** explicitly **parameterize the UE exponent $p$** (or warn that JSON must be regenerated if $p$ changes) so G‑12 remains stable across the UE decision (Task C).
3. In the narrative around Theorem 11.1 / §12, add one line: **tail closure requires UE exponent $p>1$** (or equivalent suppression of the local term).

---

## 1) Task A (CRITICAL): UE‑$\delta^1$ obstruction under width‑1 local window

### A.1 Context: where the obstruction enters in v33

v33 tail inequality (Theorem 11.1, eq. (19)) is (notation as in v33):
\[
2C_{\rm up}\Big(\delta^{3/2}L(m) + \delta^{1/2}\frac{N_{\rm up}(m)}{\kappa}\Big)
\;<\;
c-\delta\Big(K_{\rm alloc}c_0L(m)+C_h''(\log m+1)\Big),
\tag{19}
\]
with $N_{\rm up}(m)=1.01\log m+17$ for $m\ge 10$, $L(m)=C_1\log m + C_2$, and fixed forcing constants
$c_0=\frac{3\log2}{8\pi}$, $c=\frac{3\log2}{16}$, $K_{\rm alloc}=3+8\sqrt3$.

The **local term exponent $\delta^{1/2}$** comes from:
* UE prefactor $\delta^{3/2}$ (Lemma 10.2), multiplied by
* collar bound $\sup_{\partial B}\big|Z'_{\rm loc}/Z_{\rm loc}\big|\le N_{\rm up}(m)/(\kappa\delta)$ (Lemma 10.7).

If instead UE only gives a **$\delta^1$ prefactor**, that local contribution becomes **$\delta^{0}\cdot N_{\rm up}(m)/\kappa$**.

### A.2 Clean “no‑go” lemma (paste‑ready for v34)

Below is the requested checkpoint lemma/remark. It is deliberately *mechanical* and uses only:

* fixed forcing constant $c$,
* monotonicity $N_{\rm up}(m)\to\infty$,
* the collar form $N_{\rm up}(m)/(\kappa\delta)$.

It does **not** assume RH, and it does **not** require any additional analytic input.

---

## 2) Task B: can forcing be strengthened to avoid needing UE (p>1)?

### B.1 Why the forcing side is fundamentally constant‑limited (in current spine)

In v33 the forcing side is encoded by fixed constants $(c_0,c,K_{\rm alloc})$ that arise from:

* a bounded phase rotation forced by the aligned pair factor on a short side (Lemma 8.1 / “short‑side forcing”), and
* an allocation argument that distributes this forcing against boundary costs with an explicit coefficient $K_{\rm alloc}$.

This forcing is **geometric/topological at one height** and has no natural mechanism to scale like $\log m$.

Therefore, if the envelope side contributes an unavoidable **$\asymp \log m$** term (as it does under UE‑$\delta^1$ with width‑1 local window), **no choice of $\eta$ or $\delta$ can rescue the inequality**: the forcing side is capped by $c$ while the envelope cost diverges.

### B.2 Candidate modifications (≤2), ranked

**Candidate 1 (best): redesign the local window so that $N_{\rm up}(m)$ is $\delta$‑suppressed.**  
*Idea:* Replace the fixed “width‑1” local window by a $\delta$‑dependent window whose zero count is $O(1)$ at the chosen scale $\delta=\eta/(\log m)^2$.  
*Effect:* If $N_{\rm up}(m)$ becomes $O(1)$, then even UE‑$\delta^1$ would yield a bounded local term $O(1/\kappa)$, removing the $\log m$ obstruction.  
*Cost:* This is **not a forcing‑side patch**; it is a redesign of $Z_{\rm loc}$ / the collar machinery (dependency on RH‑ENVELOPE / RH‑COLLAR branches).  
*Viability:* **Medium‑Low** (plausible in principle, but would require re‑proving the residual envelope Lemma 7.1 with the new $Z_{\rm loc}$ definition and ensuring the collar bound still holds).

**Candidate 2 (poor): multi‑box forcing accumulation to manufacture $\log m$ forcing.**  
*Idea:* Try to “stack” forcing contributions from multiple boxes/heights and sum them.  
*Risk:* This would fundamentally alter the proof spine and is likely to introduce either circularity (using many off‑axis objects to rule out off‑axis objects) or uncontrolled dependencies across heights.  
*Viability:* **Very Low / not recommended**.

**Conclusion for Task B:** Under the current single‑height boundary program, **forcing is constant‑limited** and cannot offset an envelope term growing like $\log m$.

---

## 3) Task C: scaffold robustness (G‑12 continuity) under UE exponent decision

### C.1 v34‑ready appendix note (parameterize the UE exponent p)

Even if the repro pack is “sanity check only,” it must remain aligned to the theorem **as written**. The clean way to keep the harness robust to UE‑gate decisions is to parameterize the exponent.

* If Lemma 10.2 is $\delta^p\cdot\sup_{\partial B}|E'/E|$, and the collar bound is $N_{\rm up}(m)/(\kappa\delta)$, then after the log‑derivative split
  \[
  \mathrm{LHS}(m,\delta;p)
  = 2C_{\rm up}\Big(\delta^{p}L(m) + \delta^{p-1}\frac{N_{\rm up}(m)}{\kappa}\Big).
  \]
  v33 corresponds to $p=\tfrac32$; the UE‑gate “bad” case is $p=1$.

**Harness requirement:** store and print `p` (and therefore the exponents $p$ and $p-1$) in the JSON, and compute LHS using the formula above.

This prevents accidental “silently changed exponent” drift.

---

# MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* Prompt Batch Number: 3
* Callsign: RH-FORCE
* Result classification: **CONDITIONAL**
  * PASS on Tasks A/C deliverables (obstruction lemma + scaffold parameterization).
  * CONDITIONAL for global S1′ viability: depends on whether UE can truly deliver $p>1$ (nominally $p=3/2$).
* Target gaps closed (by ID):
  * **G-12 (continuity/robustness)** — parameterize UE exponent in the sanity harness so theorem–check alignment survives UE edits.
* Target gaps still open (by ID):
  * **G-2 / UE scaling gate** (the missing $\sqrt{\delta}$ in Lemma 10.2’s proof text).
  * **G-4** (δ‑uniformity for absorption) insofar as it depends on the correct UE exponent.
* Key conclusions (5 bullets max):
  1. v33’s **UE lemma is stated with $p=3/2$** but the **proof as written only supports $p=1$** (scale factors shown multiply to $\delta^1$).
  2. If UE is only **$\delta^1$**, then the tail inequality acquires an **unavoidable $\asymp N_{\rm up}(m)/\kappa \sim \log m$** term and **cannot hold for all large $m$**, regardless of $\eta$.
  3. Therefore **S1′ η‑absorption tail closure fails** under $p=1$ with the current width‑1 local window + collar scheme.
  4. The forcing mechanism in the current spine is **constant‑limited**; it cannot plausibly generate $\log m$ forcing to defeat the obstruction.
  5. The repro/sanity harness must **record UE exponent $p$** and compute $\mathrm{LHS}(m,\delta;p)$ accordingly to prevent exponent drift (G‑12 continuity).

* Paste-ready manuscript edits:

  **(i) revised lemma/proposition statements**

  Add the following checkpoint in §11 (immediately after Theorem 11.1, or as a Remark at the start of §12):

  ```tex
  \begin{lemma}[UE--$\delta^1$ obstruction under width--1 local window]\label{lem:UE-d1-obstruction}
  Assume that in place of Lemma~10.2 one only has an upper-envelope bound with exponent $p=1$, i.e.
  \[
    \sum_{\pm}\big|W(v_\pm)-e^{i\phi^\pm_0}\big|
    \le 2C_{\rm up}\,\delta\,
    \sup_{v\in\partial B}\Big|\frac{E'(v)}{E(v)}\Big|.
  \]
  Assume also the log-derivative split (Lemma~10.6), the residual envelope
  $\sup_{\partial B}|F'/F|\le L(m)$ (Lemma~7.1), and the collar bound
  $\sup_{\partial B}|Z'_{\rm loc}/Z_{\rm loc}|\le N_{\rm up}(m)/(\kappa\delta)$ (Lemma~10.7),
  with $N_{\rm up}(m)=1.01\log m+17\to\infty$.
  Then the tail inequality cannot hold for all $m\ge 10$ under the $\eta$--absorption scheme:
  for every fixed $(C_{\rm up},\kappa,c)$ there exists $m_0$ such that for all $m\ge m_0$ and all
  $\delta\in(0,1]$,
  \[
    2C_{\rm up}\Big(\delta L(m)+\frac{N_{\rm up}(m)}{\kappa}\Big)\;\ge\; c
    \;\ge\;
    c-\delta\Big(K_{\rm alloc}c_0L(m)+C_h''(\log m+1)\Big),
  \]
  hence the strict tail inequality fails.
  \end{lemma}

  \begin{proof}
  Under $p=1$ the UE bound and the split give
  $\sum_{\pm}|W(v_\pm)-e^{i\phi^\pm_0}|
  \le 2C_{\rm up}\delta\big(L(m)+N_{\rm up}(m)/(\kappa\delta)\big)
  =2C_{\rm up}(\delta L(m)+N_{\rm up}(m)/\kappa)$.
  The forcing side of the tail inequality is at most $c$ for every $\delta>0$ since the bracketed factor
  is nonnegative. Because $N_{\rm up}(m)\to\infty$, choose $m_0$ so that
  $2C_{\rm up}N_{\rm up}(m_0)/\kappa\ge c$. Then for all $m\ge m_0$ the left-hand side is $\ge c$
  (even after dropping the nonnegative term $\delta L(m)$), so the strict tail inequality cannot hold.
  \end{proof}
  ```

  **(ii) revised definitions/remarks**

  Add a short remark to Theorem 11.1 (or to the start of §12) making the UE gate explicit:

  ```tex
  \begin{remark}[UE exponent gate]\label{rem:UE-gate}
  The $\eta$--absorption tail closure requires an upper-envelope exponent $p>1$ in Lemma~10.2
  (as written, $p=3/2$). If only $p=1$ were available, the collar/local-window term would contribute
  $\asymp N_{\rm up}(m)/\kappa\sim\log m$ to the tail inequality, obstructing any uniform tail closure;
  see Lemma~\ref{lem:UE-d1-obstruction}.
  \end{remark}
  ```

  **(iii) revised theorem/inequality lines**

  No change to Theorem 11.1 (eq. (19)) is proposed here.  
  This branch instead adds the **explicit obstruction checkpoint** so v34 cannot silently rely on an unproved exponent.

* Dependencies on other branches:
  * **RH-ENVELOPE / UE proof branch:** must either (a) supply the missing in-text step that truly yields $p=3/2$ (or any $p>1$), or (b) redesign the local-window/collar mechanism so the local term is $\delta$-suppressed even with $p=1$.
  * **RH-CERT / scaffold branch:** implement the `p` parameterization in the JSON and verifier output.

* Referee risk notes (anticipated objections + how addressed):
  * **Objection:** “This lemma is negative / discouraging.”  
    **Response:** It is an *honesty checkpoint* ensuring the program cannot proceed on an unproved UE exponent. It is purely deductive and uses only monotonicity of $N_{\rm up}(m)$ and the sign of the forcing bracket.
  * **Objection:** “Maybe cancellations reduce the local term.”  
    **Response:** The collar bound is an absolute-value sup bound. Without a new mechanism proving cancellations uniformly, the obstruction applies to the current absolute-value framework.
  * **Objection:** “Could $\kappa$ be tuned with $m$?”  
    **Response:** In v33 $\kappa$ is fixed once and for all (Definition 10.4). Allowing $\kappa=\kappa(m)\to\infty$ is not geometrically meaningful and would require a redesign of admissibility and all dependent lemmas.
