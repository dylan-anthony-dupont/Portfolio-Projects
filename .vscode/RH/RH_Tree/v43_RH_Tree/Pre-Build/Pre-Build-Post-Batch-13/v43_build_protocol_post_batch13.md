# v43 Build Protocol (pre-build, post Batch 13)
Date: 2026-01-30

## Objective
Produce a v43 manuscript where:
- GEO‑C4 endpoint + forcing chain is unchanged (locked),
- The **only active OPEN statement** is `UE‑INPUTᴴ¹(D)` (channel-compatible),
- The old v42 UE‑INPUT is demoted with a proof-grade NO‑GO explanation.

## Inputs
- `manuscript_v42.tex` (locked baseline)
- Batch 13 integration notes + patch queue (this pre-build package)

## Steps (deterministic)
1. **Create branch copy**
   - Duplicate `manuscript_v42.tex` → `manuscript_v43.tex`.

2. **Apply P0 patches**
   - Insert NO‑GO lemma immediately before UE section.
   - Replace UE‑INPUT box text.
   - Replace UE reduction lemma (IBP → L¹ bridge).

3. **Apply P1 patches**
   - Move old UE‑INPUT to appendix or “over-strong interface” subsection.
   - Add baseline lemma + “why too weak” paragraph.

4. **Sanity audit (must pass)**
   - Paper still has one closure chain: FORCE + UE ⇒ contradiction.
   - Verify the UE interface uses only the required admissibility (4 shift traces).
   - Ensure no corridor `t∈[a-h,a+h]` assumptions remain in the active box.

5. **Compile + verify**
   - Run LaTeX build.
   - Verify labels: `box:ue-input-v43` (new) resolves; old `box:ue-input-v42` is either removed or moved.

6. **Update dashboards**
   - Update CR dashboard: only open item is UE‑INPUTᴴ¹(D).

## Acceptance criteria (v43 pre-build quality gate)
- **Clarity:** UE lever is stated in one line, with explicit quantifiers.
- **Non-circularity:** NO‑GO lemma removes appearance of “smuggling RH” through pointwise bounds.
- **Convergence:** The manuscript is strictly simpler than v42 in the UE section (fewer derivatives, fewer assumptions).

