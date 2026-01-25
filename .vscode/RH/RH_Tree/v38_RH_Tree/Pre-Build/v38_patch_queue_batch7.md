# v38 patch queue — Batch 7 (v37 → v38) — 2026-01-25
*(Each patch item is paste-ready. Apply in the order below to avoid label drift.)*

---

## PQ38.1 — Insert corollary: forcing automatic for \(\widetilde D_B\) (close G‑2b)
**Where:** immediately after Lemma 12.17 (`lem:phase-forcing-argprinciple`).  
**Source:** Batch‑7 RH‑FORCE.

```tex
% --- Insert immediately after Lemma 12.17 ---
\begin{corollary}[S5$'$ forcing is automatic for the buffered phase endpoint]
\label{cor:S5prime-force-automatic}
Let $B=B(\alpha,m,\delta)$ be a $\kappa$--admissible aligned box and let $W$ be its boundary quotient.
Define $\widetilde D_B(W)$ as in Definition~\ref{def:buffered-phase-endpoint}.
If $W$ has at least one zero in $B_{\kappa/2}^\circ$ (equivalently, $E$ has at least one zero there), then
\[
\widetilde D_B(W)\ge \pi/2.
\]
In particular, in Theorem~\ref{thm:S5prime-budget}, the hypothesis \textup{(S5$'$--FORCE)}
may be taken with $c_{\mathrm{force}}:=\pi/2$ and $\Xi(m)\equiv 0$ when
$\mathcal D_B\equiv \widetilde D_B$.
\end{corollary}
```

---

## PQ38.2 — Parenthetical correction in Definition 12.11 (close G‑10 wording bug)
**Where:** replace only the parenthetical line inside Definition 12.11.  
**Source:** Batch‑7 RH‑FORCE (minimal-risk patch).

```tex
% --- Replace the parenthetical sentence in Definition 12.11 ---
(\emph{This lies strictly inside $B$. It is separated from the unshifted vertical line
$I_+=\{\alpha+iy:|y-m|\le\delta\}$ by horizontal distance $\lambda\delta$, and its distance to $\partial B$
 is at least $(1-\lambda)\delta$.})
```

---

## PQ38.3 — Insert forceability gate remark (harden NO‑GO constraints)
**Where:** near Remark 12.18 / S5′ frontier list.  
**Source:** Batch‑7 RH‑FORCE.

```tex
% --- Add near Remark 12.18 (or in the S5' frontier gate list) ---
\begin{remark}[Forceability gate for phase endpoints]
\label{rem:forceability-gate-phase}
The single-box forcing chain in this manuscript supplies a lower bound only for a \emph{forced endpoint}.
For S5$'$ we have a direct forcing lemma for the buffered phase endpoint
$\widetilde D_B(W)$ (Lemma~\ref{lem:phase-forcing-argprinciple}).
Consequently, any proposed S5$'$ contradiction endpoint $\Phi_B$ is admissible only if either
\begin{enumerate}
\item $\Phi_B(W)\ge \widetilde D_B(W)$ on every $\kappa$--admissible aligned box (so forcing transfers), or
\item a new forcing lemma is proved that targets $\Phi_B$ directly.
\end{enumerate}
Without such a link, the forcing half and envelope half of the S5$'$ budget theorem are logically
 disconnected.
\end{remark}
```

---

## PQ38.4 — Replace local phase lemma with strengthened line-segment version (close G‑8 θ)
**Where:** replace Lemma `lem:local_phase_delta_inert` in Section 12 (S5′ toolkit).  
**Source:** Batch‑7 RH‑LOCAL.

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

---

## PQ38.5 — Insert Bridge collar nonvanishing lemma (close G‑6 for phase endpoints)
**Where:** immediately after Definition 12.16 (Buffered boundary phase endpoint), before any branch choice of \(\arg\).  
**Source:** Batch‑7 RH‑BRIDGE.

```tex
% Place immediately after Definition 12.16 (Buffered boundary phase endpoint).

\begin{lemma}[Collar nonvanishing for phase arcs]\label{lem:phase_collar_nonvanishing}
Let $B=B(\alpha,m,\delta)$ be an aligned box and assume $\kappa$--admissibility:
\[
\dist(\partial B,\mathcal Z(E))\ge \kappa\delta.
\]
Let $B_{\kappa/2}:=\{v\in B:\dist(v,\partial B)\ge \kappa\delta/2\}$.
Then there exists $r=r(\kappa,\delta)>0$ (e.g. $r=\kappa\delta/4$) such that
\[
\dist(\partial B_{\kappa/2},\mathcal Z(E))\ge r.
\]
In particular, $E$ is holomorphic and nonvanishing on an open $r$--neighborhood of
$\partial B_{\kappa/2}$, and for every side $S\subset \partial B_{\kappa/2}$ the phase
increment $\Delta_S \arg E$ (Definition~\ref{def:phase_increment}) is well-defined.

If $G_{\rm out}$ is the Dirichlet outer factor on $B$ and $W:=E/G_{\rm out}$, then $G_{\rm out}$
is holomorphic and zero-free on $B^\circ$, hence $W$ is holomorphic on $B^\circ$ and also
nonvanishing on an open neighborhood of $\partial B_{\kappa/2}$. Consequently
$\Delta_S\arg W$ is well-defined for every side $S\subset\partial B_{\kappa/2}$.
\end{lemma}

\begin{lemma}[Refined kernel phase bound on a vertical segment]\label{lem:phase_kernel_refined}
Let $x_0\in\mathbb R$, $\delta_*>0$, and let $I(x_0;\delta_*):=\{x_0+iy:\ |y-m|\le \delta_*\}$
be oriented upward. Let $\rho=x_\rho+i y_\rho\notin I(x_0;\delta_*)$ and set $d:=|x_0-x_\rho|$.
Then
\[
\left|\Im\int_{I(x_0;\delta_*)}\frac{dv}{v-\rho}\right|
= \Big|\arg(x_0+i(m+\delta_*)-\rho)-\arg(x_0+i(m-\delta_*)-\rho)\Big|
\le 2\arctan\!\Big(\frac{\delta_*}{d}\Big)
\le \min\!\Big(\pi,\frac{2\delta_*}{d}\Big),
\]
with the convention that the right-hand side is $\le \pi$ when $d=0$.
\end{lemma}
```

---

## PQ38.6 — Insert refined kernel phase lemma (optional but recommended)
**Where:** after PQ38.4 (local phase lemma) or near other kernel geometry lemmas.  
**Source:** Batch‑7 RH‑BRIDGE (text lemma; copied verbatim).

```tex
\begin{lemma}[Refined kernel phase bound on a vertical segment]\label{lem:phase_kernel_refined}
Let $x_0\in\mathbb R$, $\delta_*>0$, and let $I(x_0;\delta_*):=\{x_0+iy:\ |y-m|\le \delta_*\}$
be oriented upward. Let $\rho=x_\rho+i y_\rho\notin I(x_0;\delta_*)$ and set $d:=|x_0-x_\rho|$.
Then
\[
\left|\Im\int_{I(x_0;\delta_*)}\frac{dv}{v-\rho}\right|
= \Big|\arg(x_0+i(m+\delta_*)-\rho)-\arg(x_0+i(m-\delta_*)-\rho)\Big|
\le 2\arctan\!\Big(\frac{\delta_*}{d}\Big)
\le \min\!\Big(\pi,\frac{2\delta_*}{d}\Big),
\]
with the convention that the right-hand side is $\le \pi$ when $d=0$.
\end{lemma}
```

---

## PQ38.7 — Insert endpoint-only NO‑GO lemma + proof (install Batch‑7 filter; narrows G‑4′)
**Where:** in Section 12 directly under the “Missing Lever / UE redesign” discussion.  
**Source:** Batch‑7 RH‑ENVELOPE.

```tex
\begin{lemma}[Endpoint-only NO--GO: $\theta=0$ per pole forbids any $p>0$ UE gain]
\label{lem:phase-UE-theta0-nogo}
Fix $\kappa\in(0,1/10)$. Let $B=B(\alpha,m,\delta)$ be an aligned box and let
$E$ be holomorphic on a neighborhood of $\overline B$, with outer factorization
$E=G_{\rm out}\,W$ on $B$ (so $W$ is inner on $B$).

Assume $\Phi_B$ is a boundary functional acting on the trace of $E'/E$ and that
there exist constants $C_{\rm loc}=C_{\rm loc}(\kappa)$ and $u\ge 0$ such that,
for every $\rho\in B_{\kappa/2}$ and the test function $E_\rho(v):=v-\rho$, one has
the per-pole bound
\[
\Phi_B\!\left(\frac{E_\rho'}{E_\rho}\right)
=\Phi_B\!\left(\frac1{v-\rho}\right)
\le C_{\rm loc}\,\kappa^{-u},
\]
uniformly in $\delta$ (this is the strong form of ``$\theta=0$ per pole'').

Then there do not exist constants $C_{\rm up}>0$ and $p>0$ (independent of $\delta$)
such that the phase-class UE inequality
\[
\widetilde D_B(W) \;\le\; C_{\rm up}\,\delta^{p}\,\Phi_B\!\left(\frac{E'}{E}\right)
\]
holds for all such boxes $B$ and all such holomorphic $E$.
In fact, for $E=E_\rho(v)=v-\rho$ with $\rho\in B_{\kappa/2}$, the inequality forces
\[
\frac{\pi}{2} \;\le\; C_{\rm up}\,C_{\rm loc}\,\kappa^{-u}\,\delta^{p},
\]
which fails for sufficiently small $\delta$.
\end{lemma}

\begin{proof}
Fix $\rho\in B_{\kappa/2}$ and take $E(v)=E_\rho(v)=v-\rho$.
Then $E$ has a zero in $B_{\kappa/2}$, so its inner quotient $W$ has a zero in $B_{\kappa/2}$.
By Lemma~12.17 (phase forcing by the argument principle), this implies
$\widetilde D_B(W)\ge \pi/2$.
On the other hand $E'/E=1/(v-\rho)$, so by hypothesis
$\Phi_B(E'/E)\le C_{\rm loc}\kappa^{-u}$ uniformly in $\delta$.
Substituting into the claimed UE bound gives
$\pi/2 \le C_{\rm up}C_{\rm loc}\kappa^{-u}\delta^{p}$, contradicting $p>0$ as $\delta\to 0$.
\end{proof}
```

---

## PQ38.8 — Insert consequence remark (binds NO‑GO to the Missing Lever box)
**Where:** immediately after PQ38.7.  
**Source:** Batch‑7 RH‑ENVELOPE.

```tex
\begin{remark}[Consequence for P38.2: endpoint-only $\theta=0$ cannot yield any $p>0$ gain]
Any attempt to close G--4$'$ by choosing an endpoint class $\Phi_B$ that is $\delta$--inert on each
local Cauchy kernel $(v-\rho)^{-1}$ (``$\theta=0$ per pole'') cannot produce a $\delta^p$ UE gain with
$p>0$ via a purely local analytic argument: the test input $E(v)=v-\rho$ contradicts such a bound
(Lemma~\ref{lem:phase-UE-theta0-nogo}). Therefore any successful phase-class UE inequality with
$p\ge 1/2$ must incorporate additional structure that defeats the one-pole model (e.g.\ forcing redesign
or pair-isolation/cancellation in the local factor).
\end{remark}
```

---

## PQ38.9 — Insert “local isolation needed” lemma (recommended design constraint)
**Where:** directly after PQ38.8 or inside the Missing Lever box context.  
**Source:** Batch‑7 RH‑ENVELOPE.

```tex
\begin{lemma}[LOCAL isolation needed to beat the one-pole obstruction]
\label{lem:local-isolation-needed}
Fix $\kappa\in(0,1/10)$ and let $\Phi_B$ be the endpoint class targeted in S5′.
To obtain any UE gain $p>0$ with a local exponent $\theta<p$ in the S5′ budget theorem,
it is necessary to prove a structural statement of the following form:

Whenever $B=B(\alpha,m,\delta)$ is $\kappa$-admissible at the nominal scale
$\delta\le \delta_0(m,\alpha)$ and $Z_{\rm loc}$ is the local factor of $E$ on $B$,
there exists a factorization
\[
Z_{\rm loc} \;=\; Z_{\rm forced}\cdot Z_{\rm rest}
\]
such that (i) $Z_{\rm forced}$ contains only $O(1)$ zeros (the “forced pair”), and (ii)
\emph{in the chosen endpoint class} one has the δ-small bound
\[
\Phi_B\!\left(\frac{Z_{\rm rest}'}{Z_{\rm rest}}\right)
\;\le\;
C\,\kappa^{-u}\,(\log m)^{q_{\rm eff}}\,\delta^{-(\theta_{\rm eff})}
\qquad\text{with}\qquad \theta_{\rm eff}<p
\]
(and ideally $\theta_{\rm eff}=0$ with $q_{\rm eff}=0$ or with an extra $\delta$ factor).
\end{lemma}
```

---

## PQ38.10 — Insert the “Missing Lever box (S5′)” latch (prevents silent closure)
**Where:** just before `thm:S5prime-closure` and/or inside `rem:S5prime-gate`.  
**Source:** Batch‑7 RH‑ABSORB.

```tex
% === BEGIN: Missing Lever box (S5') ===
\begin{center}
\fbox{\begin{minipage}{0.96\linewidth}
\textbf{OPEN (Missing Lever for S5$'$ tail closure; no silent closure).}
\vspace{2mm}

Fix $\eta\in(0,1]$, $\kappa\in(0,1/10)$, and the nominal scale
$\delta_0(m,\alpha)=\eta\alpha/(\log m)^2$.
Let $B=B(\pm \alpha,m,\delta)$ be any $\kappa$--admissible aligned box with $0<\delta\le \delta_0(m,\alpha)$.
Let $G_{\rm out}$ be the Dirichlet outer factor on $B^\circ$ and $W:=E/G_{\rm out}$ the corresponding quotient.
Let $\widetilde D_B(W)$ be the buffered boundary phase endpoint (Def.~\ref{def:Db-tilde-phase}).

\medskip
\textbf{FORCE (already proved).}
If $W$ has a zero in $B^\circ_{\kappa/2}$ then $\widetilde D_B(W)\ge \pi/2$
(Lemma~\ref{lem:phase-forcing-argprinciple}).

\medskip
\textbf{ENVELOPE (missing).}
To activate Theorem~\ref{thm:S5prime-closure}, it remains to prove a phase-class UE+split bound of the form
\[
\widetilde D_B(W)\ \le\ C_{\rm up}\,\delta^{p}\Bigl(\mathrm{Res}(m)+C_{\rm loc}\,\delta^{-\theta}\,G(N_{\rm eff}(m,\delta),\kappa)\Bigr),
\]
uniformly for all $m\ge 10$, all $\alpha\in(0,1]$, and all $\kappa$--admissible $0<\delta\le\delta_0(m,\alpha)$,
with $C_{\rm up},C_{\rm loc}$ independent of $\delta$ and with an explicit growth model
$G(n,\kappa)\le C_G\,\kappa^{-u}\,n^{q}$.

\medskip
\textbf{BUDGET GATE (non-negotiable).}
The declared exponent tuple $(p,\theta,q)$ must satisfy the acceptance gate:
\[
2p\ge 1,\qquad 2(p-\theta)\ge q,\qquad p-\theta>0,
\]
otherwise uniform $\eta$--shrinking at $\delta=\delta_0(m,\alpha)$ is impossible under constant-limited forcing.

\medskip
\textbf{LOCAL REDESIGN (one of these is decisive).}
Because phase is $\delta$--inert per zero (Lemma~\ref{lem:local-phase-delta-inert}),
the default choice $N_{\rm eff}(m,\delta)=N_{\rm loc}(m)\sim \log m$ forces $q=1$.
Any one of the following would be decisive:
(i) a phase-class UE mechanism achieving $p\ge 1/2$ while keeping $\theta=0$ in the same endpoint class;
(ii) a micro-window clustering bound $N_{\rm eff}(m,\delta_0)=O(1)$ (so $q=0$ effectively);
(iii) a pair-isolation mechanism: only the forced pair contributes $O(1)$ to $\widetilde D_B$ while the remainder contributes $O(\delta\log m)$.

\medskip
\textbf{NO CLAIM POLICY.}
Until the ENVELOPE bound and one decisive LOCAL redesign item are proved in-text (or cited referee-grade),
the manuscript makes \emph{no} claim of tail closure and \emph{no} claim of RH from S5$'$.
\end{minipage}}
\end{center}
% === END: Missing Lever box (S5') ===
```

---

## PQ38.11 — (Optional) Insert pair-isolation remark (only if lemma `lem:phase_kernel_refined` is included)
**Where:** near the frontier list / S5′ redesign agenda.  
**Source:** Batch‑7 RH‑BRIDGE.

```tex
% Optional: insert after Corollary 12.15 to expose the pair-isolation obligation.

\begin{remark}[Phase-local contributions: what must be proved for closure]\label{rem:phase_pair_isolation}
Lemma~\ref{lem:phase_kernel_refined} shows that a zero $\rho$ contributes $O(\delta_*/d)$ to the
phase increment on a vertical segment at horizontal separation $d$.
Thus, to make a phase endpoint shrink with $\delta$ (and satisfy the budget condition
$p-\theta\ge 1/2$), it suffices to prove a structural lemma of the form:
all but $O(1)$ zeros in $\mathcal Z_{\rm loc}(m)$ have horizontal separation $d\gg \delta$ from the
endpoint contour, so their total phase contribution is $O(\delta\log m)$.
\end{remark}
```

---

## PQ38.12 — Repro-pack latch updates
**Where:** repro pack schema + verifier.  
**Action:** keep `missing_lever_open=true`; optionally add `phase_endpoint_only_nogo_installed=true`.
