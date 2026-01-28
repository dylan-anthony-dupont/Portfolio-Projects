# Batch 10 — RH-LOCAL (v39 locked)  
**Mission:** ML‑3 Resonance control (decision-grade)  
**Choice (Deliverable A):** **(L‑1) Pair isolation (height‑local)** — pursued to a decisive **NO‑GO / FAIL** under current inputs.

---

## 1) Executive verdict (ML‑3)

### Verdict: **FAIL (NO‑GO in current architecture)**
Using only the inputs currently available inside v39’s S5^{def} tooling (even/entire structure of \(E\), κ‑admissibility, local cancellation, and the coarse local-window zero-count majorant), **there is no proof-grade route to exclude or bound the near-resonant quartet configuration** that drives the δ‑inert obstruction. The toy-model lemma already embedded in v39 shows the obstruction is real at the level of “allowed local geometry,” and the present resonance accounting object \(\mathcal R_a(m)\) does **not** detect the δ‑scale triggering mechanism.  

Concretely: a near-resonant quartet at real part \(a-\varepsilon\) with \(\varepsilon \asymp \delta\) can force \(\Phi^{\rm def}_B(a)\ge c_0>0\) even while \(\delta a\,\mathcal R_a(m)=O(\delta)\to0\). This disproves any hope that (Remark 12.6)’s target defect‑UE bound can be proved **without adding a δ‑aware resonance exclusion/bound**. 【816:5†manuscript_v39.pdf†L32-L83】

---

## 2) What resonance really is in v39 (Deliverable B)

### Ground truth objects (v39)
- Defect quotient and log-derivative:  
  \[
  \mathcal Q_a(v)=\frac{E(v+a)}{E(v-a)},\qquad 
  \mathcal L_a(v)=\frac{\mathcal Q_a'(v)}{\mathcal Q_a(v)}=\frac{E'}{E}(v+a)-\frac{E'}{E}(v-a).
  \]
  【816:6†manuscript_v39.pdf†L17-L33】

- Defect phase endpoint:
  \[
  \Phi^{\rm def}_B(a):=\max_{I\in {\rm Sides}(\partial B_{\kappa/2})}
  \left|\Im\int_I \mathcal L_a(v)\,dv\right|.
  \]
  【816:6†manuscript_v39.pdf†L34-L55】

- δ‑inert NO‑GO mechanism: if a second quartet exists at real part \(a-\varepsilon\) with \(\varepsilon\asymp \delta\), then \(\mathcal Q_a\) gains a **zero–pole pair** at \(w=\pm\varepsilon\) (where \(w=v-im\)), forcing a side phase increment bounded below by an absolute constant \(c_0\), hence \(\Phi^{\rm def}_B(a)\ge c_0\). 【816:4†manuscript_v39.pdf†L3-L58】

### Why the current \(\mathcal R_a(m)\) is δ-blind
v39 defines
\[
\mathcal R_a(m):=\sum_{\rho:\,E(\rho)=0,\ |\Im\rho-m|\le1} \frac{1}{|\Re\rho-a|+a}\ \le\ \frac{1}{a}N_{\rm loc}(m).
\]
【816:5†manuscript_v39.pdf†L32-L42】

But in the NO‑GO configuration with an extra quartet at real part \(a-\varepsilon\), the contributing terms are \(\asymp 1/a\) (independent of \(\varepsilon\)), so \(\delta a\mathcal R_a(m)=O(\delta)\to0\) while \(\Phi^{\rm def}_B(a)\ge c_0\). Hence **\(\mathcal R_a(m)\) cannot serve as the resonance-control object for δ‑uniform UE**.

---

## 3) Corrected δ-aware resonance object (proposed replacement / augmentation)

To control the δ‑inert phenomenon, the resonance object must “see” whether \(\mathcal Q_a\) acquires a **zero or pole inside** the defect box \(B(0,m,\delta)\) (besides the removable singularity coming from the forced pair).

### Proposed δ-aware “near-resonance count”
Define, for \(a\in(0,1)\), \(m\ge 10\), \(0<\delta\le a/4\),
\[
N_{\rm res}(a,m,\delta)
:=\#\Bigl\{\rho:\ E(\rho)=0,\ |\Im\rho-m|\le1,\ 0<\bigl||\Re\rho|-a\bigr|\le 2\delta\Bigr\},
\]
counted with multiplicity.

**Interpretation:** \(N_{\rm res}(a,m,\delta)\ge1\) means there is at least one additional quartet whose real-part displacement is within \(O(\delta)\) of \(a\); this is exactly the geometric trigger that can place a zero/pole of \(\mathcal Q_a\) at \(w=\pm O(\delta)\) and cause δ‑inert phase.

### Consequence (restate the NO‑GO as a usable gate)
The existing NO‑GO lemma implies:  
> If \(N_{\rm res}(a,m,\delta)\ge 1\), then **δ‑uniform shrink of \(\Phi^{\rm def}_B(a)\)** is not available in general; there exist admissible \(E\) with the same local cancellation property but with \(\Phi^{\rm def}_B(a)\ge c_0\) for \(\delta\asymp\varepsilon\).【816:4†manuscript_v39.pdf†L3-L58】

So ML‑3 should be framed as either:
- **(R2′ Exclusion):** prove \(N_{\rm res}(a,m,\delta_0(m,a))=0\) for the actual \(E\), uniformly in \((m,a)\); or
- **(R1′ Bound):** replace the UE target by a bound that explicitly includes \(N_{\rm res}(a,m,\delta)\) (or a weighted δ-aware sum), accepting that the bound cannot shrink when \(N_{\rm res}\neq0\).

**Key point:** this is a strictly stronger / cleaner obligation than bounding the δ‑blind \(\mathcal R_a(m)\), and it matches the geometry of Lemma 12.7.

---

## 4) Deliverable C — κ‑admissibility + nominal δ‑policy compatibility

- Nominal policy: \(\delta_0(m,a)=\eta a/(\log m)^2\) appears in Box 12.1’s ML‑1 regime statement and in the resonance discussion. 【816:4†manuscript_v39.pdf†L68-L70】【816:5†manuscript_v39.pdf†L46-L50】
- Monotonicity under shrink: if \(N_{\rm res}(a,m,\delta_0)=0\) then \(N_{\rm res}(a,m,\delta)=0\) for all \(0<\delta\le\delta_0\). Thus any **κ‑admissible shrink** preserves “no near-resonance,” so the condition is shrink‑safe.
- Current status: v39 does **not** provide any theorem implying \(N_{\rm res}(a,m,\delta_0)=0\) (or even \(O(1)\)) for the actual \(E\); and known unconditional zeta technology does not supply a horizontal separation bound at scale \(\delta_0\) in a fixed height window.

Hence ML‑3 remains open; and within current inputs it is **not forceably provable**.

---

## 5) S6 harness cross‑check (explicit formula interpretation)

**Frame mapping (locked):**  
\(s=\beta+i\gamma\), \(u=2s\), \(v=u-1\).  
An off‑axis zero \(s=\beta+i\gamma\) corresponds to \(v=(2\beta-1)+i(2\gamma)=a+im\).

- **Amplitude leak:** in the explicit formula for \(\psi(x)\), a zero at \(\beta+i\gamma\) contributes a term with magnitude \(\asymp x^\beta\) (times oscillation \(e^{i\gamma\log x}\)). Thus \(a=2\beta-1>0\) corresponds to an \(x^{(1+a)/2}\) growth leak.
- **Resonance meaning:** “near-resonant quartets” in v39’s defect geometry correspond to **multiple off‑axis zeros with nearly the same ordinate \(\gamma\)** and real parts \(\beta,\beta'\) separated by \(|\beta-\beta'|\asymp \delta\) (in v‑frame: \(|a-a'|\asymp \delta\)). In explicit-formula terms these are multiple leak terms with the **same oscillatory frequency** \(\gamma\log x\) but slightly different growth exponents; their coexistence can create instability in defect-style phase diagnostics even if a single quartet cancels at the aligned point.

---

# MANDATORY PATCH PACKET FORMAT

* **Callsign:** RH-LOCAL  
* **Result classification:** **FAIL (NO‑GO for proving ML‑3 from current v39 inputs)**  
* **Target gaps closed (by ID):** ML‑3 **not closed** (this packet is a decisive *NO‑GO + corrected obligation*)  
* **Target gaps still open (by ID):** **ML‑3 (Resonance control)** remains open; depends on new zeta-specific input or architecture change  
* **Key conclusions (≤5 bullets):**
  1. The δ‑inert mechanism is triggered by δ‑scale near-resonant quartets and is already demonstrated by Lemma 12.7. 【816:4†manuscript_v39.pdf†L3-L58】
  2. The current resonance sum \(\mathcal R_a(m)\) is δ‑blind and cannot control δ‑inertness; thus Remark 12.6 cannot become a theorem as stated without a δ‑aware resonance term/hypothesis. 【816:5†manuscript_v39.pdf†L32-L52】
  3. A δ‑aware resonance indicator \(N_{\rm res}(a,m,\delta)\) exactly captures the geometric trigger (additional quartets within \(O(\delta)\) in real part).
  4. No available v39-local inputs imply \(N_{\rm res}(a,m,\delta_0)=0\) for the actual \(E\); thus ML‑3 cannot be closed within current architecture.
  5. Any v40/v41 plan must either (i) add a new proof input targeting δ‑scale horizontal separation, or (ii) redesign the endpoint so δ‑inert resonance is irrelevant.

* **Paste‑ready manuscript edits (TeX blocks):**

  **(i) Revised definition / new resonance object (add after Def. 12.5):**
  ```tex
  \begin{definition}[Near-resonance count at scale $\delta$]\label{def:near-resonance-count}
  Fix $a\in(0,1)$, $m\ge 10$, and $0<\delta\le a/4$. Define
  \[
    N_{\rm res}(a,m,\delta)
    :=\#\Bigl\{\rho:\ E(\rho)=0,\ |\Im\rho-m|\le 1,\ 0<\bigl||\Re\rho|-a\bigr|\le 2\delta\Bigr\},
  \]
  counting zeros with multiplicity. We say the local window is \emph{$\delta$-nonresonant at $(a,m)$}
  if $N_{\rm res}(a,m,\delta)=0$.
  \end{definition}
  ```

  **(ii) New remark clarifying why $\mathcal R_a(m)$ is insufficient (insert after Remark 12.6):**
  ```tex
  \begin{remark}[Why $\mathcal R_a(m)$ is $\delta$-blind for resonance]\label{rem:Ra-deltablind}
  Lemma~\ref{lem:defect-resonance-nogo} exhibits an even entire $E_\varepsilon$ with a second quartet at
  real part $a-\varepsilon$ (with $\varepsilon\asymp \delta$) such that $\Phi^{\rm def}_{B(0,m,\delta)}(a)\ge c_0>0$
  uniformly in $\delta,\varepsilon$. In that example, however, $\mathcal R_a(m)$ remains $O(1/a)$
  (independent of $\varepsilon$), so the term $\delta a\,\mathcal R_a(m)$ is $O(\delta)\to 0$.
  Therefore any defect-UE inequality of the schematic form in Remark~\ref{rem:defect-UE-target}
  must incorporate a $\delta$-aware resonance control term/hypothesis (e.g.\ $N_{\rm res}(a,m,\delta)$).
  \end{remark}
  ```

  **(iii) Missing Lever box edit (ML‑3 line; replace “bound $\mathcal R_a(m)$” by δ-aware obligation):**
  ```tex
  \item[(ML-3) Resonance control.] Provide a $\delta$-aware resonance control that rules out the
  $\delta$-inert configuration of Lemma~\ref{lem:defect-resonance-nogo}. For example, prove that
  the local window is $\delta_0(m,a)$-nonresonant at every $(a,m)$ (Definition~\ref{def:near-resonance-count}),
  or else replace the defect-UE target by a bound that explicitly depends on the near-resonance count.
  ```

* **Dependencies on other branches:**  
  - **RH-ENVELOPE:** must decide whether ML‑2 “defect UE” will incorporate \(N_{\rm res}\) (δ-aware) or require a separate proved exclusion (R2′).  
  - **RH-FORCE / RH-BRIDGE:** no direct dependency, except that any transfer lemma ML‑1 must specify its δ-regime and thus inherits the δ-aware resonance definition.

* **Referee risk notes (anticipated objections + how addressed):**
  - *Objection:* “You are changing the resonance object; this is drift.”  
    *Response:* The change is forced by Lemma 12.7’s δ‑inert geometry; a δ‑blind sum cannot control a δ‑scale phenomenon. This is a strictly stronger, more faithful statement of ML‑3, not a new endpoint class. 【816:5†manuscript_v39.pdf†L43-L52】【816:4†manuscript_v39.pdf†L27-L33】
  - *Objection:* “Can \(N_{\rm res}\) be proved zero?”  
    *Response:* Not from current v39-local inputs; it requires new zeta-specific horizontal separation/repulsion information (or an architectural redesign that bypasses resonance).
