# batch9_RH-FORCE.md

## Batch 9 — RH-FORCE  
**Mission:** forceability for the *defect endpoint* built from  
\[
\mathcal Q_a(v):=\frac{E(v+a)}{E(v-a)},\qquad 
\mathcal L_a(v):=\frac{E'}{E}(v+a)-\frac{E'}{E}(v-a)=\partial_v\log \mathcal Q_a(v).
\]

This response is **forcing-only**: it supplies a proof-grade forcing lemma (or a no-go) for a defect-phase endpoint. It does **not** attempt envelope/UE/local-term bounds.

---

## 1) Frame map (mandatory s→u→v)

* **s-frame:** \(s=\sigma+it\).  
* **u-frame (width–2):** \(u:=2s\).  
* **v-frame (centered):** \(v:=u-1\), so \(u=1+v\), \(s=\tfrac{1+v}{2}\).

A nontrivial zero \(\rho=\beta+i\gamma\) corresponds to  
\[
u_\rho=2\rho=(1+a)+im,\qquad v_\rho=u_\rho-1=a+im,
\]
with
\[
a:=2\beta-1\in(-1,1),\qquad m:=2\gamma>0.
\]
“Off critical line” is exactly \(a\neq 0\) (equivalently \(\beta\neq\tfrac12\)).  

---

## 2) The defect objects and their symmetry (mandatory)

Let \(E(v)\) denote the centered entire completion (\(E(v)=E(-v)\)). Define

\[
\mathcal Q_a(v):=\frac{E(v+a)}{E(v-a)},\qquad 
\mathcal L_a(v):=\frac{\mathcal Q_a'(v)}{\mathcal Q_a(v)}=\frac{E'}{E}(v+a)-\frac{E'}{E}(v-a).
\]

### 2.1 Symmetry under \(v\mapsto -v\)

Using evenness \(E(-v)=E(v)\) and oddness of the log-derivative \(E'(-v)/E(-v)=-E'(v)/E(v)\):

* \(\mathcal Q_a(-v)=\dfrac{E(-v+a)}{E(-v-a)}=\dfrac{E(v-a)}{E(v+a)}=\mathcal Q_a(v)^{-1}\).
* \(\mathcal L_a(-v)=\dfrac{E'}{E}(-v+a)-\dfrac{E'}{E}(-v-a)=\mathcal L_a(v)\) (so \(\mathcal L_a\) is even).

These identities matter because they explain why certain *symmetric* contours can have cancelling phase increments; the forcing contour below is **not symmetric**.

---

## 3) Endpoint functional to be forced (mandatory: specify Φ_B)

I will force a **boundary phase endpoint** for \(\mathcal Q_a\), expressed via \(\mathcal L_a\) to avoid branch choices.

Let \(B\subset\mathbb C\) be a rectangle/box and let \(\mathcal S(B)\) be the set of its four oriented sides. For a meromorphic \(f\) with **no zeros/poles on \(\partial B\)** define
\[
\Phi_B(f)\;:=\;\max_{S\in\mathcal S(B)}\left|\Im\int_{S}\frac{f'(v)}{f(v)}\,dv\right|
=\max_{S\in\mathcal S(B)}|\Delta_S\arg f|.
\]
For \(f=\mathcal Q_a\) we have \(f'/f=\mathcal L_a\).

This is in the same *boundary phase* structural class as the legacy forcing (short-side \(\Delta\arg\) forcing), but it is attached to the defect quotient rather than \(W\).

---

## 4) Where tilt creates a forced singularity (key mechanism)

### 4.1 Transport of zeros of \(E\) to poles/zeros of \(\mathcal Q_a\)

If \(E(\rho)=0\) (multiplicity \(\mu\)), then:

* \(E(v-a)=0\) at \(v=\rho+a\) (same multiplicity \(\mu\)), hence \(\mathcal Q_a\) has a **pole** at \(v=\rho+a\) (unless canceled by a numerator zero at the same point).
* \(E(v+a)=0\) at \(v=\rho-a\), hence \(\mathcal Q_a\) has a **zero** at \(v=\rho-a\) (unless canceled).

In particular, if there is an off-axis zero at \(v_\rho=a+im\) (so \(a>0\)), then:
\[
E(a+im)=0\quad\Longrightarrow\quad \mathcal Q_a \text{ has a pole at } (a+im)+a = 2a+im,
\]
provided \(E(3a+im)\neq 0\) (to prevent cancellation).

This is the core “tilt forcing” mechanism: the **presence of tilt \(a>0\)** transports a zero of \(E\) to a **pole of \(\mathcal Q_a\)** at a shifted location.

---

## 5) The defect-scale box and δ-policy (mandatory)

We adopt the defect scale:
\[
\delta_0=\delta_0(a,m):=\frac{\eta a}{(\log m)^2},\qquad 0<\eta<1,
\]
and work at \(0<\delta\le \delta_0\).

Define the **defect pole box**
\[
B_{\mathrm{def}}(a,m,\delta):=B(2a,m,\delta)
=\{v\in\mathbb C:\ |\Re v-2a|\le \delta,\ |\Im v-m|\le \delta\}.
\]

This box is **not** the old “aligned box around the zero” \(B(a,m,\delta)\). It is centered at the *transported pole location* \(2a+im\).

---

## 6) Forcing lemma (decision-grade; π/2-type constant)

### 6.1 Extremal-tilt selection (to prevent pole cancellation)

To make the pole at \(2a+im\) unconditional, we select \(a\) as **locally extremal**.

> **Extremal tilt hypothesis (standard WLOG move):**  
> Fix a height \(m>0\) for which there is at least one off-axis zero \(v=\Re v+i\Im v\) of \(E\) with \(|\Im v-m|\le 1\).  
> Let  
> \[
> a:=\max\{\,|\Re v|:\ E(v)=0,\ |\Im v-m|\le 1\,\}\in(0,1).
> \]
> Then \(E\) has a zero at \(a+im_0\) for some \(m_0\) with \(|m_0-m|\le 1\), and by shrinking the window center we may (re)name \(m:=m_0\).

This is the usual “choose a worst-case quartet in the local window” move: it does **not** add strength; it just chooses the most dangerous configuration.

With this choice, any would-be cancellation of the pole at \(2a+im\) would require a numerator zero at \(v=2a+im\), i.e. \(E(3a+im)=0\), which contradicts extremality since \(3a>a\) and \(|\Im(3a+im)-m|=0\le 1\).

---

### 6.2 Lemma statement

> **Lemma (Defect forcing via pole-winding).**  
> Let \(E\) be the centered entire completion with evenness \(E(v)=E(-v)\).  
> Assume there exists an off-axis quartet in the local window \(|\Im v-m|\le 1\), and let \(a>0\) be the **extremal tilt** in that window as above.  
> Define \(\mathcal Q_a,\mathcal L_a\) as in §2 and \(B_{\mathrm{def}}(a,m,\delta)\) as in §5 with \(0<\delta\le\delta_0(a,m)\).  
> Assume \(\partial B_{\mathrm{def}}\) contains **no zeros or poles** of \(\mathcal Q_a\) (i.e. the defect box is collar-admissible for \(\mathcal Q_a\)).  
> Then:
> 1. \(\mathcal Q_a\) has at least one **pole** in \(B_{\mathrm{def}}\) and **no zeros** in \(B_{\mathrm{def}}\).  
> 2. The boundary phase endpoint obeys the uniform forcing lower bound
>    \[
>    \Phi_{B_{\mathrm{def}}}(\mathcal Q_a)\ \ge\ \frac{\pi}{2},
>    \qquad\text{equivalently}\qquad
>    \Phi_{B_{\mathrm{def}}}(\mathcal L_a)\ \ge\ \frac{\pi}{2}.
>    \]
> In particular, the lower bound does **not** vanish under the δ-policy \(\delta\le\eta a/(\log m)^2\).

#### Proof (audit-grade, minimal)

1. Because \(E(a+im)=0\), the denominator \(E(v-a)\) vanishes at \(v=2a+im\), so \(\mathcal Q_a\) has a pole there unless canceled.
2. By extremality of \(a\), \(E(3a+im)\neq 0\), so there is no cancellation. Hence \(2a+im\) is a pole of \(\mathcal Q_a\) inside \(B_{\mathrm{def}}\).
3. Any zero of \(\mathcal Q_a\) in \(B_{\mathrm{def}}\) would require a zero of \(E(v+a)\) in the translated region \(v+a\in B(3a,m,\delta)\), i.e. a zero of \(E\) with real part near \(3a>a\) and height within \(\delta\le 1\) of \(m\), contradicting extremality. Thus \(\mathcal Q_a\) has no zeros in \(B_{\mathrm{def}}\).
4. By the argument principle (applied to the meromorphic function \(\mathcal Q_a\) on \(B_{\mathrm{def}}\) with no boundary singularities),
   \[
   \int_{\partial B_{\mathrm{def}}}\frac{\mathcal Q_a'(v)}{\mathcal Q_a(v)}\,dv
   =2\pi i\,(N_Z-N_P),
   \]
   where \(N_Z\) and \(N_P\) are the numbers of zeros and poles of \(\mathcal Q_a\) inside \(B_{\mathrm{def}}\), counted with multiplicity.
   Here \(N_Z=0\) and \(N_P\ge 1\), so
   \[
   \Im\int_{\partial B_{\mathrm{def}}}\mathcal L_a(v)\,dv
   =\Im\int_{\partial B_{\mathrm{def}}}\frac{\mathcal Q_a'}{\mathcal Q_a}\,dv
   =-2\pi N_P.
   \]
5. Decomposing \(\partial B_{\mathrm{def}}\) into its four sides \(S_1,\dots,S_4\), we have
   \[
   \sum_{j=1}^4 \Im\int_{S_j}\mathcal L_a(v)\,dv = -2\pi N_P,
   \]
   hence by pigeonhole,
   \[
   \max_{1\le j\le 4}\left|\Im\int_{S_j}\mathcal L_a(v)\,dv\right|
   \ge \frac{2\pi N_P}{4}\ge \frac{\pi}{2}.
   \]
   This is exactly \(\Phi_{B_{\mathrm{def}}}(\mathcal L_a)\ge \pi/2\), equivalently \(\Phi_{B_{\mathrm{def}}}(\mathcal Q_a)\ge \pi/2\).

∎

---

## 7) Forced-zero obstruction check (mandatory)

**Why this is not “interior zero ⇒ winding” in disguise.**

If you take the *old* aligned box around the zero \(v=a+im\), the defect quotient is designed to **cancel** that quartet contribution:

* At \(v=im\), both \(E(v+a)=E(a+im)=0\) and \(E(v-a)=E(-a+im)=0\), so \(\mathcal Q_a\) has a removable \(0/0\) structure there (and \(\mathcal L_a\) is regular).
* Consequently, a box enclosing \(a+im\) does **not** topologically force any winding of \(\mathcal Q_a\).

The forcing above uses a **different** topological witness: the transported pole at \(v=2a+im\), which exists only when \(a\neq 0\). That is “tilt forcing,” not mere “zero existence.”

---

## 8) S6 explicit-formula interpretation (mandatory)

In the v-frame, the displacement \(a=\Re(v_\rho)=2\beta-1\) is exactly the real-part deviation \(\beta-\tfrac12\). Thus \(\beta=(1+a)/2\).  

In the classical explicit formula for prime counting functions, an off-axis zero \(\rho=\beta+i\gamma\) contributes terms of size roughly \(x^{\beta}\) (an “amplitude leak” compared to the \(x^{1/2}\) critical-line scale). Therefore, **any endpoint that is genuinely tilt-forced (detects \(a>0\)) is, at interpretation level, detecting the same off-axis parameter that controls amplitude leaks**.

That said, the forcing lemma here is *geometric/topological* (pole-winding of \(\mathcal Q_a\)) and does not directly quantify the size of an explicit-formula oscillation; it only certifies the presence of \(a\neq 0\) via a nontrivial phase defect.

---

## 9) Minimal integration notes for the program (what this does / does not solve)

* This provides a **non-vanishing (π/2) forcing lower bound** for a defect-phase endpoint built from \(\mathcal Q_a\) / \(\mathcal L_a\), under a clean extremal-tilt selection and collar-admissibility for \(\mathcal Q_a\).
* It does **not** address whether ENVELOPE can upper-control \(\Phi_{B_{\mathrm{def}}}(\mathcal Q_a)\) without pointwise UE. That remains ENVELOPE/LOCAL work.
* It shifts the forced box center from \(a+im\) to \(2a+im\). If the global contradiction chain is built around boxes centered at \(\alpha+im\) with \(\alpha\in(0,1]\), the manuscript must explicitly allow these defect boxes, or else the lemma is not usable in the tail chain.

---

## MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* **Callsign:** RH-FORCE  
* **Result classification:** **PASS** (defect endpoint is forceable with a uniform constant via pole-winding; no vanishing \(c_0\) under \(\delta=\eta a/(\log m)^2\))  
* **Target gaps closed (by ID):** *(new forcing target; not previously in G-1…G-12)* — “defect endpoint forceability”  
* **Target gaps still open (by ID):** G-4 (δ-uniform upper control), G-5 (κ-policy interactions), G-8 (local growth model), G-12 (theorem↔artifact alignment) — **not addressed here**  
* **Key conclusions (≤5 bullets):**
  1. Off-axis tilt \(a>0\) forces \(\mathcal Q_a\) to have a pole at \(2a+im\); choosing \(a\) as a local extremal tilt prevents cancellation.
  2. A defect box \(B_{\mathrm{def}}(a,m,\delta)=B(2a,m,\delta)\) yields a **π/2** forcing lower bound for a phase endpoint \(\Phi_{B_{\mathrm{def}}}(\mathcal Q_a)\) (equivalently for \(\mathcal L_a\)).
  3. The forcing is genuinely **tilt forced**: if \(a=0\), \(\mathcal Q_0\equiv 1\) and the endpoint is \(0\).
  4. This does **not** rely on the obsolete “interior zero ⇒ winding on the same box” mechanism; the quartet cancels in \(\mathcal Q_a\) on the original aligned box.
  5. To be usable, the global program must allow defect boxes centered at \(2a+im\) (and ENVELOPE must upper-control this endpoint).
* **Paste-ready manuscript edits (TeX blocks):**

  (i) **Revised definitions/endpoint functional**
  ```tex
  \begin{definition}[Defect quotient and defect log-derivative]
  Let $E(v)=\Xi_2(1+v)$ be the centered entire completion.  For $a>0$ define
  \[
    \mathcal Q_a(v):=\frac{E(v+a)}{E(v-a)},\qquad 
    \mathcal L_a(v):=\frac{\mathcal Q_a'(v)}{\mathcal Q_a(v)}
    =\frac{E'}{E}(v+a)-\frac{E'}{E}(v-a).
  \]
  \end{definition}

  \begin{definition}[Boundary phase endpoint for a meromorphic function]
  Let $B\subset\C$ be a box and let $\mathcal S(B)$ be the set of its four oriented sides.
  For a meromorphic function $f$ with no zeros or poles on $\partial B$ define
  \[
    \Phi_B(f):=\max_{S\in\mathcal S(B)}\left|\Im\int_S \frac{f'(v)}{f(v)}\,dv\right|.
  \]
  \end{definition}
  ```

  (ii) **Defect scale + defect box**
  ```tex
  \begin{definition}[Defect scale and defect pole box]
  Fix $\eta\in(0,1)$ and set
  \[
    \delta_0(a,m):=\frac{\eta a}{(\log m)^2}.
  \]
  For $0<\delta\le \delta_0(a,m)$ define the defect pole box
  \[
    B_{\mathrm{def}}(a,m,\delta):=B(2a,m,\delta)
    =\{v\in\C:\ |\Re v-2a|\le\delta,\ |\Im v-m|\le\delta\}.
  \]
  \end{definition}
  ```

  (iii) **Defect forcing lemma**
  ```tex
  \begin{lemma}[Defect forcing via pole-winding]
  Assume there exists an off-axis quartet in the local window $|\Im v-m|\le 1$.
  Let
  \[
    a:=\max\{|\Re v|:\ E(v)=0,\ |\Im v-m|\le 1\}>0.
  \]
  For $0<\delta\le \delta_0(a,m)$ assume $\partial B_{\mathrm{def}}(a,m,\delta)$ contains no zeros
  or poles of $\mathcal Q_a$.  Then $\mathcal Q_a$ has at least one pole and no zeros in
  $B_{\mathrm{def}}(a,m,\delta)$, and
  \[
    \Phi_{B_{\mathrm{def}}(a,m,\delta)}(\mathcal Q_a)\ge \frac{\pi}{2}
    \qquad(\text{equivalently }\ \Phi_{B_{\mathrm{def}}(a,m,\delta)}(\mathcal L_a)\ge \frac{\pi}{2}).
  \]
  \end{lemma}

  \begin{proof}
  Since $E(a+im)=0$, the denominator $E(v-a)$ vanishes at $v=2a+im$, hence $\mathcal Q_a$ has a pole
  there unless canceled.  If $E(3a+im)=0$, then there is a zero of $E$ with real part $3a>a$ and
  $|\Im(3a+im)-m|=0\le 1$, contradicting maximality.  Thus the pole is not canceled and lies in
  $B_{\mathrm{def}}$.

  Any zero of $\mathcal Q_a$ in $B_{\mathrm{def}}$ would correspond to a zero of $E(v+a)$ with
  $v\in B_{\mathrm{def}}$, hence to a zero of $E$ in the translated region $B(3a,m,\delta)$, again
  contradicting maximality.  Therefore $N_Z=0$ and $N_P\ge 1$ in $B_{\mathrm{def}}$.

  By the argument principle,
  $\int_{\partial B_{\mathrm{def}}} \mathcal L_a(v)\,dv = 2\pi i (N_Z-N_P)$, so the total argument
  increment is $-2\pi N_P$.  Decomposing into four sides and applying the pigeonhole principle gives
  $\Phi_{B_{\mathrm{def}}}(\mathcal L_a)\ge \pi/2$.
  \end{proof}
  ```

  (iv) **Forced-zero obstruction remark (optional but recommended)**
  ```tex
  \begin{remark}[Why defect forcing is tilt-forced, not “interior zero forced”]
  The defect quotient $\mathcal Q_a(v)=E(v+a)/E(v-a)$ cancels the original quartet at $\pm a\pm im$:
  at $v=im$ both numerator and denominator vanish, and $\mathcal Q_a$ has a removable $0/0$ structure.
  Thus a box enclosing $a+im$ does not topologically force winding of $\mathcal Q_a$.
  Defect forcing instead uses the transported pole at $2a+im$, which exists only when $a\neq 0$.
  \end{remark}
  ```

* **Dependencies on other branches:**  
  ENVELOPE/LOCAL must (i) accept \(\Phi_B(\mathcal Q_a)\) in the admissible endpoint class, and (ii) provide a δ-uniform **upper bound** for it on \(B_{\mathrm{def}}(a,m,\delta)\) without pointwise UE; ABSORB must confirm budget feasibility.  
* **Referee risk notes (anticipated objections + how addressed):**
  1. *Objection:* “You assumed a maximality property.”  
     *Answer:* This is a WLOG extremal selection inside the finite local window \(|\Im v-m|\le 1\); any off-axis configuration implies existence of such an extremal quartet.
  2. *Objection:* “What if \(\partial B_{\mathrm{def}}\) hits a zero/pole of \(\mathcal Q_a\)?”  
     *Answer:* The lemma is stated under collar-admissibility. The program already enforces admissibility by shrinking/shift policies; the same mechanism must be applied to \(\mathcal Q_a\).
  3. *Objection:* “This moves the box center to \(2a+im\).”  
     *Answer:* Correct; if the global program is restricted to \(\alpha\in(0,1]\) boxes, it must be generalized or the lemma is unusable. This is explicitly flagged.
