# Claim synthesis — MECH-457 ↔ MECH-471 ↔ Q-089

**Date:** 2026-08-07T21:43Z
**Skill:** `/claim-synthesis` (proposal-first; nothing registered — see §0)
**Trigger:** `failure_autopsy_V3-EXQ-890_2026-08-07.json` routing line — *"claim-synthesis
(examine MECH-457<->MECH-471<->Q-089 mechanism cross-reference; substrate_queue.json has no
entry unblocking MECH-471, and MECH-457's own bottleneck is blocked_pending_discrimination —
implement-substrate would be premature)"*.
**Chip:** `chip-20260807-mech457-471-q089-claim-synthesis`.
**Sibling input read:** `competence_floor_instrument_audit_2026-08-07.md`
(`chip-20260807-competence-floor-instrument-audit`, landed 21:40Z) — the measurement-frame
audit of MECH-457's own competence-floor campaign. Its findings are load-bearing for §6.

---

## 0. What this document is, and is not

This is a **relationship-and-priority synthesis**, not a decomposition. The `/claim-synthesis`
discrimination gate (§3) **STOPs before proposing any new child claim** — the cluster is not
granularity debt. **Nothing was written to `claims.yaml` or `hypothesis_space_registry.v1.json`.**
Reasons, so governance can override cheaply:

- The skill is explicitly *"Proposal-first, governance-touching. Nothing lands in `claims.yaml`
  without the user's explicit per-child approval. Not safe headless."* This ran headless.
- `docs/claims/claims.yaml` is under an **active, non-stale TASK_CLAIMS claim** by
  `igw-auto-igw-208-substrate-ready-sd014-decouple-w` (opened 2026-08-07T20:16:02Z). Editing it
  would race that session.
- The two structural corrections this synthesis recommends (§5: a `depends_on` edge; §6: a
  readiness-vocabulary reclassification) are governance's call under `/governance` Step 2b/4,
  exactly as the sibling instrument audit deferred its own registry edits.

Every recommendation below is **copy-paste ready for governance** and **promotes/demotes nothing**.

---

## 1. The three claims, restated at their true level in the stack

The autopsy asks whether these three describe **one** mechanism gap, **separate** claims sharing
symptoms, or a **dependency chain**. The answer is legible only once each is placed at its actual
level — they are *not* peers.

| claim | kind | what it is *about* | level |
|---|---|---|---|
| **MECH-457** | `mechanism_hypothesis` | the ACQUISITION machinery — a dedicated RPE-driven actor-critic converter that turns exploration into a competent policy | **mechanism of acquisition** |
| **Q-089** | `open_question` | a candidate EXPLANATION for *why* acquisition is unreliable seed-to-seed (epistemic-deficit accumulator MECH-482 + orient/survey regime MECH-483) | **candidate axis under the acquisition-reliability question** |
| **MECH-471** | `mechanism_hypothesis` | the UPDATE DISCIPLINE competence edits should carry once acquired (bounded / provenanced / rollback-capable, by generalisation from consolidation's MECH-392/INV-080/MECH-401) | **hygiene of updates, downstream of acquisition** |

The single fact that organises all three: **the `mech471_competence_acquisition_reliability`
hypothesis-space question** (registered 2026-08-05, `hypothesis_space_registry.v1.json:3279`).
V3-EXQ-875/875a/882a/890 all fail *at the acquisition precondition* — only ~12.5% of seeds
(2/16) cross the baseline competence floor at all — so none of them ever reaches the falsifier of
the claim they are tagged to. That question is the hinge the three claims turn on, and each sits
at a different point around it.

---

## 2. The cluster's failure record (what actually failed, and where)

| run | tag | outcome / class | where it failed |
|---|---|---|---|
| V3-EXQ-875 | MECH-471 | FAIL, `precondition_unmet` | SD-070 defect — `zworld_p0_episodes` omitted at all 3 call sites; z_world a frozen random projection |
| V3-EXQ-875a | MECH-471 | FAIL, `competence_implementation_gap`, `evidence_direction: unknown` | SD-070 fixed; ~12.5% seed clear-rate — an **acquisition-reliability characterization gap**, *not a verdict on MECH-471* |
| V3-EXQ-882a | MECH-472 (→MECH-471 dep) | FAIL, `non_degenerate: false` per its own guard | acquisition floor unmet on 6/8 seeds even at 10× budget; the held-out gap never became reachable |
| V3-EXQ-890 | MECH-471 (diagnostic) | CHARACTERIZES, `non_contributory` | H2 (hazard-layout difficulty) ELIMINATED; H1 (exploration-init variance) CONFIRMED necessary-not-sufficient; H3 (bias-head/OFC) open/exploratory |

**Every FAIL is upstream of MECH-471's own falsifier.** MECH-471's falsifier is a *local-update
interference test* — train a targeted competence, measure degradation of unrelated **already-acquired**
competences. Its own non-degeneracy guard requires the unrelated competences to be *demonstrably
acquired* ("above-floor performance with live cross-seed variance"). With a 12.5% acquisition
clear-rate there is nothing to interfere *with*. **MECH-471 has never been tested. It has been
blocked at the door.**

---

## 3. Discrimination gate → STOP (this is not granularity debt)

Applying the Step-3 classification to the cluster:

- V3-EXQ-875: `precondition_unmet` (SD-070) → **EXCLUDE** (substrate-not-ready).
- V3-EXQ-882a: `non_degenerate: false` per the claim's own pre-registered guard → **EXCLUDE**
  (test-design / precondition debt — the decisive comparison was never reachable).
- V3-EXQ-875a: `competence_implementation_gap`, `evidence_direction: unknown` → a **precondition/
  characterization gap**, not a genuine substrate-ready falsification of MECH-471.
- V3-EXQ-890: diagnostic, `non_contributory`, CHARACTERIZES — resolves two legs of the *acquisition-
  reliability* question, but tests **nothing** about MECH-471's update-discipline falsifier.

There are **zero distinct, genuine, non-degenerate, substrate-ready FAIL signatures circling
MECH-471's own assertion.** The residue that Step 3 requires (≥2 such signatures) is empty. The
cluster is **precondition/substrate-not-ready debt**, and it is furthermore **already metabolized**
(the exclude-guard from Step 1 fires on multiple signals):

- a registered hypothesis-space question owns it (`mech471_competence_acquisition_reliability`,
  3 legs, 1 confirmed + 1 eliminated + 1 alive);
- MECH-457 already carries two registered children from the 2026-07-22 decomposition — **MECH-475**
  (`baseline_informativeness` — uninformative value baseline makes optimisation iatrogenic) and
  **MECH-476** (`acquisition_retention_dissociation`);
- Q-089 is itself a freshly-registered candidate axis (2026-08-05) for the same phenomenon.

**Verdict: STOP. Do not decompose. No new child claim is warranted.** Forcing a decomposition here
would manufacture untested claims out of an acquisition-floor blocker — exactly the anti-proliferation
failure the gate exists to prevent. This is the *expected* PASS outcome for a cluster whose reactive
discipline (a live hypothesis-space question + prior decomposition) already owns it.

---

## 4. The relationship, in one picture

```
                    mech471_competence_acquisition_reliability   ← the hinge question
                    (why do only ~12.5% of seeds cross the floor?)
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        │                           │                           │
   MECH-457                    candidate axes                MECH-471
   the ACQUISITION            (explanations for the         the UPDATE DISCIPLINE
   mechanism itself           split)                        (rollback/provenance/bound)
   — the competence           ├─ H-exploration-init  CONFIRMED (nec-not-suff)
   FLOOR / conversion         ├─ H-hazard-layout     ELIMINATED
   ceiling; BC is the         ├─ H-bias-head/OFC     alive (exploratory)
   only floor-clearing        └─ Q-089 (epistemic-   NOT YET a registered leg;
   existence proof               deficit / orient-      gated on MECH-482/483 substrate
                                  survey)
        │                                                       │
   FACET of the hinge         Q-089 is a candidate ANSWER   DOWNSTREAM of the hinge:
   (same failure family)      to the hinge question         its falsifier is UNTESTABLE
                                                             until the floor is crossed
```

**Answer to the autopsy's three-way question:**

1. **MECH-457 and the acquisition-reliability phenomenon are facets of ONE gap.** The autopsy says
   so directly: V3-EXQ-890's H1 mechanism — *"early, unrecoverable exploration failure in a
   REINFORCE-bias-head readout"* — *"plausibly belongs to the same failure family as MECH-457's
   already-established substrate-ceiling finding."* MECH-457's campaign already established that BC
   (imitation) is the **only** floor-clearing existence proof and that the RL converter cannot
   bootstrap a competent policy from a *provably sufficient* observation, invariant to capacity,
   drive-schedule, reward-coupling and credit-horizon (4 axes eliminated). The ~12.5% seed clear-rate
   observed on MECH-471's driver is the **same competence floor, measured on a different driver**.
   The hinge question is genuinely a *MECH-457-domain* question wearing a MECH-471 label (§5b).

2. **Q-089 is a candidate axis under that hinge question**, at the same level as MECH-457's
   eliminated axes — its own notes say exactly this (*"a NEW candidate axis, not a re-litigation of
   the eliminated ones"*). Its `depends_on: MECH-457` (conceptual match) and
   `related_claims: MECH-471/472` (literal citation) wiring is **already correct** and is the most
   accurately-wired of the three claims. It proposes that the confirmed-but-unexplained
   H-exploration-init-variance is really epistemic-deficit-driven orient/survey timing.

3. **MECH-471 is a genuinely SEPARATE claim, one layer up, that is BLOCKED BY the hinge.** It is not
   a facet of the acquisition mechanism — it asserts an *update-hygiene asymmetry* (competence edits
   lack the rollback/provenance discipline consolidation already has). That is a real, distinct,
   non-duplicative claim. But it is **strictly downstream of acquisition**: you cannot test whether
   competence updates interfere destructively until competence can be reliably acquired.

So: **not one claim, not three unrelated claims — a dependency chain around a shared hinge.** One
facet (MECH-457), one candidate explanation (Q-089), one downstream-and-blocked claim (MECH-471).

---

## 5. Wiring corrections (proposal-only; governance's call)

### 5a. MECH-471 is missing its real blocker in `depends_on` — the one load-bearing edit

MECH-471 `depends_on: [MECH-392, INV-080, MECH-401, MECH-083, MECH-261, ARC-092]` — the
consolidation-discipline analogs it *generalises from*. It does **not** depend on MECH-457 or on the
acquisition-reliability question, **even though its falsifier is untestable until the competence
floor is crossed**. This is the graph's one substantive error: the empirically-demonstrated blocker
(875/875a/882a/890 all die at acquisition) is invisible in the dependency structure.

**Recommended (governance to apply under an active claims.yaml claim):** add to MECH-471 `depends_on`

```yaml
    - MECH-457   # ACQUISITION-FLOOR GATE (added 2026-08-07 /claim-synthesis, claim_synthesis_MECH-457-MECH-471-Q-089_2026-08-07.md §5a):
                 # MECH-471's local-update-interference falsifier requires DEMONSTRABLY-ACQUIRED unrelated
                 # competences (its own non-degeneracy guard). V3-EXQ-875a/882a/890 show acquisition clears
                 # only ~12.5% of seeds -- MECH-457's competence-floor / conversion-ceiling bottleneck --
                 # so MECH-471 is not testable until MECH-457's acquisition floor is crossed reliably.
                 # This is a TESTABILITY gate, not a mechanism dependency; PROMOTES/DEMOTES NOTHING.
```

This makes the chain the autopsy identified legible in the registry and stops a future session
re-deriving "MECH-471 is testable now" from its (stale) notes (§6).

### 5b. The hinge question is claim-keyed to MECH-471 but studies MECH-457's phenomenon

`mech471_competence_acquisition_reliability` has `claims: ["MECH-471"]`, yet its title — *"Why does
survival-competence ACQUISITION succeed reliably for some seeds and fail near-baseline for others"* —
is a MECH-457 competence-floor / cold-start question. Q-089's own notes already flag this
attribution ambiguity (*"depends_on wires the conceptual match MECH-457; related_claims records the
literal citation MECH-471/472"*). The runs landed on MECH-471's driver because MECH-471 was the
*next* thing being tested, not because the phenomenon is MECH-471's.

**Recommended (soft, non-blocking):** widen the question's `claims` to `["MECH-471", "MECH-457"]`
(or add MECH-457 as the primary and MECH-471 as the *gated-by* claim). This is a bookkeeping
correction that makes the hinge findable from MECH-457, where it conceptually lives. Not urgent;
stated so a later reader is not misled by the label.

### 5c. Q-089's axis is not yet a registered leg of the hinge question

Q-089 proposes epistemic-deficit/orient-survey as an explanation for the CONFIRMED-but-unexplained
H-exploration-init-variance. That axis is **not** among the question's three registered legs. It
should become a **pre-registered `alive` leg** (`H-epistemic-deficit-orienting`, `axis: exploration/
drive`) **only when MECH-482/MECH-483 substrate exists** — Q-089 is `substrate_conditional`,
`v3_pending`, and explicitly *"gated on MECH-482/MECH-483 existing; not V3-tractable as stated."*
Registering the leg now would be a standing invitation to spawn a probe against absent substrate.
Record it as a *deferred* candidate leg; do not pre-register it live yet.

---

## 6. The autopsy's actual question — does this change substrate priority for MECH-471?

**No. A substrate build for MECH-471 remains PREMATURE, and this synthesis sharpens *why*.**

The autopsy asked whether the cross-reference changes what to build. Three convergent reasons say
*build nothing for MECH-471 yet*:

**(i) MECH-471 is `complex (probe-gated)`, not `complicated (buildable)` — its own notes are stale.**
MECH-471's `notes` assert *"TESTABLE NOW on existing substrate; complicated (buildable). This is the
cheapest real probe in cluster E and the right first move."* That was written 2026-07-22, **before**
V3-EXQ-875/875a/882a/890 demonstrated the acquisition floor blocks it. The empirical record now
contradicts the readiness label: MECH-471 sits behind the `complex (probe-gated)` acquisition-floor
node (is the split epistemic-deficit timing (Q-089), or the eliminated axes, or a measurement
artifact (iii)?), which is itself `blocked_pending_discrimination`. Building rollback/provenance
discipline now would be building update-hygiene for competences the agent **cannot reliably acquire**
— untestable by MECH-471's own non-degeneracy guard. **Recommended:** governance amend MECH-471's
notes to reclassify it `complex (probe-gated)` behind the acquisition floor, superseding the
"complicated (buildable) / testable now" line.

**(ii) MECH-457's frontier is itself contaminated — the discrimination MECH-471 waits behind is not
clean.** MECH-457's `blocked_pending_discrimination` bottleneck is H-bc-prior vs H-approach-primitive.
The sibling instrument audit (§4–§5e) shows that discrimination rests on a **misread instrument**:
H-approach-primitive's load-bearing "approach-without-consummation" finding is contradicted by an
env-observable directed-approach statistic in the same manifest (it is **proximity-camping** — a
Goodhart of the shaping term — not a consummation deficit), and H-bc-prior child 3's entire basis is
a single contaminated frozen-random-projection arm that the audit recommends **voiding**. So MECH-471
is gated on a MECH-457 discrimination that must first be re-posed. Building MECH-471 substrate ahead
of that would double down on an unresolved upstream artifact.

**(iii) Part of the "acquisition unreliability" may be the same composite-DV artifact the instrument
audit indicts.** V3-EXQ-890 itself noted the fixed-threshold official split (2-vs-14) undercounts a
cleaner natural 5-vs-11 cluster. The instrument audit shows the DV `foraging_competence` multiplies
foraging *rate* by episode *duration*, and that survival_horizon is **bimodal** on D3 (camp-and-live
vs forage-and-die). A seed scored "did not acquire" on the composite DV may be camping alive at a low
per-episode count — a strategy split, not an acquisition failure. **Before** anyone builds MECH-471
discipline *or* concludes acquisition is fundamentally unreliable, the DV should be re-posed (report
foraging *rate* alongside per-episode count; treat survival as a covariate) per the instrument audit's
recommendation 3. The acquisition-reliability phenomenon and MECH-457's floor may both be *partly*
measurement-frame artifacts.

**Net priority ordering (proposal):**

1. **Land the instrument audit's cheap fixes first** (void H-bc-prior child 3; the one-line
   `make_probe_fn` sub-skill-series fix; re-pose the DV to rate + duration). These are pre-requisite
   to *interpreting* both the MECH-457 frontier and the acquisition-reliability split.
2. **Resolve MECH-457's H-bc-prior vs H-approach-primitive discrimination on the re-posed DV** — the
   competence floor is MECH-471's gate.
3. **If MECH-482/MECH-483 substrate is built** (Q-089's precondition), register Q-089's axis as a
   live leg and test whether epistemic-deficit/orient-survey timing explains H-exploration-init-variance.
4. **Only then** is MECH-471's local-update-interference falsifier reachable — the agent can reliably
   acquire, so unrelated acquired competences exist to interfere-test against.

MECH-471 is item 4, gated behind three upstream nodes. **`recommended_substrate_queue_entry: none`
for MECH-471 stands, and the autopsy's read that a build would be premature is confirmed and
strengthened.**

---

## 7. Summary of recommendations (all proposal-only, promote/demote nothing)

| # | recommendation | who applies | urgency |
|---|---|---|---|
| R1 | **Do NOT decompose** — cluster is precondition/already-metabolized debt, not granularity debt (§3) | — (this synthesis) | done |
| R2 | Add `MECH-457` to MECH-471 `depends_on` as a **testability gate** (§5a) | `/governance` (claims.yaml under claim) | **load-bearing** |
| R3 | Reclassify MECH-471 `complicated (buildable)` → **`complex (probe-gated)`** behind the acquisition floor; supersede the stale "testable now" notes line (§6i) | `/governance` | high |
| R4 | Widen `mech471_competence_acquisition_reliability` question `claims` to include MECH-457 (§5b) | `/governance` / `/failure-autopsy` Step 9b | soft |
| R5 | Record Q-089's epistemic-deficit axis as a **deferred** candidate leg of the hinge question; do NOT pre-register live until MECH-482/483 substrate exists (§5c) | `/governance` | soft |
| R6 | Confirm MECH-471 substrate build stays **deferred/premature**; sequence behind instrument-audit fixes + MECH-457 discrimination (§6) | `/governance` Step 2b | confirm |

**Not proposed:** any new child claim; any merge or split of MECH-457/471/Q-089; any claims.yaml
edit by this session; any experiment queued.

---

## Provenance

- Inputs read in full: MECH-457 / MECH-471 / Q-089 entries in `docs/claims/claims.yaml`; MECH-472,
  MECH-475, MECH-476, MECH-482, MECH-483 entries (context); `failure_autopsy_V3-EXQ-890_2026-08-07.json`;
  `competence_floor_instrument_audit_2026-08-07.md` (sibling chip); the
  `mech471_competence_acquisition_reliability` block in `hypothesis_space_registry.v1.json:3279`.
- No experiment run, re-run, or queued. No substrate change. No compute.
- **Not written by this session:** `claims.yaml`, `hypothesis_space_registry.v1.json`, any manifest,
  `substrate_queue.json`, `review_tracker.json`. `docs/claims/claims.yaml` was under an active
  TASK_CLAIMS claim by `igw-auto-igw-208-substrate-ready-sd014-decouple-w` at the time; deliberately
  not touched.
- Chip: `chip-20260807-mech457-471-q089-claim-synthesis`.
