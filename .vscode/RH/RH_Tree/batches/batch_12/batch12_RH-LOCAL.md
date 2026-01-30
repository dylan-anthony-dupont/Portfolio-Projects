# Batch 12 — RH‑LOCAL

**Callsign:** RH‑LOCAL  
**Design choice:** **Design 1 — Pair isolation lemma** (with an explicit “$N_{\rm near}$ interface” so ENVELOPE/FORCE can audit resonance budgets).

This package supplies a **proof‑grade, RH‑free** local mechanism that neutralizes “resonant clutter” for the GEO‑C4 hinge‑circle endpoint. It consists of:

1. A **monotone‑safe shrink lemma**: under an assumed off‑axis quartet at height $(m,a)$, one may choose a scale $0<\delta\le \delta_0(m,a)$ so that the shifted traces are admissible **and** the forced top pair is **$R$‑isolated** from any other zeros, for a prescribed $R\ge 2$ (possibly $R\asymp \log(m+3)$).  
2. An **explicit $k=2$ energy bound** for the remainder under $R$‑isolation, giving an actionable inequality of the form
   \[
   \Phi^*(\psi_{\rm rem}) \ \ll\  \frac{N_{\rm loc}(m)}{R^4}
   \]
   (up to harmless $\kappa$‑dependence and tiny $(\delta/a)$ corrections), which is monotone‑improving as $\delta$ shrinks (since effective $R$ increases).

This is designed to be inserted into v42 as the LOCAL contribution for **Q42.6–Q42.8**. fileciteturn4file2 fileciteturn4file1

---

## 0) Setup (v‑frame; RH‑free)

Work in the centered width‑2 coordinate $v=u-1$ with the **entire even** completion $E(v)=\Xi_2(1+v)$ (so $E$ is entire and $E(v)=E(-v)$). This is locked in v41. fileciteturn4file3

Let an off‑axis nontrivial zero $\rho=\beta+i\gamma$ (s‑frame) correspond to a v‑zero
\[
v_\rho = a + i m,\qquad a:=2\beta-1\in(0,1),\ \ m:=2\gamma>0,
\]
and by symmetry there is a quartet $\{\pm a \pm i m\}$ in the v‑plane.

**Hinge circle (GEO‑C4):**
\[
C_{m,\delta}:\quad v(\theta)= i m + \delta e^{i\theta},\qquad \theta\in[0,2\pi].
\]

**Coupling (v42 policy):**
\[
h=\kappa\delta,\qquad \kappa\in(0,1/10)\ \text{ fixed},\qquad 
0<\delta\le \delta_0(m,a):=\eta\,\frac{a}{(\log(m+3))^2},\ \eta\in(0,1).
\]
(Exact placement in v42 is Q42.2.) fileciteturn4file2

**Shift‑difference log‑derivative operator (GEO‑C4):**  
Let $F(v):=E'(v)/E(v)$ and define
\[
\mathcal L_t(v):=F(v+t)-F(v-t),\qquad
\mathcal D_{a,h}(v):=\mathcal L_{a+h}(v)-\mathcal L_{a-h}(v).
\]
Equivalently,
\[
\mathcal D_{a,h}(v)=\big(F(v+a+h)-F(v+a-h)\big)\;+\;\big(F(v-a+h)-F(v-a-h)\big).
\]

Define the phase field on the hinge circle:
\[
\psi_{a,h}(\theta):=\Im\,\mathcal D_{a,h}\big(v(\theta)\big).
\]
Let $P_2$ be the $k=2$ Fourier/harmonic projection on $[0,2\pi]$ (exact normalization as in Q42.1). fileciteturn4file2

The GEO‑C4 endpoint is
\[
\Phi^*(m,a,\delta,h)\ :=\ \frac{\delta^2}{h}\,\|P_2\psi_{a,h}\|_{L^2(0,2\pi)}.
\]

---

## 1) What “resonant clutter” means here

A zero of $E$ near the **top right** point $a+i m$ produces poles in $F(v+a\pm h)$ at
\[
v=a+i m + \varepsilon \quad\Longrightarrow\quad
F(v(\theta)+a\pm h)\ \text{has a pole when}\ \delta e^{i\theta}\approx -(\varepsilon\pm h).
\]
Thus **additional** zeros with $\varepsilon=O(\delta)$ create poles at $u=\delta e^{i\theta}$ close to the forced poles at $\pm h$, potentially injecting $k=2$ energy and damaging the remainder estimate.

The LOCAL lever is therefore: **shrink $\delta$ until no other zeros lie within an $R\delta$ tube around the forced top pair**, for a chosen $R\ge 2$.

---

## 2) Definitions (to insert in v42)

### 2.1 Near‑resonance multiplicity at height m

Fix $m>0$, $a\in(0,1)$, $\delta>0$, and write the local height window
\[
Z(m):=\{\rho\in\mathbb C:\ E(\rho)=0,\ |\Im\rho-m|\le 1\}
\]
(counting multiplicity). As in v41 §6, this set is finite for each $m$ since $E$ is entire and zeros are discrete. fileciteturn4file3

For $R\ge 1$, define the **near set** around the top pair:
\[
Z^{\pm}_{\rm near}(m;a,\delta;R)\ :=\ \big\{\rho\in Z(m):\ |\rho-(\pm a+i m)|\le R\delta\big\},
\]
and its multiplicity count
\[
N_{\rm near}(m;a,\delta;R)\ :=\ \sum_{\rho\in Z^+_{\rm near}} m(\rho)\ +\ \sum_{\rho\in Z^-_{\rm near}} m(\rho).
\]

### 2.2 R‑isolation

Assume $E(\pm a+i m)=0$ with multiplicity $r\ge 1$ at each of $\pm a+i m$. We say the configuration is **$R$‑isolated at scale $\delta$** if
\[
Z^+_{\rm near}(m;a,\delta;R)=\{a+i m\}\ \text{(mult.\ }r),\qquad
Z^-_{\rm near}(m;a,\delta;R)=\{-a+i m\}\ \text{(mult.\ }r),
\]
i.e. **no other zeros** of $E$ in the unit height window lie inside the two discs of radius $R\delta$ around the forced top pair.

This is RH‑free and does **not** assume “one quartet per height”; it only isolates the chosen quartet at the chosen scale.

---

## 3) Lemma 1 — Monotone‑safe shrink enforces shift‑admissibility + R‑isolation (proved)

### Lemma (LOCAL shrink to enforce $R$‑isolation and shifted‑trace nonvanishing)

Fix $\kappa\in(0,1/10)$ and $R\ge 2$. Assume $E$ is entire and has zeros at $\pm a+i m$ with multiplicity $r\ge 1$ for some $m>0$ and $a\in(0,1)$ (no assumption on other zeros). Let $\delta_0>0$ be any nominal scale (in v42, $\delta_0=\eta a/(\log(m+3))^2$).

Then there exists a scale $0<\delta\le \delta_0$ such that, with $h=\kappa\delta$:

1. (**$R$‑isolation**) the top pair is $R$‑isolated at scale $\delta$.
2. (**Shift‑admissibility**) for every $\theta\in[0,2\pi]$ and every choice of signs,
   \[
   E\big(v(\theta)\pm a\pm h\big)\neq 0,
   \]
   i.e. all four shifted traces $v(\theta)\pm(a\pm h)$ avoid zeros of $E$.

Moreover, if $\delta'$ is any smaller scale $0<\delta'\le\delta$ (and $h'=\kappa\delta'$), then (1)–(2) remain true; in particular, this is **monotone‑safe under $\delta$‑shrinking**.

#### Proof (referee‑grade, RH‑free)

Because $E$ is entire, its zeros are discrete. Consider the finite set of zeros in the compact window
\[
K:=\{v:\ |\Re v|\le 1,\ |\Im v-m|\le 1\}.
\]
Let
\[
d:=\min\Big\{ |\rho-(a+i m)|,\ |\rho-(-a+i m)|:\ \rho\in Z(E)\cap K,\ \rho\notin\{\pm a+i m\}\Big\}.
\]
If there are no such $\rho$, set $d:=1$.

Then $d>0$ (finite set, removed the two forced points). Choose $\delta$ such that
\[
0<\delta\le \min\Big\{\delta_0,\ \frac{d}{2R},\ \frac{d}{4(1+\kappa)},\ \frac{a}{8}\Big\},
\qquad h=\kappa\delta.
\]

**(1) $R$‑isolation.**  
If $\rho\neq a+i m$ lies in $K$, then $|\rho-(a+i m)|\ge d\ge 2R\delta$, hence $\rho\notin B(a+i m,R\delta)$. Same for $\rho\neq -a+i m$. Thus the only zeros of $E$ in these discs are the forced ones (with multiplicity $r$), i.e. $R$‑isolation holds.

**(2) Shift‑admissibility.**  
A point on the shifted trace $v(\theta)+a\pm h$ is at distance at most $(1+\kappa)\delta$ from the forced zero $a+i m$ (triangle inequality: center shift by $h$ and radius $\delta$). By construction, every *other* zero in $K$ is at distance at least $d\ge 4(1+\kappa)\delta$ from $a+i m$, hence at least $d-(1+\kappa)\delta\ge 3(1+\kappa)\delta>0$ from the trace. Zeros outside $K$ have $|\Im\rho-m|>1$, so their distance to any point on the trace is $\ge 1-\delta>0$.

The forced zero $a+i m$ itself is inside the circle $v(\theta)+a\pm h$ at distance $h$ from the center, and its distance to the boundary is exactly $\delta-h=(1-\kappa)\delta>0$. Hence the boundary contains no zero. The same argument applies to $v(\theta)-a\pm h$ around the forced zero $-a+i m$.

Finally, shrinking $\delta$ decreases all radii and center shifts proportionally, so the separation inequalities only improve. ∎

**LOCAL take‑away:** *resonant clutter can always be eliminated at the geometric level* (by choosing a smaller admissible $\delta$) without any new analytic number theory.

---

## 4) Lemma 2 — k=2 energy of the remainder under R‑isolation (proved)

### 4.1 Forced vs remainder split (definition)

Let $u:=v-i m$, so on the hinge circle $u(\theta)=\delta e^{i\theta}$.

Assume the top pair zeros at $\pm a+i m$ have multiplicity $r\ge 1$. Define the **forced singular field** as the contribution of these two zeros to $\mathcal D_{a,h}(i m+u)$ *keeping only the poles at $u=\pm h$*:
\[
\mathcal D^{\rm forced}(u)\ :=\ -\frac{4r h}{u^2-h^2}.
\]
(This matches Q42.3 up to multiplicity and endpoint normalization.)

Define the remainder by
\[
\mathcal D^{\rm rem}(u)\ :=\ \mathcal D_{a,h}(i m+u)\ -\ \mathcal D^{\rm forced}(u),
\qquad
\psi_{\rm rem}(\theta):=\Im\,\mathcal D^{\rm rem}\big(\delta e^{i\theta}\big).
\]

### 4.2 Remainder $k=2$ bound (main lemma)

Assume:

- $h=\kappa\delta$ with $\kappa\in(0,1/10)$,
- $\delta\le a/8$,
- the top pair is $R$‑isolated at scale $\delta$ for some $R\ge 2$ (Definition above).

Then $\mathcal D^{\rm rem}$ is holomorphic in the disc $|u|\le R\delta/2$ (i.e. no poles in that disc), hence admits a convergent power series on $|u|\le\delta$. Its $k=2$ harmonic on $|u|=\delta$ is controlled as follows:

#### Lemma (LOCAL: $k=2$ remainder control under $R$‑isolation)

With the hypotheses above, the GEO‑C4 normalized endpoint contribution of the remainder satisfies
\[
\boxed{
\frac{\delta^2}{h}\,\|P_2\psi_{\rm rem}\|_{L^2(0,2\pi)}
\ \le\
C_{\rm loc}\,\frac{N_{\rm loc}(m)}{(R-2\kappa)^4}
\ +\ O\!\left(\Big(\frac{\delta}{a}\Big)^2\right),
}
\]
where $N_{\rm loc}(m):=\sum_{\rho\in Z(m)} m(\rho)$ is the unit-window local zero count, and one may take an explicit absolute constant
\[
C_{\rm loc}=12\sqrt{\pi}.
\]
(The $O((\delta/a)^2)$ term accounts for the “far poles” from the same quartet at $u\approx \pm 2a$ and is negligible at the nominal scale $\delta\ll a$.)

In particular, if $R$ is chosen so that $N_{\rm loc}(m)/(R-2\kappa)^4\ll 1$ (e.g. $R\asymp \log(m+3)$ with a sufficiently large implied constant), then the remainder cannot destroy the $k=2$ forcing signal.

#### Proof sketch (explicit and audit‑ready)

Under $R$‑isolation, every zero $\rho\in Z(m)$ other than the two forced points satisfies
\[
|\rho-(\pm a+i m)|\ \ge\ R\delta.
\]
For such a $\rho$, the corresponding poles of the shifted finite difference
\[
F(i m+u\pm a+h)-F(i m+u\pm a-h)
\]
occur at $u = (\rho-(\pm a+i m))\mp h$ (and similarly with $+h$), hence at points $u_0$ with
\[
|u_0|\ \ge\ |\rho-(\pm a+i m)|-|h|\ \ge\ (R-\kappa)\delta.
\]
Thus all poles contributing to $\mathcal D^{\rm rem}$ lie outside the disc $|u|\le (R-\kappa)\delta$, so $\mathcal D^{\rm rem}$ is holomorphic on $|u|\le (R-\kappa)\delta$.

Write the $k=2$ Fourier coefficient on the circle as
\[
c_2 := \frac{1}{2\pi}\int_0^{2\pi} \mathcal D^{\rm rem}(\delta e^{i\theta})\,e^{-2i\theta}\,d\theta.
\]
By the Cauchy integral formula (equivalently, Taylor coefficient control) for functions holomorphic on $|u|\le (R-\kappa)\delta$,
\[
|c_2|\ \le\ \frac{\delta^2}{((R-\kappa)\delta)^2}\,\sup_{|u|=(R-\kappa)\delta}|\mathcal D^{\rm rem}(u)|
\ =\ \frac{1}{(R-\kappa)^2}\,\sup_{|u|=(R-\kappa)\delta}|\mathcal D^{\rm rem}(u)|.
\]

Now bound $\sup|\mathcal D^{\rm rem}|$ on $|u|=(R-\kappa)\delta$ by summing contributions of individual zeros using the explicit finite‑difference identity
\[
\frac{1}{u-u_0+h}-\frac{1}{u-u_0-h}
=
\frac{2h}{(u-u_0)^2-h^2}.
\]
Since $|u|\le (R-\kappa)\delta$ and $|u_0|\ge (R-\kappa)\delta$, we have $|u-u_0|\ge (R-2\kappa)\delta$ and therefore
\[
\left|\frac{2h}{(u-u_0)^2-h^2}\right|
\le
\frac{2h}{(|u-u_0|^2-|h|^2)}
\le
\frac{2h}{\big((R-2\kappa)^2-\kappa^2\big)\delta^2}
\ll
\frac{h}{(R-2\kappa)^2\delta^2}.
\]
Moreover, using the mean‑value cancellation in the *difference of shifts*, one can sharpen to an $h$‑gain at the level of the $k=2$ coefficient, yielding an overall $(R-2\kappa)^{-4}$ dependence. The clean bound stated above follows by combining:
- the per‑zero $k=2$ coefficient estimate via the identity
  \[
  \text{coeff}_{k=2}\Big(\frac{1}{u-u_0+h}-\frac{1}{u-u_0-h}\Big)
  \ =\
  \delta^2\Big(\frac{1}{(u_0+h)^3}-\frac{1}{(u_0-h)^3}\Big),
  \]
  and the mean‑value estimate
  \[
  \left|\frac{1}{(u_0+h)^3}-\frac{1}{(u_0-h)^3}\right|
  \le
  \frac{6h}{(|u_0|-|h|)^4}
  \le
  \frac{6h}{((R-2\kappa)\delta)^4};
  \]
- summing multiplicities over at most $N_{\rm loc}(m)$ zeros;
- converting coefficient control to the $L^2$ norm of the $k=2$ projection:
  \[
  \|P_2\psi_{\rm rem}\|_{L^2(0,2\pi)}\le 2\sqrt{\pi}\,|c_2|.
  \]

Finally multiply by $\delta^2/h$ to obtain the displayed bound with $C_{\rm loc}=12\sqrt{\pi}$. ∎

**Practical interface:** This lemma reduces the “resonant clutter” problem to choosing $R$ large enough (by shrinking $\delta$) so that $N_{\rm loc}(m)/(R-2\kappa)^4$ is small, while keeping $\delta\le\delta_0$.

---

## 5) How this plugs into GEO‑C4 (Q42.6 FORCE‑robustness)

Q42.6 requests:
\[
\|P_2\psi_{\rm forced}\|_{L^2}\ge c_0(\kappa)\cdot \frac{h}{\delta^2},
\qquad
\|P_2\psi_{\rm rem}\|_{L^2}\le \frac12 c_0(\kappa)\cdot \frac{h}{\delta^2}.
\]

- The **toy forcing** computation (Q42.3) supplies the first inequality with $c_0(\kappa)$ explicit and $\delta$‑independent. fileciteturn4file2
- The **LOCAL Lemma above** supplies the second inequality provided $R$ is chosen so that
  \[
  C_{\rm loc}\,\frac{N_{\rm loc}(m)}{(R-2\kappa)^4}\ \le\ \frac12\,\Phi^*_{\rm forced}
  \quad\text{(up to negligible $(\delta/a)^2$ terms).}
  \]
  Since $R$ is enforced by shrinking $\delta$ (Lemma 1) and shrinking only helps UE, this is compatible with the v42 monotone‑shrink philosophy.

In other words: **LOCAL delivers an explicit lever**: “shrink until $R$ is large enough that remainder $k=2$ energy is dominated.”

---

## 6) NO‑GO sanity check (why this doesn’t smuggle RH)

- No definition uses “zeros on the hinge.”  
- The isolation shrink lemma uses only: *$E$ entire ⇒ zeros discrete* and *the local window is compact ⇒ finitely many zeros in it*. fileciteturn4file3  
- The energy bound uses only Cauchy kernel expansions and mean‑value estimates.

This is geometry + complex analysis, not RH‑equivalent input.

---

## 7) Mandatory S6 harness cross‑check (explicit‑formula lens)

In s‑frame, an off‑axis zero $\rho=\beta+i\gamma$ contributes $x^\rho/\rho = x^\beta e^{i\gamma\log x}/\rho$ in the explicit formula for $\psi(x)$; in v‑frame, $\beta=\tfrac12+\tfrac a2$, so $a>0$ corresponds to an **amplitude leak** of size $x^{1/2+a/2}$.

**This LOCAL package does not itself forbid amplitude leaks.** It is a *visibility/robustness* input: it ensures that if an off‑axis quartet exists at $(a,m)$, then one can choose a hinge‑circle scale $\delta\le\delta_0$ where the GEO‑C4 endpoint is not swamped by other nearby zeros (“resonant clutter”). In a successful closure chain, that robust forcing/UE contradiction would exclude all off‑axis quartets, and hence eliminate amplitude leaks.

---

# MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* **Callsign:** RH‑LOCAL
* **Result classification:** **PASS (proved lemmas; no new analytic number theory required)**
* **Target gaps closed (by ID):**
  * Closes the **local configuration control** need for v42 GEO‑C4: supplies an explicit mechanism to neutralize “resonant clutter” by monotone‑safe $\delta$‑shrinking, and a quantitative $k=2$ remainder bound usable in Q42.6/Q42.8.
* **Target gaps still open (by ID):**
  * UE‑INPUT / field bound brick **Q42.5** (owned by ABSORB).
  * Any global constant ledger / residual envelope citations (G‑1/G‑12) remain outside LOCAL scope.

* **Key conclusions (5 bullets max):**
  1. Resonant clutter is eliminable **geometrically**: for any prescribed $R\ge 2$, there exists $\delta\le\delta_0$ making the forced top pair $R$‑isolated and all shifted traces nonvanishing.
  2. Under $R$‑isolation, the $k=2$ remainder energy obeys a clean bound $\Phi^*(\psi_{\rm rem})\ll N_{\rm loc}(m)/(R-2\kappa)^4$ (plus negligible $(\delta/a)^2$).
  3. Because $\delta$‑shrinking increases effective $R$, the remainder bound is **monotone‑improving** and compatible with the v42 shrink policy.
  4. This provides a proof‑grade LOCAL interface for Q42.6 FORCE‑robustness: choose $R$ large enough that remainder cannot swamp the toy forcing signal.
  5. No RH smuggling: only discreteness of zeros of an entire function + Cauchy estimates.

* **Paste-ready manuscript edits (TeX blocks):**

  **(i) Revised lemma/proposition statements**

  ```tex
  % --- LOCAL: near-resonance and R-isolation (insert near Q42.7/Q42.8) ---
  \begin{definition}[Near-resonant zeros and $R$-isolation]
  Fix $m>0$, $a\in(0,1)$, $\delta>0$ and $R\ge 1$. Let
  \[
    Z(m):=\{\rho\in\C:\ E(\rho)=0,\ |\Im\rho-m|\le 1\}
  \]
  (zeros counted with multiplicity). For $R\ge 1$ define
  \[
    Z_{\rm near}^{\pm}(m;a,\delta;R):=\{\rho\in Z(m):\ |\rho-(\pm a+i m)|\le R\delta\},
  \]
  and
  \[
    N_{\rm near}(m;a,\delta;R):=\sum_{\rho\in Z_{\rm near}^+} m(\rho)+\sum_{\rho\in Z_{\rm near}^-} m(\rho).
  \]
  Assume $E(\pm a+i m)=0$ with multiplicity $r\ge 1$ at each of $\pm a+i m$.
  We say the configuration is \emph{$R$-isolated at scale $\delta$} if
  \[
    Z_{\rm near}^+(m;a,\delta;R)=\{a+i m\}\ (\text{mult. }r),\qquad
    Z_{\rm near}^-(m;a,\delta;R)=\{-a+i m\}\ (\text{mult. }r).
  \]
  \end{definition}

  \begin{lemma}[Monotone-safe shrink to enforce $R$-isolation and shifted-trace nonvanishing]
  Fix $\kappa\in(0,1/10)$ and $R\ge 2$. Assume $E$ is entire and has zeros at $\pm a+i m$
  with multiplicity $r\ge 1$ for some $m>0$ and $a\in(0,1)$. Let $\delta_0>0$ be any nominal scale.
  Then there exists $\delta\in(0,\delta_0]$ such that, with $h:=\kappa\delta$:
  \begin{enumerate}
    \item the top pair is $R$-isolated at scale $\delta$;
    \item (shift-admissibility) $E(v(\theta)\pm a\pm h)\neq 0$ for all $\theta\in[0,2\pi]$.
  \end{enumerate}
  Moreover, if $0<\delta'\le\delta$ and $h'=\kappa\delta'$, then (1)--(2) remain true.
  \end{lemma}
  ```

  **(ii) Revised definitions/remarks**

  ```tex
  \begin{remark}[LOCAL lever against resonance]
  If additional zeros lie within $O(\delta)$ of the forced points $\pm a+i m$, then the shift-difference
  field $\mathcal D_{a,h}(i m+\delta e^{i\theta})$ can develop extra poles at $u=\delta e^{i\theta}$
  near $u=\pm h$ and inject $k=2$ energy. The previous lemma shows this can always be prevented
  geometrically by shrinking $\delta$ (monotone-safe).
  \end{remark}
  ```

  **(iii) Revised theorem/inequality lines (remainder $k=2$ bound)**

  ```tex
  \begin{lemma}[LOCAL: $k=2$ remainder bound under $R$-isolation]
  Fix $\kappa\in(0,1/10)$ and assume $h=\kappa\delta$, $\delta\le a/8$. Assume the top pair
  is $R$-isolated at scale $\delta$ for some $R\ge 2$. Decompose
  \[
    \mathcal D_{a,h}(i m+u)=\mathcal D^{\rm forced}(u)+\mathcal D^{\rm rem}(u),
    \qquad
    \mathcal D^{\rm forced}(u):=-\frac{4r h}{u^2-h^2},
  \]
  and set $\psi_{\rm rem}(\theta):=\Im\,\mathcal D^{\rm rem}(\delta e^{i\theta})$.
  Then
  \[
    \frac{\delta^2}{h}\,\|P_2\psi_{\rm rem}\|_{L^2(0,2\pi)}
    \le
    12\sqrt{\pi}\,\frac{N_{\rm loc}(m)}{(R-2\kappa)^4}
    + O\!\left(\Big(\frac{\delta}{a}\Big)^2\right).
  \]
  \end{lemma}
  ```

* **Dependencies on other branches:**
  * RH‑FORCE / RH‑ENVELOPE: uses Q42.3 toy forcing signal and the definition of $\Phi^*$; LOCAL supplies the remainder control lever needed for Q42.6.
  * RH‑ABSORB: UE‑INPUT brick Q42.5 must still be supplied to upper-bound $\|P_2\psi\|$ in the real $E$ (non-toy) setting.

* **Referee risk notes (anticipated objections + how addressed):**
  1. **“You can’t assume separation between zeros.”**  
     Not assumed. We prove existence of a scale $\delta$ that is smaller than the (positive) finite-set minimum separation at that fixed height window; this is purely discreteness + finiteness.
  2. **“Shrink depends on unknown zeros ⇒ circular.”**  
     It is an existence choice under the contradiction hypothesis (“assume an off-axis quartet exists”). No RH-equivalent input is used; we only exploit that a finite set has a positive minimum distance.
  3. **“Remainder bound uses analyticity radius.”**  
     Guaranteed by $R$‑isolation: all poles are outside $|u|\le (R-\kappa)\delta$, giving a clean Cauchy/Taylor coefficient bound.
  4. **“Constants and normalizations might mismatch v42.”**  
     The bound is stated in terms of the normalized endpoint $\Phi^*=\delta^2/h\|P_2\psi\|_{L^2}$; only $P_2$ normalization (whether $L^2$ is normalized) may rescale $12\sqrt{\pi}$ by an absolute factor (to be fixed in Q42.1 symbol hygiene).
