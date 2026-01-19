# v32 Status / Decision (2026-01-19)

This memo records what was built in v32, what was changed relative to v31, what
was executed in the reproducibility bundle, and what remains to be *fully*
audit-tight.

## Build artifacts produced

- `manuscript_v32.tex`
- `manuscript_v32.pdf` (compiled from the above)
- `v32_repro_pack.zip` (optional sanity-check certificates)

SHA256 (artifacts):

```
f799ec9c729d2c32925225519664b9f8ab86322cfbdeec29c8e4016d7740e9ad  manuscript_v32.tex
f1f5b225cd9546fc2c049f285363f071cf2442a27211a860cae6b0844759a9d5  manuscript_v32.pdf
9bfc784be4d8f3c5d136e2f6e1c87c0081b268107196a3100639de4a29b30e6a  v32_repro_pack.zip
```

## What changed from v31 to v32

### 1) Upper-envelope scope mismatch fixed

- **v31 problem:** the upper-envelope lemma bounded dial deviations of the *inner quotient* 
  \(W := E / G_{\rm out}\) using a bound for \(F'/F\) (the residual after local zero removal). 
  This skipped the local factor contribution to \(E'/E\) and made the stated inequality non-derived.

- **v32 fix:** Lemma `lem:upper-envelope` is rewritten in an **outer-aligned** form:
  \[
    \sum_{\pm} |W(v_\pm)-e^{i\varphi_0^\pm}|\ \le\ 2C_{\rm up}\,\delta^{3/2}\,\sup_{\partial B}\left|\frac{E'}{E}\right|.
  \]
  A subsequent log-derivative split then reintroduces the residual factor \(F\) *plus*
  an explicit **local** term.

### 2) Local-factor collar control made explicit

A new collar-admissibility policy (`def:collar-admissible`) is added:

- Fix \(\kappa\in(0,1/10)\).
- Require \(\dist(\partial B,\mathcal Z(E))\ge \kappa\delta\).
- If violated, shrink \(\delta\) until it holds (zeros are isolated), which only makes the
  tail inequalities easier.

Under \(\kappa\)-admissibility, Lemma `lem:Zloc-logder-collar` gives
\(
\sup_{\partial B}|Z_{\rm loc}'/Z_{\rm loc}|\le N_{\rm loc}(m)/(\kappa\delta)
\), and Lemma `lem:Nloc-logm` bounds \(N_{\rm loc}(m)\ll \log m\).

### 3) Horizontal budget is now audit-grade

The previously placeholder “horizontal nonforce budget” is now defined
(`def:Delta-nonforce`) in terms of the **residual** factor \(F\), and proved
(Lemma `lem:horizontal-budget`) using only
\(\sup_{\partial B}|F'/F|\le C_1\log m + C_2\).

This removes any chance that hidden local-zero contributions leak into the
budget term with an untracked \(\delta^{-1}\) blowup.

### 4) Tail inequality updated with explicit local term

The tail inequality (Eq. `eq:tail-ineq`) becomes
\[
2C_{\rm up}\Big(\delta^{3/2}L(m)+\delta^{1/2}\,\frac{N_{\rm up}(m)}{\kappa}\Big)
\ <\ c-\delta\big(K_{\rm alloc}c_0L(m)+C_h''(\log m+1)\big),
\]
with \(L(m)=C_1\log m+C_2\) and \(N_{\rm up}(m)=A_N\log m+B_N\).

### 5) Post-pivot closure via η-absorption

Section `sec:eta-absorption` now provides a purely analytic “**η-absorption**”
mechanism: because all constants are fixed (and δ-uniform), taking η sufficiently
small forces the inequality at the worst case \((m,\alpha)=(10,1)\), hence for all
\(m\ge 10\) by monotonicity.

## What was executed in the v32 repro pack

The bundle `v32_repro_pack.zip` contains **optional** sanity checks.

Running:

```bash
cd v32_repro_pack
./verify_all.sh
```

produces/updates:

- `v32_tail_certificate_m10.json` and `v32_verifier_output_m10.txt`
- `v32_frontend_certificate.json` and `v32_frontend_verifier_output.txt`

The tail certificate checks the v32 tail inequality over the band
\(m\in[10,10^{18}],\ \alpha\in[0,1]\) for the conservative constants in
`v32_constants_m10.json` (with η = 1e-20) and returns **PASS**.

## Decision

**v32 resolves the principal internal inconsistency identified in v31** (the
upper-envelope scope mismatch) and replaces the v31 “ledger-certification hard
gate” with an **η-absorption** posture.

From a *logical dependency* perspective, the tail no longer requires *numerically*
certifying sharp constants: it only needs that a fixed list of analytic constants
exist and are δ-uniform, after which η can be chosen small enough.

## Remaining audit obligations (what to certify next)

Even after this build, the following items should be made maximally explicit in
order to be “external-audit ready” without relying on informal knowledge:

1. **Pin down primary references / theorem statements** for the boundedness of the
   boundary conjugation operator on the square and the corresponding outer-factor
   estimates (CMM / Hardy space references). The manuscript now cites these, but
   can be strengthened by giving a theorem number and a one-paragraph mapping from
   the cited result to the operator \(H_{\partial Q}\) used here.

2. **Residual envelope lemma proof completeness:** Lemma `lem:residual-envelope`
   is still a proof sketch. To make this watertight, expand it to a full proof
   (or cite a single primary result) that yields
   \(\sup_{\partial B}|F'/F|\le C_1\log m+C_2\) uniformly in \(\delta\) and \(\alpha\).

3. **Collar policy integration:** The “shrink δ until κ-admissible” step should be
   checked against every place δ is used (forcing lemma, allocation budgets, etc.),
   ensuring that shrinking δ never invalidates a hypothesis.

If (1)–(3) are fully written out (with theorem-level citations where used), then
v32's tail mechanism is positioned to be **unconditional in the tail** (computer-
assisted only in the finite-height front-end).
