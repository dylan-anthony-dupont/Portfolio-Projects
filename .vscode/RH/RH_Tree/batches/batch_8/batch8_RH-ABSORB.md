# Batch 8 — RH-ABSORB (v38 ground truth)

## A) Mechanism selection (commit)

**Committed mechanism: M3 = Pair-isolation / pair-dominance** (the “forced pair gives the only O(1) phase; the rest is δ-small” option).

**Mapping note (to avoid ambiguity):** In the v38 “Missing Lever” OPEN box, the three decisive options are:
- **(M1)** Phase-class UE producing a prefactor **δ^p with p ≥ 1/2** while remaining in the buffered phase endpoint class \(\widetilde D_B\).
- **(M2)** Micro-window clustering: effective local multiplicity \(N_{\mathrm{eff}}(m,\delta_0)=O(1)\) at nominal scale.
- **(M3)** Pair-isolation/pair-dominance: isolate the forced interior pair and show the rest contributes \(O(\delta\log m)\) in the phase endpoint class.

I am choosing **(M3)** because it (i) directly defeats the **one-pole worst-case** that underlies the endpoint-only NO-GO, and (ii) makes the local gate constraint slack (\(q=0\)), so the closure burden concentrates on a single envelope exponent \(p\) (and δ-uniformity).

---

## B) Acceptance-gate audit (for M3)

### B1) Endpoint chain (as in v38)

The S5′ contradiction spine in v38 is:

1. **FORCE:** off-axis quartet \(\Rightarrow\) there exists a \(\kappa\)-admissible aligned box \(B\) with interior zero \(\Rightarrow\)
   \[
   \widetilde D_B(W)\ \ge\ \frac{\pi}{2}.
   \]
2. **ENVELOPE (missing lever):** prove an upper bound of the form
   \[
   \widetilde D_B(W)\ \le\ C_{\rm up}\,\delta^{p}\Big(\mathrm{Res}(m)\ +\ C_{\rm loc}\,\delta^{-\theta}\,G(N_{\rm eff},\kappa)\Big),
   \]
   with **δ-uniform** constants and an explicit growth model
   \[
   G(n,\kappa)\ \le\ C_G\,\kappa^{-u}\,n^{q}.
   \]
3. Evaluate at nominal \(\delta_0(m,\alpha)=\eta\alpha/(\log m)^2\) and apply η-shrinking.

The hard-latched exponent gate in v38 is:
\[
2p\ge 1,\qquad 2(p-\theta)\ge q,\qquad p-\theta>0.
\]

### B2) Gate-check table (M3 instantiation)

Below, “value” means the **effective** exponent in the envelope bound *after* applying M3 (pair isolation).

| Parameter | Meaning in v38 gate | Value under M3 | What must be proved / supplied | Gate impact |
|---|---:|---:|---|---|
| \(p\) | UE prefactor exponent in \(\delta^p\) | **REQUIRED:** \(p\ge \tfrac12\) | **ENVELOPE** must supply a phase-class UE inequality with \(p\ge \tfrac12\) and δ-uniform constants | Controls residual shrink: requires \(2p\ge 1\) since residual is \(O(\delta \log m)\) |
| \(\theta\) | δ-blowup exponent in local bound | \(0\) | **Built-in for phase class:** local phase per zero is δ-inert (per-zero phase \(\le \pi\)) | Makes δ-shrink monotone safe if \(p>0\) |
| \(q\) | local growth exponent from \(n^q\) | \(0\) (effective) | **LOCAL (M3) lemma:** isolate forced pair giving \(O(1)\), and show rest is \(O(\delta\log m)\) so it can be absorbed into the residual term | Makes \(2(p-\theta)\ge q\) automatic |
| \(u\) | κ-exponent in growth model | \(0\) (target) | Preferably the M3 local phase bound should be κ-free; if κ appears, it must be **κ-fixed** and δ-uniform | No direct gate pressure; affects constants only |
| \(w\) | residual log-growth exponent via \(\mathrm{Res}(m)\sim (\log m)^w\) | \(1\) | v38 residual phase budget is \(O(\delta\log m)\), i.e. \(w=1\) | Forces \(p\ge 1/2\) (this is the non-negotiable “residual gate”) |

### B3) PASS/FAIL logic under M3

- **Gate PASS (M3):** If ENVELOPE supplies any \(p\ge 1/2\) (with δ-uniform constants) **and** LOCAL supplies the M3 isolation lemma (so \(q=0\)), then the gate inequalities hold:
  \[
  2p\ge 1,\quad 2(p-0)\ge 0,\quad p>0.
  \]
  At \(\delta_0=\eta\alpha/(\log m)^2\), the envelope upper bound becomes \(O(\eta^{p})\) uniformly in \(m\ge 10\) (residual term gives \(\eta^p (\log m)^{1-2p}\), bounded if \(p\ge 1/2\)). Hence for sufficiently small η this contradicts \(\widetilde D_B(W)\ge \pi/2\).

- **Gate FAIL (M3):** If the only available phase-class envelope estimate has \(p=0\) (as in the endpoint-only θ=0 per pole NO-GO regime), then the first gate constraint \(2p\ge 1\) fails immediately. In that regime, **no η-shrinking can force a contradiction** because the envelope upper bound remains δ-inert at leading order and cannot be driven below \(\pi/2\).

---

## C) Closure theorem patch (diff-only)

### C1) Patch: “Missing Lever” OPEN box (latch M3 + exponents)

```tex
% --- PATCH: S5' Missing Lever (M3 selected) ---
\begin{openbox}{Missing Lever for S5$'$ tail closure (M3 selected)}
To activate Theorem~\ref{thm:S5prime-closure} we must prove a phase-class ENVELOPE inequality
for the buffered phase endpoint $\widetilde D_B$ (Definition~\ref{def:phase-endpoint-buffered})
with \emph{$\delta$-uniform} constants.

\medskip
\noindent\textbf{(ENVELOPE target)} There exist constants
$C_{\rm up},C_{\rm loc},C_G<\infty$ and exponents $p>0$, $\theta\ge 0$, $u,q\ge 0$
such that for every $\kappa$-admissible aligned box $B=B(\alpha,m,\delta)$ with
$0<\delta\le \delta_0(m,\alpha)$ one has
\[
\widetilde D_B(W)
\le
C_{\rm up}\,\delta^{p}\Big(\mathrm{Res}(m)\ +\ C_{\rm loc}\,\delta^{-\theta}\,G(N_{\rm eff},\kappa)\Big),
\qquad
G(n,\kappa)\le C_G\,\kappa^{-u}n^q,
\]
with constants independent of $\delta$ and $m$.

\medskip
\noindent\textbf{(LOCAL redesign: M3 / pair isolation)} In addition, we require the following
pair-isolation input (Lemma~\ref{lem:S5prime-pair-isolation}): writing the local factor as
$Z_{\rm loc}=Z_{\rm pair}\cdot Z_{\rm rest}$ where $Z_{\rm pair}$ consists of the forced interior pair,
the phase endpoint contribution of $Z_{\rm rest}$ satisfies
$\widetilde D_B(Z_{\rm rest})\ll \delta\log m$ on $\partial B_{\kappa/2}$,
while $\widetilde D_B(Z_{\rm pair})\ll 1$.
Equivalently, for the gate bookkeeping one may take $N_{\rm eff}\asymp 1$ (so $q=0$) and
absorb the $O(\delta\log m)$ remainder into $\mathrm{Res}(m)$.

\medskip
\noindent\textbf{(Gate constraints)} Under M3 the local gate is slack ($q=0,\theta=0$), but the
residual term forces $2p\ge 1$ since $\mathrm{Res}(m)=O(\log m)$ in the phase class.
\end{openbox}
% --- END PATCH ---
```

### C2) Patch: Add the M3 isolation lemma (LOCAL-owned, but must be stated here)

```tex
% --- PATCH: M3 pair-isolation lemma (statement only) ---
\begin{lemma}[Pair-isolation for buffered phase endpoints]\label{lem:S5prime-pair-isolation}
Let $B=B(\alpha,m,\delta)$ be a $\kappa$-admissible aligned box and let $\partial B_{\kappa/2}$
be the buffered contour (Definition~\ref{def:phase-endpoint-buffered}).
Assume an off-axis quartet exists with parameters $(\alpha,m)$ so that $E$ has an interior zero
at the dial center $v_+=\alpha+im$ (hence also at $v_-=-\alpha+im$ by symmetry).
Factor the local zero polynomial as
\[
Z_{\rm loc}(v)=Z_{\rm pair}(v)\,Z_{\rm rest}(v),
\]
where $Z_{\rm pair}$ consists exactly of the forced interior pair (with multiplicity), and
$Z_{\rm rest}$ contains the remaining local zeros in $Z(m)$.

Then there exist $\delta$-uniform constants $C_{\rm pair},C_{\rm rest}<\infty$ (independent of $m,\delta$)
such that
\[
\widetilde D_B(Z_{\rm pair}) \le C_{\rm pair},
\qquad
\widetilde D_B(Z_{\rm rest}) \le C_{\rm rest}\,\delta\log m.
\]
\end{lemma}
% --- END PATCH ---
```

### C3) Patch: Add a corollary instantiating Theorem 12.6 under M3 (gate check becomes explicit)

```tex
% --- PATCH: Corollary (M3 gate-pass instantiation) ---
\begin{corollary}[S5$'$ closure under M3 once ENVELOPE supplies $p\ge \tfrac12$]\label{cor:S5prime-M3-gatepass}
Assume the forcing lower bound $\widetilde D_B(W)\ge \pi/2$ (Lemma~\ref{lem:phase-forcing-argprinciple}).
Assume the ENVELOPE inequality of the OPEN box holds with $\theta=0$ and some $p\ge 1/2$
(with $\delta$-uniform constants), and assume Lemma~\ref{lem:S5prime-pair-isolation}.
Then the exponent gate of Theorem~\ref{thm:S5prime-closure} holds and there exists $\eta_\star>0$
such that for all $\eta\in(0,\eta_\star]$ no off-axis quartets exist at any height $m\ge 10$.
\end{corollary}
% --- END PATCH ---
```

---

## D) κ-shrink / δ-uniformity compatibility (non-circularity)

### D1) What must be monotone-safe

In v38 the endpoint \(\widetilde D_B\) is defined on the buffered contour \(\partial B_{\kappa/2}\) under κ-admissibility (Definition 12.19). Shrinking \(\delta\) is permitted to enforce κ-admissibility (and should not be allowed to “break” either forcing or the envelope bound).

For S5′ to be non-circular, we must ensure:

- the **forced interior zero remains interior** when \(\delta\) is shrunk (true if the box is centered at the dial center determined by the zero parameters \((\alpha,m)\));
- the **forcing lower bound is δ-independent** (it is constant-limited at \(\pi/2\));
- the **envelope upper bound is monotone nonincreasing under \(\delta\downarrow\delta'\)** (this is guaranteed if \(p\ge 0\) and \(p-\theta\ge 0\), and \(N_{\rm eff}(m,\delta)\) does not increase when δ shrinks).

### D2) Patch: explicit “κ-shrink compatibility” lemma

```tex
% --- PATCH: κ-shrink compatibility lemma (S5') ---
\begin{lemma}[κ-shrink compatibility for S5$'$]\label{lem:S5prime-kappa-shrink-safe}
Assume the forcing bound $\widetilde D_B(W)\ge \pi/2$ holds on every $\kappa$-admissible aligned box.
Assume the ENVELOPE bound holds on every $\kappa$-admissible aligned box with exponents $p\ge 0$,
$\theta\ge 0$ and constants independent of $\delta$, and assume moreover that
$p-\theta\ge 0$ and that $N_{\rm eff}(m,\delta)$ is nonincreasing under $\delta\downarrow\delta'$.

Then shrinking $\delta$ to any smaller $\kappa$-admissible scale $\delta'\le \delta$ cannot
increase the right-hand side of the ENVELOPE inequality, while the forcing bound is unchanged.
Consequently, verifying the ENVELOPE inequality at the nominal scale $\delta_0(m,\alpha)$
implies it for every $\kappa$-admissible $\delta\le \delta_0(m,\alpha)$, and the S5$'$
forcing-vs-envelope contradiction is non-circular.
\end{lemma}
% --- END PATCH ---
```

Under M3, \(N_{\rm eff}\asymp 1\) is δ-independent, so the monotonicity hypothesis is automatic.

---

## E) S6 explicit-formula mapping (amplitude leak check)

**Does “gate PASS” correspond to forbidding \(x^\beta\) amplitude leaks?** Yes, in the standard RH-equivalent sense.

- A nontrivial zero \(\rho=\beta+i\gamma\) corresponds in width-2 to \(u_\rho=2\rho=(1+a)+im\) with \(a=2\beta-1\) and \(m=2\gamma\), and in the centered coordinate to \(v_\rho=a+im\). Thus **\(\beta>1/2 \iff a>0 \iff \Re(v_\rho)>0\)**.
- In explicit-formula terms (e.g. for \(\psi(x)\)), a zero \(\rho\) contributes a term of size \(x^\beta\) (up to logarithmic factors), so any \(\beta>1/2\) is precisely an “amplitude leak” beyond square-root scale.
- The S5′ contradiction is designed to rule out **any** off-axis quartet, i.e. any \(a\neq 0\). Therefore, if the S5′ closure theorem activates (gate PASS + Missing Lever proven), the conclusion “no \(a\neq 0\) zeros” is exactly “no \(\beta\neq 1/2\) zeros,” which (by standard equivalences) implies the classical RH-quality explicit-formula error terms (and, in particular, forbids \(x^\beta\) leaks with \(\beta>1/2\)).

This mapping is interpretive only; the S5′ proof spine itself remains a forcing-vs-envelope contradiction in the v-frame and does not need explicit-formula machinery.

---

## MANDATORY FINAL SECTION — PATCH PACKET FORMAT

* Callsign: RH-ABSORB
* Result classification: **CONDITIONAL**
* Target gaps closed (by ID): **None fully closed in v38** (this batch latches the **M3 instantiation** and the **non-circular κ-shrink condition** as explicit lemma statements).
* Target gaps still open (by ID):
  - **S5′ Missing Lever / ENVELOPE phase-class UE inequality** (must supply \(p\ge 1/2\) with δ-uniform constants and avoid banned endpoint classes).
  - **M3 LOCAL lemma** `lem:S5prime-pair-isolation` (proof required; statement added here).
* Key conclusions (≤5 bullets):
  1. Under **M3**, the acceptance gate reduces to the single non-negotiable condition \(p\ge 1/2\) (residual gate), with the local gate slack (\(q=0\)).
  2. If ENVELOPE yields \(p\ge 1/2\) in the buffered phase endpoint class \(\widetilde D_B\) with δ-uniform constants, S5′ closure becomes mechanically complete via Theorem~\ref{thm:S5prime-closure}.
  3. If only \(p=0\) is available (endpoint-only θ=0 per pole regime), closure is impossible because \(2p\ge 1\) fails.
  4. κ-admissible shrinking is non-circular and monotone-safe provided \(p-\theta\ge 0\) and \(N_{\rm eff}\) is nonincreasing under δ-shrink (automatic under M3).
  5. A gate PASS implies “no off-axis zeros” and is consistent with the explicit-formula interpretation “no \(x^\beta\) amplitude leaks with \(\beta>1/2\).”
* Paste-ready manuscript edits:
  (i) revised lemma/proposition statements  
  - Insert `lem:S5prime-pair-isolation` (statement) and `lem:S5prime-kappa-shrink-safe` (κ-shrink compatibility).

  (ii) revised definitions/remarks  
  - Patch the S5′ “Missing Lever” OPEN box to explicitly select **M3** and latch \(q=0\), \(\theta=0\), and the residual gate \(p\ge 1/2\).

  (iii) revised theorem/inequality lines  
  - Add corollary `cor:S5prime-M3-gatepass` instantiating Theorem~\ref{thm:S5prime-closure} under M3 once ENVELOPE supplies \(p\ge 1/2\).
* Dependencies on other branches:
  - **RH-ENVELOPE:** must deliver the phase-class UE inequality with \(p\ge 1/2\) in endpoint class \(\widetilde D_B\), with δ-uniform constants, outside the NO-GO endpoint families.
  - **RH-LOCAL:** must prove `lem:S5prime-pair-isolation` (or replace M3 with a proved alternative mechanism).
  - **RH-FORCE / RH-BRIDGE:** must confirm forcing lemma hypotheses remain valid under the κ-admissible δ-shrink policy (no hidden RH-equivalents).
* Referee risk notes (anticipated objections + how addressed):
  1. **Objection:** “Your M3 lemma is unproven; you are smuggling structure.”  
     **Response:** The statement is explicitly isolated as an external dependency; closure is labeled CONDITIONAL.
  2. **Objection:** “κ-shrink could invalidate forcing or worsen the envelope bound.”  
     **Response:** Forcing is constant-limited; envelope monotonicity is enforced by \(p-\theta\ge 0\) plus monotone \(N_{\rm eff}\) (formalized in `lem:S5prime-kappa-shrink-safe`).
  3. **Objection:** “You are implicitly using RH via ‘height’/centering.”  
     **Response:** The v-frame definitions use RH-free parameters \(a=2\beta-1\), \(m=2\gamma\); no tie to \(\beta=1/2\).
