# Batch 15 — RH‑LOCAL
*(Local geometry + admissibility + resonance: checkability of UE‑INPUT)*

This note stress‑tests the **local geometry conditions** (shift‑admissibility, buffering, resonance) against the v43/v44 UE interface, and against the proposed *signed* k=2 replacement.

The goal is not to re‑derive forcing (GEO‑C4 is frozen), but to make the **UE‑INPUT interface proof‑grade and audit‑stable**, especially under **δ‑shrink** and **near‑resonant quartets**.

---

## 0) Notation recap (only what’s needed locally)

- Hinge circle: \(v(\theta)= i m+\delta e^{i\theta}\), \(\theta\in[0,2\pi]\).
- Coupling: \(h=\kappa\delta\) with fixed \(\kappa\in(0,1)\).
- Log‑derivative difference: \(\mathcal L_t(v)=\frac{E'}{E}(v+t)-\frac{E'}{E}(v-t)\).
- Double‑shift field: \(\mathcal D_{a,h}(v)=\mathcal L_{a+h}(v)-\mathcal L_{a-h}(v)\).
- Endpoint: \(\Phi^\star=(\delta^2/h)\,\|P_2(\Im \mathcal D_{a,h}(v(\theta)))\|_{L^2_\theta}\) (locked GEO‑C4).

v43 UE‑INPUT (single open box) is the absolute‑value \(L^1\) bound
\[
\int_0^{2\pi}|\mathcal D_{a,h}(v(\theta))|\,d\theta\ \le\ C\,h\,\frac{(\log(m+3))^{C'}}{a^2},
\]
with \(\delta\le\delta_0=\eta a/(\log(m+3))^2\) and allowing smaller \(\delta\) for buffering【1049:5†integration_notes_v44_prebuild_pre_batch15.md†L8-L13】.

An inactive candidate replacement is the signed k=2 channel bound
\[
\Big|\int_0^{2\pi}\mathcal D_{a,h}(v(\theta))\,e^{-2i\theta}\,d\theta\Big|\ \le\ C\,h\,\frac{(\log(m+3))^{C'}}{a^2},
\]
which preserves phase【1049:5†integration_notes_v44_prebuild_pre_batch15.md†L24-L27】.

---

## 1) Local dependency map: where shift‑admissibility is used

### 1.1 Definitions (local geometry gate)

v43 defines **shift‑admissible** for the hinge circle at \((a,h)\) as the nonvanishing of \(E\) along the four shifted traces \(v(\theta)\pm(a\pm h)\), and **buf‑admissible** as a *distance* condition \(\mathrm{dist}(\cdot,\mathcal Z(E))\ge \mathrm{buf}\cdot \delta\) along those traces【1045:7†manuscript_v43.pdf†L46-L67】.

This is the only “local geometry” hypothesis needed to even *state* the UE and forcing claims, since \(\mathcal D_{a,h}\) is built from \(E'/E\) evaluated at those traces.

### 1.2 Where it enters FORCE (locked chain)

- **Toy forcing** identifies the k=2 harmonic in the pure singular model \(\mathcal D_{\mathrm{sing}}\) (poles at \(u=\pm h\) in the \(u\)-disk), giving explicit \(k=2\) coefficients and a lower bound for \(\Phi^\star\)【1045:11†manuscript_v43.pdf†L1-L28】.
- **Stability forcing** (hinge forcing is stable) says: if \(C_{m,\delta}\) is buf‑admissible at \((a,h)\), then the true endpoint is close to the singular endpoint:
  \(\Phi^\star=\Phi^\star_{\mathrm{sing}}+O(\delta)\), hence \(\Phi^\star\ge 2\sqrt\pi\) for \(\delta\) small enough【1045:1†manuscript_v43.pdf†L46-L92】.
  The proof uses buf‑admissibility to ensure all non‑quartet contributions are holomorphic near the hinge disk, so the remainder \(\mathcal R\) is bounded and becomes \(O(\delta)\) after the \(\delta^2/h\) normalization【1045:14†manuscript_v43.pdf†L6-L12】.

**Local take:** shrinking \(\delta\) (while preserving admissibility) makes forcing *easier*, because the analytic remainder contribution \(O(\delta)\) improves.

### 1.3 Where it enters UE‑REDUCE and UE‑INPUT

- UE‑REDUCE (v43) uses only the inequality \(\|P_2 f\|_{L^2}\le (1/\sqrt\pi)\|f\|_{L^1}\) to bound \(\Phi^\star\) in terms of \((\delta^2/h)\int|\mathcal D|\)【1045:8†manuscript_v43.pdf†L2-L25】.
- UE‑INPUT itself requires **shift‑admissibility / buf‑admissibility** so that \(\mathcal D_{a,h}(v(\theta))\) is well‑defined on the integration contour (and the “allow smaller \(\delta\)” clause is meaningful)【1045:10†manuscript_v43.pdf†L1-L35】.

### 1.4 δ‑shrink: what improves / worsens

v43 explicitly says one may shrink \(\delta\) to enforce buf‑admissibility, and indicates a desire for “monotone‑safe” δ‑dependence【1045:7†manuscript_v43.pdf†L62-L67】. The v44 patch queue strengthens this into an explicit quantifier contract: \(\delta\) is any \(0<\delta\le\delta_0\) that is buffered; all claims must quantify over this choice【1049:2†v44_patch_queue_pre_batch15.md†L27-L34】.

**Local monotonicity ledger** (important for audit):

- **Admissibility:** becomes *easier* as \(\delta\downarrow 0\) (buffer target is \(\mathrm{buf}\,\delta\)).
- **FORCE stability:** becomes *easier* as \(\delta\downarrow 0\) (remainder \(O(\delta)\) shrinks)【1045:14†manuscript_v43.pdf†L6-L12】.
- **UE‑INPUT(L1):** becomes *harder* as \(\delta\downarrow 0\) **if any pole sits \(O(\delta)\) from the contour**, because \(\int|\mathcal D|\) has per‑pole contribution \(\asymp h/\delta^2=\kappa/\delta\) in the toy model (see §2 and Lemma 12.23)【1045:11†manuscript_v43.pdf†L77-L118】.
  So the phrase “RHS shrinks with \(h\sim\delta\)” is not a monotonicity proof; it is just the RHS scaling. Any monotone‑safe statement must be attached to the *actual functional being bounded* (or else quantified for **all** buffered \(\delta\)).

This is exactly why v44 wants the explicit quantifier contract and a resonance paragraph【1049:2†v44_patch_queue_pre_batch15.md†L27-L34】.

---

## 2) Dangerous configuration: two distinct tilts at the same height

### 2.1 The configuration

Assume (as a local stress test) that \(E\) has **two quartets** at the same height \(m\):

- Quartet A: zeros at \(\pm a\pm i m\).
- Quartet B: zeros at \(\pm(a-\varepsilon)\pm i m\), with \(\varepsilon\asymp \delta\).

We study the UE contour for parameter \(a\) (so the “expected” quartet is at \(\pm a\pm i m\)), and ask what the nearby quartet at \(a-\varepsilon\) does to \(\mathcal D_{a,h}\).

### 2.2 Local pole geometry in the \(u\)-disk

Write \(u:=v-im\), so \(|u|=\delta\) on the hinge circle.

A zero at \(v_0=(a-\varepsilon)+im\) produces poles in the shifted log-derivatives whenever \(v(\theta)+(a\pm h)=v_0\), i.e.
\[
u = (a-\varepsilon) - (a\pm h)= -\varepsilon\mp h.
\]
Thus the **double‑shift difference** sees poles at
\[
u = -\varepsilon\pm h.
\]

If \(\varepsilon\asymp \delta\), then for typical \(\kappa\) we have \(|-\varepsilon+h|<\delta\) (inside the \(u\)-disk) and \(|-\varepsilon-h|>\delta\) (outside), so **exactly one of these poles lies inside the witness disk**. This is the “resonant clutter” scenario: a second quartet pushes an *extra pole* into the local disk at scale \(\delta\).

### 2.3 Consequences for UE‑INPUT(L1)

Once an extra pole is inside \(|u|<\delta\), the absolute \(L^1\) integral is forced to be large (no phase cancellation allowed). Concretely, v43 already proves the core mechanism in the single‑quartet model: for \(\mathcal D_{\mathrm{sing}}(v)=-4h/(u^2-h^2)\),
\[
\int_0^{2\pi}|\mathcal D_{\mathrm{sing}}(v(\theta))|\,d\theta\ \gtrsim\ \frac{h}{\delta^2}=\frac{\kappa}{\delta},
\]
and therefore any UE bound of the schematic form \(\int|\mathcal D|\ll h(\log m)^{C'}/a^2\) is **incompatible with the presence of an off‑axis quartet at that height**【1045:11†manuscript_v43.pdf†L77-L118】.

With **two quartets** at the same height, the problem only gets worse for an absolute‑value UE: the extra pole contributes an additional \(\asymp h/\delta^2\) “per‑pole” spike, so resonance makes the obstruction *more* robust, not less.

**Verdict (L1): FAIL for “resonance robustness” as an interface.**  
UE‑INPUT(L1) is explicitly designed to *rule out* quartets; absolute value means any near‑resonant quartet in the \(\delta\)-window produces δ‑inert mass rather than cancelling. This is compatible with the closure logic (it yields contradiction), but it makes the UE statement extremely strong and phase‑blind (see §3).

### 2.4 Is signed k=2 more robust?

Signed k=2 controls are **phase‑sensitive**; they can in principle allow cancellation between different local contributors. The v44 notes explicitly flag the “phase‑loss issue” for the v43 absolute‑value interface and motivate a signed channel bound as a bridge‑compatible alternative【1049:5†integration_notes_v44_prebuild_pre_batch15.md†L16-L27】.

However, purely locally:

- A pole at location \(u_0\) inside the disk has a Fourier series on \(|u|=\delta\) whose coefficients scale like \((u_0/\delta)^{k-1}/\delta\). When \(|u_0|\asymp \delta\) (the resonant case), its **k=2 coefficient is \(\asymp 1/\delta\)**, i.e. δ‑inert after the \(\delta^2/h\) normalization.
- Therefore, signed k=2 is not automatically safe: a second quartet can contaminate the k=2 channel at the same scale as the forced quartet *unless* (i) \(\delta\) is chosen small enough that \(|u_0|\ll \delta\) or \(|u_0|>\delta\), or (ii) one can prove **structural cancellation** in the signed channel.

**Verdict (signed k=2): CONDITIONAL PASS.**  
More robust than \(L^1\) because it is targeted and allows phase cancellation, but a near‑resonant quartet with \(\varepsilon\asymp\delta\) can still inject δ‑inert mass into the k=2 coefficient in worst case. Any manuscript claim of “automatic resonance suppression” should be stated with this caveat.

---

## 3) Reader‑guide Part III lens: why k=2 is the “right channel” (parity projector)

Part III of the reader‑guide isolates **odd/even lane projectors** on the integer lattice:
\[
P_{\mathrm{odd}}(n)=\sin^2(\pi n/2)=\tfrac12(1-\cos(\pi n)),\qquad
P_{\mathrm{even}}(n)=\cos^2(\pi n/2)=\tfrac12(1+\cos(\pi n)),
\]
which form an orthogonal split of “odd slots” vs “even slots”【1019:1†reader_guide_v1.pdf†L21-L30】. The guide explicitly interprets this as separating a “nontrivial stream” from a “trivial ladder” by parity projection【1019:1†reader_guide_v1.pdf†L36-L44】.

### 3.1 Continuous analogue on the hinge circle

On the hinge circle, the natural “lattice sampling” is the \(\pi/2\) grid:
\(\theta_n = n\pi/2\) (the four quadrants). Then
\[
e^{-2i\theta_n}=e^{-i\pi n}=(-1)^n=\cos(\pi n).
\]
So the **k=2 Fourier mode** on the circle is exactly the continuous analogue of the **parity projector** \(n\mapsto (-1)^n\) that underlies the reader‑guide’s Part III decomposition.

This explains, geometrically, why k=2 is the right channel for GEO‑C4:
- The quartet‑forced singular model is a *dipole* \(\propto 1/(u^2-h^2)\), i.e. an “even” object in \(u\), so its angular dependence lives in even harmonics and locks onto k=2 (the first nontrivial even mode)【1045:11†manuscript_v43.pdf†L1-L28】.
- The k=2 projection is the minimal “parity‑sensitive” probe on the \(\pi/2\) carrier grid; it is the continuous version of \(P_{\mathrm{odd}}-P_{\mathrm{even}}\).

### 3.2 What to add to the v44 manuscript (expository, not math)

**Suggested remark location:** immediately after the definition of \(P_2\) / the endpoint \(\Phi^\star\).

**Suggested remark text (one paragraph):**
> “The k=2 harmonic is not an arbitrary choice: on the \(\pi/2\) sampling grid \(\theta_n=n\pi/2\) it coincides with the parity character \(e^{-2i\theta_n}=(-1)^n\), i.e. the continuous analogue of the odd/even lane projectors \(P_{\mathrm{odd}},P_{\mathrm{even}}\) (reader‑guide Part III). The forced quartet singularity is even in \(u\) and hence lives naturally in the first even channel k=2.”

This makes future builds easier because it turns “k=2 looks magical” into a stable structural identity anchored to the Part III projector calculus.

---

## 4) Obstruction packaged as a NO‑GO lemma + minimal repair

### 4.1 NO‑GO lemma (quantified failure mode)

> **NO‑GO (local resonance → δ‑inert channel mass).**  
> If there exists a second quartet at the same height \(m\) whose tilt differs by \(\varepsilon\lesssim\delta\), then one of its induced poles \(u=-\varepsilon\pm h\) lies inside the hinge disk \(|u|<\delta\). This produces a per‑pole contribution of size \(\asymp h/\delta^2\) to \(\int|\mathcal D_{a,h}(v(\theta))|d\theta\) (hence δ‑inert after multiplying by \(\delta^2/h\)), and in worst case can also contribute δ‑inert mass to the signed k=2 coefficient.

This is the exact same “δ‑inert resonance” mechanism that was truth‑latched earlier for defect endpoints (v39)【1049:14†manuscript_v39.pdf†L1-L6】—here it reappears as a *local* warning about UE interfaces that use absolute values or nonnegative norms.

### 4.2 Minimal repairs (ordered by “least disruption to locked machinery”)

1) **Quantifier hygiene (must land in v44):**  
   Adopt the explicit δ‑shrink contract in v44 (patch queue P2): \(\delta\) is any \(0<\delta\le\delta_0\) that satisfies buf‑admissibility, and every lemma must quantify over this choice explicitly (no hidden monotonicity claims)【1049:2†v44_patch_queue_pre_batch15.md†L27-L34】.

2) **Optional (inactive) signed channel interface:**  
   Keep v43 UE‑INPUT(L1) as the single active box for now, but install the signed k=2 alternative as an *inactive candidate* (patch queue P3). This is exactly the candidate already recorded in the v44 queue【1049:2†v44_patch_queue_pre_batch15.md†L36-L42】 and in the v44 integration notes【1049:5†integration_notes_v44_prebuild_pre_batch15.md†L24-L27】.

3) **If a proof attempt for UE‑INPUT(L1) hits resonance spikes:**  
   The smallest “local repair” is to replace the absolute \(L^1\) control with a direct bound on the signed k=2 coefficient (UE‑k2). This preserves phase (needed for Weil/Li)【1049:1†integration_notes_v44_prebuild_pre_batch15.md†L1-L5】 and targets only the channel used by \(\Phi^\star\).

4) **If even UE‑k2 is contaminated by resonant quartets:**  
   One must add an explicit **δ‑aware resonance accounting** term (counting poles with \(|u_0|<\delta\)) or prove an isolation lemma that, after shrinking δ, no extra poles remain in the hinge disk. This is conceptually the same “δ‑aware resonance sum” logic developed in v40 for the defect branch【1049:15†manuscript_v40.pdf†L27-L58】.

---

## 5) PASS/FAIL table (requested)

| UE interface (candidate) | Uses only 4 shift traces? | Phase‑sensitive? | Behavior under “two tilts ε≈δ” | Local verdict |
|---|---:|---:|---|---|
| **UE‑INPUT(L1)**: \(\int|\mathcal D|\) bound (active v43)【1049:5†integration_notes_v44_prebuild_pre_batch15.md†L8-L13】 | ✅ | ❌ (absolute value) | Extra quartet injects δ‑inert \(h/\delta^2\) spikes; no cancellation | **FAIL** as resonance‑robust interface (but strong enough to contradict quartet) |
| **UE‑k2 (signed)**: \(\big|\int \mathcal D\,e^{-2i\theta}\big|\) bound (inactive)【1049:5†integration_notes_v44_prebuild_pre_batch15.md†L24-L27】 | ✅ | ✅ | Can still be δ‑inert in worst case, but allows cancellation and targets only the needed channel | **CONDITIONAL PASS** (needs either isolation via δ choice or structural cancellation) |
| **\(L^2\partial_t\mathcal L_t\)**‑type bound (legacy v42 flavor) | ❌ (typically needs corridor in \(t\)) | mixed | Near poles derivatives blow up; mean‑square doesn’t automatically kill spikes | **FAIL / likely RH‑strength** locally (matches v42 NO‑GO logic) |

---

## 6) TeX‑ready “LOCAL admissibility lemma” (requested)

**Insert location suggestion:** right after Definition 12.19 / Remark 12.20 (so the δ‑shrink contract becomes proof‑grade before UE‑INPUT is stated). This matches the v44 patch queue goal of making δ‑shrink quantifiers explicit【1049:2†v44_patch_queue_pre_batch15.md†L27-L34】.

```tex
\begin{lemma}[LOCAL buf--admissible shrink for shifted hinge traces]
\label{lem:local-buf-shrink}
Fix $m\ge 0$, $a\in(0,1)$, $\kappa\in(0,1)$, and ${\rm buf}\in(0,1)$.
Let $v(\theta):=im+\delta e^{i\theta}$ and set $h:=\kappa\delta$.
Assume only that $E$ is entire (evenness not needed here) and that its zero set $\mathcal Z(E)$
is discrete.

Then there exists $\delta_\star=\delta_\star(E;m,a,\kappa,{\rm buf})>0$ such that for every
$0<\delta\le \delta_\star$ we have
\[
{\rm dist}\big(v(\theta)\pm(a\pm h),\ \mathcal Z(E)\big)\ \ge\ {\rm buf}\cdot\delta
\qquad\forall\theta\in[0,2\pi].
\]
In particular, for all $0<\delta\le\delta_\star$ the hinge circle $C_{m,\delta}$ is
${\rm buf}$--admissible at $(a,h)$ (Definition~\ref{def:shift-admissible-hinge-circle}).
\end{lemma}

\begin{proof}[Proof sketch]
Let $S_\delta:=\{v(\theta)\pm(a\pm\kappa\delta):\theta\in[0,2\pi]\}$.
As $\delta\to 0$ the compact set $S_\delta$ converges (in Hausdorff distance) to the finite set
$S_0:=\{im\pm a\}$.
Since $\mathcal Z(E)$ is discrete, either $\mathcal Z(E)\cap S_0=\emptyset$ (in which case
${\rm dist}(S_0,\mathcal Z(E))=:d_0>0$ and continuity yields ${\rm dist}(S_\delta,\mathcal Z(E))\ge d_0/2$
for $\delta$ small), or else some point of $S_0$ is a zero (the quartet case), in which case
the explicit geometry gives ${\rm dist}(v(\theta)+(a\pm h),\,a+im)\ge |\,\delta-h\,|=(1-\kappa)\delta$.
Taking ${\rm buf}<1-\kappa$ (as in the global $\kappa$--admissibility policy) and shrinking $\delta$
if necessary to separate $S_\delta$ from all other zeros yields the claim.
\end{proof}
```

*(If the build wants full proof instead of “sketch”: expand the two cases, and in the quartet case also handle multiplicities; the geometry is unchanged.)*

---

## 7) Patch map for v44 (requested)

This matches the current v44 documentation plan (P0–P2)【1049:3†v44_build_protocol_pre_batch15.md†L12-L21】.

1) **Section near Definition 12.19 / Remark 12.20 (main text):**
   - Add Lemma `lem:local-buf-shrink` above (formalizes “shrink δ to enforce buffering”).
   - Add one explicit sentence: “No monotonicity of the UE integrand in δ is assumed; all statements quantify over the chosen buffered δ.” (this is exactly patch queue P2)【1049:2†v44_patch_queue_pre_batch15.md†L27-L34】.

2) **Immediately after the UE‑INPUT box (main text):**
   - Add a short “resonance stress test” remark: absolute‑value interfaces are phase‑blind and can be δ‑inert under near‑resonant quartets (cross‑reference Lemma 12.23 and the v39 δ‑inert resonance latch). Use two‑tilt picture from §2.

3) **Near the definition of \(P_2\) / \(\Phi^\star\) (main text):**
   - Add the k=2 parity‑projector remark (reader‑guide Part III link) to stabilize the intuition for future builds【1019:1†reader_guide_v1.pdf†L21-L30】.

4) **Appendix (v44 documentation upgrades):**
   - UE Playbook: include the δ‑shrink quantifier contract and list both UE‑INPUT(L1) and the inactive UE‑k2 box【1049:2†v44_patch_queue_pre_batch15.md†L6-L14】【1049:2†v44_patch_queue_pre_batch15.md†L36-L42】.
   - Weil/Li harness subsection: include the “phase‑loss caution” and why UE‑k2 is bridge‑compatible【1049:5†integration_notes_v44_prebuild_pre_batch15.md†L16-L27】.

---

# Patch packet (concise)

**Callsign:** RH‑LOCAL  
**Batch:** 15  
**Scope:** local geometry / admissibility / resonance hygiene for UE interface (no change to FORCE machinery).

**Delivered:**
- Local dependency map (§1).
- Two‑tilt resonance analysis with PASS/FAIL verdicts (§2 + §5).
- Reader‑guide Part III → k=2 parity‑projector explanation (§3) with explicit citation to the projector identities【1019:1†reader_guide_v1.pdf†L21-L30】.
- TeX‑ready “LOCAL buf‑admissible shrink” lemma (§6).
- v44 patch insertion map aligned with patch queue P2/P3 (§7).

**Main local conclusion:**  
Absolute‑value \(L^1\) UE interfaces are **not resonance‑robust** and are **phase‑blind**; signed k=2 is more bridge‑compatible but still needs either isolation via δ choice or structural cancellation to neutralize δ‑inert resonant clutter.

