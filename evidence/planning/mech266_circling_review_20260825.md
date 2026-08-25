# MECH-266 mode-arbitration-saturation -- circling review + H4 lit-pull gate

- **Generated (UTC):** 2026-08-25T17:31:01Z
- **Scope:** re-adjudication note over the `mech266_mode_arbitration_saturation` GOV-FANOUT-1
  question (qid), NOT a new experiment autopsy. No new run adjudicated.
- **Session:** mech-266-rescore-circling-2d31ca (worktree)
- **Question:** `mech266_mode_arbitration_saturation`, H1-H4 (MECH-266 / SD-032a)
- **Supersedes/extends:** `failure_autopsy_mech266-464e-467e-cluster_2026-08-13` (confirmed,
  original portfolio pre-registration) and its two later resolving autopsies
  (`failure_autopsy_V3-EXQ-934_2026-08-16`, `failure_autopsy_V3-EXQ-935_2026-08-18`), plus this
  worktree's own prior `mech266_h3_rescoring_20260825.md` (H3 re-scoring, ad hoc, same session
  slug, TASK_CLAIMS entry closed 2026-08-25T10:57:19Z).

**Claim disposition: no change.** MECH-266 and SD-032a remain `non_contributory` /
`epistemic_category: standard`, exactly as the confirmed cluster autopsy left them. Nothing
here is a per-claim recommendation for `/governance` to apply -- `per_claim_recommendation`
would be `STANDS` on both claims and is therefore skipped per the skill's own STANDS rule. This
document is a re-adjudication of the *portfolio's own hypothesis-ledger state*, not of the
claim layer.

---

## 1. Why this session exists

The worktree name (`mech-266-rescore-circling-2d31ca`) records two open threads left by the
2026-08-25 H3 re-scoring session on this same slug:

1. `hypothesis_space_registry.v1.json`'s H3 leg was resolved informally (basis text updated,
   no formal `/failure-autopsy` treatment -- no interactive gate, no red-team pass, no
   `per_claim_recommendation`).
2. `hypothesis_space.v1.json`'s DERIVED `convergence.convergence_class` for this qid reads
   `"circling"` -- a signal that, per the standing re-derive-brake discipline, normally means
   "stop and route to `/implement-substrate`, do not spend more probes on this question."

This session ran the full failure-autopsy discipline (dry-run gate n/a -- no new run; Step 1
re-adjudication read of the full superseded cluster artifact and driver; Steps 4/5 biological
triage re-derivation against the existing literature corpus; Step 8 interactive gate) over
those two threads.

## 2. Fact check -- H1/H2/H3/H4 state as found (2026-08-25T17:30Z)

Re-read directly from `hypothesis_space_registry.v1.json` (`qid:
mech266_mode_arbitration_saturation`), not summarised from memory:

| Leg | State | Resolving run(s) | Note |
|---|---|---|---|
| H1 cap-miscalibration | `alive` | V3-EXQ-934, V3-EXQ-935 | STRONGLY SUPPORTED (C1/C2/C3 all PASS at r=2.45/2.65 in 935's own sweep) but deliberately not confirmed -- r was picked post hoc from the same sweep. Confirmation run: V3-EXQ-935a, **not yet queued** (`ree-v3/experiment_queue.json` has 0 hits for `935a`). |
| H2 structural-bang-bang | `eliminated` | V3-EXQ-935 | Bar fully met (control_passed, non_degenerate, discriminating direction). Time-averaged occupancy IS graded and cap-controllable; the instantaneous mode label stays discrete by construction (SD-032a, never in dispute). |
| H3 instrument-illposed | `alive` | V3-EXQ-935 + this worktree's 2026-08-25 re-scoring of the ORIGINAL 464e/467e banked data | SUPPORTED but not sole cause. Re-scoring flips both runs' readiness gate NOT-MET->MET and flips 467e's C1/C2 from a definite FAIL to UNDECIDABLE (no same-mode dwell comparison exists in the banked data -- confirms the cluster autopsy's M3 argument quantitatively). 464e's C1/C2 are unchanged (never dwell-based). Neither eliminated (real defects confirmed) nor confirmed as sole cause (935's own corrected instrument still found real graded structure). |
| H4 clip-not-normalisation | `alive` | none yet | NEWLY DISCOVERED 2026-08-18 (Mode C-adjacent labelled fan-out from V3-EXQ-935's own analysis). Probe-gated on a `/lit-pull` per its own pre-registration text. **This gate is the subject of Section 4 below.** |

No chip or queue entry currently covers V3-EXQ-935a or a `targeted_review_salience_gain_normalisation`
lit-pull (checked `TASK_CHIPS.json` and `ree-v3/experiment_queue.json` directly, 2026-08-25).

## 3. Circling-verdict review

`build_hypothesis_space.py`'s DERIVED `convergence` block for this qid reads:

```
"convergence_class": "circling",
"reason": "a growth event added ONLY legs re-entering already-eliminated families",
"families_touched": ["constitution"],
"families_fresh": ["instrumentation", "representation"],
"growth_events": [{"added": [{"hid": "H4-clip-not-normalisation", "family": "constitution"}],
                    "re_entered": [{"hid": "H4-clip-not-normalisation", "family": "constitution"}],
                    "families_already_dead": ["constitution"]}]
```

This is mechanically correct at FAMILY granularity: H2's axis (`intrinsic-architecture`) and
H4's axis (`substrate`) both map to family `constitution` under `axis_families.map`, and H2 is
eliminated. Read naively, "a new leg re-entered the family holding the just-eliminated leg" is
exactly the re-derive-brake smell -- the registry's own conventions (see the arousal-variance
and `f-dominance` questions elsewhere in this file) treat that pattern as a genuine
non-convergence signal warranting a stop.

**But `axis_families`'s own `_explanandum_blindness_caveat` (recorded 2026-07-19T15:14:23Z,
from the competence_floor precedent) is a standing, general limitation of exactly this
classifier**, not a one-off note: `convergence_class` partitions on intervention LOCUS only --
"what layer of the system a hypothesis blames" -- and has no dimension for the EXPLANANDUM,
the thing being explained. Its stated OPERATIONAL RULE: *"when a question's convergence_class
reads 'circling', check whether its EXPLANANDUM changed before reading the verdict as the
re-derive-brake smell. If it did, the verdict is expected and carries no information."*

Applying that rule here, independently rather than taking H4's own pre-registration text at
face value (H4's basis already asserted "this is not H2 re-entering its family" when it was
written 2026-08-18 -- the check below is this session's own re-derivation of that claim, not a
restatement of it):

- **H2's explanandum:** can SD-032a's discrete argmax mode register produce graded occupancy
  AT ALL, at any cap? Answer, per V3-EXQ-935: **yes** -- time-averaged occupancy is monotone
  and cap-controllable within every seed across a 5-point sweep.
- **H4's explanandum:** given that it can, WHY does producing a mixed regime require a
  per-agent-tuned scalar constant (the cap value) in the first place? This is a question about
  the GAIN STAGE upstream of the argmax (a hard clip vs. a divisive/scale-free normalisation),
  not about the argmax's capacity to produce gradedness. H4's own basis states this explicitly:
  "Refuting H2 is a precondition of H4 being interesting" -- i.e. H4 is only a live question
  BECAUSE H2 was refuted, not despite it.

Same intervention locus (both concern the same substrate-level gain/arbitration machinery,
hence same family under the coarse taxonomy), genuinely different explananda. This is the exact
shape the caveat's worked instance describes (competence_floor's H-consummation-binding: same
locus as an eliminated leg, but conditioned on a state no prior leg had reached, hence
refinement not circling).

**Verdict: CONFIRMED false-positive circling.** The mechanical classifier is doing what it is
documented to do (family-granularity, locus-only), and the correct reading -- per the
registry's own standing operational rule -- is that this is expected and non-informative, not
a re-derive-brake trigger. Recorded on the qid's `fanout_growth_note` (this session,
2026-08-25) so a future reader does not have to re-derive this from the raw `circling` string,
and so a future governance walk or GOV-FANOUT-1-style scan does not misroute this question to
`/implement-substrate` on the strength of the bare classifier output.

**What would change this verdict:** a FIFTH leg landing in the `constitution` family whose
explanandum is the SAME as H2's ("can the register produce gradedness") rather than H4's
("why is a scale constant needed given that it can") would be genuine circling -- the
re-derive-brake logic should fire on that, not on H4.

## 4. H4 lit-pull gate

H4's pre-registration text (2026-08-18) states: "PROBE-GATED: a `/lit-pull` commission
(`targeted_review_salience_gain_normalisation`) must establish the biological case before any
substrate proposal." Before recommending that commission proceed, this session checked the
existing literature corpus directly (`REE_assembly/evidence/literature/`) rather than assuming
the topic is unpulled -- the C3 pre-routing check this skill's Step 7b names, applied by hand
since H4 has not yet had a formal autopsy pass to run the automated checker against.

**The biological case is already established, independently, in three existing targeted
reviews:**

| Review | Relevant entries | What it establishes |
|---|---|---|
| `targeted_review_connectome_mech_439` | Carandini & Heeger 2012 (canonical normalisation), Louie 2013 (value divisive normalisation), Reynolds 2009 (normalisation + attention), Kravitz 2010 (D1/D2 opponency) | Divisive normalisation as a canonical, cross-species, cross-domain computation, EXPLICITLY including value coding and attention -- the domain closest to salience arbitration |
| `targeted_review_sd_082` | Carandini & Heeger 2012 (independently pulled a second time), Louie 2011 (divisive normalisation, value) | Same canonical case, applied to an ANALOGOUS prior REE fix: SD-082 replaced a hard clamp with a bounded/soft (centering+tanh) gain stage on a different consumer (rule-selection action-bias head) precisely because "the hard clamp... zeroes the REINFORCE gradient... divisive gain control bounds responses without ever having a flat region." This is the exact argument H4 needs, already written, on a structurally analogous fix. |
| `targeted_review_striatal_gain_control_bounding` | Pommer et al. 2021 (SPN-SPN lateral inhibition), Kohnomi 2016 (DA-graded normalizer), Chen 2020 + Gowrishankar 2018 (D2-autoreceptor homeostat / runaway) | Pommer 2021 is the closest anatomical match in the whole corpus to `SalienceCoordinator`: striatal spiny-projection-neuron lateral inhibition, described by its own authors as "divisive-normalization-flavoured" competitive gain, directly inside the basal-ganglia substrate MECH-266/SD-032a already cite as their reference mechanism. Kohnomi/Chen/Gowrishankar establish that the biological normalizer is itself gain-tunable and that removing its saturating constraint produces exactly the runaway/bang-bang dynamics this cluster observed. |

This is a direct instance of the pattern the skill's own Step 7c names as the largest
adversarial-review finding class: "a literature entries exist for a question declared ABSENT"
(C3), citing V3-EXQ-936 as precedent (a red-team pass caught an autopsy commissioning a
`/lit-pull` for four entries already in the corpus).

**What the existing corpus does NOT establish**, stated so this is not oversold: none of these
entries measure divisive normalisation specifically in a mode-ARBITRATION / task-commitment
gate (they cover contrast, value coding, attention, and general striatal lateral inhibition).
If a substrate proposal for H4 needs a citation more specific than "divisive normalisation is
the canonical BG/cortical gain-control mechanism and SPN lateral inhibition is its concrete
striatal instantiation," that is a narrower, cheaper gap-fill question than the fresh full
review H4's pre-registration called for -- and per the user's decision at the Step 8 gate
below, is deferred rather than commissioned now.

**Recorded on the registry (this session, 2026-08-25):** H4's `basis` and `resolution.basis`
both updated to state the probe-gate is satisfied by the existing corpus, citing the three
reviews above; no `targeted_review_salience_gain_normalisation` commission is owed. H4 remains
`alive` (the biological case existing is not itself an adjudicating run) and is noted as
blocked behind V3-EXQ-935a (H1 confirmation) so any substrate proposal is tested against a
settled operating point rather than a still-provisional one.

## 5. Interactive gate (Step 8) -- confirmed 2026-08-25

Presented to the user: the circling-verdict analysis (Section 3) and the H4 lit-pull-gate
finding (Section 4), each with a recommended disposition. Both recommendations confirmed:

1. **Record the circling-vs-refinement resolution explicitly** on the registry (done, Section
   3) rather than leaving it implicit in H4's pre-registration prose.
2. **Mark the H4 lit-pull gate satisfied by existing lit** (done, Section 4) rather than
   commissioning a fresh `/lit-pull` or narrowing its scope.

Both answers logged to `RECOMMENDATION_LOG.jsonl` per the standing recommendation-agreement
ledger rule (`record_recommendation_outcome.py`, both pushed to `REE_Working` origin/master).

## 6. Routing (reported, not chipped)

Per the standing rule (a `/failure-autopsy` session does not `spawn_task` follow-on that
depends on its own not-yet-governance-reviewed disposition), the following are reported here
and in the closing WORKSPACE_STATE note, not chipped from this session:

- **`/queue-experiment`: V3-EXQ-935a** -- H1's confirmatory run, pre-registering r=2.45 against
  FRESH out-of-sample seeds (per V3-EXQ-935's own basis). Not yet queued. This is the single
  next experiment that would move `mech266_mode_arbitration_saturation` toward `decidable`.
- **No `/lit-pull` commission** for H4 -- see Section 4. If a future session judges the
  gap-fill question in Section 4's caveat worth pursuing, scope it narrowly (mode-arbitration /
  task-commitment specific), not as a fresh general review.
- **No `/implement-substrate` action** -- the `mode-governance-engagement` substrate entry
  already covers the open build question and does not need amending again from this session;
  nothing here changes its `severity`/`substrate_paths`/`implementation_hint`.
- **No `/claim-synthesis` action** -- re-checked `granularity_debt_cluster.py MECH-266`
  (2026-08-25): alignment distribution now `intact=6, unclear=2, weakened=2, unstamped=1`
  against the FULL corpus, but the standing scan (`check_granularity_debt_recurrence.py`)
  restricted to the recent 4-run chain reports NO target reading `weakened` -- still
  measurement/implementation debt, not granularity debt. The original cluster autopsy's
  `defer_until: "the H1/H2 portfolio resolves"` is PARTIALLY met (H2 resolved, H1 not yet
  confirmed) -- re-check again once V3-EXQ-935a lands.

## 7. Coordination-plane pause -- not obtained (recorded per skill discipline)

This session's coordination-plane pause claim (`mech-266-rescore-circling-2d31ca-autopsy-pause`,
`autopsy-pause:` prefix) was refused by `task_claim.py open` arbitration: `TASK_CLAIMS.json` and
`TASK_CHIPS.json` are legitimately owned by a concurrent, unrelated active claim
(`f-dominance-regime-retest-ddbe10-wedge`, "Mac umbrella ref-wedge repair", opened
2026-08-25T17:18:29Z, still active) genuinely repairing an umbrella `REE_Working` ref-wedge
(ahead/behind churn on `master`). Per the arbitration rule, the earlier claim owns and this
session deferred rather than overriding it. Proceeded WITHOUT the pause: this session's writes
are narrow (this document + the two registry note edits in Section 3/4) and do not touch
`claims.yaml`, `experiment_queue.json`, or `substrate_queue.json`, so the metaworker-interference
risk the pause exists to close is low for this specific scope.

## 8. Dry-run gate

Not applicable -- no new experiment run is adjudicated by this document. The re-scoring cited
in Section 2/H3 (`mech266_h3_rescoring_20260825.md`) already ran its own dry-run check against
the two source manifests (`v3_exq_464e_...`, `v3_exq_467e_...`), both confirmed real full-budget
runs by the original 2026-08-13 cluster autopsy's Step 2a gate (`dry_run_checked: true,
excluded_dry_run_ids: []`).
