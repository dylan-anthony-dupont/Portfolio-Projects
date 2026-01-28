# v41 patchlog (relative to v40)

This patchlog records **truth‑latching** changes made in the v41 build.

## 1) Geometry pivot (single active frontier)
- Replaced the v40 “Missing Lever (ML‑Δa)” boxed open statement with the **v41 Geometry Change Requirement** (Box `box:geometry-change-v41`).
- Added an explicit scope remark clarifying that all NO‑GO latches are **endpoint‑ and witness‑family specific** (no global over‑blocking).

## 2) New NO‑GO latch installed (aligned boxes)
- Inserted **Lemma `lem:deltaa-alignedbox-nogo`**: in the toy quartet model the two‑sided shift‑difference endpoint
  \(\Phi^{(2\mathrm{s})}_B(a;h)\) is *not forceable* on the **aligned witness family** \(B(a,m,\delta)\)
  at the nominal micro‑step coupling \(h\asymp\delta\asymp \eta a/(\log m)^2\).
- This is now the definitive reason the aligned‑box ML‑Δa forcing route is archived, and why the frontier is re‑framed as “geometry change required”.

## 3) Hygiene / clarity edits
- Corrected the expanded form of \(\mathcal D_{a,h}\) to the grouped “difference‑of‑differences” expression.
- Updated Executive Proof Status / Abstract to reflect v41 posture and the new single active frontier.

## 4) Archive updated
- Added a new discarded‑routes entry documenting that “ML‑Δa on aligned boxes at nominal coupling” is ruled out,
  and pointing explicitly to the v41 Geometry Change Requirement box as the next frontier.

## 5) Reproducibility pack rollover
- Rolled the audit harness forward to a **v41**‑named repro pack (`v41_repro_pack/`, zipped as `v41_repro_pack.zip`)
  and refreshed `SHA256SUMS.txt`.

