# Claim-gap analysis: goal / wanting / liking stream (object-bound incentive salience)

**Date:** 2026-06-01
**Intake:** `thought_intake_2026-06-01_goal_wanting_liking_stream_repair.md`
**Lit:** `literature_synthesis_2026-06-01_object_bound_incentive_salience.md`
**Status:** ANALYSIS + PROPOSALS. **No `claims.yaml` edit made.** Every "PROP-*" ID below is
a placeholder; real IDs are allocated by governance, not here. Existing claim status quoted
from `docs/claims/claims.yaml` as of this session.

---

## Part 1: existing claims mapped to the chain

Chain links (from intake closure map): L0 benefit pulse, L1 forced-seed -> z_goal,
L2 object-identity binding, L3 incentive/wanted token, L4 z_goal write-source,
L5 persistence, L6 cue-triggered wanting, L7 consumer readout, L8 pre-consummatory approach,
L9 wanting!=liking dissociation.

Coverage legend: Y = directly covers, ~ = partial/adjacent, . = does not cover.

| Claim | Current wording (abbrev.) | Status / evidence | L0 | L1 | L2 | L3 | L4 | L5 | L6 | L7 | L8 | L9 | Gap verdict |
|---|---|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|---|
| **SD-012** | Goal-directed behaviour requires drive-modulated benefit for z_goal seeding | provisional; 085f C1 PASS, C2 FAIL; GAP-3 done (582a) | Y | ~ | . | . | . | . | ~ | . | . | . | OK for L0; multiplier sits on the seeding gate not on a cue-recalled object value (lit A4) -- **mis-located, not wrong** |
| **MECH-306** | sustained_drive_trace (drive EMA/floor) | candidate_substrate_landed; 582a PASS | Y | ~ | . | . | . | ~ | . | . | . | . | OK; maintenance of drive, not object binding |
| **SD-015** | Dedicated z_resource encoder (object-type features, location-invariant) | candidate; encoder landed, goal_resource_r weak | . | . | ~ | . | Y | . | . | . | . | . | Closest to L4 write-source; identity head trains but binding to wanting unproven |
| **MECH-112** | E3 needs structured latent goal repr distinct from harm avoidance | candidate; 074d/e C1 confounded | . | Y | . | . | ~ | . | . | ~ | . | . | Covers "a goal repr exists"; silent on object identity |
| **MECH-230** | z_goal latent structure (norm>0) distinct from harm | provisional; v3_pending; substrate confirmed | . | Y | . | . | ~ | . | . | . | . | . | L1 covered; needs amend for "written from object pointer" (L4) |
| **MECH-116** | E1 LSTM = working memory maintaining goal w/o ongoing benefit | candidate; 076d FAIL (persists too long) | . | . | . | . | . | Y | . | . | . | . | L5 covered (un-tuned, not absent) |
| **ARC-032** | Theta-rate E1 packaging is primary path goal-context->E3 | candidate; theta-bypass never ablated | . | . | . | . | . | ~ | . | ~ | . | . | L5 transport; untested standalone |
| **MECH-117** | Wanting (z_goal distance) and liking (benefit_eval) functionally dissociable | **stable**; 074d/e C2+C3 PASS, C1 confounded; pending_retest_after_substrate | . | . | . | ~ | . | . | . | . | . | Y | **Stale/over-strong relative to 514k**: dissoc fraction 0.0 in 514k. The L9 claim is "stable" but the only non-degenerate identity test failed. Flag for governance re-examination. |
| **MECH-229** | E3 produces distinct wanting vs liking behavioural signals (approach vs consummatory) | provisional; PASS evidence on z_world fallback (degenerate) | . | . | . | ~ | . | . | ~ | ~ | Y | ~ | L8 covered; L9 selectivity NOT shown non-degenerately (514k) |
| **MECH-295** | Drive->liking-stream->approach-cue (modulation, not sole route) | candidate; v3_pending; 493 isolation 6/6 PASS | . | . | . | ~ | . | . | Y | ~ | Y | . | L6/L8 covered in isolation; cue is env-proximity, NOT a recalled object cue |
| **MECH-307** | Anticipatory affect conjunction (signed surprise + schema + anticipatory liking + predicted-loc) | candidate_substrate_landed; v3_pending; 540g PASS | . | . | . | ~ | . | . | ~ | ~ | . | . | Anticipatory write substrate; not object-bound |
| **MECH-186/187/188** | 5-HT wanting floor / seeding gain / PFC top-down persistence | candidate; 186/188 conf 0.0, 187 conf 0.55 | . | . | . | . | . | Y | . | . | . | . | Maintenance only; explicitly NOT the binding gap (lit D2) |
| **SD-049** | Multi-resource heterogeneity; goal-identity vocabulary | candidate; v3_pending; Phase 2 blocked (GAP-2) | . | . | Y | ~ | ~ | . | . | . | . | ~ | Provides identity *substrate* (per-type tags) but binding to wanting unproven; 514k weakens |
| **ARC-030** | BG approach-avoidance symmetry (Go+NoGo) | candidate; held under SD-012 | . | . | . | . | . | . | . | ~ | Y | . | L8 selection; goal-conditioning untested |
| **ARC-036** | Multidimensional valence map | candidate | . | . | . | ~ | . | . | . | ~ | . | ~ | valence channels exist; identity dim absent |
| **ARC-051** | Multi-level wanting hierarchy (contact+schema+replay) | candidate | . | . | . | ~ | . | ~ | ~ | . | . | . | hierarchy of wanting; no object binding |

### Coverage summary by link

- **Well covered:** L0 (SD-012/MECH-306), L1 (MECH-112/230), L5 (MECH-116/186-188/ARC-032).
- **Partial / present-but-starved:** L6 (MECH-295), L7 (MECH-295/307; dACC does not read
  z_goal directly), L8 (MECH-229/ARC-030).
- **NOT covered (the holes):** **L2 object-identity binding** and **L3 incentive/wanted
  token**. **L4** is only adjacently covered (SD-015 z_resource is the closest, but z_goal is
  still seeded from raw z_world unless the encoder path is on, and even then no binding step).
- **L9 (dissociation) is claimed but contradicted by the only non-degenerate test (514k).**

### Too broad / too narrow / stale / missing-bridge flags

- **MECH-117 (`stable`) is the most urgent governance flag.** Its "stable" status rests on
  074d/e (C1 confounded) plus z_world-fallback evidence; the one non-degenerate identity
  probe (514k) returned dissoc fraction 0.0 and is `weakens`/`non_contributory`. A "stable"
  dissociation claim with a failing non-degenerate retest is a candidate for demotion review
  or at minimum a `pending_retest_after_substrate` re-flag. **Do not silently normalise.**
- **MECH-229 evidence is degenerate** (z_world fallback seeding, per SD-049 failure record).
  Its provisional status is appropriate; the non-degenerate retest is exactly GAP-2/514-successor.
- **SD-012 multiplier is mis-located** (lit A4/E5): correct, but applied to the seeding gate
  rather than to a cue-recalled object value. This is a *refinement* target, not a falsification.
- **Missing bridge claims:** there is no claim asserting that benefit must *bind to object
  identity* (L2), nor that a *wanted-object token* with its own dynamics exists (L3), nor that
  z_goal is *written from* an object/affordance pointer (L4 explicit). These are the bridge
  claims the chain needs.

---

## Part 2: proposed missing claims (CANDIDATES -- not ratified)

Each proposal includes: statement, link, lit anchors, the experiment that would support it,
the falsifier, and the dependency on existing claims. **None may be marked supported without
a direct test.** Naming uses PROP-* placeholders; governance assigns MECH-/SD-/ARC- IDs.

### PROP-BIND-obj (MECH-class) -- object-bound benefit binding (L2)
- **Statement:** "Benefit pulses must bind to resource/cue *identity* rather than only to
  undifferentiated z_world state; the binding produces a per-identity association that
  persists beyond the contact step."
- **Lit anchors:** Berridge&Robinson 1998 (A1); Flagel 2011 (A5, sign- vs goal-tracking);
  Cardinal/Everitt 2002 (B1, BLA identity binding); Diuk 2008 (E3).
- **Supporting test:** Stage 1 -- single resource identity, forced benefit; verify an
  object-keyed record is written and is retrievable after the agent leaves the cell.
- **Falsifier:** with two distinct resource identities, the bound records are
  indistinguishable (no identity information recoverable) -> claim fails; benefit binds to
  location only.
- **Depends on:** SD-049 (identity substrate), SD-015 (z_resource).

### PROP-INCENT-token (MECH-class) -- incentive-salience / wanted-object token (L3)
- **Statement:** "A liked-object identity can acquire a persistent, drive-revaluable
  incentive-salience amplitude (a wanted-object token) that is dissociable from immediate
  hedonic impact."
- **Lit anchors:** Robinson&Berridge 1993 (A2, sensitization/persistence); Zhang et al. 2009
  (A4, V = r * kappa(drive) at recall); Dayan&Berridge 2014 (E5, model-based revaluation).
- **Supporting test:** Stage 2 -- after one benefit encounter, present cue with NO benefit;
  verify wanting amplitude rises (driven by stored token * current drive) while liking does not.
- **Falsifier:** wanting amplitude is zero or equals the liking pulse on cue re-presentation
  (no independent token) -> claim fails.
- **Depends on:** PROP-BIND-obj, SD-012/MECH-306 (drive multiplier relocated to recall).

### PROP-CUEWANT (MECH-class) -- cue-to-wanting bridge with identity selectivity (L6/L9)
- **Statement:** "Recognised cues for previously beneficial resources can trigger wanting
  *for the identity-matched resource* before consumption (specific-PIT-like selectivity)."
- **Lit anchors:** Corbit&Balleine 2005/2011 (B2, specific PIT depends on BLA); Berridge et
  al. 2009 (A3, cue-triggered wanting); Schultz 1998 (D1, signal transfer to cue).
- **Supporting test:** Stage 2/4 -- cue for resource X raises approach to X, not Y
  (dissoc fraction > 0 with identity-matched selectivity).
- **Falsifier:** cue raises approach equally to all resources (general only, no specific PIT)
  -> downgrade to a general-arousal claim (CeA-like), not identity-matched wanting.
- **Depends on:** PROP-INCENT-token, MECH-295.

### PROP-GOALPTR (amend MECH-230 / SD-015) -- z_goal from object/affordance pointer (L4)
- **Statement:** "z_goal should be written from an object/cue/outcome pointer (or affordance
  embedding) -- the wanted-object token -- not only from raw current z_world at contact."
- **Lit anchors:** Schoenbaum 2009 (B3, OFC outcome identity); Wilson/Niv 2014 (B4, cognitive
  map); Dayan 1993 / Barreto 2017 (E1, what/where factorization); Khetarpal 2020 (E4).
- **Supporting test:** Stage 1 -- z_goal direction tracks the object token / z_resource, is
  stable across locations, and is invariant to the agent's position at contact.
- **Falsifier:** z_goal written from the token performs no better than (and is
  indistinguishable from) z_world-at-contact on identity-recovery and dissociation -> the
  pointer adds nothing; keep the simpler z_world seeding.
- **Note:** framed as an AMENDMENT to MECH-230 (and a use-case for SD-015), not necessarily a
  brand-new claim. Governance decides amend-vs-new.

### PROP-CONSUME (MECH-class) -- consumer readout is non-zero & behaviourally consequential (L7)
- **Statement:** "dACC / E3 / commitment consumers must receive a non-zero, behaviourally
  consequential wanting/goal signal; a non-trivial z_goal that does not change behaviour is a
  wiring failure, not a substrate result."
- **Lit anchors:** Balleine&O'Doherty 2010 (C2, goal-directed corticostriatal control);
  Miller&Cohen 2001 (C1, PFC bias). Positive control: V3-EXQ-623 (signal->behaviour works).
- **Supporting test:** Stage 3 -- with consumer enabled vs ablated under matched non-zero
  z_goal, behaviour differs (approach selectivity / commitment).
- **Falsifier:** non-zero z_goal with consumer enabled produces no behavioural delta vs
  ablated -> the consumer is not reading z_goal; route to consumer-wiring autopsy (this is the
  626 interpretation-grid row "non-trivial z_goal does not reach dACC").
- **Depends on:** L1 (clean positive control), dACC/E3 wiring.
- **Note:** the wiring map shows dACC does NOT currently read z_goal directly (it reads harm
  PE + payoff/effort + drive). This claim makes that an explicit, testable target.

### PROP-POSCTRL (diagnostic-support; SD/INV-class) -- minimal positive-control seeding (L1)
- **Statement:** "A forced benefit + known object-identity pulse must seed a non-zero,
  direction-stable z_goal under protected conditions before any ecological test of the goal
  stream is interpretable."
- **Lit anchors:** methodological (positive-control discipline); biology-neutral.
- **Supporting test:** Stage 0 unit test -- forced inputs to `GoalState.update`, assert
  z_goal norm crosses threshold and direction is stable. **Requires no new substrate code.**
- **Falsifier:** forced ideal inputs still yield z_goal ~ 0 -> the substrate gate itself is
  broken (would be a genuine substrate regression -- but 622 S0 + 582a say it is not).
- **Note:** this is a *gating/diagnostic* claim. It primarily prevents the Class-1 harness
  error (626) from being read as a Class-2 substrate result.

---

## Part 3: governance routing summary

| Item | Action proposed (governance owner decides) |
|---|---|
| MECH-117 | Re-examine `stable` status vs 514k dissoc=0.0; consider `pending_retest_after_substrate` re-flag. **Flag, do not auto-change.** |
| MECH-229 | Keep provisional; non-degenerate retest = 514-successor under object-bound substrate + SP-CEM. |
| MECH-230 / SD-015 | Candidate amendment PROP-GOALPTR (z_goal write-source). |
| SD-012 / MECH-306 | Note multiplier relocation option (cue-recall) per lit A4; refinement, not falsification. |
| New candidates | PROP-BIND-obj, PROP-INCENT-token, PROP-CUEWANT, PROP-CONSUME, PROP-POSCTRL -- register ONLY after Stage 0-2 produce evidence; until then they live here as proposals. |
| 625 headline/acceptance conflict | Separate governance flag (harm-axis consumer-input zero); cross-ref failure autopsy. |

**Hard rule honoured:** no proposal is registered or marked supported in this session. The
diagnostic ladder (separate doc) is what would generate the evidence; claim registration is a
later governance step gated on that evidence.
