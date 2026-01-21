Understood. I am operating as **RH‑FORCE**, with a single target: **close G‑3 / E‑7** by reconstructing the forcing/allocation constant and reconciling the v31 vs v32 drift. I will stay strictly inside the forcing/allocation mechanism and its constant bookkeeping.

## 1) Reconstruction: where \(K_{\rm alloc}\) comes from and how it is supposed to be frozen

### 1.1 The allocation scheme and parameter \(\lambda\)

The forcing/allocation constant originates in the **vertical Lipschitz allocation** step: you split each vertical side of the box boundary into a **central sub‑arc** of length \(\lambda\delta\) and the remaining **tails** of total length \((2-\lambda)\delta\), and you bound the phase variation lost on those tails by a coefficient times \(\delta \sup_{\partial B} |E'/E|\). This is exactly Lemma “Vertical Lipschitz allocation (L\(^2\))” as already present in the early lineage.

In **v11**, Lemma 4.3 states:

- On each vertical side,
  \[
  \int_{\text{tails}} |\partial_\tau \arg W|\,ds
  \ \le\
  \Big[(2-\lambda) + 2\sqrt{2(2-\lambda)}\Big]\,
  \delta\,
  \sup_{\partial B}\Big|\frac{E'}{E}\Big|.
  \]
- Summing both vertical sides yields
  \[
  \Delta_{\rm cent}\ \ge\ \Delta_{\rm vert}\ -\ K_{\rm alloc}(\lambda)\,\delta\,\sup_{\partial B}\Big|\frac{E'}{E}\Big|
  \quad\text{with}\quad
  K_{\rm alloc}(\lambda):=2\Big[(2-\lambda)+2\sqrt{2(2-\lambda)}\Big].
  \]
- And (crucially) it explicitly permits a **more conservative “stricter” coefficient**
  \[
  K_{\rm alloc}^{\star}(\lambda):=2\Big[(2-\lambda)+4\sqrt{2(2-\lambda)}\Big].
  \]
This “stricter” \(K_{\rm alloc}^{\star}\) is explicitly written in v11. 【456:4†manuscript_v11.pdf†L59-L110】

So: the allocation scheme is parameterized by \(\lambda\in(0,1)\), and the manuscript explicitly defines a **canonical conservative coefficient** \(K_{\rm alloc}^{\star}(\lambda)\) coming from that scheme.

### 1.2 Where the *fixed* number \(3+8\sqrt3\) comes from

Once you **choose** \(\lambda=\tfrac12\), the “stricter” coefficient evaluates to a fixed explicit constant:

\[
K_{\rm alloc}\ :=\ K_{\rm alloc}^{\star}\!\Big(\tfrac12\Big)
=
2\Big[\Big(2-\tfrac12\Big)+4\sqrt{2\Big(2-\tfrac12\Big)}\Big]
=
2\Big[\tfrac32+4\sqrt3\Big]
=
3+8\sqrt3.
\]

This value is already used explicitly by the time you are in the certificate era:

- **v27** fixes \(\lambda=\tfrac12\) and states \(K_{\rm alloc}(\tfrac12)=3+8\sqrt3\) inside the lower‑envelope forcing inequality. 【404:12†manuscript_v27.pdf†L80-L114】
- **v28** carries \(K_{\rm alloc}:=3+8\sqrt3\) into the tail inequality theorem as part of the explicit constants list. 【404:11†manuscript_v28.pdf†L23-L40】
- **v31** freezes it as a numerical constant in the certified tail inequality:  
  “Fix the numerical constants … \(K_{\mathrm{alloc}}:=3+8\sqrt3\)” and the theorem’s RHS uses \(K_{\mathrm{alloc}}c_0L(m)\). 【404:3†manuscript_v31.pdf†L44-L70】

Additionally, v31’s embedded certificate-generation code literally computes it as `Kalloc = 3 + 8*sqrt(3)`. 【456:10†manuscript_v31.pdf†L25-L43】

### 1.3 Where \(K_{\rm alloc}\) enters the tail inequality (the exact insertion point)

In the certified tail inequality form (v31), \(K_{\rm alloc}\) enters only through the **lower envelope / forcing side** as the coefficient of the \(\delta\,c_0\,L(m)\) subtractive term:

\[
2C_{\rm up}\,\delta^{3/2}L(m)
<
c-\delta\Bigl(K_{\rm alloc}c_0L(m)+C_h''(\log m+1)\Bigr).
\]
【404:3†manuscript_v31.pdf†L44-L70】

This is the key: **if \(K_{\rm alloc}\) drifts downward**, the RHS becomes artificially larger, and the tail inequality becomes artificially easier to satisfy.

---

## 2) Drift reconciliation: v31 vs v32

### 2.1 What v31 says (baseline)

v31 sets
\[
K_{\mathrm{alloc}}:=3+8\sqrt3
\]
as a frozen numerical constant and uses it in the certified tail inequality theorem statement. 【404:3†manuscript_v31.pdf†L44-L70】

### 2.2 What v32 says (the drift)

v32’s tail inequality theorem lists the forcing constants as:
\[
c_0:=\frac{3\log 2}{8\pi},\qquad
c:=\frac{3\log 2}{16},\qquad
K_{\rm alloc}:=\frac14
\]
and then uses \(K_{\rm alloc}\) in exactly the same RHS slot:
\[
2C_{\mathrm{up}}\Bigl(\delta^{3/2}L(m)+\delta^{1/2}\frac{N_{\rm up}(m)}{\kappa}\Bigr)
<
c-\delta\Bigl(K_{\rm alloc}c_0L(m)+C_h''(\log m+1)\Bigr).
\]
【404:7†manuscript_v32.pdf†L2-L36】

It then asserts: **“The forcing side is unchanged from v31.”** 【404:7†manuscript_v32.pdf†L2-L36】

Moreover, v32’s embedded certificate JSON reports `derived: { "K_alloc": "0.25", ... }`. 【404:8†manuscript_v32.pdf†L55-L76】

### 2.3 Reconciliation outcome (must choose A/B/C)

There is no documented new allocation scheme, no new \(\lambda\)-choice, and v32 explicitly claims forcing unchanged while changing \(K_{\rm alloc}\) by ~\(67\times\). Therefore:

**Outcome B (definitive): v32 is in error.**  
The correct forcing/allocation constant under the already‑stated allocation scheme and the already‑used choice \(\lambda=\tfrac12\) is
\[
K_{\rm alloc}=3+8\sqrt3,
\]
and v32 must retract/replace \(K_{\rm alloc}:=\tfrac14\).

This closes the “constant provenance” question: **the only consistent reading of your own lineage is that v31’s value is the frozen allocation constant, and v32’s value is a bookkeeping drift.**

---

## 3) Propagation map: where \(K_{\rm alloc}\) flows downstream and why magnitude matters

### 3.1 Direct downstream uses (proof spine)

1. **Tail inequality theorem RHS (core)**  
   The RHS subtractive term contains \(\delta K_{\rm alloc}c_0L(m)\). Smaller \(K_{\rm alloc}\) makes the theorem’s hypothesis easier to satisfy and can create a false “zero‑exclusion” conclusion.  
   - v31: \(K_{\mathrm{alloc}}=3+8\sqrt3\) used here. 【404:3†manuscript_v31.pdf†L44-L70】  
   - v32: \(K_{\rm alloc}=1/4\) used here. 【404:7†manuscript_v32.pdf†L2-L36】

2. **Monotonicity / reduction-to-\(m=10\) bookkeeping (supporting core)**  
   In v31, the derivative/monotonicity argument defines constants \(A,B\) that *depend linearly* on \(K_{\mathrm{alloc}}\). 【404:3†manuscript_v31.pdf†L44-L70】

3. **Certified computation artifacts (audit harness)**  
   The certificate-generation code explicitly computes and uses `Kalloc = 3 + 8*sqrt(3)` in v31. 【456:10†manuscript_v31.pdf†L25-L43】  
   The v32 certificate bundle explicitly reports `K_alloc: 0.25`. 【404:8†manuscript_v32.pdf†L55-L76】

### 3.2 Why sign/magnitude matters (one sentence)

Because \(K_{\rm alloc}\) enters the **subtractive** lower-envelope term, **understating it makes the inequality easier and can “prove” a false exclusion band**—precisely the G‑3 / E‑7 failure mode.

---

## 4) Minimal corrective action: what to change to repair v32

### 4.1 Manuscript-level correction (v32)

Replace the forcing constant line
\[
K_{\rm alloc}:=\frac14
\]
with
\[
K_{\rm alloc}:=3+8\sqrt3 \quad (=K_{\rm alloc}^{\star}(1/2)).
\]

And add a provenance sentence that ties it back to the allocation lemma and the frozen parameter choice \(\lambda=\tfrac12\) (see Patch edits below).

### 4.2 Certificate-level correction (v32 artifact)

Any “derived constants” JSON / code should compute
\[
K_{\rm alloc}=3+8\sqrt3
\]
(or compute \(K_{\rm alloc}^{\star}(\lambda)\) from the formula and then evaluate at \(\lambda=\tfrac12\)), and must not output 0.25.

Given your own certificate note that \(\eta\) is extremely small, this correction is unlikely to break the inequality numerically, but **it must be corrected regardless** because G‑3 is a provenance/soundness requirement.

---

# PATCH PACKET

**Prompt Batch Number:** 1

Callsign: RH-FORCE

Result classification: PASS

Target gaps closed (by ID): G-3 (K\_{\rm alloc} provenance / drift), E-7 (constant drift entry point)

Target gaps still open (by ID): None *within RH‑FORCE scope* (note: tail inequality still depends on other branches’ constants/lemmas, but that is outside this work order)

Key conclusions (≤5 bullets):
- \(K_{\rm alloc}\) is the **allocation coefficient** from the vertical \(L^2\) allocation lemma with parameter \(\lambda\), with an explicitly permitted conservative form \(K_{\rm alloc}^{\star}(\lambda)=2[(2-\lambda)+4\sqrt{2(2-\lambda)}]\). 【456:4†manuscript_v11.pdf†L59-L110】
- With the manuscript’s later fixed choice \(\lambda=\tfrac12\), \(K_{\rm alloc}=K_{\rm alloc}^{\star}(1/2)=3+8\sqrt3\), used in v27/v28/v31 and in the v31 certificate toolchain. 【404:12†manuscript_v27.pdf†L80-L114】【404:3†manuscript_v31.pdf†L44-L70】【456:10†manuscript_v31.pdf†L25-L43】
- v32 changes \(K_{\rm alloc}\) to \(1/4\) while stating “forcing unchanged,” and its certificate reports `K_alloc = 0.25`; this is incompatible with the established provenance. 【404:7†manuscript_v32.pdf†L2-L36】【404:8†manuscript_v32.pdf†L55-L76】
- Therefore the correct reconciliation is: **v32 is in error**; restore \(K_{\rm alloc}=3+8\sqrt3\) (or explicitly document a new allocation scheme—which v32 does not do).
- \(K_{\rm alloc}\) flows into the tail inequality only via the subtractive term \(\delta(K_{\rm alloc}c_0L(m)+\cdots)\); making it too small artificially eases the inequality and can invalidate the RH endgame exclusion logic. 【404:3†manuscript_v31.pdf†L44-L70】

Paste-ready manuscript edits:
(i) revised lemma/proposition statements
- **(Add / restate explicitly in the forcing/allocation section)**  
  *Lemma (Vertical Lipschitz allocation; conservative coefficient).*  
  Let \(\lambda\in(0,1)\). Summing the two vertical sides of \(\partial B\) after removing central sub‑arcs of length \(\lambda\delta\), the retained central vertical gap satisfies
  \[
  \Delta_{\rm cent}\ \ge\ \Delta_{\rm vert}\ -\ K_{\rm alloc}^{\star}(\lambda)\,\delta\,
  \sup_{\partial B}\Bigl|\frac{E'}{E}\Bigr|,
  \qquad
  K_{\rm alloc}^{\star}(\lambda):=2\Big[(2-\lambda)+4\sqrt{2(2-\lambda)}\Big].
  \]
  Fixing \(\lambda=\tfrac12\) gives the frozen numerical constant
  \[
  K_{\rm alloc}:=K_{\rm alloc}^{\star}\!\Big(\tfrac12\Big)=3+8\sqrt3.
  \]

(ii) revised definitions/remarks
- **(Insert into v32 near the constant list in the tail inequality theorem)**  
  *Remark (Provenance and immutability of \(K_{\rm alloc}\)).*  
  The constant \(K_{\rm alloc}\) is not a tunable parameter: it is the explicit coefficient produced by the vertical \(L^2\) allocation scheme with the globally fixed choice \(\lambda=\tfrac12\). Consequently \(K_{\rm alloc}=K_{\rm alloc}^{\star}(1/2)=3+8\sqrt3\) throughout.

(iii) revised theorem/inequality lines
- **v32 Theorem 11.1 constant line:** replace
  \[
  K_{\rm alloc}:=\frac14
  \]
  by
  \[
  K_{\rm alloc}:=3+8\sqrt3.
  \]
- **v32 certificate bundle:** ensure the “derived” constant is computed/recorded as
  \[
  \texttt{"K\_alloc": "3 + 8*sqrt(3)"}\ \text{(exact/symbolic) or its decimal enclosure, not }0.25.
  \]

Dependencies on other branches:
- None for the *value/provenance* of \(K_{\rm alloc}\). (Downstream validity of the tail inequality still depends on residual envelope, horizontal budget, etc., but that is outside RH‑FORCE scope.)

Referee risk notes: anticipated objections + how addressed
- **Objection:** “Maybe v32 changed the allocation scheme, so \(1/4\) is correct.”  
  **Addressed:** v32 explicitly states the forcing side is unchanged while changing \(K_{\rm alloc}\), and gives no new scheme/parameterization; the constant is positioned identically in the tail inequality. Therefore it is a bookkeeping drift, not a documented scheme change. 【404:7†manuscript_v32.pdf†L2-L36】
- **Objection:** “Perhaps \(K_{\rm alloc}\) was redefined (e.g., absorbed into \(c_0\)).”  
  **Addressed:** v32 lists \(c_0,c,K_{\rm alloc}\) separately and still uses the product \(K_{\rm alloc}c_0L(m)\), matching v31’s slot; this is not a mere renaming. 【404:7†manuscript_v32.pdf†L2-L36】