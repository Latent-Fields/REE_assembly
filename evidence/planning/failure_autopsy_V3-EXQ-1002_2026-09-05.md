# Failure autopsy -- V3-EXQ-1002 (z_world actor-adequacy locus: H-B vs H-C)

**Generated:** 2026-09-05T02:38:25Z - **Confirmed:** 2026-09-05T09:36:37Z by `governance-20260905 (user gate, inline route A)`
**Scope:** single - **Status:** `confirmed` (Step 7c cross-model adversarial pass RUN -- verdict CONTESTED; Step 8 interactive gate HELD; Step 9b registry writes still owed, see section 9)
**Target:** `v3_exq_1002_zworld_actor_adequacy_oracle_adapter_20260905T005017Z_v3` - **Purpose:** diagnostic - **Outcome:** FAIL
**Claims tagged:** NONE (`claim_ids: []`, deliberate) - **Bears on:** INV-088, MECH-457 - **Machine-readable:** `failure_autopsy_V3-EXQ-1002_2026-09-05.json`
**Question:** `zworld_actor_adequacy_locus` (frozen ledger, registered 2026-09-03 from `failure_autopsy_V3-EXQ-978_2026-09-03`)

---

## 0. The one-paragraph verdict

**H-B is eliminated and that is solid.** With RL credit assignment removed entirely and the
reader held at the consumer's exact capacity, the `local_view_greedy` oracle's policy is
recoverable from the raw 25-dim observation at **0.979** held-out agreement and from V3-EXQ-978's
frozen 32-dim `z_world` at **0.664**. The deficit is on the representation side of the interface,
not in the consumer's learning. **H-C is confirmed at its registered gate, on a caveated basis.**
The pre-registered `live_gate` reads "CANNOT reproduce -> H-C", the adapter could not reproduce,
every readiness gate is green, and the grid fired correctly -- so the gate's verdict stands. The
caveat is recorded in the basis rather than by reopening the gate: the run's own untrained control
-- a random projection through the same encoder channel -- scores **0.688**, i.e. at or above the
verdict arm on every seed, so the *gloss* "**this** latent's **learned** geometry" is not
established. And the encoder's actual input is the **full 250-dim `world_state`** (the 25-dim
field is 10% of it), so that comparator's failure is equally consistent with a **250 -> 32
channel-input bound** no rotation could fix. Two parallel probes on already-banked data separate
them, and either can weaken the confirmed leg.

---

## 1. Facts (no interpretation)

**Provenance.** `ree-cloud-2`, `linux-x86_64-py3.10-torch2.12.0+cpu`, 18,850.9 s (5 h 14 m),
3 seeds (42/43/44), rung `D3_hazard_free`, `substrate_hash 5125cc63eb...`, `recording_schema
rec/v1`. `validate_recording.py`: **OK, no always-core gaps.** **Dry-run gate (Step 2a):**
`check_dry_run_citations.py` on the target, `V3-EXQ-1002` and the predecessor
`v3_exq_978_...` -- 0 dry cited, 0 dry in named families, 2 clean, exit 0. No **top-level**
`dry_run` field on the manifest (`config.dry_run` is present and `false`); the full 40 oracle +
20 random episode budget ran.

**Design.** Per seed the oracle drives 40 episodes; the full observation sequence is stored once,
and **all three arms read the SAME stored steps** (raw field directly; `z_world` by replaying each
stored episode through that arm's warmed agent). Split by **episode**, 70/30. The adapter *is*
`x734.PPOPolicyNet` -- the class V3-EXQ-978 instantiated as its reader -- so the capacity match
holds by construction (21,381 action-path parameters on both `z_world` arms; 20,485 on the
raw-field control, i.e. the positive control is 4.19% *under*-powered, the conservative
direction). Per-dimension standardisation is fitted on each arm's own training split.

**Primary DV -- held-out top-1 agreement with the oracle's action.**

| arm | seed 42 | seed 43 | seed 44 | mean | seeds clearing bar |
|---|---|---|---|---|---|
| `rawfield_ceiling` (positive control) | 0.9846 | 0.9796 | 0.9730 | **0.9791** | 3/3 |
| `zworld_untrained` (negative control) | 0.6876 | 0.6817 | 0.6947 | **0.6880** | 0/3 |
| `zworld_off` (**verdict arm**) | 0.6695 | 0.6735 | 0.6478 | **0.6636** | 0/3 |

Effective per-seed pass threshold = `max(0.80, trivial+0.20, untrained+0.10)` = **0.80** on all
three seeds. Trivial baseline (repeat-previous-executed-action) 0.566 / 0.580 / 0.572;
state-blind majority 0.2495 / 0.2484 / 0.2463. Verdict-arm minus paired untrained control:
**-0.0182 / -0.0082 / -0.0468 -- 0 of 3 seeds clear the +0.10 margin.**

**Every readiness gate is green.** `per_arm_gate.all_green` true, `red_arms []`, `vacuous_arms
[]`, `dv_headroom_gate_green` true, `criteria_non_degenerate` true on all four criteria. Positive
control 0.9730 (worst seed) against a 0.60 floor; oracle majority-class share 0.254 against a 0.60
ceiling; held-out steps 1,965 against a 500 floor; `zworld_encoder_trained_in_p0` weight delta
0.28159 against 1e-06; `zworld_not_collapsed` PR 4.22 against 2.0; demonstrator anchor 45.75
res/ep against the 1.0 floor. The elevation-headroom gate passed by its disclosed narrow margin
(0.41970 vs 0.40 required, ratio 1.049).

**Which criteria failed.** Both **load-bearing** criteria:
`C_zworld_adapter_reproduces_oracle` (0/3) and `C_verdict_arm_beats_untrained_control` (0/3).
Both **non-load-bearing** criteria passed: `C_positive_control_learns_from_raw_field` and
`C_untrained_control_below_bar`. This is a scored scientific null on a fully green instrument,
not a readiness failure.

**The secondary readouts -- this is where the run says more than its label does.**

| readout | `rawfield` | `zworld_untrained` | `zworld_off` |
|---|---|---|---|
| held-out agreement | 0.985 / 0.980 / 0.973 | 0.688 / 0.682 / 0.695 | 0.669 / 0.673 / 0.648 |
| **training-split** agreement | 0.997 / 0.992 / 0.986 | **0.828 / 0.828 / 0.821** | **0.766 / 0.760 / 0.752** |
| random-driven states | 0.988 / 0.991 / 0.981 | 0.613 / 0.636 / 0.631 | 0.572 / 0.602 / 0.611 |
| turn states (shortcut-free) | 0.982 / 0.976 / 0.962 | 0.609 / 0.616 / 0.623 | 0.578 / 0.635 / 0.586 |
| **unstandardised** held-out | 0.969 / 0.977 / 0.952 | **0.494 / 0.467 / 0.538** | **0.534 / 0.542 / 0.553** |
| participation ratio | n/a | **7.49 / 10.31 / 10.01** | **4.57 / 4.22 / 5.67** |
| final CE loss (standardised) | 0.025 / 0.036 / 0.041 | 0.466 / 0.463 / 0.473 | 0.610 / 0.613 / 0.630 |
| cloned foraging (res/ep) | 48.2 / 52.6 / 53.8 | 17.4 / 15.9 / 14.3 | 19.1 / 17.5 / 14.2 |
| cloned death rate | 0.50 / 0.75 / 0.45 | 0.90 / 1.00 / 1.00 | 0.85 / 0.90 / 1.00 |

Oracle anchor: 45.75 / 49.70 / 48.70 res/ep from the **same** 5x5 field the adapter reads.

---

## 2. Central adjudication (1): does the H-C verdict hold?

### 2a. What is not in doubt

The elimination of **H-B** is clean and is the run's load-bearing result. The frozen-latent
reader had failed twice before -- V3-EXQ-948 (`ppo_ree_latent`, 0.5 res/ep) and V3-EXQ-978's OFF
arm (0.267), both 0/3 against a 1.0 floor -- and both failures were confounded with RL credit
assignment. This design removes that confound by construction: supervision is the oracle's action
at every visited state, so there is no credit-assignment problem left to fail at, and the reader
is the consumer's own class at the consumer's own width. It still does not recover the mapping,
while the identical reader on the identical steps recovers it from the raw field at 0.973-0.985.
**The deficit is on the representation side of the interface.** That conclusion survives every
objection below.

### 2b. The tell: the warmed latent is not ahead of its untrained control -- and on the pre-registered instrument it is slightly behind

`zworld_off` (0.6636) and `zworld_untrained` (0.6880) sit 0.024 apart on a scale where the raw
field sits 0.315 away from both. `zworld_off` is at or **below** its untrained control on
(differences recomputed at the Step 7c pass; "x" = multiples of the pooled within-arm seed SD):

- the **held-out** split, 3/3 seeds -- -0.018/-0.008/-0.047, mean -0.024, **2.3x**;
- the **training** split, 3/3, by a larger and much less noisy margin (0.766/0.760/0.752 vs
  0.828/0.828/0.821) -- mean -0.067, **11.7x** -- the training split measures how much
  action-relevant structure the features carry *at this capacity*, with generalisation removed;
- the **final standardised CE loss**, 3/3 -- +0.145/+0.150/+0.157, **17.7x**, `zworld_off` worse;
- the **random-driven** state distribution, 3/3 (mean -0.032, 1.9x);
- the **turn-state** (shortcut-free) subset, 2/3 (seed 43 has `off` ahead by +0.019).

**The reported *unstandardised* readout reverses the sign** (`zworld_off` 0.534/0.542/0.553 vs
`zworld_untrained` 0.494/0.467/0.538, off ahead 3/3) -- **but it carries no sign at all.** Both z
arms sit **below the trivial repeat-previous-action baseline** (0.5661/0.5803/0.5720) on 3/3
seeds on that readout, with unstandardised CE 1.048-1.170 against `ln 5 = 1.609`: that adapter did
not converge on either arm, so it is not an alternative measurement of the same quantity, it is a
broken one. The driver itself **pre-registers** how to read a large standardised/unstandardised
gap (`_unstandardised_secondary`): *"the primary (standardised) number is the one that answers the
actual question, because it is the one with the scaling explanation removed."*

So the correct statement is **"no better than -- and on the pre-registered primary instrument
consistently slightly *worse* than -- a random projection of the same input"**, by an amount
(0.02 held-out, 0.07 train) an **order of magnitude smaller than the ~0.30 deficit** to the raw
field. That is why the warmup is not the *locus* of the deficit, and equally why the ordering does
**not** license the grid's `untrained_projection_clears_warmed_arm_does_not` cell (which requires
the untrained arm to clear the absolute bar; it does not).

The one preprocessing-invariant asymmetry is dimensional and points the same way: the warmup
roughly **halves** the latent's participation ratio (4.57/4.22/5.67 vs 7.49/10.31/10.01, 0.53x)
while buying no action-relevant agreement. It converges with V3-EXQ-978's own independent finding
that the SD-018 ON leg moved the latent two to three orders *below* the seed spread.

### 2c. Are "the geometry blocks the mapping" and "z_world carries no more action-relevant information than a random projection at 32 dims" the same hypothesis?

**No, and the run does not separate them.** They differ in what they say is *fixable*: H-C says
the information is there in a bad arrangement, so an information-preserving rotation should
recover it -- which is exactly why the H-C corroborator is the owed follow-on. The rival says the
observation-to-32-dim channel does not deliver the content in the first place, in which case a
rotation is a foregone null.

**The load-bearing fact, and the one the staged draft got wrong: the encoder's input is the FULL
250-dim `world_state`, not the 25-dim field.** `causal_grid_world.py` sets `world_obs_dim = 250`
under `use_proxy_fields=True` (local_view 175 + contamination 25 + hazard_field 25 +
resource_field 25, with `resource_field_view == world_state[225:250]`), and the driver passes the
whole `world_state` to `agent.sense`. So `zworld_untrained` is a random **nonlinear compression of
250 dims into 32**, in which the field the positive control reads is **10% of the input**. Its
failing at 0.688 is evidence about a **channel-input bottleneck** (250 -> 32 with no pressure to
isolate the field) -- not about "32 dimensions of *this observation*".

That kills the staged draft's proposed control. A 32-dim projection of the **25-dim field** is
information-preserving by rank (25 <= 32); composed with the adapter's `Linear(32,128)` first
layer it spans *exactly* the `Linear(25,128)` function class, so the positive control's own
0.973-0.985 function is representable and the "declared null" could only fire through an
optimisation artefact. It is a re-basis of the positive control, not a capacity test. The
informative comparator is a 32-dim projection of the **250-dim `world_state`**, whose null *is*
realisable -- and that is what the respecified H-E leg now asks.

**The "inverted conjunct" argument is recorded and withdrawn.** The staged draft read
`C_untrained_control_below_bar`'s own text --

> "... is what makes an H-C label attributable to THIS latent's geometry rather than to '32
> dimensions of anything cannot do it'. True (the expected case) means the untrained random
> projection does NOT itself clear the bar."

-- as inverted, on the ground that an untrained 32-dim projection *failing* is that alternative's
evidence rather than its exclusion, and used that to hold H-C open. **Withdrawn at the Step 8
gate.** The conjunct's *documented* purpose, stated in three places (the driver's ARMS section,
the manifest's `interpretation.question`, and `C_verdict_arm_beats_untrained_control`'s
description), is **attribution to the warmup** -- *"whether any actionability found is creditable
to SD-018's warmup"* -- plus a guard against a spurious H-C via a collapsed comparator; for that
purpose the conjunct's sign is correct. The phrase "32 dimensions of anything" is loose English
and was incoherent as written (32 > 25 field dims; the encoder's input is 250), so it is a
**wording defect in the driver**, not a licence to reopen a pre-registered gate. What survives of
the objection is substantive, and is recorded where the registry puts doubt: in H-C's caveated
`basis` and in the two new legs.

Two further structural notes, both about the grid and neither about arithmetic:

- **H-C is the grid's terminal `else` branch** (`_adjudicate` returns it when no other cell
  fires), so it is a *residual* cell rather than a positively attributed one.
- **The neighbouring cell would have read this shape as a finding about the warmup.** The
  `untrained_projection_clears_warmed_arm_does_not` cell -- untrained ahead of the warmed arm --
  is exactly this run's *ordering*, and it is withheld only because the untrained arm did not
  itself clear the absolute bar. The boolean thresholding discretises away a 3/3 consistent
  ordering that the cell exists to notice.

`_adjudicate` evaluated its booleans correctly, and the three red-team passes that hardened it
(the `beats_untrained` requirement, the `comparator_green` gate) all did their jobs. What escaped
them is a criterion whose **English claim about what it establishes** does not follow from the
condition it tests.

### 2d. The two null readings the driver names, checked against this run

- **`substrate_not_ready_requeue`** -- does NOT apply. It fires on (a) a red positive control or
  (b) no DV headroom. The positive control reached 0.973-0.985 and the headroom gate passed. The
  instrument is interpretable.
- **`zworld_supports_mapping_but_warmup_non_contributory`** -- does NOT apply either, and the
  distinction matters: that cell requires `off_clears`, i.e. the adapter *did* reproduce the
  oracle above the bar. It did not (0.664 vs 0.80). This run is the strictly worse case: the
  warmup is non-contributory **and** the latent does not support the mapping.

### 2e. Verdict on (1)

**H-C is CONFIRMED, with a caveated basis** (user decision at the Step 8 gate, 2026-09-05). The
registered `live_gate` reads "CANNOT reproduce -> H-C"; the adapter could not reproduce; every
readiness gate is green and `criteria_non_degenerate` is true on all four criteria, so
`control_passed` is true and the grid fired correctly. Leaving the leg `alive` after its own
pre-registered gate ran and returned its branch would be a post-hoc reinterpretation of a
pre-registered gate -- the thing GOV-FROZEN-1 exists to police -- and the staged draft's stated
reason for doing so does not hold: the owed corroborator carries **its own declared null**
("agreement is flat under an information-preserving, separability-improving re-basis"), so
confirming H-C makes the corroborator a **test of H-C** (a flat result weakens a confirmed leg;
registry states are not terminal, and `met_elimination_bar: false` already records the debt),
whereas leaving it alive makes the corroborator a test of nothing registered.

**Its scientific gloss is what carries the caveat, in the `basis` rather than in the state.**
"z_world's geometry blocks the mapping" implies a property of *this* latent's **learned**
arrangement, and this run has no measurement distinguishing that latent from an untrained
projection of the same 250-dim input -- which ties with it. The deficit may be a 250 -> 32
channel-input property. The owed rotation corroborator and the respecified H-E leg are the two
tests, run in **parallel**, and either can weaken this leg.

---

## 3. Central adjudication (2): does GFLAG-0131 apply?

**Not to the load-bearing criterion. It applies squarely to one secondary, and that secondary is
not verdict-bearing.**

GFLAG-0131 (open, raised 2026-09-04) warned that V3-EXQ-978's eval reader fell into a
deterministic two-cell limit cycle in 9 of 12 episodes, that the contamination rule then killed
the agent at step 11-23, and that the follow-on "should pre-register a stochastic or
contamination-off eval, or a survival-normalised DV, else the same truncation will mask the
adapter contrast."

**The load-bearing DV here is not an episode return.** It is per-state top-1 agreement on a
**behaviour-cloning dataset whose states were driven by the ORACLE**, which survives (45.75-49.70
res/ep, `competence_supra_floor` true on all seeds), plus a second split driven by a **RANDOM**
policy. Neither distribution is generated by an evaluated policy, so no dithering reader can
truncate the data the criterion reads, and there is no rollout in the DV at all. The flag's
mechanism cannot reach it.

**The random-state column IS the stochastic-eval answer the flag asked for**, and it replicates
the finding rather than overturning it: `rawfield` 0.988/0.991/0.981, `zworld_untrained`
0.613/0.636/0.631, `zworld_off` 0.572/0.602/0.611 -- same ordering, same ~0.37 gap to the raw
field. The shortcut-free turn-state subset agrees. So the driver did not adopt the flag's literal
remedies (it pre-registers neither a contamination-off eval nor a survival-normalised DV) but it
satisfied their **intent** for the verdict, by moving the DV off episode return entirely and
adding a second, policy-independent state distribution.

**One qualification on the random-state column, added at the Step 7c pass.** `_collect_episodes`
breaks on `done`, and the RANDOM-driven split retained only **760 / 786 / 968 of a possible 4000
steps (19-24%)** -- the random walker is being killed early by the *same* contamination rule
GFLAG-0131 describes ("random_walk survives ~48 steps"), so that column samples
**early-episode states only** (~40 steps/episode). The oracle-driven split retained 79-90%
(5038/4997/4423 of 5600 train, 2148/2061/1965 of 2400 held-out). This is **not a confound for the
differential** -- the split is paired across arms, all three arms read the identical stored steps
-- but "the random-state column IS the stochastic-eval answer the flag asked for" should be read
as "on a truncated, early-episode state distribution", not as a full-episode stochastic eval.

**Where the flag does bite:** the *secondary* cloned-competence readout (`zworld_off` 16.88,
`zworld_untrained` 15.82, `rawfield` 51.50 res/ep) is measured by rolling the cloned policy out,
and its `cloned_death_rate` is **0.85-1.00 on both z_world arms** (and 0.45-0.75 even on the
raw-field arm) -- the exact truncation signature GFLAG-0131 describes. Those numbers should not be
read as clean competence measures, and this autopsy does not route on them. Recommend GFLAG-0131
stays **open**: the follow-on it names has now run, its load-bearing criterion is immune, but its
warning still applies to every rollout-scored readout in this family.

---

## 4. Claim layer -- claim-free, and correctly so

`claim_ids` is empty by design (driver "CLAIM LAYER" section; queue note; V3-EXQ-978's confirmed
autopsy section 3 recorded INV-088 and MECH-457 as **peripheral co-tags** with
`recommended_epistemic_category_per_claim` set so neither claim's counter incremented). This run
exercises neither claim's mechanism: MECH-457's actor-critic substrate is absent by construction
(the manipulation *is* that no policy is learned by RL), and INV-088's evaluator-bounded-by-z_world
relation is untouched (no E3 evaluator is trained or read; its own re-check stays gated on
SD-e1-rollout-consistency-training ITEM 2, a different route).

Both are recorded as **`bears_on`** so the finding is discoverable from the claims, and both get
a note-only `per_claim_recommendation` with `recommended_diagnostic_evidence_adjudicated: true`:

- **INV-088** -- `non_contributory`, `standard`, stays `candidate`. Bears-on fact for its
  `evidence_quality_note`: z_world's differentiation deficit is now measured on an **action**
  readout (0.664 vs 0.979 from the raw observation, and **no better than** -- on the
  pre-registered standardised primary consistently slightly *worse* than -- an untrained random
  projection of the same 250-dim input at 0.688), not only on a decode readout. `epistemic_category` is already `standard`
  and `diagnostic_evidence_adjudicated` is already `true`, so no storable field moves -- the
  change string ends on the citation stamp, which is not yet true and clears by provenance.
- **MECH-457** -- `non_contributory`, `standard`, stays `candidate/v3_pending`. Bears on it in the
  **constraining** direction: with credit assignment removed entirely, a reader at the consumer's
  exact capacity still reaches only 0.664 from frozen z_world, so a dedicated actor-critic
  substrate reading *this* latent would inherit a representation-side ceiling before any RPE
  teaching signal is applied. Necessity untouched; the sufficiency disclaimer already in its note
  is further constrained. The claim carries **no** `diagnostic_evidence_adjudicated` field at all,
  so the change string ends there -- storable and not yet true.

---

## 5. Biological-reference triage

**Closest reference mechanism: DiCarlo-style manifold untangling.** Two entries already in the
corpus, both directly on point:
`evidence/literature/targeted_review_perceptual_manifold_adaptors/entries/2026-06-12_arc_087_ventral_stream_manifold_untangling_dicarlo2012`
and `evidence/literature/targeted_review_sd_015/entries/2026-04-02_sd_015_object_untangling_dicarlo2007`.
Untangling is close to a literal statement of H-C: a population code can carry a variable that is
*present* and yet unusable by a simple downstream readout until a cascade whose **job** is
reshaping has flattened and separated the behaviourally relevant manifolds. `lit_status:
present` for that principle.

**Dependency the reference mechanism has and REE's translation does not.** In the biological
case, untangling is produced by (i) an objective/architecture whose purpose is that reshaping and
(ii) a *dorsal* action-formatted stream distinct from the ventral recognition stream. REE's
`z_world` is trained for **sensory prediction/reconstruction** (SD-056 e2 world-forward
contrastive) plus the SD-018 auxiliary field head -- objectives with no pressure to untangle the
**action-relevant** variable -- and there is no separate action-formatted stream for an actor to
read: every consumer reads the one shared prediction-trained latent. So the failure **matches a
missing-dependency signature**, which under the skill's core principle makes it a discovered
prerequisite rather than a falsification.

**The inversion that makes this cheap to act on.** The SD-015 DiCarlo entry's own caveat
predicted it: *"A 2-layer MLP can likely extract resource type from this input without needing
the hierarchical, multi-stage architecture that biology requires."* That is precisely what the
positive control measures -- a 2x128 MLP reaches 0.979 on `resource_field_view`. **The raw field
is already untangled for this task.** The encoder is therefore not failing a hard untangling
problem; it is tangling or discarding an easy one. That is a much more tractable diagnosis than
"REE needs a ventral-stream-depth cascade".

**Lit gap worth a commission (secondary, not this autopsy's primary route):** no
`targeted_review_*` covers the specific architectural question *"does biology route action
selection through a single shared prediction-trained latent, or maintain a separate
action-formatted stream?"* The nearest is
`targeted_review_action_policy_decomposition` (five levels; REE covers level 4 well, is missing
levels 2-3), which is about the *policy* decomposition rather than the representational format
the policy reads.

---

## 6. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **n/a** (claim-free) | neither `bears_on` claim's mechanism exercised; constrained obliquely only |
| Biological reference | **clear** | DiCarlo untangling; failure matches a missing-dependency signature (no untangling objective, no action-formatted stream) |
| Prerequisites | **present** | encoder trained (delta 0.2816), latent not collapsed (PR 4.22+), oracle clears the floor from the same 5x5 view, 1,965 held-out steps |
| Implementation | **complete** | adapter *is* `x734.PPOPolicyNet` at the consumer's width (21,381 params); latent reproduced from 978's own warmup, imports not re-definitions |
| Environment | **adequate** | the mapping demonstrably exists from the same observation (oracle 45.75-49.70 res/ep; raw-field reader 0.973-0.985). Not too sparse |
| Measurement | **under-instrumented (for attribution)** | the encoder's input is the full **250-dim** `world_state` and no run carries a 32-dim reference *of that input* known to be *able* to clear the bar; the trained/untrained differential is consistent on the pre-registered standardised primary (train 11.7x, CE 17.7x) and reverses only on an unstandardised readout that sits below the trivial baseline on 3/3 seeds on both z arms; the competence secondary carries the GFLAG-0131 truncation confound |
| Integration | **isolated by design** | the consumer is deliberately severed from the representation -- that is the manipulation, not a defect |
| Scale / capacity | **adequate**, one gate marginal | 40+20 episodes x 3 seeds, converged positive control (CE 0.025-0.041); the elevation-headroom gate passed at ratio 1.049 (disclosed, not loosened) and did not bind |

### Failure-location summary (GOV-FAILLOC-1)

| Bucket | Reads | Established? |
|---|---|---|
| MECHANISM FAILED | Implementation **complete** | **established** |
| MEASURES FAILED | Measurement **under-instrumented** | **partial** |
| ENVIRONMENT FAILED | Environment **adequate** | **established** |
| REE FAILED | needs all three | **NO** |

**Net: MIXED (MECHANISM + ENVIRONMENT established, MEASURES partial) -- explicitly NOT chargeable
to REE as a whole.** The mechanism under test -- the observation-to-`z_world` encoding, read as a
representation an actor must use -- is fully implemented, trained, non-collapsed and faithfully
reproduced, and the environment demonstrably contains a mapping a simple reader learns from the
raw observation; both buckets are established. Measurement is only *partial*, because the
attribution conjunct cannot distinguish "this latent's **learned** geometry blocks the mapping"
from "a 32-dim compression of the full 250-dim `world_state` cannot support it under this reader"
-- the only 32-dim comparator in the run is itself such a compression, and it also fails. With
MEASURES partial, the fourth bucket cannot be reached, and no "REE failed to forage" read is
licensed by this artifact.

### Recommended epistemic category

**`standard`** (blanket and per-claim). Claim-free diagnostic; `standard` asserts no epistemic
suppression, which is the correct verdict. Deliberately **not** `substrate_ceiling`: that value
would suppress GOV-GRAN-1 surfacing and mark both `bears_on` claims not-v3-testable, and this run
does not assert the answer is gated on a build -- it asserts that two cheap parallel probes on
already-banked data separate the confirmed leg's gate sense from its learned-geometry gloss. The
failure-mode diagnosis lives in the note fields.

---

## 7. Granularity-debt trigger and the re-derive brake

**Granularity-debt recurrence trigger: DOES NOT FIRE.** Run for both `bears_on` claims with
`granularity_debt_cluster.py` (targets whose own `claim_ids` name the claim, never a grep):

- **MECH-457** -- 31 targets across 21 files; alignment distribution `intact=17, strengthened=5,
  unclear=2, unstamped=2, untested=2, weakened=2, other=1`. Already **decomposed** 2026-07-22
  (children MECH-475 / MECH-476, user-approved), so the debt this trigger exists to surface has
  already been discharged; nothing in this run adds a new structurally-different failure
  signature to it.
- **INV-088** -- 9 targets across 9 files; `intact=2, other=2, untested=2, weakened=2,
  unstamped=1`.
- **This run adds no target to either cluster:** `claim_ids` is empty, so it is invisible to the
  reader by construction. Routing is not `/claim-synthesis`.

**Re-derive brake (R1-R3): counts UNCHANGED; this run does not fire it and does not increment
it.** Re-run under the binding R1-R3 recipe on 2026-09-05:

- **MECH-457 = 13 hits** (756, 750, 752, 753, 754, 755, 770, 771, 772, 781, 765, 769, 821b)
- **INV-088 = 2 hits** (750, 754)

Both identical to what V3-EXQ-978's autopsy recorded, and both at or past the threshold of 2 --
so the **standing brake on both claims remains fired** and a same-claim lettered re-run against
the same substrate is still refused. The prior autopsy explicitly said 978 must not count as a
ceiling hit; **this run likewise does not count -- because it is claim-free, the counter's
`claim in target.claim_ids` test never reaches it.** Stated so no later session re-derives it.

**What this autopsy refuses, on its own account:** a lettered `V3-EXQ-1002b` that re-runs this
design at a larger BC budget, more adapter passes, or a wider adapter. The positive control
already converged (final CE 0.025-0.041, agreement 0.973-0.985); the null is not a power problem
and more of the same is the loop the brake exists to stop. What is recommended is a **new EXQ
number asking two different questions in parallel** (section 8), which the brake explicitly
permits and which reuses this run's own banked dataset and adapter.

---

## 8. Routing -- a parallel two-leg portfolio on already-banked data

**Node classification: `complex (probe-gated) / puzzle (known rules)`.** The frame is well posed
and two missing *facts* bear on the confirmed H-C leg from opposite directions. It is not
`complicated (buildable)`: SD-018 shape (b) is a named build, but building it now raises the score
while leaving the locus unlocalised. It is not `mystery (known data)`: both deciding data are
absent from every run so far.

**Routing: `/queue-experiment`, a NEW EXQ number, a PARALLEL two-leg GOV-FANOUT-1 portfolio.**
Not ordered, not conditional -- the ordering in the staged draft rested on a leg-1 specification
whose declared null was unrealisable by construction, which made the "portfolio" a sequential
chain with a decorative first step: exactly the single-letter shape GOV-FANOUT-1 exists to
prevent. Both legs run on V3-EXQ-1002's banked BC dataset, the same `x734.PPOPolicyNet` adapter
and the same standardiser.

1. **(instrumentation axis) LEG 1 -- THE CHANNEL-INPUT CONTROL (adjudicates H-E).** A
   32-dimensional random-Gaussian and/or PCA projection of the **full 250-dim `world_state`** --
   the encoder's *actual* input, optionally plus `body_state` to mirror the topdown term -- fitted
   on the training split, read by the same adapter. Declared null: this 250 -> 32 projection also
   fails the 0.80 bar.
   - **Clears** -> an optimal *linear* 250 -> 32 compression preserves what the task needs;
     **H-E eliminated**; the deficit is specific to what the REE encoder channel does, and H-C's
     learned-geometry gloss survives.
   - **Does not clear** -> **H-E confirmed**; the deficit is a channel-**input** bound no rotation
     of `z_world` can fix, the confirmed H-C leg is **weakened** to its narrow gate sense, and the
     route is instrument/interface redesign rather than a geometry build.
   - *Sanity anchor only, explicitly **not** a gate:* a 32-dim projection of the **25-dim field
     alone** is expected to clear trivially (any injective `R^25 -> R^32` composed with
     `Linear(32,128)` spans exactly `Linear(25,128)`), which is why the staged draft's 25-dim
     version of this leg is **dropped**.
2. **(representation axis) LEG 2 -- THE OWED H-C CORROBORATOR, run in PARALLEL.** An
   information-preserving rotation/reweighting of the frozen `z_world` (whitening,
   decision-relevant reweighting, or a train-split-fitted supervised linear re-basis), same
   adapter. Declared null: agreement is flat under a separability-improving,
   information-preserving re-basis. **This is the test of the now-confirmed H-C leg:** a flat
   result *weakens* it, a lift *corroborates* it. It is no longer conditional on leg 1, because
   with leg 1 respecified to the 250-dim input neither leg's outcome is foregone and neither can
   make the other unnecessary in advance.

Cost for both: no `ree_core` change, no new warmup family, no contract-gate exposure. A lettered
`V3-EXQ-1002b` power-bump stays **refused** (section 7).

**GOV-FANOUT-1 / growth-restriction compliance.** The target question carries **no**
`growth_restriction` (checked; field absent), so growth is permitted without a gate. Recorded
because the adjacent `competence_floor` qid -- which names the same two claims -- **is** closed to
further fan-out; this qid exists precisely because that restriction was surfaced at the
2026-09-03 gate. **Nothing here attaches to `competence_floor`.** Leg 2 sits in the
`representation` family, which already holds the eliminated H-B and the confirmed H-C, but it adds
**no leg** to the registry -- it tests an existing confirmed leg, so it is not circling. The two
*new legs* (H-D `constitution`, H-E `instrumentation`) land in families with no prior leg here.

**Does H-C make the SD-018 shape-(b) build the next move?** **No -- and the hold now rests on two
independent grounds, stated separately because they can come apart.**

- **(i) The predecessor's condition, now positively met.**
  `failure_autopsy_V3-EXQ-978_2026-09-03` pre-registered *"CANNOT [reproduce] -> H-C, shape (b)
  would raise the score without addressing the constraint"*, and `claims.yaml` INV-088's note
  requires the discriminator *"BEFORE SD-018 shape (b) is built"*. This run took the CANNOT
  branch and H-C is confirmed, so that hold is established rather than merely asserted.
- **(ii) Independently of any H-C disposition:** shape (b) side-channels the raw field **past**
  `z_world`, i.e. it **bypasses** the interface rather than repairing it, and that interface is
  the v3 binding constraint. Promoting it on this result would bank exactly the
  confident-but-wrong localisation GOV-FANOUT-1 exists to prevent. This ground would hold even if
  H-C had been left alive.

**The hold is an OVERRIDE of the design doc's own fallback rule, and is recorded as such.**
`docs/architecture/sd_018_resource_proximity_supervision.md` line 94 says, of exactly this owed
validation: *"If it nulls, build shape (b)."* V3-EXQ-978's autopsy overrode that rule; this
autopsy continues the override on ground (ii) plus the now-met (i). Governance should either
ratify the override on the SD-018 entry or amend line 94, so the design doc and the evidence
record stop disagreeing.

Recorded for governance as **notes on the existing SD-018 entry, not a new build**
(`recommended_substrate_queue_entry.action = none`): SD-018 shape (a) is now validated-negative
twice over -- V3-EXQ-978 showed the ON leg does not move the latent, and this run shows the latent
it produces is **no better than, and on the pre-registered standardised primary consistently
slightly worse than**, an untrained random projection of the same 250-dim input on the action
readout.

**Draft `evidence_quality_note` text** for governance: see
`targets[0].recommended_evidence_quality_note` in the JSON (written through verbatim).

## 9. Ledger delta -- the EXACT registry patch (Step 9b; registry NOT yet written)

Question `zworld_actor_adequacy_locus`. Growth-restriction check: **absent, proceed**. The
machine-readable patch is `hypothesis_space_ledger_pending` in the sibling JSON, and is also
written standalone to `registry_patch_1002.json` (scratchpad) so the confirming session can apply
it programmatically. It carries step-by-step `apply_instructions`.

| leg | mode | state | bar fields |
|---|---|---|---|
| `H-B-consumer-learning` | B (resolve) | **eliminated** | `control_passed` T, `non_degenerate` T, `met_elimination_bar` T |
| `H-C-geometry-mismatch` | B (resolve) | **confirmed** (caveated basis; corroborator owed) | T, T, **F** |
| `H-D-warmup-not-the-locus` | **labelled FAN-OUT (3a), git-witnessed** | **confirmed** (necessary-not-sufficient) | T, T, **F** |
| `H-E-channel-input-capacity` | **labelled FAN-OUT (3a), ordinary Mode A** | alive, unqueued | bar not met |

`resolved_utc` for the three resolved legs = **2026-09-05T00:50:17Z** (the run's own
`timestamp_utc`). `evidence_direction` on the leg is `non_contributory` for the eliminated H-B
(discriminating) and `supports` for the two confirmed legs (the run supports those legs at their
own gates); the run-level manifest disposition stays `non_contributory`, as a claim-free
diagnostic.

**H-D is NOT a Mode C discovery -- it is labelled fan-out on a git witness.** "The warmup is not
the locus" was named in writing in `evidence/planning/exq1002_redteam_findings_20260904.md`, first
committed **`ac85c048a2`, 2026-09-04 19:45 +0100 = 18:45Z** -- about **6 h before the run
resolved** (2026-09-05T00:50:17Z) and ~50 min before it *started*. Invariant 3a(a) is satisfied by
that commit date, which cannot be manufactured. Mode C is the wrong door: the rival was
*anticipated* (the driver's own `_adjudicate` grid carries two warmup-locus cells,
`zworld_supports_mapping_but_warmup_non_contributory` and
`untrained_projection_clears_warmed_arm_does_not`, and the manifest's `interpretation.question`
names the untrained arm as an ATTRIBUTION axis), so discovery growth's born-not-anticipated
condition fails and using it would be the escape hatch the `discovery_growth` invariant explicitly
forbids. **The staged draft's `discovery_growth_event` block is deleted, not amended.**

H-D's `pre_registered_utc` is the witness stamp `2026-09-04T18:45:00Z` (<= its `resolved_utc`, so
invariant 2 holds); H-E's is `2026-09-05T09:36:37Z` with `pre_registration_source` =
this autopsy (ordinary Mode A -- its adjudicating run is not queued, let alone resolved). The
event-level `pre_registered_utc` records the earlier witness stamp that licenses the batch.

**Counters:** `initial_frozen_count` **2 -> 4** via **one** labelled fan-out event, `delta: 2 ==
len(added_hids)`. `initial_frozen_count_at_registration` **stays 2**. `fanout_sources` gains both
`exq1002_redteam_findings_20260904.md` and this artifact.

**Axis families:** `intrinsic-architecture` -> `constitution` and `instrumentation` ->
`instrumentation` are both existing rows in `axis_families.map` (verified against the live
registry); **no map addition needed**. Both new legs land in families with **no prior leg on this
question**, while the eliminated leg sat in `representation` -- so the growth is **refining, not
circling**.

**`fanout_growth_note`:** this question took one fan-out growth event (delta 2) in its first
adjudication cycle; the denominator moved 2 -> 4 while one leg was eliminated and two confirmed,
so the headline narrowing ratio is inflated exactly here and must be read alongside the growth
event.

**`decision` block:** `decidable` moves to **`true`** -- the registered question (H-B vs H-C) *is*
decided. `live_gate` becomes the parallel two-leg portfolio of section 8; `distance_phrase`
records that the residual attribution is one portfolio away on already-banked data;
`observation_bottleneck` records that no run carries a 32-dim reference of the encoder's *actual*
250-dim input known to be able to clear the bar, and none applies an information-preserving
re-basis to the frozen latent. `decision_log_ref` stays `null` (human-owned).

**After applying:** run `build_hypothesis_space.py` and `check_hypothesis_space_integrity.py`,
confirm the append lands under *Advisory -- labelled fan-out growth* (not a bucket-(b) flag), and
clear any (a)-(d) flag before committing.

## 10. Step 7b mechanical pre-routing checks

`autopsy_pre_routing_checks.py --artifact ... --json`: **`fire_count: 0`**.

`inapplicable`: **C1, C2, C3** -- all three are claim-keyed and this target carries
`claim_ids: []`, so they are **structurally blind** here. **C5** (a run already scored on a bed
the prose calls unique or unrun) and **C6-narrow** (a metric agreeing across arms in most seeds
and dissenting in a minority against a prose absolute) were applicable once the sibling `.md`
existed and **did not fire**. Per the skill, *"`inapplicable` is NOT
'no fire'"*: a quiet report on a claim-free artifact means the checks could not look, and the
load falls on Step 7c (the adversarial pass) and on the Step 8 gate. **Both have since been
run** -- see section 12 -- and both moved the artifact, which is the concrete case for treating a
quiet `inapplicable` report as "the checks could not look", never as "no fire".

---

## 11. Withdrawn arguments (recorded, not deleted)

- **"The `C_untrained_control_below_bar` conjunct is inverted relative to its own stated purpose,
  so H-C stays `alive`."** The staged draft's central move, **withdrawn at the Step 8 gate** after
  the cross-model red-team pass. Two grounds. (1) The conjunct's *documented* purpose -- in the
  driver's ARMS section, the manifest's `interpretation.question`, and
  `C_verdict_arm_beats_untrained_control`'s description -- is **attribution to the warmup**
  ("whether any actionability found is creditable to SD-018's warmup") plus a guard against a
  spurious H-C via a collapsed comparator; for *that* purpose the sign is correct. The draft
  picked the wrong stated purpose. (2) The phrase "32 dimensions of anything" is loose English and
  was **incoherent as written** -- 32 > 25 field dims, and the encoder's actual input is 250 dims
  -- so it is a **wording defect in the driver**, not a licence to reopen a pre-registered gate.
  The draft's own Open Doubt 2 had already conceded this reading. The substantive residue is
  recorded in H-C's caveated `basis` and in the two new legs instead. *Also withdrawn with it:*
  the argument that "confirming H-C would make the owed corroborator's premise unfalsifiable" --
  the corroborator carries its own declared null, so confirming H-C makes it a **test** of H-C,
  while leaving H-C alive would make it a test of nothing registered.
- **"The warmup DEGRADED actionability" -- withdrawn, then RE-INSTATED in a qualified form.**
  Drafted from the standardised held-out, training-split and random-state columns (all 3/3 in that
  direction); withdrawn in the staged draft because the unstandardised column reverses the sign
  3/3; **re-instated as the weaker, correct statement** at the Step 8 gate. The unstandardised
  readout sits **below the trivial baseline on 3/3 seeds on both z arms** (CE 1.05-1.17 against
  `ln 5 = 1.609`) -- that adapter did not converge, so it carries no sign -- and the driver
  *pre-registers* the standardised primary as the number that answers the question when the two
  diverge. What is asserted now is neither "degraded" nor "indistinguishable within one
  preprocessing nuisance" (both wrong): it is **"no better than, and on the pre-registered primary
  consistently slightly worse than, a random projection of the same input"** -- by an amount an
  order of magnitude smaller than the ~0.30 deficit, which is exactly why the warmup is not the
  *locus*.
- **"A 32-dim information-preserving projection of the RAW 25-dim field is the missing control."**
  Proposed as leg 1 of the staged routing, **dropped**: it is information-preserving by rank
  (25 <= 32) and composes with the adapter's `Linear(32,128)` to span exactly `Linear(25,128)`, so
  its declared null is unrealisable and it is a re-basis of the positive control rather than a
  capacity test. Retained only as a **sanity anchor**, never as a gate. The informative version --
  a 32-dim projection of the full **250-dim `world_state`** -- replaces it.
- **"`H-D` is a Mode C discovery."** **Withdrawn**: it was named in a git-committed artifact ~6 h
  before the run resolved, and the driver's own grid carries two warmup-locus cells, so it was
  anticipated. Recorded instead as labelled fan-out growth on that git witness (section 9).
- **"The `untrained_projection_clears_warmed_arm_does_not` cell should have fired."** Checked and
  **not adopted**: that cell requires the untrained arm to clear the absolute bar, and it does not
  (0.688 < 0.80). The grid is internally consistent; what is recorded instead is that the cell's
  *ordering* condition is met while its *level* condition is not.
- **"Route to `/implement-substrate` on SD-018 shape (b)."** Considered because the raw-field arm
  makes shape (b) look like a large performance lever, and **rejected** on two independent grounds
  (section 8), one of which overrides the SD-018 design doc's own "if it nulls, build shape (b)"
  fallback and is recorded as an override.

## 12. Step 7c red-team pass and Step 8 gate outcome

**Red-team pass (Step 7c).** Cross-model adversarial review, model **`fable-5.1`**, read-only,
ordering enforced (draft JSON first, then raw evidence, then the draft `.md` last). **Verdict:
CONTESTED** -- four defects, three qualifications, eleven hygiene items, and an independent
recomputation of every number in the artifact (all matched). Findings file:
`scratchpad/redteam_1002.md`; recorded machine-readably as the top-level `red_team` block in the
JSON, with `findings_applied: ["1","2","3","4","5","6","hygiene"]`.

**Step 8 gate (user decision, binding, 2026-09-05).** *"H-C confirmed, caveated basis; H-D becomes
a labelled fan-out leg on the git witness (not Mode C); H-E respecified against the full 250-dim
`world_state`; route the owed rotation corroborator + respecified H-E as parallel legs."*

| draft's open doubt | disposition |
|---|---|
| 1. The H-C disposition (`alive` vs `confirmed`) | **CONFIRMED, caveated basis.** Sections 2e / 9. The `alive` argument is withdrawn (section 11). |
| 2. Is the inverted-conjunct reading right? | **No.** The draft picked the wrong stated purpose, and the phrase it attacked was incoherent as written. Wording defect in the driver. Sections 2c / 11. |
| 3. Is `H-D` really Mode C? | **No -- labelled fan-out on a git witness** (`ac85c048a2`, 2026-09-04 18:45Z, ~6 h pre-resolution). Section 9. |
| 4. Step 7c not run | **Now run**, cross-model, CONTESTED; it moved findings 1-4 and the routing. |
| 5. GFLAG-0131 disposition | **Stays open, unchanged**, with the random-split truncation qualification added (section 3). |

**What the pass changed, beyond the four defects.** The load-bearing correction is a **premise**:
the staged artifact treated `z_world` as a 32-dim encoding of the 25-dim `resource_field_view`. It
is not -- the encoder reads the **full 250-dim `world_state`** -- and on the wrong premise the
proposed missing control was vacuous by construction and the "ordered portfolio" was a sequential
chain with a decorative first step. **Generalisable guard, recorded in `learning_extracted`:**
before designing an "information-preserving reference" control, check the dimensionality and
identity of the *actual input tensor in the code*, not the field the write-up talks about.

**What the pass did NOT overturn.** H-B's elimination (explicitly uncontested); the arithmetic
(independently recomputed, every figure matched); the GFLAG-0131 verdict for the load-bearing DV;
the per-claim `change`-string tails for INV-088 and MECH-457 (both verified against `claims.yaml`
and kept); the `re_derive_brake` encoding; the `growth_restriction` absence; and the
`epistemic_category: standard` recommendation.
