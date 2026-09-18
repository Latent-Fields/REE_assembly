---
status: candidate/v3_pending
status_asof: 2026-09-18
status_claim: MECH-566
---

# Objective -> consumer transfer mechanisms

**Status:** stub. Three `candidate` claims, no experimental evidence, no build licensed.
**Registered:** 2026-09-17, CDQ-010 Mine+Register (Convergence Demand Pipeline, plan of record
`evidence/planning/convergence_demand_pipeline_plan.md` s.5 steps 2-3).
**Claims:** [`MECH-566`](../claims/claims.yaml), `MECH-567`, `MECH-568` -- all wired into
`SD-106.depends_on`.

## The measured gap this page exists for

`failure_autopsy_V3-EXQ-1023a_2026-09-17` (confirmed, ratified REE_assembly `eeeb0550ed5`,
adjudicated `weakens` by cycle `governance-20260917`):

| quantity | 12 epochs | 40 epochs (3.3x) | delta |
|---|---|---|---|
| `sd106_preservation_holdout_r2` (the objective) | 0.7318 | 0.8501 | **+0.1184**, still rising |
| consumer `oracle_action_agreement` (the DV) | 0.7192 | 0.7273 | **+0.0081** |

Shortfall to the 0.85 bar: 0.1227. Observed transfer slope **0.068** agreement per unit R^2 against a
PCA-anchored **3.4655** -- a **~50x** shortfall. `H-transfer-amplification` FALSIFIED; the
training-budget branch CLOSED. The autopsy's own summary: **"the lever is not spent; it is not
connected."**

The anchor that makes this a transfer question rather than a capacity question: **PCA-32 clears the
same bar at the same width on 3/3 seeds** (0.8771 / 0.8578 / 0.8702) while explaining 99.84% of
`world_obs` against SD-106's 0.9974. Two codes at near-identical preserved variance, 0.14 apart at the
consumer.

## Why a mechanism and not another locus

The frozen registry question `zworld_actor_adequacy_locus`
(`evidence/planning/hypothesis_space_registry.v1.json`) carries 11 legs, four confirmed, and **every
leg names a LOCUS at which adequacy is lost**. None names a transfer failure between an *adequate*
objective and its consumer. That shape mismatch is the `GOV-HOTHER-1` `h_other_events` entry with
`response=rotation` recorded on that question the same day. CDQ-010's completion criterion required a
mechanism for exactly this reason.

## The three claims

| Claim | Mechanism | Cheapest falsifying step |
|---|---|---|
| **MECH-566** | The preservation loss is **exactly invariant to GL(32) on the code** (freely-trained linear decoder absorbs any reparameterisation), so the objective cannot see conditioning -- the one property the consumer's learnability depends on. PCA-32 is the well-conditioned representative of the *same* orbit. | **ZCA/whitening on the frozen latent.** Changes no information, leaves preservation R^2 exactly unchanged, needs no retraining. Decisive both ways. |
| **MECH-567** | The objective contains **no term carrying the consumer's target**. MuZero trains the encoder only through consumer heads (and needs an MCTS-*improved* target to avoid a degenerate fixed point); DreamerV3 carries the consumer's **target, not gradient**, via reward/continue auxiliary heads. | Auxiliary `oracle_action` CE head on the same latent during P0a, with preservation R^2 held at or below 0.8501. |
| **MECH-568** | A task-aligned term that *is* present gets **crowded out**; protection must be a **saturating floor** (free bits), not a weight ratio. REE's crowding curve is already measured. | Log **per-term gradient-norm shares** at the P0a operating point. Cheap, no substrate change, and can weaken the claim before anything is built. |

### The invariance argument, stated once

SD-106's preservation term is `||W f(x) - x||^2 / var` with `W` a freely-trained linear decoder in the
same optimiser as the encoder (`ree-v3 ree_core/latent/zworld_p0.py:550-614`). For any invertible `A`,
`(A.f, W.A^-1)` attains an **identical** loss. The substrate's own comment cites Baldi & Hornik (1989)
-- "with a linear decoder the MSE optimum IS the principal subspace" -- and that theorem gives the
principal **subspace** only up to an arbitrary invertible transformation, never the principal
**components**. The objective is therefore blind to where in that orbit it lands; the consumer is not.

**The counterweight, recorded:** REE does carry partial conditioning pressure -- the VICReg variance
term (80.3% of trained loss share) and covariance term (9.3%). But the variance term is a **one-sided
floor**, `mean relu(gamma - std_j)`, with no cap on anisotropy above the floor, and decorrelation is
not equalisation. If measured condition numbers come back comparable to PCA-32's, MECH-566 is weakened
before its whitening test is run.

## Relation to CDQ-007 -- the mine's finding is that they do NOT share a mechanism

CDQ-010's row instructed that if the two rows share a mechanism it be registered once and wired into
both. **They do not.** `MECH-459` (CDQ-007) locates its failure in the **return pathway** -- two
stacked two-sided normalisers forming a scale-invariance operator. MECH-566 locates its failure in the
**encoder objective** -- GL-invariance of a jointly-trained reconstruction loss. Different operator,
different pathway, different falsifier.

What they share is a **family resemblance and a diagnostic habit**: *an invariance sitting between a
lever and a consumer annihilates the lever, so a "this lever is exhausted" conclusion should be
preceded by a check for one.* Both autopsies reached that conclusion independently. It is recorded
here and in both claims' notes rather than registered as a merged claim, because a single claim
spanning both would have no single falsifier.

## What is NOT licensed

- **No build.** The pipeline's Mine+Register step ends at registered testable claims; Adjudicate is
  normal governance.
- **No experiment queued.** The falsifiers above are discriminating observables, not queue entries.
- **`hypothesis_space_registry.v1.json` NOT amended.** Its single producer is `/failure-autopsy` Step
  9b. MECH-566 is *offered* as a candidate re-operationalization of `zworld_actor_adequacy_locus` --
  the first non-locus shape available to that question -- but the re-pose is routed on `GFLAG-0312`
  and registry corrections on `GFLAG-0329`.
- **The shared-latent cost is unpriced.** `z_world` serves SD-015, ARC-030, MECH-117, the EXQ-085h..o
  cluster, MECH-457 and ARC-065. MECH-567 carries a mandatory co-measurement of grounding lift for
  this reason; Poort et al. 2015 is the biological counterweight.

## Sources

- Biology: `evidence/literature/targeted_review_objective_consumer_transfer/` (5 entries: Semedo 2019
  communication subspace; Kaufman 2014 output-null subspace; Rumyantsev 2020 information present vs
  used; David 2012 task reward reshapes receptive fields; Poort 2015 as the MIXED counterweight).
  Scope boundary: this is the **transfer** pull, not the generic-vs-task-relevant **compression** pull
  owned by `chip-20260916-sd106-compression-litpull`.
- External: `REE_convergence/sources/muzero/consumer_trained_encoder.md`,
  `REE_convergence/sources/dreamer-v3/objective_transfer_balance.md`.
