# Batch 10 — RH‑BRIDGE  
**Ground truth:** v39 locked.  
**Target:** ML‑1 (“Transfer / domination”) in Box `box:missing-lever-v39`.  
**Chosen transfer story:** **(T1) Same‑box transfer to the centered defect box** \(\widehat B=B(0,m,\delta)\).  
**Verdict:** **FAIL (NO‑GO in current hypotheses).**  

---

## 1) Executive finding (decision‑grade)

A **same‑height transfer** of forcing from the forced phase endpoint \(\widetilde D_{B(\pm a,m,\delta)}(W)\) to the *centered* defect endpoint \(\Phi^{\rm def}_{B(0,m,\delta)}(a)\) is **impossible** under the currently stated analytic hypotheses (even entire \(E\), \(\kappa\)-admissibility, nominal scale \(\delta\le \delta_0=\eta a/(\log m)^2\)).  

Reason: the forcing lower bound \(\widetilde D_B(W)\ge \pi/2\) (argument principle) is **\(O(1)\)**, while the forced quartet’s direct contribution to the centered defect endpoint is **\(O(\delta/a)\)** by the built‑in cancellation mechanism. Hence any \(\delta\)-uniform domination \(\widetilde D_B(W)\lesssim \Phi^{\rm def}_{B(0,m,\delta)}(a)+\text{absorbable error}\) fails for large \(m\) (since \(\delta_0/a\sim 1/(\log m)^2\to 0\)).  

This is not a “missing estimate”; it is a **structural incompatibility** between (i) forcing by winding of an inner quotient around a box containing a zero, and (ii) the defect endpoint on the centered box, where the quartet produces only a removable singularity.

---

## 2) Proof‑grade NO‑GO lemma (closes ML‑1(T1) as impossible)

### Lemma (NO‑GO: no \(\delta\)-uniform same‑height transfer to the centered defect box)

There do **not** exist constants \(C_{\rm tr}>0\) and an “absorbable” error \(\mathrm{Err}(m,a,\delta)=o_{m\to\infty}(1)\) (uniform for \(\delta=\delta_0(m,a)=\eta a/(\log m)^2\)) such that for every \(\kappa\)-admissible forcing box \(B=B(\pm a,m,\delta)\) and the centered comparison box \(\widehat B=B(0,m,\delta)\) one has
\[
\widetilde D_{B}(W)\ \le\ C_{\rm tr}\,\Phi^{\rm def}_{\widehat B}(a)\ +\ \mathrm{Err}(m,a,\delta),
\]
where \(W\) is the boundary quotient on \(B\) from the Dirichlet outer factorization and \(\Phi^{\rm def}\) is the defect endpoint from \(\mathcal L_a=\partial_v\log\mathcal Q_a\).

#### Proof (counterexample within the manuscript’s hypothesis class)

Take the even entire model function
\[
E(v)\ :=\ \prod_{\sigma,\tau\in\{\pm1\}}\bigl(v-\sigma(a+i\tau m)\bigr),
\]
which has exactly one quartet at height \(m\) with displacement \(a\) (so \(E(\pm a\pm i m)=0\)).  
Fix \(\kappa\in(0,1/10)\) and choose \(\delta\le a/4\) small so that the boxes \(B(\pm a,m,\delta)\) and \(B(0,m,\delta)\) are \(\kappa\)-admissible (no boundary zeros).

1. **Forcing side is \(O(1)\).**  
   On \(B(a,m,\delta)\), \(E\) has a zero in \(B_{\kappa/2}^\circ\), hence the inner quotient \(W=E/G_{\rm out}\) has a zero there.  
   By Lemma `lem:phase-forcing-argprinciple`,  
   \[
   \widetilde D_{B(a,m,\delta)}(W)\ \ge\ \frac{\pi}{2}.
   \]

2. **Centered defect endpoint is \(O(\delta/a)\).**  
   On the centered box \(\widehat B=B(0,m,\delta)\), Lemma `lem:defect-cancellation` gives on \(\partial\widehat B_{\kappa/2}\):
   \[
   \Phi^{\rm def}_{\widehat B}(a)\ \le\ C\,\frac{\delta}{a}\ +\ \delta\,\|H(\cdot+a)-H(\cdot-a)\|_{L^\infty(\partial\widehat B_{\kappa/2})},
   \]
   where \(H\) is holomorphic on \(\widehat B_{\kappa/2}\).  
   Since \(\delta\le a/4\), the domain \(\widehat B_{\kappa/2}\) stays inside a fixed compact set (depending on \(a,m\) but not shrinking hypotheses), so \(\|H(\cdot+a)-H(\cdot-a)\|_{L^\infty}\) is bounded independently of \(\delta\). Therefore \(\Phi^{\rm def}_{\widehat B}(a)=O(\delta/a)\).

3. **Nominal policy forces a contradiction.**  
   Under \(\delta=\delta_0(m,a)=\eta a/(\log m)^2\), we have \(\delta/a=\eta/(\log m)^2\to 0\) as \(m\to\infty\), hence
   \[
   \Phi^{\rm def}_{\widehat B}(a)\ =\ o_{m\to\infty}(1),
   \]
   while \(\widetilde D_B(W)\ge\pi/2\).  
   This contradicts any inequality of the displayed transfer form with \(\delta\)-uniform \(C_{\rm tr}\) and absorbable \(\mathrm{Err}\).

Therefore ML‑1(T1) (centered same‑height transfer) is **NO‑GO** under the current hypotheses. ∎

---

## 3) Forceability‑gate integrity and toy‑model reconciliation

* This NO‑GO is **consistent** with the existing cancellation lemma: Lemma `lem:defect-cancellation` already proves the quartet’s contribution to \(\Phi^{\rm def}_{B(0,m,\delta)}(a)\) is shrinkable \(O(\delta/a)\), so any successful ML‑1 transfer to the centered defect box would *force* a non‑shrinkable defect endpoint from a single quartet, contradicting the cancellation mechanism.
* Therefore, **any viable transfer must change the comparison geometry** (or add new, manuscript‑explicit structure beyond “even entire + admissible box”).

---

## 4) What this implies for v40 planning (non‑drift, but decisive)

**Conclusion for ML‑1:** as written in Box `box:missing-lever-v39`, ML‑1 cannot be closed with \(\widehat B=B(0,m,\delta)\) (or any \(O(\delta)\)-shift that keeps the buffered contour away from the *defect singularities* at \(v=\pm(2a+i m)\)).  

Only two logically consistent options remain:

1. **Replace ML‑1 by a new forcing lemma for \(\Phi^{\rm def}\)** on a box enclosing a genuine zero/pole of \(\mathcal Q_a\) (e.g. centered near \(v=2a+i m\) or \(v=-2a+i m\)), per the forceability gate (“new forcing lemma” branch).  
2. **Add additional hypotheses that force the \(H(v+a)-H(v-a)\) term to be \(O(1)\)** on the centered box (a “resonance transfer” hypothesis). But this immediately collides with ML‑3’s resonance NO‑GO (defect \(\delta\)-inertia), so it is not an obviously viable route.

---

## 5) S6 harness cross‑check (explicit‑formula interpretation)

Mapping: \(u=2s\), \(v=u-1\). An off‑critical‑line zero \(s=\beta+i\gamma\) corresponds to \(v=(2\beta-1)+i(2\gamma)\). Hence \(a=2\beta-1\), \(m=2\gamma\).  

* \(\widetilde D_B(W)\) is a **topological winding witness** of a zero in the forcing box; it is not directly a prime‑side amplitude functional.  
* The centered defect endpoint \(\Phi^{\rm def}_{B(0,m,\delta)}(a)\) is designed to detect left/right asymmetry \(\mathcal Q_a(v)=E(v+a)/E(v-a)\), but the quartet produces only a **removable singularity** at \(v=i m\), so there is no automatic \(O(1)\) “\(x^\beta\) leak witness” at that same height/center.  

Thus ML‑1(T1) failing is conceptually aligned with the fact that *phase forcing* and *defect asymmetry* are not equivalent “amplitude leak” witnesses without extra structure.

---

# PATCH PACKET (mandatory)

* Callsign: RH‑BRIDGE  
* Result classification: **FAIL (NO‑GO for ML‑1(T1) same‑height centered transfer)**  
* Target gaps closed (by ID): **ML‑1 (T1 formulation) — closed as NO‑GO**  
* Target gaps still open (by ID): **ML‑2, ML‑3; ML‑1 only via alternative geometry (defect‑pole forcing) or extra hypotheses**  
* Key conclusions (≤5 bullets):  
  1. Under current v39 hypotheses, **no \(\delta\)-uniform domination** can transfer forcing from \(\widetilde D_B(W)\) to \(\Phi^{\rm def}_{B(0,m,\delta)}(a)\).  
  2. The obstruction is structural: **argument‑principle forcing is \(O(1)\)**, while the centered defect endpoint from a single quartet is **\(O(\delta/a)\)** by cancellation.  
  3. Therefore ML‑1 as written (suggesting \(\widehat B=B(0,m,\delta)\)) is **not closable**.  
  4. Any salvage must either (i) force \(\Phi^{\rm def}\) on a box enclosing a genuine \(\mathcal Q_a\) zero/pole, or (ii) add a resonance‑type hypothesis—likely incompatible with ML‑3.  
  5. v40 should **revise the Missing Lever box** to record this NO‑GO explicitly and prevent drift.

* Paste‑ready manuscript edits (TeX blocks):  

  (i) **Insert lemma (place near Box `box:missing-lever-v39` or immediately after Lemma `lem:defect-cancellation`)**
  ```tex
  \begin{lemma}[NO--GO: no $\delta$--uniform transfer to the centered defect box]
  \label{lem:ML1-samebox-nogo}
  Fix $\kappa\in(0,1/10)$. There do not exist constants $C_{\rm tr}>0$ and an absorbable error
  ${\rm Err}(m,a,\delta)=o_{m\to\infty}(1)$ (uniform for $\delta=\delta_0(m,a)=\eta a/(\log m)^2$)
  such that for every $\kappa$--admissible forcing box $B=B(\pm a,m,\delta)$ and the centered box
  $\widehat B=B(0,m,\delta)$ one has
  \[
  \widetilde D_{B}(W)\ \le\ C_{\rm tr}\,\Phi^{\rm def}_{\widehat B}(a)\ +\ {\rm Err}(m,a,\delta).
  \]
  In particular, ML--1 cannot be discharged with $\widehat B=B(0,m,\delta)$ under the current hypotheses.
  \end{lemma}

  \begin{proof}
  Consider the even entire model
  $E(v)=\prod_{\sigma,\tau\in\{\pm1\}}\bigl(v-\sigma(a+i\tau m)\bigr)$.
  Choose $\delta\le a/4$ so that $B(\pm a,m,\delta)$ and $B(0,m,\delta)$ are $\kappa$--admissible.
  Then $E$ (hence $W$) has a zero in $B(a,m,\delta)_{\kappa/2}^\circ$, so
  $\widetilde D_{B(a,m,\delta)}(W)\ge \pi/2$ by Lemma~\ref{lem:phase-forcing-argprinciple}.
  On the centered box $\widehat B=B(0,m,\delta)$, Lemma~\ref{lem:defect-cancellation} gives
  $\Phi^{\rm def}_{\widehat B}(a)\le C\,\delta/a+\delta\|H(\cdot+a)-H(\cdot-a)\|_\infty=O(\delta/a)$.
  Under $\delta=\delta_0(m,a)=\eta a/(\log m)^2$ the RHS is $O(1/(\log m)^2)\to0$ as $m\to\infty$,
  contradicting any transfer inequality with $\delta$--uniform $C_{\rm tr}$ and absorbable ${\rm Err}$.
  \end{proof}
  ```

  (ii) **Edit Box `box:missing-lever-v39` (ML‑1 item) to prevent a false target**
  ```tex
  % In Box~\ref{box:missing-lever-v39}, item (Transfer / domination):
  % replace D_B(W) by \widetilde D_B(W) and record the centered-box NO--GO.

  \item \textbf{(Transfer / domination)} Prove a domination link that connects the forced phase endpoint
  $\widetilde D_B(W)$ to the UE--friendly \emph{defect} endpoint class:
  \[
  \widetilde D_B(W)\ \le\ C_{\rm tr}\,\Phi^{\rm def}_{\widehat B}(a)\ +\ {\rm Err}(m,a,\delta),
  \]
  for every $\kappa$--admissible aligned box $B=B(\pm a,m,\delta)$ at the nominal scale
  $0<\delta\le \delta_0(m,a)=\eta\,a/(\log m)^2$.
  \emph{NO--GO:} choosing $\widehat B=B(0,m,\delta)$ (or any $O(\delta)$ shift away from the defect singularities
  $v=\pm(2a+i m)$) cannot yield a $\delta$--uniform transfer; see Lemma~\ref{lem:ML1-samebox-nogo}.
  ```

  (iii) **(Optional but recommended) Add a one‑line remark near the phase forceability gate**
  ```tex
  \begin{remark}
  Lemma~\ref{lem:ML1-samebox-nogo} shows $\Phi^{\rm def}_{B(0,m,\delta)}(a)$ does not dominate the forced endpoint
  $\widetilde D_B(W)$; any forcing transfer to defect endpoints must therefore use different geometry (a box enclosing
  a genuine zero/pole of $\mathcal Q_a$) or add new hypotheses beyond $\kappa$--admissibility.
  \end{remark}
  ```

* Dependencies on other branches: **None** (uses existing v39 lemmas: `lem:phase-forcing-argprinciple`, `lem:defect-cancellation`).  
* Referee risk notes (anticipated objections + how addressed):  
  1. **“Counterexample not equal to the true \(E\)”** — correct; the point is that **v39 hypotheses** do not restrict \(E\) beyond “even entire + admissibility.” Thus ML‑1(T1) cannot be proved from stated assumptions without adding new structure.  
  2. **Admissibility choices** — choose \(\delta\le a/4\) and \(\kappa\in(0,1/10)\) so boundaries avoid the quartet; standard in v39.  
  3. **Notation drift** — Box `box:missing-lever-v39` uses \(D_B(W)\) but the forced endpoint in v39 is \(\widetilde D_B(W)\) (Definition `def:Db-tilde-phase`). The patch above corrects this to avoid future logical miswiring.
