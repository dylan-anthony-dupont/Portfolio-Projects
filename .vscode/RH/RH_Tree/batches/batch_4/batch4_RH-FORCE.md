# batch4_RH-FORCE — Forcing scaling NO‑GO + forceability criterion for envelope redesign (v34 ground truth)

**Callsign:** RH‑FORCE  
**Ground truth:** `manuscript_v34.pdf` (compiled 2026‑01‑22)  
**Key refs (v34):** Lemma 8.1 (Short‑side forcing), Theorem 11.1 (Tail inequality / criterion form), Appendix A (tail harness)

---

## 0) v34 anchors (what “forcing” is in v34)

1. **Raw forcing input (pair factor):** Lemma 8.1 gives a fixed *phase rotation lower bound* on the near vertical side for the pair factor
   \[
   Z_{\rm pair}(v)=(v-(a+im))(v-(-a+im)),
   \]
   namely \(\Delta_{I_+}\arg Z_{\rm pair}\ge \pi/2\).【527:0†manuscript_v34.pdf†L47-L65】

2. **Forcing vs envelope comparison point (the tail criterion):** Theorem 11.1 states the tail criterion inequality (18) with **pointwise UE exponent \(p=1\)**:
   \[
   2C_{\rm up}\Big(\delta L(m)+\tfrac{N_{\rm up}(m)}{\kappa}\Big)
   \;<\;
   c-\delta\Big(K_{\rm alloc}c_0L(m)+C''_{h}(\log m+1)\Big),
   \tag{18}
   \]
   where \(c_0=\frac{3\log 2}{8\pi}\), \(c=\frac{3\log 2}{16}\), \(K_{\rm alloc}=3+8\sqrt3\).【528:5†manuscript_v34.pdf†L7-L52】

3. **Why absorption fails under \(p=1\):** v34 explicitly records that when the UE prefactor is \(\delta^p\) and the collar contributes \(N_{\rm loc}(m)/(\kappa\delta)\), the local term scales as \(\delta^{p-1}N_{\rm loc}(m)/\kappa\), hence is suppressible by shrinking \(\delta\) only if \(p>1\). In the proved pointwise form \(p=1\), the local term is **\(\delta\)-inert**.【528:13†manuscript_v34.pdf†L41-L71】

4. **Harness contract:** Appendix A states the harness checks strict separation \(\mathrm{LHS}_{\rm hi}<\mathrm{RHS}_{\rm lo}\) for (18), given a constants file and recorded parameters (including \(p\)), and explicitly warns it is *audit harness only* (not a proof substitute).【530:15†manuscript_v34.pdf†L4-L11】

---

## 1) PRIMARY TASK 1 — Forcing scaling feasibility (single‑box / single‑height)

### Decision (required)

**Forcing strengthening feasibility (within the current v34 single‑box / single‑height forcing architecture): FAIL.**  
Within v34’s architecture, the forcing margin is intrinsically **\(O(1)\)** (bounded by an absolute constant) and cannot be made to grow like \(\log m\) or any unbounded function of \(m\) without changing the forcing architecture itself.

### Lemma (formal NO‑GO; paste‑ready for v35)

> **Lemma (Single‑box forcing is constant‑limited).**  
> In the v34 forcing architecture (one aligned box at one height \(m\), forcing induced only by the local pair factor \(Z_{\rm pair}\) on a single near vertical side \(I_+\)), the total available forcing contribution is bounded above by an absolute constant independent of \(m\). In particular, it cannot grow like \(\log m\) (or any unbounded function of \(m\)) as \(m\to\infty\).
>
> **Proof (referee‑grade, short).**  
> On \(I_+=\{\alpha+iy:\;|y-m|\le \delta\}\) one has
> \[
> Z_{\rm pair}(\alpha+iy)=\big((\alpha-a)+i(y-m)\big)\big((\alpha+a)+i(y-m)\big).
> \]
> Along \(y\in[m-\delta,m+\delta]\), the argument of each linear factor varies by at most \(\pi\), because it is an \(\arctan\) function whose range is contained in \((-\pi/2,\pi/2)\) and whose endpoint difference is at most \(\pi\). Therefore
> \[
> \Delta_{I_+}\arg Z_{\rm pair}\le \pi+\pi = 2\pi,
> \]
> uniformly in \(m\). In v34 the “forcing budget” enters the tail inequality only through a fixed conversion scalar \(c_0\) (and fixed allocation/budget constants), producing a forcing constant \(c=c_0\cdot(\pi/2)\) in Theorem 11.1.【528:5†manuscript_v34.pdf†L22-L52】  
> Hence the forcing side is bounded by an absolute constant depending only on the chosen comparison metric and cannot scale with \(m\). \(\square\)

### What locks forcing to \(\delta^0\) (assumption audit)

This NO‑GO is driven by three structural facts of the v34 forcing mechanism:

1. **One quartet ⇒ one quadratic pair factor.** The forcing input is a bounded phase jump from a degree‑2 polynomial factor (two zeros). That argument change is bounded by \(2\pi\), independent of \(m\).

2. **One box / one pass around boundary.** The boundary program uses a single simple loop around the box. Without allowing multiple windings or multiple disjoint boxes, there is no mechanism to accumulate unbounded phase.

3. **Fixed metric conversion.** The conversion from phase to the tail inequality’s “dial deviation” scale uses a fixed scalar \(c_0\) and produces a fixed positive constant \(c\) used in Theorem 11.1.【528:5†manuscript_v34.pdf†L22-L52】

### If you *did* try to force unbounded growth: only 2 viable architectures exist, both high‑risk

(You asked for ≤2 candidates; these are the only two that could even *conceptually* yield unbounded forcing.)

1. **Multi‑box accumulation at the same height (sum forcing across many disjoint boxes).**  
   **Why it fails in the RH‑exclusion posture:** you cannot guarantee the existence of *multiple* off‑axis quartets at the same height \(m\); your contradiction hypothesis is typically “there exists at least one”. Any forcing that sums over many boxes requires additional hypotheses about the zero set (or a selection lemma that manufactures many forced boxes from one quartet), which is currently absent and plausibly RH‑equivalent.

2. **Vertical stacking across many heights (sum forcing across a tower of boxes).**  
   **Why it fails:** it presupposes off‑axis quartets at many heights (or a propagation law from one quartet to many), again a new deep obligation. It also breaks the one‑height reduction framework and introduces heavy new dependencies (window counts, inter‑height coupling, and selection rules), with high circularity risk.

**Conclusion:** Under v34’s intended logic (“one quartet at height \(m\) leads to a single forcing‑vs‑envelope contradiction at that same \(m\)”), forcing is fundamentally constant‑limited.

---

## 2) PRIMARY TASK 2 — Forcing compatibility with an ENVELOPE redesign functional \(\Phi_B(W,E)\)

### What forcing actually lower‑bounds in v34

The v34 forcing‑vs‑envelope comparison is built around the **dial deviation endpoint**:
\[
D_B(W):=\sum_{\pm}\big|W(v_\pm)-e^{i\phi_{\pm,0}}\big|,
\]
where \(v_\pm=\pm\alpha+im\) are the dial centers and \(e^{i\phi_{\pm,0}}\) are fixed boundary anchors.

- The **upper envelope** bounds this dial deviation by a function of \(\sup_{\partial B}|E'/E|\) and then by the residual+local split, yielding a bound of the form
  \[
  D_B(W)\le 2C_{\rm up}\Big(\delta L(m)+\tfrac{N_{\rm loc}(m)}{\kappa}\Big),
  \]
  stated explicitly in v34 (Cor. 10.10).【528:13†manuscript_v34.pdf†L24-L40】

- The **forcing side** supplies the positive constant \(c\) and subtracts \(\delta\)-scaled budget terms, producing the right side of (18) in Theorem 11.1.【528:5†manuscript_v34.pdf†L22-L52】

### Lemma (forceability criterion for any redesigned endpoint functional)

> **Lemma (Forceability criterion for redesigned endpoints).**  
> Let \(\Phi_B(W,E)\ge 0\) be any proposed “envelope endpoint functional” intended to replace the dial deviation \(D_B(W)\) in the forcing‑vs‑envelope contradiction at height \(m\). Under the v34 forcing mechanism, a forcing lower bound for \(\Phi_B\) is available **only if** one proves a structural inequality
> \[
> \Phi_B(W,E)\;\ge\; D_B(W)
> \quad\text{for all admissible boxes }B.
> \]
> In that case, the existing forcing chain yields
> \[
> \Phi_B(W,E)\;\ge\; c-\delta\big(K_{\rm alloc}c_0L(m)+C''_h(\log m+1)\big).
> \]
>
> **Proof.** Immediate from \(\Phi_B\ge D_B\) and the fact that the v34 forcing side lower‑bounds \(D_B\) by the RHS appearing in Theorem 11.1’s contradiction inequality.【528:5†manuscript_v34.pdf†L22-L52】 \(\square\)

### No‑go statement (if ENVELOPE changes the endpoint but does not dominate \(D_B\))

> **No‑go (endpoint mismatch kills forcing).**  
> If ENVELOPE proposes a redesigned endpoint functional \(\Phi_B(W,E)\) and does **not** provide a lemma linking it to \(D_B(W)\) (e.g. \(\Phi_B\ge D_B\) or a direct “quartet ⇒ \(\Phi_B\ge\) forcing margin” statement), then **the pair‑factor forcing argument does not apply to \(\Phi_B\)**. In that case, the redesign is not compatible with the current forcing architecture and cannot be used in the tail contradiction without a new forcing lemma.

### Practical compatibility guidance (for ENVELOPE)

- **Safe redesign (compatible):** Keep the endpoint as \(D_B(W)\) and redesign only the *upper bound* (replace Cor. 10.10 by a stronger estimate that avoids the sup‑based collar blow‑up, or achieves an effective \(p>1\) in the sense of Remark 10.11).【528:13†manuscript_v34.pdf†L41-L71】

- **Unsafe redesign (incompatible unless patched):** Replace \(D_B(W)\) by a different \(\Phi_B\) without simultaneously proving a forceability link \(\Phi_B\ge D_B\) or a direct forcing lower bound for \(\Phi_B\).

---

## 3) PRIMARY TASK 3 — Certificate/harness implications (G‑12 alignment hardening)

### Current v34 harness contract (what it checks)

Appendix A records that the harness checks **exactly** Theorem 11.1 / equation (18) by computing interval enclosures for LHS and RHS and reporting whether \(\mathrm{LHS}_{\rm hi}<\mathrm{RHS}_{\rm lo}\).【530:15†manuscript_v34.pdf†L4-L11】

### Forcing‑side fields that should be explicit in JSON (even if “exact”)

To keep theorem↔artifact alignment audit‑safe (and prevent a repeat of v32’s \(K_{\rm alloc}\) drift), the tail‑check JSON should record the forcing constants *as inputs*, not as implicit hard‑codes:

- \(c_0 = 3\log 2/(8\pi)\),
- \(c   = 3\log 2/16\),
- \(K_{\rm alloc}=3+8\sqrt3\).

These appear explicitly in Theorem 11.1’s assumptions.【528:5†manuscript_v34.pdf†L22-L33】

### Minimal JSON schema extension (paste‑ready; v35 harness hardening)

Add to `v34_constants_m10.json` (or its v35 successor):

```json
"tail_inequality": {
  "theorem": "Theorem 11.1",
  "equation": "(18)",
  "lhs_expr": "2*C_up*(delta*L + Nup/kappa)",
  "rhs_expr": "c - delta*(Kalloc*c0*L + C_hpp*(logm+1))",
  "forcing_constants": {
    "c0_exact": "3*log(2)/(8*pi)",
    "c_exact": "3*log(2)/16",
    "Kalloc_exact": "3+8*sqrt(3)"
  },
  "forcing_architecture": "single_box_single_height_Zpair",
  "endpoint_functional": "dial_deviation_sum"
}
```

### Verifier modifications (exactly what must change)

1. Parse and display these fields in the verifier’s “inputs summary”.
2. Compute \(c_0,c,K_{\rm alloc}\) from the recorded expressions (or treat them as exact constants with directed rounding into tiny intervals).
3. Assert in the verifier that the theorem referenced in JSON is exactly the inequality being checked:
   - print: `Checking Theorem 11.1 / Eq (18)`.
   - print the LHS/RHS expressions from JSON.
4. If ENVELOPE redesign changes the inequality form, bump:
   - `equation`, `lhs_expr`, `rhs_expr`, and `endpoint_functional`,
   - and keep `forcing_architecture` unchanged only if the forcing lemma truly is unchanged.

---

## 4) Paste‑ready manuscript edits (v35) to stop “maybe forcing can be strengthened” speculation

### (i) Insert after Lemma 8.1 (Short‑side forcing) — constant‑limited forcing remark

```tex
\begin{lemma}[Single-box forcing is constant-limited]
In the single-box, single-height forcing architecture of \S\ref{sec:short-side-forcing},
the total forcing available from the pair factor $Z_{\rm pair}$ is bounded by an absolute
constant independent of the height $m$. In particular, forcing cannot grow like $\log m$ (or any
unbounded function of $m$) as $m\to\infty$ without changing the forcing architecture.
\end{lemma}

\begin{proof}
On $I_+=\{\alpha+iy:|y-m|\le\delta\}$ one has
$Z_{\rm pair}(\alpha+iy)=((\alpha-a)+i(y-m))((\alpha+a)+i(y-m))$.
Each factor contributes an argument variation of at most $\pi$ as $y$ ranges over an interval,
hence $\Delta_{I_+}\arg Z_{\rm pair}\le 2\pi$, uniformly in $m$. The forcing budget in the tail
criterion is obtained by multiplying this phase increment by fixed geometry/normalization constants.
\end{proof}
```

### (ii) Insert near Theorem 11.1 — compatibility criterion for redesigned endpoints

```tex
\begin{remark}[Forceability criterion for redesigned envelope endpoints]
The forcing mechanism in this paper lower-bounds the dial deviation
$D_B(W)=\sum_{\pm}|W(v_\pm)-e^{i\phi_{\pm,0}}|$.
Any redesign that replaces $D_B$ by a different endpoint functional $\Phi_B(W,E)$ must supply
a lemma linking $\Phi_B$ to $D_B$ (e.g. $\Phi_B\ge D_B$), or else provide a new forcing lemma
directly lower-bounding $\Phi_B$ under the existence of an off-axis quartet.
\end{remark}
```

### (iii) Appendix A (harness) — record forcing constants explicitly

Add a short note in Appendix A.1:

```tex
\paragraph{Forcing constants recorded.}
The tail-check JSON records the forcing constants $(c_0,c,K_{\rm alloc})$ explicitly (even though
they are exact closed forms) to prevent silent drift across versions. The verifier prints these
constants and the exact theorem inequality it checks.
```

---

## MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* **Callsign:** RH‑FORCE
* **Result classification:** **PASS** (delivered a proof‑grade forcing NO‑GO + compatibility criterion + harness hardening spec)
* **Target gaps closed (by ID):**
  * **(none newly closed)** — this batch is a decision/boundary clarification; it **freezes** the forcing architecture constraints.
* **Target gaps still open (by ID):**
  * **G‑12** (theorem↔artifact alignment): **still open globally**, but the JSON/harness edits above directly harden the forcing side against future drift.
  * **UE‑Gate / envelope redesign blockers** (owned by ENVELOPE): not owned here.
* **Key conclusions (≤5 bullets):**
  1. **Forcing strengthening is a NO‑GO** under v34’s single‑box/single‑height pair‑factor mechanism: forcing is \(O(1)\), not \(\log m\).
  2. Any attempt to get unbounded forcing requires **multi‑box** or **multi‑height stacking**, which introduces major new obligations and circularity risks.
  3. The forcing mechanism lower‑bounds the **dial deviation** endpoint \(D_B(W)\); it does **not** automatically lower‑bound arbitrary redesigned functionals.
  4. A redesigned envelope endpoint \(\Phi_B\) is compatible **only if** one proves \(\Phi_B\ge D_B\) (or provides a new forcing lemma for \(\Phi_B\)).
  5. The harness should **record** \((c_0,c,K_{\rm alloc})\) explicitly in JSON to prevent a repeat of v32‑style constant drift.
* **Paste-ready manuscript edits:**
  (i) revised lemma/proposition statements: see Lemma “Single‑box forcing is constant‑limited” (new, after Lemma 8.1)  
  (ii) revised definitions/remarks: see Remark “Forceability criterion for redesigned envelope endpoints” (near Theorem 11.1)  
  (iii) revised theorem/inequality lines: **none** (Theorem 11.1 / (18) unchanged; only harness metadata and narrative clarifications)
* **Dependencies on other branches:**
  * ENVELOPE must decide whether redesign keeps \(D_B(W)\) as endpoint or supplies \(\Phi_B\ge D_B\)/new forcing lemma.
* **Referee risk notes (anticipated objections + how addressed):**
  * **“Why can’t forcing scale with \(m\)?”** Addressed by the explicit bound \(\Delta\arg Z_{\rm pair}\le 2\pi\) for the quadratic pair factor on a single pass.
  * **“Does this rule out all future forcing improvements?”** No—only within the *current* single‑box architecture; any stronger forcing requires an explicit new architecture and new hypotheses, which must be stated and audited.
  * **“Endpoint redesign ambiguity.”** Resolved by the forceability criterion: forcing applies to \(D_B\) unless a bridge lemma to \(\Phi_B\) is proved.
