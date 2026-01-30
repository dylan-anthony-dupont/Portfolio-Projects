# Batch 14 — RH‑ENVELOPE  
**Callsign:** RH‑ENVELOPE‑14  
**Outcome chosen:** **Outcome B — NO‑GO (RH‑strength / not provable from RH‑free toolkit as a “routine UE bound”)**

> **Target v43 closure statement (UE‑INPUTᴴ¹(D))**  
> \[
> \int_0^{2\pi}\bigl|\mathcal D_{a,h}(v(\theta))\bigr|\,d\theta \ \le\ C\,h\,\frac{(\log(m+3))^{C'}}{a^2}
> \quad\text{on }v(\theta)=im+\delta e^{i\theta},\ \delta=\eta\frac{a}{(\log(m+3))^2},\ h=\kappa\delta.
> \]
> (Everything else—GEO‑C4 endpoint, forcing brick, contradiction scaffold—is treated as locked.)

---

## 1) Final lemma statement (TeX‑ready): Off‑axis quartet forces an \(L^1\) blow‑up

```tex
\begin{lemma}[NO--GO: off-axis quartet forces $L^1$ blow-up for $\mathcal D_{a,h}$]
\label{lem:D-L1-nogo}
Let $E$ be the completed even entire object in the $v$--frame, and set
$f(v):=E'(v)/E(v)$,
$\mathcal L_t(v):=f(v+t)-f(v-t)$,
$\mathcal D_{a,h}(v):=\mathcal L_{a+h}(v)-\mathcal L_{a-h}(v)$.
Fix $\kappa\in(0,1)$ and let $h=\kappa\delta$ with $\delta>0$.

Assume there exists an off-axis quartet of zeros at height $m$:
\[
E(\pm a\pm i m)=0
\qquad\text{for some }a\in(0,1],\ m>0,
\]
(counted with multiplicity).  Define the hinge circle
\[
v(\theta)=im+\delta e^{i\theta},\qquad \theta\in[0,2\pi].
\]
Let $\psi(\theta):=\Im\bigl(\mathcal D_{a,h}(v(\theta))\bigr)$.

Assume the (locked) GEO--C4 forceability brick: there exists an absolute constant $c_0>0$
such that the forced harmonic endpoint satisfies
\[
\Phi^\star(m,a,\delta,h):=\frac{\delta^2}{h}\,\|P_2\psi\|_{L^2([0,2\pi])}\ \ge\ c_0.
\]
Then one has the quantitative lower bound
\[
\int_0^{2\pi}\bigl|\mathcal D_{a,h}(v(\theta))\bigr|\,d\theta
\ \ge\
\int_0^{2\pi}|\psi(\theta)|\,d\theta
\ \ge\
\frac{\sqrt{\pi}\,c_0\,h}{\delta^2}
\ =\
\frac{\sqrt{\pi}\,c_0\,\kappa}{\delta}.
\]
In particular, if $c_0=2\sqrt{\pi}$ (toy-quartet forcing constant), then
\[
\int_0^{2\pi}\bigl|\mathcal D_{a,h}(v(\theta))\bigr|\,d\theta
\ \ge\ \frac{2\pi\kappa}{\delta}.
\]
\end{lemma}
```

---

## 2) Proof (line‑by‑line; no RH smuggling)

```tex
\begin{proof}
We use only (i) the locked forcing lower bound $\Phi^\star\ge c_0$ and
(ii) the elementary inequality that an $L^1$ norm controls any Fourier coefficient.

Step 1 (Fourier coefficient extracted from $P_2$).
Write $P_2\psi(\theta)=A\cos(2\theta)+B\sin(2\theta)$.
Then
\[
\|P_2\psi\|_{L^2([0,2\pi])}^2
=\int_0^{2\pi}(A\cos(2\theta)+B\sin(2\theta))^2\,d\theta
=\pi(A^2+B^2).
\]
Define the complex Fourier coefficient
\[
\widehat{\psi}(2):=\frac1{2\pi}\int_0^{2\pi}\psi(\theta)\,e^{-2i\theta}\,d\theta.
\]
A direct computation gives
$A=2\Re(\widehat{\psi}(2))$ and $B=-2\Im(\widehat{\psi}(2))$, hence
\[
|\widehat{\psi}(2)|
=\frac12\sqrt{A^2+B^2}
=\frac{1}{2\sqrt{\pi}}\|P_2\psi\|_{L^2([0,2\pi])}.
\]

Step 2 ($L^1$ dominates that Fourier coefficient).
By the triangle inequality,
\[
|\widehat{\psi}(2)|
=\left|\frac1{2\pi}\int_0^{2\pi}\psi(\theta)e^{-2i\theta}\,d\theta\right|
\le \frac1{2\pi}\int_0^{2\pi}|\psi(\theta)|\,d\theta.
\]
Combining with Step 1 yields
\[
\int_0^{2\pi}|\psi(\theta)|\,d\theta
\ge 2\pi|\widehat{\psi}(2)|
\ge 2\pi\cdot \frac{1}{2\sqrt{\pi}}\|P_2\psi\|_{L^2}
= \sqrt{\pi}\,\|P_2\psi\|_{L^2}.
\]

Step 3 (insert the locked forcing lower bound).
By definition,
\[
\Phi^\star(m,a,\delta,h)=\frac{\delta^2}{h}\|P_2\psi\|_{L^2}\ge c_0
\quad\Longrightarrow\quad
\|P_2\psi\|_{L^2}\ge c_0\,\frac{h}{\delta^2}.
\]
Therefore,
\[
\int_0^{2\pi}|\psi(\theta)|\,d\theta
\ge \sqrt{\pi}\,c_0\,\frac{h}{\delta^2}.
\]

Step 4 (pass from $\psi=\Im(\mathcal D)$ to $\mathcal D$).
Since $|\Im z|\le |z|$ for all complex $z$, we have
$|\psi(\theta)|\le |\mathcal D_{a,h}(v(\theta))|$, hence
\[
\int_0^{2\pi}|\mathcal D_{a,h}(v(\theta))|\,d\theta
\ge \int_0^{2\pi}|\psi(\theta)|\,d\theta
\ge \sqrt{\pi}\,c_0\,\frac{h}{\delta^2}
=\frac{\sqrt{\pi}\,c_0\,\kappa}{\delta}.
\]
This completes the proof.
\end{proof}
```

---

## 3) Why this makes UE‑INPUTᴴ¹(D) **RH‑strength** (and why it is the right “NO‑GO”)

Assume the v43 closure statement (UE‑INPUTᴴ¹(D)) held *unconditionally* (i.e. for all admissible \((m,a,\delta,h)\) in the nominal regime).  
Then if an off‑axis quartet \(\pm a\pm i m\) existed, Lemma~\ref{lem:D-L1-nogo} would force
\(\int|\mathcal D_{a,h}|\gtrsim 1/\delta\), while UE‑INPUTᴴ¹(D) would force
\(\int|\mathcal D_{a,h}|\lesssim h(\log(m+3))^{C'}/a^2\).

Under the nominal coupling \(\delta=\eta a/\log^2(m+3)\) and \(h=\kappa\delta\), these become:

* **Forced lower bound**
  \[
  \int_0^{2\pi}\bigl|\mathcal D_{a,h}(v(\theta))\bigr|\,d\theta
  \ \gtrsim\ \frac{1}{\delta}
  \ =\ \frac{\log^2(m+3)}{\eta\,a}.
  \]
* **Claimed UE upper bound**
  \[
  \int_0^{2\pi}\bigl|\mathcal D_{a,h}(v(\theta))\bigr|\,d\theta
  \ \lesssim\ h\,\frac{(\log(m+3))^{C'}}{a^2}
  \ =\ \kappa\eta\,\frac{(\log(m+3))^{C'-2}}{a}.
  \]

Hence the ratio (lower)/(upper) is \(\asymp (\log(m+3))^{4-C'}/\eta^2\).  
In the regime needed for the GEO‑C4 contradiction to clear \(\pi/2\) (i.e. effectively \(C'\le 4\), and/or \(\eta\) small), these inequalities are incompatible for large \(m\). Therefore:

* **UE‑INPUTᴴ¹(D) + locked forcing ⇒ no off‑axis quartet at large height**, i.e. the intended RH closure mechanism.
* Consequently, UE‑INPUTᴴ¹(D) is not a “routine RH‑free envelope bound”; it is an RH‑strength statement (exactly as v43 intends).

---

## 4) Dependency latch (exactly what was used, and where it plugs)

**Used bricks (locked):**
1. **GEO‑C4 forceability brick**: off‑axis quartet \(\pm a\pm im\) ⇒ \(\Phi^\star\ge c_0\).  
2. **UE‑reduction scaffold is *not* used here**; we instead extract an \(L^1\) lower bound directly from the forced \(k=2\) harmonic.
3. Elementary Fourier/L¹ inequality: \(\int|f|\ge 2\pi|\widehat f(2)|\) and \(|\widehat f(2)|=\|P_2 f\|_{2}/(2\sqrt\pi)\).

**Where this plugs:**  
This lemma is the **exact NO‑GO alternative** to proving UE‑INPUTᴴ¹(D). It shows that any unconditional proof of UE‑INPUTᴴ¹(D) would, together with the already‑locked forcing brick, exclude off‑axis quartets (and hence is RH‑strength).

---

## Patch Packet (mandatory)

* **Callsign:** RH‑ENVELOPE‑14
* **Result classification:** **NO‑GO (RH‑strength latch)**
* **Target gaps closed (by ID):** UE‑INPUTᴴ¹(D) audit: shows the closure inequality is not “derivable for free”; it is the decisive RH‑strength brick.
* **Target gaps still open (by ID):** UE‑INPUTᴴ¹(D) remains OPEN as an unconditional inequality unless proved by new technology; no RH‑free proof supplied.
* **Key conclusions (≤5 bullets):**
  1. Off‑axis quartet forcing implies \(\|P_2\psi\|_{2}\gtrsim h/\delta^2\), hence \(\int|\mathcal D_{a,h}|\gtrsim h/\delta^2\asymp 1/\delta\).
  2. Therefore any UE bound of size \(O(h/a^2)\) on the hinge circle is **incompatible with an off‑axis quartet** at nominal \(\delta=\eta a/\log^2 m\) (for the log‑exponent regimes needed to clear \(\pi/2\)).
  3. UE‑INPUTᴴ¹(D) is an **RH‑strength closure brick** (not obtainable from generic RH‑free bounds without excluding the quartet configuration).
  4. The inequality can be used as the **single decisive “if proved, then RH”** latch in v43, but should not be presented as RH‑free routine unless proved.
  5. The quantitative lower bound is robust: it uses only forced \(k=2\) harmonic and the inequality \(|\Im z|\le |z|\).

* **Paste‑ready manuscript edits (TeX blocks):**
  (i) **Insert Lemma \ref{lem:D-L1-nogo} + proof** immediately after the v43 box that states UE‑INPUTᴴ¹(D), under a header “Why this UE is RH‑strength.”  
  (ii) Add the following short remark next to UE‑INPUTᴴ¹(D):

```tex
\begin{remark}[UE--INPUT$^{H^1}(D)$ is RH--strength]
Lemma~\ref{lem:D-L1-nogo} shows that, combined with the locked GEO--C4 forcing brick,
any unconditional bound of the form $\int_0^{2\pi}|\mathcal D_{a,h}(v(\theta))|\,d\theta
\ll h(\log m)^{C'}/a^2$ on the hinge circle would exclude off-axis quartets at large height.
Thus UE--INPUT$^{H^1}(D)$ is the decisive closure brick (RH--strength), not a routine RH--free estimate.
\end{remark}
```

  (iii) No theorem/inequality lines elsewhere need changing for this NO‑GO latch.

* **Dependencies on other branches:** None (uses only locked FORCE brick + elementary Fourier estimate).
* **Referee risk notes (anticipated objections + how addressed):**
  - *Objection:* “You used forcing; isn’t that circular?”  
    *Response:* Forcing is locked and RH‑free; the lemma only converts forced \(k=2\) harmonic into an \(L^1\) blow‑up via Fourier inequalities.
  - *Objection:* “Does this assume zero simplicity?”  
    *Response:* No; forcing constant \(c_0\) (locked) already accounts for multiplicity. If multiplicity increases, the lower bound only strengthens.
  - *Objection:* “What about resonance / cancellation by other zeros?”  
    *Response:* The forcing brick already produces a uniform lower bound on \(\|P_2\psi\|_2\) in the presence of the quartet; the argument never assumes other zeros are absent.
