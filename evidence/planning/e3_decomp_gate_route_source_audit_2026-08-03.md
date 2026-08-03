# Corpus audit: `modulatory_channel_route_source` x `e3_score_decomp_enabled` silent-no-op

**Generated:** 2026-08-03T12:58:33Z
**Session:** `metaworker-chip-20260803-e3-decomp-gate-corpus-audit` (`[chip_ref: chip-20260803-e3-decomp-gate-corpus-audit]`)
**Bases audited:** `ree-v3` `be5f93b3` (working tree + full history), `REE_assembly` `cd659a3b07`
**Scope:** the blast-radius question left open as item 1 of Section 8 ("Not investigated this session") in
`failure_autopsy_V3-EXQ-863-route-decomp-gate_2026-08-02.md`.

## 0. Headline

**The blast radius is exactly three runs, and they are the three already known.** Across the *entire*
committed history of `ree-v3/experiments/` — 3,923 unique file versions — only **four** driver scripts have
ever set `modulatory_channel_route_source` to one of the four decomp-gated channels, all four to
`lateral_pfc`, all four inside the ARC-062 GOV-FANOUT-1 lineage of 2026-07-31 -> 2026-08-02.

| Run | Route source | `e3_score_decomp_enabled` | Route actually fired? | Verdict |
|---|---|---|---|---|
| **V3-EXQ-851** | `lateral_pfc` | **not set** | **No** — 0.0 on all 6 cells | **AFFECTED** (claim-tagged) |
| **V3-EXQ-859** | `lateral_pfc` vs `none` | **not set** | **No** — 0.0 on all 6 cells | **AFFECTED** |
| **V3-EXQ-863** | `lateral_pfc` vs `none` | **not set** | **No** — 0.0 on all 6 cells | **AFFECTED** (already re-adjudicated) |
| **V3-EXQ-858** | `lateral_pfc` | **set** (line 694) | **Yes** — up to 0.1296 | **CLEARED** |

Two results that are new relative to the 863 autopsy:

1. **V3-EXQ-858 is CLEARED.** The 863 autopsy's Section 7 flagged 858 as *"likely affected by the identical
   wiring defect"* and recommended it remain suspended pending a targeted check. That check is done here and
   comes back negative: 858 sets `agent.e3.e3_score_decomp_enabled = True` per cell, and its manifest shows
   genuinely live routing. **858's f_weight ladder is not invalidated by this defect.**
2. **`curiosity`, `gated_policy` and `mech295` have never been used at all** — not in any driver, at any point
   in the repo's history. Every apparent hit is docstring prose describing the P-A erratum. So three of the
   four gated channels carry zero historical exposure, and the *entire* realised blast radius of a coupling
   that has existed since V3-EXQ-571 (2026-05-16) is the 48 hours of the ARC-062 P-A/P-B lineage.

## 1. The coupling, restated precisely

Confirmed independently against `ree-v3/ree_core/agent.py` at `be5f93b3` (this reproduces the 863 autopsy's
Section 1c trace; line numbers are current-base):

| Route source | Backing local | Assignment site | Gated on decomp? |
|---|---|---|---|
| `lateral_pfc` | `_bdc_lpfc` | `agent.py:6718-6719` | **YES** |
| `gated_policy` | `_bdc_gp` | `agent.py:6530-6531` | **YES** |
| `mech295` | `_bdc_m295` | `agent.py:6909-6910` | **YES** |
| `curiosity` | `_bdc_curiosity` | `agent.py:6997-6998` | **YES** |
| `coherence` | `_bdc_coherence` | `agent.py:7460-7461` | no — gated on `_tp_bias is not None` |
| `cand_world_summary` | built in-branch | `agent.py:7611-7617` | no — separate code path |

All eight `_bdc_*` locals are initialised to `None` at `agent.py:6193-6204` and assigned only inside
`if self.e3.e3_score_decomp_enabled:` blocks. The routing dispatch at `agent.py:7607-7635` reads those same
locals and applies `project_channel_range` only under `if _route_repr is not None`. With the flag off, the
selected channel's local is still `None`, `channel_route_bias` stays `None`, and the configuration is
functionally **identical to `route_source="none"`** — silently, with no warning and no error.

`e3_score_decomp_enabled` defaults `False` (`e3_selector.py:424`) and has **no `REEConfig` field**; the only
way to set it is a post-construction `agent.e3.e3_score_decomp_enabled = True` statement. So the failure mode
is not "someone passed the wrong value" — it is that the correct configuration requires an undocumented second
statement in an unrelated part of the driver.

## 2. Method

Two independent passes, deliberately chosen so that neither's blind spot is shared by the other.

**(a) Driver-side AST audit, over all of history.** `ast`-parsing rather than grep, because every
`gated_policy` / `curiosity` / `mech295` occurrence in this corpus is *docstring prose* and a textual scan
reports 4 false positives on `gated_policy` alone. The scanner resolves module-level string constants (the
`MODULATORY_CHANNEL_ROUTE_SOURCE = "..."` idiom used by most drivers), `str(...)` wrappers, ternaries and
dict-literal arm specs, and records every value ever bound to `modulatory_channel_route_source`,
`use_modulatory_channel_routing` and `e3_score_decomp_enabled`.

Run over (i) the current working tree — 71 of 1,271 drivers reference the key — and (ii) **every unique blob
of every `experiments/*.py` ever committed on any ref: 3,926 commit/file pairs, 3,923 distinct versions.** The
historical pass is what rules out the "driver was edited after it ran" hazard, which the working-tree pass
alone cannot see.

Every route value in the corpus resolved to a literal; the only unresolved expressions were per-arm dict
lookups inside 859/863, both already flagged by other means.

**(b) Manifest-side sweep, driver-independent.** All 38 manifests in
`REE_assembly/evidence/experiments/` mentioning `modulatory_channel_route*` were scanned for declared route
source and for `modulatory_channel_route_range_{mean,max}`. This pass does not consult the drivers at all, so
it would catch an affected run whose driver has since been deleted, renamed, or rewritten.

**The two passes agree exactly**: 4 manifests declare a gated route source, 3 read exact 0.0 everywhere, and
no manifest with an *ungated* source reads all-zero. Nothing is visible to one pass and not the other.

### Route-source values ever used, corpus-wide

| Value | Current drivers | Gated? | Ever run |
|---|---|---|---|
| `cand_world_summary` | 65 | no | yes |
| `lateral_pfc` | 4 | **YES** | yes — the 4 runs above |
| `coherence` | 2 | no | yes |
| `none` | 2 | n/a | yes |
| `gated_policy` / `curiosity` / `mech295` | **0** | **YES** | **never** |

## 3. The manifest signature, and an important caveat about reading it

`modulatory_channel_route_range` is initialised to `0.0` at `e3_selector.py:2702` and overwritten only when
`channel_route_bias is not None` (`:2704-2712`). A dead route therefore emits exact `0.0` — not small, not
noisy, exactly zero — on every tick of every cell.

**But exact 0.0 in a single cell is not by itself diagnostic.** V3-EXQ-858, which routes correctly, still
reads exactly 0.0 in 2 of its 12 cells (ARM_F100 and ARM_F050 at seed 42) — a live channel can legitimately
produce no cross-candidate spread on a given seed. The signature that identifies the defect is **exact 0.0 on
every cell of every arm and every seed**, and it is confirmed only in combination with the driver-side check.
Recorded explicitly because a future reader scanning manifests for isolated zeros would generate false
positives on clean runs.

Observed:

| Run | Cells | `route_range` |
|---|---|---|
| 851 | 6 | 0.0 x 6 (`route_ready: False`; its own C1g gate measured 0.0 vs threshold 2.0) |
| 859 | 6 | 0.0 x 6 |
| 863 | 6 | 0.0 x 6 |
| 858 | 12 | 0.0 x 2, else 5.2e-05 -> 0.1296 (10/12 live) |

## 4. New evidence: 859 and 863's arms are bit-identical, field by field

The 863 autopsy inferred from the code trace that the manipulation never fired. That inference is now
confirmed **empirically and independently of the code**, by comparing the two arms' recorded results at
matched seeds:

| Run | Seeds | Measured fields identical ARM_LPFC vs ARM_NONE | Fields differing |
|---|---|---|---|
| V3-EXQ-859 | 42, 43, 44 | **15 / 15, all three seeds** | 2: `modulatory_channel_route_source` (the declared label) and `arm_fingerprint` (a hash that folds the config in) |
| V3-EXQ-863 | 42, 43, 44 | **17 / 17, all three seeds** | same 2 |

Not one measured quantity differs between treatment and control, at any seed, in either experiment. The only
two differing fields are the config string itself and a hash of it. Both experiments were built specifically
to contrast `lateral_pfc` against `none`; the two arms were the same arm.

This closes the ambiguity the 863 autopsy correctly identified — bit-identical arms are equally consistent
with "no effect" and with "no manipulation" — from the other direction. A genuine null with 350 episodes/cell
across 3 seeds would not reproduce *every* metric to the bit.

## 5. Findings, in priority order

**F1 — V3-EXQ-851's confirmed autopsy rests on an attribution that this audit invalidates. Re-adjudication
owed.** `failure_autopsy_V3-EXQ-851_2026-08-01.md` is `confirmed` and reads the 654j -> 851 contrast as an
effect of *which channel is routed* ("the only design change is the route-source change", §2/§3). The change
from `cand_world_summary` to `lateral_pfc` was in fact a change from a **live** route to **no route at all**
— 654j used the one gated-exempt value. The observed MECH-448/449 duty-cycle reduction (~24-58% vs ~100%,
per that autopsy's own 21:19Z addendum) is therefore real and deterministic, but its cause is **loss of
modulatory channel routing**, not the lateral-PFC channel. This is the only affected run carrying claim tags.

**F2 — V3-EXQ-859's confirmed autopsy is likewise built on a null that never existed.** Not claim-tagged, and
859 is superseded in practice by 863, so the exposure is narrative rather than evidential — but its
`confirmed` status currently asserts a route-source result that Section 4 shows was never measured.

**F3 — V3-EXQ-858 is cleared, and the 863 autopsy's open recommendation on it can be closed.** 858 sets the
flag at driver line 694 and routes live. Worth noting *why* it is clean: the line is annotated
`# populates _last_traj_components (C1h)` — it was added for an unrelated instrumentation need, not because
its author knew routing depended on it. **858 is correct by accident.** That is evidence about the coupling's
severity, not reassurance: the one driver in the family that got it right did so for the wrong reason.

**F4 — the recommended substrate fix has not been queued.** The 863 autopsy's
`recommended_substrate_queue_entry.action: create` was user-confirmed on 2026-08-02 ("Confirm and land
as-is"), but `evidence/planning/substrate_queue.json` (140 entries) contains no entry for decoupling
`_bdc_*` population from `e3_score_decomp_enabled`, and neither `igw_routine_ledger.json` nor
`igw_assignments.json` mentions it. The defect is still live in the substrate at `be5f93b3`.

**F5 — no forward exposure in the queue right now.** `ree-v3/experiment_queue.json` holds 1 item and no
pending entry uses a gated route source. The exposure is entirely historical *provided* F4 is closed before
any new experiment reaches for one of these four values.

## 6. Claim-layer exposure

Only V3-EXQ-851 is claim-tagged: `claim_ids = ['MECH-309', 'ARC-062']`. Both entries in
`claim_evidence.v1.json` (`entries[5210]`, `entries[5211]`) carry `evidence_direction: non_contributory`, so
**no claim confidence was moved by this run and no revert is owed.** `ARC-062` is `candidate` /
`v3_pending: true`; `MECH-309` is `candidate`. 858, 859 and 863 all carry `claim_ids: []` by the lineage's
diagnostic convention.

The exposure is therefore **narrative, not numeric**: a `confirmed` autopsy feeds a causal story forward into
the ARC-062/MECH-309 reasoning chain, and that story is wrong about the mechanism. Re-adjudication should
correct the routing and the `evidence_quality_note`; it should not touch claim confidence.

## 7. Recommended follow-on

1. **Re-adjudicate V3-EXQ-851** (`/failure-autopsy`) — F1. Highest priority: it is the only claim-tagged
   affected run and its autopsy is `confirmed`. The substantive question its re-adjudication should answer is
   whether the duty-cycle reduction attributable to *routing loss* is itself an ARC-062-relevant finding.
2. **Re-adjudicate V3-EXQ-859** (`/failure-autopsy`) — F2, lower priority, no claim exposure.
3. **Queue the substrate fix** — F4. Populate `_bdc_lpfc` / `_bdc_gp` / `_bdc_m295` / `_bdc_curiosity`
   unconditionally for routing, gating only the diagnostic *exposure* (`last_score_decomp`, component
   trackers) behind `e3_score_decomp_enabled`; or at minimum raise when a gated route source is selected with
   the flag off. A contract test pinning "gated route source + flag off -> raises" would convert this class of
   defect from silent to loud.
4. **Un-suspend V3-EXQ-858 on its own merits** — F3. This audit removes the wiring-defect objection; whether
   it resumes is a separate question for its own autopsy's routing.
5. **Reinstate the route-range readiness gate** in any successor. 851 carried a C1g gate that caught this
   correctly and self-routed `substrate_not_ready_requeue`; 859 and 863 dropped it and could not self-catch.

Items 1-2 are `/failure-autopsy` work and are reported inline rather than chipped, per CLAUDE.md Session Land
Protocol step 6. Items 3-5 are governance-ratified routing decisions arising from an autopsy recommendation
and belong to `/governance` Step 2b/4/6a.

## 8. Scope and limits, stated honestly

- **Audited:** `ree-v3/experiments/` only — working tree plus complete git history, all refs. This is where
  the chip scoped the question and where the config field exists.
- **Not audited:** `ree-v2`, `ree-v1-minimal`, `REE_convergence`, `REE_OpenClaw` are not cloned in this
  worker's checkout. `modulatory_channel_route_source` is a V3 `REEConfig` field with no counterpart in the
  V1/V2 substrates, so cross-repo exposure is expected to be nil — but it was **not verified**, and that is a
  gap rather than a conclusion.
- **Not audited:** experiment code that sets the route source from outside `experiments/` (e.g. a `_lib`
  helper taking it as a parameter). The one `_lib` file referencing the key
  (`_lib/baselines/exq700_arc108_settling_baseline.py`) uses `cand_world_summary` and is unaffected.
- **The AST scanner cannot see** a value assembled at runtime from a non-literal expression. No such case
  exists in the current corpus; the assertion is that none was found, not that none can exist.

## 9. Reproducing this audit

The scanner is not committed — it is a one-shot corpus query, not standing tooling. Its logic:
`ast.parse` each driver, resolve module-level string constants, collect every value bound to
`modulatory_channel_route_source` via kwarg / dict-literal / attribute-assignment, and cross-check against
`e3_score_decomp_enabled` assignments. For the historical pass, enumerate
`git log --all --name-only --diff-filter=AM -- experiments/`, dedupe by blob sha, and scan each version.

The cheap standing check, if F4's contract test is not built: any manifest whose
`modulatory_channel_route_range_mean` is exactly 0.0 in **every** cell while declaring a route source other
than `none` is affected. See Section 3's caveat before applying it to a single cell.
