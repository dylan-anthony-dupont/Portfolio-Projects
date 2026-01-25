# Batch 7 — RH-LOCAL

**Ground truth:** v37 locked build (`manuscript_v37.tex/pdf`).

**Mission focus (Batch‑7):** supply drop‑in lemma(s) showing the local term has **θ = 0** (no δ blow‑up) **in the same phase/endpoint class** used for S5′ candidates built from boundary phase data.

Key v37 anchors:
- Local phase lemma (per zero ≤ π) is currently stated for the vertical segment \(I_+\) (Lemma `\ref{lem:local_phase_delta_inert}` in v37 TeX; “Local phase is \(\delta\)–inert: per‑zero contribution is \(O(1)\)”).  
- The forceable phase endpoint is the buffered boundary phase endpoint \(\widetilde D_B(W)\) on \(\partial B_{\kappa/2}\) (Definition `\ref{def:Db-tilde-phase}`).  
- The “Missing Lever” box explicitly requires an endpoint class with \(p\ge \tfrac12\) and a local interface exponent \(\theta\le p-\tfrac12\) (ideally \(\theta=0\)).【705:5†manuscript_v37.pdf†L14-L36】

This note closes the *local* part of that requirement by extending the δ‑inert phase bound from \(I_+\) to **any boundary side segment** used by \(\widetilde D_B\) (and, more generally, to any phase endpoint built as a finite max/sum of such signed phase increments).

---

## 1) Endpoint class fixed for this note

In v37, the phase endpoint used for S5′ forcing is
\[
\widetilde D_B(W):=\max_{1\le j\le 4}\Bigl|\Delta_{S_j}\arg W\Bigr|,\qquad 
\Delta_{S_j}\arg W := \Im\int_{S_j}\frac{W'(v)}{W(v)}\,dv,
\]
where \(S_j\) are the four oriented sides of the buffered inner boundary \(\partial B_{\kappa/2}\).【694:1†manuscript_v37.pdf†L1-L63】

For local control, the relevant induced endpoint class on a log‑derivative \(f\) is the functional
\[
\Phi_B^{\rm ph}(f)\ :=\ \max_{1\le j\le 4}\left|\Im\int_{S_j} f(v)\,dv\right|,
\]
so that \(\Phi_B^{\rm ph}(W'/W)=\widetilde D_B(W)\) by definition.

**Target (Missing‑Lever local bound):**
\[
\Phi_B^{\rm ph}\!\left(\frac{Z'_{\rm loc}}{Z_{\rm loc}}\right)\ \le\ C\,N_{\rm loc}(m),
\quad\text{with }\theta=0,\ q=1,\ u=0.
\]

---

## 2) Local lemma: θ = 0 in the buffered boundary phase class

### Lemma (δ‑inert local phase on any line segment)
Let \(S\subset\mathbb C\) be any oriented line segment, let \(\rho\notin S\), and choose a continuous branch of \(\arg(v-\rho)\) along \(S\). Then
\[
\left|\Im\int_{S}\frac{dv}{v-\rho}\right|
=\left|\arg(v_1-\rho)-\arg(v_0-\rho)\right|
\le \pi,
\]
where \(v_0,v_1\) are the endpoints of \(S\).

**Proof sketch (geometric; δ‑free):**  
Along a line segment \(S\) not passing through \(\rho\), the vector \(v-\rho\) traces a line segment in \(\mathbb C\setminus\{0\}\). The argument function can be chosen continuously on this segment, and the argument difference between two nonzero complex numbers is always bounded by \(\pi\) in absolute value. The identity with the integral is the standard log‑derivative primitive: \(\Im \int dv/(v-\rho)=\Delta\arg(v-\rho)\). \(\square\)

### Corollary (local term bound in the \(\widetilde D_B\) endpoint class)
Fix an aligned \(\kappa\)‑admissible box \(B=B(\alpha,m,\delta)\), and write
\[
Z_{\rm loc}(v)=\prod_{\rho\in Z_{\rm loc}(m)} (v-\rho)^{m_\rho},\qquad 
N_{\rm loc}(m)=\sum_{\rho\in Z_{\rm loc}(m)} m_\rho.
\]
Then for each buffered side \(S_j\subset \partial B_{\kappa/2}\),
\[
\left|\Im\int_{S_j}\frac{Z'_{\rm loc}(v)}{Z_{\rm loc}(v)}\,dv\right|
=\left|\Delta_{S_j}\arg Z_{\rm loc}\right|
\le \pi\,N_{\rm loc}(m),
\]
and hence
\[
\Phi_B^{\rm ph}\!\left(\frac{Z'_{\rm loc}}{Z_{\rm loc}}\right)\ \le\ \pi\,N_{\rm loc}(m).
\]

**δ‑uniformity and constants:**  
The constant is \(\pi\) and is independent of \((m,\alpha,\delta)\) and of \(\kappa\) (except for the nonvanishing requirement that \(\rho\notin S_j\), supplied in practice by \(\kappa\)‑admissibility / collar separation).

**Exponent data (in S5′ acceptance‑gate notation):**
- local blow‑up exponent: \(\theta=0\) (no δ factor appears),
- growth exponent: \(q=1\) when \(G(n,\kappa)=n\) (and \(N_{\rm loc}(m)\ll \log m\) is handled separately),
- \(\kappa\) exponent: \(u=0\).

This matches the “local phase is δ‑inert” posture already recorded in v37 for \(I_+\) (Lemma `\ref{lem:local_phase_delta_inert}`), but now in the *actual buffered boundary endpoint geometry* used by \(\widetilde D_B\).【694:1†manuscript_v37.pdf†L1-L63】

---

## 3) Micro‑window clustering (Task B)

This θ=0 bound **does not require any micro‑window clustering control** (it is valid even if zeros cluster arbitrarily tightly), because it is purely a per‑zero geometric phase increment bound.

What it does **not** do:
- It does not reduce the \(N_{\rm loc}(m)\sim \log m\) growth (so if ENVELOPE fails to supply \(p\ge \tfrac12\), then the program may still need one of the other decisive routes listed in the “Missing Lever” box: micro‑window clustering \(N_{\rm micro}=O(1)\) or forced‑pair isolation).【705:5†manuscript_v37.pdf†L24-L36】

---

## 4) S6 harness check: explicit formula interpretation

The local bound here is a **phase/winding** control:
\[
\Im\int \frac{Z'_{\rm loc}}{Z_{\rm loc}}\,dv=\Delta \arg Z_{\rm loc}.
\]
It is therefore naturally aligned with *argument principle forcing* (counting/winding), not directly with the explicit‑formula amplitude term \(x^\beta\). Under the frame map \(s\mapsto u=2s\mapsto v=u-1\), a zero \(\rho=\beta+i\gamma\) corresponds to \(v_\rho=(2\beta-1)+i\,2\gamma\); off‑critical‑line means \(\Re(v_\rho)\neq 0\). The phase endpoint detects winding around such \(v_\rho\), but does not by itself quantify the explicit‑formula amplitude leak \(x^\beta\) (which is governed by \(\beta\), not by boundary phase increments alone).

---

# Patch Packet (MANDATORY)

* Callsign: RH-LOCAL
* Result classification: **PASS** (θ=0 local bound in the buffered boundary phase endpoint class is proof‑grade)
* Target gaps closed (by ID): **G‑8 (local interface exponent θ in phase class)** — specifically, the δ‑inert local bound in the \(\widetilde D_B\) / phase‑increment class.
* Target gaps still open (by ID): **G‑8 (micro‑window / q‑reduction component)** remains open if ENVELOPE cannot reach \(p\ge \tfrac12\); UE redesign itself is ENVELOPE/ABSORB/FORCE scope.
* Key conclusions (≤5 bullets):
  1. In the phase‑increment endpoint class induced by \(\widetilde D_B\), the local term has **θ=0** (no δ blow‑up).
  2. Each local zero contributes at most **π** to the sidewise phase increment along any line segment, including each buffered side \(S_j\subset\partial B_{\kappa/2}\).
  3. Therefore \(\Phi_B^{\rm ph}(Z'_{\rm loc}/Z_{\rm loc})\le \pi N_{\rm loc}(m)\) with δ‑uniform constant.
  4. This lemma is robust to arbitrary micro‑clustering; clustering is only relevant if one seeks to reduce growth in \(N_{\rm loc}(m)\).
  5. The bound is purely geometric and does not encode explicit‑formula amplitude leakage \(x^\beta\).
* Paste-ready manuscript edits (TeX blocks):
  (i) revised lemma/proposition statements  
  (ii) revised definitions/remarks  
  (iii) revised theorem/inequality lines

```tex
% --- Replace Lemma \ref{lem:local_phase_delta_inert} by the following strengthened form ---

\begin{lemma}[Local phase is $\delta$--inert on line segments (per-zero contribution is $O(1)$)]
\label{lem:local_phase_delta_inert}
Let $S\subset\mathbb C$ be any oriented line segment and let $\rho\notin S$.
Choose a continuous branch of $\arg(v-\rho)$ along $S$.
Then
\[
\left|\Im\int_{S}\frac{dv}{v-\rho}\right|
=\left|\arg(v_1-\rho)-\arg(v_0-\rho)\right|
\le \pi,
\]
where $v_0,v_1$ are the endpoints of $S$.
Consequently, writing $Z_{\rm loc}(v)=\prod_{\rho\in Z_{\rm loc}(m)}(v-\rho)^{m_\rho}$,
for any segment $S$ avoiding $Z_{\rm loc}(m)$ one has
\[
\left|\Im\int_{S}\frac{Z'_{\rm loc}(v)}{Z_{\rm loc}(v)}\,dv\right|
=\left|\Delta_{S}\arg Z_{\rm loc}\right|
\le \pi\,N_{\rm loc}(m).
\]
\end{lemma}

% --- Add a short corollary after Definition \ref{def:Db-tilde-phase} if desired ---

\begin{corollary}[Local term in the buffered boundary phase endpoint class]\label{cor:local_phase_on_buffered_boundary}
Assume $B$ is $\kappa$--admissible and let $\partial B_{\kappa/2}=\bigcup_{j=1}^4 S_j$ be as in
Definition~\ref{def:Db-tilde-phase}. Then, for each $j$,
\[
\left|\Im\int_{S_j}\frac{Z'_{\rm loc}(v)}{Z_{\rm loc}(v)}\,dv\right|
\le \pi\,N_{\rm loc}(m).
\]
Equivalently, for the induced phase functional
\[
\Phi_B^{\rm ph}(f):=\max_{1\le j\le 4}\left|\Im\int_{S_j} f(v)\,dv\right|,
\]
one has $\Phi_B^{\rm ph}(Z'_{\rm loc}/Z_{\rm loc})\le \pi N_{\rm loc}(m)$ (local exponent $\theta=0$, growth $q=1$).
\end{corollary}
```

* Dependencies on other branches:
  - ENVELOPE/ABSORB/FORCE must still supply an S5′‑UE mechanism with \(p\ge \tfrac12\) that is **not** an absolute \(L^r\) endpoint and that is compatible with the forcing chain (either dominates forced quantity or has its own forcing lemma).【705:5†manuscript_v37.pdf†L24-L42】
* Referee risk notes (anticipated objections + how addressed):
  1. **Branch of \(\arg\)**: addressed by explicitly choosing a continuous branch along each segment (valid since \(\rho\notin S\)); κ‑admissibility ensures separation from zeros on buffered contours.
  2. **“Per-zero ≤ π” for horizontal segments**: holds for any line segment not passing through \(\rho\); the proof is geometric (argument difference between endpoints).
  3. **Does this re‑introduce pointwise collar estimates?** No; the bound uses only signed phase increments, not \(\sup|Z'_{\rm loc}/Z_{\rm loc}|\).
  4. **Growth in \(m\)** remains via \(N_{\rm loc}(m)\sim\log m\); this is explicitly acknowledged (micro‑window/pair‑isolation is separate and remains open if needed).
