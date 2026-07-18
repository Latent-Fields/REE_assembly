# Decision: MECH-459 governance status — registry leg + re-derive brake

- **decided_utc**: 2026-07-18T07:35:11Z
- **claim**: MECH-459 (`return_scale_invariance_blocks_actor_bootstrap`), registered 2026-07-18 by the CDQ-007 convergence intake (REE_assembly master f4b253a543)
- **question 1**: should `competence_floor` gain a third ALIVE leg (H-return-scale)?
- **question 2**: does the shape-preserving normaliser knock-out survive the re-derive brake?
- **status of both at intake**: deliberately left open; this artifact rules on both.
- **live discrimination NOT pre-empted**: V3-EXQ-780 (`claimed` ree-cloud-2) and V3-EXQ-781
  (`claimed` ree-cloud-3) are untouched; `mech457_competence_bootstrap_explorer` stays
  `blocked_pending_discrimination`. No queue entry was added by this adjudication.

---

## 0. Code verification (done before ruling — the facts both decisions turn on)

The two-sided normaliser is real, and it is **not confined to the one function MECH-459 names**.
Verified sites (ree-v3, working tree):

| Site | Running-std | Per-episode standardisation |
|---|---|---|
| `experiments/_lib/mech457_fanout.py::train_rawview_ac_rl` | :244 | :253 |
| `experiments/_lib/mech457_fanout.py` (z_world AC) | :411 | :420 |
| `experiments/_lib/mech457_explorer_classes.py` (composed bootstrap) | :688 | :697 |
| `experiments/_lib/mech457_explorer_classes.py` (second trainer) | :941 | :950 |

This matters: V3-EXQ-770/771 do **not** run `train_rawview_ac_rl` — they run the composed
bootstrap in `mech457_explorer_classes.py`. The normaliser is present there too, so the locus
generalises and the claim's citation, while under-inclusive, is not wrong about scope.

**Finding V1 — the mathematical core of the strong form is CORRECT.**
Multiply the entire reward stream by `c`: Welford's `std` scales by `c`, so
`scaled = c*r / (c*std + eps) ~= r/std` is unchanged, hence GAE advantages, returns, the policy
loss *and* the value loss are all unchanged. Invariance to a **global multiplicative reward
rescaling** holds to within `REWARD_STD_EPS` and the Welford warm-up transient. The
running-std alone is sufficient for this; the advantage standardisation is a second, within-episode
operator on top. MECH-459's operator analysis is sound as written.

**Finding V2 — the INFERENTIAL step from V1 to "770 and 771 were divided out by construction"
is FALSE.** None of the three fan-out legs is a global multiplicative rescaling:

- **V3-EXQ-770 (drive-schedule)** varies `intrinsic_coef` on *one component* of `shaped`
  (relative reweighting = **shape**, not global scale) — and, decisively, its treatment also holds
  `entropy_beta` constant at 0.10 where the control anneals 0.10 -> 0.03
  (`mech457_bootstrap_explorer.py:84-85`). `beta_eff` multiplies the **loss**
  (`explorer_classes.py:698`, `loss = policy_loss + value_loss - beta_eff * entropy_bonus`),
  entirely **outside** the normaliser. So 770 moved a lever the scale-invariance operator
  provably does *not* divide out.
- **V3-EXQ-771 (reward-coupling)** is a metabolic forage-to-survive **environment** change —
  it alters the termination structure and the state distribution. A scale operator does not
  touch it at all.
- **V3-EXQ-772 (credit-horizon)** is potential-based shaping = shape, not scale. This was
  already conceded on the claim as the honest counterweight.

The counterweight the claim recorded for 772 therefore **generalises to 770 and 771**. The
eliminations are *not* laundered "by construction". What survives is only the weakest form the
claim already names: per-episode standardisation re-amplifies co-present novelty noise
(`NOVELTY_COEF 0.1/sqrt(visit_count)`, firing every step) back to unit variance, **swamping**
whatever shape change a treatment introduced. That is a claim about **noise dominance**, not
about scale invariance — and it is empirical, not architectural.

**Finding V3 — an asymmetry that is decision-relevant for the LIVE portfolio.**
The two queued legs are not equally exposed to the surviving weak form:

- **V3-EXQ-780 (H-bc-prior)** adds `bc_aux_coef * bc_loss` as a **loss-side** cross-entropy term
  (`explorer_classes.py:703-708`). It never enters `shaped`, so the normaliser cannot swamp it.
  **780 is NOT confounded by MECH-459.**
- **V3-EXQ-781 (H-approach-primitive)** adds `appr = approach_coef * approach_drive(obs_dict)`
  directly into `shaped` (`explorer_classes.py:660-662`). It is inside the normaliser and is
  exactly the kind of reward-side magnitude signal the weak form predicts gets standardised back
  into parity with novelty noise. **A 781 NULL is confounded; a 781 POSITIVE is not.**

This asymmetry is the single most useful product of this adjudication, and it was not visible
at intake.

---

## DECISION 1 — hypothesis-space registration: **NO third ALIVE leg now** (conditional trigger armed)

**Ruling: `competence_floor` does NOT gain H-return-scale at this time.** The registry is not
amended by this decision. `initial_frozen_count` stays 12;
`initial_frozen_count_at_registration` stays 7; no `fanout_growth_events[]` entry is written.

**Primary rationale — category, not merit.** A leg in this registry is an *answer to the
question's `decision_question`*: "which competence-directed dependency lets the actor-critic
convert a sufficient observation into competent foraging — a learned behavioural prior or an
innate approach primitive?" In its **surviving weak form**, MECH-459 does not answer that. It
asserts that *the prior eliminations are less informative than they look* — a claim about the
**validity of the question's own evidence base**, i.e. about the measuring instrument. Registering
an instrument-validity claim as a rival *answer* would category-error the ledger: its
elimination or confirmation would not narrow the decision question, so it would inflate the
denominator without ever being able to reduce the numerator.

**Secondary rationale — the growth contract's own warning.** The registry's `fanout_growth_note`
already records that this question's denominator grew 7 -> 12 across two labelled portfolios while
8 legs were eliminated, and states plainly that this means "the campaign has not converged: it is
inventing new candidate explanations as fast as it rules old ones out." Adding a 13th leg for a
hypothesis whose **strong form this adjudication has just found to be false** (Finding V2) would
be precisely the failure that note warns against.

**Honest-pair reporting (what adding WOULD have cost), per `labelled_fanout_growth`:**

| Basis | Surviving / denominator | Ratio |
|---|---|---|
| Against ORIGINAL frozen count (7) | 2 / 7 | 0.286 |
| Against CURRENT count (12) | 2 / 12 | 0.167 |
| Hypothetically, had H-return-scale been added (13) | 3 / 13 | 0.231 |

Note the tell: adding the leg would have made the ratio against the current count *look better*
(0.167 -> 0.231) purely by enlarging the numerator with an unadjudicated leg. That is the exact
laundering the `labelled_fanout_growth` invariant exists to keep visible, and it is a further
reason to decline.

**Conditional trigger (armed, auditable, non-retro-padding).** MECH-459 graduates to a genuine
rival *answer* — and is then registered as `hid: H-return-scale`, axis `normalisation-pathway`,
under a labelled `fanout_growth_events[]` entry citing this decision artifact as `fanout_source`
— **if and only if** the composition readout (Decision 2, probe R) shows the predicted signature:
forage-contact |adv| mass tiny **pre**-standardisation and rescaled to ~parity
**post**-standardisation. At that point value-pathway stabilisation becomes a candidate
competence-directed dependency in its own right, not merely an instrument caveat.

**Pre-registration hygiene for that path (stated now so it cannot be challenged later).** Probe R
is a **diagnostic on intermediate quantities**; it is explicitly **NOT** the adjudicating run for
H-return-scale. The adjudicating run would be a subsequent competence-lifting experiment. So
registering the leg *after* probe R reports still satisfies invariant (a) —
`pre_registered_utc <= resolved_utc` of the adjudicating run — because probe R does not adjudicate
it. Recording this here is what makes the sequence auditable rather than retro-padded.

---

## DECISION 2 — the re-derive brake: **knock-out is PERMITTED, but is NOT the right first move**

Two separable rulings.

### 2a. Class ruling — a normalisation-pathway change is a DISTINCT mechanism class. Brake permits.

The brake as recorded in `failure_autopsy_MECH-457-fanout-770-771-772_2026-07-18.json`
(`fired: true`, threshold 2, 6 prior substrate-ceiling autopsies, `refused_requeue: true`)
refuses "further config/env/credit/capacity same-axis re-pose" and explicitly permits
"DIFFERENT mechanism classes under NEW EXQ numbers — the sanctioned route the brake permits,
same sanction as 769 -> 770/771/772."

The knock-out qualifies, on four independent grounds:

1. It changes the **update operator itself** (`(adv-mean)/(std+eps)` -> `adv / max(1, Per95-Per5)`),
   not a hyperparameter of the existing rule. Every braked axis (capacity, drive, environment,
   credit) held the learning rule fixed and moved an input to it.
2. It carries **different `claim_ids`** — MECH-459, not MECH-457. The brake counts prior
   substrate-ceiling autopsies *per claim*; MECH-459's count is 0.
3. It has a **declared, symmetric falsifier**: "SUPPORTED if the floor moves; FALSIFIED if it
   does not — the two-sided normaliser is then exonerated and the weaker
   noise-re-amplification form falls with it." It can come back negative and settle something.
4. It is at least as distinct from capacity/drive/environment/credit as those four were from
   each other — and the brake permitted all of those transitions.

**The brake is therefore not the blocker.** Ruling 2a is unconditional.

### 2b. Sequencing ruling — run the cheap intermediate readouts FIRST; the knock-out is conditional on them.

Passing the brake is a licence, not an obligation. Given Findings V1–V3, the knock-out is the
**wrong first spend**:

- It tests only the **weak** form, since the strong form is already dead by Finding V2. A
  full competence run is a heavy instrument for a hypothesis that has lost its architectural
  half.
- Readouts (a) and (b) are on **intermediate quantities**, are far cheaper, and — critically —
  **discriminate the weak form from a bootstrap-signal-absence account directly**, which the
  knock-out does not: a knock-out null is compatible with both.
- Readout (a) additionally resolves **Finding V3** — whether a V3-EXQ-781 null can be read at
  face value. That is decision-relevant to the live portfolio *within its runtime*, which no
  other pending work delivers.

**Routing:** one combined DIAGNOSTIC probe (call it **probe R**), governance-scoring-excluded,
new EXQ number, via `/queue-experiment`. Not a modification to 780/781. Two readouts,
one instrumented short run each on the composed-bootstrap path:

- **R-(a) advantage composition, logged BEFORE standardisation.** Fraction of `|adv|` mass on
  forage-contact steps vs novelty/harm steps, reported both pre- and post-standardisation.
  *MECH-459 weak form predicts*: forage fraction tiny pre, rescaled to ~parity post.
  *Signal-absence predicts*: stays tiny in the gradient either way.
- **R-(b) critic calibration on BC-visited states.** BC reaches 32.72, so its state distribution
  contains genuinely high-return states.
  *MSE/bimodal-collapse half predicts*: values cluster near the never-observed mean of the
  bimodal return distribution, failing to separate pre-reward from post-reward states.
  *Signal-absence predicts*: a flat critic everywhere.

**The knock-out (probe K) is sanctioned but HELD**, to be queued only if R-(a) returns the
parity-rescaling signature. If R-(a) shows the forage fraction stays tiny post-standardisation,
the weak form falls with it and probe K should **not** be queued at all — the normaliser is
exonerated and MECH-459 goes to `weakened`.

---

## Consequences

| Artifact | Action |
|---|---|
| `hypothesis_space_registry.v1.json` | **No write.** No third leg; counts unchanged (7 / 12). |
| `claims.yaml` MECH-459 | notes amended with this adjudication (status stays `candidate`) |
| `substrate_queue.json` `mech457_competence_bootstrap_explorer` | **unchanged**, stays `blocked_pending_discrimination` |
| V3-EXQ-780 / 781 | **unchanged**, running unmodified on ree-cloud-2 / ree-cloud-3 |
| Next action | ~~queue probe R as a DIAGNOSTIC via `/queue-experiment`, new EXQ (next free >= 782)~~ **DONE 2026-07-18T08:16Z -> V3-EXQ-782** |

## Execution record (appended after the ruling)

**Probe R queued as `V3-EXQ-782`** (`v3_exq_782_mech459_advantage_composition_probe`,
`experiment_purpose: diagnostic`, priority 7, `machine_affinity: any`, 5 arms x 3 seeds x 3000 ep).
Landed ree-v3 `origin/main 16fd4ef`; ingested into the coordinator DB (`/queue/active` confirms).
**Do not re-queue it.** Two departures from the ruling's letter, both recorded in the script:

1. **Instrumentation is a separate mirror module** (`ree-v3/experiments/_lib/mech459_probe_r.py`),
   not a hook added to `mech457_explorer_classes.train_a2c`. A default-None hook would be
   numerically byte-identical when OFF, but it still changes the *bytes* of a file V3-EXQ-780/781
   are running against -- perturbing their `arm_fingerprint` substrate_hash and reaching any worker
   that restarts mid-run. The mirror imports every operator-defining quantity (`FORAGE_BONUS`,
   `_novelty_bonus`, `_RunningStd`, `_compute_gae`, `AC_*`, `_prioritized_credit_replay`,
   `warm_then_anneal`) rather than re-declaring it, and documents the faithfulness contract
   line-by-line against `explorer_classes.py:646-720`. `git status` confirms zero `mech457_*`
   modifications, satisfying section 0's "live discrimination NOT pre-empted".

2. **R-(a) is prevalence-normalised, and carries a THIRD outcome this ruling did not enumerate.**
   Forage contacts are rare, so a raw "tiny mass fraction" partly just measures rarity; the probe
   therefore routes on the CONCENTRATION `C = (forage |adv| mass fraction) / (forage step
   fraction)`, where `C == 1` means forage steps carry exactly their per-step share of the
   gradient. Branches: **parity-rescaling** (`C_pre<0.5`, `C_post>=1.0`, `delta>=0.25`) -> weak form
   supported, queue probe K, register `H-return-scale`; **stays-tiny** (`C_post<1.0`,
   `delta<0.25`) -> normaliser exonerated, weak form falls, K NOT queued, MECH-459 -> `weakened`;
   **already-concentrated** (`C_pre>=0.5`) -> the weak form's PREMISE fails (forage already carries
   its share BEFORE standardisation), so the weak form falls by a different route and K is likewise
   not queued.

**Analytic constraint worth carrying forward** (recorded in the script's interpretation grid, and
absent from this ruling): the standardisation is `(a - mean)/(std + eps)`. Division by a positive
scalar is a global rescale and leaves every `|adv|` mass *fraction* exactly invariant -- so **only
the mean subtraction can move the composition**. The parity-rescaling signature is therefore a
demanding, specific prediction (it requires a large negative episode-mean advantage relative to
forage-step advantages), not a generic consequence of normalising. `mean_episode_mean_adv` is
emitted per cell as the audit of that mechanism.

**Readiness gates match the routed statistic** (so a starved run cannot masquerade as a
falsification): R-(a) is count-gated -> COUNT readiness (`>=30` forage steps per cell in the
measured window; below that "stays tiny" is vacuous, not falsifying). R-(b) is spread-gated ->
SPREAD readiness (`std(return-to-go) >= 0.25` over demonstrator-visited states). Either below
floor -> `substrate_not_ready_requeue`, never a substrate-verdict label. The dry-run exercised this
for real (toy budget produced 1 forage step -> correctly self-routed `substrate_not_ready_requeue`).

The Finding V3 corollary is emitted at runtime as `headline.exq_781_null_readable`, and the
conditional follow-ons as `headline.probe_k_recommended` /
`headline.hypothesis_registry_action` -- so this artifact's routing is machine-readable off the
manifest rather than needing re-derivation from prose.

**MECH-459 status: `candidate`, NARROWED.** The strong form (architectural invariance
laundering the 770/771 eliminations) is **refuted by Finding V2** and should not be restated.
The surviving weak form (novelty-noise re-amplification swamping shape changes) is live,
cheap to test, and now carries a concrete decision-relevant corollary (Finding V3).

**This claim promotes nothing and licenses no build** — not the twohot critic, not the
percentile normaliser, not an imagination loop.

---

*Adjudicated by session `kind-leakey-2e738b`. Inputs: `claims.yaml` MECH-459;
`failure_autopsy_MECH-457-fanout-770-771-772_2026-07-18.json`;
`hypothesis_space_registry.v1.json` (`competence_floor`);
`.claude/skills/failure-autopsy/SKILL.md` Step 9b / GOV-FANOUT-1;
ree-v3 `experiments/_lib/mech457_fanout.py`, `mech457_explorer_classes.py`,
`mech457_bootstrap_explorer.py`, `v3_exq_770_mech457_drive_schedule_discrimination.py`.*
