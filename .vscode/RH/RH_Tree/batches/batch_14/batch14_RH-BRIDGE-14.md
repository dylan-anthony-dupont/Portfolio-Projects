# Batch 14 — RH-BRIDGE-14  
**Mission:** Make the hinge-circle setup + new UE interface bulletproof, and provide the clean bridge lemma turning UE-INPUT\(^{{L^1}}\) / UE-INPUT\(^{{H^1}}\)(\(\mathcal D\)) into \(\Phi^\star=o(1)\) without pointwise/sup leakage.

**Locked context:** GEO–C4 endpoint is unchanged:
\[
\Phi^\star(a,m,\delta,h)\ :=\ \frac{\delta^2}{h}\,\|P_2\psi_{a,h}\|_{L^2([0,2\pi])},
\qquad
\psi_{a,h}(\theta)=\Im(\mathcal D_{a,h}(v(\theta))),
\quad
v(\theta)=im+\delta e^{i\theta}.
\]
UE interface is replaced by **boundary \(L^1\)** control of \(\mathcal D_{a,h}\) on the hinge circle.

---

## Paste‑in block (definitions + bridge lemma + proof + non‑circularity note)

```tex
% =============================================================
% GEO–C4: hinge-circle setup + L^1-to-endpoint bridge (UE interface)
% =============================================================

\begin{definition}[Shift-admissibility and buffered hinge circle]\label{def:shift-admissibility-hinge}
Let $m>0$, $\delta>0$, $a>0$, $h>0$, and define the hinge circle
\[
C_{m,\delta}:=\{v(\theta):\theta\in[0,2\pi]\},\qquad v(\theta):=im+\delta e^{i\theta}.
\]
Let $E$ be the even entire completed object in the centered $v$--frame (Definition~\ref{def:E-vframe})
and set $f(v):=E'(v)/E(v)$.
Define the shift set
\[
T_{a,h}:=\{a+h,\ a-h,\ -a+h,\ -a-h\}.
\]
We say $C_{m,\delta}$ is \emph{$(a,h)$--shift-admissible} if
\[
E(v(\theta)+t)\neq 0\qquad\text{for all }\theta\in[0,2\pi]\text{ and all }t\in T_{a,h}.
\]
Equivalently, $f$ is holomorphic on each shifted trace $C_{m,\delta}+t$ $(t\in T_{a,h})$.
\end{definition}

\begin{definition}[Two-sided shift differences and the GEO--C4 trace observable]\label{def:DaH-psi}
Assume $C_{m,\delta}$ is $(a,h)$--shift-admissible.
For $t\in\mathbb R$ define
\[
\mathcal L_t(v):=f(v+t)-f(v-t),
\qquad
\mathcal D_{a,h}(v):=\mathcal L_{a+h}(v)-\mathcal L_{a-h}(v).
\]
Define the real trace observable on the hinge circle by
\[
\psi_{a,h}(\theta):=\Im\big(\mathcal D_{a,h}(v(\theta))\big)\in\mathbb R.
\]
Let $P_2$ denote the $n=2$ Fourier projection on $[0,2\pi]$:
for $g\in L^2([0,2\pi])$,
\[
\widehat g(n):=\frac1{2\pi}\int_0^{2\pi} g(\theta)e^{-in\theta}\,d\theta,
\qquad
(P_2 g)(\theta):=\widehat g(2)e^{2i\theta}+\widehat g(-2)e^{-2i\theta}.
\]
\end{definition}

\begin{remark}[No $\log$ branch or pointwise argument is used]\label{rem:no-log-branch-v43}
All objects above are defined from the meromorphic function $f=E'/E$ on admissible traces.
We do not choose a global branch of $\log E$ and we do not require pointwise definitions of $\arg E$ or $\arg\mathcal Q$.
The endpoint uses only $\psi_{a,h}(\theta)=\Im(\mathcal D_{a,h}(v(\theta)))$ and Fourier projection.
\end{remark}

\begin{lemma}[L$^1$\,→\,endpoint bridge for the $k=2$ harmonic]\label{lem:L1-to-P2}
Let $\psi\in L^1([0,2\pi])$ and let $P_2$ be the $n=2$ Fourier projection as above. Then
\begin{equation}\label{eq:P2-L2-by-L1}
\|P_2\psi\|_{L^2([0,2\pi])}\ \le\ \frac{1}{\sqrt{\pi}}\int_0^{2\pi}|\psi(\theta)|\,d\theta.
\end{equation}
If $\psi(\theta)=\Im(\mathcal D_{a,h}(v(\theta)))$ for a complex-valued function $\mathcal D_{a,h}$ on $C_{m,\delta}$, then
\begin{equation}\label{eq:P2-L2-by-D}
\|P_2\psi\|_{L^2([0,2\pi])}\ \le\ \frac{1}{\sqrt{\pi}}\int_0^{2\pi}|\mathcal D_{a,h}(v(\theta))|\,d\theta.
\end{equation}
Consequently, for the GEO--C4 endpoint
\[
\Phi^\star(a,m,\delta,h):=\frac{\delta^2}{h}\|P_2\psi_{a,h}\|_{L^2([0,2\pi])}
\]
one has the deterministic reduction
\begin{equation}\label{eq:Phi-star-L1-reduction}
\Phi^\star(a,m,\delta,h)\ \le\ \frac{1}{\sqrt{\pi}}\frac{\delta^2}{h}\int_0^{2\pi}\big|\mathcal D_{a,h}(v(\theta))\big|\,d\theta.
\end{equation}
\end{lemma}

\begin{proof}
By orthogonality of $e^{\pm 2i\theta}$ in $L^2([0,2\pi])$,
\[
\|P_2\psi\|_2^2
=\int_0^{2\pi}|\widehat\psi(2)e^{2i\theta}+\widehat\psi(-2)e^{-2i\theta}|^2\,d\theta
=2\pi\big(|\widehat\psi(2)|^2+|\widehat\psi(-2)|^2\big).
\]
For each $n\in\mathbb Z$, the Fourier coefficient bound gives
\[
|\widehat\psi(n)|
=\Big|\frac1{2\pi}\int_0^{2\pi}\psi(\theta)e^{-in\theta}\,d\theta\Big|
\le \frac1{2\pi}\int_0^{2\pi}|\psi(\theta)|\,d\theta.
\]
Applying this with $n=\pm 2$ yields
\[
\|P_2\psi\|_2^2
\le 2\pi\cdot 2\cdot\Big(\frac1{2\pi}\int_0^{2\pi}|\psi(\theta)|\,d\theta\Big)^2
=\frac1{\pi}\Big(\int_0^{2\pi}|\psi(\theta)|\,d\theta\Big)^2,
\]
which implies \eqref{eq:P2-L2-by-L1}.  Since $|\Im z|\le |z|$, \eqref{eq:P2-L2-by-D} follows immediately.
Finally \eqref{eq:Phi-star-L1-reduction} is obtained by multiplying by $\delta^2/h$.
\end{proof}

\begin{remark}[UE interface: what is actually needed to force $\Phi^\star=o(1)$]\label{rem:UE-interface-L1}
Lemma~\ref{lem:L1-to-P2} reduces the analytic frontier to bounding the boundary $L^1$ quantity
\[
\int_0^{2\pi}|\mathcal D_{a,h}(v(\theta))|\,d\theta
\qquad\text{with}\qquad v(\theta)=im+\delta e^{i\theta}.
\]
Thus any UE-INPUT statement of the form
\begin{equation}\label{eq:UE-input-L1-template}
\int_0^{2\pi}|\mathcal D_{a,h}(v(\theta))|\,d\theta\ \le\ C_{\rm UE}\,\frac{h}{\delta}\,\frac{(\log(m+3))^{C'}}{a^2}
\end{equation}
implies the endpoint bound
\[
\Phi^\star(a,m,\delta,h)\ \le\ \frac{1}{\sqrt{\pi}}\,C_{\rm UE}\,\frac{\delta^2}{h}\cdot \frac{h}{\delta}\cdot\frac{(\log(m+3))^{C'}}{a^2}
= \frac{C_{\rm UE}}{\sqrt{\pi}}\ \delta\ \frac{(\log(m+3))^{C'}}{a^2}.
\]
Under the nominal policy $\delta=\delta_0(m,a)=\eta\,a/(\log(m+3))^2$ this becomes
\[
\Phi^\star(a,m,\delta_0,h)\ \le\ \frac{C_{\rm UE}}{\sqrt{\pi}}\ \eta\ \frac{(\log(m+3))^{C'-2}}{a},
\]
so in particular $\Phi^\star=o(1)$ as $m\to\infty$ provided the program also enforces a uniform lower bound
$a\ge a_{\min}>0$ at the contradiction stage (or replaces the final algebra by the manuscript’s
standard “$a=a(m)$ forced by the quartet at height $m$” contradiction mechanism).
\end{remark}

\paragraph{Non-circularity audit (RH-free).}
The bridge Lemma~\ref{lem:L1-to-P2} uses only:
(i) orthogonality of exponentials in $L^2([0,2\pi])$,
(ii) the definition of Fourier coefficients, and
(iii) the inequality $|\Im z|\le |z|$.
No step invokes any statement about the location of zeros of $\zeta$, $\xi$, $\Xi_2$, or $E$.
Shift-admissibility is a contour well-posedness condition (avoid poles of $E'/E$ on the trace)
and is enforceable by $\delta$-shrink using only that $E$ is entire (zeros isolated).
Therefore, the UE-interface change removes the prior RH-strength vulnerability of pointwise/sup
derivative field bounds: the new bridge depends only on boundary integrability of $\mathcal D_{a,h}$.
```

---

## Notes (implementation intent)

- This block is designed to be inserted verbatim into the v43+ manuscript at the start of the “UE reduction / UE-INPUT” subsection (where the old v42 “sup-derivative” interface lived).  
- It is compatible with the “R2 decision” (replace UE-INPUT by an \(L^1\) / \(H^1\) boundary-control interface). fileciteturn3file0

---

# MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* Callsign: RH-BRIDGE-14
* Result classification: **PASS**
* Target gaps closed (by ID):
  - **UE-INPUT interface bridge (pointwise→boundary norm):** installs Lemma \(\ref{lem:L1-to-P2}\) and the deterministic reduction \(\Phi^\star \le \frac{\delta^2}{h}\int|\mathcal D_{a,h}|\).
  - **Contour/log hygiene for the new interface:** definitions explicitly avoid \(\log\) branches and use only \(E'/E\) on admissible traces.
* Target gaps still open (by ID):
  - **UE-INPUT\(^{{L^1}}\)/UE-INPUT\(^{{H^1}}\)** itself: the analytic estimate \(\int|\mathcal D_{a,h}(v(\theta))|\,d\theta \le \cdots\) remains to be proved (ENVELOPE/LOCAL ownership).
  - Any final contradiction algebra around \(a(m)\to 0\) (FORCE/ENVELOPE integration).
* Key conclusions (≤5 bullets):
  1. \(k=2\) harmonic extraction admits an **explicit L¹→L² bound** with constant \(1/\sqrt\pi\).
  2. This yields a **clean UE reduction**: bounding \(\Phi^\star\) is reduced to bounding \(\int |\mathcal D_{a,h}|\) on the hinge circle.
  3. The reduction uses only Fourier orthogonality and coefficient bounds—**no RH-equivalent assumptions**.
  4. Shift-admissibility is treated strictly as contour well-posedness; no interior zero-freeness is required.
  5. The new interface avoids the forbidden “pointwise/sup derivative field” mechanism and its \(\delta^{-2}\) blow-up.
* Paste-ready manuscript edits:
  (i) revised lemma/proposition statements  
  - Insert Lemma `lem:L1-to-P2` + proof.  
  (ii) revised definitions/remarks  
  - Insert Definitions `def:shift-admissibility-hinge`, `def:DaH-psi`, Remarks `rem:no-log-branch-v43`, `rem:UE-interface-L1`.  
  (iii) revised theorem/inequality lines  
  - Replace the old UE-reduction displayed line by \eqref{eq:Phi-star-L1-reduction}.
* Dependencies on other branches:
  - ENVELOPE/LOCAL must provide the actual UE-INPUT\(^{{L^1}}\)/\(^{{H^1}}\) inequality (e.g. Carleson/Hardy control for \(\mathcal D_{a,h}\) on shifted hinge circles) with δ-uniform constants.
* Referee risk notes (anticipated objections + how addressed):
  - **“Projection increases \(L^1\)”**: avoided; proof uses Fourier coefficient bounds directly, not \(\|P_2\psi\|_{L^1}\le \|\psi\|_{L^1}\).
  - **“Hidden log/arg branch”**: explicitly ruled out; endpoint uses only \(E'/E\) on admissible traces.
  - **“Admissibility is RH-smuggling”**: addressed; admissibility is a shrink-enforceable contour condition (zeros isolated for entire \(E\)).
