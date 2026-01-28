# Batch 11 — RH-FORCE
**Mechanism choice (mandatory): (A) Pair isolation.**  
We isolate a *single* tilt-forced singularity of a defect object on a *shifted* contour family. This bypasses the micro-step obstruction **NG-(\Delta a)-A** (small \(h\) kills forcing) by forcing on a contour where the defect object is genuinely *meromorphic with a pole*, so the argument principle yields an \(\Omega(1)\) phase increment (indeed \(\pi/2\) on some side).

---

## (1) Proposed geometry change: a pole-centered witness family \(\mathscr B=\mathfrak B^{\rm pole}\)

Work in the centered width–2 frame:
\[
u=2s,\qquad v=u-1,\qquad s=\tfrac{1+v}{2}.
\]
An off-axis nontrivial zero \(\rho=\beta+i\gamma\) corresponds to
\[
v_\rho = (2\beta-1) + i\,2\gamma = a + i m,\quad a:=2\beta-1,\quad m:=2\gamma.
\]

Let \(E(v)\) be the even entire completion (so zeros of \(E\) are exactly nontrivial zeros in the \(v\)-frame). Fix \(\kappa\in(0,1/10)\) as in the manuscript.

### Defect objects (already standard in v40+)
\[
\mathcal Q_a(v):=\frac{E(v+a)}{E(v-a)},\qquad 
\mathcal L_a(v):=\frac{\mathcal Q_a'(v)}{\mathcal Q_a(v)}=\frac{E'}{E}(v+a)-\frac{E'}{E}(v-a).
\]
(These agree with the manuscript’s defect quotient/log-derivative definitions.)

### New witness family: *pole boxes* (shifted geometry)
Given a tilt \(a>0\), a height \(m>0\), and a nominal scale \(\delta_0=\delta_0(m,a)\) (e.g. \(\delta_0=\eta a/(\log m)^2\)), define the **pole-centered box**
\[
B^{\rm pole}(a,m,\delta)\ :=\ \bigl\{v\in\mathbb C:\ \|v-(2a+i m)\|_\infty\le \delta\bigr\},
\qquad 0<\delta\le \delta_0.
\]

### \(\kappa\)-admissibility for defect objects
We say \(B^{\rm pole}(a,m,\delta)\) is **\(\kappa\)-admissible for \(\mathcal Q_a\)** if the boundary avoids both the poles and zeros of \(\mathcal Q_a\) with the same collar policy:
\[
\operatorname{dist}\!\Bigl(\partial B^{\rm pole}(a,m,\delta),\ Z(E(\cdot-a))\cup Z(E(\cdot+a))\Bigr)\ \ge\ \kappa\delta.
\]
Equivalently: \(\mathcal Q_a\) is holomorphic and nonvanishing on a \(\kappa\delta\)-collar neighborhood of \(\partial B^{\rm pole}\), so \(\arg \mathcal Q_a\) can be chosen continuously along the buffered contour.

### Buffered contour
As in the existing “buffered boundary phase endpoint” policy, set
\[
B^{\rm pole}_{\kappa/2}(a,m,\delta)\ :=\ \{v\in B^{\rm pole}(a,m,\delta):\operatorname{dist}(v,\partial B^{\rm pole})\ge \tfrac{\kappa\delta}{2}\},
\]
and write its oriented boundary as \(\partial B^{\rm pole}_{\kappa/2}=\bigsqcup_{j=1}^4 S_j\) (counterclockwise).

This defines the witness family
\[
\mathfrak B^{\rm pole}(a,m,\delta_0)\ :=\ \Bigl\{B^{\rm pole}(a,m,\delta):\ 0<\delta\le\delta_0,\ B^{\rm pole}(a,m,\delta)\text{ is }\kappa\text{-admissible for }\mathcal Q_a\Bigr\}.
\]

---

## (2) Endpoint definition \(\Phi_{\mathscr B}\)

On any \(B\in\mathfrak B^{\rm pole}(a,m,\delta_0)\), define the **defect phase endpoint** (same endpoint class as v40’s defect phase endpoint, but on the *new* contour family):
\[
\Phi^{\rm pole}_{B}(a)\ :=\ \max_{1\le j\le 4}\left|\Im\int_{S_j}\mathcal L_a(v)\,dv\right|
\ =\ \max_{1\le j\le 4}\left|\Delta_{S_j}\arg \mathcal Q_a\right|.
\]

This endpoint is:
* **tilt-sensitive**: if \(a=0\), then \(\mathcal Q_0\equiv 1\) and \(\Phi^{\rm pole}_{B}(0)=0\);
* **argument-principle compatible**: for \(\kappa\)-admissible \(B\), \(\mathcal Q_a\) is nonzero on \(\partial B_{\kappa/2}\), so \(\arg\mathcal Q_a\) is well-defined along the boundary and the integral \(\int (\mathcal Q_a'/\mathcal Q_a)\,dv\) equals the net winding.

---

## (3) Forcing lemma (line-by-line proof; \(\pi/2\)-type)

### Lemma (Defect pole-box forcing; closes OPEN-GEO(1) and OPEN-GEO(3) on the forcing side)
Assume \(E\) has an off-axis quartet at height \(m\) with tilt \(a>0\), i.e. \(E(a+i m)=0\).  
Let \(\delta_0>0\) be any nominal scale. Then there exists \(\delta\in(0,\delta_0]\) such that \(B:=B^{\rm pole}(a,m,\delta)\in\mathfrak B^{\rm pole}(a,m,\delta_0)\) and
\[
\Phi^{\rm pole}_{B}(a)\ \ge\ \frac{\pi}{2}.
\]

#### Proof
**Step 1 (meromorphic structure).**  
\(\mathcal Q_a(v)=E(v+a)/E(v-a)\) is meromorphic with poles at zeros of \(E(\cdot-a)\) and zeros at zeros of \(E(\cdot+a)\).

**Step 2 (a pole is forced at the shifted point).**  
Since \(E(a+i m)=0\), we have
\[
E\bigl((2a+i m)-a\bigr)=E(a+i m)=0,
\]
hence \(\mathcal Q_a\) has a pole at
\[
v_\star := 2a+i m.
\]

**Step 3 (pair-isolation: choose a \(\kappa\)-admissible box around the pole).**  
Because poles/zeros of \(\mathcal Q_a\) are isolated, pick \(\varepsilon>0\) such that the closed sup-norm ball
\[
\overline{B(v_\star,\varepsilon)}:=\{v:\|v-v_\star\|_\infty\le\varepsilon\}
\]
contains **no** zeros of \(E(\cdot+a)\) and contains **no** zeros of \(E(\cdot-a)\) except those at \(v_\star\) (with its multiplicity).

Set
\[
\delta := \min\Bigl\{\delta_0,\ \frac{\varepsilon}{1+\kappa}\Bigr\}.
\]
Then for every \(v\in\partial B^{\rm pole}(a,m,\delta)\), we have \(\|v-v_\star\|_\infty=\delta\le \varepsilon/(1+\kappa)\), so every boundary point remains at distance \(\ge \kappa\delta\) from any other singularity/zero of \(\mathcal Q_a\). Thus \(B^{\rm pole}(a,m,\delta)\) is \(\kappa\)-admissible for \(\mathcal Q_a\), i.e. \(B\in\mathfrak B^{\rm pole}(a,m,\delta_0)\).

**Step 4 (argument principle on the buffered contour).**  
Since \(\mathcal Q_a\) is meromorphic on a neighborhood of \(B\) and nonzero on \(\partial B_{\kappa/2}\), the argument principle gives
\[
\Im\int_{\partial B_{\kappa/2}} \frac{\mathcal Q_a'(v)}{\mathcal Q_a(v)}\,dv
= 2\pi\bigl(N_Z(\mathcal Q_a;B_{\kappa/2})-N_P(\mathcal Q_a;B_{\kappa/2})\bigr).
\]
By construction, \(B_{\kappa/2}\) contains at least one pole (at \(v_\star\)), hence \(N_P\ge 1\). Also by construction it contains no zeros of \(\mathcal Q_a\), hence \(N_Z=0\). Therefore
\[
\left|\Im\int_{\partial B_{\kappa/2}} \frac{\mathcal Q_a'(v)}{\mathcal Q_a(v)}\,dv\right|
= 2\pi N_P\ \ge\ 2\pi.
\]

**Step 5 (extract a \(\pi/2\) side increment).**  
Write \(\partial B_{\kappa/2}=\bigsqcup_{j=1}^4 S_j\). Then
\[
\Im\int_{\partial B_{\kappa/2}} \frac{\mathcal Q_a'}{\mathcal Q_a}\,dv
=\sum_{j=1}^4 \Im\int_{S_j} \mathcal L_a(v)\,dv.
\]
Taking absolute values and using the triangle inequality,
\[
2\pi\ \le\ \sum_{j=1}^4 \left|\Im\int_{S_j}\mathcal L_a(v)\,dv\right|
\ \le\ 4\max_{1\le j\le 4}\left|\Im\int_{S_j}\mathcal L_a(v)\,dv\right|.
\]
Hence \(\Phi^{\rm pole}_{B}(a)\ge \pi/2\), as claimed. ∎

**Why NG-(\(\Delta a\))-A does not apply.**  
The obstruction NG-(\(\Delta a\))-A is a *micro-step* phenomenon: a difference quotient in the \(a\)-direction at step \(h\asymp\delta\) produces an \(O(h)\) forcing ceiling because the contour never probes a genuine pole. Here the geometry is shifted so that the defect object \(\mathcal Q_a\) has an *actual pole inside* the witness region (at \(v_\star=2a+im\)), yielding a topological \(2\pi\) winding and hence a \(\pi/2\) side forcing, independent of \(\delta\).

---

## (4) Resonance sanity: why extra nearby quartets cannot erase forcing

**Claim (monotone forcing under extra poles).**  
On any \(\kappa\)-admissible \(B\in\mathfrak B^{\rm pole}\), the phase forcing is quantized by the integer \(N_Z-N_P\). Adding additional poles of \(\mathcal Q_a\) inside \(B\) (coming from additional zeros of \(E(\cdot-a)\)) can only increase \(|N_Z-N_P|\) unless additional *zeros* of \(\mathcal Q_a\) enter \(B\).

**How pair isolation enforces robustness.**  
The witness family \(\mathfrak B^{\rm pole}(a,m,\delta_0)\) is explicitly defined to include **shrunk** boxes (any \(0<\delta\le\delta_0\)). Since the singular set is discrete, we can always shrink until exactly the pole at \(v_\star\) is isolated and no zero of \(\mathcal Q_a\) lies inside. This makes the forcing *resonance-proof* at the forcing stage:
\[
N_Z=0,\quad N_P\ge 1\quad\Longrightarrow\quad \Phi^{\rm pole}_{B}(a)\ge \pi/2.
\]

*Interpretation:* “near-resonant quartets” may complicate **upper bounds** (UE side), but they do not invalidate the existence of a *forceable* witness region in \(\mathfrak B^{\rm pole}\) carrying a fixed \(\pi/2\) phase defect.

---

## (5) Compatibility checklist vs v40/v41 NO-GOs (PASS/FAIL)

* **Old centered defect cancellation \(O(\delta/a)\): PASS.**  
  That cancellation is specific to centered/“aligned-to-\(im\)” defect contours where \(\mathcal Q_a\) has a removable \(0/0\) at \(v=im\). Here we force on the pole-centered contour around \(v=2a+im\), where the denominator genuinely vanishes.

* **\(\delta\)-inert resonance obstruction: PASS (for forcing).**  
  Forcing is topological (argument principle) and quantized; it cannot be “erased by cancellation” once we isolate a pole and keep zeros out of the region. (Upper control remains a separate UE/local obligation.)

* **NG-(\(\Delta a\))-A (micro-step kills absolute forcing): PASS.**  
  We do not use the two-sided shift-difference \(\mathcal D_{a,h}\) at \(h\asymp\delta\). The forcing comes from a genuine pole of \(\mathcal Q_a\) inside a shifted box, so the lower bound is \(\Omega(1)\) independent of \((\delta,h)\).

* **Pointwise UE exponent ceiling \(p\le 1\): PASS.**  
  No pointwise UE exponent is invoked in the forcing lemma. The lower bound is purely geometric/topological.

---

## (6) S6 harness: mapping + explicit-formula interpretation

### Frame map (mandatory)
\[
s=\sigma+i t,\quad u=2s,\quad v=u-1.
\]
An off-axis zero \(\rho=\beta+i\gamma\) gives
\[
v_\rho=(2\beta-1)+i(2\gamma)=a+i m,\quad a=2\beta-1,\ m=2\gamma,
\]
so \(\beta=\tfrac{1+a}{2}\). Off-critical-line means \(a\neq 0\).

### Explicit-formula “amplitude leak” meaning (qualitative)
An off-axis zero with \(\beta>1/2\) contributes an explicit-formula term \(\asymp x^{\beta}/\rho\) (an “\(x^\beta\) amplitude leak” relative to the \(x^{1/2}\) RH scale). The defect object \(\mathcal Q_a(v)=E(v+a)/E(v-a)\) is built to *distinguish the tilt parameter \(a\)*: if \(a=0\), \(\mathcal Q_a\equiv 1\); if \(a>0\) and \(E(a+im)=0\), then \(\mathcal Q_a\) has a forced pole at \(v=2a+im\), producing a quantized phase defect.

This is not a direct quantitative measurement of the explicit-formula amplitude, but it is a **tilt detector**: it certifies \(a>0\) (hence \(\beta>1/2\)) via a forced winding event in a defect quotient built from the completed zeta object.

---

# MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* **Callsign:** RH-FORCE
* **Result classification:** **PASS** (forceability + resonance robustness achieved for a concrete \(\mathfrak B\), with explicit \(c_0=\pi/2\); UE/gate passing remains external by design).
* **Target gaps closed (by ID):**
  * **OPEN-GEO(1) Forceability:** satisfied on \(\mathfrak B^{\rm pole}\) with \(c_0=\pi/2\).
  * **OPEN-GEO(3) Resonance robustness (forcing side):** satisfied via pair-isolation shrink within \(\mathfrak B^{\rm pole}\).
* **Target gaps still open (by ID):**
  * **OPEN-GEO(2) UE bound (gate passing)** for the *same* contour family \(\mathfrak B^{\rm pole}\) (ENVELOPE/LOCAL responsibility).
* **Key conclusions (≤5 bullets):**
  1. The correct way to obtain \(\Omega(1)\) defect forcing is to force on a contour where \(\mathcal Q_a\) has a *genuine pole*, not to difference in \(a\) at micro-step \(h\asymp\delta\).
  2. The pole-centered witness family \(B^{\rm pole}(a,m,\delta)\) makes forcing topological: \(|\Delta_{\partial B}\arg \mathcal Q_a|=2\pi N_P\).
  3. This yields a clean \(\pi/2\) side increment lower bound for the defect phase endpoint \(\Phi^{\rm pole}_B(a)\) on some side.
  4. Forcing is tilt-sensitive: \(a=0\Rightarrow \mathcal Q_a\equiv 1\Rightarrow\) no forcing.
  5. Remaining program obligation is an admissible-class UE upper bound for \(\Phi^{\rm pole}_B(a)\) on the same contour family.
* **Paste-ready manuscript edits (TeX blocks):**
  (i) **Revised / new definitions**
  ```tex
  % --- Defect pole-box geometry (RH-FORCE; v41 insertion) ---
  \begin{definition}[Defect quotient/log-derivative]\label{def:defect-quotient}
  Fix $a>0$. Define
  \[
    \mathcal Q_a(v):=\frac{E(v+a)}{E(v-a)},\qquad
    \mathcal L_a(v):=\frac{\mathcal Q_a'(v)}{\mathcal Q_a(v)}
    =\frac{E'}{E}(v+a)-\frac{E'}{E}(v-a),
  \]
  whenever the expressions are defined.
  \end{definition}

  \begin{definition}[$\kappa$--admissibility for defect objects]\label{def:kappa-adm-defect}
  Let $B\subset\C$ be a closed box of $\ell^\infty$-radius $\delta>0$ and fix $\kappa\in(0,1/10)$.
  We say $B$ is \emph{$\kappa$--admissible for $\mathcal Q_a$} if
  \[
    \dist\!\bigl(\partial B,\ Z(E(\cdot-a))\cup Z(E(\cdot+a))\bigr)\ \ge\ \kappa\delta.
  \]
  In particular $\mathcal Q_a$ is holomorphic and nonvanishing on a $\kappa\delta$--collar neighborhood
  of $\partial B$.
  \end{definition}

  \begin{definition}[Pole-box witness family]\label{def:pole-box-family}
  Let $a>0$, $m>0$, and let $\delta_0>0$ be a nominal scale (e.g. $\delta_0=\eta a/(\log m)^2$).
  For $0<\delta\le \delta_0$ define the pole-centered box
  \[
    B^{\rm pole}(a,m,\delta)\ :=\ \{v\in\C:\ \|v-(2a+im)\|_\infty\le \delta\}.
  \]
  Let $\mathfrak B^{\rm pole}(a,m,\delta_0)$ be the collection of such boxes with $0<\delta\le \delta_0$
  that are $\kappa$--admissible for $\mathcal Q_a$ (Definition~\ref{def:kappa-adm-defect}).
  \end{definition}

  \begin{definition}[Defect phase endpoint on pole boxes]\label{def:defect-phase-endpoint-pole}
  Let $B\in\mathfrak B^{\rm pole}(a,m,\delta_0)$. Let $B_{\kappa/2}$ be the buffered inner rectangle and
  write $\partial B_{\kappa/2}=\bigsqcup_{j=1}^4 S_j$ (counterclockwise).
  Define
  \[
    \Phi^{\rm pole}_B(a)\ :=\ \max_{1\le j\le 4}\left|\Im\int_{S_j}\mathcal L_a(v)\,dv\right|.
  \]
  \end{definition}
  ```
  (ii) **Lemma statement + proof**
  ```tex
  \begin{lemma}[Defect pole-box forcing]\label{lem:defect-pole-forcing}
  Assume $E(a+im)=0$ with $a>0$. Let $\delta_0>0$ be any nominal scale.
  Then there exists $\delta\in(0,\delta_0]$ such that $B:=B^{\rm pole}(a,m,\delta)\in\mathfrak B^{\rm pole}(a,m,\delta_0)$ and
  \[
    \Phi^{\rm pole}_B(a)\ \ge\ \frac{\pi}{2}.
  \]
  \end{lemma}

  \begin{proof}
  Since $E(a+im)=0$, the defect quotient $\mathcal Q_a(v)=E(v+a)/E(v-a)$ has a pole at
  $v_\star:=2a+im$ because $E(v_\star-a)=E(a+im)=0$.
  Zeros and poles of $\mathcal Q_a$ are isolated, so choose $\varepsilon>0$ such that the closed box
  $\overline{B(v_\star,\varepsilon)}$ contains no zeros of $E(\cdot+a)$ and contains no zeros of $E(\cdot-a)$
  except those at $v_\star$ (with multiplicity).
  Set $\delta:=\min\{\delta_0,\varepsilon/(1+\kappa)\}$ and let $B:=B^{\rm pole}(a,m,\delta)$.
  Then $B$ is $\kappa$--admissible for $\mathcal Q_a$ and $B_{\kappa/2}$ contains at least one pole and no zeros of $\mathcal Q_a$.
  By the argument principle,
  \[
    \left|\Im\int_{\partial B_{\kappa/2}}\frac{\mathcal Q_a'}{\mathcal Q_a}\,dv\right|
    =2\pi\,N_P(\mathcal Q_a;B_{\kappa/2})\ \ge\ 2\pi.
  \]
  Writing $\partial B_{\kappa/2}=\bigsqcup_{j=1}^4 S_j$ and using the triangle inequality gives
  $2\pi \le 4\max_j\left|\Im\int_{S_j}\mathcal L_a(v)\,dv\right|$, hence $\Phi^{\rm pole}_B(a)\ge \pi/2$.
  \end{proof}
  ```
  (iii) **Edit to the Geometry Change Requirement box (optional short insertion)**
  ```tex
  \medskip
  \noindent\textbf{Forced witness family (available now).}
  One concrete forcing-compatible choice for criterion (1) is the \emph{pole-box} family
  $\mathfrak B^{\rm pole}(a,m,\delta_0)$ (Definition~\ref{def:pole-box-family}) together with the defect
  phase endpoint $\Phi^{\rm pole}_B(a)$ (Definition~\ref{def:defect-phase-endpoint-pole}).
  If $E$ has an off-axis quartet $\pm a\pm im$ with $a>0$, then Lemma~\ref{lem:defect-pole-forcing}
  produces $B\in\mathfrak B^{\rm pole}$ with $\Phi^{\rm pole}_B(a)\ge \pi/2$.
  (The remaining OPEN criterion is to prove a gate-passing UE upper bound on the \emph{same} family.)
  ```
* **Dependencies on other branches:**
  * **RH-ENVELOPE / RH-LOCAL:** must deliver OPEN-GEO(2): a gate-passing UE upper bound for \(\Phi^{\rm pole}_B(a)\) (or a comparable upper control) on \(\mathfrak B^{\rm pole}\) with \(\delta\)-uniform constants.
  * **RH-ABSORB:** must confirm how \(\Phi^{\rm pole}_B(a)\) is integrated into the budget theorem (if it replaces/augments existing forced endpoints).
* **Referee risk notes (anticipated objections + how addressed):**
  1. **“You moved the contour outside the strip (\(\Re v\) up to \(2a\)).”**  
     Addressed: \(E\) is entire in \(v\); the argument principle and defect quotient are valid on any \(\kappa\)-admissible box. (However: UE/growth bounds may change with \(\Re v\); that is explicitly left to OPEN-GEO(2).)
  2. **“Resonant extra quartets could cancel winding.”**  
     Addressed: pair isolation/shrink ensures a witness box exists containing a pole and no zeros of \(\mathcal Q_a\), making the winding nonzero and quantized.
  3. **“This is just ‘interior zero ⇒ winding’ again.”**  
     Addressed: tilt sensitivity: when \(a=0\), \(\mathcal Q_a\equiv 1\) and the endpoint is identically zero; the forcing is driven by the *tilt-shifted pole* at \(2a+im\).
