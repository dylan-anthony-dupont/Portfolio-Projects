# Batch 6 — RH-ENVELOPE  
**Ground truth:** v36 (`manuscript_v36.tex/pdf`)  
**Callsign:** RH-ENVELOPE  
**Role:** Provide δ-uniform upper control for the **S5′ boundary-phase endpoint** \(\widetilde D_B\) **without** (i) point evaluation, (ii) absolute \(L^r\) endpoints on \(|E'/E|\), (iii) projection-kill tricks.

---

## Executive decision (one page)

**Result classification (branch-level): CONDITIONAL.**

I can supply a **proof-grade, δ-uniform “phase-split” envelope lemma** for any phase endpoint defined as an **argument increment** (equivalently, a **signed integral of the log-derivative**) along the near-vertical segment \(I_+\) (or a shifted segment \(I_{+,\lambda}\)). This avoids point evaluation and does not introduce absolute \(L^r(\partial B)\) norms as endpoints.

However, **whether S5′ can close** depends on a separate, currently missing ingredient: controlling the **local phase contribution** from the full \(Z_{\mathrm{loc}}\) (or showing it cancels/isolates to the forced pair). In the present architecture, the local phase increment can be bounded only by a coarse \(\pi N_{\mathrm{loc}}(m)\), which is too large to compare against constant-limited forcing unless FORCE/LOCAL supplies a mechanism that isolates the pair (or supplies a micro-window clustering bound).

What follows is the **upper-control lemma package** (TeX-ready) that Control Room can drop into v37+ as the envelope half of S5′.

---

## 0) Frame map and the log-derivative (v36-consistent)

Recall the frame relations:

- \(u = 1+v\) (width‑2 frame, centered at \(u=1\)),
- \(s = u/2 = (1+v)/2\) (s‑frame).

In v36 the entire completion in the v-frame is (notation as in §5–§6 of v36)
\[
E(v)\;:=\;\Xi_2(1+v)\;=\;\xi\!\left(\frac{1+v}{2}\right),
\]
so \(E\) is entire and its zeros correspond to nontrivial zeta zeros (pushed into the \(v\)-plane).

The explicit log-derivative identity (useful for interpretation) is:
\[
\frac{E'}{E}(v)
= \frac{1}{1+v}+\frac{1}{v-1}
-\frac14\log\pi
+\frac14\frac{\Gamma'}{\Gamma}\!\left(\frac{1+v}{4}\right)
+\frac12\frac{\zeta'}{\zeta}\!\left(\frac{1+v}{2}\right).
\]
This simply expands the completion \(\Xi_2(u)\) into gamma/power/zeta parts and then evaluates at \(u=1+v\).

---

## 1) Endpoint definition that avoids point evaluation and absolute norms

In v36, the near-vertical forcing segment is
\[
I_+ \;:=\;\{\alpha+i y:\ |y-m|\le\delta\}
\qquad\text{(Lemma 8.1, v36).}
\]

### Key geometry note (orientation)
Along a **vertical** segment \(v(y)=x+i y\), the argument increment satisfies
\[
\Delta_{I}\arg H
=\int_{y_0}^{y_1} \Re\!\left(\frac{H'}{H}(x+i y)\right)\,dy,
\]
not an \(\Im(\cdot)\) integral. (For a horizontal segment it is \(\Im(H'/H)\,dx\).)

So any “phase endpoint” on \(I_+\) naturally lives in the **signed, linear functional** class
\[
\widetilde D_B(H;\lambda)\;:=\;\Delta_{I_{+,\lambda}} \arg H
\quad\text{with}\quad
I_{+,\lambda}:=\{\alpha+\lambda\delta+i y:\ |y-m|\le\delta\}.
\]
The shift parameter \(\lambda\in[0,1]\) is a technical convenience to keep the contour off any zeros (if needed) without changing the δ-scale.

This endpoint is:
- **not** a point evaluation,
- **not** an absolute \(L^r\) norm,
- **forceable** in the same way as the v36 forcing lemma for \(Z_{\mathrm{pair}}\) (FORCE will decide the exact \(\lambda\) policy).

---

## 2) Main deliverable: phase-split envelope lemma (δ‑uniform)

### 2.1 Exact phase split \(E = F \cdot Z_{\mathrm{loc}}\)

v36 defines the local zero set and its factor:
\[
Z(m):=\{\rho:\ E(\rho)=0,\ |\Im\rho-m|\le 1\},\qquad
Z_{\mathrm{loc}}(v):=\prod_{\rho\in Z(m)}(v-\rho)^{m_\rho},
\]
and the residual factor
\[
F(v):=\frac{E(v)}{Z_{\mathrm{loc}}(v)}.
\]
By construction \(F\) is holomorphic and **zero-free** on any aligned box \(B(\alpha,m,\delta)\) with \(\delta\le 1\), because all zeros with \(|\Im\rho-m|\le 1\) have been removed.

### 2.2 δ-uniform phase split lemma (TeX-ready)

**Core point:** on any contour avoiding zeros of \(Z_{\mathrm{loc}}\), the phase increment splits additively, and the residual part is controlled by the v36 residual-envelope constants.

---

## 3) Local term bookkeeping: what we can (and cannot) bound

The local phase increment admits an **exact discrete representation**:
\[
\Delta_{I_{+,\lambda}}\arg Z_{\mathrm{loc}}
=\sum_{\rho\in Z(m)} m_\rho\,
\Big(\arg(\alpha+\lambda\delta+i(m+\delta)-\rho)-\arg(\alpha+\lambda\delta+i(m-\delta)-\rho)\Big).
\]

**Uniform upper bound (coarse):**
each summand has magnitude \(\le \pi\), hence
\[
\big|\Delta_{I_{+,\lambda}}\arg Z_{\mathrm{loc}}\big|\;\le\;\pi\,N_{\mathrm{loc}}(m).
\]
This bound is δ‑uniform but too weak for closure against constant forcing.

**Better bound (available but still needs a micro-window input):**  
For a zero \(\rho=\beta+i\gamma\), the derivative identity gives
\[
\frac{d}{dy}\arg\big((\alpha+\lambda\delta-\beta)+i(y-\gamma)\big)
=\frac{\alpha+\lambda\delta-\beta}{(\alpha+\lambda\delta-\beta)^2+(y-\gamma)^2},
\]
so for zeros with \(|\gamma-m|\gg \delta\) the contribution is \(O(\delta)\) and summable over \(N_{\mathrm{loc}}(m)\). The **only potentially \(O(1)\)** contributions come from zeros with \(|\gamma-m|\lesssim \delta\) and \(|\beta-(\alpha+\lambda\delta)|\lesssim \delta\), i.e. zeros in a micro-neighborhood of the short segment.

**Blocking issue (for global S5′ viability):**  
v36 has an explicit \(N_{\mathrm{loc}}(m)\) bound for the *unit* window \(|\Im\rho-m|\le 1\), but **no bound** on the micro-count
\[
N_{\mathrm{micro}}(m,\delta)
:=\#\{\rho:\ E(\rho)=0,\ |\Im\rho-m|\le \delta\}.
\]
Without a bound on \(N_{\mathrm{micro}}(m,\delta)\), one cannot exclude a worst-case scenario where \(\Delta_{I_{+,\lambda}}\arg Z_{\mathrm{loc}}\) is as large as \(O(N_{\mathrm{loc}}(m))\) on the segment (clustered ordinates).

This is not an ENVELOPE responsibility to fix, but it is the correct **dependency handoff** to FORCE/LOCAL if S5′ is to have a chance.

---

## 4) Relation back to v36 residual ledger (what is δ‑uniform “for free”)

v36 already provides the residual-envelope bound (Lemma `\ref{lem:residual-envelope}`):
\[
\sup_{\partial B}\left|\frac{F'}{F}\right| \le C_1\log m + C_2,
\]
with constants independent of \(\delta\) (and, in the v36 setup, uniform across \(\alpha\in(0,1]\) once the box is in \(\Re v>0\) and \(\delta\le\delta_0(m,\alpha)\)).

Therefore any phase endpoint built as \(\Delta_{I_{+,\lambda}}\arg F\) has the δ‑uniform budget
\[
\big|\Delta_{I_{+,\lambda}}\arg F\big|
\le 2\delta(C_1\log m + C_2),
\]
and the completion terms in \(E'/E\) contribute only \(O(\delta/m)\) along \(I_{+,\lambda}\).

This is exactly the kind of δ‑uniform residual control S5′ needs.

---

## 5) “Does this collapse to a dead NO‑GO class?”

No.

- There is **no point evaluation** (no \(W(v_\pm)\), no Poisson interior evaluation).
- The endpoint is a **signed linear functional** (argument increment / log-derivative integral), **not** an absolute \(L^r\) norm on \(|E'/E|\).
- The only place a sup bound appears is in bounding the **residual** \(F'/F\) using an already-proved lemma; it is not introduced as a new endpoint to be forced.

So ENVELOPE’s contribution is compatible with the v36 NO‑GO constraints.

---

## 6) Explicit-formula interpretation check (S6 harness)

**Does this endpoint correspond to an \(x^\beta\) amplitude leak?**  
Not directly, at least not in the same “amplitude” sense as a modulus growth witness.

- The endpoint \(\Delta_{I_{+,\lambda}}\arg E\) (or \(\Delta\arg W\)) is a **phase/argument** functional: in s‑frame it is a change of \(\arg\xi(\sigma+i t)\) over a very short \(t\)-interval at \(\sigma=(1+\alpha+\lambda\delta)/2>1/2\).
- Argument variation is more naturally tied to **zero counting** (via the argument principle / Riemann–von Mangoldt \(N(t)\) and the error term \(S(t)\)), rather than directly to the prime-side \(x^\beta\) amplitude contribution.

**Qualitative link:**  
The log-derivative \(\zeta'/\zeta\) is exactly what appears when one derives explicit formulas by contour shifting. A forceable phase jump can be interpreted as a detectable “singularity signature” consistent with a nearby zero. But extracting a direct \(x^\beta\) amplitude leak from this endpoint would require an additional step that links this short-interval phase deviation to a failure of cancellation in \(\sum_\rho x^\rho/\rho\). That step is outside this branch.

---

# MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* Callsign: RH-ENVELOPE
* Result classification: CONDITIONAL
* Target gaps closed (by ID):  
  - No legacy G‑IDs are fully closed here. This is an **S5′ redesign insertion**: “δ‑uniform upper control for boundary-phase endpoints” (new package).
* Target gaps still open (by ID):  
  - **(new, S5′-blocking)** Micro-window clustering control for the local phase term, i.e. a bound on \(N_{\mathrm{micro}}(m,\delta)\) or an endpoint choice that isolates the forced pair’s phase contribution.
  - Any FORCE-side requirement: a π/2 forcing lemma for the exact \(\widetilde D_B\) definition (including \(\lambda\)-shift policy).
* Key conclusions (≤5 bullets):
  1. A phase endpoint \(\widetilde D_B=\Delta_{I_{+,\lambda}}\arg(\cdot)\) avoids point evaluation and absolute \(L^r\) endpoints by construction.
  2. The residual contribution is δ‑uniform and shrinkable: \(|\Delta_{I_{+,\lambda}}\arg F|\le 2\delta(C_1\log m+C_2)\).
  3. The local contribution has an exact discrete representation; the only unconditional bound currently available is \(|\Delta\arg Z_{\mathrm{loc}}|\le \pi N_{\mathrm{loc}}(m)\).
  4. S5′ viability hinges on a new mechanism to prevent/neutralize micro-clustering of zeros in \(|\Im\rho-m|\le\delta\), or an endpoint definition that isolates the forced pair.
  5. This branch does not introduce any forbidden NO‑GO endpoint class.
* Paste-ready manuscript edits (TeX blocks):

  (i) **Revised lemma/proposition statements**  
  ```tex
  % ===== S5' boundary-phase endpoint (ENVELOPE package) =====

  \begin{definition}[Shifted near-vertical segment and phase increment]\label{def:phase-endpoint}
  Let $B=B(\alpha,m,\delta)$ be an aligned box and let $\lambda\in[0,1]$.
  Define the shifted near-vertical segment
  \[
    I_{+,\lambda}:=\{\alpha+\lambda\delta+i y:\ |y-m|\le\delta\}.
  \]
  If $H$ is holomorphic and nonvanishing on a neighborhood of $I_{+,\lambda}$, define the oriented phase increment
  \[
    \Delta_{I_{+,\lambda}}\arg H
    := \arg H(\alpha+\lambda\delta+i(m+\delta))-\arg H(\alpha+\lambda\delta+i(m-\delta)),
  \]
  where the branch of $\arg$ is chosen continuously along $I_{+,\lambda}$.
  Equivalently,
  \[
    \Delta_{I_{+,\lambda}}\arg H
    = \int_{m-\delta}^{m+\delta}\Re\!\left(\frac{H'}{H}(\alpha+\lambda\delta+i y)\right)\,dy.
  \]
  \end{definition}

  \begin{lemma}[Phase split on $I_{+,\lambda}$]\label{lem:phase-split}
  Let $B=B(\alpha,m,\delta)$ be an aligned box with $\delta\le 1$, and let
  $E$, $Z_{\mathrm{loc}}$, $F=E/Z_{\mathrm{loc}}$ be as in \S\ref{sec:local-subtraction}.
  Assume $I_{+,\lambda}$ contains no zero of $Z_{\mathrm{loc}}$.
  Then
  \[
    \Delta_{I_{+,\lambda}}\arg E
    = \Delta_{I_{+,\lambda}}\arg F + \Delta_{I_{+,\lambda}}\arg Z_{\mathrm{loc}}.
  \]
  Moreover, since $F$ is holomorphic and zero-free on $B$,
  \[
    \big|\Delta_{I_{+,\lambda}}\arg F\big|
    \le 2\delta\,\sup_{\partial B}\left|\frac{F'}{F}\right|.
  \]
  \end{lemma}

  \begin{corollary}[Residual phase budget (δ-uniform)]\label{cor:residual-phase-budget}
  Under the hypotheses of Lemma \ref{lem:phase-split}, we have
  \[
    \big|\Delta_{I_{+,\lambda}}\arg F\big|
    \le 2\delta\,(C_1\log m+C_2),
  \]
  where $(C_1,C_2)$ are the constants from Lemma \ref{lem:residual-envelope}.
  \end{corollary}

  \begin{lemma}[Local phase representation and coarse bound]\label{lem:local-phase-budget}
  Under the hypotheses of Lemma \ref{lem:phase-split},
  \[
    \Delta_{I_{+,\lambda}}\arg Z_{\mathrm{loc}}
    = \sum_{\rho\in Z(m)} m_\rho\Big(
      \arg(\alpha+\lambda\delta+i(m+\delta)-\rho)
      -\arg(\alpha+\lambda\delta+i(m-\delta)-\rho)\Big).
  \]
  In particular,
  \[
    \big|\Delta_{I_{+,\lambda}}\arg Z_{\mathrm{loc}}\big|\le \pi\,N_{\mathrm{loc}}(m).
  \]
  \end{lemma}
  ```

  (ii) **Revised definitions/remarks**  
  ```tex
  \begin{remark}[S5' envelope interface]\label{rem:S5p-envelope-interface}
  The endpoint $\Delta_{I_{+,\lambda}}\arg(\cdot)$ is a signed (non-absolute) boundary-phase functional.
  It avoids (i) point evaluation at dial points and (ii) absolute $L^r(\partial B)$ endpoints on $|E'/E|$.
  The residual contribution is controlled δ-uniformly by Lemma \ref{lem:residual-envelope} via
  Corollary \ref{cor:residual-phase-budget}.
  Any S5' closure must additionally control the local phase term in Lemma \ref{lem:local-phase-budget},
  either by isolating the forced pair factor or by bounding micro-window clustering.
  \end{remark}
  ```

  (iii) **Revised theorem/inequality lines**  
  (No direct replacement lines proposed here; FORCE/ABSORB will decide how to insert the new endpoint into the tail criterion once the forcing lower bound is fixed.)

* Dependencies on other branches:
  - **RH-FORCE:** must specify the exact endpoint \( \widetilde D_B \) (choice of \(H\), and whether an \(\lambda\)-shift is required) and prove the π/2-type forcing lower bound in that definition.
  - **RH-LOCAL:** if S5′ requires controlling micro-clustering in \(|\Im\rho-m|\le\delta\), that is a LOCAL-type lemma (or a NO-GO).
  - **RH-BRIDGE/RH-ABSORB:** will determine how the new endpoint plugs into the contradiction/tail closure and whether additional outer-factor structure is needed.
* Referee risk notes (anticipated objections + how addressed):
  1. **Arg/log branch ambiguity:** the definition requires \(H\) nonvanishing on a neighborhood of \(I_{+,\lambda}\). This is explicitly stated; if zeros lie on \(I_+\), shift by \(\lambda\) or interpret as a limit (FORCE should lock a policy).
  2. **Orientation mistake (Re vs Im):** the patch makes explicit that on a vertical segment the argument increment is the \(y\)-integral of \(\Re(H'/H)\).
  3. **Hidden absolute endpoint:** the only absolute bound used is the already-proved residual sup bound on \(F'/F\) from Lemma \ref{lem:residual-envelope}; the endpoint itself remains a signed functional.
  4. **Local term too large:** the patch explicitly flags this as the remaining blocking issue, rather than claiming closure.
