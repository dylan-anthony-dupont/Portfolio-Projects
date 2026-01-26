# Batch 9 — RH-LOCAL  
**Callsign:** RH-LOCAL  
**Mission:** Local factorization / cancellation story for the defect objects  
\[
\mathcal Q_a(v)=\frac{E(v+a)}{E(v-a)},\qquad 
\mathcal L_a(v)=\frac{E'}{E}(v+a)-\frac{E'}{E}(v-a)=\partial_v\log \mathcal Q_a(v),
\]
so the defect endpoint is **zero-neutral** (not topologically forced by one interior zero) but **tilt-sensitive** (depends on the horizontal displacement \(a=2\beta-1\)).  

This note is written to be *drop‑in* compatible with the v‑frame conventions and \(\delta\)-policy
\[
\delta_0=\frac{\eta a}{(\log m)^2},\qquad a=2\beta-1,\quad m=2\gamma.
\]

---

## 0) Frame mapping + symmetry hypotheses (RH‑free)

### 0.1 s→u→v mapping
We work in the centered width‑2 frame:
\[
u:=2s,\qquad v:=u-1,\qquad s=\frac{1+v}{2}.
\]
A nontrivial zero \(s_\rho=\beta+i\gamma\) corresponds to
\[
v_\rho=(2\beta-1)+i(2\gamma)=a+im,
\]
so **off‑critical‑line** is **\(\Re(v_\rho)\neq 0\)** (equivalently \(\beta\neq \tfrac12\)).  

### 0.2 Completed object and evenness (what must be hardened)
In v38 the completed object is presented in the centered \(v\)-frame as
\[
E(v):=\Xi_2(1+v),\qquad \Xi_2(u):=\xi(u/2),
\]
with \(\xi\) the Riemann \(\xi\)-function. 【784:1†manuscript_v38.pdf†L16-L18】

From the functional equation \(\xi(s)=\xi(1-s)\), one gets
\[
\Xi_2(u)=\Xi_2(2-u)\quad\Rightarrow\quad E(v)=E(-v).
\]
Complex conjugation gives the standard reality condition
\[
E(\overline v)=\overline{E(v)}.
\]
**Referee note:** older manuscript versions sometimes wrote \(E(v)=E(\overline v)\); the correct statement is \(E(\overline v)=\overline{E(v)}\).

### 0.3 Quartet symmetry (what we use locally)
From \(E(-v)=E(v)\) and \(E(\overline v)=\overline{E(v)}\): if \(E(\rho)=0\) then \(E(-\rho)=E(\overline\rho)=E(-\overline\rho)=0\), with **equal multiplicity**.

---

## A) Local quartet model (mandatory)

### Lemma A.1 (Local quartet factorization near the *top pair*)
Assume \(E\) is holomorphic on a neighborhood of \(v=im\) and has zeros at
\[
\rho_\pm := \pm a + i m\qquad (a>0,\ m>0)
\]
of common multiplicity \(r\ge 1\). (This common multiplicity follows from the symmetries in §0.3.)

Then there exists a holomorphic function \(G\) on a neighborhood of \(v=im\) with \(G(im)\neq 0\) such that
\[
E(v)=\bigl((v-im)^2-a^2\bigr)^r\,G(v)
\]
throughout that neighborhood.

#### Proof sketch (local analytic factorization)
Near \(\rho_+\), write \(E(v)=(v-\rho_+)^r h_+(v)\) with \(h_+(\rho_+)\neq 0\); similarly at \(\rho_-\).
Multiplying and absorbing the nonvanishing factors into \(G\) yields
\[
E(v)=(v-\rho_+)^r(v-\rho_-)^rG(v)=\bigl((v-im)^2-a^2\bigr)^rG(v).
\]
\(\square\)

---

## B) Cancellation check (mandatory)

### Lemma B.1 (Defect quotient \(\mathcal Q_a\) is *removable* at the aligned point)
Under the hypotheses of Lemma A.1, define
\[
\mathcal Q_a(v):=\frac{E(v+a)}{E(v-a)}.
\]
Then \(\mathcal Q_a\) admits a holomorphic, nonvanishing extension to a neighborhood of \(v=im\).  
Moreover, in that neighborhood,
\[
\mathcal Q_a(v)
=\Bigl(\frac{v-im+2a}{\,v-im-2a\,}\Bigr)^r\cdot \frac{G(v+a)}{G(v-a)}.
\]
In particular, the singular \(0/0\) at \(v=im\) cancels.

#### Proof (direct substitution using Lemma A.1)
Using \(E(v)=((v-im)^2-a^2)^rG(v)\),
\[
E(v+a)=\bigl((v-im+a)^2-a^2\bigr)^rG(v+a)=\bigl((v-im)(v-im+2a)\bigr)^rG(v+a),
\]
\[
E(v-a)=\bigl((v-im-a)^2-a^2\bigr)^rG(v-a)=\bigl((v-im)(v-im-2a)\bigr)^rG(v-a).
\]
Divide to get the claimed formula; the factors \((v-im)^r\) cancel identically. \(\square\)

### Lemma B.2 (Forced-pair pole cancellation in \(\mathcal L_a\))
Define the defect log-derivative
\[
\mathcal L_a(v):=\frac{E'}{E}(v+a)-\frac{E'}{E}(v-a)=\partial_v\log\mathcal Q_a(v).
\]
Under Lemma A.1, \(\mathcal L_a\) is holomorphic at \(v=im\) (no \(1/(v-im)\) pole), and
\[
\mathcal L_a(v)
=
r\Bigl(\frac{1}{v-im+2a}-\frac{1}{v-im-2a}\Bigr)
+\Bigl(\frac{G'}{G}(v+a)-\frac{G'}{G}(v-a)\Bigr).
\]
In particular, the “forced pair” singular residues cancel exactly.

#### Proof
Differentiate \(\log\mathcal Q_a(v)\) from Lemma B.1. \(\square\)

### Corollary B.3 (Unimodularity on the symmetry line; reality of \(\mathcal L_a\))
Assume also \(E(\overline v)=\overline{E(v)}\). Then for real \(y\) where \(E(iy\pm a)\neq 0\),
\[
E(iy-a)=E(a-iy)=\overline{E(a+iy)}=\overline{E(iy+a)}\quad\Rightarrow\quad |\mathcal Q_a(iy)|=1.
\]
Hence \(\mathcal Q_a(iy)=e^{i\theta(y)}\) and \(\mathcal L_a(iy)\in\mathbb R\) (as a function of \(y\)).

**Referee note:** This is the key “phase-class compatibility” property: \(\mathcal Q_a\) is a unit-modulus defect on the symmetry line.

---

## C) Local contribution bound under the \(\delta\)-policy (mandatory)

### C.1 What endpoint is being bounded (LOCAL’s choice)
For a defect **phase** endpoint centered on the symmetry line, a canonical choice is
\[
\Phi_B^{\rm def}(\mathcal L_a)\ :=\ \left|\Im\int_{I_0(m,\delta)} \mathcal L_a(v)\,dv\right|,
\qquad
I_0(m,\delta):=\{v=iy:\ |y-m|\le \delta\}.
\]
Using Corollary B.3, \(\mathcal L_a(iy)\in\mathbb R\), so
\[
\Im\!\left(\mathcal L_a(iy)\,i\,dy\right)=\mathcal L_a(iy)\,dy,\qquad
\Phi_B^{\rm def}(\mathcal L_a)=\left|\int_{m-\delta}^{m+\delta} \mathcal L_a(iy)\,dy\right|.
\]

### Lemma C.1 (Forced-pair contribution is \(O(\delta/a)\); vanishes at \(\delta_0=\eta a/(\log m)^2\))
In the quartet model Lemma A.1, isolate the “pair part”
\[
\mathcal L_a^{\rm pair}(v):=
r\Bigl(\frac{1}{v-im+2a}-\frac{1}{v-im-2a}\Bigr)
= -\frac{4ar}{(v-im)^2-4a^2}.
\]
Then for \(v=iy\) on the symmetry line:
\[
\mathcal L_a^{\rm pair}(iy)=\frac{4ar}{(y-m)^2+4a^2}\ \ge 0.
\]
Consequently, for any \(\delta>0\),
\[
\int_{m-\delta}^{m+\delta} \mathcal L_a^{\rm pair}(iy)\,dy
=4r\arctan\!\Bigl(\frac{\delta}{2a}\Bigr)\ \le\ 2r\frac{\delta}{a}.
\]
In particular, under the policy \(\delta=\delta_0=\eta a/(\log m)^2\),
\[
\int_{m-\delta_0}^{m+\delta_0} \mathcal L_a^{\rm pair}(iy)\,dy
\le \frac{2r\eta}{(\log m)^2}\ \xrightarrow[m\to\infty]{}\ 0.
\]

**Interpretation:** the aligned quartet does **not** force a fixed \(\Omega(1)\) phase increment in the defect endpoint; its local contribution **vanishes** at the program’s \(\delta_0\)-scale.

### Forced-zero obstruction (explicitly addressed)
For the defect quotient \(\mathcal Q_a(v)=E(v+a)/E(v-a)\), an interior quartet at \(\pm a\pm im\) contributes **matched zeros** to numerator and denominator after shifting. Thus \(\mathcal Q_a\) has no zero/pole at the aligned point \(v=im\) (Lemma B.1), and on a sufficiently small defect box \(B_0(im,\delta)\) with \(\delta\ll a\), \(\mathcal Q_a\) is holomorphic and nonvanishing. Therefore the argument principle gives **zero winding**:
\[
\Delta_{\partial B_0}\arg \mathcal Q_a \;=\;0,
\]
so the defect endpoint is **not topologically forced** by a single interior zero of \(E\). (This is exactly the desired “zero‑neutrality” property.)

---

## D) What replaces \(N_{\rm loc}\) (mandatory)

### D.1 Natural near-count for the defect log-derivative
The poles of \(\mathcal L_a(v)\) occur at points \(v=\rho-a\) and \(v=\rho+a\) where \(\rho\) ranges over zeros of \(E\).
For a defect box centered at \(im\) of half-side \(\delta\), define the “near” set of zeros:
\[
\mathcal Z_{\rm near}(m;a,\delta)
:=\Bigl\{\rho:\ E(\rho)=0,\ \rho\in (B_0(im,\delta)+a)\ \cup\ (B_0(im,\delta)-a)\Bigr\},
\]
and the count (with multiplicity)
\[
N_{\rm near}(m;a,\delta):=\sum_{\rho\in\mathcal Z_{\rm near}(m;a,\delta)} m_\rho.
\]
This is the correct substitute for \(N_{\rm loc}\) **for defect objects**, because only zeros whose shifted images enter the defect box can create large contributions.

### D.2 What can be proven unconditionally *without* new short-interval input
Without importing new short-interval zero-density theorems, the safe statement is the inclusion
\[
\mathcal Z_{\rm near}(m;a,\delta)\subseteq
\{\rho:\ |\,\Im\rho-m\,|\le 1\},
\]
whenever \(\delta\le 1\). Hence
\[
N_{\rm near}(m;a,\delta)\ \le\ N_{\rm loc}(m)
:=\sum_{\substack{E(\rho)=0\\ |\Im\rho-m|\le 1}} m_\rho.
\]
In v38, \(N_{\rm loc}(m)\) is explicitly bounded by a \(\log m\) inequality (Lemma 10.10 / Cor. 10.11). 【801:0†manuscript_v38.pdf†L420-L468】

**Local upshot for the defect mechanism:** the forced quartet itself does not require \(N_{\rm near}\) (it cancels at \(v=im\)), but any global defect endpoint will need either  
(i) a way to avoid dependence on \(N_{\rm near}\), or  
(ii) accept \(N_{\rm near}\lesssim \log m\) and ensure the UE/absorption budget includes a compensating \(\delta\)-gain.

---

## E) S6 explicit-formula mapping (mandatory)

A zero \(s_\rho=\beta+i\gamma\) contributes to the explicit formula for \(\psi(x)\) a term of size
\[
\sim \frac{x^\beta}{|\rho|}\cos(\gamma\log x+\cdots),
\]
so the **amplitude leak** is controlled by \(\beta\), equivalently by
\[
a=2\beta-1>0\quad\Longleftrightarrow\quad \beta=\frac{1+a}{2}>\frac12.
\]
Under the frame map \(s=(1+v)/2\), the defect quotient compares \(\xi\) at horizontal shifts:
\[
\mathcal Q_a(v)=\frac{E(v+a)}{E(v-a)}
=\frac{\xi\!\left(\frac{1+v+a}{2}\right)}{\xi\!\left(\frac{1+v-a}{2}\right)}.
\]
So \(\mathcal Q_a\) (and \(\mathcal L_a=\partial_v\log\mathcal Q_a\)) is, morally, a **finite-difference probe in the \(\sigma\)-direction**, which is the direction that controls amplitude \(x^\beta\).

**However:** the local quartet computation shows the singular forcing from an off-axis quartet cancels in \(\mathcal L_a\) at the aligned point (Lemma B.2) and its phase contribution on the \(\delta_0\)-scale vanishes (Lemma C.1).  
Therefore, any “amplitude-leak detection” by defect endpoints must come from **nonlocal** structure (e.g., how the defect interacts with outer factors / envelopes), not from a topologically forced local spike.

---

# MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* **Callsign:** RH-LOCAL
* **Result classification:** **CONDITIONAL**
* **Target gaps closed (by ID):** (local component for defect program) **NEW‑LOCAL‑DEFECT** (not previously numbered); supports “forced‑zero obstruction” gate in Batch‑9 prompt
* **Target gaps still open (by ID):** depends on Control Room numbering; likely the global “defect endpoint UE budget” and any required \(N_{\rm near}\) elimination
* **Key conclusions (≤5 bullets):**
  1. Under quartet symmetry, \(E(v)\) factors locally as \(((v-im)^2-a^2)^rG(v)\) near the aligned point.
  2. The defect quotient \(\mathcal Q_a(v)=E(v+a)/E(v-a)\) is **holomorphic and nonzero** at \(v=im\); the \(0/0\) cancels.
  3. The defect log derivative \(\mathcal L_a(v)=E'/E(v+a)-E'/E(v-a)\) has **no pole at \(v=im\)**; residues cancel exactly.
  4. The forced quartet’s contribution to the defect phase endpoint on a \(\delta_0=\eta a/(\log m)^2\) window is \(O(\eta/(\log m)^2)\to 0\): **zero-neutrality** is achieved.
  5. Any remaining dependence on “many zeros near height \(m\)” must be routed through a new near-count \(N_{\rm near}(m;a,\delta)\), which is only safely bounded by \(N_{\rm loc}(m)\lesssim \log m\) absent new short-interval inputs.
* **Paste-ready manuscript edits (TeX blocks):**

  **(i) Revised lemma/proposition statements**
  ```tex
  % --- Defect objects (Batch-9 / v39 prebuild candidate) ---
  \begin{definition}[Defect quotient and defect log-derivative]
  Fix $a>0$. For the completed even object $E$ in the centered $v$-frame, define
  \[
    \mathcal Q_a(v):=\frac{E(v+a)}{E(v-a)},\qquad
    \mathcal L_a(v):=\partial_v\log \mathcal Q_a(v)
    =\frac{E'}{E}(v+a)-\frac{E'}{E}(v-a).
  \]
  \end{definition}

  \begin{lemma}[Local quartet factorization near the aligned point]\label{lem:defect-local-factor}
  Assume $E$ is holomorphic near $v=im$ and has zeros at $\rho_\pm:=\pm a+im$ of common multiplicity $r\ge 1$.
  Then there exists a holomorphic $G$ with $G(im)\neq 0$ such that
  \[
    E(v)=\bigl((v-im)^2-a^2\bigr)^r\,G(v)
  \]
  throughout a neighborhood of $v=im$.
  \end{lemma}

  \begin{lemma}[Defect cancellation at the aligned point]\label{lem:defect-cancel}
  Under Lemma \ref{lem:defect-local-factor}, $\mathcal Q_a$ admits a holomorphic, nonvanishing extension to $v=im$ and
  \[
    \mathcal Q_a(v)=\Bigl(\frac{v-im+2a}{v-im-2a}\Bigr)^r\cdot \frac{G(v+a)}{G(v-a)}.
  \]
  Consequently $\mathcal L_a$ is holomorphic at $v=im$ and
  \[
    \mathcal L_a(v)
    =
    r\Bigl(\frac{1}{v-im+2a}-\frac{1}{v-im-2a}\Bigr)
    +\Bigl(\frac{G'}{G}(v+a)-\frac{G'}{G}(v-a)\Bigr).
  \]
  \end{lemma}

  \begin{lemma}[Forced-pair contribution on the $\delta_0$-scale]\label{lem:defect-pair-delta0}
  In the quartet model of Lemma \ref{lem:defect-local-factor}, the pair part
  \[
    \mathcal L_a^{\rm pair}(v)
    :=r\Bigl(\frac{1}{v-im+2a}-\frac{1}{v-im-2a}\Bigr)
    =-\frac{4ar}{(v-im)^2-4a^2}
  \]
  satisfies for $v=iy$:
  \[
    \int_{m-\delta}^{m+\delta}\mathcal L_a^{\rm pair}(iy)\,dy
    =4r\arctan\!\Bigl(\frac{\delta}{2a}\Bigr)\le 2r\frac{\delta}{a}.
  \]
  In particular, for $\delta_0=\eta a/(\log m)^2$ one has
  \[
    \int_{m-\delta_0}^{m+\delta_0}\mathcal L_a^{\rm pair}(iy)\,dy
    \le \frac{2r\eta}{(\log m)^2}.
  \]
  \end{lemma}
  ```

  **(ii) Revised definitions/remarks**
  ```tex
  \begin{remark}[Zero-neutrality / no forced winding for the defect quotient]\label{rem:defect-no-forcing}
  Unlike $\Delta_{\partial B}\arg E$, the defect quotient $\mathcal Q_a(v)=E(v+a)/E(v-a)$ is not topologically forced
  by a single interior zero of $E$: in the aligned quartet configuration $\pm a\pm im$, the shifted numerator and
  denominator contribute matched zeros and $\mathcal Q_a$ is holomorphic and nonvanishing at the aligned point $v=im$
  (Lemma \ref{lem:defect-cancel}). Hence on sufficiently small defect boxes $B_0(im,\delta)\ll a$ one has
  $\Delta_{\partial B_0}\arg \mathcal Q_a =0$ by the argument principle.
  \end{remark}

  \begin{definition}[Near-count for defect poles]\label{def:Nnear}
  For a defect box $B_0(im,\delta):=[-\delta,\delta]\times[m-\delta,m+\delta]$ define
  \[
    \mathcal Z_{\rm near}(m;a,\delta)
    :=\{\rho:\ E(\rho)=0,\ \rho\in(B_0(im,\delta)+a)\cup(B_0(im,\delta)-a)\},
  \]
  and let $N_{\rm near}(m;a,\delta):=\sum_{\rho\in\mathcal Z_{\rm near}} m_\rho$.
  \end{definition}
  ```

  **(iii) Revised theorem/inequality lines**
  ```tex
  % Typical insertion point in the endpoint budget:
  % the local forced-pair term contributes only O(\delta/a)=O(1/(\log m)^2) on the defect scale.
  By Lemma~\ref{lem:defect-pair-delta0}, the forced quartet contributes at most
  \[
    \Phi^{\rm def}_B(\mathcal L_a^{\rm pair})
    \le \frac{2r\eta}{(\log m)^2},
  \]
  hence it is $\delta_0$-subcritical and creates no $\delta^{-1}$ collar blow-up.
  ```

* **Dependencies on other branches:**
  - ENVELOPE/ABSORB must specify the exact defect endpoint \(\Phi_B\) used; Lemma C.1 is written for the canonical phase integral on the symmetry line but can be reparameterized for any curve of length \(O(\delta)\) in the defect box.
  - FORCE must decide what forcing architecture applies to defect endpoints, since the argument-principle forcing is intentionally removed (zero-neutrality).
* **Referee risk notes (anticipated objections + how addressed):**
  1. **“You used \(E(v)=E(\overline v)\)”** — explicitly corrected: only \(E(\overline v)=\overline{E(v)}\) is used (§0.2).
  2. **Multiplicity mismatch** — shown ruled out by symmetry; Lemma A.1 assumes common multiplicity \(r\) and notes its symmetry provenance.
  3. **Branch/log issues** — \(\mathcal L_a=\partial_v\log\mathcal Q_a\) is branch-independent where \(\mathcal Q_a\neq 0\); and Lemma B.1 shows removability at the aligned point.
  4. **Hidden use of RH** — avoided: the quartet is described in v-frame terms (\(\Re(v_\rho)=\pm a\neq 0\)), not by “zeros on \(\Re(s)=1/2\)”.
