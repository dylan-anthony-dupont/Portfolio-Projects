# v32_status_decision_v2

Date: 2026-01-20  
Scope: Full manuscript audit of `manuscript_v32.tex` (top-to-bottom) using the A1–E1 checklist supplied in-chat.

## 0. Executive decision

**Unconditional RH closure is *not yet* achieved in v32.**  
What v32 *does* achieve (and does cleanly) is a *conditional, certificate-ready tail criterion* whose interface is the single strict inequality (Theorem `thm:tail-inequality`, Eq. `tail-ineq`) plus a finite-height “front-end” discharge. The *architecture* is coherent post-pivot (UE depends on `E'/E`, HB depends on the residual `F'/F`, and local zeros are isolated into an explicit `N_loc` term), but **three items remain necessary for external audit readiness**, and **one additional critical item is now visible**:

### Critical remaining obligations (must be closed for a referee-grade v33)

1. **Residual envelope lemma completeness (critical)**: Lemma `lem:residual-envelope` is still a proof sketch; it must be expanded to a full proof (or replaced by a single primary theorem with hypotheses matching the paper’s strip/box geometry) yielding
   \(\sup_{\partial B}|F'/F|\le C_1\log m + C_2\) **uniformly in** \(\delta\) and \(\alpha\), and for both signs \(\pm\alpha\).

2. **Collar policy integration / monotonicity (major → critical if left informal)**: Definition `def:collar-admissible` asserts “shrink \(\delta\) until \(\kappa\)-admissible; all inequalities become easier.” This must be checked and *proved* against every appearance of \(\delta\) in the forcing, UE, HB, and tail inequality assembly.

3. **Operator / outer-factor citations pinned at theorem level (major)**: Lemma `lem:upper-envelope` uses boundedness of the boundary conjugation (Hilbert/Cauchy) operator on the square, and existence/properties of the outer factor `G_out`. v32 cites the right sources, but still needs a theorem-number mapping and a one-paragraph “how the cited theorem implies the exact operator bounds used here.”

4. **Tail inequality assembly constants (critical)**: Theorem `thm:tail-inequality` introduces **new absolute constants** `c_0`, `c`, and `K_alloc` and states “details unchanged from v31.” In v32, **the allocation/assembly step is not fully written** (and `K_alloc` differs dramatically from v31). For external audit, v33 must either:
   - provide a complete derivation of Eq. `tail-ineq` from Lemmas 3.2–3.6 (including where `c_0` and `K_alloc` come from), **or**
   - restate Theorem `thm:tail-inequality` with *clearly quantified* “there exists an absolute constant `K_alloc` …” and prove existence with an explicit bound.

If (1)–(4) are fully written, v32’s tail mechanism becomes genuinely “etched in stone,” and the only remaining non-analytic dependency is the finite-height computational front-end (which is already handled via Platt–Trudgian).

---

## 1. Global invariants (A1)

### 1.1 Precise target statement

- v32 states RH in canonical form: all nontrivial zeros of \(\zeta(s)\) satisfy \(\Re(s)=\tfrac12\). (Section 2.1.)
- v32’s *main deliverable* is not a direct unconditional proof but a **global criterion** (Theorem `thm:global`) that reduces RH to:
  - an analytic tail inequality holding for all heights above a small anchor, and
  - a verified finite-height front-end.

### 1.2 Strategy commitment

- v32’s committed strategy is a **band/box exclusion mechanism**: assume an off-axis quartet at a given height and derive a contradiction by comparing:
  - a *forcing* lower bound (short-side argument change),
  - an *upper envelope* control (how close the inner quotient can be to a constant), and
  - a *horizontal non-forcing budget* (residual phase variation along horizontal edges).

- The post-pivot commitment is: **UE must be stated in terms of** \(E'/E\), then split \(E'/E=F'/F+Z'/Z\) and bound residual vs local separately. This is implemented.

### 1.3 Trusted primitives (declared + actually used)

Used primitives (some need theorem-level pinning):

- Analytic continuation + functional equation of \(\xi(s)\); evenness \(E(-v)=E(v)\).
- Argument principle / winding number logic (implicit in forcing / band criterion).
- Inner–outer factorization on simply connected domains with Lipschitz boundary (square). Implemented via harmonic extension of \(\log|E|\) and a boundary conjugation operator.
- Boundedness of the Cauchy singular integral / Hilbert transform on Lipschitz curves (CMM).
- Riemann–von Mangoldt / zero counting in short windows (for \(N_{\rm loc}(m)\)).
- Finite-height verification of RH (Platt–Trudgian).

### 1.4 “Are we proving RH by accident?”

- v32 does **not** claim unconditional RH; it explicitly labels the analytic tail as conditional on several lemmas/constants.
- However: once (1)–(4) above are fully proven, the global theorem *would* assert unconditional RH in the tail + literature/certificate front-end. That is exactly why the missing steps must be treated as **high-stakes** and written with maximal conservatism.

### 1.5 Where the real difficulty lives

In the current v32 text, the true hard steps concentrate into:

- **Residual envelope**: proving a \(\delta\)-uniform, \(\alpha\)-uniform bound for \(\sup_{\partial B}|F'/F|\) after deleting zeros in a fixed ordinate window.
- **Assembly/allocation**: producing Eq. `tail-ineq` with explicit constants from the forcing/UE/HB ingredients without hidden assumptions.

These are the correct “hard lemmas.” If any part of the manuscript feels “too easy,” it is because these are currently only sketched.

---

## 2. Minimal dependency graph (A1: DAG check)

### 2.1 Definitions

- RH definition  → `\xi(s)` → width–2 variable `v` → `E(v)`.
- Boxes `B(\alpha,m,\delta)`.
- Local product `Z(m;v)` → residual `F=E/Z`.
- Outer factor `G_out` on a box → inner quotient `W=E/G_out`.
- Collar admissibility (`\kappa`-admissible).

### 2.2 Lemma chain

- Lemma `lem:short-side-forcing` (forcing).
- Lemma `lem:upper-envelope` (UE in terms of \(\sup|E'/E|\)).
- Lemma `lem:logder-split` + Lemma `lem:Zloc-logder-collar` + Lemma `lem:Nloc-logm` (convert \(\sup|E'/E|\) into residual+local ledger).
- Lemma `lem:horizontal-budget` (HB in terms of residual \(\sup|F'/F|\)).
- Theorem `thm:tail-inequality` (assembly).
- Lemma `lem:worst-alpha` + Lemma `lem:monotone-m` (reductions).
- Theorem `thm:tail-closure` (tail closure from one anchor height).
- Section 4 + Appendix `app:frontend` (finite-height discharge).
- Theorem `thm:global` (global conditional criterion).

### 2.3 Cycle / circularity check

No explicit logical cycles are present *provided* the collar policy is treated as a contour-selection convention (not an analytic hypothesis) and monotonicity under shrinking \(\delta\) is proven.

The only potential “hidden cycle” would be if the residual envelope lemma implicitly requires RH-strength information (it should not, but this must be validated in the full proof).

---

## 3. Section-by-section contract, dependencies, open risks (D1)

### Section 1 — Executive status

- **Contract:** States what is proved vs what is conditional; enumerates computational artifacts.
- **Dependencies:** none.
- **Open risks:** none; it is honest but should be kept synchronized with later constants (`K_alloc`, collar policy).

### Section 2 — Setup and reduction

- **Contract:** Defines the objects (`E`, boxes, local factor `Z`, residual `F`, collar admissibility) and states the proof goal: exclude off-axis quartets by a box/band criterion.
- **Dependencies:** basic properties of \(\xi\), symmetry \(E(-v)=E(v)\).
- **Open risks:**
  - Collar admissibility is stated as a “shrink \(\delta\)” policy without a lemma proving monotone safety.
  - The exact sense in which the criterion covers “all possible quartets” is implicit; v33 should add a short paragraph formalizing the reduction: “any off-axis quartet produces the two boxes used below.”

### Section 3 — Band criterion

#### 3.1 Short-side forcing (Lemma `lem:short-side-forcing`)

- **Contract:** Gives explicit argument increment of the local pair factor along the central vertical segment `I_+`.
- **Dependencies:** elementary geometry of arguments.
- **Open risks:** clarify how this segment-based forcing enters the global “band” argument (in the assembly step).

#### 3.2 Upper envelope (Lemma `lem:upper-envelope`)

- **Contract:** Bounds \(|W(v_0)-e^{i\varphi_0}|\) at the dial point by \(\delta^{3/2}\sup_{\partial B}|E'/E|\) with a shape-only constant.
- **Dependencies:**
  - harmonic measure / Poisson kernel boundedness at the center of a square,
  - Poincaré/Wirtinger on a loop,
  - outer factor boundary conjugation identity and boundedness of the conjugation operator.
- **Open risks:** theorem-level citation mapping (CMM + Hardy-space outer factor machinery).

#### 3.2 Local split (Lemmas `lem:logder-split`, `lem:Nloc-logm`, `lem:Zloc-logder-collar`)

- **Contract:** Makes local-zero contribution explicit and bounded by `N_loc/(\kappa\delta)` under collar admissibility.
- **Dependencies:** short-window zero count \(N_{\rm loc}(m)\ll\log m\).
- **Open risks:** must prove collar monotonicity and ensure `Z(m;v)` window is aligned with the box geometry (currently OK since \(\delta\le 1/10\)).

#### 3.3 Horizontal budget (Definition `def:Delta-nonforce`, Lemma `lem:horizontal-budget`)

- **Contract:** Defines non-forcing horizontal phase budget using the residual `F` and bounds it by `4δ sup|F'/F|`.
- **Dependencies:** only that `F` is zero-free on a neighborhood of \(\partial B\).
- **Open risks:** none (this part is “audit-grade”).

#### 3.4 Allocation + tail inequality (Theorem `thm:tail-inequality`)

- **Contract:** Provides the single inequality interface `tail-ineq` such that if it holds, no off-axis quartet exists at that height.
- **Dependencies:** forcing + UE + HB + a comparison/assembly argument.
- **Open risks (critical):**
  - the **assembly argument is still schematic** (“details unchanged from v31”),
  - the provenance and correctness of `c_0`, `c`, and especially `K_alloc` are not spelled out,
  - `K_alloc` differs from v31, so v33 must either justify the new value or treat `K_alloc` as an existential constant.

#### 3.5 Reductions (Lemma `lem:worst-alpha`, Lemma `lem:monotone-m`)

- **Contract:** Reduces the inequality checking to \(\alpha=1\) and to the anchor height \(m=m_*\) (monotonicity in `m`).
- **Dependencies:** calculus monotonicity of explicit functions of \(m\).
- **Open risks:** provide explicit derivative checks (currently stated tersely).

#### 3.6 Tail closure and global criterion (Theorems `thm:tail-closure`, `thm:global`)

- **Contract:** If the inequality holds at the anchor, it holds for all \(m\ge m_*\), and combined with front-end yields a global RH criterion.
- **Dependencies:** reductions, plus the finite-height front-end.
- **Open risks:** statement is conditional on analytic inputs; ensure the list of assumptions exactly matches what is used (especially collar and residual envelope).

### Section 4 — Finite-height front-end

- **Contract:** Discharges \(\Im(s)\le 5\) via Platt–Trudgian.
- **Dependencies:** mapping between \(m\) and \(\gamma\), and the cited computational theorem.
- **Open risks:** editorial: text says “In v31 we take \(m_*=10\)” — should be “In this manuscript / v32.”

### Section 5 + Appendices — Reproducibility

- **Contract:** Specifies how to reproduce the tail certificate and records SHA256.
- **Dependencies:** Python + `mpmath` + included scripts.
- **Open risks:** editorial mismatch in Section 5: the command block references `v31_repro_pack/...` even though v32 ships `v32_repro_pack/...`.

---

## 4. Definition register (B1: Defined / Used / Needed)

Below: **Object** — *Defined at* — *Used at* — *Needed because*

- **RH** — §2.1 — Theorem `thm:global` — target statement.
- **\(\xi(s)\)** — §2.1 — definition of `E` — entire completion, symmetry.
- **Width–2 variables** `u=2s`, `v=u-1` — §2.1 — throughout — keeps symmetry and scaling simple.
- **\(E(v)=\xi((1+v)/2)\)** — §2.1 — all analytic lemmas — entire even function with zeta zeros.
- **Zero parametrization** `ρ=a+im` — §2.1 — forcing/box placement — converts quartet to ±a boxes.
- **Box** `B(α,m,δ)` — Def. `def:box` — all band arguments — localizes the analysis.
- **Outer factor** `G_out` — §2.2 — UE lemma — provides inner quotient with unimodular boundary.
- **Inner quotient** `W=E/G_out` — §2.2 — UE lemma, tail inequality — object whose dial evaluation is controlled.
- **Local factor** `Z(m;v)` — Def. `def:zloc` — residual split, collar lemma — removes zeros near the working height.
- **Residual** `F=E/Z` — Def. `def:zloc` — HB + residual envelope lemma — isolates “smooth” part.
- **Collar admissibility** `dist(∂B,Z(E)) ≥ κδ` — Def. `def:collar-admissible` — local term bound — prevents boundary-near poles in `Z'/Z`.
- **Local zero count** `N_loc(m)` — Def. `def:Nloc` — local term in tail inequality — quantifies remaining local contribution.
- **Residual envelope** `L(m)=C_1 log m + C_2` — Lemma `lem:residual-envelope` — UE/HB closure — supplies uniform log-derivative control.
- **Horizontal budget** `Δ_nonforce(B)` — Def. `def:Delta-nonforce` — tail inequality — controls horizontal phase variation.
- **Allocation constants** `c_0,c,K_alloc` — Theorem `thm:tail-inequality` — tail inequality — convert forcing into the inequality ledger.

---

## 5. Lemma register (core/supporting/cosmetic)

### Core (blockers if incomplete)

- Lemma `lem:residual-envelope` (residual log-derivative envelope) — **core**.
- Theorem `thm:tail-inequality` (tail inequality assembly) — **core**.
- Theorem `thm:tail-closure` (tail closure) — **core**.
- Theorem `thm:global` (global criterion) — **core**.

### Supporting (important, but classical / readily patched)

- Lemma `lem:upper-envelope` (UE in terms of \(E'/E\)).
- Lemma `lem:short-side-forcing` (forcing geometry).
- Lemma `lem:Zloc-logder-collar` (local term under collar).
- Lemma `lem:Nloc-logm` (short window zero count).
- Lemma `lem:horizontal-budget` (HB residual form).
- Lemma `lem:worst-alpha` and `lem:monotone-m` (reductions).

### Cosmetic / editorial

- Section 4 and Section 5 text consistency (“v31” wording, repro path).

---

## 6. Gap register (D1 + C1 stress tests)

Each entry: **Gap** — *Type* — *Severity* — *Fix path*

### G1. Residual envelope lemma is only a sketch

- **Type:** missing proof / uniformity
- **Severity:** **critical**
- **Fix path:** Expand Lemma `lem:residual-envelope` into a full proof with explicit steps:
  1) write \(\xi'/\xi\) (or \(E'/E\)) as gamma/log term + sum over zeros using a convergent partial-fraction expansion;
  2) subtract local zeros in \(|\Im \rho-m|\le 1\) to obtain \(F'/F\);
  3) bound remaining zero-sum using (i) a unit-window counting bound and (ii) a dyadic decomposition in \(|\gamma-m|\); show the sum is \(O(\log m)\) uniformly for \(\Re(v)\in[-1,1]\) and \(|\Im(v)-m|\le\delta\);
  4) bound gamma term via Stirling for \(\psi\) on the corresponding strip.

A v33-ready proof should explicitly track that **no step introduces a \(1/\delta\)**.

### G2. Collar policy monotonicity not proven globally

- **Type:** hidden hypothesis / monotonicity under parameter change
- **Severity:** **major** (becomes **critical** if used without proof)
- **Fix path:** Add a lemma: “All terms in Eq. `tail-ineq` are monotone in \(\delta\) in the direction needed.” Then restate the collar policy as:

  - define \(\delta_{\max}=\eta\alpha/(\log m)^2\);
  - choose any \(\delta\in(0,\delta_{\max}]\) that is \(\kappa\)-admissible;
  - prove that if `tail-ineq` holds at \(\delta_{\max}\), then it holds for any smaller admissible \(\delta\).

This avoids any suggestion that \(\delta\) must remain exactly equal to \(\eta\alpha/(\log m)^2\) after shrinking.

### G3. Boundary conjugation operator and outer factor machinery not pinned at theorem-level

- **Type:** reference precision / operator definition
- **Severity:** major
- **Fix path:** Add a short subsection/appendix:

  - define \(H_{\partial Q}\) precisely (principal value Cauchy integral, boundary limits);
  - cite **CMM (Annals 1982)** with theorem statement (or a clean modern restatement) and specify: square boundary is Lipschitz, so \(\|H_{\partial Q}\|_{2\to2}<\infty\);
  - cite a Hardy-space/outer-function reference for existence of \(G_{\rm out}\) on a Lipschitz Jordan domain with boundary data \(\log|E|\), and for the identity relating boundary conjugation to \(\arg G_{\rm out}\).

### G4. Tail inequality assembly / allocation constants not derived in v32

- **Type:** missing derivation / cross-version drift
- **Severity:** **critical**
- **Fix path:** v33 must either:

  **Option A (preferred):** Write a complete proof of Theorem `thm:tail-inequality`, step-by-step, showing how forcing (Lemma `lem:short-side-forcing`) minus non-forcing (HB + UE deviations) yields Eq. `tail-ineq`, and derive explicit constants.

  **Option B:** Replace `K_alloc=1/4` by “there exists an absolute constant `K_alloc>0`” and prove such a constant exists (with any explicit upper bound). Do the same for the specific `c_0` lower bound if it is not fully justified in-text.

Additionally: reconcile with v31’s value `K_alloc=3+8\sqrt3` or explicitly state why the definition changed.

### G5. Minor reproducibility/editorial mismatches

- **Type:** manuscript↔code mismatch
- **Severity:** minor
- **Fix path:**
  - Section 4: replace “In v31 we take \(m_*=10\)” with v32 wording.
  - Section 5: update the command snippet to use `v32_repro_pack/v32_generate_tail_certificate.py` and `v32_constants_m10.json`.

### G6. Sign coverage of residual bounds

- **Type:** domain coverage
- **Severity:** minor→major depending on how residual lemma is proved
- **Fix path:** ensure Lemma `lem:residual-envelope` is stated for both boxes `B(\pm\alpha,m,\delta)` (or for \(|\Re(v)|\le 1\)) so the symmetric box is covered without an implicit appeal to evenness.

---

## 7. Computational verification status (what is actually certified)

### 7.1 What was executed (local run)

From the shipped `v32_repro_pack.zip`, running `bash verify_all.sh`:

- regenerates the interval certificate `v32_tail_certificate_m10.json`,
- verifies the strict inequality `LHS_hi < RHS_lo` across the chosen parameter band,
- checks SHA256 against `sha256sums.txt`.

### 7.2 What the certificate *does and does not* certify

- It certifies *only the numerical inequality check* for the parameter band and the constants provided in `v32_constants_m10.json`.
- It does **not** certify the analytic inputs (residual envelope lemma, boundedness of the conjugation operator, etc.). Those remain “math proofs,” not “compute proofs.”

---

## 8. Stress-test summary (C1)

### Domain stress tests

- All log-derivatives are only used where the relevant function is nonzero on the contour; v32 addresses this by boundary-contact and then strengthens it to collar admissibility.
- No use of Dirichlet series beyond its region; v32 uses completed \(\xi\) object.

### Uniformity stress tests

- **Main risk remains**: residual envelope must be proven uniformly in \(\delta\) and \(\alpha\). Nothing else appears to introduce hidden \(\delta^{-p}\) growth.

### Branch stress tests

- UE proof uses only derivatives of logs; branch constants drop out.

### “Equivalent to RH” landmine test

- The residual envelope lemma as stated *should* be unconditional (classical), but this must be confirmed in the full proof: ensure it does not smuggle in RH via a bound on \(S(t)\) stronger than known unconditional estimates.

---

## 9. Updated go/no-go statement

- **Go** for a v33 plan whose purpose is to make v32 externally audit-ready.
- **No-go** for claiming “unconditional closure achieved” until G1–G4 are closed.

If v33 completes G1–G4 cleanly, then the manuscript’s logical progression is positioned to support an unconditional tail closure (with a computational front-end), subject to standard community scrutiny.
