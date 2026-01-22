# Batch 2 — RH-FORCE
**Base (ground truth):** `manuscript_v33.tex` / `manuscript_v33.pdf`  
**Assigned targets:** **G-3 freeze audit** (K\_alloc immutability + propagation) and **G-12** (certificate/theorem interface alignment; sanity-check harness)

---

## Task A (HIGH) — G-3 freeze audit in v33

### A1) Stray-value scan: confirm no `K_{\rm alloc}=1/4` remains in v33

**Scope scanned (per work order):** manuscript text + theorem constant lists + proofs + appendices + embedded repro-pack listings in the PDF.

**Result:**
- No occurrence of **`K_{\rm alloc}:=\frac14`**, **`Kalloc = 0.25`**, or **`0.25`** tied to K\_alloc appears anywhere in `manuscript_v33.tex` or the compiled PDF.
- The only remaining mention of “1/4” is *outside the manuscript* (e.g., historical patchlog language), not in the proof spine.

### A2) Propagation check: confirm `K_{\rm alloc}=3+8\sqrt3` is used everywhere it must be

**(i) Tail inequality constants list (theorem-level):**
- `manuscript_v33.tex` defines the forcing constants as
  \[
  c_0:=\frac{3\log 2}{8\pi},\qquad c:=\frac{3\log 2}{16},\qquad K_{\rm alloc}:=3+8\sqrt3,
  \]
  in the assumptions of **Theorem `\ref{thm:tail-inequality}`** (TeX line ~637; see `\label{thm:tail-inequality}` block).

**(ii) Tail inequality RHS insertion point (the only place the forcing constant matters):**
- In **Eq. `\ref{eq:tail-ineq}`**, the subtractive forcing term is
  \[
  c-\delta\bigl(K_{\rm alloc}c_0L(m)+C_h''(\log m+1)\bigr),
  \]
  and uses the restored `K_{\rm alloc}` (TeX line ~650/681).

**(iii) Absorption coefficient D (low-anchor η-absorption):**
- In the η-absorption section, v33 defines
  \[
  D:=\frac{K_{\rm alloc}c_0L(10)+C_h''(\log 10+1)}{(\log 10)^2}
  \]
  and therefore inherits the restored `K_{\rm alloc}` (TeX line ~777).

**(iv) Certificate scaffold / code / JSON (as printed in Appendix `\ref{app:certificate}` in the PDF):**
- The embedded generator code explicitly computes
  `Kalloc = 3 + 8*sqrt(3)` and records a `Kalloc_interval` in the derived-constants block.
- The printed tail certificate JSON contains `"Kalloc_interval": { "lo": …, "hi": … }` with the correct magnitude (~16.8564…), consistent with `3+8\sqrt3`.

**Conclusion (Task A):** G-3 is not only “fixed in the theorem statement,” it is also **frozen** into the absorption coefficient and the reproducibility scaffold.

---

## Task B (HIGH) — Close G-12 at the interface level (sanity-check harness alignment)

### B1) Inequality checked (exact theorem target)

The v33 sanity-check harness must check **exactly** the tail inequality
\[
\tag{Eq. \ref{eq:tail-ineq}}
2C_{\mathrm{up}}\Bigl(\delta^{3/2}L(m)+\delta^{1/2}\,\frac{N_{\rm up}(m)}{\kappa}\Bigr)
\ <\
 c-\delta\Bigl(K_{\rm alloc}c_0L(m)+C_h''(\log m+1)\Bigr),
\]
from **Theorem `\ref{thm:tail-inequality}`**, evaluated at the **nominal scale**
\[
\delta=\delta_0(m,\alpha)=\frac{\eta\alpha}{(\log m)^2},
\]
with the **low-anchor sanity-check point** `(m,\alpha)=(10,1)` as used by Theorem `\ref{thm:tail-closure}`.

### B2) Harness inputs (constants and parameters)

**Constants file (inputs, interval-enclosed):**
- `C1_interval` (JSON key `intervals.C1`)  → theorem constant `C_1`
- `C2_interval` (JSON key `intervals.C2`)  → theorem constant `C_2`
- `Cup_interval` (JSON key `intervals.C_up`) → theorem constant `C_{\mathrm{up}}`
- `Chpp_interval` (JSON key `intervals.C_hpp`) → theorem constant `C_h''`  
  *(ASCII-safe key: “hpp” corresponds to “h double-prime”)*
- `kappa` (JSON key `kappa`) → theorem parameter `\kappa`

**Parameters (scalar inputs):**
- `m_band` (JSON key `m_band`) → theorem height `m` *(historical name retained; equals 10 in v33)*
- `eta` (JSON key `eta`) → theorem parameter `\eta`
- `alpha_worst` (JSON key `alpha_worst`) → theorem dial displacement `\alpha` *(set to 1 in v33)*

**Hard-coded from the manuscript (not inputs):**
- `N_up(m) = 1.01*log(m) + 17` (from Lemma `\ref{lem:Nloc-logm}` and Sec. `\ref{sec:tail}`)

### B3) Derived constants (computed inside the harness; not user-supplied)

To eliminate interface drift, the harness must compute (with directed rounding):
- `ln2 = ln(2)`
- `c = (3 ln 2)/16`
- `c0 = (3 ln 2)/(8 pi)` using an explicit pi enclosure
- `Kalloc = 3 + 8*sqrt(3)`

This matches the theorem’s “forcing lemma constants list” and prevents “silent constant injection.”

### B4) Outputs recorded (what the harness must emit)

For audit-grade alignment, the harness must record:
- `delta_interval` (computed from `eta, alpha, log(m)`),
- `L_interval`, `Nup_interval`,
- `lhs_interval`, `rhs_interval`,
- `derived_constants.{c_interval, c0_interval, Kalloc_interval}`,
- `pass` boolean defined by **strict separation**: `lhs.hi < rhs.lo`.

### B5) Verifier behavior (alignment + reproducibility)

Minimal verifier contract:
1. Load **constants file** + **pinned certificate JSON**.
2. Regenerate all computed fields from constants.
3. Check exact JSON equality on regenerated fields.
4. Check strict inequality `lhs.hi < rhs.lo`.
5. Print `LHS_hi`, `RHS_lo`, `STRICT`, and `PASS`, and exit 0 on success.

### B6) Overclaim prevention (“sanity-check only”)

v33 already contains the correct posture:
- main-text remark: computations are **not** used in the η-absorption logical closure,
- appendix subsection: certificates prove `LHS < RHS` **given** a constants file, and do **not** certify the constants file.

However, **one interface clarification is still recommended** to make G-12 closure referee-proof: explicitly state that the certificate checks **Eq. (\ref{eq:tail-ineq}) evaluated at** `\delta=\delta_0(m,\alpha)` and identify the JSON-key ↔ notation mapping.

---

## Minimal edits needed (surgical) to close G-12 fully

### Edit 1 — Make the appendix quote explicitly reference Eq. (\ref{eq:tail-ineq}) and δ=δ0
In Appendix `\ref{app:certificate}`, subsection `\ref{app:what-proves}`, the existing quote should explicitly state:
- the inequality is Eq. `\ref{eq:tail-ineq}`,
- δ is computed as `\delta_0(m,\alpha)=\eta\alpha/(\log m)^2`,
- the v33 demo certificate fixes `(m,\alpha)=(10,1)`.

### Edit 2 — Add a short “Interface mapping (notation → JSON keys)” paragraph
Still in subsection `\ref{app:what-proves}`, add a 4–6 line mapping:
- `C_{\mathrm{up}} ↔ C_up`,
- `C_h'' ↔ C_hpp`,
- `m ↔ m_band`,
- `\alpha ↔ alpha_worst`.

### Edit 3 — Remove the accidental coupling “G-12” ↔ “constants correctness” in the demo JSON note
The demo constants JSON printed in the PDF currently says (paraphrasing): “replace with audit-proven enclosures when G-1/G-12 are closed.”
To avoid conflating **alignment** (G-12) with **provenance** (G-1), the note should read: “replace with audit-proven enclosures when **G-1** is closed.”

(If you do not wish to edit the JSON artifact itself in v33, add a manuscript sentence overriding that note: “G-12 refers to interface alignment only; constants provenance is G-1.”)

---

# PATCH PACKET

* Callsign: RH-FORCE
* Result classification: PASS
* Target gaps closed (by ID): G-12 (interface alignment closed with the edits below), G-3 freeze audit (confirmed no stray 1/4 and propagation complete)
* Target gaps still open (by ID): G-1 (constants provenance) — explicitly **not** in RH-FORCE scope
* Key conclusions (5 bullets max):
  1. v33 contains **no** stray `K_{\rm alloc}=1/4` anywhere in manuscript text or embedded repro-pack listings.
  2. `K_{\rm alloc}=3+8\sqrt3` is propagated into the **tail inequality constants list**, the **RHS forcing term**, and the **η-absorption coefficient D**.
  3. The v33 repro scaffold (generator + certificate JSON) computes and records `Kalloc = 3 + 8*sqrt(3)` and a consistent `Kalloc_interval`.
  4. The sanity-check harness implements Eq. (\ref{eq:tail-ineq}) at `\delta=\delta_0(m,\alpha)` with strict separation (`lhs.hi < rhs.lo`).
  5. A small appendix interface-mapping note is sufficient to make G-12 closure referee-proof and prevent misreading the scaffold as proving the constants.
* Paste-ready manuscript edits:
  (i) revised lemma/proposition statements
  - **None required** for RH-FORCE (forcing lemma already frozen by the restored constant list).

  (ii) revised definitions/remarks
  - **Appendix `\ref{app:certificate}` / subsection `\ref{app:what-proves}` (replace the current quote block with the following):**

    > Each tail certificate proves the following statement:
    > 
    > Given a constants file providing interval enclosures for \((C_1,C_2,C_{\mathrm{up}},C_h'',\kappa)\) and chosen parameters \((m,\eta,\alpha)\), the generator evaluates Eq. \(\eqref{eq:tail-ineq}\) at the nominal scale
    > \(\delta=\delta_0(m,\alpha)=\eta\alpha/(\log m)^2\) and produces interval bounds satisfying strict separation
    > \(\mathrm{LHS}_{\mathrm{hi}}<\mathrm{RHS}_{\mathrm{lo}}\).
    > 
    > In the v33 demo bundle we fix \((m,\alpha)=(10,1)\).
    > 
    > It does **not** certify that the constants file provides correct enclosures for the analytic lemmas.

  - **Immediately after the quote (same subsection), add:**

    *Interface mapping (notation → JSON keys).* The repro pack uses ASCII-safe keys:
    \(C_{\mathrm{up}}\leftrightarrow\texttt{C\_up}\), \(C_h''\leftrightarrow\texttt{C\_hpp}\), \(m\leftrightarrow\texttt{m\_band}\) (historical name; equals 10 here), and \(\alpha\leftrightarrow\texttt{alpha\_worst}\).

  (iii) revised theorem/inequality lines
  - **None required** (Eq. \(\ref{eq:tail-ineq}\) is already aligned with the harness).
* Dependencies on other branches:
  - None. (This closes the alignment/freeze interface; proving constants is G-1 and belongs elsewhere.)
* Referee risk notes (anticipated objections + how addressed):
  - **Objection:** “The certificate might check a different inequality than the theorem.”  
    **Answer:** the proposed appendix edits explicitly anchor the certificate to Eq. (\ref{eq:tail-ineq}) and δ=δ0(m,α), and provide key-mapping.
  - **Objection:** “The certificate proves the constants.”  
    **Answer:** appendix language explicitly states the constants file is assumed and not certified; the harness is a sanity check only.
  - **Objection:** “K\_alloc drift could recur.”  
    **Answer:** v33 now computes K\_alloc internally in the generator (not as an input), and the theorem constant list freezes it as `3+8\sqrt3`.
