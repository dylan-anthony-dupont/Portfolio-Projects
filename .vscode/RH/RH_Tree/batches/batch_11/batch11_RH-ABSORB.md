# Batch 11 — RH-ABSORB  
**Mechanism selection (hard constraint): (C) non-pointwise UE**  

This response is scoped to the **geometry pivot v40→v41**: ensure the new defect/Δa endpoint class is *globally consistent* (admissibility, buffering, and a usable “phase→envelope” absorption lemma) without importing RH-equivalent assumptions.

Key anchors (v40): defect primitives `(\mathcal Q_a,\mathcal L_a)`, two-sided shift-difference `\mathcal D_{a,h}`, and phase endpoints `\Phi_B^{\rm def}` and `\Phi_B^{(2s)}` are in Definitions 12.1–12.5. `\Phi_B^{(2s)}` uses the nominal coupling `h=\delta=\delta_0(m,a):=\eta a/(\log m)^2`.【938:9†manuscript_v40.pdf†L1-L38】【938:7†manuscript_v40.pdf†L46-L83】  
Key anchors (v41 prebuild): aligned-box Δa forcing is **NO–GO** (NG-Δa-A), so the witness family/coupling must change; candidate geometry directions GEO-C1/2/3 are enumerated.【938:14†integration_notes_v41_prebuild.md†L20-L39】【938:12†integration_notes_v41_prebuild.md†L1-L11】

---

## (1) Admissibility + buffering policy for the new geometry

### 1.1. What *must* be true for the integrals to make sense (baseline)

In v40, the defect log-derivative is defined by  
\[
\mathcal L_a(v)=(\log \mathcal Q_a)'(v)=\frac{E'}{E}(v+a)-\frac{E'}{E}(v-a),
\]
whenever the expressions are defined, and is holomorphic on any domain where \(E(v\pm a)\neq 0\).【938:9†manuscript_v40.pdf†L1-L16】  
The corresponding defect phase endpoint is  
\[
\Phi_B^{\rm def}(a):=\max_{I\in \mathrm{Sides}(\partial B_{\kappa/2})}\left|\Im\int_I \mathcal L_a(v)\,dv\right|,
\]
with \(\partial B_{\kappa/2}\) the buffered contour (Definition 12.36).【938:9†manuscript_v40.pdf†L17-L38】【923:7†manuscript_v40.pdf†L60-L90】

Similarly, the **two-sided shift-difference** operator is defined by  
\[
\mathcal D_{a,h}(v):=\mathcal L_{a+h}(v)-\mathcal L_{a-h}(v),
\]
and the two-sided phase endpoint by  
\[
\Phi_B^{(2s)}(a;h):=\max_{I\in \mathrm{Sides}(\partial B_{\kappa/2})}\left|\Im\int_I \mathcal D_{a,h}(v)\,dv\right| .
\]【938:9†manuscript_v40.pdf†L94-L107】【938:7†manuscript_v40.pdf†L60-L83】

**Important hygiene (v41 Patch 1):** the displayed “equivalently” expansion of \(\mathcal D_{a,h}\) in v40 is sign-inconsistent; v41 prebuild explicitly fixes it to match \(\mathcal D_{a,h}=\mathcal L_{a+h}-\mathcal L_{a-h}\).【938:0†v41_patch_queue.md†L8-L26】  
Hence throughout this batch, the *correct* expansion is:
\[
\boxed{
\mathcal D_{a,h}(v)
=
\frac{E'}{E}(v+a+h)-\frac{E'}{E}(v-a-h)
-\frac{E'}{E}(v+a-h)+\frac{E'}{E}(v-a+h).
}
\tag{D-correct}
\]【938:0†v41_patch_queue.md†L20-L26】

### 1.2. κ-admissibility and buffering (already in the spine)

v40 already has the core admissibility construct:

- **κ-admissible box** \(B=B(\alpha,m,\delta)\): defined so that \(E\) has no zeros on \(\partial B\) and the distance from each boundary point to the zero set is \(\ge \kappa\delta\).【923:2†manuscript_v40.pdf†L4-L24】
- **Shrink existence**: given any aligned box \(B(\alpha,m,\delta)\), there exists a \(\delta'\in[\delta/2,\delta]\) such that \(B(\alpha,m,\delta')\) is κ-admissible (Lemma 10.6).【923:2†manuscript_v40.pdf†L25-L46】
- **Buffered contour** \(\partial B_{\kappa/2}\): the inset rectangle used for phase endpoints and “buffered boundary” phase functionals (Definition 12.36).【923:7†manuscript_v40.pdf†L60-L90】

These three items are the *non-circular* way to ensure the boundary integrals are legitimate without “knowing where zeros are”: you shrink δ until the contour misses the discrete zero set, while keeping the box geometry and the intended interior content stable.

### 1.3. What changes under the Δa/defect endpoint class (new requirement)

The defect endpoints do **not** only depend on \(E\) on \(\partial B_{\kappa/2}\); they depend on **shifted evaluations** \(v\mapsto v\pm(a\pm h)\). Therefore κ-admissibility for \(E\) alone is insufficient: we need *shifted admissibility*.

#### Definition (shifted κ-admissibility for the defect/Δa geometry)

Let \(B=B(\alpha,m,\delta)\) be a rectangle in the \(v\)-plane, and fix \(\kappa\in(0,1/10)\). Define the evaluation set
\[
\Sigma(B;a,h)
:=\left\{\,v+\sigma a+\tau h \;:\; v\in \partial B_{\kappa/2},\ \sigma,\tau\in\{\pm1\}\right\}.
\]

We say \(B\) is **\((\kappa;a,h)\)-admissible for \(\mathcal D_{a,h}\)** if:

1. \(B\) is κ-admissible for \(E\) in the original sense (so \(\partial B_{\kappa/2}\) itself misses zeros with buffer), and  
2. \(E\) has **no zeros on \(\Sigma(B;a,h)\)**, and moreover
\[
\mathrm{dist}\big(\Sigma(B;a,h),\,Z(E)\big)\ \ge\ \kappa\delta.
\tag{SA}
\]

This condition implies each map \(v\mapsto (E'/E)(v+\sigma a+\tau h)\) is holomorphic on an open neighborhood of \(\partial B_{\kappa/2}\); hence \(\mathcal L_{a\pm h}\) and \(\mathcal D_{a,h}\) are holomorphic there, and every line integral defining \(\Phi_B^{\rm def}\) and \(\Phi_B^{(2s)}\) is well-defined.

#### (v,a)-space admissibility (needed if GEO‑C3 is used)

If the geometry is upgraded to a 2D “\((a,v)\)-rectangle” (GEO‑C3), one must strengthen (SA) uniformly in the \(a\)-interval. Concretely, if \(a\) ranges over an interval \(J=[a_-,a_+]\), the analogue is:
\[
\mathrm{dist}\Big(\big\{v\pm t: v\in\partial B_{\kappa/2},\ t\in J\big\},\,Z(E)\Big)\ \ge\ \kappa\delta.
\tag{SA-2D}
\]
This is the minimal admissibility condition that permits: (i) differentiating in \(a\), (ii) swapping \(a\)- and \(v\)-integrals, and (iii) controlling any “flux/winding” endpoint built from \(\partial_v \log \mathcal Q_a\).

### 1.4. Why this is compatible with “local cancellation” (no hidden assumptions)

v40’s Lemma 12.6 shows that if an off-axis quartet \(\pm a\pm i m\) exists and \(B=B(0,m,\delta)\) with \(\delta\le a/4\), then \(\mathcal Q_a\) has a removable singularity at \(v=i m\) and \(\mathcal L_a\) is holomorphic on \(B_{\kappa/2}\).【938:7†manuscript_v40.pdf†L83-L114】  

This is a *local interior* regularity statement (removable singularity at \(v=i m\)). It does **not** remove the need for boundary admissibility (SA) or (SA‑2D): poles on the *boundary* still invalidate \(\log\) branches and phase integrals. Thus, for global consistency we must explicitly impose (SA)/(SA‑2D) as a hypothesis whenever \(\Phi_B^{\rm def}\) or \(\Phi_B^{(2s)}\) is used.

---

## (2) Absorption lemma (the one we’ll actually use) — phase endpoint → envelope‑controllable quantity

### 2.1. Why we need a non‑pointwise absorption lemma

v40 already proves a “side-length ceiling”: any bound obtained solely from a pointwise control \(\sup_{\partial B_{\kappa/2}}|\mathcal L_a|\) can never beat \(p=1\) in a δ‑gain, because \(|I|\asymp \delta\).【938:9†manuscript_v40.pdf†L39-L57】  

This is exactly why this batch commits to mechanism **(C) non‑pointwise UE**: the endpoint must be bounded by a quantity that can plausibly enjoy cancellation and δ‑gain, not merely by a supremum times side length.

### 2.2. Define the “L¹ envelope endpoint” attached to \(\mathcal D_{a,h}\)

For any \((\kappa;a,h)\)-admissible box \(B\), define
\[
\Psi_B^{(2s)}(a;h)\ :=\ \int_{\partial B_{\kappa/2}} |\mathcal D_{a,h}(v)|\,|dv|.
\tag{Psi-2s}
\]
Likewise, for defect endpoints,
\[
\Psi_B^{\rm def}(a)\ :=\ \int_{\partial B_{\kappa/2}} |\mathcal L_a(v)|\,|dv|.
\tag{Psi-def}
\]
These are the *minimal* non-pointwise objects an envelope branch can target without invoking the banned absolute \(L^r\) endpoint class on \(|E'/E|\) itself (v36 NO‑GO).【945:0†v36_patchlog.md†L21-L27】

### 2.3. Lemma (phase absorption for \(\Phi_B^{(2s)}\) into \(\Psi_B^{(2s)}\)) — full proof

**Lemma (Absorption inequality for the Δa phase endpoint).**  
Fix \(\kappa\in(0,1/10)\). Let \(B=B(\alpha,m,\delta)\) be \((\kappa;a,h)\)-admissible for \(\mathcal D_{a,h}\) (Definition (SA)), so \(\mathcal D_{a,h}\) is holomorphic on an open neighborhood of \(\partial B_{\kappa/2}\). Then
\[
\boxed{
\Phi_B^{(2s)}(a;h)\ \le\ \Psi_B^{(2s)}(a;h)
\ =\ \int_{\partial B_{\kappa/2}} |\mathcal D_{a,h}(v)|\,|dv|.
}
\tag{Absorb-2s}
\]

*Proof (line-by-line).*  

1. By definition,
   \[
   \Phi_B^{(2s)}(a;h)=\max_{I\in \mathrm{Sides}(\partial B_{\kappa/2})}\left|\Im\int_I \mathcal D_{a,h}(v)\,dv\right|.
   \]
   (This is exactly Definition 12.5.)【938:7†manuscript_v40.pdf†L60-L83】

2. For any complex number \(z\), \(|\Im z|\le |z|\). Hence for each side \(I\),
   \[
   \left|\Im\int_I \mathcal D_{a,h}(v)\,dv\right|
   \ \le\
   \left|\int_I \mathcal D_{a,h}(v)\,dv\right|.
   \]

3. Parametrize the (rectifiable) side \(I\) by a \(C^1\) map \(\gamma:[0,1]\to I\). Then
   \[
   \int_I \mathcal D_{a,h}(v)\,dv
   \ =\
   \int_0^1 \mathcal D_{a,h}(\gamma(t))\,\gamma'(t)\,dt.
   \]

4. Apply the triangle inequality for integrals:
   \[
   \left|\int_0^1 \mathcal D_{a,h}(\gamma(t))\,\gamma'(t)\,dt\right|
   \ \le\
   \int_0^1 \left|\mathcal D_{a,h}(\gamma(t))\right|\cdot\left|\gamma'(t)\right|\,dt.
   \]

5. The right-hand side is precisely \(\int_I |\mathcal D_{a,h}(v)|\,|dv|\). Therefore
   \[
   \left|\Im\int_I \mathcal D_{a,h}(v)\,dv\right|
   \ \le\
   \int_I |\mathcal D_{a,h}(v)|\,|dv|.
   \]

6. Taking the maximum over the four sides \(I\) yields
   \[
   \Phi_B^{(2s)}(a;h)
   \ \le\
   \max_{I}\int_I |\mathcal D_{a,h}(v)|\,|dv|
   \ \le\
   \sum_{I}\int_I |\mathcal D_{a,h}(v)|\,|dv|
   \ =\
   \int_{\partial B_{\kappa/2}} |\mathcal D_{a,h}(v)|\,|dv|.
   \]
   This equals \(\Psi_B^{(2s)}(a;h)\) by definition, proving (Absorb‑2s). ∎

### 2.4. Why this lemma is the *correct* interface for the closure chain

- It **does not** “win locally but lose globally”: it requires only boundary holomorphicity (guaranteed by (SA)/(SA‑2D)), and it outputs a boundary integral object \(\Psi\) that is stable under κ-admissible δ-shrinking.
- It avoids the known NO‑GO: bounding \(\Phi\) by \(\int |E'/E|\) on a contour that encloses a zero is δ‑inert (scale-invariant pole contribution).【938:14†integration_notes_v41_prebuild.md†L1-L3】  
  By contrast, \(\Psi_B^{(2s)}\) integrates \(|\mathcal D_{a,h}|\), which is a **difference of shifts** and is precisely the object where cancellation (and thus δ‑gain) is plausible.

(Any further reduction of \(\Psi_B^{(2s)}\) to \(\int|E'/E|\) is optional and, in general, risks reintroducing δ‑inert pole terms.)

---

## (3) Non-circularity audit (where RH could leak in, and why the above does not)

Below are the main RH-smuggling failure modes relevant to this batch, and how the admissibility + absorption lemma avoids them.

1. **“Height tied to Re(v)=0” definitions.**  
   Not used. All parameters are in the v-frame with \(a=2\beta-1\), \(m=2\gamma\); the lemmas above treat \(a,m\) as free real parameters, not assuming \(\beta=1/2\).

2. **Assuming zero-free boundaries without justification.**  
   Avoided by explicitly requiring κ-admissibility and invoking the existing shrink lemma (Lemma 10.6) to guarantee existence of a nearby δ′ with a zero-free boundary. This is a topological/analytic fact (discreteness of zeros), not an RH-equivalent assumption.【923:2†manuscript_v40.pdf†L25-L46】

3. **Assuming “one zero per height” or sharp \(N(T)\).**  
   Not used. Neither (SA) nor Lemma (Absorb‑2s) requires any counting information.

4. **Assuming the defect quotient is globally holomorphic because cancellation occurs at the *center*.**  
   Explicitly avoided: Lemma 12.6 grants local holomorphicity near \(v=i m\) under a quartet, but our definitions require **boundary** holomorphicity via (SA)/(SA‑2D).【938:7†manuscript_v40.pdf†L83-L114】

5. **Hidden use of the argument principle to conclude “phase must be π/2”.**  
   Not invoked here. The absorption lemma is a pure inequality for contour integrals; forcing is delegated to the FORCE branch and must respect NG‑Δa‑A.

Net: the only analytic inputs are (i) κ-admissibility existence via δ-shrink, and (ii) triangle inequalities. No RH-equivalent statements enter.

---

## (4) Interaction with NG-(Δa)-A (aligned-box forcing NO‑GO)

v41 prebuild locks the key obstruction:

- On aligned boxes \(B(a,m,\delta)\) with \(h\le \delta\le a/4\), the toy quartet model yields  
  \(\Phi^{(2s)}_{B(a,m,\delta)}(a;h)\le C\,\delta h/a^2\), hence at nominal coupling \(h=\delta=\eta a/(\log m)^2\) the endpoint \(\to 0\). Therefore v40’s forcing bullet for \(\Phi^{(2s)}\) cannot hold on aligned boxes.【938:0†v41_patch_queue.md†L34-L53】【938:6†v41_next_build_plan_diff.md†L20-L28】

**Compliance statement (this batch):**

- The absorption lemma (Absorb‑2s) is **forcing‑agnostic**: it never assumes \(\Phi^{(2s)}\) has a positive lower bound; it only upper-bounds it by \(\Psi^{(2s)}\).
- Therefore, it does not violate NG‑Δa‑A. Instead, it clarifies what any *new* geometry/coupling must provide:

  1) **FORCE obligation:** produce a witness family \(\mathfrak B(m,a,\delta,h)\) and an endpoint (possibly \(\Phi^{(2s)}\) on a non-aligned family) that is *forceable* (δ‑independent lower bound) — but not by the aligned-box mechanism ruled out by NG‑Δa‑A.【938:14†integration_notes_v41_prebuild.md†L20-L39】

  2) **ENVELOPE/LOCAL obligation:** bound \(\Psi_B^{(2s)}(a;h)\) (or a close variant that retains cancellation) with δ‑gain and resonance robustness on the *same* witness family.

If v41 chooses GEO‑C1 (hinge-centered \(B(0,m,\delta)\)), note that admissibility must be stated carefully “so shifted evaluations do not land on zeros.”【938:12†integration_notes_v41_prebuild.md†L7-L10】

---

## (5) S6 harness (explicit-formula amplitude-leak check)

An off-critical-line zero \(\rho=\beta+i\gamma\) corresponds in v-frame to \(v_\rho=a+i m\) with  
\[
a=2\beta-1,\qquad m=2\gamma.
\]
Thus excluding **all** \(a>0\) quartets is equivalent to excluding all \(\beta>1/2\) zeros.

**Amplitude-leak interpretation:** a \(\beta>1/2\) zero contributes a term of size \(\asymp x^\beta\) to explicit-formula oscillations (e.g. in \(\psi(x)-x\)), i.e. an “amplitude leak” beyond the \(x^{1/2+\varepsilon}\) regime. A closure theorem that rules out \(a>0\) via a forceable contradiction therefore rules out such \(x^{1/2+a/2}\) leaks (since \(\beta=(1+a)/2\)).  

This batch’s lemma does **not** itself produce an explicit formula bound; it only provides the analytic inequality interface needed so that a future “forceable endpoint \(\Rightarrow\) contradiction” chain (if completed) can be interpreted as forbidding \(\beta>1/2\) contributions.

---

## PATCH PACKET (v41 insertion-ready)

* Callsign: RH-ABSORB  
* Result classification: **CONDITIONAL**  
  (Absorption/consistency lemmas are proof-grade; overall closure remains conditional on FORCE/ENVELOPE producing a forceable witness family with a δ-gain bound for \(\Psi^{(2s)}\).)
* Target gaps closed (by ID):  
  - **Inner/outer consistency hazard for new endpoint** (well-definedness + phase→envelope bridge).  
  - **Definition hygiene**: adopts the v41-correct expansion (Patch 1).
* Target gaps still open (by ID):  
  - **OPEN‑GEO** (geometry/coupling redesign to replace aligned boxes)【938:6†v41_next_build_plan_diff.md†L46-L54】  
  - **Forceability** for the new geometry (FORCE branch)  
  - **δ‑gain UE/control** for \(\Psi^{(2s)}\) (ENVELOPE/LOCAL branches)

* Key conclusions (≤5 bullets):
  1. Defect/Δa phase endpoints require **shifted κ-admissibility** (SA)/(SA‑2D), not just κ-admissibility of \(E\).  
  2. The correct “absorption” interface is \(\Phi^{(2s)}\le \Psi^{(2s)}:=\int_{\partial B_{\kappa/2}}|\mathcal D_{a,h}|\,|dv|\), not \(\int|E'/E|\) (δ‑inert NO‑GO).  
  3. The absorption lemma is **forcing-agnostic** and thus compatible with NG‑Δa‑A.  
  4. Any viable v41+ closure must target δ‑gain control of \(\Psi^{(2s)}\) on a witness family not killed by NG‑Δa‑A.  
  5. The endpoint chain, if closed, corresponds to forbidding explicit-formula \(x^{1/2+a/2}\) amplitude leaks (i.e. \(\beta>1/2\)).

* Paste-ready manuscript edits:

  (i) **New definition (shifted admissibility; insert near Def. `def:two-sided-endpoint`)**
  ```tex
  \begin{definition}[(\(\kappa;a,h\))-admissibility for the \(\Delta a\) endpoint]
  \label{def:shifted-admissible}
  Fix \(\kappa\in(0,1/10)\) and let \(B=B(\alpha,m,\delta)\) be a rectangle with buffered contour
  \(\partial B_{\kappa/2}\) (Definition~\ref{def:buffered-boundary-endpoint}).
  For parameters \(a>0\), \(h>0\), define the evaluation set
  \[
    \Sigma(B;a,h):=\{\,v+\sigma a+\tau h:\ v\in\partial B_{\kappa/2},\ \sigma,\tau\in\{\pm1\}\,\}.
  \]
  We say \(B\) is \((\kappa;a,h)\)-admissible for \(\mathcal D_{a,h}\) if \(B\) is \(\kappa\)-admissible for \(E\)
  and
  \[
    \dist(\Sigma(B;a,h),Z(E))\ge \kappa\delta.
  \]
  \end{definition}
  ```

  (ii) **New lemma (absorption inequality; insert after Def. `def:two-sided-endpoint`)**
  ```tex
  \begin{lemma}[Phase absorption for the \(\Delta a\) endpoint]
  \label{lem:deltaa-absorb}
  Fix \(\kappa\in(0,1/10)\). If \(B=B(\alpha,m,\delta)\) is \((\kappa;a,h)\)-admissible
  (Definition~\ref{def:shifted-admissible}), then
  \[
    \Phi_B^{(2\mathrm{s})}(a;h)
    \le
    \int_{\partial B_{\kappa/2}} |\mathcal D_{a,h}(v)|\,|dv|.
  \]
  \end{lemma}
  \begin{proof}
  For each side \(I\) of \(\partial B_{\kappa/2}\),
  \(|\Im\int_I \mathcal D_{a,h} dv|\le |\int_I \mathcal D_{a,h} dv|
  \le \int_I |\mathcal D_{a,h}|\,|dv|\). Taking the maximum over sides and
  summing the four side integrals yields the claim.
  \end{proof}
  ```

  (iii) **Remark (NO‑GO scope; keep explicit)**
  ```tex
  \begin{remark}[Why \(\int|E'/E|\) is not a \(\delta\)-shrinking closure endpoint]
  On a contour enclosing a zero of \(E\), the per-pole contribution to \(\int|E'/E|\) is scale-invariant,
  hence \(\delta\)-inert. Therefore upper-bounding a phase endpoint by \(\int|E'/E|\) cannot yield
  \(\delta\)-gain closure. Any viable \(\Delta a\) strategy must instead bound a cancellation-bearing
  object such as \(\int |\mathcal D_{a,h}|\).
  \end{remark}
  ```

* Dependencies on other branches:
  - **RH-FORCE:** must supply forceability on the new witness family (not aligned boxes) and respect NG‑Δa‑A.  
  - **RH-ENVELOPE / RH-LOCAL:** must bound \(\int_{\partial B_{\kappa/2}}|\mathcal D_{a,h}|\) with δ‑gain and resonance robustness on the same family.  
  - **RH-BRIDGE:** any transfer from \(D_B(W)\) to the new defect endpoint must preserve κ-admissibility hypotheses.

* Referee risk notes (anticipated objections + how addressed):
  - **“Your integrals assume \(E\neq 0\) on shifted contours; is that circular?”**  
    Addressed by explicitly using κ-admissibility + δ-shrink existence (Lemma 10.6) and by stating shifted admissibility as a hypothesis, not a conclusion.
  - **“You reduced the endpoint to an absolute integral; doesn’t that kill δ-gain?”**  
    Not necessarily, because the integrand is \(\mathcal D_{a,h}\) (difference of shifts) where cancellation may occur; we explicitly warn that reducing further to \(\int|E'/E|\) reintroduces δ‑inert pole terms (NO‑GO).
  - **“Does this violate NG‑Δa‑A?”**  
    No: the lemma is an upper bound only and is compatible with the aligned-box forcing NO‑GO.
