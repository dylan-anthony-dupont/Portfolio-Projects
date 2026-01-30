# v44 PATCH QUEUE — post‑Batch‑15 (pre‑post‑build)

**Date:** 2026-01-30  
**Primary goal:** promote UE‑INPUT(k=2) as the *single active statement* and make UE‑REDUCE endpoint‑native (no phase loss).

---

## P0 (MECH) — Rename the frontier box

- **Archive:** `box:ue-input-v43` (L1/H¹ bound on \(\int|\mathcal D|\))  
- **Activate:** `box:ue-input-k2-v44`

This is the single biggest “make every build easier” move.

---

## P1 (TEX) — Add the k=2 coefficient identity lemma (replaces UE‑REDUCE)

**Insert near the endpoint definition (right after \(\Phi^\star\) is defined).**

```tex
\begin{lemma}[k=2 coefficient identity]\label{lem:P2-coefficient-identity}
Let $\psi\in L^2([0,2\pi])$ be real-valued and let $P_2$ denote the orthogonal projection
onto $\mathrm{span}\{\cos(2\theta),\sin(2\theta)\}$. Then
\[
\|P_2\psi\|_{L^2([0,2\pi])}
=\frac{1}{\sqrt{\pi}}\left|\int_0^{2\pi}\psi(\theta)e^{-2i\theta}\,d\theta\right|.
\]
Consequently, for $\Phi^\star:=\frac{\delta^2}{h}\|P_2\psi\|_{L^2}$ one has the exact identity
\[
\Phi^\star
=\frac{\delta^2}{h\sqrt{\pi}}\left|\int_0^{2\pi}\psi(\theta)e^{-2i\theta}\,d\theta\right|.
\]
\end{lemma}

\begin{proof}
Write the Fourier coefficient $c_2=\frac1{2\pi}\int_0^{2\pi}\psi(\theta)e^{-2i\theta}\,d\theta$.
Then $P_2\psi(\theta)=c_2e^{2i\theta}+\overline{c_2}e^{-2i\theta}$ (since $\psi$ is real).
A direct computation gives
$\|P_2\psi\|_{L^2}^2=4\pi|c_2|^2$, hence $\|P_2\psi\|_{L^2}=2\sqrt{\pi}|c_2|
=\frac{1}{\sqrt{\pi}}\left|\int_0^{2\pi}\psi(\theta)e^{-2i\theta}\,d\theta\right|$.
\end{proof}
```

---

## P2 (TEX) — Replace the single active UE box by UE‑INPUT(k=2)

**Replace the old L1 box with:**

```tex
\fbox{%
\begin{minipage}{0.95\textwidth}
\textbf{UE-INPUT(k=2) (v44, single active statement).}\label{box:ue-input-k2-v44}

\smallskip
Fix $\kappa\in(0,1)$ and let $E$ be the completed even entire object in the $v$--plane.
Let
\[
\mathcal L_t(v):=\frac{E'}{E}(v+t)-\frac{E'}{E}(v-t),
\qquad
\mathcal D_{a,h}(v):=\mathcal L_{a+h}(v)-\mathcal L_{a-h}(v).
\]
For height $m>0$, tilt $a>0$, and scale $\delta>0$, set $h:=\kappa\delta$,
$v(\theta)=im+\delta e^{i\theta}$, and $\psi(\theta):=\Im(\mathcal D_{a,h}(v(\theta)))$.
Assume the usual shift-admissibility (the boundary trace avoids poles).

\smallskip
Prove that there exist absolute constants $C,C'>0$ such that for all sufficiently large $m$
and all admissible $(a,\delta)$ one has
\[
\boxed{\ 
\left|\int_{0}^{2\pi}\psi(\theta)\,e^{-2i\theta}\,d\theta\right|
\ \le\ C\,h\,\frac{(\log(m+3))^{C'}}{a^{2}}.
\ }
\]
(\emph{Exponent budget target:} $C'<4$, or $C'=4$ with a small $\eta$ policy.)
\end{minipage}}
```

**Immediate corollary to add right after the box:**
```tex
By Lemma~\ref{lem:P2-coefficient-identity}, UE-INPUT(k=2) implies
\[
\Phi^\star \le \frac{C}{\sqrt{\pi}}(\log(m+3))^{C'}\Big(\frac{\delta}{a}\Big)^2,
\]
and under $\delta=\eta a/(\log(m+3))^2$ one has
$\Phi^\star\le \frac{C}{\sqrt{\pi}}\eta^2(\log(m+3))^{C'-4}=o(1)$ if $C'<4$.
```

---

## P3 (TEXT) — Archive the old L1 interface as an explicit “phase-loss” NO-GO note

Add a short remark:

- L1/H¹ control implies UE‑INPUT(k=2), but is stronger than necessary.
- L1 control discards phase and is not Weil‑bridge compatible.
- (Optional) include a local blow‑up computation showing why \(\sup_\theta\) derivative bounds are RH‑strength.

---

## P4 (APPENDIX) — Add the one‑page “UE playbook” appendix

Include:
- Definitions,
- target coefficient inequality,
- decomposition into archimedean + zero kernel (ABSORB),
- candidate analytic routes.

---

## P5 (APPENDIX / NOTE) — Weil/Li harness block (non-essential)

Add a non‑load‑bearing section:

- state Weil positivity criterion,
- note contrapositive “off-axis ⇒ negativity witness exists,”
- state “Bridge Lemma target” (what would be needed to identify your kernel with a Weil test),
- emphasize this is a future route only.

---

## P6 (EXPOSITION) — Reader‑guide Part III interpretation remark

One paragraph:
- k=2 mode corresponds to π/2‑carrier / mod‑4 projector intuition.
- Not used in proofs; for conceptual alignment only.

