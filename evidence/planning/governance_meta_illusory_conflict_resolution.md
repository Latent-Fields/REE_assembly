# Governance Meta-Note: Illusory Conflict Resolution Risk

Created: 2026-04-06
Status: active methodology caveat

## The Pattern

When experiments FAIL due to substrate limitation (z_goal not seeded, proxy offline phases, missing
wiring), governance reclassifies them as `non_contributory` — correctly removing them from
confidence and conflict scoring. But this creates a systematic bias:

1. **Removing "weakens" entries improves the conflict ratio** — making it appear that the claim's
   evidence is resolving toward support, when actually we just stopped counting the failures.

2. **The remaining "supports" entries were generated on the same incomplete substrate.** They survive
   not because they represent strong evidence but because they tested a narrow pathway that happened
   to work (e.g., wanting/liking circuit) while the broader claim remains untested.

3. **The claim appears to be progressing toward promotion** when in fact its evidence base is
   narrower than the numbers suggest.

## Affected Claims (as of 2026-04-06)

### MECH-112 (goal latent representation)
- **Supports**: EXQ-074f PASS, EXQ-234 PASS (wanting/liking circuit only)
- **Removed weakens**: EXQ-235 (non-contributory, z_goal alignment failure)
- **Risk**: Wanting/liking tests a specific z_goal pathway (incentive salience). MECH-112 claims
  E3 requires a *structured* goal latent for flexible goal-directed behavior. The broader claim
  is untested. When z_goal seeding works generally (post SD-012/SD-015), the broader claim may
  still fail.
- **Status**: pending_retest_after_substrate

### ARC-030 (Go/NoGo sub-channel symmetry)
- **Supports**: from specialized selector experiments
- **Removed weakens**: EXQ-235 (non-contributory), EXQ-086 (measurement bug)
- **Risk**: Go/NoGo symmetry untested with real z_goal. The approach sub-channel can't be
  evaluated when the goal signal that drives approach behavior is absent.
- **Status**: pending_retest_after_substrate

### ARC-032 (theta-rate E1->E3 pathway)
- **Supports**: none genuine (all from proxy measurements)
- **Removed weakens**: EXQ-228, EXQ-228a (both non-contributory, z_goal precondition failure)
- **Risk**: Zero genuine evidence in either direction. The conflict ratio is undefined, not
  resolved. Any promotion signal is illusory.
- **Status**: pending_retest_after_substrate

### SD-011 (dual nociceptive streams)
- **All experimental evidence is diagnostic**: EXQ-241 (morning + afternoon), EXQ-178/178a/178b
- **Risk**: Affective stream shows R^2 > sensory in all seeds (D3 reversal). This isn't just
  "untested" — it's an active signal that the current AffectiveHarmEncoder is a monotone
  transform of the sensory stream, not a genuinely distinct pathway. The wiring needs a second
  source (context, history, residue field) that sensory cannot access.
- **Status**: pending_retest_after_substrate (EXQ-247 is the gate)

### SD-012 (homeostatic drive)
- **All experimental evidence is diagnostic/non-contributory**: EXQ-085 series, EXQ-233, EXQ-238
- **Risk**: Drive-level extraction has never produced z_goal_norm > 0.1 in any experiment.
  Evidence is entirely negative but classified as substrate limitation.
- **Status**: pending_retest_after_substrate (EXQ-247 is the gate)

### MECH-153 (supervised context labeling)
- **Weakens**: EXQ-239 (does_not_support, with substrate caveat)
- **Risk**: The "weakens" classification is genuine but substrate-confounded. cosine_sim=1.0 in
  both supervised and ablated conditions means the context_memory infrastructure is too immature
  for either pathway. A deeper analysis of the attribution pipeline's expected mathematical
  functions is needed to design a test that can actually distinguish supervised from unsupervised
  differentiation.
- **Status**: needs_redesign (pipeline mathematical analysis first)

### MECH-163 (dual goal-directed systems)
- **Removed weakens**: EXQ-237a (non-contributory, z_goal substrate limitation)
- **Risk**: Even the habit condition showed zero lift in simple tasks. This suggests the test
  paradigm itself may be flawed — habit formation isn't observable in the current task design.
  Superseding experiment needs a task where habit IS the correct strategy before testing
  planned-system added value.
- **Status**: needs_redesign (task paradigm, not just substrate)

### MECH-165 (offline replay diversity)
- **Weakens**: EXQ-244 (evidence, held at candidate)
- **Risk**: Replay can't increase entropy without alternative strategies as source material. The
  experiment tested replay in isolation when the mechanism requires exploration-generated
  candidates to replay diversely. The "weakens" may be a test design issue, not a claim issue.
- **Status**: needs_redesign (pair replay with exploration mechanism)

## Governance Methodology Implications

### 1. Non-contributory != nothing learned
Every non-contributory experiment should generate one of:
- A **prerequisite gate** (which substrate piece must work first)
- A **redesign specification** (what the superseding experiment needs)
- A **design signal** (what the failure reveals about architecture)

### 2. Conflict ratio after reclassification needs a health warning
When `hold_candidate_resolve_conflict` status was reached before reclassifications, and the
reclassifications removed weakens entries, the claim should be flagged `pending_retest_after_substrate`
rather than treated as trending toward resolution.

### 3. "Supports" evidence needs substrate-adequacy tagging
Evidence entries should note which substrate features were present when the experiment ran. A
"supports" from a substrate missing z_goal, SD-011, or SD-017 tells you less than a "supports"
from a substrate with all dependencies resolved. The governance algorithm doesn't currently
distinguish these.

### 4. Practical criterion: EXQ-247 as the gate
If EXQ-247 (SD-011/SD-012 integration) PASSes and z_goal_norm rises above 0.1, then:
- Re-queue EXQ-228a (ARC-032), EXQ-235 (ARC-030/MECH-112), EXQ-237a (MECH-163) unchanged
- Their results become genuine evidence rather than substrate artifacts
- The conflict ratios become real

If EXQ-247 FAILs, the z_goal substrate needs fundamental redesign and all claims depending on
z_goal remain in governance limbo.

## Action Items
- Add `pending_retest_after_substrate` evidence_quality_note to affected claims
- Track EXQ-247 as the gate for the next wave of genuine evidence
- Create superseding experiment proposals for MECH-153, MECH-163, MECH-165 (needs_redesign)
- Consider adding substrate-adequacy tags to the evidence indexer (future governance improvement)
