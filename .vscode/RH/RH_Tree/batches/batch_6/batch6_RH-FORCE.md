# Batch 6 — RH-FORCE
**PROGRAM:** RH Convergence Program (v36 truth-latched)  
**Callsign:** RH-FORCE  
**Role (Batch‑6):** Propose a *forceable boundary phase endpoint* \(\widetilde D_B\) (Δarg / \(\int \Im(\log\text{-derivative)\)) that:
1) is defined purely from v‑frame analytic objects on a box \(B(\alpha,m,\delta)\),  
2) is *forceable* by an off-axis quartet (π/2‑type lower bound), and  
3) avoids point-evaluation as an endpoint (no “dial point” endpoint).  

> Quick note (user check): yes, the legacy PDFs v10–v14 are still accessible in this session.

---

## 0) Context latch (v36)

In v36 the forcing architecture is explicitly **single‑box and constant‑limited**: the “pair factor” produces a large phase rotation \(\Delta_{I_+}\arg Z_{\rm pair}\ge \pi/2\), but the total variation is \(\le 2\pi\), so forcing cannot grow with \(m\). This is already codified (Lemma 8.1–8.2).  

Batch‑6 asks for a *boundary phase* endpoint to pursue S5′ without pointwise UE.

---

## 1) Candidate families (≤2) and ranking

### **Rank 1 (preferred): F1 — Inner quotient phase-winding endpoint**
Take \(\mathcal S(v)=W(v)\), where \(W:=E/G_{\rm out}\) is the inner quotient from Bridge‑1 outer factorization on a \(\kappa\)-admissible box (v36 §9–§10).

**Why this is the right forcing object:**  
- \(W\) shares the *interior zeros* of \(E\) (outer factor is zero‑free).  
- \(W\) is *nonvanishing in a \(\kappa\delta\)-collar* around \(\partial B\) under \(\kappa\)-admissibility, so a buffered Δarg endpoint is legal.  
- The argument principle gives a clean, cancellation‑free forcing mechanism: the *total winding* of \(W\) around a buffered rectangle is \(2\pi\cdot(\#\text{zeros inside})\), hence at least one side must carry ≥ π/2 of phase increment.

This gives a true “π/2 forcing” lemma *without* importing point evaluation or absolute \(L^r\) endpoints.

### **Rank 2 (conditional): F2 — Legacy column ratio \(L/R\) rewritten in v‑frame**
Take \(\mathcal S(v)=L(v)/R(v)\) where \(L,R\) are RH‑free “left/right columns” from the legacy Part‑I/III material transported to v‑frame.

**Status:** I cannot certify a forcing lemma here without the audited legacy column definitions and their analyticity/nonvanishing domains. This remains **CONDITIONAL**.

---

## 2) Proposed endpoint definition (TeX‑ready)

### 2.1 Setup and buffer
Let \(B=B(\alpha,m,\delta)\) be the aligned box
\[
B(\alpha,m,\delta):=\{v\in\mathbb C: |\Re v-\alpha|\le \delta,\ |\Im v-m|\le \delta\},
\]
and assume **\(\kappa\)-admissibility** (boundary-contact with quantitative collar):
\[
\operatorname{dist}(\partial B, Z(E))\ge \kappa\delta.
\]
Let \(G_{\rm out}\) be the Dirichlet outer factor on \(B^\circ\) and \(W:=E/G_{\rm out}\) the inner quotient (Bridge‑1 setup).

Define the **buffered inner rectangle**
\[
B_{\kappa/2}:=\{v\in B:\operatorname{dist}(v,\partial B)\ge \tfrac{\kappa\delta}{2}\},
\]
so \(\partial B_{\kappa/2}\) is the boundary of the smaller rectangle concentric with \(B\), with side lengths \(2\delta(1-\kappa/2)\).

**Key collar fact:** Under \(\kappa\)-admissibility, \(E\) (hence \(W\)) is nonzero on a neighborhood of \(\partial B_{\kappa/2}\), so \(\log W\) is holomorphic on that neighborhood.

### 2.2 Sidewise phase increment and endpoint
Let \(\partial B_{\kappa/2}=\bigcup_{j=1}^4 S_j\) be the four oriented sides in positive (counterclockwise) orientation. Define the sidewise phase increment by
\[
\Delta_{S_j}\arg W \ :=\ \int_{S_j} \Im\!\left(\frac{W'(v)}{W(v)}\right)\,dv,
\]
(which is branch‑independent because it is defined from \(W'/W\)).

Define the **boundary phase endpoint**
\[
\widetilde D_B(W)\ :=\ \max_{1\le j\le 4}\ \Bigl|\Delta_{S_j}\arg W\Bigr|.
\]

This is a *boundary-only* (buffered-boundary) functional: it uses values of \(W'/W\) on \(\partial B_{\kappa/2}\) only; no interior point evaluation occurs.

---

## 3) Forcing lemma (π/2‑type) — TeX‑ready

### Lemma (Phase forcing from an interior zero via argument principle)
Assume \(B(\alpha,m,\delta)\) is \(\kappa\)-admissible and let \(W\) be the inner quotient on \(B^\circ\).  
If \(W\) has at least one zero in \(B_{\kappa/2}^\circ\) (equivalently \(E\) has at least one zero there), then
\[
\widetilde D_B(W)\ \ge\ \frac{\pi}{2}.
\]

**Proof (audit-grade sketch).**  
Because \(W\) is holomorphic and nonvanishing on a neighborhood of \(\partial B_{\kappa/2}\), the argument principle applies on \(\partial B_{\kappa/2}\):
\[
\oint_{\partial B_{\kappa/2}} \frac{W'(v)}{W(v)}\,dv\ =\ 2\pi i\,N,
\]
where \(N\ge 1\) is the number of zeros of \(W\) in \(B_{\kappa/2}^\circ\), counted with multiplicity.

Taking imaginary parts and decomposing \(\partial B_{\kappa/2}\) into its four sides,
\[
\sum_{j=1}^4 \Delta_{S_j}\arg W
\ =\ \Im\!\oint_{\partial B_{\kappa/2}} \frac{W'}{W}\,dv
\ =\ 2\pi N\ \ge\ 2\pi.
\]
Hence at least one term satisfies \(\Delta_{S_j}\arg W \ge (2\pi)/4=\pi/2\), and therefore
\(\max_j |\Delta_{S_j}\arg W|\ge \pi/2\), i.e. \(\widetilde D_B(W)\ge \pi/2\). ∎

### Corollary (Off-axis quartet ⇒ phase forcing on the aligned box)
Let \(\rho=\beta+i\gamma\) be a nontrivial zero of \(\zeta(s)\) with \(\beta\neq \tfrac12\), and let \(v_\rho=a+im\) in v‑frame, where \(a=2\beta-1\neq 0\) and \(m=2\gamma\).  
Fix \(\alpha:=|a|\in(0,1]\) and choose any \(\delta>0\) so that the aligned box \(B(\alpha,m,\delta)\) is \(\kappa\)-admissible (by shrinking if needed). Then the associated inner quotient \(W\) satisfies
\[
\widetilde D_B(W)\ \ge\ \frac{\pi}{2}.
\]

---

## 4) Forceability gate remark (required to prevent drift)

In v36 the *forced object* is \(D_B(W)\) (dial deviation). The endpoint \(\widetilde D_B(W)\) is **not known** to dominate \(D_B(W)\) or vice‑versa.

Therefore any S5′ redesign that adopts \(\widetilde D_B\) must do one of the following, explicitly:

1. **Replace** the forced contradiction endpoint: rewrite the tail inequality to use \(\widetilde D_B(W)\) as the forced quantity, with the forcing lemma above, **or**
2. Prove a **transfer inequality** \( \widetilde D_B(W)\ge c\,D_B(W)\) (or \(D_B(W)\ge c\,\widetilde D_B(W)\)) on all admissible boxes.

Absent (1) or (2), the forcing chain and the envelope chain are logically disconnected (forceability NO‑GO).

---

## 5) “Upper control without point evaluation” (what RH‑FORCE certifies)

RH‑FORCE does **not** claim an S5′ closure here; that is ENVELOPE/LOCAL/BRIDGE territory. What I certify is:

- \(\widetilde D_B(W)\) is *intrinsically boundary‑phase* (buffered boundary), with no dial point evaluation.
- Its natural upper control targets are **signed/cancellation endpoints** (Hardy/BMO/arg‑principle style), since the v36 NO‑GO results forbid relying on absolute \(L^r(\partial B)\) control of \(|E'/E|\).

A minimal inequality template that does **not** use point evaluation is:
\[
\Bigl|\Delta_{S}\arg W\Bigr|
\le \int_{S}\left|\frac{W'}{W}\right|\,|dv| ,
\]
so any non‑absolute/cancellation control mechanism that bounds the RHS uniformly is in principle compatible.

---

## 6) Explicit‑formula interpretation check (S6 harness check)

**Does \(\widetilde D_B\) correspond to an \(x^\beta\) amplitude leak?**  
**Qualitatively yes, but indirectly.**

- An off-axis zero \(\rho=\beta+i\gamma\) with \(\beta\neq \tfrac12\) produces a term \(x^\rho/\rho\) in the classical explicit formula (e.g. for \(\psi(x)\)), whose magnitude behaves like \(x^\beta/|\rho|\). This is the “amplitude leak” mechanism.
- In v‑frame, \(\beta\neq\tfrac12\) is exactly \(\Re(v_\rho)=a\neq 0\). The endpoint \(\widetilde D_B(W)\) is forced precisely when such a zero lies in an aligned v‑box, because it detects a nontrivial winding number of the inner quotient \(W\), i.e. the presence of a zero with \(\Re(v)\neq 0\).

So \(\widetilde D_B\) is a **geometric phase proxy** for the same off-axis zeros that generate \(x^\beta\) growth; it does not measure \(x^\beta\) magnitude directly, but it is logically tied to the existence of the amplitude‑leak source.

---

## 7) Paste-ready manuscript edits (v37+ insertion blocks)

### (i) New definition block
```tex
\begin{definition}[Buffered boundary phase endpoint]\label{def:Db-tilde-phase}
Let $B=B(\alpha,m,\delta)$ be an aligned box and assume $\kappa$--admissibility:
$\dist(\partial B, Z(E))\ge \kappa\delta$.
Let $G_{\rm out}$ be the Dirichlet outer factor on $B^\circ$ and $W:=E/G_{\rm out}$ the inner quotient.
Define the buffered inner rectangle
\[
B_{\kappa/2}:=\{v\in B:\dist(v,\partial B)\ge \tfrac{\kappa\delta}{2}\},
\]
and write its oriented boundary as $\partial B_{\kappa/2}=\bigcup_{j=1}^4 S_j$ (counterclockwise).
Define the sidewise phase increment
\[
\Delta_{S_j}\arg W := \int_{S_j}\Im\!\left(\frac{W'(v)}{W(v)}\right)\,dv,
\]
and the phase endpoint
\[
\widetilde D_B(W):=\max_{1\le j\le 4}\Bigl|\Delta_{S_j}\arg W\Bigr|.
\]
\end{definition}
```

### (i) New forcing lemma block
```tex
\begin{lemma}[Phase forcing from an interior zero]\label{lem:phase-forcing-argprinciple}
Assume the setup of Definition~\ref{def:Db-tilde-phase}. If $W$ has at least one zero in
$B_{\kappa/2}^\circ$ (equivalently $E$ has at least one zero there), then
\[
\widetilde D_B(W)\ge \frac{\pi}{2}.
\]
\end{lemma}

\begin{proof}
Since $W$ is holomorphic and nonvanishing on a neighborhood of $\partial B_{\kappa/2}$,
the argument principle gives
\[
\oint_{\partial B_{\kappa/2}} \frac{W'(v)}{W(v)}\,dv = 2\pi i\,N,
\]
where $N\ge 1$ is the number of zeros of $W$ in $B_{\kappa/2}^\circ$, counted with multiplicity.
Taking imaginary parts and decomposing $\partial B_{\kappa/2}$ into four sides yields
\[
\sum_{j=1}^4 \Delta_{S_j}\arg W = 2\pi N \ge 2\pi.
\]
Hence at least one side satisfies $\Delta_{S_j}\arg W\ge \pi/2$, so
$\max_j|\Delta_{S_j}\arg W|\ge \pi/2$, i.e. $\widetilde D_B(W)\ge \pi/2$.
\end{proof}
```

### (ii) Forceability gate remark block
```tex
\begin{remark}[Forceability gate for phase endpoints]\label{rem:forceability-phase-gate}
The v36 forcing chain lower-bounds the dial deviation $D_B(W)$.
The phase endpoint $\widetilde D_B(W)$ in Definition~\ref{def:Db-tilde-phase} is not known to dominate
$D_B(W)$ or vice-versa. Therefore any redesign that replaces $D_B(W)$ by $\widetilde D_B(W)$ must
either:
(i) rewrite the tail inequality so that $\widetilde D_B(W)$ is the forced object (using
Lemma~\ref{lem:phase-forcing-argprinciple}), or
(ii) prove a transfer inequality relating $\widetilde D_B(W)$ and $D_B(W)$ on all admissible boxes.
Without (i) or (ii), forcing and envelope are logically disconnected.
\end{remark}
```

---

## 8) Dependencies and what is *not* claimed

- This note supplies **S5′-FORCE** (a forcing lemma targeting a boundary‑phase functional).
- It does **not** supply:
  - an S5′ upper envelope inequality (UE redesign),
  - a local/collar bound in the same endpoint class,
  - a complete tail inequality rewrite.

Those are dependencies on ENVELOPE/LOCAL/BRIDGE/ABSORB.

---

# MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* Callsign: RH-FORCE
* Result classification: **CONDITIONAL**
* Target gaps closed (by ID): 
  - **S5–FORCE obligation** (v36 Remark “forceability gate”): provides a direct forcing lemma for a *new* boundary-phase endpoint \(\widetilde D_B(W)\).
* Target gaps still open (by ID):
  - S5–UE redesign (non-pointwise upper control in a cancellation class)
  - S5–LOC redesign (local term control in the same endpoint class)
  - Tail inequality rewrite (if \(\widetilde D_B\) replaces \(D_B\))
* Key conclusions (5 bullets max):
  1. A clean **π/2 forcing lemma** exists for the *max sidewise phase increment* of the inner quotient \(W\), via the argument principle.
  2. The endpoint \(\widetilde D_B(W)\) is **boundary-only (buffered)** and avoids point evaluation by construction.
  3. This endpoint is **forceable without cancellation risk** (total winding is \(2\pi N\)).
  4. \(\widetilde D_B\) does **not** presently transfer to \(D_B(W)\); adopting it requires either a transfer inequality or a tail rewrite.
  5. Explicit-formula meaning: \(\widetilde D_B\) is a **phase proxy** detecting the same off-axis zeros that generate \(x^\beta\) leakage.
* Paste-ready manuscript edits (TeX blocks):
  - (i) revised lemma/proposition statements: **Definition \ref{def:Db-tilde-phase}**, **Lemma \ref{lem:phase-forcing-argprinciple}**
  - (ii) revised definitions/remarks: **Remark \ref{rem:forceability-phase-gate}**
  - (iii) revised theorem/inequality lines: **None in this batch** (requires ENVELOPE/ABSORB integration decision)
* Dependencies on other branches:
  - RH-ENVELOPE: must produce an S5′ upper bound that controls \(\widetilde D_B(W)\) in a non-absolute/cancellation endpoint class.
  - RH-LOCAL: must redesign the local term bound in the same endpoint class.
  - RH-BRIDGE: must confirm \(W\) nonvanishing on the buffered boundary under \(\kappa\)-admissibility, and that the buffered contour is legitimate.
  - RH-ABSORB: must insert the new endpoint into the budget calculus and tail criterion rewrite if adopted.
* Referee risk notes (anticipated objections + how addressed):
  - **Boundary regularity of \(W\):** avoided by defining the endpoint on a *buffered* contour \(\partial B_{\kappa/2}\) where \(W\) is holomorphic and nonzero by \(\kappa\)-admissibility.
  - **“Phase forcing might land on the wrong side”:** endpoint takes a **max over sides**, so forcing is unconditional given any interior zero.
  - **Relevance to off-axis quartets:** boxes are in \(\Re v>0\) for \(\delta<\alpha\), so any zero inside is off-axis; aligned choice \(\alpha=|a|\) captures the hypothetical quartet height-local zero.
