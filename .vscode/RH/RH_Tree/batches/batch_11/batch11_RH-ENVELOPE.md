# Batch 11 — RH-ENVELOPE  
**Callsign:** RH-ENVELOPE  
**Mechanism choice (hard constraint):** **(C) non-pointwise UE** (2D “(a,v) rectangle” averaging; GEO‑C3).  

This note delivers the **UE half** of the v41 “Geometry Change Requirement” by proposing a geometry/endpoint pair whose **upper bound is provably < π/2** at the nominal coupling scale, *without* using point evaluation and without smuggling RH. This is framed as a *candidate UE package* that FORCE can try to pair with a compatible forcing lemma.  

Key context: the post‑v40 audit established **NG‑Δa‑A**: aligned‑box forcing for the pointwise Δa endpoint is false, so the active frontier is a **geometry/coupling redesign**, not an exponent tweak. 【968:1†integration_notes_v41_prebuild.md†L22-L45】【968:4†v41_next_build_plan_diff.md†L18-L28】  

---

## (1) Geometry family \(\mathscr B\) (GEO‑C3: 2D “\((a,v)\)” rectangle)

**v‑box component (standard):** for parameters \(m\ge 10\), \(a\in(0,1]\), \(0<\delta\le a/4\), let  
\[
B(a,m,\delta):=[a-\delta,a+\delta]\times[m-\delta,m+\delta]\subset\mathbb C_v,
\]
with buffered contour \(\partial B_{\kappa/2}\) as in the manuscript (fixed \(\kappa\in(0,1/10)\)).  

**a‑window component (new):** for \(h\in(0,a/4]\), set  
\[
\mathcal I_a(h):=[a-h,a+h].
\]

**2D witness geometry (product):**  
\[
\mathscr B(a,m,\delta,h)\ :=\ \mathcal I_a(h)\ \times\ \partial B(a,m,\delta)_{\kappa/2}.
\]

This is exactly the “treat \(a\) as an orthogonal axis” candidate direction **GEO‑C3** flagged in the v41 prebuild notes. 【968:2†integration_notes_v41_prebuild.md†L7-L11】

---

## (2) Endpoint \(\Phi_{\mathscr B}\) (phase‑class, non‑pointwise in \(a\))

Recall the v40 defect primitives (for \(E\) entire/even, in v‑frame):  
\[
\mathcal Q_a(v):=\frac{E(v+a)}{E(v-a)},\qquad 
\mathcal L_a(v):=\partial_v\log \mathcal Q_a(v)=\frac{E'}{E}(v+a)-\frac{E'}{E}(v-a),
\]
and the two‑sided shift‑difference (in \(a\))  
\[
\mathcal D_{a,h}(v):=\mathcal L_{a+h}(v)-\mathcal L_{a-h}(v),
\]
as in v40 (noting v41 Patch‑1 corrects the displayed expansion to match this definition). 【968:8†manuscript_v40.pdf†L79-L107】【968:9†v41_patch_queue.md†L8-L27】

**New endpoint (2D averaged phase flux):** for \(B=B(a,m,\delta)\), define  
\[
\boxed{
\Phi^{\rm 2D}_{B}(a;h)\ :=\ \max_{I\in{\rm Sides}(\partial B_{\kappa/2})}
\left|
\Im\int_{t\in \mathcal I_a(h)}\ \int_{v\in I}\ \mathcal D_{t,h}(v)\,dv\,dt
\right|.
}
\]

*Why this is “phase‑class” and not a forbidden swap:* it is built from **imaginary parts of boundary integrals of log‑derivative expressions** (no point evaluation, no \(\sup_{\partial B}\), no absolute \(L^r(\partial B)\) endpoint replacement). The only non‑pointwise ingredient is the additional integration over an \(a\)-window.

---

## (3) Main UE bound (proof‑grade lemma) and \(\pi/2\) clearance

### Lemma (2D‑averaged Δa upper envelope; rectangle geometry)

Fix \(\kappa\in(0,1/10)\). Let \(m\ge 10\), \(a\in(0,1]\), and choose parameters  
\[
0<\delta\le \frac a4,\qquad 0<h\le \frac a4,
\]
and let \(B=B(a,m,\delta)\) be \(\kappa\)-admissible with buffered contour \(\partial B_{\kappa/2}\).  

Assume:
1. (**Holomorphy on the evaluation collar**) For every \(t\in[a-2h,a+2h]\), the functions \(E(v\pm t)\) are nonzero on an open neighborhood of \(\partial B_{\kappa/2}\).  
   (Equivalently: \(\mathcal L_t\) and \(\mathcal D_{t,h}\) are holomorphic near \(\partial B_{\kappa/2}\) for the required \(t\)-range.)
2. (**Residual envelope input, δ‑uniform**) On the same neighborhood, we may decompose
   \[
   \frac{E'}{E}(w)=\frac{F'}{F}(w)+\frac{Z'_{\rm loc}}{Z_{\rm loc}}(w),
   \]
   where \(F\) is the residual factor and \(Z_{\rm loc}\) is the local factor, with the δ‑uniform bound
   \[
   \sup_{w\in \mathcal N(\partial B_{\kappa/2})}\left|\frac{F'}{F}(w)\right|\ \le\ C_{\rm res,1}\log m + C_{\rm res,2}
   \]
   (constants depend only on the fixed box shape and the constants ledger, not on \(\delta\)).  

Then there exists an absolute rectangle constant \(C_{\rm geom}>0\) (side‑length bound on \(\partial B_{\kappa/2}\)) such that:
\[
\boxed{
\Phi^{\rm 2D}_B(a;h)
\ \le\ 
8\,C_{\rm geom}\,\delta\,h\,
\left(
C_{\rm res,1}\log m+C_{\rm res,2}
+\sup_{\substack{t\in[a-2h,a+2h]\\ v\in\partial B_{\kappa/2}}}
\left|\frac{Z'_{\rm loc}}{Z_{\rm loc}}(v+t)\right|
+\sup_{\substack{t\in[a-2h,a+2h]\\ v\in\partial B_{\kappa/2}}}
\left|\frac{Z'_{\rm loc}}{Z_{\rm loc}}(v-t)\right|
\right).
}
\]

Moreover, in the “geometrically separated” regime where every local zero \(\rho\) contributing to \(Z_{\rm loc}\) satisfies  
\[
\inf_{\substack{t\in[a-2h,a+2h]\\ v\in\partial B_{\kappa/2}}}|(v\pm t)-\rho|\ \ge\ \frac a2,
\]
and if \(N_{\rm loc}(m)\) denotes the local window count used in the manuscript, we have the crude but δ‑uniform bound
\[
\sup_{\substack{t\in[a-2h,a+2h]\\ v\in\partial B_{\kappa/2}}}
\left|\frac{Z'_{\rm loc}}{Z_{\rm loc}}(v\pm t)\right|
\ \le\ 
\frac{2\,N_{\rm loc}(m)}{a}.
\]
Hence,
\[
\boxed{
\Phi^{\rm 2D}_B(a;h)
\ \le\ 
8\,C_{\rm geom}\,\delta\,h\,
\left(
C_{\rm res,1}\log m+C_{\rm res,2}+\frac{4\,N_{\rm loc}(m)}{a}
\right).
}
\]

#### Proof (referee‑grade skeleton)

Let \(I\) be a side of \(\partial B_{\kappa/2}\). By definition and triangle inequality,
\[
\left|\Im\int_{t\in[a-h,a+h]}\int_{v\in I}\mathcal D_{t,h}(v)\,dv\,dt\right|
\le \int_{t\in[a-h,a+h]}\int_{v\in I}|\mathcal D_{t,h}(v)|\,|dv|\,dt.
\]
Thus
\[
\le (2h)\,|I|\,\sup_{\substack{t\in[a-h,a+h]\\ v\in I}}|\mathcal D_{t,h}(v)|
\le (2h)\,(C_{\rm geom}\delta)\,\sup_{\substack{t\in[a-h,a+h]\\ v\in\partial B_{\kappa/2}}}|\mathcal D_{t,h}(v)|.
\]

Next, since \(\mathcal D_{t,h}=\mathcal L_{t+h}-\mathcal L_{t-h}\),
\[
|\mathcal D_{t,h}(v)|\le |\mathcal L_{t+h}(v)|+|\mathcal L_{t-h}(v)|.
\]
For any \(s\) in the range \([a-2h,a+2h]\),
\[
|\mathcal L_s(v)|
=\left|\frac{E'}{E}(v+s)-\frac{E'}{E}(v-s)\right|
\le \left|\frac{E'}{E}(v+s)\right|+\left|\frac{E'}{E}(v-s)\right|.
\]
Therefore
\[
\sup_{t,v}|\mathcal D_{t,h}(v)|\ \le\ 
2\sup_{\substack{s\in[a-2h,a+2h]\\ v\in\partial B_{\kappa/2}}}
\left(\left|\frac{E'}{E}(v+s)\right|+\left|\frac{E'}{E}(v-s)\right|\right).
\]
Using the residual/local split \(E'/E=F'/F+Z'_{\rm loc}/Z_{\rm loc}\) and the residual bound gives the displayed estimate.

Finally, for the local term:
\[
\left|\frac{Z'_{\rm loc}}{Z_{\rm loc}}(w)\right|=\left|\sum_{\rho\in Z_{\rm loc}}\frac{1}{w-\rho}\right|
\le \sum_{\rho\in Z_{\rm loc}}\frac{1}{|w-\rho|}
\le \frac{2N_{\rm loc}(m)}{a}
\]
under the separation hypothesis \(|w-\rho|\ge a/2\) for all relevant \(w=v\pm t\).  □

---

### \(\pi/2\) clearance at nominal coupling

Adopt the nominal scale (as in v40)  
\[
\delta=\delta_0(m,a)=\eta\,\frac{a}{(\log m)^2},
\]
and choose \(h=\delta\) (one natural coupling; any \(h\ll 1\) works even better on the UE side).

Then, using \(a\le 1\),
\[
\Phi^{\rm 2D}_B(a;\delta)
\ \le\ 
8\,C_{\rm geom}\,\eta^2\,\frac{a^2 '}{(\log m)^4}
\left(
C_{\rm res,1}\log m+C_{\rm res,2}+\frac{4\,N_{\rm loc}(m)}{a}
\right)
\ \ll\
\frac{1}{(\log m)^3}
\]
(using \(N_{\rm loc}(m)\ll \log m\)).  

A completely explicit sufficient condition for strict clearance is:
\[
\log m\ \ge\ 
\left(\frac{16\,C_{\rm geom}\,\eta^2\,(C_{\rm res,1}+4C_{\rm loc})}{\pi}\right)^{1/3},
\]
where \(C_{\rm loc}\) is any constant such that \(N_{\rm loc}(m)\le C_{\rm loc}\log m\) for \(m\ge 10\). Under this condition,
\[
\Phi^{\rm 2D}_B(a;\delta)\ <\ \frac{\pi}{2}.
\]

(Referee note: the purpose here is the **scaling** and **δ‑uniformity**; the exact numeric \(m_0\) depends on the constants ledger values.)

---

## (4) Where the win comes from (one precise sentence)

**The gain is the extra small factor \(h\) from non‑pointwise averaging in the tilt parameter \(a\):** the endpoint scales like an **area** \(\delta\cdot h\) rather than a **length** \(\delta\), while the integrand size remains at most polylogarithmic in \(m\) away from the local poles.

*Single bottleneck term:* obtaining a δ‑uniform bound for \(\sup |F'/F|\) (constants‑ledger residual envelope) and ensuring the evaluation collar stays a fixed distance from the local zeros in the relevant shifted sets \(v\pm t\).

---

## (5) Interaction with NG‑\((\Delta a)\)‑A and NG‑\((\Delta a)\)‑A consistency

- NG‑Δa‑A proves that **pointwise‑in‑\(a\)** forcing for the Δa endpoint on aligned boxes is impossible at nominal coupling. 【968:1†integration_notes_v41_prebuild.md†L22-L45】  
- The present endpoint \(\Phi^{\rm 2D}_B\) is **even more shrinkable** on those geometries, since it introduces an additional \(a\)-integration. Therefore there is **no contradiction** with NG‑Δa‑A; instead it sharpens the lesson:
  - endpoints that remain a distance \(\asymp a\) away from the quartet poles will be δ‑small (hence **cannot** be topologically forced),
  - any future forcing mechanism for a 2D endpoint must lower‑bound a **nontrivial \(a\)-mass** of phase response, not a single “micro‑step” \(a\)-witness.
- **Not “micro‑step forcing”:** we do not claim that taking \(h\to 0\) creates forcing; indeed, if forcing holds only for a single \(a\)-value, the \(a\)-average could wash it out. Any forcing lemma for \(\Phi^{\rm 2D}\) must show persistence over an \(a\)-interval of length \(\asymp h\), or else the endpoint must be changed (e.g. replace the \(a\)-integral by an \(a\)-max).

---

## (6) S6 harness (explicit‑formula mapping)

**Frame map:** \(u=2s\), \(v=u-1\), so \(s=(1+v)/2\). An off‑critical‑line zero \(\rho=\beta+i\gamma\) corresponds to  
\[
v_\rho=(2\beta-1)+i\,2\gamma = a + i m,\quad a=2\beta-1,\quad m=2\gamma.
\]

**Explicit‑formula interpretation:** the zero term in explicit formula has magnitude \(x^\beta\); in terms of \(a\), \(\beta=\tfrac12+\tfrac a2\), so any \(a>0\) corresponds to an amplitude leak at scale \(x^{1/2+a/2}\).  

The present endpoint is an **\(a\)-sensitivity functional**: it integrates a finite difference (in \(a\)) of the boundary log‑derivative phase response. If an off‑axis quartet created a *persistent* (in \(a\)) boundary phase signal, that would be a boundary‑side witness of an amplitude leak. This note does **not** claim such persistence (that is the forcing half / OPEN‑GEO forcing obligation).

---

## Patch Packet (optional; for v41 queue)

**Callsign:** RH-ENVELOPE  
**Result classification:** **CONDITIONAL** (UE half proved for the 2D‑averaged endpoint; forceability on any witness family remains to be proven by FORCE).  
**Target gap(s) closed:** UE‑half candidate for **OPEN‑GEO** (GEO‑C3 direction).  
**Still open:** forceability of \(\Phi^{\rm 2D}\) (or a domination link to a forced endpoint); resonance robustness if forcing persists only on small \(a\)-sets.  
**Key conclusions (≤5):**
1. A 2D “\(a\)-window × boundary” endpoint yields a provable δ‑uniform UE scaling \(\Phi^{\rm 2D}\ll \delta h\,\mathrm{polylog}(m)\), clearing \(\pi/2\) at nominal \(\delta=\eta a/\log^2 m\) (with \(h=\delta\)).  
2. The win is geometric: **area factor \(\delta h\)** replaces length factor \(\delta\), without forbidden endpoint swaps.  
3. This is consistent with NG‑Δa‑A; it does not “evade” that NO‑GO, it formalizes why pointwise‑in‑\(a\) forcing dies on separated geometries.  
4. Any forcing lemma must lower‑bound \(a\)-averaged response (not a single \(a\) witness), else the average endpoint will wash out forcing.  
5. Residual constants must remain δ‑uniform; all δ‑dependence is explicit in \(\delta h\).

**Paste‑ready TeX blocks (defs/lemmas):**

```tex
\begin{definition}[2D averaged $\Delta a$ endpoint on a $\kappa$--admissible box]
Fix $\kappa\in(0,1/10)$. Let $B=B(a,m,\delta)$ be a $\kappa$--admissible box with buffered contour $\partial B_{\kappa/2}$.
For $h\in(0,a/4]$ define the $a$--window $\mathcal I_a(h)=[a-h,a+h]$ and set
\[
\Phi^{\rm 2D}_B(a;h)
:=\max_{I\in{\rm Sides}(\partial B_{\kappa/2})}
\left|
\Im\int_{t\in\mathcal I_a(h)}\int_{v\in I}\mathcal D_{t,h}(v)\,dv\,dt
\right|.
\]
\end{definition}
```

```tex
\begin{lemma}[2D averaged $\Delta a$ upper envelope]
\label{lem:2D-deltaa-UE}
Fix $\kappa\in(0,1/10)$. Let $m\ge 10$, $a\in(0,1]$, and $0<\delta,h\le a/4$.
Let $B=B(a,m,\delta)$ be $\kappa$--admissible.
Assume $\mathcal D_{t,h}$ is holomorphic on a neighborhood of $\partial B_{\kappa/2}$ for all $t\in[a-2h,a+2h]$.
Assume the residual/local split $E'/E=F'/F+Z'_{\rm loc}/Z_{\rm loc}$ and the residual envelope bound
$\sup_{\mathcal N(\partial B_{\kappa/2})}|F'/F|\le C_{\rm res,1}\log m+C_{\rm res,2}$.
Then
\[
\Phi^{\rm 2D}_B(a;h)
\le 8C_{\rm geom}\,\delta h\left(
C_{\rm res,1}\log m+C_{\rm res,2}
+\sup_{t,v}\left|\frac{Z'_{\rm loc}}{Z_{\rm loc}}(v+t)\right|
+\sup_{t,v}\left|\frac{Z'_{\rm loc}}{Z_{\rm loc}}(v-t)\right|
\right),
\]
where the suprema are over $t\in[a-2h,a+2h]$ and $v\in\partial B_{\kappa/2}$, and $C_{\rm geom}$ is a rectangle-shape constant.
If additionally all local zeros are at distance $\ge a/2$ from the shifted collar sets $v\pm t$, then
\[
\Phi^{\rm 2D}_B(a;h)
\le 8C_{\rm geom}\,\delta h\left(
C_{\rm res,1}\log m+C_{\rm res,2}+\frac{4N_{\rm loc}(m)}{a}
\right).
\]
\end{lemma}
```

**Dependencies on other branches:**
- **FORCE:** must produce a forcing lemma for \(\Phi^{\rm 2D}\) (or a domination link from a forced endpoint) on an admissible witness family; NG‑Δa‑A blocks pointwise aligned‑box forcing.  
- **LOCAL:** if the forcing geometry brings shifted evaluation points near poles, must quantify local contributions in the same 2D endpoint class.

**Referee risk notes:**
- The holomorphy collar hypothesis must be stated explicitly to avoid hidden RH‑equivalents (“no zeros on boundary”).  
- The “geometric separation” condition is the critical point: if forcing requires the shifts \(v\pm t\) to approach quartet points at distance \(\asymp\delta\), the \(a/2\) separation bound fails and the local term becomes δ‑inert again.  
- This UE package is therefore a *candidate* for OPEN‑GEO only if FORCE can prove forcing with the same separation (or an alternative local estimate that remains gate‑passing).
