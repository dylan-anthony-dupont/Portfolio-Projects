# Batch 6 — RH-LOCAL

**PROGRAM:** RH Convergence Program  
**LINE IN THE SAND:** v35/v36 truth‑latching. No drift.  
**CURRENT FRONTIER:** **S5′ = boundary phase endpoint** (Δarg / signed ∫Im(log‑derivative)) that is **forceable** and has **δ‑uniform upper control** without pointwise UE, without absolute (L^r) endpoints, and without projection‑kill tricks that break forceability.

## Local brief (RH‑LOCAL scope)

My scope is *only* the **local term** in the proposed **phase/Δarg endpoint class**:
\[
L_{\rm loc}(v)\;:=\;\frac{Z'_{\rm loc}}{Z_{\rm loc}}(v)\;=\;\sum_{\rho\in Z(m)}\frac{m_\rho}{v-\rho}.
\]
I compute the contribution of this local term to a **phase endpoint** of the form
\[
\Delta_{I_+}\arg(\cdot)\quad\text{or equivalently}\quad
\Im\int_{I_+}\frac{(\cdot)'}{(\cdot)}\,dv,
\]
and determine whether the “collar blow‑up exponent” can be taken **θ = 0** (i.e., **O(1) per local zero**, no δ^{-1}).

This is explicitly motivated by v36’s NO‑GO against absolute endpoints and the note that viable replacements must exploit **cancellation / signed structure / less singular boundary objects**.【621:0†manuscript_v36.pdf†L108-L115】

---

## Ground‑truth definitions from v36 (what I am matching)

### Aligned box and local factor
v36 defines the aligned square
\[
B(\alpha,m,\delta):=[\alpha-\delta,\alpha+\delta]\times[m-\delta,m+\delta],\qquad 
\delta:=\frac{\eta\alpha}{(\log m)^2},
\]
and the local window
\[
Z(m):=\{\rho\in Z(E):|\Im\rho-m|\le 1\},\qquad 
Z_{\rm loc}(v):=\prod_{\rho\in Z(m)}(v-\rho)^{m_\rho},
\]
with local count \(N_{\rm loc}(m)=\sum_{\rho\in Z(m)} m_\rho\).【621:0†manuscript_v36.pdf†L1-L15】

### The forcing segment \(I_+\)
In the forcing lemmas, v36 defines
\[
I_+ := \{\alpha + i y : |y-m|\le \delta\}.
\]
【674:2†manuscript_v36.pdf†L47-L53】

v36 already proves “π per linear factor” style upper control for the *pair factor* by exactly this mechanism: “argument of each linear factor varies by at most π.”【674:2†manuscript_v36.pdf†L58-L65】

---

## Task 1 (PRIMARY): local phase endpoint bound on \(I_+\) (θ = 0)

### Key point: the correct “phase integrand” is **Im( (Z'/Z) dv )**, not \((\Im Z'/Z)\,dv\)

If the endpoint is truly a **phase/Δarg** endpoint, the quantity that matches \(\Delta_{I_+}\arg\) is:
\[
\Delta_{I_+}\arg Z_{\rm loc}
\;=\;\Im\int_{I_+}\frac{Z'_{\rm loc}}{Z_{\rm loc}}(v)\,dv
\quad(\text{with a branch/contact convention}).
\]
On a vertical segment \(v=\alpha+i y\) (so \(dv=i\,dy\)), this is
\[
\Im\int_{m-\delta}^{m+\delta}\frac{Z'_{\rm loc}}{Z_{\rm loc}}(\alpha+i y)\,i\,dy
\;=\;\int_{m-\delta}^{m+\delta}\Re\!\left(\frac{Z'_{\rm loc}}{Z_{\rm loc}}(\alpha+i y)\right)\,dy,
\]
which is exactly the signed derivative of the argument along \(I_+\).

**Warning (audit‑grade):** the literal quantity \(\int_{I_+}(\Im(Z'_{\rm loc}/Z_{\rm loc}))\,dv\) on a vertical path corresponds to log‑magnitude variation and can produce \(\log\)-type blowups if the path passes close to a zero. That is **not** the “Δarg endpoint class” advertised in the Batch‑6 cover memo. The manuscript should parenthesize as \(\Im\int (Z'/Z)\,dv\).

### Lemma (TeX‑ready): \(\Delta_{I_+}\arg Z_{\rm loc}\) is \(O(N_{\rm loc})\), δ‑free

For a single linear factor, \(\Delta_{I_+}\arg(v-\rho)\) is controlled by an arctan range and is ≤ π. This extends multiplicatively to \(Z_{\rm loc}\).

**Conclusion:** the **phase endpoint** local contribution has exponent **θ = 0**.

---

## Task 2: quartet symmetry — does it cancel the local phase contribution?

### What is unconditional
In v‑frame, the completed xi‑type object \(E(v)\) has the unconditional symmetries coming from:
- reality on the real axis (complex conjugation symmetry),
- the functional equation (evenness in v, i.e. \(v\mapsto -v\)),

which together imply zeros occur in quartets \(\{\rho,\bar\rho,-\rho,-\bar\rho\}\).

### Does this cancel \(\Delta_{I_+}\arg Z_{\rm loc}\)?
**No automatic cancellation.** Even when a local window around height \(m>0\) contains the paired zeros \(\rho=a+ib\) and \(-\bar\rho=-a+ib\) (same height), the argument contributions along \(I_+=\{\alpha+i y\}\) are sign‑coherent in general. In particular:
- On a vertical segment, the arg‑derivative per zero is \(\Re(1/(v-\rho))\), which does not change sign in a way that forces cancellation between \(a\) and \(-a\) at fixed \(\alpha>0\).
- v36’s own forcing lower bound for \(Z_{\rm pair}(v)\) is *driven* by a large positive phase swing, not cancellation.【674:2†manuscript_v36.pdf†L47-L57】

So symmetry is **not** a mechanism to reduce the worst‑case upper bound below \(O(N_{\rm loc})\). The robust (referee‑grade) posture is the π‑per‑zero upper bound.

---

## Task 3: if \(N_{\rm loc}(m)\sim \log m\), can contradiction still work?

Local phase bound gives \(|\Delta_{I_+}\arg Z_{\rm loc}|\lesssim \pi N_{\rm loc}(m)\), and v36 provides an explicit unconditional count:
\[
N_{\rm loc}(m)\le 1.01\log m + 17\qquad(m\ge 10).
\]
【678:1†manuscript_v36.pdf†L84-L88】

So the local phase term is \(O(\log m)\). Whether this still permits a contradiction depends on the **residual side’s δ‑gain**:

- If the redesigned UE/envelope chain yields a **positive δ‑power prefactor** \(δ^p\) (p>0) multiplying the residual endpoint, then at the nominal scale \(δ_0\asymp(\log m)^{-2}\) one has \(δ_0^p \log m \to 0\). In that regime the \(O(\log m)\) local phase term is asymptotically subcritical.
- If the redesign yields **no δ gain** (p=0), then \(O(\log m)\) is not suppressible by η‑shrinking and becomes a structural obstruction.

This is consistent with v36’s “UE exponent gate” discussion in the pointwise class, where absence of δ‑gain leaves a surviving local obstruction.【678:1†manuscript_v36.pdf†L4-L18】【678:3†manuscript_v36.pdf†L67-L76】

---

## Task 4: tight unconditional \(N_{\rm loc}\) bound and Γ\_λ remarks

### Tight unconditional bound currently in the manuscript toolchain
v36 already contains the explicit window bound:
\[
N(T+1)-N(T-1)\le 1.01\log T+17 \quad(T\ge 5)
\;\Rightarrow\;
N_{\rm loc}(m)\le 1.01\log m+17 \quad(m\ge 10).
\]
【678:1†manuscript_v36.pdf†L84-L88】

This remains the “tightest *in‑manuscript* explicit constant bound” currently used.

### Does restricting to a Γ\_λ sub‑arc change the effective *count*?
Not the count \(N_{\rm loc}(m)\) as defined (it is a *height window* definition). A Γ\_λ restriction can only:
- shorten the path \(I_+\) (or replace it by a subsegment), thus reducing the **per‑zero phase swing** bound from π to at most \(2\arctan(\lambda\delta/|\alpha-\Re\rho|)\le\pi\);
- but it does not change which zeros are included in \(Z(m)\) unless the definition of \(Z_{\rm loc}\) itself is changed.

Given the Batch‑6 forceability constraints, the safe local posture is still the uniform π‑per‑zero bound.

---

## S6 harness check (explicit formula interpretation)

**Does the phase endpoint correspond to an \(x^\beta\) amplitude leak?**  
Not directly.

- In the classical explicit formula for \(\psi(x)\), an off‑critical‑line zero \(\rho=\beta+i\gamma\) contributes a term of size roughly \(x^\beta/\rho\) (amplitude) with oscillatory factor \(e^{i\gamma\log x}\) (phase). The *amplitude leak* is the \(x^\beta\) growth with \(\beta>1/2\).
- A boundary **phase** endpoint \(\Delta\arg\) built from \(\Im\int (E'/E)\,dv\) is structurally closer to the **argument** of zeta/xi (the \(S(t)\)‑type objects), i.e. it measures signed phase rotation induced by nearby poles/zeros in the log derivative, rather than directly estimating \(x^\beta\) contributions.

That said, the forcing mechanism exploits the fact that an off‑axis displacement \(\Re(v_\rho)\neq 0\) (equivalently \(\beta\neq 1/2\)) produces a **geometric phase swing** in the v‑plane (arctan law). So the endpoint is sensitive to \(\beta\) through geometry, but it is not literally an “\(x^\beta\) amplitude detector”.

---

## Paste‑ready TeX edits (v36 base)

> Placement suggestion: immediately after v36’s S5‑frontier note (after Proposition 12.7 / Remark 12.8), since it supplies a concrete endpoint class whose **local exponent is θ=0** (in contrast to the dead absolute endpoint classes).

### (i) New lemma: local phase budget on \(I_+\)

```tex
\begin{lemma}[Local phase budget on $I_+$]\label{lem:Zloc-phase-budget}
Fix $m\ge 10$, $\alpha\in(0,1]$, and $\delta>0$. Let
\[
I_+ := \{\alpha + i y : |y-m|\le \delta\}.
\]
Let $Z_{\rm loc}(v)=\prod_{\rho\in Z(m)}(v-\rho)^{m_\rho}$ be the local factor from Section~6,
where $Z(m)=\{\rho\in Z(E):|\Im\rho-m|\le 1\}$ and $N_{\rm loc}(m):=\sum_{\rho\in Z(m)} m_\rho$.
Then, under the $I_+$-contact convention (continuous argument along $I_+$ with small detours
around any zeros lying on the path),
\[
\bigl|\Delta_{I_+}\arg Z_{\rm loc}\bigr|
=\left|\Im\int_{I_+}\frac{Z_{\rm loc}'}{Z_{\rm loc}}(v)\,dv\right|
\le \pi\,N_{\rm loc}(m).
\]
In particular, for the phase endpoint $\Delta_{I_+}\arg(\cdot)$, the local term contributes with
phase exponent $\theta=0$ (no negative power of $\delta$).
\end{lemma}

\begin{proof}
Write $Z_{\rm loc}(v)=\prod_{\rho\in Z(m)}(v-\rho)^{m_\rho}$. Along $I_+$, each linear factor
$v-\rho=(\alpha-\Re\rho)+i(y-\Im\rho)$ has argument variation at most $\pi$ as $y$ ranges over an
interval (arctan range). Summing over $\rho$ with multiplicity gives
$|\Delta_{I_+}\arg Z_{\rm loc}|\le \pi\sum_{\rho\in Z(m)}m_\rho=\pi N_{\rm loc}(m)$.
\end{proof}
```

### (ii) Clarifying remark: parentheses matter (phase vs magnitude)

```tex
\begin{remark}[Phase endpoint vs magnitude endpoint]\label{rem:phase-parentheses}
For a $C^1$ curve $\Gamma$, the phase change $\Delta_\Gamma\arg f$ is represented by
$\Im\int_\Gamma (f'/f)\,dv$ (with a branch/contact convention), i.e. by $\Im((f'/f)\,dv)$
integrated along $\Gamma$. This is not the same object as $\int_\Gamma \Im(f'/f)\,dv$ when $\Gamma$
is not horizontal. In particular, on vertical segments $dv=i\,dy$, $\Im\int_\Gamma (f'/f)\,dv
=\int \Re(f'/f)\,dy$ is the signed arg-derivative; whereas $\int \Im(f'/f)\,dv$ corresponds to a
log-magnitude variation and can exhibit $\log$-blowup near zeros. The phase endpoint class in S5'
must therefore be written with the parentheses $\Im\int (f'/f)\,dv$.
\end{remark}
```

### (iii) Optional: record the explicit \(N_{\rm loc}\) plug‑in (existing lemma citation)
No new proof needed; just reference Lemma 10.10 for the explicit bound
\(N_{\rm loc}(m)\le 1.01\log m+17\).【678:1†manuscript_v36.pdf†L84-L88】

---

## Dependencies on other branches (what this unlocks / does not)

- **Unlocks for RH‑FORCE / RH‑ENVELOPE:** local term does **not** reintroduce a δ^{-1} collar obstruction in a **Δarg / phase integral endpoint**; local exponent is θ=0.
- **Still needed (out of scope for RH‑LOCAL):**
  - a forceability lemma for the chosen phase endpoint (π/2‑type lower bound) beyond the Z\_pair component,
  - a δ‑uniform **upper** envelope inequality in the phase endpoint class (must avoid absolute endpoints; must be δ‑uniform),
  - the absorption / tail closure bookkeeping (RH‑ABSORB).

---

## MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* Callsign: RH-LOCAL
* Result classification: **PASS (with a notation/parenthesis correction)**
* Target gaps closed (by ID): **G‑8 (local technology, phase-endpoint variant)**; supports Batch‑6 S5′ redesign by delivering **θ=0** local behavior.
* Target gaps still open (by ID): (owned by other branches) forceability for the new endpoint; δ‑uniform envelope in the new endpoint class; absorption closure.
* Key conclusions (≤5 bullets):
  1. For the **phase endpoint** \(\Delta_{I_+}\arg(\cdot)\) (equivalently \(\Im\int_{I_+} (\cdot)'/(\cdot)\,dv\)), the local term satisfies a **δ‑free** bound \(|\Delta_{I_+}\arg Z_{\rm loc}|\le \pi N_{\rm loc}(m)\) ⇒ **θ=0**.
  2. Quartet symmetry does **not** force cancellation of this local phase budget; worst‑case remains \(O(N_{\rm loc})\).
  3. v36’s explicit unconditional bound \(N_{\rm loc}(m)\le 1.01\log m+17\) implies local phase cost is \(O(\log m)\).
  4. If the redesigned envelope yields any **positive δ‑gain** \(δ^p\) on the residual term, then at \(δ_0\asymp(\log m)^{-2}\) the \(O(\log m)\) local phase term is asymptotically subcritical.
  5. Notation must be parenthesized as \(\Im\int (f'/f)\,dv\) (phase), not \(\int \Im(f'/f)\,dv\) (magnitude).
* Paste-ready manuscript edits (TeX blocks):
  (i) revised lemma/proposition statements: **Lemma \ref{lem:Zloc-phase-budget}** (above)  
  (ii) revised definitions/remarks: **Remark \ref{rem:phase-parentheses}** (above)  
  (iii) revised theorem/inequality lines: none beyond referencing Lemma 10.10 for \(N_{\rm loc}\).
* Dependencies on other branches:
  - RH‑FORCE: must define the S5′ endpoint and prove the forcing lower bound in that endpoint.
  - RH‑ENVELOPE: must supply δ‑uniform upper control in that endpoint class (no absolute L^r endpoints).
  - RH‑ABSORB: must check δ‑uniformity and closure once the endpoint is fixed.
* Referee risk notes (anticipated objections + how addressed):
  - **Objection:** “Your integral is ill‑defined if \(I_+\) crosses a zero.”  
    **Response:** lemma is stated under an explicit **contact convention** (detours) exactly analogous to the boundary‑contact convention already used on ∂B; the π‑per‑zero bound is stable under such detours.
  - **Objection:** “You used the wrong integrand (Im vs Re).”  
    **Response:** clarified: the phase change is \(\Im\int (f'/f)\,dv\), which on vertical segments equals \(\int \Re(f'/f)\,dy\). A remark is added to freeze the parentheses and prevent log‑magnitude misuse.
