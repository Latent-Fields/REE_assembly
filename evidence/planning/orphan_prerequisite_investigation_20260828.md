# Orphan-prerequisite investigation: classifying the 30, and what they turn out to mean

**Date:** 2026-08-28 · **Session:** `metaworker-chip-20260828-orphan-prerequisite-investigation`
(chip `chip-20260828-orphan-prerequisite-investigation`, `task_256fc89c`)
**Status:** FINDING -- registry investigation. No claim status changed here; five
`governance_flag.py` entries raised (GFLAG-0094..0098) for the user / `/governance` to
disposition.
**Prompted by** `evidence/planning/unrunnable_falsifier_population_20260828.md` Section 7's
addendum: of 185 claims that declare an unmet falsifier precondition, 155 name a registered
claim id inside that precondition and 30 name none. The user: *"prerequisites could be matched
to existing claims and where there are orphan prerequisites this may need further investigation
as it could be enlightening."*

---

## 1. Method

For each of the 30, the full `what_would_answer` + `notes` text was read verbatim and the
precondition classified by what it is actually asserting, then cross-checked against
`docs/claims/claims.yaml` (other claims' `depends_on`), `evidence/planning/substrate_queue.json`
(`unblocks_claims`), the IGW ledger/workset (`igw_routine_ledger.json`, `igw_assignments.json`,
`inter_governance_workset.md`), `evidence/planning/*_plan.md`, and `ree-v3/ree_core/` (for an
unregistered code build under a different name).

**The 30, phase in brackets:** ARC-007(-), Q-007(-), ARC-018(-), MECH-035(-), MECH-037(-),
MECH-048(-), INV-090(-), MECH-342(v3), Q-062(v4), Q-065(v4), Q-066(post_v5), Q-069(-),
Q-072(v4), Q-073(v5), MECH-424(v6), MECH-425(v4), MECH-426(v3), MECH-427(v3), ARC-105(v4),
MECH-453(v4), Q-083(v4), Q-086(v3), Q-089(v3), MECH-481(v3), MECH-489(v3), MECH-490(v3),
Q-092(v3), SD-097(v3), Q-093(v3), MECH-521(v4).

## 2. The set is not binary -- five kinds, not two

The addendum's own spot-check already found two kinds (runtime-state vs. genuine orphan).
Reading all 30 in full splits it further:

| Kind | What it means | Count |
|---|---|---|
| **A -- runtime-state / measurement-adequacy** | Asserts what a RUN must exhibit (non-degenerate variance, a value clearing a floor, a matched design) on substrate that already exists. Correctly claim-free -- there is nothing to cite. | 16 |
| **B -- genuine orphan** | Names a specific unbuilt substrate/capability with NO owner anywhere in the registry, substrate_queue, or IGW ledger. | 5 (incl. one partial) |
| **C -- self-referential** | The "prerequisite" is this claim's OWN unbuilt mechanism -- not a distinct blocker, just the claim's own not-yet-built status restated as a precondition. | 4 |
| **D -- detection-scope artifact** | The precondition text is claim-free ONLY inside the strict clause the original scan matched; the substrate it needs is already named and already in `depends_on` (or `substrate_queue`/IGW) a sentence or two earlier in the SAME field. Not a finding about the registry, a finding about the detector's scope. | 4 |
| **D' -- naming/dependency GAP** | The claim's own text names a specific registered claim as the real blocker, but that id is missing from `depends_on`. A genuine registry defect, but the fix is "add an edge," not "build something." | 2 |
| **E -- resolved-but-unlinked** | The needed substrate appears to have ALREADY been built and validated (a PASS experiment exists), but the validating run was never tagged to the claim, so the precondition was never re-checked. | 2 |

(Counts sum to 31 because MECH-521 straddles B and E -- see Section 4.)

## 3. Full classification

| Claim | Kind | Precondition, quoted | Verdict |
|---|---|---|---|
| **ARC-007** | A | "(a) the residue field must carry live non-flat structure in A0... (b) the A0->A1 harm gap must reproduce EXQ-114's magnitude... (c) the permutation must verifiably change the field state" | Run-time adequacy on the existing hippocampal/residue substrate. Nothing to cite. |
| **Q-007** | B/E | "Substrate-blocked on the candidate-differentiated modulatory-variance substrate (per-candidate modulatory variance + range-not-magnitude readiness gate seeded by the 643 autopsy)" | See Section 4.1 -- likely already built (V3-EXQ-643a), never linked. GFLAG-0097. |
| **ARC-018** | A | "e2_world_r2 >= 0.6 measured IN-RUN"; "rollout-derived scores must carry non-zero cross-candidate variance"; "harm_advantage_mean EXACTLY 0.0... trap it explicitly" | Run-time adequacy on the existing E2/rollout substrate. |
| **MECH-035** | A | "requires the named VALENCE component streams... to be independently computable per candidate trajectory and to show non-zero cross-candidate variance on at least two components simultaneously" | Adequacy check on existing VALENCE streams (SD-010/SD-011/MECH-302/etc, already `depends_on`-linked via ARC-017/ARC-003/ARC-005). |
| **MECH-037** | C | "This claim currently has no V3 substrate or experiment built against it... a run attempting to test it before the provenance-gating pathway... actually exists in the substrate should self-route substrate_not_ready" | The "pathway" named IS MECH-037's own mechanism. Building MECH-037 discharges its own precondition; there is no external claim to cite. |
| **MECH-048** | D | "requires mu driven from UPSTREAM environmental state... requires the contested modes to actually be occupied" | Both legs ARE routed -- `sd_032d_mu_kappa_mode_prior_overlays` (status `implemented_pending_validation`) and `sd_salience_contested_mode_occupancy` (status `probe_queued`) both list MECH-048 in `unblocks_claims`. The claim's own prose just cites the *mechanism* ("write_gate breadth"), not the substrate_queue `sd_id` -- an artifact of citing by build description rather than id, not an unrouted claim. |
| **INV-090** | D' | "needs a NEW maturation curriculum... [2026-07-16 UPDATE] the real unblock is a DISTINCT, non-flat, experienced harm-evaluation signal..., itself blocked on the committed-action/conversion (F-dominance) ceiling" | The named blocker ("F-dominance ceiling") IS MECH-439 ("F-dominance bounds committed-action diversity"), absent from `depends_on`. GFLAG-0094. |
| **MECH-342** | A | "a run only tests MECH-342 if it first establishes GENUINE sustained commitment... AND the readiness-degradation manipulation is verified non-vacuous" | Run-time adequacy; internal correctness already confirmed by V3-EXQ-592g. |
| **Q-062** | D | "Once a durable model-update substrate with an OPEN online write channel exists" | Tracked as `inter_governance_workset.md` **IGW-20260828-026** ("Event-level write-authority gate over the durable model-update path (MECH-368) + its falsifier (Q-062)"), status `blocked`. Routed, just not by claim-id citation in the prose, and not (yet) in the IGW ledger/assignments JSON the original 64/185 measurement scanned. |
| **Q-065** | D | "HARD PRECONDITION: at least two NON-DEGENERATE sense-specific adaptors must exist" | The substrate (ARC-087 + MECH-372) IS named, one sentence earlier in the same field, and IS in `depends_on`. Detection-scope artifact only. |
| **Q-066** | A/C | "a physical-cognifold-substrate DECISION must have been taken and a candidate medium must actually be available to characterise" | Not a build precondition at all -- an organisational DECISION (which physical medium to characterise). The candidate (MECH-374) is already named and `depends_on`-linked. |
| **Q-069** | **B** | "the benchmark harness must EXIST and be non-degenerate... The harness is PLANNED-not-built" | Genuine orphan. See Section 4.2. |
| **Q-072** | D | "Resolvable only against a V4 plasticity-gain substrate" | The substrate is ARC-093 + MECH-398 (state-conditional plasticity gain gate), already `depends_on`-linked. Not unowned. |
| **Q-073** | D | "a non-degenerate multi-agent substrate with SEPARATELY representable other-bound suffering/threat and other-bound liking/wanting streams must exist" | ARC-059 (social spine) + MECH-408 (developmental ordering) are named earlier in the field and already `depends_on`-linked. |
| **MECH-424** | D' | "requires a linguistic input channel REE-v3 does not have (the V6 language interface: ARC-009 realisation / MECH-373 / MECH-422)" | ARC-009 is in `depends_on`; **MECH-373 and MECH-422 are not**, despite being named as the needed channel. GFLAG-0095. |
| **MECH-425** | **B** | "REE-v3 has no explicit retrieval-readiness gain knob and no content-selective retrieval-suppression operator over episodic/ContextMemory read-out" | Genuine orphan. See Section 4.3. |
| **MECH-426** | C | "the velocity signal must have non-zero cross-condition RANGE... a range-zero velocity self-routes substrate_not_ready" | The velocity signal is this claim's OWN mechanism. Self-referential. |
| **MECH-427** | A | "subgoals must actually be attained at a NON-ZERO rate in the run (else there is nothing to credit -- the goal_pipeline GAP-2 foraging/benefit-contact-ceiling trap...)" | Run-time adequacy; the one bare-ish GAP citation here is self-qualified ("goal_pipeline GAP-2") in the prose itself. |
| **ARC-105** | **B** | "requires a multi-scale goal-representation substrate that does not yet exist" | Genuine orphan. See Section 4.4. |
| **MECH-453** | C | "SUBSTRATE-CONDITIONAL / NOT YET BUILT (no event-locked plasticity-window gate exists on the selector...)" | The gate IS this claim's own mechanism (paired with MECH-452, already `depends_on`-linked, "build together"). Self-referential. |
| **Q-083** | **B** | "SUBSTRATE-BLOCKED: V3 has only one real domain, so the transfer test has no second domain to run in" | Genuine orphan. See Section 4.5. |
| **Q-086** | A | "the sensory tier z_harm_s must differ across arms" | Run-time adequacy on the existing SD-086/SD-087 substrate; just a parameter sweep. |
| **Q-089** | A/D | "requires seeds to show non-degenerate variance in BOTH the competence outcome AND a measurable information-seeking trajectory statistic" | Run-time adequacy; the actual substrate gate (MECH-482/MECH-483) is already `depends_on`-linked and stated in the notes, just not repeated in this sentence. |
| **MECH-481** | A | "the underlying typed discrepancy signals... must show non-zero cross-trial-type variance in Arm 1's baseline" | Substrate (SD-091 coalition controller) is already built and wired (2026-08-02/03); only the falsifier experiment (step 7) remains. |
| **MECH-489** | A | "requires the two onset channels... to show non-zero variance in the evaluation run" | Substrate already built 2026-08-09 (SD-099); run-time adequacy only. |
| **MECH-490** | A | "requires (a) spawn position matched... and (b) E3Selector commit-variance/commit-gate-engagement logged" | Design/measurement precondition on the existing E3Selector; forward plan is a `/queue-experiment` fix, not a build. |
| **Q-092** | A | "requires both trained-policy arms... to produce non-zero-variance trajectory-segment feature vectors"; pipeline-validity precondition | Measurement-methodology precondition on the existing SD-054 reef substrate. |
| **SD-097** | C | "no ree-v3 code implements any form of typed multi-relation possibility storage as of registration" | This claim IS the proposed substrate (a `substrate_design` claim). Self-referential by construction. |
| **Q-093** | A' | "the comparison is vacuous unless REE and the baseline system are first matched at approximately equal behavioural competence" | Not a REE substrate gap at all -- an evaluation-design precondition (a matched external comparison point must exist). Own text says the measurement protocol is fully describable now; only the matching hasn't happened. |
| **MECH-521** | **B**/E | "three gates, ALL currently FALSE in V3: (P0) unit count must be endogenous, (P1) the resource horn must be expressible, (P2) capacity and occupancy must be independently manipulable" | Split verdict. See Section 4.6. |

## 4. The genuinely enlightening cases

### 4.1 Q-007 -- the substrate this claim is waiting on may already be validated, and nobody linked it

Q-007's HARD PRECONDITION reads: *"z_beta must carry cross-context variance -- V3-EXQ-643's
autopsy found the modulatory signal had magnitude but ZERO cross-candidate range... Substrate-
blocked on the candidate-differentiated modulatory-variance substrate... seeded by the 643
autopsy."*

`ree-v3/experiments/v3_exq_643a_modulatory_authority_validation.py` is the direct successor to
that same 643 autopsy. Its own docstring: *"WHY 643 FAILED... the real binding cause: [a
float32 catastrophic-cancellation bug]... At normal score magnitude the substrate already fires
correctly."* Its manifest
(`evidence/experiments/v3_exq_643a_modulatory_authority_validation_20260606T222930Z_v3.json`):
`outcome: PASS`, `evidence_direction: supports`, `readiness_met: True`,
`p_range_measured: 0.221807` (clearing the floor the original 643 autopsy found at zero) --
**and `claim_ids: []`**. The fix landed in `e3_selector.py` 2026-06-06 and the validating run
passed the same day. Nothing tags it to Q-007.

**Caveat, stated plainly:** 643/643a's "cross-candidate range" is about the E3 candidate-
SELECTION authority gate (whether the modulatory bias differentiates across the K candidates
scored at a single tick); Q-007's own question is whether z_beta clusters into stable regimes
across affect CONTEXTS (harm-proximal / goal-proximal / resource-depleted) over an episode.
These are related (both are "does the modulatory channel carry real cross-X variance") but not
obviously the *same* substrate claim. This is not resolved here -- it is exactly what
GFLAG-0097 asks an owning session to check. If they are the same, Q-007's `substrate_conditional`
gate may already be lifted and nobody has looked; if they are different, Q-007's citation of the
643 autopsy needs updating to point at whatever DOES carry the z_beta-context gap.

### 4.2 Q-069 -- a claim that says "the harness is planned" that is, in fact, not tracked anywhere

Q-069's falsifier needs "a purpose-built meta-agent benchmark harness... PLANNED-not-built."
That word choice implies a plan exists. Search of `evidence/planning/*.md`,
`igw_routine_ledger.json`, `igw_assignments.json`, and `inter_governance_workset.md` for
"meta-agent benchmark" / "evaluation-channel-integrity" / "Q-069" turns up **only Q-069's own
claims.yaml entry**. "Planned" describes the claim's own intent, not a tracked artifact. This is
the cleanest orphan in the set: a real, specific, buildable thing (a sandboxed toy repo +
mock evaluation API + decoy scoring artifacts) that nothing routes.

### 4.3 MECH-425 -- the named READ-side sibling of an existing WRITE-side gate family, unbuilt and untracked

MECH-425 explicitly frames itself as "the READ-side sibling of MECH-261's mode-conditioned
WRITE-gate family: REE owns the gates but not this retrieval-time gating POLICY." Its own sibling
question, Q-076, *depends on* MECH-425 (asks about the interaction of MECH-425's Line A/Line B),
it does not build it. No `substrate_queue` entry, no IGW mention, no code hit for
`reinstatement_gain` / `retrieval_readiness` / `competitor_suppression` anywhere in
`ree-v3/ree_core/`. Confirmed unowned.

### 4.4 ARC-105 -- goal granularity is a named, real, orthogonal gap

ARC-105 is explicit that it is NOT covered by ARC-051 ("Extends ARC-051's emergent multi-LEVEL
wanting hierarchy... with an ORTHOGONAL axis -- the representational GRANULARITY of the goal
itself"). No other claim, substrate_queue entry, or IGW item references a multi-scale /
granularity-matched goal representation. Confirmed unowned.

### 4.5 Q-083 -- the multi-domain substrate that would let any domain-generality claim run

Q-083 needs "a genuinely multi-domain substrate" -- V3 has exactly one domain, so there is
nothing to transfer between. This is arguably the highest-leverage orphan in the set: if it
were ever built, it would also unblock any FUTURE claim about domain-generality (rule
apprehension, cross-domain transfer, generalization), not just Q-083. Confirmed unowned
anywhere.

### 4.6 MECH-521 -- split: the cheap desk-derivation was already done; the substrate build gaps were not

MECH-521's own text names a "DERIVATIONAL PRECONDITION, OWED FIRST AND CHEAPEST" -- a small
lateral-inhibition settling toy, explicitly "NO REE substrate at all" -- as the thing to do
*before* any substrate work is justified.

That toy was already run: `evidence/planning/mech521_settling_signature_derivation_20260826.md`
(2026-08-26, session `insights-7fd98a`). Verdict: settling alone gives only the pure SLOT horn
(per-item fidelity pinned at 1.000, no graceful phase) -- MECH-521's claimed hybrid signature
needs a **third ingredient** (a shared normalisation budget) that the claim as registered does
not name. The doc identifies where that ingredient already lives in the substrate
(`_loop_normalize` / MECH-448's rank-preserving envelope) and ends with an explicit, unapplied
recommendation: *"Amend MECH-521 to name the shared budget as a required third ingredient... Do
not retire the claim: leg 2 is derived."* That recommendation has no governance flag and is not
reflected in claims.yaml -- GFLAG-0096 now raises it.

The claim's actual **build** preconditions (P0 endogenous unit count, P1 the resource horn,
P2 capacity/occupancy independence) remain unmet and untracked. The closest existing substrate,
`mech-045-object-file-buffer` (ObjectFileBuffer, `unblocks_claims: [MECH-045, ARC-006, ARC-080
Pillar 1]`), is about persistence validation at `world_dim>=128`, not about endogenising the
item count or decoupling capacity from occupancy -- it does not cover MECH-521's specific gaps.
So MECH-521 is a genuine orphan for its BUILD leg even though its DERIVATION leg is already
discharged. GFLAG-0096 covers both halves.

## 5. GAP-id hygiene (minor, as scoped)

Confirmed: `GAP-N` ids are **plan-namespaced and heavily reused**, not globally unique. A single
grep for `\bGAP-2\b` across `evidence/planning/*_plan.md` hits 11 different plans; `\bGAP-7\b`
hits 11 different plans with visibly unrelated meanings in at least two of them (e.g.
`goal_pipeline_plan.md`'s GAP-7 is object-bound incentive-salience binding; `infant_substrate_plan.md`'s
GAP-7 is an unrelated end-of-episode trajectory-pair statistic).

Within this 30-claim set specifically:
- **MECH-427** cites `GAP-2` already qualified in prose ("the goal_pipeline GAP-2
  foraging/benefit-contact-ceiling trap") -- self-disambiguating, confirmed to match
  `goal_pipeline:GAP-2` in `goal_pipeline_plan.md`. No action needed.
- **Q-065** and **Q-069** both use the bare phrase "off the V3 / GAP-7 critical path" with no
  plan qualifier. `goal_pipeline_plan.md`'s GAP-7 (object-bound incentive salience) is
  semantically unrelated to either claim's subject (multimodal perception; meta-agent
  governance benchmarking) and was in any case already reported CLOSED in
  `evidence/planning/critical_path_synthesis_2026-06-15.md` -- so if this bare "GAP-7" is meant
  to reference that node, the citation is stale as well as ambiguous. More likely it is a stock
  phrase from a shared drafting template rather than a real dependency edge, but as written it
  cannot be resolved to one specific plan. Not flagged separately (per the brief's own scoping,
  this is a minor note); worth a future pass qualifying both occurrences (`goal_pipeline:GAP-7`
  or whichever plan is actually intended, once identified) if anyone touches these two claims.
- `GAP-1`, `GAP-14`, `GAP-3b` (the other three ids named in the parent measurement) do not
  appear inside this 30-claim set's precondition text -- they belong to claims among the other
  155 (matched-claim) orphans and were out of this chip's scope.

## 6. Governance flags raised (this session, all `stale_note`, pushed to `origin/master`)

| Flag | Claims | What it asks for |
|---|---|---|
| GFLAG-0094 | INV-090, MECH-439 | Add MECH-439 to INV-090's `depends_on` (real blocker per its own 2026-07-16 note). |
| GFLAG-0095 | MECH-424, MECH-373, MECH-422 | Add MECH-373 + MECH-422 to MECH-424's `depends_on` (named as the needed V6 channel, both absent). |
| GFLAG-0096 | MECH-521 | Apply the unapplied 2026-08-26 derivation recommendation (name the shared-budget third ingredient); note the P0-P2 build gaps remain separately unmet and untracked. |
| GFLAG-0097 | Q-007 | Check whether V3-EXQ-643a (PASS, `claim_ids=[]`) already satisfies or informs Q-007's precondition; link or clarify. |
| GFLAG-0098 | ARC-105, Q-083, MECH-425 | Three claims whose named substrate has zero build route anywhere (no claim, no substrate_queue entry, no IGW mention, no code). Decide whether to register substrate_queue entries (deferred is fine, all are off-critical-path by their own text) or mark explicitly out of scope. |

No claim status was changed. No new claims were registered. No substrate_queue entries were
created. No experiments were queued.

## 7. What this adds to the parent finding

`unrunnable_falsifier_population_20260828.md`'s core diagnosis -- REE's claims carry
load-bearing structural assertions in PROSE that nothing routes or checks -- gets sharper here.
Of the 30 claims whose precondition names no registered claim, **most (D/D'/A/C, 26 of 30) are
either correctly claim-free or already tracked under a different label** (a substrate_queue
`sd_id`, an IGW item, a `depends_on` edge one field over) -- the absence of a claim-id citation
in the strict precondition sentence overwhelmingly over-counts genuine orphaning. **A genuine
minority (ARC-105, Q-083, MECH-425, Q-069, and MECH-521's build leg) really do point at
substrate nobody owns.** None of the five converge on the SAME missing thing -- they are five
independent gaps (goal granularity, multi-domain infrastructure, retrieval-time gating, a
meta-agent benchmark harness, and object-file capacity/occupancy decoupling), not one shared
claim waiting to be written. The more load-bearing finding is the other direction: **twice in
this set (Q-007, MECH-521) a claim's own stated blocker looks like it has already been
addressed by work that was never linked back** -- which is the same "prose nothing reads"
failure mode as the unrouted-121 finding, just running the opposite way: not "the registry
promised a route and never built it," but "the substrate got built and the registry never
noticed."

## 8. Limits

- Classification (Kind A-E) is a judgment call made by reading each claim's full text once;
  it is not machine-checked and a second reader could draw a line differently at the A/D or
  C/B boundary in a few cases (MECH-037, MECH-453 in particular are close to B).
- The "no owner anywhere" verdict for the five Kind-B/E claims is based on keyword/phrase
  grep across claims.yaml, substrate_queue.json, the IGW ledger/workset, `*_plan.md`, and
  `ree_core/` -- a differently-worded reference (as with MECH-048's `sd_id` citation) could
  still exist and be missed by this method. This is the same recall caveat the parent
  measurement documents.
- Q-007's Section 4.1 finding is deliberately left as an open question for governance, not a
  claimed resolution -- the two substrates (E3 candidate-selection authority vs. z_beta
  cross-context clustering) may or may not be the same thing.
