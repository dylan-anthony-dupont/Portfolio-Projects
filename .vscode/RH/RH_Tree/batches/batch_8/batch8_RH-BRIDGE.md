# batch8_RH-BRIDGE.md

**CALLSIGN:** RH-BRIDGE  
**GROUND TRUTH:** v38 locked build  
**BATCH:** 8  
**MISSION:** Provide the geometric/analytic bridge lemmas that make a chosen LOCAL redesign mechanism work on the **buffered contour** (collar-safe, branch-safe, and δ-scaled correctly).

---

## A) Mechanism choice (mandatory)

I support **M3 = pair-isolation on the buffered contour** (the v38 “LOCAL REDESIGN” option (iii): *only the forced pair contributes \(O(1)\) to \(\widetilde D_B\) while the remainder contributes \(O(\delta\log m)\)*).

**What RH-BRIDGE contributes:** a proof-grade *distance–weighted* phase-increment inequality on each buffered side, showing that any zero \(\rho\) whose Euclidean distance to a boundary segment \(S\) is \(\gg \delta\) contributes only \(O(\delta/d)\) to \(\Delta_S\arg(v-\rho)\). This is the geometric input needed to turn “isolation of the forced pair” into an actual \(\delta\)-gain.

---

## B) Endpoint functional supported + setup (v38-consistent)

### Endpoint class

We work in the **buffered boundary phase endpoint class** (v38 Def. 12.19):
\[
\widetilde D_B(W)\ :=\ \max_{1\le j\le 4}\left|\Delta_{S_j}\arg W\right|,
\qquad 
\Delta_{S_j}\arg W\ :=\ \Im\int_{S_j}\frac{W'(v)}{W(v)}\,dv,
\]
where \(\partial B_{\kappa/2}=\bigcup_{j=1}^4 S_j\) is the oriented boundary of the buffered inner rectangle.

### Geometry

An aligned box is
\[
B(\alpha,m,\delta):=\{v\in\mathbb C:\ |\Re v-\alpha|\le \delta,\ |\Im v-m|\le \delta\}.
\]
The buffered inner rectangle is
\[
B_{\kappa/2}:=\{v\in B:\ \mathrm{dist}(v,\partial B)\ge \kappa\delta/2\}.
\]
For a square, \(\partial B_{\kappa/2}\) is the boundary of the smaller concentric square with half-side
\[
\delta_{\mathrm{in}}:=\delta-\kappa\delta/2=(1-\kappa/2)\delta,
\]
hence each side has length
\[
|S_j| = 2\delta_{\mathrm{in}}=(2-\kappa)\delta.
\]

### Collar and branch hygiene (mandatory)

Assume **κ-admissibility** (v38 Def. 12.19):
\[
\mathrm{dist}(\partial B,\ Z(E))\ \ge\ \kappa\delta.
\]

Then the **collar nonvanishing lemma** (v38 Lem. 12.20) gives
\[
\mathrm{dist}(\partial B_{\kappa/2},\ Z(E))\ \ge\ \kappa\delta/2.
\]
Consequently, if \(G_{\mathrm{out}}\) is the Dirichlet outer factor on \(B^\circ\) and \(W:=E/G_{\mathrm{out}}\), then both \(G_{\mathrm{out}}\) and \(W\) are holomorphic and nonvanishing on an open neighborhood of \(\partial B_{\kappa/2}\). Therefore each \(\Delta_{S_j}\arg W\) is well-defined and **branch choices are harmless**: one may define it via \(\Im\int (W'/W)\) (branch-free), and this equals the usual argument increment for any continuous branch of \(\arg W\) along \(S_j\).

---

## C) Bridge lemma(s) (proof-grade) in the endpoint class

### Lemma 1 (refined per-zero phase increment on a segment; v38 Lem. 12.22)

Let \(S\subset\mathbb C\) be an oriented line segment of length \(|S|\), and let \(\rho\notin S\). Write
\[
d:=\mathrm{dist}(\rho,S).
\]
Then
\[
\left|\Im\int_S\frac{dv}{v-\rho}\right|\ \le\ \min\Bigl\{\pi,\ \frac{|S|}{d}\Bigr\}.
\]

**Proof sketch (fully standard, but the δ-scaling is the point):**
- Since \(v\mapsto \arg(v-\rho)\) changes by at most \(\pi\) along a line segment avoiding \(\rho\), one always has the crude bound \(\le\pi\).
- Also,
\[
\left|\Im\int_S\frac{dv}{v-\rho}\right|
\le \left|\int_S\frac{dv}{v-\rho}\right|
\le \int_S\frac{|dv|}{|v-\rho|}
\le \frac{|S|}{d}.
\]
Taking the minimum gives the stated inequality.

**Key δ-gain:** when \(|S|\asymp \delta\) and \(d\) is independent of \(\delta\), the contribution is \(O(\delta)\).

---

### Lemma 2 (distance-weighted local phase bound on buffered sides)

Let \(Z_{\mathrm{loc}}(v)=\prod_{\rho\in Z_{\mathrm{loc}}(m)}(v-\rho)^{m_\rho}\) be the local factor (zeros in the chosen local window around height \(m\), counted with multiplicity \(m_\rho\)).  
Let \(S\subset\mathbb C\) be an oriented line segment such that \(S\cap Z_{\mathrm{loc}}(m)=\varnothing\) (equivalently, \(Z_{\mathrm{loc}}\) is holomorphic and nonvanishing on a neighborhood of \(S\)). Then:
\[
\boxed{
\ \bigl|\Delta_S\arg Z_{\mathrm{loc}}\bigr|
\ =\ \left|\Im\int_S\frac{Z'_{\mathrm{loc}}(v)}{Z_{\mathrm{loc}}(v)}\,dv\right|
\ \le\ \sum_{\rho\in Z_{\mathrm{loc}}(m)} m_\rho\ \min\Bigl\{\pi,\ \frac{|S|}{\mathrm{dist}(\rho,S)}\Bigr\}.
\ }
\]

#### Proof (complete)
Since \(Z_{\mathrm{loc}}\) is nonvanishing near \(S\), we may write
\[
\frac{Z'_{\mathrm{loc}}(v)}{Z_{\mathrm{loc}}(v)}=\sum_{\rho\in Z_{\mathrm{loc}}(m)}\frac{m_\rho}{v-\rho}
\]
(pointwise on a neighborhood of \(S\)). Therefore
\[
\Delta_S\arg Z_{\mathrm{loc}}
=\Im\int_S\sum_{\rho}\frac{m_\rho}{v-\rho}\,dv
=\sum_{\rho}m_\rho\ \Im\int_S\frac{dv}{v-\rho}.
\]
Taking absolute values and using the triangle inequality gives
\[
\bigl|\Delta_S\arg Z_{\mathrm{loc}}\bigr|
\le \sum_{\rho}m_\rho\ \left|\Im\int_S\frac{dv}{v-\rho}\right|.
\]
Apply Lemma 1 to each \(\rho\) to obtain the claimed bound.

---

### Corollary 3 (near/far decomposition; explicit δ-gain for the “far” cluster)

Fix a threshold \(d_\star>0\). For a segment \(S\), define
\[
Z_{\mathrm{near}}(S;d_\star):=\{\rho\in Z_{\mathrm{loc}}(m):\ \mathrm{dist}(\rho,S)<d_\star\},
\qquad
Z_{\mathrm{far}}(S;d_\star):=Z_{\mathrm{loc}}(m)\setminus Z_{\mathrm{near}}(S;d_\star),
\]
and the weighted counts
\[
N_{\mathrm{near}}(S;d_\star):=\sum_{\rho\in Z_{\mathrm{near}}(S;d_\star)} m_\rho,
\qquad
N_{\mathrm{loc}}(m):=\sum_{\rho\in Z_{\mathrm{loc}}(m)} m_\rho.
\]

Then Lemma 2 implies
\[
\boxed{
\ \bigl|\Delta_S\arg Z_{\mathrm{loc}}\bigr|
\ \le\ \pi\,N_{\mathrm{near}}(S;d_\star)\ +\ |S|\sum_{\rho\in Z_{\mathrm{far}}(S;d_\star)}\frac{m_\rho}{\mathrm{dist}(\rho,S)}.
\ }
\]
In particular, since \(\mathrm{dist}(\rho,S)\ge d_\star\) for \(\rho\in Z_{\mathrm{far}}(S;d_\star)\),
\[
\boxed{
\ \bigl|\Delta_S\arg Z_{\mathrm{loc}}\bigr|
\ \le\ \pi\,N_{\mathrm{near}}(S;d_\star)\ +\ \frac{|S|}{d_\star}\,N_{\mathrm{loc}}(m).
\ }
\]

**Applying to buffered sides:** if \(S=S_j\subset\partial B_{\kappa/2}\), then \(|S|=(2-\kappa)\delta\), hence
\[
\bigl|\Delta_{S_j}\arg Z_{\mathrm{loc}}\bigr|
\ \le\ \pi\,N_{\mathrm{near}}(S_j;d_\star)\ +\ \frac{(2-\kappa)\delta}{d_\star}\,N_{\mathrm{loc}}(m).
\]

---

## D) Compatibility with FORCE and ENVELOPE (mandatory)

### What endpoint functional do the lemmas support?

They support the **same endpoint class** as v38:
- the sidewise phase increments \(\Delta_{S_j}\arg(\cdot)\) on \(\partial B_{\kappa/2}\);
- hence any bound on \(\max_j|\Delta_{S_j}\arg Z_{\mathrm{loc}}|\) is immediately compatible with \(\widetilde D_B(\cdot)\).

### How does it compose with forcing?

FORCE for \(\widetilde D_B\) is already proved in v38 (Lemma 12.23):  
if \(W\) has a zero in \(B_{\kappa/2}^\circ\), then \(\widetilde D_B(W)\ge \pi/2\).

The lemmas above are **upper bounds** on local-factor phase contributions; they do not alter the argument principle or the forcing statement. In particular, no RH-equivalent assumptions are used: the only structural hypothesis is κ-admissibility (a contour-avoidance condition), which is already part of the forcing setup.

### What exponent gain does the bridge lemma supply?

Corollary 3 shows:

- If \(\rho\) is **far** from a side \(S\) (distance \(\ge d_\star\)), its contribution is \(O(|S|/d_\star)=O(\delta/d_\star)\).
- Therefore, if LOCAL can ensure that *all but \(O(1)\) local-window zeros* satisfy \(\mathrm{dist}(\rho,S_j)\ge d_\star\) with a \(d_\star\) that does **not** decay like \(\delta\), then the **remainder cluster** contributes
\[
O\!\left(\frac{\delta}{d_\star}\,N_{\mathrm{loc}}(m)\right)=O(\delta\log m).
\]

At the nominal scale \(\delta_0(m,\alpha)=\eta\alpha/(\log m)^2\), this becomes
\[
O(\delta_0\log m)=O\!\left(\frac{\eta\alpha}{\log m}\right),
\]
which is **effectively \(q=0\)** in the budget calculus (bounded in \(m\), and in fact decaying).

This is exactly the “geometry \(\Rightarrow\) δ-gain” conversion needed to make the pair-isolation option (M3) algebraically decisive once ENVELOPE provides \(p\ge 1/2\).

---

## E) Where branch choices enter, and why they are harmless (mandatory)

1. For a single pole \((v-\rho)^{-1}\), \(\Im\int_S dv/(v-\rho)\) equals an argument difference for any continuous branch of \(\arg(v-\rho)\) along \(S\). Such a continuous branch exists because \(S\) is connected and avoids \(\rho\).

2. For \(Z_{\mathrm{loc}}\), we *do not need* to pick a global branch of \(\log Z_{\mathrm{loc}}\). The definition
\[
\Delta_S\arg Z_{\mathrm{loc}} := \Im\int_S \frac{Z'_{\mathrm{loc}}}{Z_{\mathrm{loc}}}\,dv
\]
is branch-free. If desired, κ-admissibility + Lemma 12.20 ensures \(Z_{\mathrm{loc}}\) (and \(W\)) is nonvanishing on a neighborhood of each buffered side, hence a local holomorphic logarithm exists there and the integral matches the branch-based definition.

---

## F) How this makes M3 “pair isolation” work on the buffered contour

The output of Corollary 3 is a **clean reduction**:

> To upgrade the crude phase-class local bound  
> \(\max_j|\Delta_{S_j}\arg Z_{\mathrm{loc}}|\le \pi N_{\mathrm{loc}}(m)\)  
> into the desired “forced pair \(+\) δ–small remainder” structure, it suffices to prove that (for each side \(S_j\)) only \(O(1)\) zeros in the local window lie within distance \(<d_\star\) of that side, where \(d_\star\) does not shrink like \(\delta\).

Concretely, if LOCAL supplies (for the forced box \(B(\alpha,m,\delta)\)) a statement of the form:

> (**Pair-isolation hypothesis on buffered sides**)  
> There exists \(d_\star\asymp 1\) (or \(d_\star\asymp \alpha\)) such that for each side \(S_j\subset\partial B_{\kappa/2}\),
> \[
> N_{\mathrm{near}}(S_j;d_\star)\ \le\ C_{\mathrm{pair}}
> \quad\text{with }C_{\mathrm{pair}}=O(1)
> \]
> and the “near” zeros consist only of the forced quartet members relevant to \(B(\alpha,m,\delta)\),

then Corollary 3 yields
\[
\max_j\bigl|\Delta_{S_j}\arg Z_{\mathrm{loc}}\bigr|
\ \le\ \pi C_{\mathrm{pair}}\ +\ O(\delta\log m),
\]
i.e. *the local growth exponent drops from \(q=1\) to effectively \(q=0\) at the nominal scale.*

This is the precise bridge from geometry (distance-to-side) to δ-gain in the phase endpoint.

---

## G) S6 explicit-formula amplitude-leak mapping (mandatory)

### s → u → v scaling language (as used in the manuscript)

- A zero \(\rho=\beta+i\gamma\) of \(\zeta(s)\) corresponds to a zero of the completed zeta \(\xi(s)\).
- In the manuscript’s \(v\)-frame, one uses \(v=2s-1\), so
\[
v_\rho = 2\beta-1 + i\,2\gamma.
\]
Thus **off-axis** means \(\beta>1/2\), equivalently \(\Re(v_\rho)>0\).

### Explicit-formula “amplitude leak”

In the classical explicit formula for prime-counting error terms (e.g. \(\psi(x)-x\)), a zero \(\rho=\beta+i\gamma\) contributes an oscillatory term of size \(\asymp x^\beta/|\rho|\). Hence \(\beta>1/2\) produces an “amplitude leak” larger than the RH-predicted \(x^{1/2}\)-scale.

### Mapping to the phase endpoint + this bridge lemma

- The buffered phase endpoint \(\widetilde D_B(W)\) is **not itself** an amplitude functional; it is a *local analytic witness* for the presence of zeros of \(E\) in \(B_{\kappa/2}^\circ\) (argument principle).
- However, it is compatible with the explicit-formula narrative: if an off-axis zero exists (\(\beta>1/2\)), then there is a corresponding \(v_\rho\) with \(\Re(v_\rho)>0\). Choosing an aligned box around \(v_\rho\) forces \(\widetilde D_B(W)\ge\pi/2\). The “large amplitude leak” is what makes such a zero dangerous globally; the endpoint is the local certificate used in the S5′ contradiction.

**What the bridge lemma says in this language:** any zeros \(\rho\) in the local window that are *not geometrically close* to the buffered contour contribute only \(O(\delta/d)\) to the phase increment; therefore they cannot be responsible for the forced \(O(1)\) phase witness. Under pair-isolation, the only \(O(1)\) contributors are precisely the forced off-axis quartet members.

---

## H) Paste-ready TeX edits (v39 candidate insertions)

Below are TeX blocks intended to drop into v39 after v38 Lemma 12.22 (or near Corollary 12.21).

```tex
% --- RH-BRIDGE Batch 8: distance-weighted local phase bound (M3 support) ---

\begin{lemma}[Distance-weighted local phase bound on a segment]
\label{lem:local_phase_dist_weighted}
Let $S\subset\C$ be an oriented line segment and let
\[
Z_{\rm loc}(v)=\prod_{\rho\in Z_{\rm loc}(m)} (v-\rho)^{m_\rho}
\]
be the local factor. Assume $Z_{\rm loc}$ is holomorphic and nonvanishing on an open
neighborhood of $S$ (equivalently $S\cap Z_{\rm loc}(m)=\varnothing$). Then
\[
\Bigl|\Delta_S \arg Z_{\rm loc}\Bigr|
=\left|\Im\int_S \frac{Z_{\rm loc}'(v)}{Z_{\rm loc}(v)}\,dv\right|
\le \sum_{\rho\in Z_{\rm loc}(m)} m_\rho\,
\min\left\{\pi,\ \frac{|S|}{\dist(\rho,S)}\right\}.
\]
\end{lemma}

\begin{corollary}[Near/far decomposition and $\delta$--gain for far zeros]
\label{cor:local_phase_near_far}
In the setup of Lemma~\ref{lem:local_phase_dist_weighted}, fix $d_\star>0$ and write
\[
Z_{\rm near}(S;d_\star):=\{\rho\in Z_{\rm loc}(m):\ \dist(\rho,S)<d_\star\},
\quad
N_{\rm near}(S;d_\star):=\sum_{\rho\in Z_{\rm near}(S;d_\star)} m_\rho.
\]
Then
\[
\Bigl|\Delta_S \arg Z_{\rm loc}\Bigr|
\le \pi\,N_{\rm near}(S;d_\star)\ +\ \frac{|S|}{d_\star}\,N_{\rm loc}(m).
\]
In particular, if $S=S_j\subset\partial B_{\kappa/2}$ is any buffered side from
Definition~12.19, then $|S_j|=(2-\kappa)\delta$ and therefore
\[
\Bigl|\Delta_{S_j}\arg Z_{\rm loc}\Bigr|
\le \pi\,N_{\rm near}(S_j;d_\star)\ +\ \frac{(2-\kappa)\delta}{d_\star}\,N_{\rm loc}(m).
\]
\end{corollary}
```

**Notes for integration:**
- No renumbering assumptions are needed; labels are new.
- These statements are *branch-safe* because they use \(\Im\int (Z'_{\rm loc}/Z_{\rm loc})\).
- The only geometric input is Lemma 12.22 (already in v38).

---

## Mandatory PATCH PACKET

**Patch file:** `batch8_RH-BRIDGE.md`  

**Mechanism chosen:** **M3 (pair isolation on buffered contour)**

**Result type:** **PROOF-GRADE LEMMA** (the distance-weighted inequalities).  
**Status vs the global missing lever:** **CONDITIONAL ENABLEMENT** — these lemmas *enable* the pair-isolation route, but do not by themselves prove the required isolation bound \(N_{\rm near}=O(1)\).

### Target gaps closed (by ID)
- **G‑4′ (S5′ Missing Lever) — LOCAL subcomponent:** provides the *geometric bridge inequality* converting distance-to-segment into a δ-gain for phase increments in the \(\widetilde D_B\) endpoint class.

### What remains open / dependencies
- LOCAL must still supply an actual **pair-isolation (or micro-window) bound** controlling \(N_{\rm near}(S_j;d_\star)\) at the nominal scale.
- ENVELOPE must still supply a **budget-eligible UE bound** with \(p\ge 1/2\) (and compatible \(\theta\)).
- FORCE is already complete for \(\widetilde D_B\) (v38 Lem. 12.23), but any redesign \(\Phi_B\) must dominate \(\widetilde D_B\) or come with its own forcing lemma (v38 Rem. 12.25).

### Key conclusions (≤5 bullets)
1. Each zero \(\rho\) contributes at most \(\min\{\pi, |S|/\dist(\rho,S)\}\) to a segment phase increment; for \(|S|\asymp\delta\) and \(\dist\gg\delta\), this is \(O(\delta/d)\).
2. The local-factor phase increment on any side is bounded by the **distance-weighted sum** over local zeros (Lemma 2).
3. Splitting into “near” and “far” zeros yields a clean bound: \(\pi N_{\rm near} + (|S|/d_\star)N_{\rm loc}\) (Corollary 3).
4. Under the pair-isolation scenario (only \(O(1)\) near zeros), the remainder contributes \(O(\delta\log m)\), i.e. **effective \(q=0\)** at \(\delta_0=\eta\alpha/(\log m)^2\).
5. All statements are collar-safe (κ-admissibility) and branch-safe (integral definition).

### Paste-ready TeX blocks included?
**Yes** (see Section H).

### Risk notes / audit flags
- The δ-gain is purely geometric; **no RH inputs** are used.
- The only nontrivial “open” ingredient is whether one can prove \(N_{\rm near}=O(1)\) (pair isolation) for the chosen boxes at the nominal scale; this patch does not claim that.
