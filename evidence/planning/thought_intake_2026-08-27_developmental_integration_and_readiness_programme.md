# Thought Intake -- Developmental Integration and Readiness Programme

**Date:** 2026-08-27
**Raw thought:** `docs/thoughts/2026-08-27_developmental_integration_and_readiness_programme.md` (1253 lines, imported verbatim from an external Dropbox capture)
**Session:** `thought-ingest-devintegration-20260827`
**Stage:** 2 (structured intake). Registration into `claims.yaml` is **STAGED, NOT APPLIED** -- see section 6.

---

## 1. What this capture is

A repo-audited synthesis/programme document, self-declared non-authoritative (its own section 20:
"complete enough to act as a routing document"). It is **unusual for this pipeline in being mostly
subtractive**: its Appendix B is eight self-retractions of its own first draft, and its section 0.1
novelty table dispositions eleven of twelve threads as already-owned or partly-owned by REE.

That posture is the correct one for Step 4 of `/thought-ingestion` ("extraction beats invention"),
and it means this intake's job is narrower than usual: verify the audit, then isolate the residue
that is genuinely not in the registry.

### 1a. Audit verification performed this pass

The document's factual claims were spot-checked rather than accepted:

| Claim in the capture | Verification | Verdict |
|---|---|---|
| 12 canonical anchors in its Appendix A | all 12 paths resolve in `REE_assembly` | **confirmed** |
| `ree_v3_baseline@v0` is an empty placeholder | `canonical_profiles/ree_v3_baseline.json`: `"overrides": {}`, frozen 2026-08-12, description says so explicitly | **confirmed** |
| "242 work items, only 22 ready and 0 in flight" | `evidence/planning/inter_governance_workset.v1.json` `summary`: `total 242, ready 22, in_flight 0` (generated 2026-08-27T18:37Z) | **confirmed verbatim**. Note the per-item `state` field shows 18 `in_progress`; the `in_flight: 0` summary field is a generator artifact, not the capture's error |
| `gumbel_learned` write-address policy exists | present in `ree-v3/ree_core/predictors/e1_deep.py`, `utils/config.py`, `agent.py` and `docs/architecture/contextmemory_write_address_selection.md` | **confirmed** |
| SD-SLEEP-ENTRY-PRESSURE / V3-EXQ-933a supersede the "sleep cannot fire in continuous life" finding | manifest `v3_exq_933a_sleep_gap9_entry_pressure_fix_20260826T072405Z_v3.json` exists; SD-SLEEP-ENTRY-PRESSURE cited across three 2026-08-16 autopsies | **confirmed** |
| No experiment-capability/plasticity preflight exists | zero tree-wide hits for `requires_mechanisms`, `requires_capabilities`, `requires_plasticity`, `capability_precondition_unmet`, `mechanism_unreached`, `nonplastic_misfire`; `torch.is_grad_enabled()` used **nowhere**; parameter-delta witnesses present ad hoc in exactly 4 experiment scripts | **confirmed -- this is the real gap** |

Consonance check: `docs/CURRENT_FRONT.md` independently names the live question as
"competence retention + installability -- 1 of 20 rival explanations still standing". The capture's
thesis and the repo's own live front agree without the capture citing that file.

---

## 2. Verbatim prompt -- the capture's core proposal

> **Turn REE's existing developmental commitments, readiness concepts and control mechanisms into a
> coherent organism-level integration programme that can explain and unblock the live V3
> competence/causal-reach failures.**

and, as its working programme hypothesis (section 1):

> **Many recurrent REE-v3 ceiling effects are different failures along a developmental causal-reach
> chain. They should become more tractable if experiments first establish the prerequisite
> organismal competencies, then test whether those competencies acquire authority, throughput,
> ecological consequence and retention.**

and the operational rule that carries most of its weight (section 3.1):

> **A run should not count as negative evidence for a learning- or development-dependent claim if
> the required learning pathway was not plastic during that run. "It did not learn" and "it could
> not have learned" are different scientific outcomes.**

---

## 3. Novelty table

| Thread in the capture | Existing REE coverage | Verdict |
|---|---|---|
| Developmental causal-reach chain (representation -> recruitment -> authority -> throughput -> ecology -> retention) | **ARC-130** owns the stage-qualified ladder verbatim; **ARC-131** owns installability; **ARC-120** owns competence-before-authority | **already owned -- cross-ref only.** The capture correctly self-dispositions this |
| "Developmental competence scoreboard" / Developmental Integration View (s2) | `developmental_curriculum.md` (ARC-019), `developmental_needs_register.md`, `developmental_metrics.md`, Levels 0-7 in `developmental_readiness_investigation_2026-08-12.md`, ARC-130/131 | **already owned x4.** Not registerable. See section 7 for the standing risk in building a fifth view |
| Ten "capability lanes" (s4) | ARC-019 stages + ARC-130 ladder, re-cut on a different axis | **already owned as content; the re-cut is a thinking aid.** Deliberately NOT registered -- see section 7 |
| Competence-to-authority bridge (s5) | ARC-120 asserts the ordering; ARC-005 control plane, SD-091/MECH-481 coalition control, existing gates provide the machinery | **already owned.** The capture's own recommendation is to test whether existing machinery suffices *before* proposing a controller -- that is a workstream, not a claim |
| Policy/representation co-development loop (s6) | SD-056, MECH-457, MECH-314a/b/c, MECH-455, MECH-496/INV-101, developmental repertoire gates | **already owned in components.** The gap named (a joint longitudinal assay) is an experiment, not a claim |
| Learning progress as a developmental objective (s6.3) | MECH-314c, MECH-455 | **already owned.** The capture explicitly retracts this from its own first draft (Appendix B) |
| Heterogeneous memory / no universal memory score (s7) | ContextMemory, hippocampal, E1 persistent, E2, residue, policy, categories all registered separately; MECH-094/MECH-261 write eligibility; V4 allocation line | **already owned.** Live need is validation, not registration |
| Non-oracular injections (s8) | **GOV-INTERVENE-1** owns the oracle/non-oracle x silky/oddly-composed taxonomy; **INV-103** owns the distinct runtime evidence-ingestion invariant | **already owned.** Capture retracts this itself |
| Sleep: liveness -> transformational competence (s9) | `sleep_substrate_plan.md`, SD-SLEEP-ENTRY-PRESSURE, causal matched-arm designs | **already owned.** The success-criterion sharpening is an experiment-design note |
| Waking vs offline update-transform taxonomy (s9.4, Deliverable 6) | **MECH-511** deep-update learning-eligibility gating | **adjacent, already owned.** The capture itself says "tie this to MECH-511 ... instead of inventing a standalone rule system" -- honoured; nothing registered |
| Endogenous recruitment / metacognition (s10) | SD-091 / MECH-481 substrate live-wired with eight consumer sites; falsifier scaffold exists | **already owned.** The gap is a competent adapting harness, i.e. an experiment blocker |
| Event-sourced developmental state (s12) | `status_history_plane_separation_design.md` -- append-only events + pure projector + `status_snapshot/v1` | **already owned.** Capture retracts its own "new ledger" proposal |
| **Capability/plasticity precondition for negative evidence (s3.1, s11.1, Deliverable 4B)** | **GOV-PATHVALID-1** guards a false *PASS* from a mocked precondition. **GOV-FAILLOC-1** triages an observed *FAIL* post-hoc into REE/mechanism/measures/environment. **Neither names plasticity at all**; grep confirms no claim anywhere covers `no_grad`/frozen-parameter runs as an interpretation category | **ADJACENT-BUT-DISTINCT -> REGISTER NARROWLY.** See 3a |
| **Four separable continuities of organismal long life (s11)** | Nothing owns the decomposition. Fishtank/906-lineage planning docs describe the *behaviour* (cognitive state persists, body/environment resets) but no claim makes the four-way distinction load-bearing | **GENUINELY NEW -> REGISTER** |
| Populated canonical integrated V3 profile (Deliverable 4A) | Mechanism exists (`canonical_profile.py`, `canonical_profile_admission_criteria.md`, `canonical_profile_fingerprint.py`); admission process has **never been run** | **not claim-shaped -- it is a task.** Route as a chip, not a registration |
| Behavioural Evidence Ladder (s18.4) | No such artifact exists (grep: zero hits) | **not claim-shaped -- an outward-facing curation artifact.** Route as a chip |
| Within-life plasticity inventory (Deliverable 5) | Not present | **not claim-shaped -- an audit artifact**, and a prerequisite input to GOV-CAPCONTRACT-1's preflight. Route as a chip |
| Research-philosophy principles (s18.6) | ARC-120, ARC-130/131, GOV-* family, existing architecture docs already carry each principle in claim form | **already owned.** The capture explicitly says these should be "preserved as research-method orientation, not automatically minted as claims" -- honoured |

### 3a. Why the capability/plasticity rule is distinct from GOV-PATHVALID-1 and GOV-FAILLOC-1

This is the discrimination the whole intake turns on, so it is stated explicitly rather than left
for a future session to re-derive:

- **GOV-PATHVALID-1** is a rule about **false positives**: a PASS obtained by injecting the state
  an upstream stage would have supplied is not evidence the pathway is reachable. Its own notes say
  it is "a DESIGN-TIME check on whether a PASS (not a fail) is entitled to the interpretation it is
  being given."
- **GOV-FAILLOC-1** is a rule about **false negatives**, and is therefore the near neighbour -- but
  it is (i) **post-hoc**, applied at autopsy time by human judgement, and (ii) its four buckets are
  REE / MECHANISM / MEASURES / ENVIRONMENT. A run in which the mechanism was correctly instantiated,
  the measures were adequate, and the environment was informative, but **every relevant parameter
  was frozen under `torch.no_grad()`**, ticks none of those four buckets. It is a fifth category,
  and it is currently invisible to the registry.
- The new rule is therefore the **pre-registered, machine-checkable, plasticity-aware complement**:
  the organism's required capabilities and its permitted modes of change are declared *before* the
  run and verified against the instantiated organism, and a run failing that check self-routes to a
  diagnostic status rather than entering the evidence record as negative evidence.

The capture's own falsifier for this (its section 17) is honest and worth preserving: *"runs that
pass the full capability/configuration/plasticity preflight still show the same apparent failures at
the same rate, indicating mis-instantiation was not an important source of prior nulls."*

---

## 4. Key formulations (verbatim, load-bearing)

> "It did not learn" and "it could not have learned" are different scientific outcomes.

> A scientifically negative-looking result can therefore arise because the target mechanism was
> absent, unreachable, competitively powerless, or non-plastic rather than because the proposed
> faculty failed.

> Otherwise an experiment can watch a frozen policy for a long time and mistake duration for
> developmental opportunity.

> Cognition should be developed, not merely installed. A mechanism existing in source is not the
> same as an organism possessing the faculty.

> A `health_depleted` boundary therefore regenerates the body/environment around a persisting
> cognitive system rather than constituting organismal death.

> Explicitness beats assumption. Mechanism enabled? Gradient flowing? Memory writable? Commitment
> reachable? Ecology informative? These should become recorded facts, not assumptions inferred
> after a null result.

> **REE already exhibits genuine behaviour and causal mechanism effects; REE has not yet
> demonstrated robust, accumulating, general organism-level competence.**

---

## 5. Affected existing claims

**Cross-referenced (`depends_on` / `related_claims` targets for the staged registrations):**
ARC-019, ARC-120, ARC-130, ARC-131, GOV-PATHVALID-1, GOV-FAILLOC-1, GOV-INTERVENE-1, GOV-DIAG-1,
MECH-511, SD-091 / MECH-481, MECH-457, SD-056, INV-103.

**Explicitly distinguished-from (recorded so a future session neither duplicates nor wrongly merges):**
GOV-PATHVALID-1 (PASS-side, not FAIL-side), GOV-FAILLOC-1 (post-hoc triage without a plasticity
bucket), MECH-511 (deep-update eligibility inside the organism, not experiment-interpretation
validity), INV-103 (runtime evidence ingestion, not experimental method).

**Amended:** none. No existing claim's `status`, `confidence`, `evidence`, or `live_status` was
touched in this pass, and none should be by this capture -- it registers nothing by its own
section 20.

---

## 6. Candidate claims -- STAGED, registration DEFERRED (concurrency block)

**Why this section says STAGED rather than REGISTERED.** `/thought-ingestion` Step 6 is a standing
correction against leaving new ideas as prose out of caution. This is **not** caution. At
2026-08-27T19:25Z `task_claim.py open` **refused with exit 3**: session
`responsibility-epistemic-hygiene-d6f9d3` (opened 19:00:29Z, `thought-digestion v3-closure
(grouped)`) holds an active claim on `REE_assembly/docs/claims/claims.yaml`,
`docs/assets/data/claims.json` and `WORKSPACE_STATE.md`, and is writing `what_would_answer` blocks
into existing entries right now. Appending to `claims.yaml` concurrently is the exact
read-modify-write contamination shape CLAUDE.md documents. The arbitration verdict is binding.

A narrowed claim was opened instead, covering only the two uncontended files this intake writes.
**Both entries below are drafted to paste; the registration pass owes only an ID re-check and the
append.** IDs are deliberately NOT pre-allocated (`ARC-` max was 134 at read time; another session
may register in the interim).

### STAGED-1 -- `GOV-CAPCONTRACT-1` (name verified free: 0 hits in `claims.yaml`)

- `claim_type`: `governance_rule`
- `subject`: `governance.epistemics.instantiated_organism_capability_contract`
- `polarity`: `asserts`
- `status`: `candidate`
- `epistemic_category`: `governance_rule`
- `claim_level`: `governance`
- `binds_at_version`: `v3`
- `blocks_v3_green_board`: `false`
- `registered_utc`: (date of the registration pass)
- `source_thought`: `docs/thoughts/2026-08-27_developmental_integration_and_readiness_programme.md`
- `depends_on`: `GOV-PATHVALID-1`, `GOV-FAILLOC-1`, `ARC-130`, `ARC-131`
- `related_claims`: `GOV-INTERVENE-1`, `GOV-DIAG-1`, `ARC-120`
- `location`: `docs/architecture/experiment_capability_contract.md#gov-capcontract-1` (new stub;
  `parent` to be chosen by surveying `grep -h "^parent:" docs/architecture/*.md | sort | uniq -c`)

**title (draft):**
> A run is not admissible as negative evidence for a claim unless the organism instantiated for
> that run was demonstrably able to express, and where the claim is learning-dependent to acquire,
> the faculty under test. Each organism-level experiment must therefore declare, and a preflight
> must machine-verify against the instantiated organism, at minimum: the canonical profile identity
> and every explicit deviation from it; the mechanisms and capabilities the hypothesis presupposes;
> whether those mechanisms were constructed, enabled and reached on the production path; whether
> their decisive readouts engaged often enough for the test to be non-vacuous; whether their output
> could compete at the relevant arbitration surface at the scale present in the run; which forms of
> change were permitted (parameters, policy/value, E1/E2 representations, memory state, residue/EMA
> state, offline updates); and, where online learning is load-bearing, whether gradients were
> enabled, the intended parameters were in an optimizer, and a parameter-delta witness confirms an
> actual update path. A run failing any declared precondition self-routes to a
> capability-precondition diagnostic status and MUST NOT be recorded as evidence against the claim.
> "It did not learn" and "it could not have learned" are different scientific outcomes.

**notes (draft):** carries the section 3a discrimination above verbatim -- PASS-side vs FAIL-side vs
plasticity-bucket -- plus: motivating observation is that `torch.is_grad_enabled()` appears nowhere
in the tree and parameter-delta witnesses exist ad hoc in 4 experiment scripts, while long-life
observational drivers run under `no_grad`, so "more observed ticks" has been silently equatable with
"more developmental opportunity". Nearest existing primitives are `experiments/_lib/precondition_gate.py`
(per-arm, per-run, regime-conditioned non-vacuity) and `experiments/_lib/canonical_profile_fingerprint.py`
(identity only) -- both real, neither joined into a per-run contract. **NOT YET APPLIED** to
`/queue-experiment` or `/failure-autopsy` skill text; formalising it there is a follow-on requiring
CLAUDE.md's GOV-HELDOUT-1 held-out check first. **STATUS STAYS CANDIDATE** until it has actually
changed at least one real experiment design or autopsy verdict, per the discipline GOV-HELDOUT-1
applies to itself.

### STAGED-2 -- `ARC-1xx` (allocate at registration; max was ARC-134)

- `claim_type`: `architectural_commitment`
- `subject`: `architecture.organismal_continuity_decomposition`
- `polarity`: `asserts`
- `status`: `candidate`
- `epistemic_category`: `substrate_conditional`
- `implementation_phase`: `v3` -- **flag for a `/governance` routing decision.** The capture places
  the persistent-ecology assay family in V3, and the 906 lineage already supplies partial cognitive
  continuity, so this is cheaply testable on existing substrate; but the routing call is not this
  skill's to make unilaterally.
- `version_relevance`: `v3_v4`
- `depends_on`: `ARC-130`, `ARC-131`, `ARC-019`
- `related_claims`: `ARC-120`, `MECH-511`
- `location`: `docs/architecture/organismal_continuity_decomposition.md#arc-1xx` (new stub)

**title (draft):**
> "Long life" in an artificial organism is not one property but at least four separable continuities
> -- cognitive/affective/mnemonic state continuity, parameter/plasticity continuity, body/homeostatic
> continuity, and ecological/world continuity -- which can be held or broken independently. A
> persistent-organism experiment must therefore declare which of the four it preserves, because
> duration under a broken continuity is not developmental opportunity: an organism whose cognitive
> state persists while its body and world regenerate at each boundary is not aging in a world, and
> an organism observed for many ticks with parameters frozen is not developing. Confounds that this
> decomposition separates and a scalar "lifespan" cannot: age from layout luck, learning from reset
> effects, injury/recovery from death, and memory accumulation from environmental regeneration.

**notes (draft):** motivated by the 906 lineage, where cognitive/affective/mnemonic state persists
across segment boundaries while the environment resets local layout and body health -- so a
`health_depleted` boundary regenerates body and world around a persisting cognitive system rather
than constituting organismal death. Distinct from ARC-131 (installability = simultaneous composition)
and from competence retention (survival of a competence through later learning): this claim is about
which *substrates of persistence* an experiment holds fixed, and is a precondition for interpreting
either. **DO NOT build a new continuity mechanism in V3 on the strength of this registration** -- the
claim's first use is as a declaration requirement on existing long-life drivers, and it composes with
GOV-CAPCONTRACT-1's plasticity field rather than duplicating it.

### Deliberately NOT registered

- **The programme hypothesis itself (capture s1/s17).** ARC-130 already owns the ladder, and the
  live hypothesis space is *already* working exactly this question -- `CURRENT_FRONT.md`:
  "competence retention + installability -- 1 of 20 rival explanations still standing (80% ruled
  out, ~4.32 bits removed)". Registering it would duplicate an active hypothesis space with a claim.
- **The ten capability lanes (s4).** They map to no claim ids, re-cut ARC-019 + ARC-130 on a third
  axis, and the capture's own disclaimer that they are "not a replacement" for the stage model is
  exactly the disclaimer that erodes once a vocabulary is written down. Useful as a thinking aid;
  registering them would create the second ladder the capture warns against.
- **The research-philosophy principles (s18.6).** The capture asks that these be preserved as
  method orientation, "not automatically minted as claims". Honoured.
- **The Developmental Integration View (s2), Behavioural Evidence Ladder (s18.4), populated
  canonical profile (Deliverable 4A), plasticity inventory (Deliverable 5).** Artifacts and tasks,
  not claim-shaped. Routed as chips -- see section 7.

---

## 7. Next steps

**Owed by this intake (blocked, not abandoned):**

1. **Register STAGED-1 and STAGED-2** once `responsibility-epistemic-hygiene-d6f9d3` closes its
   claim on `claims.yaml`. Re-check max `ARC-` id at write time; re-read `claims.yaml`'s tail
   immediately before appending; validate (`validate_claims.py --strict`), rebuild
   (`build_claims_json.py`), pathspec-limited commit.
2. **Write the two architecture stubs** named in the `location` fields, with `parent` surveyed
   rather than guessed.

**Routing / decisions owed to `/governance`, not decidable here:**

3. **STAGED-2's `implementation_phase: v3`** needs a routing ratification.
4. **Deliverable 4A (populate the canonical integrated V3 profile)** is a governance decision about
   which mechanisms are admitted, gated on the existing admission criteria and, for anything
   E3-adjacent, on the F-dominance investigation (per `ree_v3_baseline.json`'s own `notes`).

**Chippable follow-on (work-type is `/implement-substrate` or curation, not governance):**

5. Within-life plasticity inventory across long-life drivers -- prerequisite input to
   GOV-CAPCONTRACT-1's preflight, and the cheapest item in the whole programme.
6. The preflight/contract implementation itself (`experiments/_lib/` module + manifest fields +
   self-routing status), composing with `precondition_gate.py` rather than replacing it.
7. Behavioural Evidence Ladder v0, derived from `review_tracker.json` + reviewed manifests, **not
   written from memory**.

**Standing risk to carry forward (recorded because it will otherwise be rediscovered):**

8. The capture's section 2 warns against a second scoreboard and then proposes a Developmental
   Integration View, with the word "derived" as its only safeguard, and specifies no generator. The
   cautionary evidence is one directory away: `docs/CURRENT_FRONT.md` is a generated derived view
   that is **currently emitting `(could not derive front headline)` and `needs_review: true`**. If
   the Integration View cannot be a `generate_*.py` in `governance.sh` reading the four existing
   sources, it should not be built as prose.

**Literature:** none owed. This capture is an internal repo synthesis with no external citations
requiring verification (contrast the ARC-130 intake, which carried a Gulli citation needing a
verification pass).

**Honouring the capture's own maintenance criterion (its s20):** it asks not to be expanded as REE
changes. Imported once, marked processed, frozen. Live status belongs in the derived view if that
view is ever built; the capture remains the programme rationale and initial handover only.
