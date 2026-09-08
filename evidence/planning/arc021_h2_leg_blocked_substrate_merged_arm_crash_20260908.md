# ARC-021 channel-separation portfolio, H2 (real-stack merge) leg -- NOT QUEUED, `blocked_substrate`: the MERGED arm does not run on the current substrate

**Status: NOT QUEUED. No new EXQ number consumed, no driver authored, no queue entry, no coordinator row.** Stopped at `/queue-experiment` Step 2.5a (empirical premise check) and, independently, Step 2.5c (open `corrupting` substrate-path overlap). The reproducer is landed at `ree-v3/experiments/_scratch/arc021_h2_merged_optimizer_runnability_probe.py`. A governance flag (`evidence_discrepancy`, ARC-021 / MECH-069) carries the follow-on.

- **Written:** 2026-09-08T16:19:13Z
- **Session:** `w5-s2a-queue-fill-20260908` (Mac `DLAPTOP`, main checkout), campaign W5-S2a item 3 (`chip-20260905-exq993a-arc021-portfolio`).
- **Authority:** the chip's own terms -- *"Substrate-readiness is YOUR call: if the real E1/E2/E3-stack merge cannot run on the current substrate, mark the backing proposals ... `blocked_substrate` with durable keys and stop."*

---

## 1. The finding

`failure_autopsy_V3-EXQ-993a_2026-09-05`'s H2 probe sketch is explicit that the leg must **start from the existing driver** `ree-v3/experiments/v3_spark_arc021_three_loop_scale.py` ("START FROM THE EXISTING DRIVER, DO NOT AUTHOR A FOURTH"), lists six mandatory repairs, and then says in terms:

> "RUNNABILITY IS UNVERIFIED, and the artifact says so rather than implying otherwise: every agent method the spark calls resolves by NAME against the current `ree_core/agent.py` ... but SIGNATURES were not checked and the file has never executed. **A smoke run against current agent.py is the FIRST step of this leg, not an afterthought.**"

That smoke run was performed. **The MERGED arm -- the ablation itself -- crashes on its second step, deterministically.**

```
SEPARATE (three independent optimizers)                 -> 4/4 steps clean
MERGED   (one optimizer over agent.parameters(),
          combined loss E1 + E2 + E3)                   -> CRASH on step 1

RuntimeError: one of the variables needed for gradient computation has been
modified by an inplace operation: [torch.FloatTensor [16, 256]], which is
output 0 of AsStridedBackward0, is at version 1; expected version 0 instead.
```

**Mechanism, pinned with `torch.autograd.set_detect_anomaly`.** The `[16, 256]` tensor is the learnable parameter `e1.context_memory.memory` (`ree_core/predictors/e1_deep.py:127`, `nn.Parameter(torch.randn(num_slots, memory_dim) * 0.01)`). `ContextMemory.write` mutates it **in place through `.data`** (`e1_deep.py:272-273`):

```python
self.memory.data[min_idx] = 0.9 * self.memory.data[min_idx] + 0.1 * write_signal.mean(0)
```

which advances the parameter's autograd version counter. The anomaly traceback names the invalidated forward as the **previous environment step's** `_e1_tick` -> `E1Deep.forward` -> `generate_prior` -> `ContextMemory.read` -> `value_proj(memory)` (`agent.py:5878`; `e1_deep.py:1741`, `:1002`, `:226`). The merged arm's combined loss therefore retains a graph that reaches back across an env step into a read of `self.memory`, and the in-place write invalidates it before `backward()`.

**Why only the merged arm, and why this is not a driver bug.** The SEPARATE arm backwards each of its three losses immediately and independently, so no graph survives long enough to be invalidated. The MERGED arm is *defined* by the opposite property -- one backward over a combined objective spanning all three modules. The entanglement is therefore intrinsic to the manipulation under test. `self.memory` is a learnable parameter inside `ree_core`; excluding it from the merged optimizer, or wrapping the write in `torch.no_grad()`, would change what the MERGED arm **is**, and the merged arm is the ablation. A `/queue-experiment` session cannot repair this from the driver.

## 2. Step 2.5c reaches the same stop independently

`ContextMemory.write` is the sole `substrate_paths` entry of substrate-queue item **`contextmemory-write-path-addressing-degeneracy`**: `severity: corrupting`, `status: implemented_pending_validation` -- which the gate counts as **OPEN** ("any status containing `pending` is still OPEN -- the substrate landed but is unconfirmed, exactly the window a corrupting defect is most likely still live in"). The H2 leg's driver imports and exercises that exact path. Step 2.5c's rule for a `corrupting` overlap is: do not write the script, do not add a queue entry, route to `/implement-substrate`, stop.

**The two defects are DIFFERENT, in the same function.** That entry concerns hard-argmin addressing degeneracy (a deterministic single-slot fixed point under a low-variance query stream). This is an autograd-version violation under a merged objective. So section 1 is a **new** finding, not a restatement -- and it is one nothing currently audits: no contract exercises a merged-optimizer backward over `agent.parameters()`.

Also worth recording alongside, from the campaign brief's standing carry-forward: the write-content harness trains `write_addr_tagger` on **detached** buffered latents, so `latent_stack` never receives gradient (LINEAGE bit-identical to UNTRAINED_ENCODER, 8/8 seeds, V3-EXQ-970/971/972/970a). That is a third, independent gradient-plumbing problem in the same module. Three distinct defects now cluster on `ree_core/predictors/e1_deep.py`'s memory path.

## 3. What this does and does not decide about ARC-021

**It decides nothing about the claim.** The H2 leg is the one the autopsy calls "the highest-value leg (it is the claim's own named test)" and "the one thing 993a did not do". It remains undone. ARC-021's necessity half is untested on the real stack.

Registry question `arc021_channel_separation_necessity`, all four legs still `alive`:

| leg | axis | `adjudicating_runs` | state after this session |
|---|---|---|---|
| `H-surrogate-trunk-merge-degrades` | -- | `["V3-EXQ-993a"]` | unchanged |
| `H-encoder-level-merge-degrades` (H1) | drive | `[]` | unchanged -- **not blocked** (see below) |
| `H-real-stack-merge-degrades` (H2) | representation | `[]` | **blocked_substrate** by this finding |
| `H-submargin-degradation-exists` (H3) | measurement | `[]` | unchanged -- **not blocked** (see below) |

`adjudicating_runs` left untouched: nothing was queued, and writing a run id that does not exist is the failure mode that field exists to prevent.

## 4. What is owed

1. **Substrate (the blocker).** `ContextMemory.write`'s in-place `.data` mutation of a learnable parameter must be made compatible with a retained cross-step graph -- or `ContextMemory`'s write path must be made explicitly non-differentiable in a way the merged objective can tolerate. This is `/implement-substrate` work on `ree_core/predictors/e1_deep.py`, and it plausibly belongs as an **amend to `contextmemory-write-path-addressing-degeneracy`** (same function, and that entry is already open and `corrupting`) rather than as a new entry -- but that is governance's call at `/governance` Step 6a, not this session's. The governance flag names it.
2. **The two portfolio legs that are NOT blocked.** Neither needs the merged real stack, so the portfolio is not dead -- only its most valuable leg is parked:
   - **H3 (measurement axis)** is the cheapest and needs no substrate at all: a sub-margin-sensitive re-pose of the **existing 993a design** -- `>= 16` seeds, paired variance reduction (shared P0, common random numbers across arms), pre-registering **0.05** rather than 0.15, with the criterion stated as a **confidence interval on the paired mean** rather than threshold-plus-sign-consistency. Declared null: the 95% CI on the paired mean excludes -0.05 in both conditions. This directly answers the power problem the autopsy quantified (joint ~12% at -0.15 on n=4).
   - **H1 (drive axis)** runs the 993a surrogate two-arm design with the **encoder unfrozen and jointly optimised in P1**, localising any effect to representation learning. It does not require a merged optimizer over the whole agent, so the crash above does not apply -- but its runnability must be smoke-tested on the same principle before queuing.
   - When designing either, honour the autopsy's other binding constraints: read **both** ARC-021 falsifier DVs (`calibration_gap` AND attribution accuracy -- 993a read only the first), and do **not** declare `dv_bounds: [0.0, 1.0]` for `calibration_gap`, which is a difference of mean logit differences and is unbounded below (the 993a red-team's F4; the 993a driver's own lines 203-205 say so).
3. **Proposals.** `EXP-0008` (ARC-021) and `EXP-0006` (MECH-069) in `experiment_proposals.v1.json` are both already `executed`, `executed_by: V3-EXQ-993a`. They were **deliberately left untouched**: overwriting an `executed` status with `blocked_substrate` would erase a true record of a run that did happen, and the chip's "mark the backing proposals blocked_substrate" instruction was written on the assumption they were still open. The honest representation is this record plus the governance flag; if governance wants a durable `blocked_substrate` key it should open a NEW proposal for the H2 leg specifically (which the chip anticipated: "open a new proposal if needed").

## 5. Reproducer

`ree-v3/experiments/_scratch/arc021_h2_merged_optimizer_runnability_probe.py` -- writes nothing, ~20 s, runs both arms for 4 steps with the spark driver's own env kwargs, config and train-step bodies, and reports `SEPARATE runnable: True / MERGED runnable: False`. Its module docstring carries the full mechanism and the source citations. Run it before assuming the substrate has been fixed.
