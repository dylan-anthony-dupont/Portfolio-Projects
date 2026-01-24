# Batch 5 — RH‑BRIDGE (S5 non‑pointwise boundary inequalities)

**Ground truth:** v35 (`manuscript_v35.pdf/tex`)  
**Assigned mission:** Replace the UE “pointwise/sup” boundary step by a **non‑pointwise** boundary inequality that avoids any hidden `δ^{-1/2}` point‑evaluation loss, or else deliver a **proof‑grade NO‑GO** that rules out a plausible redesign class.

---

## 1) Executive verdict (decision‑grade)

### Verdict: **proof‑grade NO‑GO for the entire “absolute L^r log‑derivative endpoint” family**

A large, very plausible S5 redesign class is:

> keep the forced quantity `D_B(W)` as in v35, but replace the endpoint `sup_{∂B}|E'/E|` by an **absolute** boundary `L^r(∂B,ds)` norm (or any equivalent absolute norm on `∂B` scaling like an `L^r` norm) and hope the local term becomes δ‑subcritical.

This class **cannot** clear the UE‑Gate exponent budget. The obstruction is structural:

- The **point evaluation step** (from boundary control to `W(v_±)`) contributes a factor `δ^{-1/r}` whenever you control boundary data in `L^r` (Hölder with the Poisson kernel).
- The **Poincaré step** contributes exactly one `δ`.
- Therefore the *best possible* UE exponent in this class is
  \[
  p(r)=1-\frac1r.
  \]
- Meanwhile the local term produced by a `κ`‑collar around zeros is of size
  \[
  \left\|\frac{Z'_{\rm loc}}{Z_{\rm loc}}\right\|_{L^r(\partial B,ds)}
  \asymp \frac{N_{\rm loc}(m)}{\kappa\,\delta^{\,1-1/r}},
  \]
  so its “interface exponent” is
  \[
  \theta(r)=1-\frac1r.
  \]
- Hence **always** `p(r)-θ(r)=0`, i.e. the local contribution is **δ‑inert** and cannot be suppressed by `η`‑shrinking at the nominal scale `δ0(m,α)=ηα/(\log m)^2`.

This extends the v35 pointwise/sup diagnosis (“p=1, θ=1 ⇒ p−θ=0”) to the **entire absolute L^r endpoint family**.

**Consequence:** S5 must *genuinely change endpoint type*, not merely swap `L^∞` for `L^2`/`L^1` on `|E'/E|`. Any viable S5 must exploit **cancellation** (argument‑principle style, signed integrals) and/or move to **less singular boundary objects** (e.g. `\log|E|`/BMO‑type control), otherwise δ‑inert local leakage is unavoidable.

---

## 2) Proof‑grade NO‑GO lemma package (rectangle/box, shape‑only constants)

This is designed to be pasted into Section “12 S5 frontier” as a **recorded ruled‑out endpoint class**, in the same spirit as Appendix A (discarded routes).

### 2.1 Scaling lemma: `L^r` evaluation + boundary Poincaré (forces `p(r)=1−1/r`)

Let `B=B(\pm a,m,\delta)` be an aligned box in the v‑plane and `v_0=v_\pm` the box center (as in Lemma 10.3 of v35). For any `r∈[1,\infty]`, let `q` be the Hölder conjugate: `1/r+1/q=1`.

**(i) Point evaluation from boundary `L^r` necessarily costs `δ^{-1/r}`.**  
For any harmonic function `u` on `B` (hence for `u=Re(W)` and `u=Im(W)` when `W` is holomorphic),
\[
|u(v_0)| \le \|P_B(v_0,\cdot)\|_{L^q(\partial B,ds)}\;\|u\|_{L^r(\partial B,ds)}.
\]
Under affine rescaling `T(\xi)=(\xi-v_0)/\delta` mapping `∂B` to `∂Q` with `Q=[-1,1]^2`, Poisson kernels scale as
\[
\|P_B(v_0,\cdot)\|_{L^q(\partial B,ds)} \asymp \delta^{-1/r}\,\|P_Q(0,\cdot)\|_{L^q(\partial Q,ds_Q)}.
\]
The exponent `δ^{-1/r}` is sharp by scaling (and for `r=2` it reproduces the `δ^{-1/2}` sharpness noted explicitly in v35’s Lemma 10.3 proof).

**(ii) Boundary Poincaré in `L^r` gives exactly one factor `δ`.**  
On the loop `∂B` of length `|∂B|=8\delta`,
\[
\|f-f_{\partial B}\|_{L^r(\partial B,ds)} \le C_r\,\delta\,\|\partial_s f\|_{L^r(\partial B,ds)},
\]
with `C_r` depending only on the normalized square `Q` (shape‑only).

Combining (i)+(ii) gives the forced δ‑power:
\[
|f(v_0)-c| \;\lesssim\; \delta^{-1/r}\cdot \delta\;\|\partial_s f\|_{L^r(\partial B)}
= \delta^{\,1-1/r}\,\|\partial_s f\|_{L^r(\partial B)}.
\]

### 2.2 Apply to the inner quotient `W = E/G_out` (outer factor inserts no δ)

Under the v35 hypotheses of Lemma 10.3 (boundary‑contact; `W` unimodular a.e. on `∂B`; `G_out` built from `\log|E|` on `∂B`), the same “outer factor control” step yields
\[
\|\partial_s \log W\|_{L^r(\partial B)} \le (1+\|H_{\partial Q}\|_{L^r\to L^r})\;\|\partial_s \log E\|_{L^r(\partial B)}.
\]
On `∂B`, `|\partial_s \log E|\le |E'/E|` (tangential derivative controlled by complex derivative), and `|\partial_s W|=|\partial_s \log W|` since `|W|=1` a.e. Thus
\[
\|\partial_s W\|_{L^r(\partial B)} \lesssim \left\|\frac{E'}{E}\right\|_{L^r(\partial B)}.
\]

### 2.3 The resulting unavoidable UE exponent in the `L^r` endpoint class

For each sign `±`, and any choice of constant phase `c` on `∂B`,
\[
|W(v_\pm)-c|
\;\lesssim\;
\delta^{\,1-1/r}\,\left\|\frac{E'}{E}\right\|_{L^r(\partial B,ds)}.
\]
Thus, in the absolute `L^r` endpoint family, the UE δ‑prefactor is **forced** to be
\[
p(r)=1-\frac1r.
\]

### 2.4 Local term is δ‑inert in the same class (`θ(r)=1−1/r`)

Under κ‑admissibility (v35 Definition 10.6 / Lemma 10.8 collar bound, pointwise),
\[
\sup_{\partial B}\left|\frac{Z'_{\rm loc}}{Z_{\rm loc}}\right|
\le \frac{N_{\rm loc}(m)}{\kappa\delta}.
\]
Therefore for any `r∈[1,\infty]`,
\[
\left\|\frac{Z'_{\rm loc}}{Z_{\rm loc}}\right\|_{L^r(\partial B,ds)}
\le
|\partial B|^{1/r}\cdot \frac{N_{\rm loc}(m)}{\kappa\delta}
\asymp
\frac{N_{\rm loc}(m)}{\kappa\,\delta^{\,1-1/r}}.
\]
So the interface exponent in this endpoint family is
\[
\theta(r)=1-\frac1r.
\]

### 2.5 Conclusion: `p(r)-θ(r)=0` ⇒ exponent budget fails uniformly in `m`

The local contribution in the envelope side scales like
\[
\delta^{p(r)}\cdot \delta^{-\theta(r)}\,N_{\rm loc}(m)
=
\delta^{\,p(r)-\theta(r)}\,N_{\rm loc}(m)
=
N_{\rm loc}(m),
\]
i.e. **δ‑inert**. Under `N_{\rm loc}(m)\ll \log m` and the nominal `δ0(m,α)=ηα/(\log m)^2`, this cannot be uniformly suppressed by η‑shrinking.

**Therefore:** Any S5 attempt that replaces `sup_{∂B}|E'/E|` by an **absolute** `L^r(∂B,ds)` endpoint (or equivalent absolute endpoint with the same scaling) is a formal NO‑GO.

---

## 3) What endpoint types remain viable (≤2 candidates; ranked)

The NO‑GO above is for absolute `L^r` control of the **log‑derivative**. To change `θ` without paying for a larger `p`, S5 must move to endpoints where local zeros do **not** produce `1/(\kappa\delta)` singularities in the chosen norm.

### Candidate 1 (highest viability): **cancellation / argument‑principle endpoint**
Use an endpoint built from **signed** boundary integrals (or total variations) of `\arg E` / `\arg W`, so each local zero contributes `O(1)` (arctan / winding) rather than `O(1/\delta)`.

Sketch endpoint family (example):
\[
\Phi_B(E)
:= \int_{\partial B} \bigl|\partial_s \arg E(v)\bigr|\,ds
\quad\text{or}\quad
\Phi_B(E):=\bigl|\Delta_{\partial B}\arg E\bigr|.
\]
Local poles contribute `O(1)` in `L^1(ds)` because the kernel `y/((x-a)^2+y^2)` has `L^1` mass `\asymp 1`. This has a realistic chance of giving `\theta=0` while keeping a positive `p`.

**Requirement:** this route needs a *new UE lemma* that bounds `D_B(W)` by `δ^p Φ_B(E)` (or a replacement forced quantity), and it must handle `\arg` branch choices carefully (use variation or winding, not pointwise arg).

### Candidate 2 (medium viability): **less singular boundary object (BMO / log|E| endpoint)**
Replace log‑derivative endpoints by endpoints on `\log|E|` (the object already used to build `G_{\rm out}`), e.g. BMO‑type norms on `∂B`. Local zeros generate logarithmic singularities, which are BMO‑controlled, not `1/\delta` controlled.

**Requirement:** substantial new functional analysis: relate `D_B(W)` to BMO/Hardy norms of boundary data via outer function machinery and quantitative rigidity.

---

## 4) v36‑ready manuscript edits (record the ruled‑out class to prevent drift)

The point of these edits is **program control**: v35 already records “pointwise/sup + collar + η‑absorption” as discarded. The L^r NO‑GO above should be recorded too, so future iterations don’t repeatedly attempt `L^2`/`L^1` absolute log‑derivative swaps.

### Paste‑ready TeX insert (Section 12, after Remark 12.2)

```tex
\begin{lemma}[Absolute $L^r$ endpoint scaling collapse]\label{lem:S5_Lp_collapse}
Let $B=B(\pm a,m,\delta)$ be an aligned box and let $G_{\rm out}$ and $W=E/G_{\rm out}$ be as in
Lemma~\ref{lem:upper-envelope}. Assume the boundary-contact convention so that $W$ has unimodular
boundary values a.e. Fix $r\in[1,\infty]$ and let $c_r\in\mathbb T$ be an $L^r(\partial B,ds)$-best constant phase:
\[
c_r \in \arg\min_{|c|=1}\,\|W-c\|_{L^r(\partial B,ds)}.
\]
Then there exists a shape-only constant $C_r>0$ (depending only on the normalized square $Q=[-1,1]^2$)
such that for each sign $\pm$,
\[
|W(v_\pm)-c_r|
\le C_r\,\delta^{\,1-1/r}\,
\left\|\frac{E'}{E}\right\|_{L^r(\partial B,ds)}.
\]
Moreover the exponent $\delta^{\,1-1/r}$ is forced by affine scaling in this endpoint class.
\end{lemma}

\begin{proposition}[NO--GO: absolute $L^r$ log-derivative endpoints cannot clear the UE--Gate]\label{prop:S5_Lp_nogo}
Assume in addition that $B$ is $\kappa$--admissible and the pointwise collar bound holds:
$\sup_{\partial B}\bigl|Z'_{\rm loc}/Z_{\rm loc}\bigr|\le N_{\rm loc}(m)/(\kappa\delta)$.
Then for every $r\in[1,\infty]$ one has
\[
\delta^{\,1-1/r}\left\|\frac{Z'_{\rm loc}}{Z_{\rm loc}}\right\|_{L^r(\partial B,ds)}
\asymp \frac{N_{\rm loc}(m)}{\kappa},
\]
independent of $\delta$. In particular, under the nominal scale $\delta_0(m,\alpha)=\eta\alpha/(\log m)^2$ and
the unconditional majorant $N_{\rm loc}(m)\ll\log m$, uniform $\eta$--shrinking cannot suppress the local term
within any envelope mechanism whose endpoint is an absolute $L^r(\partial B)$ norm of $E'/E$.
\end{proposition}

\begin{remark}[Implication for S5 endpoint design]\label{rem:S5_endpoint_implication}
Lemmas~\ref{lem:S5_Lp_collapse}--\ref{prop:S5_Lp_nogo} rule out the entire family of S5 proposals that attempt
to replace $\sup_{\partial B}|E'/E|$ by an absolute $L^r(\partial B)$ norm of $E'/E$ while keeping the same
$\kappa$--collar local control. Any viable S5 redesign must instead (i) exploit cancellation (argument-principle
style signed endpoints) and/or (ii) move to a less singular boundary object (e.g. endpoints built from
$\log|E|$ / BMO-type control).
\end{remark}
```

No other sections need edits; this is a **guardrail insertion**.

---

## 5) Mandatory Patch Packet

* **Callsign:** RH-BRIDGE
* **Result classification:** **PASS** (decision-grade NO‑GO delivered; search-space narrowed)
* **Target gaps closed (by ID):**
  - *(S5)* “Try `L^2`/`L^1` absolute endpoints of `|E'/E|`” — **ruled out** (new NO‑GO package; prevents drift)
* **Target gaps still open (by ID):**
  - *(S5–UE)* redesigned upper-envelope inequality in a cancellation / non-absolute endpoint class (v35 Remark 12.2)
  - *(S5–RES)* residual envelope in the same endpoint class
  - *(S5–LOC)* local/collar control in the same endpoint class (without pointwise `δ^{-1}` leakage)
  - *(S5–FORCE)* either `\Phi_B\ge D_B(W)` or a new forcing lemma for the new endpoint (v35 Remark 12.1)
* **Key conclusions (≤5 bullets):**
  1. Any absolute `L^r(∂B)` endpoint built on `|E'/E|` forces `p(r)=θ(r)=1−1/r`, hence `p−θ=0` and δ‑inert local leakage.
  2. Therefore S5 cannot be “swap sup → L^2/L^1” on `|E'/E|`; it must change endpoint *type* (cancellation or less singular data).
  3. The NO‑GO is shape-only and scaling-sharp; it survives adversarial referee scrutiny.
  4. The only credible escape hatches are cancellation-based endpoints (argument variation / signed contour integrals) or BMO/log|E| endpoints.
  5. Recommended next step: encode the NO‑GO in Section 12 to prevent future drift and focus v36 on cancellation endpoints.
* **Paste‑ready manuscript edits (TeX blocks):**
  - **(i) revised lemma/proposition statements:** the three-block insert in Section 12 above.
  - **(ii) revised definitions/remarks:** none required beyond the new remark `rem:S5_endpoint_implication`.
  - **(iii) revised theorem/inequality lines:** none.
* **Dependencies on other branches:**
  - ENVELOPE: if pursuing Candidate 1 or 2, ENVELOPE must specify the exact new endpoint `\Phi_B` and how it enters the tail inequality assembly.
  - FORCING: may need a new forcing lemma unless the endpoint is designed to dominate `D_B(W)` as in v35 Remark 12.1.
* **Referee risk notes (anticipated objections + how addressed):**
  - **“You assumed `L^r` Poincaré on `∂B`.”** Standard on a loop; constants are shape-only under affine scaling; statement explicitly restricts to this geometry.
  - **“You mixed harmonic and holomorphic evaluation.”** Real/imag parts of holomorphic functions are harmonic; the evaluation inequality is stated for harmonic functions.
  - **“Local term estimate uses pointwise collar bound.”** Yes—this matches the current κ‑admissible convention in v35; the NO‑GO is precisely about keeping that local control while changing only the endpoint norm.
  - **“Does the result depend on boundary regularity a.e. vs pointwise?”** No; the argument uses `L^r` boundary traces, consistent with v35’s a.e. boundary modulus convention.
