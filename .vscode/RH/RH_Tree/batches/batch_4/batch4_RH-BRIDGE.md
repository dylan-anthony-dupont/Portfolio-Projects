# RH Convergence Program — Batch 4 (Decision Batch)
## Callsign: RH-BRIDGE
## Ground truth: v34 (`manuscript_v34.pdf`)
## Owned scope: Bridge-1 hypotheses, boundary modulus meaning, outer/inner factor logic, boundary-vs-interior inference integrity.

### Artifacts consulted (surgical)
- **v34 PDF**: Bridge section (Lemma 9.1 / Prop 9.2 / Remark 9.3), collar section (Def 10.5 / Lemmas 10.6–10.8), UE/local-term diagnostics (Remark 10.11), tail criterion statement (Theorem 11.1), and “entire/meromorphic” occurrences (Lemma 6.1).【690:10†manuscript_v34.pdf†L28-L58】【690:3†manuscript_v34.pdf†L64-L74】【690:1†manuscript_v34.pdf†L1-L72】【690:9†manuscript_v34.pdf†L24-L71】【690:11†manuscript_v34.pdf†L24-L104】【690:14†manuscript_v34.pdf†L23-L41】

No other files were needed for this batch decision.

---

## PRIMARY TASK 1 — Boundary issue forensic: what EXACTLY the collar is fixing

### 1.1 Failure mode **without** collar-admissibility (what breaks, precisely)

**(F1) Dirichlet outer factor fails as stated (or becomes weaker than needed).**  
Bridge-1 (Lemma 9.1) explicitly assumes **boundary-contact**: `E ≠ 0 on ∂B`, so that `log|E| ∈ C(∂B)` and the classical Dirichlet solution is **continuous on the closed box**.【690:10†manuscript_v34.pdf†L28-L58】  
If `E` has a boundary zero (or boundary pole), then `log|E|` is not continuous on `∂B`, and the stated Dirichlet/continuity conclusion in Lemma 9.1 is no longer justified in the v34 form. That breaks the “pointwise boundary modulus” meaning of `|W|=1` relied on downstream.

**(F2) The UE chain becomes undefined/meaningless at the exact point it needs to be pointwise.**  
The UE step in v34 produces a **pointwise** upper-envelope of the form `δ · sup_{∂B} |E'/E|` (Lemma 10.3 and its corollary form). But `E'/E` is meromorphic and **blows up** at boundary zeros; hence `sup_{∂B} |E'/E|` is infinite if `E` vanishes on `∂B`. The upper-envelope line is then vacuous/false as a numerical bound.

**(F3) The log-derivative decomposition and the local-term bound fail at the boundary.**  
v34 explicitly states the decomposition is valid only where `E` and `Z_loc` are holomorphic and **nonvanishing** (in particular on `∂B` “under the boundary-contact convention”).【690:1†manuscript_v34.pdf†L38-L72】  
If boundary zeros are allowed, the split `E'/E = F'/F + Z_loc'/Z_loc` is not pointwise meaningful on `∂B`, and the collar bound on `Z_loc'/Z_loc` cannot be applied.

**(F4) Argument/phase objects lose meaning at the boundary.**  
Any step that tracks `arg` (forcing/non-forcing budgets, phase continuity, etc.) requires that the relevant boundary traces never hit 0 (so that arg can be selected continuously). If boundary zeros are possible, phase jump singularities appear exactly at those points.

### 1.2 What the collar **actually provides** in v34

v34’s collar-admissibility is the quantified separation condition
\[
\mathrm{dist}(\partial B, Z(E)) \ge \kappa \delta,
\]
introduced in **Definition 10.5**【690:3†manuscript_v34.pdf†L64-L74】 and guaranteed achievable (by shrinking δ) in **Lemma 10.6**【690:3†manuscript_v34.pdf†L75-L99】.

This does three distinct jobs:

1. **Discharges Bridge-1’s boundary-contact hypothesis** (`E ≠ 0 on ∂B`) automatically.  
   If `dist(∂B, Z(E)) ≥ κδ`, then in particular there are no zeros on `∂B`.

2. **Gives a zero-free collar neighborhood around the boundary** (quantitative).  
   Not just “no boundary zeros,” but “no zeros within κδ of the boundary,” which is what makes pointwise log-derivative controls possible in sup norm.

3. **Enables the explicit local-term bound**  
   \[
   \sup_{\partial B} \left|\frac{Z'_{\rm loc}}{Z_{\rm loc}}\right| \le \frac{N_{\rm loc}(m)}{\kappa\,\delta},
   \]
   stated as Lemma 10.8 in v34.【690:1†manuscript_v34.pdf†L53-L72】  
   This is exactly the quantitative step that later drives the UE/local obstruction under `p=1`.

### 1.3 What the collar does **not** fix (important for misuse prevention)

The collar is a **boundary-contact / boundary-regularity** device. It does **not** rule out interior zeros. In Bridge-1 terms: outer factorization always yields an inner quotient `W = E/G_out` with boundary modulus 1, but the interior zeros of `E` are precisely the “inner content.” Proposition 9.2 only collapses `W` to a constant **if `W` is assumed zero-free in the interior** (equivalently, `E` zero-free in the box interior).【685:5†manuscript_v34.pdf†L45-L65】

So the collar is not a substitute for the **“W has no inner factor”** step; it only makes the boundary objects well-defined and quantitative.

---

## PRIMARY TASK 1 — Is there an alternative standard technique that avoids the collar (and stays honest)?

Below are the only alternatives that are genuinely “standard” and referee-recognizable. None is a free replacement; each trades the collar for a different obligation.

### Alternative A (standard, but re-introduces a “certificate” style): **Rouché boundary inequality**

If one can exhibit a holomorphic, zero-free comparator `g` on a neighborhood of `\overline B` and prove
\[
|E-g|<|g|\quad\text{on }\partial B,
\]
then Rouché implies `E` has the same number of zeros as `g` in `B` (hence zero-free), and it also forces `E ≠ 0` on `∂B` automatically (since `|E-g|<|g|` implies `E` cannot vanish on the boundary). This route avoids “shrink-to-avoid-zeros” entirely.

**Cost:** you now owe a *comparand* and a *uniform boundary inequality*—which is exactly the “explicit certificate” posture v33→v34 pivoted away from.

### Alternative B (Hardy/Smirnov outer factor with a.e. boundary values): **drop pointwise boundary modulus**

One can define outer factors under `\log|E|\in L^1(∂B)` and obtain `|W|=1` **a.e.** as boundary nontangential limits (Hardy space technology). This can tolerate isolated boundary zeros.

**But:** then **Bridge-1 constancy is no longer valid from zero-free alone** because *singular inner functions* exist: zero-free, nonconstant inner functions with `|W|=1` a.e. (in the disk, and likewise on Jordan domains via conformal transport). So this path introduces a new, hard obligation: exclude singular inner factors by proving additional boundary regularity (often amounting to restoring continuity anyway).

### Alternative C (“fattened contour” selection): **average-over-contours instead of pointwise sup**

One can consider a 1-parameter family of contours parallel to `∂B` and select a contour where boundary values avoid zeros (a “good contour”). This is a classical trick in argument principle contexts.

**But:** v34’s UE step is *pointwise* and uses `sup_{∂B} |E'/E|`, not an average over contours. Without redesigning the UE endpoint functional, this alternative does not remove the key quantitative blow-up mechanism.

**Conclusion on alternatives:** the collar is the cleanest deterministic discharge of **pointwise** boundary-contact/regularity in v34. You can avoid it only by (i) restoring an explicit Rouché certificate posture, or (ii) weakening boundary statements to a.e. and paying for a singular-inner exclusion lemma, or (iii) redesigning UE away from pointwise sup.

---

## PRIMARY TASK 2 — “Outer/Rouché inner-vs-outer phenomenon” sanity check
### Chosen option: **(B) Proof-grade NO-GO lemma** (be decisive)

#### NO-GO LEMMA (directional limitation)
**Claim.** In the v34 Bridge setting, the data  
- `E` holomorphic on a neighborhood of `\overline B`, `E ≠ 0` on `∂B`,  
- outer factor `G_out` constructed from `\log|E|` as in Lemma 9.1, hence `|W|=1` on `∂B` for `W:=E/G_out`,  

**does not imply** that `W` is zero-free on `B°`, nor that `W` is constant. In fact, interior zeros are completely unconstrained by this boundary modulus identity: they can be prescribed arbitrarily (finite multisets) while keeping `|W|=1` pointwise on `∂B` and keeping boundary-contact.

#### Proof (referee-grade construction; sketch but standard)
Let `B°` be the interior of the rectangle, a simply connected Jordan domain. By the Riemann mapping theorem and Carathéodory’s theorem, there exists a conformal map  
\[
\phi:\mathbb{D}\to B°
\]
that extends continuously to a homeomorphism `\overline{\mathbb{D}}\to\overline{B}`.

Fix any finite multiset of points `{ρ_j} ⊂ B°`. Let `{a_j} ⊂ \mathbb{D}` be their preimages: `a_j := \phi^{-1}(ρ_j)`. Define a finite Blaschke product
\[
\mathcal{B}(z) := e^{i\theta}\prod_j \frac{z-a_j}{1-\overline{a_j}\,z}.
\]
Then `\mathcal{B}` is holomorphic on `\overline{\mathbb{D}}`, has `|\mathcal{B}(e^{it})|=1` for all boundary points, and its zeros in `\mathbb{D}` are exactly the `{a_j}` (with multiplicity). Transport to the box by defining the “inner factor on B”
\[
W(v) := \mathcal{B}(\phi^{-1}(v)).
\]
Then `W` is holomorphic on `B°`, extends continuously to `\overline B`, satisfies `|W|=1` pointwise on `∂B`, and has zeros exactly at `{ρ_j}`.

Now pick any zero-free holomorphic `G_out` on `B°` that extends continuously to `\overline B` (e.g. `G_out≡1`, or the actual `G_out` from a chosen boundary modulus). Define
\[
E(v):=W(v)\,G_out(v).
\]
Then `E` is holomorphic on `B°` and continuous on `\overline B`, is nonzero on `∂B` (since `|W|=1` and `G_out` is nonzero there), and its outer factor derived from `\log|E|=\log|G_out|` is exactly `G_out` (up to unimodular constant). Therefore the Bridge quotient is the constructed nonconstant `W`, with prescribed zeros.

This shows: **outer factorization + boundary modulus gives no control over interior zeros**. Any implication of the form “no zeros outside ⇒ no zeros inside ⇒ no boundary zeros” cannot be obtained from the Bridge data alone; you need a separate mechanism (Rouché inequality, forcing-vs-envelope, or an argument principle bound) to rule out inner factors.

#### Consequence for v34 narrative
- Proposition 9.2 is correctly one-directional: **(zero-free W)** ⇒ **(W constant)**. The converse is false in the strongest possible way; boundary modulus does not even constrain the existence of zeros, let alone exclude them.【685:5†manuscript_v34.pdf†L45-L65】  
- Therefore, any prose that suggests the collar/outer factor “pushes zeros out” must be tightened: zeros are “moved into W,” not eliminated.

---

## PRIMARY TASK 3 — ENTIRE / MEROMORPHIC hygiene (Λ₂ / E)

### 3.1 Current v34 state (what is correct / what is not)

- v34 still contains multiple places that treat **`E` as entire**, e.g. Lemma 6.1 proof (“Since `E` is entire…”)【690:14†manuscript_v34.pdf†L35-L41】 and Lemma 10.6 proof (“Zeros of the entire function `E` are isolated.”)【690:3†manuscript_v34.pdf†L93-L99】.
- However, the width–2 “completed” object `Λ₂(u)=π^{-u/4}Γ(u/4)ζ(u/2)` is classically **meromorphic**, with poles inherited from ζ at `u=2` (and from Γ at `u=0`, unless cancelled by an explicit polynomial factor). Unless v34 has introduced a hidden `(u)(u-2)` factor earlier, the statement “Λ₂ is entire” is not literally true.

**Bridge impact:** Bridge-1 itself is safe because it assumes only that `E` is holomorphic on a neighborhood of `\overline B` (Lemma 9.1), and the v34 program works at heights `m≥10`, so the boxes are far from the real-axis poles.【690:10†manuscript_v34.pdf†L32-L58】【690:11†manuscript_v34.pdf†L24-L28】

### 3.2 Minimal fix required for referee safety (recommended)

There are two clean ways to patch, in increasing order of surgicalness:

**Fix (i) Minimal textual hygiene (recommended for v34/v35):**  
Keep `E(v)=Λ₂(1+v)` as the working object but **stop calling it “entire.”** Replace “entire” with “holomorphic on a neighborhood of the region of interest,” and explicitly note that all boxes used lie in such a region (because `m≥10`).

**Fix (ii) Notation-level cleanup (stronger but larger change):**  
Redefine the completed object as the standard entire xi-function (width–2):
\[
\Xi_2(u):=\frac{u(u-2)}{8}\,\Lambda_2(u)=\xi(u/2),
\]
and set `E(v):=\Xi_2(1+v)`. This makes `E` genuinely entire and eliminates the pole discussion, at the cost of adding a trivial rational log-derivative correction in `E'/E` (small at large `m`).

For “Bridge-side correctness,” Fix (i) is sufficient.

---

## SECONDARY TASK — Bridge-compatibility lemma for future redesign (UE endpoint functional)

Batch-4 asks for a Bridge-side lemma usable if ENVELOPE redesigns UE away from sup norms.

### Lemma (boundary L¹ control of the local log-derivative; collar-friendly)
Let `B=B(α,m,δ)` be κ-admissible, and let `Z_loc(v)=∏_{ρ∈Z(m)}(v-ρ)^{m_ρ}`. Then for each zero ρ with `dist(ρ,∂B) ≥ κδ`,
\[
\int_{\partial B}\frac{|dv|}{|v-\rho|} \;\le\; C\,\log\frac{1}{\kappa}
\]
for an absolute constant `C`, hence
\[
\int_{\partial B}\left|\frac{Z'_{\rm loc}(v)}{Z_{\rm loc}(v)}\right|\,|dv|
\;\le\; C\,N_{\rm loc}(m)\,\log\frac{1}{\kappa}.
\]
**Interpretation:** the *L¹ boundary size* of the local term can be bounded with **no δ^{-1} blow-up**, provided κ-admissibility holds. This is the exact kind of estimate that becomes usable if UE is redesigned to feed on boundary integrals (or L¹/L² norms) rather than `sup_{∂B}`.

This lemma is consistent with v34’s obstruction diagnosis: the δ^{-1} comes from the **sup** bound in Lemma 10.8, not from the existence of the collar itself.【690:9†manuscript_v34.pdf†L63-L71】

*(I am not patching UE here; I’m supplying the Bridge-side inequality that would support a future UE redesign.)*

### Branch/continuation notes for redesigned functionals
- Outer factor construction only uses `\log|E|` (no branch choices) and requires `E ≠ 0` on `∂B` for continuity in the v34 Dirichlet setup.【690:10†manuscript_v34.pdf†L32-L58】
- Any step that introduces `\log E` (not just `\log|E|`) must additionally assume `E` zero-free in `B°` (equivalently `W` zero-free), since otherwise a single-valued analytic log does not exist.

---

## DECISIVE VERDICT — Is the collar “right tech” or a detour that forces log m obstruction?

### Verdict (truth-grade)
**The collar is necessary for the Bridge/boundary program as currently written, but its *quantified* use together with the pointwise UE endpoint is structurally what produces the log m obstruction.**

- **Necessary (for correctness):** Without collar-admissibility (or an equivalent boundary-contact guarantee), the Dirichlet outer factor lemma and the pointwise meaning of `|W|=1` are not robust, and the UE step `δ·sup_{∂B}|E'/E|` can be undefined/infinite. v34 explicitly uses κ-admissibility to guarantee this boundary-contact regime exists for δ≤δ0.【690:3†manuscript_v34.pdf†L64-L74】【690:3†manuscript_v34.pdf†L75-L99】  
- **Structurally blocking (for η-absorption under proven p=1):** Once UE is only `p=1`, the collar produces a δ-inert local term `(2C_up/κ)N_loc(m)` that does not shrink with δ, and grows like `~log m` under the unconditional majorant. This is stated explicitly in Remark 10.11 and in the executive proof status block.【690:9†manuscript_v34.pdf†L41-L71】【690:4†manuscript_v34.pdf†L14-L25】

**Therefore:**
- Collar is not a “detour” from a correctness perspective—it is the mechanism that prevents Bridge-1 from being referee-attacked on boundary regularity.
- But **the specific collar-to-sup bound pipeline is the quantitative bottleneck** that forces the log m obstruction under p=1. Long-term compatibility requires either (i) a UE mechanism with `p>1`, or (ii) a redesign that avoids feeding a δ^{-1} local bound into a pointwise evaluation step (e.g., by switching to an integrated boundary functional).【690:9†manuscript_v34.pdf†L41-L71】

---

# MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* Callsign: RH-BRIDGE
* Result classification: **CONDITIONAL**
* Target gaps closed (by ID): **G-6 (Bridge-1 hypothesis hygiene) — maintained; strengthened with explicit NO-GO directional warning.**
* Target gaps still open (by ID): **UE-Gate / local-term suppression (owned by ENVELOPE/UE branches, not Bridge).**

* Key conclusions (≤5 bullets):
  1. κ-admissibility is the exact mechanism discharging Bridge-1’s boundary-contact hypothesis (`E≠0` on `∂B`) and making “|W|=1 on ∂B” unambiguous/pointwise.  
  2. The collar’s quantitative separation is what enables the sup-bound `sup_{∂B}|Z'_{\rm loc}/Z_{\rm loc}| ≤ N_{\rm loc}/(κδ)`, and under UE exponent `p=1` this yields a δ-inert local term that blocks absorption.  
  3. Outer factorization + boundary modulus does **not** constrain interior zeros: the “inner quotient” can encode arbitrary prescribed interior zeros while keeping `|W|=1` pointwise on the boundary (NO-GO lemma).  
  4. v34 still has “E is entire” statements that are unsafe unless `Λ₂` was silently replaced by an entire completion; minimum fix is to replace “entire” with “holomorphic on a neighborhood of the relevant boxes (m≥10)”.  
  5. A future UE redesign could exploit L¹ (or other integral) boundary control of `Z'_{\rm loc}/Z_{\rm loc}` to avoid δ^{-1} blow-up; Bridge can support such a redesign with a collar-friendly integral bound.

* Paste-ready manuscript edits:
  (i) revised lemma/proposition statements
  ```tex
  % --- after Remark 9.3 (Meaning of boundary modulus) add:
  \begin{remark}[No converse: boundary modulus does not exclude interior zeros]
  Lemma~\ref{lem:outer_dirichlet_box} implies that for any box $B$ satisfying boundary-contact,
  the quotient $W:=E/G_{\rm out}$ has $|W|=1$ on $\partial B$ (in the pointwise boundary-limit
  sense of Remark~\ref{rem:boundary_modulus}).
  This condition alone does \emph{not} imply that $W$ is zero-free or constant on $B^\circ$:
  nonconstant holomorphic functions on $B^\circ$ can have $|W|=1$ on $\partial B$ and still
  possess arbitrarily prescribed interior zeros (e.g. via conformal transport of finite Blaschke
  products). Thus Proposition~\ref{prop:bridge1} is strictly one-directional: the additional
  hypothesis ``$W$ is zero-free on $B^\circ$'' is essential.
  \end{remark}
  ```

  (ii) revised definitions/remarks
  ```tex
  % --- in Section 9 opening paragraph (Bridge 1), replace:
  % "Assume the boundary-contact convention: E has no zeros on ∂B."
  % with:
  Assume boundary-contact: $E\neq 0$ on $\partial B$.
  (This is enforced later by $\kappa$--admissibility; see Definition~10.5 and Lemma~10.6.)
  ```

  ```tex
  % --- in Section 6 / Lemma 6.1 proof, replace the sentence
  % "Since E is entire and its zeros are discrete, ..."
  % with:
  Since $E$ is holomorphic on a neighborhood of the compact set
  $\{|\Im v-m|\le 1\}\cap\{|\Re v|\le 1\}$ (for $m\ge 10$ this region is far from the poles of the
  meromorphic completion), its zeros in this compact set are discrete and hence finite.
  ```

  ```tex
  % --- in Lemma 10.6 proof, replace "Zeros of the entire function E are isolated."
  % with:
  Zeros of holomorphic functions are isolated. In our application $E$ is holomorphic on a
  neighborhood of the relevant closed box, so $Z(E)$ is discrete there.
  ```

  ```tex
  % --- in the width--2 normalization, replace any occurrence of "Λ_2 is entire" with:
  The completion $\Lambda_2(u)=\pi^{-u/4}\Gamma(u/4)\zeta(u/2)$ is meromorphic (with poles at
  $u=0,2$). Throughout Part~II we work at heights $m\ge 10$, so $E(v):=\Lambda_2(1+v)$ is
  holomorphic on a neighborhood of every box $B(\alpha,m,\delta)$ used in the boundary program.
  % (Optionally: define the entire completion Xi_2(u):=u(u-2)\Lambda_2(u)/8.)
  ```

  (iii) revised theorem/inequality lines
  ```tex
  % No inequality-line edits required for Bridge correctness in v34.
  % (UE/local-term redesign is out of RH-BRIDGE scope; see ENVELOPE branch.)
  ```

* Dependencies on other branches:
  - **ENVELOPE / UE branches:** any move away from the pointwise sup endpoint (to exploit the L¹ local-term bound) is a UE redesign; Bridge can supply collar-friendly integral inequalities but does not own the envelope proof.
  - **CONTROL ROOM / main editor:** decide whether to adopt the minimal “meromorphic hygiene” patch or the stronger “switch to xi/Ξ₂” patch; Bridge analysis supports either.

* Referee risk notes (anticipated objections + how addressed):
  1. **“Λ₂ is not entire” objection:** addressed by patching claims of “entire” to “holomorphic on neighborhood of boxes” (or by redefining the completion as Ξ₂).  
  2. **“Boundary modulus meaning ambiguous (a.e. vs pointwise)” objection:** v34 already chooses the pointwise boundary-limit convention; collar-admissibility enforces the required continuity regime; the added cross-reference makes this explicit.  
  3. **“Bridge-1 used as if it implies zero-freeness” objection:** addressed by inserting the NO-CONVERSE remark, preventing direction drift.  
  4. **“κ-admissible shrink assumes entire/discrete zeros globally” objection:** patched by restricting to holomorphic-on-neighborhood hypotheses (what is actually used).
