# v41 Patch Queue (PRE‑BUILD) — paste‑ready TeX edits

Base: `manuscript_v40.tex`  
Purpose: lock the **geometry pivot** and prevent drift.

---

## Patch 1 — Fix the displayed expansion of `D_{a,h}` (hygiene)

**Anchor:** Definition `def:two-sided-shift-diff`.

**Replace the displayed “Equivalently” line**

```tex
\mathcal D_{a,h}(v)=\frac{E'}{E}(v+a+h)-\frac{E'}{E}(v+a-h)-\frac{E'}{E}(v-a+h)+\frac{E'}{E}(v-a-h).
```

**with**

```tex
\mathcal D_{a,h}(v)
=\frac{E'}{E}(v+a+h)-\frac{E'}{E}(v-a-h)
-\frac{E'}{E}(v+a-h)+\frac{E'}{E}(v-a+h).
```

*(This matches `\mathcal D_{a,h}=\mathcal L_{a+h}-\mathcal L_{a-h}` with `\mathcal L_t(v)=(E'/E)(v+t)-(E'/E)(v-t)`.)*

---

## Patch 2 — NEW lemma: aligned‑box Δa forcing NO‑GO

**Insertion point:** immediately after Definition `def:two-sided-endpoint`.

```tex
\begin{lemma}[NO--GO: aligned boxes cannot force the \(\Delta a\) endpoint at nominal coupling]
\label{lem:deltaa-alignedbox-nogo}
Fix \(\kappa\in(0,1/10)\). Let \(B=B(a,m,\delta)\) be the aligned box
\(B(a,m,\delta)=[a-\delta,a+\delta]\times[m-\delta,m+\delta]\) and assume \(\kappa\)--admissibility.
Let \(0<h\le \delta\) with \(\delta,h\le a/4\), and define \(\mathcal D_{a,h}\) and
\(\Phi^{(2\mathrm{s})}_B(a;h)\) as in Definitions~\ref{def:two-sided-shift-diff}--\ref{def:two-sided-endpoint}.

Consider the even quartet toy model
\[
E_0(v)=\bigl((v-a)^2+m^2\bigr)\bigl((v+a)^2+m^2\bigr),
\]
so that \(E_0(\pm a\pm i m)=0\) and \(E_0\) is even and entire.
Then there exists an absolute constant \(C>0\) such that
\[
\Phi^{(2\mathrm{s})}_{B(a,m,\delta)}(a;h)\ \le\ C\,\frac{\delta h}{a^2}.
\]
In particular at the nominal coupling \(h=\delta=\eta a/(\log m)^2\),
\(\Phi^{(2\mathrm{s})}_{B(a,m,\delta)}(a;\delta)=O((\log m)^{-4})\to 0\) as \(m\to\infty\).
Therefore the v40 forcing bullet in Box~\ref{box:missing-lever-v40} cannot hold on aligned boxes.
\end{lemma}

\begin{proof}
Write \(\mathcal L_t(v)=(E_0'/E_0)(v+t)-(E_0'/E_0)(v-t)\) and define \(F(t):=\mathcal L_t(v)\) for fixed \(v\in\partial B_{\kappa/2}\).
Then \(\mathcal D_{a,h}(v)=F(a+h)-F(a-h)\).
Differentiating in \(t\) yields
\[
F'(t)=-\sum_{\rho\in\{\pm a\pm i m\}}\frac{1}{(v+t-\rho)^2}
-\sum_{\rho\in\{\pm a\pm i m\}}\frac{1}{(v-t-\rho)^2}.
\]
On \(\partial B_{\kappa/2}\) and for \(t\in[a-h,a+h]\), the shifts \(v\pm t\) stay a real distance \(\ge a/2\)
from each quartet point \(\rho\) (since \(\delta,h\le a/4\)), hence
\(|v\pm t-\rho|\ge a/2\) and \(|v\pm t-\rho|^{-2}\le 4/a^2\).
Summing over 4 zeros and 2 sums gives \(|F'(t)|\le C_1/a^2\) for an absolute \(C_1\).
By the mean value theorem,
\(|\mathcal D_{a,h}(v)|\le 2h\sup|F'(t)|\le C_2 h/a^2\) on \(\partial B_{\kappa/2}\).
Finally, each side \(I\) has length \(\le C_{\rm geom}\,\delta\), so
\[
\left|\Im\int_I \mathcal D_{a,h}(v)\,dv\right|\le \int_I|\mathcal D_{a,h}|\,|dv|
\le (C_{\rm geom}\,\delta)\,(C_2 h/a^2)
\le C\,\delta h/a^2.
\]
Taking the maximum over sides yields the claim.
\end{proof}
```

---

## Patch 3 — Replace the active frontier box with a Geometry Change Requirement box

**Anchor:** Box `box:missing-lever-v40`.

**Action:** Replace the entire boxed minipage with the following:

```tex
\begin{center}
\fbox{%
\begin{minipage}{0.92\linewidth}
\textbf{OPEN (Geometry Change Requirement; v41).}\label{box:geometry-change-v41}

\medskip
\noindent\textbf{Why this box exists.}
The v40 ML--\(\Delta a\) forcing bullet on aligned boxes is false
(Lemma~\ref{lem:deltaa-alignedbox-nogo}).  Therefore the remaining frontier is not an exponent tweak but a
\emph{geometry/coupling redesign}: choose a witness family and endpoint class for which the off-axis quartet produces a
forceable lower bound on the same contour family on which a gate-passing UE upper bound can be proved.

\medskip
\noindent\textbf{Required closure criteria (OPEN).}
We must specify a family of \(\kappa\)-admissible witness boxes/contours
\(\mathfrak B(a,m,\delta,h)\) (not restricted to aligned boxes) and an endpoint functional \(\Phi^{\rm new}_B\) such that
for the nominal regime \(\delta=\eta a/(\log m)^2\) and an allowed coupling of \(h\) to \(\delta\) (possibly \(h\ll \delta\)):

\begin{enumerate}[leftmargin=1.5em]
\item \textbf{Forceability.}
If \(E\) has an off-axis quartet \(\pm a\pm i m\), then there exists \(B\in\mathfrak B(a,m,\delta,h)\) such that
\(\Phi^{\rm new}_B\ge c_0\) for an absolute \(c_0>0\).

\item \textbf{UE bound (gate passing).}
For all admissible \(B\in\mathfrak B\),
\(\Phi^{\rm new}_B\le \mathrm{UE}^{\rm new}(m,a,\delta,h)\) with \(\delta\)-uniform constants, and
\(\mathrm{UE}^{\rm new}\) passes the exponent-budget gate.

\item \textbf{Resonance robustness.}
Near-resonant quartets at tilts \(a-\varepsilon\) with \(\varepsilon\asymp\delta\) do not create a \(\delta\)-inert obstruction
in \(\Phi^{\rm new}\) that violates (2).
\end{enumerate}

\medskip
\noindent\textbf{Sanity: what is \emph{not} forbidden.}
The NO--GO latches in v40 forbid only specific endpoint classes:
pointwise-in-\(a\) defect endpoints, δ-gain claims on one-pole forced contours, and centered \emph{transfer} at the same δ.
They do \emph{not} forbid a geometry/coupling redesign (e.g. changing the witness family, or choosing \(h\ll\delta\)) provided
forceability and UE are proved on the same family.
\end{minipage}}
\end{center}
```

---

## Patch 4 — Add a short NO‑GO scope remark

**Insertion point:** immediately after Box `box:geometry-change-v41`.

```tex
\begin{remark}[Scope of NO--GO latches]
The NO--GO lemmas in this paper are endpoint-class statements.  For example,
Lemma~\ref{lem:defect-p-ceiling} rules out δ-gain beyond the side-length ceiling for \emph{pointwise-in-\(a\)} defect endpoints,
while Lemma~\ref{lem:defectbox-nogo-ML1} rules out using a one-pole forced defect-box as a δ-gain closure route.
These do not preclude a redesign in which the witness family \(\mathfrak B\) and/or coupling \(h=h(\delta)\) is changed,
provided the resulting endpoint is proved forceable and admits a gate-passing UE bound on the same family.
\end{remark}
```

---

## Patch 5 — Discarded-routes appendix entry (drift prevention)

Add a 6–10 line entry in Appendix `app:discarded` summarizing:
- v40 ML‑Δa on aligned boxes is NO‑GO by Lemma `lem:deltaa-alignedbox-nogo`,
- so future work must pivot to Box `box:geometry-change-v41`.

