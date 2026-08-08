# SD-021 / SD-032c blocker framing vs MECH-439 — cross-reference review (staged)

**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml (or whichever registry).**

- **Date:** 2026-08-08
- **Session:** `metaworker-chip-20260808-sd021-sd032c-mech439-crossref` (headless, metaworker-dispatch)
- **Chip:** `chip-20260808-sd021-sd032c-mech439-crossref`
- **Base read:** `REE_assembly` `origin/master` as of 2026-08-08T14:45Z
- **Why staged rather than applied:** `task_claim.py check` returned **exit 3** on
  `REE_assembly/docs/claims/claims.yaml` — the active owner is
  `mech-322-evidence-confirm-bc9fbf` ("thought-digestion campaign 2026-08-08",
  `claimed_at` 2026-08-08T09:41:28Z... 10:45:54Z, **not stale**, actively landing waves;
  wave 14 committed as `2b351a6c6c`). That is the same campaign that spawned this chip.
  Per CLAUDE.md arbitration, a non-owner does not implement. The proposed wording below
  is written to be applied verbatim by that session or by a later `/governance` pass.

---

## 1. Answer in one line

**Recommendation (b), refined.** MECH-269-alone is stale framing for both claims and
should be cross-referenced — but the right co-blocker to name is **MECH-309**
(monomodal policy collapse), with **MECH-439** as its selection-face and current live
front; and a **materially newer confirmed finding (V3-EXQ-878, 2026-08-03) supersedes
both** for the near term on this specific pathway. Do **not** touch `depends_on`.

## 2. Corrections to the chip's stated premise

Two premises in the chip brief are now out of date against `origin/master`:

1. **"SD-021 and SD-032c's own blocker text does NOT mention MECH-439 at all."**
   True for SD-032c. **False for SD-021** — SD-021's `what_would_answer` (added by the
   wave-10 thought-digestion pass that authored this chip, on `origin/master` line 28788)
   already quotes SD-032b's note verbatim and states "A fresh substrate approach to
   MECH-269, **or resolution of the MECH-439 ceiling**, is required before this
   precondition can be considered live again." So the live asymmetry is narrower than the
   brief assumed: **SD-021 is already cross-referenced in `what_would_answer` but not in
   `evidence_quality_note`; SD-032c is cross-referenced nowhere.**

2. The brief frames this as MECH-269-vs-MECH-439. There is a **third and more recent**
   framing that neither claim reflects — see §5.

## 3. Is MECH-439 itself actionable? (chip question 3)

**No — it is contested and its own ceiling is declared exhausted.** From MECH-439's block:

- `status: candidate`, `ceiling_decision: exhausted`, `epistemic_category: standard`
  (GOV-CEIL-1 ceiling-exhaustion demotion 2026-07-09, demoted *from* `substrate_ceiling`).
- **11 confirmed `substrate_ceiling`/`non_contributory` failure autopsies**
  (689a / 700 / 700a-d / 709 / 710 / 711 / 713) with no positive discrimination on any
  richer substrate. The competing **NULL reading** (F-dominance is inert, doing no causal
  work) is now carried **co-equally**.
- `awaiting: ARC-107`; `assembly_status: in_progress` (MECH-448 built+promoted,
  MECH-449 built 2026-06-21); promotion in **either** direction re-gated on
  **V3-EXQ-689g**, still pending.

**Consequence for the edit decision:** relabelling SD-021/SD-032c's blocker
MECH-269 → MECH-439 does **not** create an actionable path. Its whole value is
**redirecting the watch-point from a dead route to a live one**: MECH-269's route has
been tested to exhaustion twice (V3-EXQ-325f reef/monostrategy fix; the MECH-295
goal_pipeline:GAP-4 Tier-1 cohort 490g–k, formally CLOSED 2026-06-09 *without* landing
V_s-driven behavioural divergence, and re-scoped rather than fixed), whereas MECH-439 has
a live front (ARC-107 / MECH-448+449 / V3-EXQ-689g). That redirect is worth the edit;
an implied promise of near-term unblocking is not, and the wording below says so
explicitly.

## 4. Does MECH-439 gate SD-021/SD-032c's *specific* mechanisms? (chip question 1)

**Partially — and strictly more weakly than it gates SD-032b.** This is the substantive
finding, and it is why a straight copy of SD-032b's framing would overstate the case.

| | SD-032b | SD-021 / SD-032c |
|---|---|---|
| Failing criterion | c2 = **committed-action-class entropy shift** | drive-regime divergence in `harm_s_gain` / `aic_salience` |
| Relation to MECH-439 | **Identical metric.** MECH-439 *is* the committed-action-class-entropy conversion ceiling. 445h measured `action_class_entropy = 0.0` in every arm including OFF. | **Upstream of it.** The observed failure was `DESCENDING == CONTROL` **bit-identical** — i.e. `harm_s_gain` itself never differed, because `operating_mode` never varied. That is a *policy-mode* degeneracy, not a *selection-conversion* one. |
| Transfer strength | Exact | By shared root only |

The shared root is the **monostrategy / monomodal-policy collapse**, which is separately
registered as **MECH-309** ("Monomodal policy collapse is the equilibrium of a
parametric-policy agent without a rule-apprehension layer"; `candidate`, `v3_pending`,
`live_status.reading: candidate/v3_pending/substrate_ceiling`). MECH-439's own
`depends_on` names MECH-309 with the comment *"monomodal-policy-collapse equilibrium
this names the selection-side mechanism of"*.

So the precise chain for SD-021/SD-032c is:

```
MECH-309 (monomodal policy collapse)  <- the actual degeneracy blocking these two
   └─ MECH-439 (F-dominance)          <- its selection-side mechanism + the live front
        └─ ARC-107 / MECH-448+449 / V3-EXQ-689g   <- where a resolution signal would appear
```

...whereas SD-032b sits directly on the MECH-439 node.

**House precedent for exactly this both-name wording already exists** — SD-029's
`epistemic_category_note` (set 2026-08-07, wave 10): *"...a shared downstream mechanism
(monostrategy / lack of behavioural diversity, rooted in MECH-439 F-dominance, ~88-89% of
E3's variance) absorbs the signal before it reaches the outcome metric... Held pending
MECH-269/MECH-269b V_s landing."* SD-029's `what_would_answer` uses the same "Deeper
shared root: MECH-439..." construction. The wording below mirrors it deliberately so the
registry stays internally consistent.

## 5. The finding that supersedes both framings for the near term

**`evidence/planning/failure_autopsy_V3-EXQ-878_2026-08-03.md` (CONFIRMED, routing
user-confirmed 2026-08-03) tested exactly this pathway and found a different blocker.**

Run `v3_exq_878_mech332_efference_aic_dissociation_20260803T023041Z_v3`, against MECH-332
(two dissociable z_harm_s attenuation pathways). The autopsy names its **Pathway 2** as
*"commitment-gated PAG/RVM descending suppression, **SD-021, now subsumed by SD-032c**"*,
substrate `ree_core/cingulate/aic_analog.py`. What it found:

- `n_committed_steps = 0` vs `N_COMMITTED_FLOOR = 8`, **all 3 seeds** — E3's commitment
  gate (MECH-090 BetaGate) never elevated during eval in either AIC-active arm. Pathway 2's
  claim-intrinsic trigger never fired, so it is **UNTESTED, not falsified**.
- **Dominant diagnosis: "environment/schedule calibration gap (test-design), *not a
  substrate gap*, not a claim-layer verdict."** Explicitly `non_contributory/standard`,
  **not** `substrate_ceiling` — MECH-090's commitment gate is well-supported elsewhere.
- Work-graph classification: `complex (probe-gated) / puzzle (known rules)`.
- Routing: **`/queue-experiment` V3-EXQ-878a** — a calibration pilot watching
  `n_committed_steps` as its own gate, *before* repeating the full 2x2 dissociation.
  Plus a measurement-hygiene fix: `z_harm_s_ratio`'s empty-data fallback should be
  `NaN`/`None`, not `1.0`, so a zero-commitment run can never silently launder into a
  false "no attenuation" reading. (**Note this bears directly on the 325a/325b
  bit-identical-`s_ratio=1.0000` history in SD-021's own record.**)
- That routing **was ratified by governance and applied** — MECH-332's
  `evidence_quality_note` carries the `[2026-08-03 governance, V3-EXQ-878, confirmed
  failure_autopsy...]` block. So this is not an unratified autopsy proposal.

**Gap found:** `V3-EXQ-878a` is **not in `ree-v3/experiment_queue.json`** as of
2026-08-08 (0 occurrences of "878" in the queue). The ratified routing has not been
executed. A chip has been spawned for it — see §8.

**Why this matters to the framing question:** SD-021/SD-032c's records currently imply
nothing can be learned until a substrate ceiling lifts. The 2026-08-03 confirmed autopsy
says the *proximal* blocker on this pathway is a **calibration puzzle with a known fix**,
which is a materially cheaper and more actionable gate than either MECH-269 or MECH-439.
Both framings should coexist: calibration (proximal, live, queueable) and
MECH-309/MECH-439 (deeper, still standing behind the drive-regime-divergence half of the
test).

## 6. Recommendation on `depends_on` (chip question 4)

**Do NOT add MECH-439 (or MECH-309, or MECH-269) to either claim's `depends_on`.**

In this registry `depends_on` encodes **architectural** dependency — what the claim's
design rests on — not "what is currently blocking evidence". Evidence:

- SD-021 `depends_on: [SD-011, SD-020, ARC-016, MECH-090]` — **MECH-269 is not there**,
  despite having been SD-021's named blocker since 2026-04-22.
- SD-032c `depends_on: [SD-032, SD-032a, SD-012, SD-021, MECH-091, MECH-259]` — all
  architectural; likewise no MECH-269.
- Blocker framing consistently lives in `evidence_quality_note` / `what_would_answer` /
  `ceiling_routing_note` (SD-032b's cross-reference is in a `ceiling_routing_note`, not
  `depends_on`).

Adding it would be a category error and would ripple into the dependency-graph tooling
and auto-join audits. **Notes only.**

Likewise **do not change** `status`, `v3_pending`, `epistemic_category`, or
`live_status` on either claim — those are governance dispositions, out of scope for a
cross-reference correction.

---

## 7. Proposed wording (apply verbatim)

### 7a. SD-021 — append to `evidence_quality_note`

> BLOCKER FRAMING CROSS-REFERENCE [2026-08-08]: the MECH-269 V_s-landing
> hold recorded above (2026-04-22) is stale as the sole named blocker.
> Two corrections, neither of which changes this claim's status or
> v3_pending. (1) DEEPER SHARED ROOT: the "V_s-monostrategy-locked"
> degeneracy is the monomodal-policy collapse registered as MECH-309, whose
> selection-side mechanism is MECH-439 (F-dominance, ~88-89% of E3
> committed-selection variance). The sibling SD-032b ceiling_routing_note
> (2026-06-19) records MECH-269 as "wired_but_inert... SUPERSEDED as the
> operative blocker by the F-dominance conversion ceiling"; that supersession
> applies here too, but MORE WEAKLY than to SD-032b -- SD-032b's failing c2
> criterion IS committed-action-class entropy (MECH-439's own metric), whereas
> this claim's failure mode was DESCENDING==CONTROL bit-identical, i.e.
> harm_s_gain never varied because operating_mode never varied, which is
> upstream of the selection stage. MECH-439 is itself a CONTESTED candidate
> (GOV-CEIL-1 ceiling-exhaustion demotion 2026-07-09; 11 confirmed
> substrate_ceiling autopsies; null reading carried co-equally; awaiting
> ARC-107 / V3-EXQ-689g), so this is a redirect of the watch-point from a dead
> route to a live one, NOT an unblocking. (2) MORE PROXIMAL, NEWER BLOCKER:
> the confirmed failure_autopsy_V3-EXQ-878_2026-08-03 tested this exact
> pathway (its "Pathway 2 -- SD-021, now subsumed by SD-032c") and found
> n_committed_steps=0 vs floor=8 across all 3 seeds -- E3's commitment gate
> (MECH-090 BetaGate) never elevated in that arena/schedule, so the pathway is
> UNTESTED, not falsified. Dominant diagnosis: environment/schedule
> calibration gap (test-design), explicitly NOT a substrate gap and NOT
> substrate_ceiling; work-graph class complex (probe-gated) / puzzle (known
> rules). Ratified by governance 2026-08-03 (applied on MECH-332) and routed
> /queue-experiment V3-EXQ-878a, a calibration pilot gating on
> n_committed_steps before repeating the dissociation. That autopsy also flags
> a measurement-hygiene defect directly relevant to THIS claim's 325a/325b
> history: z_harm_s_ratio silently falls back to 1.0 on empty committed-sample
> data, so a zero-commitment run can report a spurious "no attenuation"
> (s_ratio_D=1.0000 s_ratio_C=1.0000) that is indistinguishable from a real
> null -- it should emit NaN/None. As of 2026-08-08 V3-EXQ-878a is not yet in
> ree-v3/experiment_queue.json.

### 7b. SD-021 — replace the closing sentence of `what_would_answer`'s NON-DEGENERACY PRECONDITION paragraph

Current final sentence:

> A fresh substrate approach to MECH-269, or resolution of the MECH-439 ceiling, is
> required before this precondition can be considered live again.

Proposed replacement:

> A fresh substrate approach to MECH-269, or resolution of the MECH-439
> ceiling (itself a CONTESTED candidate since the GOV-CEIL-1 demotion
> 2026-07-09, awaiting ARC-107 / V3-EXQ-689g), is required before this
> precondition can be considered live again -- with the caveat that the
> confirmed failure_autopsy_V3-EXQ-878_2026-08-03 identifies a nearer and
> cheaper gate on this pathway specifically: E3's commitment gate (MECH-090)
> did not elevate at all in that arena/schedule (n_committed_steps=0, 3/3
> seeds), a calibration puzzle routed to V3-EXQ-878a, not a substrate ceiling.
> Clear that first; the monostrategy precondition binds only the
> drive-regime-divergence half of the test.

### 7c. SD-032c — append to `evidence_quality_note`

> BLOCKER FRAMING CROSS-REFERENCE [2026-08-08]: the "blocked on MECH-269 V_s
> landing" hold above (2026-04-22) is stale as the sole named blocker; no
> status or v3_pending change is implied. (1) DEEPER SHARED ROOT: the
> V_s-monostrategy lock is the monomodal-policy collapse registered as
> MECH-309, whose selection-side mechanism is MECH-439 (F-dominance, ~88-89%
> of E3 committed-selection variance). Sibling SD-032b's ceiling_routing_note
> (2026-06-19) records MECH-269 as "wired_but_inert... SUPERSEDED as the
> operative blocker by the F-dominance conversion ceiling"; the same
> supersession applies here, but more weakly than to SD-032b, because
> SD-032b's failing criterion IS committed-action-class entropy (MECH-439's
> own metric) whereas this claim needs drive-regime divergence in
> aic_salience/harm_s_gain, which is upstream of the selection stage. MECH-439
> is itself a CONTESTED candidate (GOV-CEIL-1 demotion 2026-07-09, 11
> confirmed substrate_ceiling autopsies, null reading carried co-equally,
> awaiting ARC-107 / V3-EXQ-689g), so naming it redirects the watch-point to a
> live front rather than unblocking anything. (2) MORE PROXIMAL, NEWER
> BLOCKER: the confirmed failure_autopsy_V3-EXQ-878_2026-08-03 tested this
> module directly (its "Pathway 2", substrate ree_core/cingulate/aic_analog.py,
> named as "SD-021, now subsumed by SD-032c") and found n_committed_steps=0 vs
> floor=8 across all 3 seeds: E3's commitment gate (MECH-090 BetaGate) never
> elevated in that arena/schedule, so the pathway is UNTESTED, not falsified.
> Diagnosis: environment/schedule calibration gap (test-design), explicitly
> NOT a substrate gap; ratified by governance 2026-08-03 (applied on MECH-332)
> and routed /queue-experiment V3-EXQ-878a. Note also the autopsy's
> measurement-hygiene finding: z_harm_s_ratio silently falls back to 1.0 on
> empty committed-sample data, which is how a zero-commitment run can present
> as a spurious clean null. As of 2026-08-08 V3-EXQ-878a is not yet queued.

### 7d. SD-032c — append to `what_would_answer`, after the NON-DEGENERACY PRECONDITION paragraph

> PRECONDITION UPDATE [2026-08-08]: the MECH-269 route above has been run to
> exhaustion by two independent paths (V3-EXQ-325f reef/monostrategy fix; the
> MECH-295 goal_pipeline:GAP-4 Tier-1 cohort 490g-k, CLOSED 2026-06-09 without
> landing V_s-driven behavioural divergence, re-scoped rather than fixed), and
> MECH-269's per_region_vs remains instantaneous-only. The live front for the
> underlying monostrategy degeneracy is MECH-309/MECH-439 -> ARC-107
> (MECH-448/449) -> V3-EXQ-689g; watch there, not at MECH-269. Separately and
> more cheaply: per confirmed failure_autopsy_V3-EXQ-878_2026-08-03, this
> module's own test has never yet had its commitment trigger fire
> (n_committed_steps=0, 3/3 seeds) -- V3-EXQ-878a calibration must clear before
> either CONFIRMING or FALSIFYING below is evaluable at all, independent of the
> monostrategy question.

---

## 8. Follow-on spawned

- **`chip-20260808-exq878a-calibration-queue`** — `/queue-experiment` V3-EXQ-878a, the
  governance-ratified (2026-08-03) calibration pilot for the SD-021/SD-032c descending
  pathway, plus the `z_harm_s_ratio` NaN-fallback hardening. Not in the queue as of
  2026-08-08. Recorded in `TASK_CHIPS.json`.

## 9. Sources read

- `REE_assembly/docs/claims/claims.yaml` @ `origin/master` — SD-021, SD-032b, SD-032c,
  MECH-439, MECH-269, MECH-309, MECH-332, MECH-256, SD-029
- `REE_assembly/evidence/planning/failure_autopsy_V3-EXQ-878_2026-08-03.md` (confirmed)
- `ree-v3/experiment_queue.json` (V3-EXQ-878a absence check)
