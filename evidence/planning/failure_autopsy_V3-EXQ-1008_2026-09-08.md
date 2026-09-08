# Failure autopsy -- V3-EXQ-1008 (z_world actor-adequacy locus: the owed H-C corroborator + the H-E channel-input control)

**Generated:** 2026-09-08T05:31:03Z - **Confirmed:** 2026-09-08T06:18:57Z by `user gate (interactive), session failure-autopsy-exq1008-20260908`
**Status:** `confirmed` (Step 7b run, 0 fires; Step 7c adversarial pass RUN -- verdict CONTESTED, all 9 findings applied; Step 8 interactive gate HELD; Step 9b registry writes APPLIED)
**Scope:** single - **Target:** `v3_exq_1008_zworld_adequacy_portfolio_ws250_rebasis_20260907T233826Z_v3` - **Purpose:** diagnostic - **Outcome:** PASS
**Claims tagged:** NONE (`claim_ids: []`, deliberate) - **Bears on:** INV-088, MECH-457 - **Machine-readable:** `failure_autopsy_V3-EXQ-1008_2026-09-08.json`
**Question:** `zworld_actor_adequacy_locus` (frozen ledger; registered 2026-09-03, grown 2026-09-05)
**Supersedes in part:** `failure_autopsy_V3-EXQ-1002_2026-09-05` -- this run is the two-leg portfolio that artifact commissioned, and it WEAKENS the H-C leg that artifact confirmed.

---

## 0. The one-paragraph verdict

At **identical width (32 dims), identical reader, identical banked steps and identical standardiser**, a
fixed task-agnostic **PCA-32 of the encoder's own 250-dim input reaches 0.868** held-out oracle-action
agreement (3/3 seeds clear the 0.80 bar) while the **trained z_world reaches 0.669** (0/3), and a **random
orthonormal 32-dim projection of the same input reaches 0.772**. **H-E-channel-input-capacity is
ELIMINATED**: the deficit is not a 250->32 width bound. Three independent information-preserving linear
re-bases of the frozen latent are seed-majority **flat**, and the closed-form content witness -- the
oracle's own argmax rule applied to the linearly decoded field, no adapter -- **degrades** to 0.593/0.591/
0.607 against a 0.566/0.580/0.572 trivial baseline, so **H-C-geometry-mismatch is WEAKENED at its own
pre-registered branch**. Read together on a fully green instrument: **the deficit is neither channel WIDTH
nor readout GEOMETRY -- the observation->z_world encoding discards the decision-relevant content of its own
input.** Two qualifications are recorded rather than smoothed: the two whitening arms lift **consistently
3/3 in the positive direction** (ZCA +0.039, LDA +0.043 mean) -- a real geometry effect worth about a third
of the ~0.13 needed to reach the bar, so "geometry contributes nothing" is too strong -- and every leg-2
re-basis is **function-class-preserving by algebra**, so leg 2 measures learning dynamics and the content
witness measures LINEAR content only. **Whether the content survives NONLINEARLY, recoverable by an
over-capacity decoder, is unmeasured by this run and by every run in the lineage.** That single missing fact
gates two candidate builds whose costs differ by more than an order of magnitude, and it is the routing.

---

## 1. Facts (no interpretation)

**Provenance.** `ree-worker-3`, `linux-x86_64-py3.10-torch2.12.0+cpu`, 32,259.6 s (8 h 58 m), 3 seeds
(42/43/44), level `W3_survival_zeroed`, rung `D3_hazard_free`, `substrate_hash 875d3044d5...`,
`recording_schema rec/v1`. `validate_recording.py`: **OK, no always-core gaps, no thin-pack provenance
drop, no schema warnings.** There is therefore **no recording gap** to route.

**Dry-run gate (Step 2a), run before any metric was read.** `check_dry_run_citations.py` on the target
run_id and `V3-EXQ-1008`: 0 dry cited, 0 ambiguous, **1 clean**, exit 0. Family sweep `--family
v3_exq_1008`: **0 dry / 1 real**. No truthy top-level `dry_run`. *Criterion reachability:* the driver's dry
path sets `DRY_RUN_SEEDS=[42]` against `SEED_MAJORITY=2`, which forces `seeds_sufficient=False` and
structurally zeroes every `*_clears` and every lift class -- **a dry run of this driver can reach no verdict
at all**, so a dry manifest could never be mistaken for this one. `excluded_dry_run_ids: []`.

**Design.** Ten arms x three seeds. The dataset is re-collected from V3-EXQ-1002's deterministic recipe and
**all arms read the same stored steps**; the only thing varied is **the adapter's input representation**.
The adapter *is* `x734.PPOPolicyNet` at `x734.PPO_TRUNK_HIDDEN` (128), and every 32-dim arm carries
**identical action-path parameter counts (21,381)**; `rawfield_ceiling` (25 dims, 20,485) is conservatively
*under*-powered and `ws250_full` (250 dims, 49,285) is a **readiness anchor only, never a verdict arm**.
Adapter init is re-seeded from the cell seed before every fit. `ADAPTER_PASSES = 60`. The frozen OFF latent
is **reproduced** by re-running V3-EXQ-978's warmup (60 P0a + 200 P0 + 90 P1 episodes/seed), not loaded from
a checkpoint -- 978 and 1002 saved none -- so every leg-2 threshold is applied to the **in-run** baseline.

**That reproduction is BIT-IDENTICAL to V3-EXQ-1002's, and this artifact's draft got it wrong before the
Step 7c pass corrected it.** Both manifests carry `zworld_encoder_trained_in_p0` = **0.28158509731292725**
and `zworld_not_collapsed` = **4.222778806991767** (OFF) / **7.492851658629209** (untrained) to full double
precision, the same held-out split (2,148 / 2,061 / 1,965), and a **bit-identical `rawfield_ceiling` arm on
all three seeds** (0.984636843 / 0.979621530 / 0.973028004). The dataset recipe and both warmups reproduce
deterministically and bit-exactly; the **only** thing re-drawn is the adapter initialisation (the per-cell
`reset_all_rng(seed)`), which is why only the z arms' `final_ce_loss` differs. Two consequences, both
carried forward rather than smoothed. **(i)** This run is **not** a second independent instance of anything
the warmup produces -- see section 7 for what that costs the H-D read. **(ii)** The driver docstring and the
manifest's own `frozen_latent_source.reproduced_not_loaded` justify "not a bit-identical replay" partly on
the ground that *"the machine class differ"*. **They do not** -- both runs declare
`linux-x86_64-py3.10-torch2.12.0+cpu` (`ree-cloud-2` and `ree-worker-3` are the same declared class). That
string is provenance a later session will read; it is wrong and should be corrected at source. What the two
runs *do* differ in is `substrate_hash` (`5125cc63eb...` vs `875d3044d5...`), so the bit-identical warmup
output additionally shows that whatever landed between them does not touch the observation->z_world path.

**`ws250` means 250 DIMENSIONS, not a window.** `world_state` under `use_proxy_fields=True` is
local_view 5x5x7 one-hot `[0:175]` + contamination_view `[175:200]` + hazard_field_view `[200:225]` +
resource_field_view `[225:250]`. The oracle (`local_view_greedy`) reads exactly **five** coordinates,
`{232, 236, 237, 238, 242}`. On the training splits: numeric rank 129/129/128, participation ratio
14.1/15.0/14.7, top-32 PCs carry 0.865/0.860/0.862 of the variance (78 PCs for 0.99).

**Primary DV -- held-out top-1 agreement with the oracle's action.** Bar = `max(0.80, trivial+0.20)`;
"clears" requires bar **and** >= 0.20 elevation on >= 2 of 3 seeds.

| arm | what it is | seed 42 | seed 43 | seed 44 | mean | seeds clearing | cloned res/ep |
|---|---|---|---|---|---|---|---|
| `rawfield_ceiling` | raw 25-dim field (positive control) | 0.9846 | 0.9796 | 0.9730 | **0.9791** | 3/3 | 51.50 |
| `ws250_full` | uncompressed 250-dim input (readiness anchor) | 0.9399 | 0.9335 | 0.9425 | **0.9387** | 3/3 | 50.73 |
| `ws250_pca` | **PCA-32 of the 250-dim input (LEG 1 VERDICT ARM)** | 0.8771 | 0.8578 | 0.8702 | **0.8684** | **3/3** | 43.83 |
| `ws250_randproj` | random orthonormal 32-dim projection of it | 0.7863 | 0.7865 | 0.7445 | **0.7725** | 0/3 | 26.83 |
| `zworld_off_ldawhiten` | frozen OFF latent, Fisher whitening | 0.7142 | 0.7069 | 0.7130 | **0.7114** | 0/3 | 24.45 |
| `zworld_off_zca` | frozen OFF latent, ZCA whitening | 0.7114 | 0.7031 | 0.7089 | **0.7078** | 0/3 | 23.83 |
| `zworld_untrained_diag` | UNTRAINED latent (negative control) | 0.6988 | 0.6812 | 0.7038 | **0.6946** | 0/3 | 17.50 |
| `zworld_off_diag` | **frozen TRAINED OFF latent (LEG 2 BASELINE)** | 0.6718 | 0.6735 | 0.6606 | **0.6686** | 0/3 | 16.23 |
| `zworld_off_fielddecode` | **OFF latent, ridge field-decode re-basis (LEG 2 VERDICT ARM)** | 0.6755 | 0.6541 | 0.6672 | **0.6656** | 0/3 | 16.33 |
| `zworld_untrained_fielddecode` | untrained latent, same re-basis | 0.6625 | 0.6604 | 0.6702 | **0.6644** | 0/3 | 16.07 |

Trivial baseline (repeat-previous-executed-action) 0.5661 / 0.5803 / 0.5720; oracle demonstrator anchor
45.75 res/ep on the worst seed; oracle majority-class share 0.2539 against a 0.60 ceiling; held-out labelled
steps 1,965 on the worst seed against a 500 floor.

**Every readiness gate is green.** `per_arm_gate.all_green` true, `red_arms []`, `dv_headroom_gate_green`
true, `seeds_sufficient` true, and **`criteria_non_degenerate` is true on ALL TEN criteria**. *Read that
flag for what it is:* `arm_criteria_non_degenerate` tests arm liveness and non-nullity -- whether the arms a
criterion reads are green and the per-seed quantity is not `None` -- and carries **no counterfactual
reachability content**. It is not a warrant that each criterion could have gone either way, and this
artifact does not use it as one. Reachability is established **per criterion where it matters**: section 3
does it for leg 1 (the `ws250_linear_compression_fails_bar` branch was fully realisable and did not fire),
and section 4 does it for leg 2 by pointing at the content witness rather than the re-basis. Indeed two of
the ten -- `C_rebasis_lifts_by_margin` (>= +0.10) and `C_rebasis_clears_bar` (+0.13 from optimisation
dynamics alone) -- look close to **unreachable for this manipulation class**, given the driver's own
authoring-time calibration of re-basis effects at -0.003 to -0.047. That is a reason the leg-2 verdict rests
where it does, not a defect.

**Which criteria passed and failed.** Both **load-bearing** criteria passed (`C_leg1_adjudicated`,
`C_leg2_adjudicated`); `outcome = PASS` iff both legs reach a verdict, and the driver states in terms that
"the science is in the labels and `hypothesis_verdict`, not in PASS/FAIL". The five criteria reading false
are all non-load-bearing **discriminating readouts**: `C_ws250_randproj_clears_bar` (0/3),
`C_ws250_pca_beats_randproj` (1/3), `C_rebasis_lifts_by_margin` (flat), `C_rebasis_clears_bar` (0/3),
`C_linear_content_supports_mapping` (degrade).

**Leg-2 detail -- the paired lifts over `zworld_off_diag`.**

| re-basis | seed 42 | seed 43 | seed 44 | mean | class |
|---|---|---|---|---|---|
| field-decode (verdict arm) | +0.0037 | -0.0194 | +0.0066 | **-0.0030** | flat |
| ZCA whitening | +0.0396 | +0.0296 | +0.0483 | **+0.0392** | flat |
| LDA (Fisher) whitening | +0.0424 | +0.0335 | +0.0524 | **+0.0428** | flat (seed 44 marginal) |
| field-decode on the UNTRAINED latent | -0.0363 | -0.0209 | -0.0336 | **-0.0302** | flat |

Bands: lift >= 0.10, marginal >= 0.05, flat > -0.05, degrade otherwise. **Closed-form content witness**
(the oracle's own rule applied to the linearly decoded field, no adapter): 0.5931 / 0.5910 / 0.6066 on the
OFF latent, `content_margin_over_diag` -0.0787 / -0.0825 / -0.0539, class **degrade** on 3/3.
`reader_short` false on 3/3 (`reader_shortfall_on_decoded_basis` -0.082 / -0.063 / -0.061).

**`rebasis_witnesses` (recorded, explicitly NOT gates).** Held-out field-decode r2 absolute deltas across
the re-bases are 0.0 to 2.7e-07, i.e. the re-bases are invertible to numerical precision; condition numbers
29.97-30.24 (LDA), 68.07-102.14 (ZCA), 2455-8902 (field-decode).

**Substrate stability.** `per_cell_hashes_disagree` false, one distinct cell substrate hash,
`drifted_since_resolved` false. `process_snapshot_drift` records two repo-root hash changes on the worker
resolved at 2026-09-07T14:41:33Z -- the box's checkout moved during the 9 h run -- but **every executed
cell carries the same fingerprint**, so the executed substrate was stable. Recorded as a fact, not a
finding.

---

## 2. What the driver actually decides, and the two objections it pre-empts

**LEG 1's verdict does not depend on the PCA-minus-random margin, and that is deliberate.** The adjudicator
is `_adjudicate_leg1(gate_green, leg1_ready, pca_clears, rand_clears)` -- **four booleans, and the margin is
not among them**. `C_ws250_pca_beats_randproj` cleared on 1 of 3 seeds and is reported as attribution only.
The driver's stated reason: in V3-EXQ-1002 the margin protected the H-B label from an untrained projection
that also cleared the bar, i.e. it protected *attribution to the warmup*; in leg 1 a random compression
**also** clearing the bar would **strengthen** the H-E elimination ("any task-agnostic 32-dim linear
compression of the input supports the mapping"), so gating on it would refuse the leg's strongest answer.
This is a correct design decision and this autopsy does not reopen it. What it does mean is that the
elimination delivered is the **plain** one, not the **strong** one: `randproj` at 0.772 sits below 0.80, so
what is established is that *the variance-optimal* linear compression suffices, not that *any* does.

**LEG 2 cannot measure information, only learning dynamics -- by algebra, and the driver says so.** Every
leg-2 arm is an **invertible linear 32x32** map applied before the same adapter, and any such map is
absorbed by the adapter's first layer (`W' = W R^-1`). The function class is therefore **identical** across
leg-2 arms and the information content is identical **by algebra**; a lift can come only from optimisation
dynamics. This is stated in the driver's own docstring, and it is why the WEAKENED branch is gated on the
**closed-form content witness** also failing to lift, not on the re-basis flatness alone. The consequence
for reading this run is important and cuts both ways: *a flat re-basis is not by itself evidence about
information* (an autopsy that read it as such would over-claim), and equally *the weakening of H-C rests on
the content witness*, which is a LINEAR decode. Section 4 carries what that leaves unmeasured.

---

## 3. Central adjudication (1): is H-E eliminated?

**Yes, on its registered gate, and the gate was reachable in both directions.** H-E as registered reads:
*"A task-agnostic 32-dim compression of the full 250-dim world_state cannot support the mapping under this
reader; the deficit is a channel-INPUT bound and no rotation of z_world can fix it. ELIMINATED if
ws250_pca clears the bar; CONFIRMED if neither compression does while the uncompressed input can."*
`ws250_pca` clears bar **and** the >= 0.20 elevation on 3/3 seeds (0.877 vs trivial 0.566 = +0.311 on seed
42), the readiness anchor `ws250_full` clears at 0.939, the instrument gate is green, and the
`ws250_linear_compression_fails_bar` branch -- H-E CONFIRMED -- was fully realisable and did not fire.
`criteria_non_degenerate` is true on the criterion. **The deficit is not dimensionality.**

**One internal tension, checked and not a defect.** `pca_decision_subspace_retention_max` is ~0.288, i.e.
the PCA basis retains under 30% of the norm of the five oracle-decision coordinates -- *less* than the
random projection retains (0.30-0.42) -- while scoring 0.096 *higher*. Two things follow. First, this is
the `decision_subspace_retention_ceiling` guard (0.95) doing its job in the intended direction: it exists to
refuse a "compression" that trivially retains the decision cells, and at 0.288 the PCA arm is nowhere near
that. Second, retained-norm on five raw coordinates is evidently **not** the operative quantity -- the
mapping is recoverable through the correlated local_view block, which is 70% of the input. Recorded as a
fact about what the retention readout does and does not license, not as a challenge to the verdict.

---

## 4. Central adjudication (2): what exactly does the weakened H-C leave standing?

**H-C's registered weakening branch fired correctly.** The hypothesis reads: *"CORROBORATED by a >= 0.10
paired lift under the decode re-basis ...; WEAKENED by a flat/degrading result whose closed-form content
witness is itself flat -- the block is then information, not geometry."* The verdict arm is flat
(-0.0030 mean), the two secondary whitenings are flat, the untrained pair is flat, and the content witness
**degrades** on 3/3. Every conjunct of the registered WEAKENED branch is satisfied on a green instrument.

**But "information, not geometry" is a statement about LINEARLY decodable information, and the artifact
must say so.** Three things bound it:

- **(a) Geometry is not nothing.** The two whitening arms lift **consistently positive on 3/3 seeds each**
  (ZCA +0.0392 mean, LDA +0.0428 mean). They are binned *flat* because the 0.05 marginal band is reached by
  **one LDA seed and no ZCA seed** (ZCA's largest is +0.0483) -- correct on the pre-registered terms. Against the **~0.131** needed to lift 0.669 to the
  0.80 bar, a decision-relevant (Fisher) whitening buys about **a third** of the gap. The honest prose is
  "geometry contributes about a third of what is needed", not "geometry contributes nothing". **And that
  third is a FLOOR, not a point estimate.** The leg-2 *verdict* arm (ridge field-decode) is by far the
  worst-conditioned of the three re-bases -- per-seed condition numbers **2,455-8,902**, against 68-102
  (ZCA) and 29.97-30.24 (LDA) -- while the driver's own authoring-time calibration measures a random
  invertible reweighting of the raw field costing **-0.025 at condition number 20 and -0.047 at 100**, i.e.
  conditioning penalties of the same order as the whole effect under test. The conditioning gate was
  **demoted to a recorded witness** (`rebasis_witnesses`) because it could not fire, so nothing in the run
  protects the verdict arm from conditioning-induced suppression. The WEAKENED verdict survives (it is
  jointly gated on the content witness, which degrades 3/3) -- but the geometry contribution is bounded
  below, not measured.
- **(b) The content witness is a LINEAR decode.** It says the *linearly* decodable field content, pushed
  through the oracle's own rule, reaches 0.593-0.607 against a 0.566-0.580 trivial baseline. It does not
  and cannot speak to content recoverable only nonlinearly.
- **(c) The strongest nonlinear reader in the run is capacity-matched by design.** `zworld_off_diag` **is**
  a nonlinear decoder of z_world (32->128->action) and reaches 0.669 -- and it *beats* the closed-form
  witness by 0.054-0.083. That gap is **suggestive of, but does not isolate, nonlinear content**: the two
  readers differ in *two* ways, not one -- learned-vs-fixed rule as well as nonlinear-vs-linear, since the
  witness applies the oracle's hand-specified argmax to a noisy linear decode while the adapter is *fitted*.
  A fitted **linear** softmax on the frozen latent would plausibly also beat 0.593, and this run contains no
  such arm (all ten arms share the same 32->128 reader). The recommended probe now carries one, at the
  bottom rung of its sweep, precisely to separate them. What no run in this lineage has done is **vary the
  reader's capacity**: 1008 held it fixed at the consumer's exact width as a deliberate `capacity_match`
  requirement inherited from 1002.

**So the residual question is sharp, single and unmeasured: is the decision-relevant content recoverable
from the frozen latent by an over-capacity decoder?** That is the routing (section 8), and it is the fact
that separates the two candidate builds.

**The correction this run forces on its own lineage.** V3-EXQ-978 measured field decode r2 **0.710** (sense
path) / **0.858** (encoder path) from z_world, and its own null table concluded *"z_world already carries
the field, so ... the deficit is in the CONSUMER, not the encoder recipe."* This run applies the oracle's
own argmax rule to that same linearly decoded field and gets **0.593** against a **0.566** trivial baseline.
The two are compatible: r2 averages over 25 field coordinates while the oracle reads five and takes an
argmax, so a decode that is good on average can be worthless exactly where the decision lives. **A bulk
decode r2 is not evidence of decision-relevant content adequacy**, and this lineage came close to routing a
build on that inference.

---

## 5. Biological-reference triage

**Closest reference mechanism: DiCarlo-style ventral-stream manifold untangling** -- two entries already in
the corpus (`targeted_review_perceptual_manifold_adaptors/.../dicarlo2012`, `targeted_review_sd_015/.../
dicarlo2007`), `lit_status: present` for the principle. **The reference is not a formal-definition import**:
untangling is a mechanism claim about a real cascade, not a Pearl/Shannon/optimal-control construct, so the
"formal import with no biology" failure mode does not apply here.

**This run SHARPENS the reference read rather than confirming 1002's.** An untangling failure predicts
content that is *present but badly arranged* -- exactly H-C, and exactly what a re-basis should partly fix.
The re-bases buy a third of the gap and the linear content witness degrades. The signature is therefore
closer to **discarding than to tangling**: the encoder is not failing a hard reshaping problem, it is
dropping content on the floor. Under the skill's core principle that remains a **discovered prerequisite,
not a falsification** -- biology's untangling cascade has an objective *whose job is that reshaping* and a
**dorsal, action-formatted stream distinct from the ventral recognition stream**, and REE has neither:
`z_world` is trained for sensory prediction (SD-056 e2 world-forward contrastive) plus the SD-018 auxiliary
field head, and every consumer reads the one shared prediction-trained latent.

**The inversion that keeps this tractable, inherited from 1002 and now stronger.** The SD-015 DiCarlo entry
predicted *"A 2-layer MLP can likely extract resource type from this input without needing the
hierarchical, multi-stage architecture that biology requires."* The positive control confirms it at 0.979
from the raw field -- and this run adds that a **fixed linear PCA-32 of the full input** already gets to
0.868. **The task's representation problem is close to trivial; REE's encoder is making it hard.**

**Lit gap, secondary and unchanged in identity but stronger in weight.** No `targeted_review_*` covers
*"does biology route action selection through a single shared prediction-trained latent, or maintain a
separate action-formatted stream?"* 1002 recorded this gap; the discarding read points at it more directly,
because a separate action-formatted stream is precisely the dependency whose absence would produce
discarding. Not this autopsy's primary route.

---

## 6. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **n/a** (claim-free) | `claim_ids: []` by design; INV-088 / MECH-457 are `bears_on` relations, neither mechanism exercised |
| Biological reference | **clear** | DiCarlo untangling; signature narrowed from *tangling* to *discarding*; missing-dependency read (no objective preserves action-relevant content; no action-formatted stream) |
| Prerequisites | **present** | encoder trained, latent non-collapsed, oracle clears the demonstrator floor (45.75 res/ep), 1,965 held-out steps, 3 seeds, majority satisfied |
| Implementation | **complete** | adapter *is* `x734.PPOPolicyNet` at the consumer's width; 21,381 action-path params on every 32-dim arm; init re-seeded per fit; one distinct cell substrate hash; `validate_recording` OK |
| Environment | **adequate** | the mapping exists in the same stored steps and three non-REE readouts clear the bar (0.979 / 0.939 / 0.868) |
| Measurement | **under-instrumented (narrowly, and in a NEW place)** | 1002's debt is **discharged** -- a 32-dim reference of the encoder's *actual* input now exists and clears. The residual: leg 2 is function-class-preserving by algebra so it can only measure learning dynamics, and the content witness is a LINEAR decode; **nonlinear recoverability at above-consumer capacity is unmeasured across the whole lineage** |
| Integration | **isolated by design** | BC from oracle labels severs the consumer from the representation -- the manipulation, not a defect |
| Scale / capacity | **adequate** | 3 seeds x 10 arms, 8.96 h, 60 adapter passes, positive control converged at 0.973-0.985; no gate bound marginally |

### Failure-location summary (GOV-FAILLOC-1)

| Bucket | Reads | Established? |
|---|---|---|
| MECHANISM FAILED | Implementation **complete** | **established** |
| MEASURES FAILED | Measurement **under-instrumented** | **partial** |
| ENVIRONMENT FAILED | Environment **adequate** | **established** |
| REE FAILED | needs all three | **NO** |

**Net: MIXED (MECHANISM + ENVIRONMENT established, MEASURES partial) -- explicitly NOT chargeable to REE as
a whole.** The mechanism under test is fully implemented, trained, non-collapsed, faithfully reproduced and
read at the consumer's exact capacity, and it still does not carry the mapping. The environment
demonstrably contains a mapping three non-REE readouts recover above the bar. Measurement is only *partial*
because nonlinear recoverability is unmeasured -- and with MEASURES partial the fourth bucket cannot be
reached, so **no organism-level "REE failed" read is licensed by this artifact**, however tempting the
0.868-vs-0.669 headline is.

### Recommended epistemic category

**`standard`** (claim-free; the enum's spelling for "no epistemic suppression applies", which is the
verdict). Deliberately **not** `substrate_ceiling`: that value sits in `_EPI_SUPPRESS_PROPOSAL` and marks
claims not-v3-testable, and this run asserts the *opposite* of a build gate -- that one cheap probe on
already-banked data separates the two candidate builds. The failure-mode diagnosis lives in the note fields.

---

## 7. Granularity-debt trigger, the re-derive brake, and the diagnostic chain

**Granularity-debt recurrence trigger: DOES NOT FIRE.** Run with `granularity_debt_cluster.py` (targets
whose own `claim_ids` name the claim, never a grep). **MECH-457**: 31 targets across 21 files; alignment
distribution `intact=17, strengthened=5, unclear=2, unstamped=2, untested=2, weakened=2, other=1` -- and
MECH-457 was already **decomposed** 2026-07-22 into MECH-475 / MECH-476 (user-approved), so the debt this
trigger surfaces is discharged. **INV-088**: 9 targets across 9 files; `intact=2, other=2, untested=2,
weakened=2, unstamped=1`. **This run adds no target to either cluster** -- `claim_ids` is empty, so it is
invisible to the reader by construction. Routing is not `/claim-synthesis`.

**Re-derive brake (R1-R3): counts UNCHANGED; this run neither fires nor increments it.** Re-run under the
binding recipe on 2026-09-08: **MECH-457 = 13 hits** (756, 750, 752, 753, 754, 755, 770, 771, 772, 781,
765, 769, 821b); **INV-088 = 2 hits** (750, 754). Identical to what V3-EXQ-978 and V3-EXQ-1002 recorded.
Both are at or past the threshold of 2, so the **standing brake on both claims remains fired** and a
same-claim lettered re-run against the same substrate is still refused. **This target is claim-free, so the
counter's `claim in target.claim_ids` test never reaches it** -- stated so no later session re-derives it.

**What this autopsy refuses on its own account.** A lettered **`V3-EXQ-1008b`** that re-runs this design
with more adapter passes, a wider adapter, more seeds or more episodes. The instrument converged (positive
control 0.973-0.985; all ten criteria non-degenerate; both load-bearing criteria passed); the readings are
not power problems, and more of the same is the loop the brake exists to stop.

**What the bit-identical reproduction costs the H-D read -- a correction this artifact makes against its own
draft.** `H-D-warmup-not-the-locus` sits `confirmed` in the frozen registry on **V3-EXQ-1002 alone**
(`resolving_runs: ["V3-EXQ-1002"]`, `met_elimination_bar: false`). This run reproduces the ordering
(trained 0.6686 at or below untrained 0.6946 on 3/3 seeds, as 1002's 0.664 vs 0.688), and the draft of this
artifact credited that as **a second independent instance**. It is not: the warmup output is bit-identical
between the two runs (section 1), so this run re-reads *the same latent* with a differently-initialised
reader. **It rules out a reader-init artifact, not a warmup-draw artifact.** The correct and weaker
statement -- the one governance should bank -- is that the ordering is stable under a reader re-draw and
across an intervening substrate change, and that **H-D continues to rest on one run**. This autopsy
recommends **no change** to H-D's registry entry: not a strengthening (there is no independent instance to
add), and not a weakening (nothing contradicts it).

**Diagnostic-chain recurrence (GOV-DIAG-1): DOES NOT FIRE.** `check_diagnostic_chain_recurrence.py` on
2026-09-08 reports 26 `bears_on` work-streams carrying pure-diagnostic **no-verdict** autopsies and **0 at
the N>=3 ACTIONABLE threshold**. This lineage's autopsies are verdict-*bearing* (1002 resolved H-B/H-C/H-D;
this one resolves H-E and H-C), so they do not accumulate as no-verdict hits. **`bears_on` tokens are reused
VERBATIM from 1002** (`["INV-088", "MECH-457"]`) so the chain advances rather than starting a fresh count --
a corpus scan of 488 autopsies found no established namespaced work-stream token for this lineage.

---

## 8. Routing -- one probe on banked data, then a build

**Node classification: `complex (probe-gated) / puzzle (known rules)`.** The frame is well posed and **one**
missing fact -- is the decision-relevant content recoverable from the frozen latent at *any* capacity? --
gates two candidate builds that point in opposite directions and cost very differently. It is **not**
`complicated (buildable)`: no single build is named by the evidence yet. It is **not** `mystery (known
data)`: the deciding measurement is absent from every run in the lineage, because 1008 held capacity fixed
at the consumer's width by design. It is **not** `aleatoric`: the readings are 3/3 consistent on a converged
instrument.

**Routing: `/queue-experiment`, a NEW EXQ number, a GOV-FANOUT-1 portfolio on already-banked data.**

1. **(measurement axis) PRIMARY -- THE OVER-CAPACITY DECODER SWEEP (adjudicates H-F).** Same
   V3-EXQ-1002/1008 dataset, seeds, held-out episode split and standardiser; **the only thing varied is the
   decoder's capacity**. Sweep from the consumer's exact `x734.PPOPolicyNet` (32->128; known 0.669) up
   through progressively wider/deeper MLPs to a deliberately over-parameterised decoder, reporting both
   oracle-action agreement and a direct **nonlinear** decode of the five `DECISION_WORLD_STATE_INDICES`.
   Anchor every rung against the **same sweep applied to `ws250_pca`** (known 0.868) so the capacity axis is
   calibrated on a representation known to carry the content.
   - **Declared null:** even the over-parameterised decoder stays below 0.80 on the seed majority ->
     **H-F CONFIRMED**; the content is destroyed at encode time and the only repair is at the **encoder's
     objective** (`sd_actor_critic_action_learning`'s co-shaping hint, or an action-formatted stream).
   - **Clears** -> **H-F ELIMINATED**; the content survives but is inaccessible at the consumer's
     capacity/format, and the repair is **interface reformatting** -- an entirely different, much cheaper
     build.
   - **Why this is not the lettered re-run the brake refuses:** the brake refuses re-running the *same*
     design at more power to re-ask the *same* question. Here the DV, the question and the manipulated
     variable all change. 1008 held capacity fixed and varied the input representation; this holds the
     representation fixed and varies capacity, which no run in the lineage has done.
2. **(process axis) SECONDARY, only if H-F confirms -- THE LAYER-WISE CONTENT PROBE.** Decode the five
   decision coordinates from each intermediate tensor of the observation->z_world path on the banked
   episodes and report the profile. **Declared null:** content falls monotonically with depth with no single
   stage accounting for the loss (a distributed squeeze). A sharp single-stage drop instead **names the
   layer** and converts the node to `complicated (buildable)` at that layer. Forward passes only.

**Why one more probe rather than a build, stated against the obvious objection.** This is the fifth
diagnostic on this locus (813 -> 948 -> 978 -> 1002 -> 1008), and a reader is entitled to ask whether the
lineage is converting effort into information or circling. Three reasons it is converting: **(a)** each run
has *eliminated a named rival* rather than re-measuring -- H-B (consumer learning), H-E (channel width) and
H-C-linear (geometry) are now all closed -- of the four legs this question carried before today, **three
are resolved out and one stands confirmed**, and the single leg left live (H-F) is one this run's own
eliminations created rather than inherited;
**(b)** the recommended probe costs no `ree_core` change, no new warmup family and no contract-gate
exposure -- forward passes and decoder fits on data already banked; **(c)** it discriminates between two
builds whose costs differ by more than an order of magnitude, and building the wrong one is exactly the
confident-but-wrong localisation GOV-FANOUT-1 exists to prevent. **This autopsy states explicitly that if
H-F's probe returns CONFIRMED, the next move is a BUILD, not a sixth diagnostic.**

### The consequence for SD-018 that this autopsy must surface

`failure_autopsy_V3-EXQ-1002_2026-09-05` held SD-018 **shape (b)** (side-channelling the raw field past
`z_world`) on **two grounds it explicitly said "can come apart"**: **(i)** the predecessor's condition --
H-C is confirmed, so shape (b) "would raise the score without addressing the constraint"; and **(ii)**
independently, shape (b) **bypasses** the observation->`z_world` interface rather than repairing it, and
that interface is the v3 binding constraint.

**This run weakens H-C, so ground (i) no longer stands as stated. They have come apart exactly as
anticipated.** Ground (ii) is untouched and still holds the build. Governance must know the hold is now
**single-grounded** before it ratifies or amends the
`docs/architecture/sd_018_resource_proximity_supervision.md` line 94 override (*"If it nulls, build shape
(b)"*). *(That the prior artifact enumerated its grounds separately instead of merging them is what made
this auditable in a single read -- recorded in `learning_extracted`.)*

**Substrate write recommended: `action: amend` on SD-018 -- record-keeping, not a build authorisation.**
SD-018 currently carries **no** `failure_record` entry for either V3-EXQ-1002 or V3-EXQ-1008, though both
were commissioned off its 978 record. Two writes: append the new `failure_record_entry` (JSON), and mark the
existing `v3_exq_978` item **`superseded`** -- its target was a two-way discrimination ("reproduces -> H-B,
shape (b) is the right build" vs "cannot -> H-C, shape (b) would raise the score"), 1002 took the CANNOT
branch and 1008 has now adjudicated the H-C branch itself, so the fork is superseded by a third answer
neither branch anticipated. **`superseded`, not `resolved`: nothing was fixed.** `severity` stays
`degrading` and `substrate_paths` are unchanged -- the finding is a capability limitation, not a defect that
produces evidence which looks valid but is not, so no Step 2.5c block on unrelated experiments is warranted.

---

## 9. Ledger delta (Step 9b) -- APPLIED

Question `zworld_actor_adequacy_locus`. **Growth-restriction check: field ABSENT on this qid -> proceed, no
gate.** The registry already lists `V3-EXQ-1008` in the `adjudicating_runs` of both H-C and H-E (1002's
Mode A pre-registration was applied on 2026-09-05), so both legs resolve under **Mode B**; H-F is new
**labelled fan-out growth (3a)**.

| leg | mode | from | to | bar fields |
|---|---|---|---|---|
| `H-E-channel-input-capacity` | **B (resolve)** | `alive` | **`eliminated`** | `control_passed` T, `non_degenerate` T, `met_elimination_bar` **T** |
| `H-C-geometry-mismatch` | **B (re-resolve)** | `confirmed` | **`split`** (recommended; see below) | T, T, **T** |
| `H-F-content-discarded-at-encode` | **A / labelled fan-out (3a)** | -- | `alive`, unqueued | bar not met |

`resolved_utc` for both resolved legs = **2026-09-07T23:38:26Z** (the run's own `timestamp_utc`).
`resolving_runs: ["V3-EXQ-1008"]` on H-E; `["V3-EXQ-1002", "V3-EXQ-1008"]` on H-C.

**H-C's state is the one genuine judgement call, and it is put to the gate rather than decided here.**
The registry has no `weakened` state, and the driver's pre-registered word is *weakened*. Three readings:

- **`split` (recommended).** Children: *"an information-preserving LINEAR re-basis of the frozen latent
  restores accessibility"* -> **eliminated**; *"geometry contributes to accessibility, but far short of the
  gap"* -> **confirmed** (ZCA +0.039, LDA +0.043 mean, 3/3 positive, against ~0.131 needed). This is the
  only reading that carries **both** halves of the evidence, it matches **three of the four** existing
  `split` precedents in the registry (one child confirmed, one eliminated -- `competence_floor/H-explore`,
  `sd016_retrieval_selectivity_mechanism/H3-algorithm-competitive-gating`,
  `contextmemory_write_content_discrimination/H1-loss-objective-mismatch`; the fourth,
  `competence_floor/H-bc-prior`, has three children and no eliminated one, so the shape is a convention and
  not a rule), and it does not overwrite a pre-registered word with a stronger one. `split` is in
  `RESOLVED_OUT_STATES` in both `build_hypothesis_space.py` and `check_hypothesis_space_integrity.py`, and
  `resolution.children` is read by the builder, so the value is in-vocabulary and legal.
- **`eliminated`.** Defensible -- H-C's own first conjunct ("the information is present and linearly
  decodable") is contradicted by the content witness. Rejected as the recommendation because it discards
  qualification (a) and reads the pre-registered *weakened* as *eliminated*.
- **`alive` (confirmation withdrawn).** Rejected: leaving a leg alive after its own pre-registered, fully
  green corroborator returned its declared null is the mirror image of the error 1002's gate corrected.

**Counters:** `initial_frozen_count` **4 -> 5** via one labelled fan-out event (`delta: 1 ==
len(added_hids)`); `initial_frozen_count_at_registration` **stays 2**; `fanout_sources` gains this artifact.

**Axis family, and the circling question answered honestly.** H-F is assigned axis **`representation`**,
which maps to the `representation` family -- **the same family as the eliminated H-B (`readout`) and H-C**.
By the convergence heuristic that reads as **circling**, and this artifact records it rather than dodging
it. Two reasons it is nonetheless the right assignment: **(1)** H-F is the direct **negation** of H-C, not
a re-entry of it -- H-C asserted the content is present but badly arranged, H-F asserts it is not there to
arrange, and eliminating a hypothesis is precisely what makes its negation live; **(2)** re-labelling H-F
onto `learning-signal` (-> `constitution`, a family holding only a *confirmed* leg) to obtain a `refining`
verdict was considered and **rejected as a Goodhart move** -- the axis should describe the hypothesis, not
the metric it produces. The user may overrule this at the gate; the artifact states the trade so the
verdict is auditable either way.

**Only ONE new leg is registered, deliberately.** H-F's complement (*content present, consumer-side
capacity/format is the block*) is H-F's own **declared elimination branch**, not an independent leg;
registering both would inflate the frozen denominator by two for a single measurement. It gets registered
by the autopsy that adjudicates it, if H-F is eliminated.

**`fanout_growth_note`:** this question has now taken **two** fan-out growth events (delta 2 then delta 1)
in two adjudication cycles; the denominator has moved 2 -> 4 -> 5 while one leg was eliminated, two
confirmed, one more eliminated and one split. The headline narrowing ratio is inflated exactly here and must
be read alongside the growth events.

**`decision` block:** `decision_question` gains H-E's elimination and H-C's split. `live_gate` becomes the
over-capacity decoder sweep of section 8. `decidable` stays **`true`**. `distance_phrase`: one banked-data
capacity sweep away from choosing between an encoder-objective build and an interface-reformat build.
`observation_bottleneck`: **no run in the lineage varies the reader's capacity** -- every one holds it at
the consumer's exact width by design -- so "content discarded at encode" and "content present but
inaccessible at consumer capacity" remain confounded. `decision_log_ref` stays `null` (human-owned).

**APPLIED 2026-09-08, in the same commit as this artifact.** `H-E-channel-input-capacity` -> `eliminated`;
`H-C-geometry-mismatch` -> `split` with the two children above; `H-F-content-discarded-at-encode` appended as
labelled fan-out growth (3a); `initial_frozen_count` **4 -> 5** with `initial_frozen_count_at_registration`
held at **2**. Invariants 1 and 2 were asserted programmatically before the write (count == len(hypotheses);
`pre_registered_utc <= resolved_utc` on every resolved leg), and `delta == len(added_hids) == 1`.

`build_hypothesis_space.py` and `check_hypothesis_space_integrity.py` re-run: **flags a=0 b=0 c=0 d=0**. The
append is reported under *Advisory -- labelled fan-out growth* -- *"+1 leg(s) (H-F-content-discarded-at-encode)
added by labelled fan-out from `failure_autopsy_V3-EXQ-1008_2026-09-08.json` -- conditions (a)-(c) satisfied,
advisory not a violation"* -- and the pre-registration provenance check passes on a git witness
(*"`failure_autopsy_V3-EXQ-1002_2026-09-05.json` committed 2026-09-05 <= resolution 2026-09-07"* for H-E).

**The derived `convergence_class` for this question came back `circling`**, with the reason
*"a growth event added ONLY legs re-entering already-eliminated families"* (`families_closed`:
`constitution`, `instrumentation`; `families_touched`: `instrumentation`, `representation`; `families_fresh`:
none). That is exactly what this artifact predicted and disclosed **before** the write, and what the Step 8
gate ratified -- recorded here so the verdict is read as an accepted cost of an honest axis assignment, not as
an unnoticed one. The question's own advisory line now reads: *denominator grew 2 -> 5 across 2 labelled
events; report the reduction ratio BOTH ways.*

---

## 10. Step 7b mechanical pre-routing checks

`autopsy_pre_routing_checks.py --json`: **`fire_count: 0`** on the first pass (JSON only), re-run with the
sibling `.md` present -- see section 12 for the final counts. `inapplicable`: **C1, C2, C3** are claim-keyed
and this target carries `claim_ids: []`, so all three are **structurally blind** here. Per the skill,
*"`inapplicable` is NOT 'no fire'"*: a quiet report on a claim-free artifact means the checks could not
look, and the load falls on **Step 7c** and the **Step 8 gate** -- which is exactly what happened on this
lineage's previous artifact, where both moved the routing.

---

## 11. Withdrawn arguments (recorded, not deleted)

- **"Leg 1's verdict is unsafe because `C_ws250_pca_beats_randproj` failed 2/3."** **Withdrawn.** The
  margin is not an argument to `_adjudicate_leg1` and never was; the driver documents in three places why
  gating on it would refuse the leg's strongest answer. What survives is the narrower and correct
  statement recorded in section 3: the elimination delivered is the **plain** one, not the **strong** one.
- **"Leg 2's re-basis criterion cannot discriminate by construction, so the H-C weakening is unsafe."**
  **Withdrawn as stated, retained as a qualification.** It is true that an invertible linear re-basis is
  function-class-preserving -- but the driver says so itself and correspondingly requires the **closed-form
  content witness** to be non-lifting before the WEAKENED branch may fire, so the design already carries
  the objection. What survives is section 4(b)-(c): the weakening rests on the content witness, which is a
  **linear** decode, and nonlinear recoverability is unmeasured. That residue became the routing.
- **"Recommend `eliminated` for H-C."** Considered and **not adopted** as the recommendation; retained as
  the runner-up at the gate (section 9). It would replace a pre-registered *weakened* with a stronger word
  and would discard the consistent 3/3 whitening lift.
- **"Assign H-F to `learning-signal` (constitution family) to avoid a `circling` convergence verdict."**
  **Rejected as a Goodhart move** (section 9). The axis should describe the hypothesis, not the metric.
- **"Route to `/implement-substrate` now -- the encoder-objective build is named."** **Rejected.** Two
  builds are live and point in opposite directions (encoder re-objective vs consumer interface reformat);
  one banked-data probe separates them at a small fraction of either cost. Recorded because the
  0.868-vs-0.669 headline makes the encoder build look obvious, and it may still be wrong.
- **"SD-018 shape (b) is now unblocked, since H-C is weakened."** **Rejected.** Ground (i) of the 1002 hold
  is withdrawn, but ground (ii) -- shape (b) bypasses rather than repairs the binding-constraint interface
  -- is independent and untouched. Surfaced to governance as a *single-grounded* hold, not as a release.

---

## 12. Step 7c red-team pass and Step 8 gate

**Red-team pass: RUN. Verdict CONTESTED.** One defect, four qualifications, four hygiene items; **all nine
applied**. Findings file: `scratchpad/redteam_1008.md` (407 lines); recorded machine-readably as the
top-level `red_team` block in the sibling JSON.

**Model, stated plainly because it bears on how much the pass is worth.** The skill's preferred cross-model
reviewer (**Fable**) was attempted **first** and the spawn failed with an API `rate_limit` / out-of-credits
error for `claude-fable-5-1`. Per the skill the pass was re-spawned **once**, on the session model
(`claude-opus-5`) -- the same model that drafted the artifact. **This is a valid pass but NOT a cross-model
one**, so it does not carry independence from the drafting model's priors, and a later reader must not
credit it with that. Reasoning was withheld from the reviewer and the read order was enforced (JSON
conclusion first, then raw manifest / driver / registry / substrate_queue / claims.yaml, then the prose).

**The defect (FINDING 1), independently verified by the author before being applied.** The artifact credited
this run as *"a second, independent instance"* corroborating `H-D-warmup-not-the-locus`. It is not: the
warmup and dataset reproduce **bit-identically** from V3-EXQ-1002 -- `zworld_encoder_trained_in_p0` and
`zworld_not_collapsed` match to full double precision, the `rawfield_ceiling` arm is bit-identical on 3/3
seeds, the held-out split is identical, and `machine_class` is the *same string* on both runs, contradicting
the driver's own stated provenance reason. Only the adapter initialisation was re-drawn. **Applied in
section 1, section 7, `learning_extracted[4]` and the closing sentence of the recommended
`evidence_quality_note`.**

**The four qualifications, all applied.** (2) The JSON never stated H-F's *registry* axis, and its only
axis-shaped field for that leg reads `measurement` -- the **probe's** design axis -- which a governance
session applying the JSON alone would have written into the registry in place of `representation`; an
explicit `registry_axis_for_H_F` plus an `axis_field_semantics_note` now prevent that. (The reviewer
separately checked that the convergence verdict latches `circling` either way, so the disclosure in section 9
survives the ambiguity.) (3) `criteria_non_degenerate` is an arm-liveness/non-nullity test with **no**
counterfactual reachability content, so the draft's "every one could have gone either way" was unearned --
narrowed in section 1, with reachability now established per criterion where it matters. (4) The leg-2
*verdict* arm is 25-300x worse-conditioned than the driver's own calibration curve, so the geometry
contribution is a **floor**, not a point estimate -- added to section 4(a). (5) The "content present
nonlinearly" inference is confounded by learned-vs-fixed rule as well as nonlinear-vs-linear; softened in
section 4(c), **and the recommended probe gained a fitted-linear-readout arm to de-confound it** -- the one
finding that improved the routing rather than only the prose.

**Hygiene, all applied.** H1: only **three** of the four registry `split` precedents have the
one-confirmed/one-eliminated shape (`competence_floor/H-bc-prior` has three children and no eliminated one)
-- corrected in section 9. H2: the 0.05 marginal band is reached by one LDA seed and **no** ZCA seed --
corrected in section 4(a). H3: "four live readings has two" was ambiguous enough to read as a narrowing
claim it does not support -- rewritten in section 8. H4: `resolved_note` was a minted key; the schema's own
prose key is **`addressed_by`**, now used, and the new `failure_record_entry` additionally carries
`run_role: "unknown"` with its basis, deliberately **not** `post_build`, so an OFF-arm characterisation
cannot silently raise SD-018's `_substrate_landing_cutoff`.

**What the pass did NOT overturn.** Every load-bearing figure was independently recomputed from the
manifest's own `arm_results` cells rather than the driver's aggregation -- all ten arm means, the 0.19978
PCA-vs-encoder gap, the 0.13140 gap-to-bar, the LDA lift at 0.3254 of the gap, every content-witness margin,
and the brake and granularity counts -- with **no disagreements**. Also verified sound: leg 1's
`H-E-eliminated` despite the random control failing (and that the CONFIRMED branch was genuinely reachable);
leg 2's `H-C-weakened` firing exactly as pre-registered; `split` being in-vocabulary and legal against the
integrity checker's own bar; `superseded` matching the schema's `value_note` verbatim; the SD-018 amend
facts; both per-claim `change`-string tails being storable and not-already-true against live `claims.yaml`;
the `non_contributory` direction being storable; the "not a lettered re-run" argument; and fifteen prose
absolutes tested and unbroken.

**Step 8 interactive gate: HELD, 2026-09-08T06:18:57Z.** Four questions were put to the user, each carrying a
`(Recommended)` option; **all four recommendations were accepted**, and the outcomes are logged in the
recommendation-agreement ledger (entries 148-151).

| question | decision |
|---|---|
| H-C's registry state | **`split`**, with the two children of section 9. `eliminated` and `alive` were offered as runners-up and declined. |
| H-F's axis | **`representation`**, explicitly **accepting the `circling` convergence verdict**. The `learning-signal`/`constitution` re-label -- which would have produced a `refining` verdict -- was offered and declined as a Goodhart move. |
| SD-018 substrate write | **`amend`**: append the 1008 `failure_record` entry AND mark the `v3_exq_978` item **`superseded`**. `action: none` (notes only, the 1002 precedent) was offered and declined. |
| Routing | **One more probe on already-banked data.** Both alternatives -- *build now on the encoder objective* and *release SD-018 shape (b) as a performance lever* -- were offered and declined. |

Per CLAUDE.md Session Land Protocol step 6, this session does **not** `spawn_task` the routing's own
follow-on: the routing is a proposal until `/governance` Step 2b ratifies it, and governance is the session
that chips it.
