# Step 7c adversarial red team -- DRAFT failure_autopsy_V3-EXQ-1027-1029-cluster_2026-09-14

MODEL: Opus 5 (1M context), exact id `claude-opus-5[1m]`. Requested as opus; confirmed.
READ ORDER HONOURED: draft JSON -> raw manifests / run packs / drivers / substrate / registry /
prior autopsy / substrate_queue / claims.yaml -> draft markdown last.

## VERDICT

**CONTESTED.**

Every headline number in the draft recomputes correctly from the manifests (see
RECOMPUTATIONS) and the two core dispositions -- 1027 null, 1029 PASS -- survive. What does
not survive is a set of seven specific defects, four of which change a RECOMMENDATION
(the successor's magnitude arm, the Mode A growth, the 1028 read-across, and an un-taken
failure_record disposition) and three of which change what the artifact ASSERTS (an
absolute contradicted by the substrate and by 1029's own cells, a fleet-wide absolute
falsified by four landed drivers, and an arithmetic error in the load-bearing power claim).

---

## FINDINGS

### F1 -- SEVERE, changes a recommendation. The proposed magnitude arm cannot test SD-082's readout; and C4 is not merely "underpowered", it already brackets the achievable range.

**Claim under attack** (JSON `targets[1].failed_criterion`): "C4 (magnitude-only pair,
recorded, suffixes the label) failed 0/5 and is adjudicated below as **UNDERPOWERED BY
DESIGN, not as a null**"; (JSON `suggested_probes[0].sketch`): "Keep the MAG sub-question as
ONE extra runner with **gain set per seed from the realised authority factor**, not a fixed
50."; (md:138) "a successor sets the magnitude arm's gain per seed from the recorded
authority factor, not a fixed 50."

**Evidence.** The readout's output magnitude is hard-bounded by the substrate:
`ree_core/pfc/lateral_pfc_analog.py:479-481` -- `bias = self.config.bias_scale *
torch.tanh(bias_raw / self.config.bias_scale)` with `bias_scale: float = 0.1`
(`lateral_pfc_analog.py:154`). So |bias| < 0.1 for ANY head, trained or not. Measured native
|bias| (m1029 `arm_results[].runners[].lpfc_bias_abs_mean_prebias_gain`) is 0.0037 / 0.0222 /
0.0251 / 0.0296 / 0.0402 -- i.e. **the entire achievable head-magnitude headroom is 2.5x to
27x native**. MAG_GAIN is 50 and is applied AFTER the tanh bound (1029 driver:47-48,
`MAG_GAIN = 50.0` at :259). So the MAG pair already tested a bias 2x-20x BEYOND anything a
trained SD-082 readout can produce, and returned argmin divergence
0.000/0.000/0.017/0.000/0.000 (pooled 6/1694 = 0.35 percent).

**Why it changes the recommendation.** (a) The C4 null is not "underpowered" with respect to
the question that matters. Relative to AUTHORITY's realised factor (72-6543) it is
under-set, which is what the driver's own label rule says (driver:672-674) and is correct on
its own terms -- but the draft then carries that into a MEASUREMENT-DEBT recommendation as
if the magnitude question were open. It is closed from above for every realisable head: x50
is over-powered, not under-powered, against |bias| <= 0.1. (b) The successor arm the draft
licenses would set gain to 72-6543, producing an effective bias of 0.27 to 262 -- between
3x and 2600x the substrate's own `bias_scale` bound. Such an arm tests an arbitrary
rescaling, not SD-082's readout, and its result would be uninterpretable for the claim. The
correct successor design is either to DROP the arm (x50 brackets it) or to set the gain from
the ACHIEVABLE ceiling, `bias_scale / |bias|_native` (2.5x-27x per seed), never from
authority's factor.

**Cheap confirmer.** `sed -n '154p;479,481p' ree-v3/ree_core/pfc/lateral_pfc_analog.py` (the
0.1 tanh bound), then
`python3 -c "import json;m=json.load(open('m1029.json'));print([round(0.1/a['runners']['AUTH_OFF_INTACT']['lpfc_bias_abs_mean_prebias_gain'],1) for a in m['arm_results']])"`
-- prints the per-seed achievable gain ceiling (4.5, 27.2, 4.0, 2.5, 3.4); compare against
MAG_GAIN 50 and against the proposed 72-6543.

### F2 -- SEVERE, changes a recommendation. The proposed new leg substantially duplicates the still-`alive` H1-trained-discriminating-readout.

**Claim under attack** (JSON `hypothesis_space_ledger_plan.mode_a_growth_proposed`): grow
`initial_frozen_count` 9 -> 10 with `H-consequence-trained-readout`; (md:158) "not
circling".

**Evidence.** Registry `hypothesis_space_registry.v1.json`, qid
`sd082_candidate_discriminating_readout_locus`, hypothesis `H1-trained-discriminating-readout`
(state `alive`, `met_elimination_bar: false`): label "The TRAINED rule->bias readout produces
a candidate-DISCRIMINATING raw bias ... **and which is argmax-consequential. Adjudicated by a
TRAINED-MINUS-INIT discrimination index exceeding a margin pre-registered off the random-init
distribution, on new seeds -- NOT by an absolute index floor. Null: the trained index sits
inside the init head's own distribution.**"
The proposed leg: "a rule->action readout whose output participates in E3 selection during P1
... acquires a candidate-discriminating, **argmin-consequential** bias **BEYOND its
initialisation**", with DV = "trained-pair argmin divergence minus init-pair argmin
divergence, per seed" and "Declared null: the difference sits **inside the init pair's own
across-seed spread**". Same assertion, same trained-minus-init contrast, same
inside-the-init-distribution null. The only difference is the TRAINING REGIME (authority ON,
gated_policy ablated) -- a manipulation/design change, not a new hypothesis.

**Why it changes the recommendation.** The question's own `fanout_growth_note` reads
"Denominator has grown twice (5 at registration -> 7 -> 9). This question has NOT converged:
report narrowing against BOTH 5 (original) and 9 (current including fan-out)." Registering a
10th leg that restates the alive 1st leg makes that reporting strictly worse and manufactures
apparent non-convergence. The Step 8 gate should be offered a third option the draft does not
present: **run the successor as a new `adjudicating_run` for the existing `alive` H1 under a
changed training regime**, recorded in H1's `basis`/`adjudicating_runs`, with no Mode A
growth. (`growth_restriction` is `""`, so nothing mechanically stops the growth -- the gate is
the only check.)

**Cheap confirmer.** `python3 -c "import json;d=json.load(open('hypothesis_space_registry.v1.json'));q=[x for x in d['questions'] if x['qid']=='sd082_candidate_discriminating_readout_locus'][0];h=[y for y in q['hypotheses'] if y['hid']=='H1-trained-discriminating-readout'][0];print(h['label']);print(h['desc']);print(h['resolution']['state'])"`
and read it beside `fanout_recommendation.live_hypotheses[0]`.

### F3 -- SEVERE, changes a read-across recommendation and an assertion. The 1028 read-across attributes to 1028 a naivety its own driver pre-registers against.

**Claim under attack** (JSON `read_across_not_adjudicated[0]`): "1028's episode-level
advantage-on-flip statistic ... therefore measures a state-return correlation, not a causal
penalty. **1028's autopsy should read this before crediting a C3 sign.**"; (JSON
`targets[1].learning_extracted[5]` and md:140): "**H-learning-signal-sign's stated mechanism
is not testable in the OFF configuration as worded.**"

**Evidence.** `ree-v3/experiments/v3_exq_1028_sd082_learning_signal_extended_budget.py`:
- lines 90-93: "With `use_modulatory_selection_authority` False the head's bias **never
  changes a committed action** (1020 per_episode_returns bit-identical across arms; **1029
  measures it**), so per-episode return does not depend on the head, and a flip label from the
  FROZEN INIT head is available on every episode of P1."
- lines 110-112: "**Correlational by construction at authority OFF: a flip has no causal path
  to the return; the statistic is about which states produce flips, i.e. the sign of the
  credit REINFORCE receives, which is what the hypothesis asserts.**"

1028 not only knows the premise, it names 1029 as the run that will measure it, and it
asserts that the correlational reading IS the hypothesis's content -- the opposite of "not
testable as worded". 1028's whole C3 redesign (episode-level Pearson r against a local
+/-10-episode advantage, +/-2 SE band, `c3_degenerate` guard) exists because of this.

**Why it changes the assertion/recommendation.** The read-across as drafted (a) tells 1028's
autopsy to correct something 1028 already handles, which will read as an instruction to
discount a correctly-scoped criterion, and (b) states an adjudicative conclusion about
H-learning-signal-sign ("not testable as worded") inside a block the artifact declares
NOT-adjudicated. Correct framing: 1029 CONFIRMS by measurement the premise 1028 assumed from
1020's bit-identity, which strengthens 1028's C3 scoping rather than undermining it. Rewrite
the item to that, and drop "not testable as worded".

**Cheap confirmer.**
`sed -n '89,94p;108,113p' ree-v3/experiments/v3_exq_1028_sd082_learning_signal_extended_budget.py`

### F4 -- MODERATE-SEVERE, changes an assertion repeated eight times. "No causal loop" / "never reaches selection" / "independent by construction" is false as stated; the correct statement is a magnitude fact.

**Claim under attack** (JSON `cluster_pattern.structural_property`, `amend_note`,
`targets[1].learning_extracted[4]`, md:81, md:128): "the rule->bias readout's output **never
reaches E3's selection**"; "**no causal loop** from the readout to the return"; "the return is
**independent** of the head's output"; and (1020 sec 5.1, quoted approvingly at md:19) "a
+/-0.1 tanh-bounded bias ... **can never** change the argmin".

**Evidence.**
1. The substrate APPLIES the bias to the E3 scores when authority is OFF:
   `ree_core/predictors/e3_selector.py:3390` -- "When OFF (default), modulatory biases are
   applied **as-is** (bit-identical to pre-substrate baseline)";
   `ree_core/utils/config.py:1255` -- "Default False (backward compat: **bias applied
   as-is**)". There is no gate removing the readout from `scores`; only the rescale is absent.
2. 1029's OWN cells show that same authority-OFF path IS consequential once the magnitude
   rises: `magnitude_only` pair (AUTH_OFF_INTACT vs MAG_INTACT, authority OFF on both)
   pooled `d_argmin` **31 / 1694** and `d_action_raw_identical` **12 / 1694**; `mag_pair`
   pooled `d_argmin` **6 / 1694**. A structurally absent loop cannot produce 31 argmin
   changes.
3. The 1029 driver says so in terms: **driver:160** -- "DV is **not invariant by
   construction** -- a zero divergence is a **magnitude fact**."

**Why it changes the assertion.** "By construction / never / independent" is a structural
claim; the truth is a quantitative one -- the loop exists and is ~50x below detection at
native magnitude (0/1694 argmin, and 0/13857 sampled actions on the OFF pair). The
distinction is load-bearing for the successor: a structurally absent loop would need a
substrate change, whereas a magnitude-limited one is exactly what authority ON fixes -- which
is the design the draft proposes, so the wording undercuts its own routing rationale. It also
propagates into text governance will write (`amend_note`, `recommended_evidence_quality_note`).
Replace with "empirically inert at native magnitude (0 of 1694 argmin, 0 of 13857 sampled
actions)".

**Cheap confirmer.** `sed -n '3388,3392p' ree-v3/ree_core/predictors/e3_selector.py` and
`python3 -c "import json;m=json.load(open('m1029.json'));print(sum(a['pairs']['magnitude_only']['d_argmin'] for a in m['arm_results']), sum(a['pairs']['magnitude_only']['d_action_raw_identical'] for a in m['arm_results']))"`
-> `31 12`.

### F5 -- MODERATE, arithmetic error inside the load-bearing power claim for `eliminated`.

**Claim under attack** (JSON `targets[0].four_layer_diagnosis.scale`, md:98): "A larger real
effect cannot hide at this scale: the pre-registered margin (~0.07) is **3.7 standard errors
above the observed mean lift**."

**Evidence.** From `m1027.json per_seed[]`: mean lift 0.017757, sd 0.042650, SE 0.019074,
mean margin 0.071724.
- margin / SE = **3.760** (the margin above ZERO) <- the figure the draft printed.
- (margin - mean) / SE = **2.829** <- what "above the observed mean lift" means.
- Paired per-seed test, H0 true lift = that seed's own margin: mean(lift - margin) = -0.05397,
  SE 0.01980, **t(4) = -2.726, one-sided p = 0.026**.

**Why it changes the assertion.** The sentence is the only power argument offered for
`eliminated` over the alternative the draft itself records at the gate ("leave alive as
budget-limited"). At 2.83 SE the margin-sized effect is excluded at roughly p = 0.026, not
comfortably; an effect at 0.7x the margin (+0.050) is NOT excluded (t = -1.69, p ~ 0.08). The
disposition remains defensible on the pre-registered per-seed count (0/5, and only 2 seeds
anywhere near), but the stated number overstates the margin of exclusion by 33 percent and
should be corrected to 2.8 SE / t(4) = -2.73 / p = 0.026 before the Step 8 gate chooses
between `eliminated` and `alive`.

**Cheap confirmer.**
`python3 -c "import json,statistics as s,math;p=json.load(open('m1027.json'))['per_seed'];l=[x['lift'] for x in p];g=[x['lift_margin'] for x in p];se=s.stdev(l)/math.sqrt(5);print('margin/se',s.mean(g)/se,'(margin-mean)/se',(s.mean(g)-s.mean(l))/se)"`

### F6 -- MODERATE, a fleet-wide absolute is falsified, and a GOV-REUSE-1 disposition is missing from the successor.

**Claim under attack** (JSON `targets[1].learning_extracted[4]`, md:139): "SD-082's design doc
names the intended regime ('(b) reinforcement-style gradient from E3 action outcomes') ...
**no run has yet trained the readout in it.**" (Unscoped -- unlike the neighbouring, correctly
scoped "Every P1 run in 822f/1020/1027/1028 trained an imitator".)

**Evidence.** Four landed drivers train `lateral_pfc.bias_head_parameters()` in P1 with
`use_modulatory_selection_authority=True`:
- `experiments/v3_exq_654g_arc062_gapb_rule_apprehension_behavioural_falsifier.py:318-319`
  (`USE_MODULATORY_SELECTION_AUTHORITY = True`, `MODULATORY_AUTHORITY_GAIN = 2.0`), `:351`
  (`LR_LPFC_BIAS = 5e-4`), `:478` (`lateral_pfc_train_rule_bias_head=True`), `:742` /
  `:1006` (optimizer + clip on `bias_head_parameters()`).
- `experiments/v3_exq_699c_pcomp_demotion_x_gonogo_fixed_n.py:1037-1038, :1085, :1236, :1514`.
- `experiments/v3_exq_719_conversion_ceiling_dissociation_diagnostic.py:218-219, :265, :374, :737`.
- `experiments/v3_exq_728_trained_allon_capability_point.py:309-310, :199, :350, :570`.

The correct scoping is "no run has trained the **SD-082 consumer** readout
(`lateral_pfc_rule_readout_consumer=True`) in that regime" -- none of the four sets that flag
(they run `candidate_summary_source="e2_world_forward"` and the pre-SD-082 hard-clamp path).

**Why it changes the assertion/recommendation.** (a) As written the absolute is false, and it
is the sentence carried into the substrate-queue `amend_note` text governance will land. (b)
The successor's `/queue-experiment` Step 2.4 GOV-REUSE-1 check must now dispose of this family
explicitly -- it is the nearest prior art on "train the lpfc bias head with authority ON", and
those runs use gain **2.0**, four times 1029's 0.5, which is directly relevant to the
successor's gain choice. 1029's own Step 2.4 disposition (driver:171-175) checked only 1020
and 949 and did not see it. The autopsy should name this in `suggested_probes`.

**Cheap confirmer.**
`/usr/bin/grep -n "USE_MODULATORY_SELECTION_AUTHORITY = True" ree-v3/experiments/v3_exq_{654g*,699c*,719*}.py ; /usr/bin/grep -rln "bias_head_parameters" ree-v3/experiments/`

### F7 -- MODERATE, an available finding is not extracted and an open failure_record item is left undispositioned.

**Claim under attack** (JSON both targets): `resolves_prior_failure_record: []`; and
(`read_across_not_adjudicated[1]`) "1027's elimination of the credit-assignment rival
**strengthens whatever 1028 finds** on persistence."

**Evidence.** `substrate_queue.json` SD-082 `failure_record[]` carries an OPEN entry for
`v3_exq_1020_sd082_learning_signal_probe_...` whose `target` is verbatim: "every cell clears
>=20 fresh-select flip samples so C3 is scoreable; **C2 majority robust to seed with the
replay rule_state mismatch controlled**." 1027 controlled exactly that, and its own cells
answer the second clause. Recomputed from `m1027.json arm_results[]` (persistence_pooled vs
the 1020 C2 midpoint `(persistence_floor + persistence_ceiling)/2`):

| seed | midpoint | FAITHFUL | below? | OWN | below? |
|---|---|---|---|---|---|
| 611 | 0.5907 | 0.6523 | no | 0.6218 | no |
| 622 | 0.5890 | 0.4059 | yes | 0.4754 | yes |
| 633 | 0.6030 | 0.5582 | yes | 0.5595 | yes |
| 644 | 0.5859 | 0.4815 | yes | 0.5366 | yes |
| 655 | 0.5926 | 0.6196 | no | 0.6131 | no |

**3 of 5, on the identical seeds 622/633/644, in BOTH arms** -- a bit-for-bit reproduction of
1020's C2 reading (1020 autopsy learning 4: "C2 passes on a BARE MAJORITY and on the SAME
three seeds in both arms (622, 633, 644); seeds 611 and 655 sit ABOVE their midpoints in both
arms"), now with the replay rule_state mismatch controlled.

**Why it changes the assertion/recommendation.** (a) The open 1020 failure_record item is
half-discharged by 1027 and should be dispositioned in the `amend` (partially resolved, with
this table), not left untouched with `resolves_prior_failure_record: []`. (b) The read-across
is under-claimed: 1027 does not merely "strengthen whatever 1028 finds", it independently
REPRODUCES the persistence-low majority at T=70 with the rival controlled -- and the fact that
it lands on the SAME three seeds across two independent experiments makes seed identity, not
the credit path, the candidate explanatory variable. That is a seed-level confound the
successor's per-seed design should pre-register against, and it is not in the draft.

**Cheap confirmer.**
`python3 -c "import json;m=json.load(open('m1027.json'));[print(a['arm_id'],a['seed'],round((a['persistence_floor']+a['persistence_ceiling'])/2,4),round(a['persistence_pooled'],4),a['persistence_pooled']<(a['persistence_floor']+a['persistence_ceiling'])/2) for a in m['arm_results']]"`

---

## RECOMPUTATIONS

All from the flat manifests, independent of the draft.

**V3-EXQ-1027** (`per_seed[]`, `arm_results[]`):
| quantity | recomputed | draft | match |
|---|---|---|---|
| C1 count (lift >= margin AND summary_column_lift > 0, eligible) | 0 | 0/5 | yes |
| C2 count (lift <= -margin, eligible) | 0 | 0/5 | yes |
| per-seed lifts | -0.03058 / +0.06952 / +0.00124 / +0.05514 / -0.00653 | -0.031/+0.070/+0.001/+0.055/-0.007 | yes |
| per-seed margins | 0.07097 / 0.07011 / 0.07712 / 0.06852 / 0.07189 | 0.069-0.077 | yes |
| mean lift / SE / t(4) | +0.017757 / 0.019074 / 0.931 | +0.018 / 0.019 / 0.93 | yes |
| margin above observed mean, in SE | **2.829** | **3.7** | **NO -- see F5** |
| bracket (ceiling - floor) | 0.2741-0.3085 | 0.27-0.31 | yes |
| mean lift as fraction of bracket | 6.2 percent | "~6 percent" | yes |
| worst headroom minus margin (seed 611) | +0.009379 | +0.009 | yes |
| OWN direction mismatch range | 0.5006-0.6988 | "0.50-0.67" | **no (upper end is 0.70)** |
| norm-inclusive mismatch | 0.9703-1.1809 | 0.97-1.18 | yes |
| P1 buffer SHA-256 equal across arms | 5/5 | 5/5 | yes |
| per-episode returns equal across arms | 5/5 | 5/5 | yes |
| summary-column lifts | -0.0038/+0.0025/-0.0120/+0.0477/-0.0070 | -0.012..+0.048 | yes |
| rule-column delta (OWN - FAITHFUL) | -0.071/+0.173/+0.072/+0.078/+0.074 | "rises ~0.07 on 4/5" | direction yes; seed 622 is +0.173 |
| synth control gain / ceiling | +0.00242..+0.00356 / 0.7229-0.7573 | +0.0024..+0.0036 / 0.723-0.757 | yes |
| fallback calls / non-finite grads | 0 / 0 (all 10 cells) | 0 / 0 | yes |
| C1 reachable without marginal seeds? | yes -- seeds 622/633/644 have headroom 2.6x-4.6x margin | (not stated) | criterion NOT degenerate by construction |

**V3-EXQ-1029** (`arm_results[].pairs`, `.runners`), pooled over 5 seeds (1694 raw-identical
co-fresh ticks; 13857 total ticks):
| pair | d_argmin / 1694 | d_action (raw-identical) | d_action (all ticks) |
|---|---|---|---|
| off_pair | **0** | **0** | **0 / 13857** |
| on_pair | 162 | 69 | 540 |
| mag_pair (x50) | 6 | 1 | 10 |
| self_off / self_on | 0 / 0 | 0 / 0 | 0 / 0 |
| authority_only | 923 | 310 | 2525 |
| magnitude_only (x50 vs native, both OFF) | 31 | 12 | 98 |

| criterion | recomputed | draft | match |
|---|---|---|---|
| C1 (ON pair >= 0.02) | 4 (0.2615/0.0271/0.0144/0.0821/0.1155) | 4/5 | yes |
| C2 (OFF pair <= 0.005) | 5, all exactly 0.0 | 5/5, 0 of 1694 | yes |
| C4 (MAG >= 0.02) | 0 (0/0/0.01729/0/0) | 0/5 | yes |
| authority_scale_factor_median (AUTH_ON_INTACT) | 754.9 / 6542.9 / 72.3 / 2975.5 / 2039.6, **median 2039.6** | 755/6543/72/2976/2040, median 2040 | yes |
| |bias| / raw score range | 0.003965 / 0.000377 / 0.001291 / 0.001585 / 0.001723 | 0.0004-0.0040 | yes |
| raw E3 score range | 2.853 / 5.592 / 17.197 / 25.375 / 66.604 (23.3x spread) | 2.85-66.6, "23x" | yes |
| authority_only divergence | 0.342-0.809 | 0.34-0.81 | yes |
| ON-pair sampled-action divergence | 0.000-0.0749 | 0-7.5 percent | yes |
| head-flip fraction, intact runners | **0.162-0.408** | "16-26 percent" | **no -- seed 622 is 0.340/0.408** |
| committed_fraction | 0.0 on all 40 runners | 0.0 | yes |
| raw-identical fraction of co-fresh | **1.0 in all 35 pair-seed cells** | (asserted as a filter) | see hygiene H6 |

**Cross-leg substrate provenance (attack (d) -- FAILED, the draft is right).**
`git -C ree-v3 diff --name-only 42c03b1485 64d9ee07c8` returns exactly four paths:
`experiment_queue.json` and three NEW experiment drivers (1012a, 1037, 1038). No `ree_core/`
file changed between the two legs. The draft's `recording_provenance` note is correct and the
cluster's cross-leg inference is safe on this ground.

**An independent confirmation the draft does NOT use (in its favour).** Within 1027 alone,
the two arms' heads measurably diverge -- `n_fresh_flip_ticks / n_fresh_select_ticks` is
84/373 (FAITHFUL) vs 70/373 (OWN) on seed 644, 19/186 vs 13/186 on seed 622 -- while
`per_episode_returns` are bit-identical and `p1_buffer_sha256` matches on 5/5 seeds, across 70
ONLINE P1 episodes in which the heads were being trained apart from episode 2. That is a
within-1027 demonstration that the head's output had no behavioural consequence, independent
of 1029. It is stronger evidence for the cluster's core claim than the argument the draft
actually makes, and it should be in `learning_extracted`.

---

## MINOR HYGIENE (does not move the verdict)

- **H1.** Citation `x1020._reinforce_step, driver:656-657` (JSON x2, md:81) is off by one: the
  surrogate is at `v3_exq_1020_sd082_learning_signal_probe.py:657-658`
  (`log_p = F.log_softmax(-bias / POLICY_TEMPERATURE, dim=0)` /
  `terms.append(-adv * log_p[min(sel_idx, bias.shape[0] - 1)])`).
- **H2.** "direction mismatch 0.50-0.67" (JSON `implementation` layer, `learning_extracted[0]`)
  should be 0.50-0.70 (`buffer_direction_mismatch_mean` seed 655 = 0.6988).
- **H3.** `read_across_not_adjudicated[2]` (H2-uniform-common-mode): "16-26 percent" should be
  16-41 percent -- seed 622's intact runners read 0.340 (OFF) and 0.408 (ON). The 0.162 figure
  is the R2 gate's MIN, not the range.
- **H4.** `learning_extracted[1]` says rule-column persistence "rises by ~0.07 on 4/5 seeds"
  and then lists 0.403->0.576, i.e. +0.173 on seed 622. Three of the four are ~0.07; say
  "+0.07 to +0.17".
- **H5.** `pre_routing_checks.fire_count: 3` but `fires[]` has 2 entries (the C1 entry carries
  two queue_ids). Defensible but a reader counting entries gets 2; state it.
- **H6.** The ON-pair interpretability defence rests on the raw-identical filter excluding
  post-divergence state echo. The filter retained **100 percent of co-fresh ticks in all 35
  pair-seed cells** -- it never excluded a single tick. State echo was prevented by the
  observation-yoking (every runner stepped on the reference's observation), not removed by the
  filter; the filter is vacuously satisfied. Worth saying plainly, because "the filter
  excluded it" implies the filter did work it did not do.
- **H7.** `four_layer_diagnosis.biological_reference` for 1027 cites "0 of 1694 argmin changes
  at native magnitude" as the reason the biological dependency was absent; that measurement is
  on 1029's INIT head. A trained head can reach up to 2.5x-27x that magnitude under the tanh
  bound (F1). The conclusion survives (mag_pair at x50 gives 6/1694), but the transfer step
  from init-head 1029 to trained-head 1027/1020 is currently unstated.
- **H8.** `1027 four_layer_diagnosis.prerequisites` reads "missing"; `failure_location` then
  reads "HYPOTHESIS ELIMINATED ... Implementation, Measurement and Environment each
  independently adequate". A `missing` prerequisite layer alongside an `eliminated` verdict is
  internally consistent only because the missing prerequisite is the one the hypothesis
  presupposed; say so in the net_classification, or a governance reader will read the two as
  contradictory.
- **H9 (not a defect -- checks that PASSED).** substrate_queue SD-082 `validation_experiment`
  currently ends at 1020 and names neither portfolio leg, so the `amend` is NOT a duplicate.
  claims.yaml SD-082 stored fields match the draft exactly (`candidate_substrate_landed`,
  `standard`, `pending_retest_after_substrate: false`, `diagnostic_evidence_adjudicated: true`,
  `live_status.evidence.from = failure_autopsy_V3-EXQ-1020_2026-09-11`). "The substrate exposes
  only `bias_head_parameters()` -- the loop is driver-owned" is confirmed: every caller in the
  tree is an experiment driver, there is no substrate-side training loop
  (`/usr/bin/grep -rn bias_head_parameters ree_core/`). The re-derive-brake count of 3
  (822b/822c/822d) matches the substrate_queue and the 1020 autopsy.
