# `competence_floor` — re-posing record (GOV-FANOUT-1 recurrence, cycle 2026-07-19a)

- **Generated:** 2026-07-19T12:05:43Z
- **Session:** `angry-gauss-b9d787` — "competence_floor re-pose (GOV-FANOUT-1 recurrence)"
- **Trigger:** `hypothesis_space_integrity.md` §"Fan-out recurrence (ACTIONABLE, 1)" — N>=3 portfolios on one question, denominator 7 -> 16, 5 legs alive; plus `convergence.convergence_class == "circling"` in `hypothesis_space.v1.json`
- **Question:** `competence_floor` in `hypothesis_space_registry.v1.json`
- **Claims:** MECH-457 (candidate / v3_pending), INV-088 — **this record promotes and demotes nothing.** It is a routing/framing decision only.
- **Registry writes:** **NONE.** Governance is derive-only over the frozen registry; its single producer is `/failure-autopsy` Step 9b. The registry deltas identified in §5 are *routed*, not applied.

---

## Headline

**The recurrence flag is correct, and it was already discharged — six hours before it fired.** The re-posing it demands was performed on 2026-07-18T18:37:29Z by `mech457_retention_portfolio_2026-07-18.md`, whose §161 anticipates this exact flag and answers it. Portfolio 3 is not the third symptom of a mis-posed question; **it is the cure, miscounted as a symptom**, because the overlay counts portfolios and the metabolizing act necessarily took the form of a portfolio.

Three things nonetheless remain to be done, and this record does them:

1. The `circling` verdict is **verified as mechanically correct but substantively over-stated** — at axis granularity only **1 of 4** new legs is a true re-entry, not 4 of 4 (§2). This check is stronger than the portfolio's §3 argument and was not performed there.
2. The mis-posing is **deeper than the operationalization**: the question's *title* carries a presupposition that V3-EXQ-780 falsified (§3), and the terminal-only DV did not merely fail to see retention — it **manufactured the very recurrence signal** now indicting the question (§4).
3. The situation **changed materially after every document above was written**: two of the four retention substrate builds landed on 2026-07-18, the portfolio's own "queue nothing until two legs are buildable" gate is **now met**, and the experiment queue is **empty** (§6).

**Do not open portfolio 4.** The correct next action is to queue two already-unblocked legs from portfolio 3.

---

## 1. What was read

All 16 legs of `competence_floor`, `axis_families.map` and its `_provenance_caveat`, the question's `synthesis` / `decision` / `fanout_growth_events` blocks, the `convergence` block in `hypothesis_space.v1.json`, `mech457_retention_portfolio_2026-07-18.md` in full, the four `mech457_*` nodes in `substrate_queue.json`, and `ree-v3/experiment_queue.json`.

Leg census (16 legs; 5 alive, 1 confirmed, 1 split, 9 eliminated):

| family | eliminated | other |
|---|---|---|
| `representation` | H-rep | — |
| `world` | H2-reward-coupling | — |
| `instrumentation` | H3-credit-horizon | — |
| `process` | H-credit, H-return, H-curric, H-arbitr, H1-drive-schedule | H-optim **confirmed**, H-explore **split**, H-retention-critic *alive*, H-retention-consolidation *alive* |
| `constitution` | H-approach-primitive | H-bc-prior *alive*, H-retention-auxiliary-decay *alive*, H-consummation-binding *alive* |

---

## 2. Is `circling` true? — verified, and over-stated

`circling` asserts that new legs re-enter families that already hold eliminated legs. **At family granularity this is arithmetically correct: 4 of 4.** The verdict is not wrong about the data.

But `axis_families.map` is documented as **COARSE** and human-owned, and its `_authority` field designates disputing it as the correct way to dispute a verdict. Descending one level — to the per-leg `axis` labels the map coarsens — the picture inverts:

| new leg | axis | family | prior leg(s) on **that axis** | true re-entry? |
|---|---|---|---|---|
| `H-retention-critic` | `algorithm` | process | H-optim — **confirmed**, not eliminated | **no** |
| `H-retention-consolidation` | `policy` | process | **none — fresh axis** | **no** |
| `H-retention-auxiliary-decay` | `learning-signal` | constitution | H-bc-prior — **alive** | **no** |
| `H-consummation-binding` | `intrinsic-architecture` | constitution | H-approach-primitive — **eliminated** | **yes** |

**Only 1 of 4 lands on an axis that already holds an eliminated leg.** The other three sit on an axis that is fresh (`policy`), one whose sole prior leg is *confirmed* (`algorithm`), or one whose sole prior leg is *still alive* (`learning-signal`). The family-level "4 of 4" is produced by coarsening, not by the legs.

The portfolio's §3(a) corrected only the family arithmetic (two into `process`, not three). It never ran this axis-level check, which is checkable directly from the frozen registry and is materially more favourable to the campaign.

**The one true re-entry is defensible on its own terms.** `H-consummation-binding` re-enters `intrinsic-architecture` after `H-approach-primitive` was eliminated by V3-EXQ-781 — but it is motivated by 781's own *load-bearing positive finding*: approach drive earned at 0.707 while raw_view foraging was **suppressed** to 0.200 from a 2.983 control, tight across all three seeds. A re-entry driven by an unexplained positive inside the eliminating run is refinement, not circling. It is nonetheless the one leg of the four that should carry the heaviest justification burden, and the one to watch if the pattern repeats.

**Root cause of the verdict, and why it will recur.** `axis_families` partitions on intervention **locus** — "what layer of the system a hypothesis blames." It has no dimension for the **explanandum**. All 12 pre-retention legs explain *failure to acquire*; all 4 retention legs explain *failure to retain*, conditioned on a state (installed competence at 20.933) that no prior leg ever reached. Same locus, different thing-to-be-explained. The discriminator is structurally incapable of seeing that, so it must report `circling`.

**This record concurs with the portfolio's decision NOT to mint a `retention` axis** (§3, "retention is a question shape, not a locus" — minting one would gerrymander a locus taxonomy to dodge an unfavourable score, precisely what `_provenance_caveat` guards against). The limitation should be recorded in the discriminator's documentation instead — see §5.

---

## 3. The mis-posing is a falsified presupposition, not just a stale operationalization

The question's registered title is:

> **"Why is committed competence stuck below the foraging floor?"**

That title **presupposes competence is never reached**. The presupposition was falsified on 2026-07-18: V3-EXQ-780's raw_view arm reached **20.933** immediately post-BC — above the 13.05 lift-competence target, inside the 32.72 BC-expert band, against a 48.05 `local_view_greedy` ceiling — with 3/3 seeds taking the install. RL refinement then eroded it to **11.667**.

So the question as posed asks why something never happens **that in fact does happen**. That is the precise form of the mis-posing, and it is worse than a stale framing: a question with a false presupposition cannot be answered, only endlessly re-explained. Every leg that fails to produce terminal competence looks like "another rival is needed," when the actual structure is *competence is reachable, transient, and invisible to the DV*.

The portfolio changed the **operationalization**. The registry's `title`, `synthesis`, and `decision` blocks still carry the **acquisition** framing (`decision.decision_question`: "Which competence-directed dependency lets the actor-critic **convert** a sufficient observation into competent foraging"). Those are the residual deltas.

---

## 4. The terminal DV manufactured the recurrence signal

This is the sharpest available statement of what went wrong, and it is stronger than "the prior legs could not have detected a retention deficit" (portfolio §3(b), §32 — the passive form).

Ten legs were adjudicated on **terminal** competence. **If competence is acquired and then eroded, a terminal-only DV returns "flat" for every intervention — whether or not the intervention worked.** Such a measurement architecture cannot distinguish a failed manipulation from a successful one that decayed. It therefore *manufactures nulls at a constant rate*, independent of the science. A campaign receiving a steady stream of nulls responds by enumerating more rivals. More rivals across more portfolios is exactly what the recurrence overlay counts.

**So the recurrence signal is, in substantial part, an artifact of the DV — not evidence of under-enumeration, and not evidence that any of the 16 hypotheses is wrong.** The overlay's own reading ("MIS-POSED rather than under-enumerated") is correct, and this is the mechanism behind it.

V3-EXQ-780 is the proof case, and it is unusually clean: the covariate that catches the failure mode (`post_bc_foraging_competence`) was **present, declared, and load-bearing** — yet the interpretation grid enumerated only a `~0` null, so a manipulation that succeeded above target was scored as a null and self-routed `bc_prior_not_the_axis`. The autopsy rejected that self-route. **The instrumentation was adequate; the interpretation grid was not.** Portfolio 3's four `measurement_requirement` blocks encode the fix (mandatory trajectory DV; mandatory "manipulation succeeded and then decayed" branch; mandatory `substrate_not_ready_requeue` when an install did not take). That fix is correct and should be treated as binding on any future leg of this question.

---

## 5. Re-posed operationalization

### 5a. Is RETENTION the right frame? — yes, but the question **bifurcates**

Retention is correct for `raw_view`, where the install took 3/3 and eroded. It is **not** the right frame for `z_world`, where post-BC was **0.583 with 0/3 seeds taking the install** — the manipulation never installed at all. That is an acquisition/installability question, and it is a *different* question wearing the same qid.

Carrying both under one question is itself part of what makes the campaign look non-convergent: two explananda, one denominator.

| | Q1 — retention | Q2 — installability |
|---|---|---|
| **Re-posed as** | Competence above the lift target is installable but not retained. **What sets the decay half-life of an installed competent policy under continued RL refinement?** | **Why does the imitation pathway fail to install on the detached `z_world` representation (0/3) while installing on `raw_view` (3/3)?** |
| **Positive control** | raw_view 20.933 post-BC, 3/3 seeds | raw_view 3/3 install is the contrast case |
| **DV** | competence **trajectory** post-installation; half-life | install success rate at the post-BC checkpoint |
| **Decisive when** | one lever moves the half-life while the anti-aliased others do not | representational-capacity vs plumbing vs interface accounts are separated |
| **Legs** | H-retention-critic, H-retention-consolidation, H-retention-auxiliary-decay, H-consummation-binding | currently none — 780's secondary finding |
| **Status** | 2 of 4 buildable **now** (§6) | under active diagnosis, session `blissful-hugle-5dd043` |

### 5b. What a decisive answer looks like (Q1)

A half-life / trajectory statistic that separates three branches, with the third being the one the old grid could not express:

1. **never installed** → uninformative about retention; self-route `substrate_not_ready_requeue`, never a retention verdict;
2. **installed and held** → that lever is the retention mechanism;
3. **installed and decayed, at a measurable rate** → decay rate is the readout, and a lever is implicated when it moves the rate.

Decisive when one lever moves the half-life and the anti-aliased others do not. The three-way anti-alias is already designed and is load-bearing: value estimator only (`H-retention-critic`) / update constraint only (`H-retention-consolidation`) / auxiliary persistence only (`H-retention-auxiliary-decay`), with the substrate notes recording that both landed builds hold the constraint (distributional critic: policy head bit-identical, contracts C2/C2b; bc_aux_schedule: `linear_anneal` not `warm_then_anneal`, deliberately outside the mode-gate).

### 5c. `H-bc-prior` now carries two questions

`H-bc-prior` is `alive` with `evidence_direction: inconclusive`, but its own `resolution.basis` states the open question "shifts from whether a behavioural prior can produce competence (**it can**) to why the substrate does not RETAIN it." As originally posed — a *competence-directed behavioral prior* as an acquisition dependency — the leg is effectively **answered affirmatively**. What remains alive under that hid is a different question, already covered by the four retention legs.

Leaving one hid straddling an answered question and an open one inflates the alive count and blurs the frontier. **Recommend `/failure-autopsy` split it**: resolve the acquisition half on the 20.933 existence proof, and route the retention half to the legs that own it.

### 5d. Registry deltas — ROUTED, not applied

**Nothing below is written by this session.** Route through a `/failure-autopsy` session (Step 9b is the registry's single producer):

| # | Delta | Basis |
|---|---|---|
| D1 | Re-pose `title` — drop the falsified "stuck below the floor" presupposition | §3 |
| D2 | Refresh `synthesis` (`under_test` still reads "pending — H-bc-prior / H-approach-primitive portfolio (to be queued)"; that portfolio ran and resolved 2026-07-18) | stale |
| D3 | Refresh `decision` — `decision_question` still acquisition-framed; `live_gate` and `distance_phrase` both still read "not yet queued" | stale |
| D4 | Clear `probe_status: substrate_blocked` on `H-retention-critic` and `H-retention-auxiliary-decay` — **both builds landed** (`ree-v3` `8e88ffc`, `9a8dbae`) | §6 |
| D5 | Split `H-bc-prior` per §5c | §5c |
| D6 | Consider splitting qid `competence_floor` into retention and installability questions per §5a | §5a |

D4 is the only one that is a plain factual staleness; D1/D2/D3 are the re-posing proper; D5/D6 are recommendations for the autopsy to adjudicate, not conclusions.

**Discriminator documentation (separate from the registry, and NOT a map edit):** record in `axis_families._purpose` or the integrity report's narrative that `convergence_class` partitions on **locus only** and is blind to a change of **explanandum**, so a legitimate re-pose that keeps its loci will score `circling`. Without this, §2's finding is re-litigated every cycle.

---

## 6. What changed after every document above was written

| fact | as at |
|---|---|
| `mech457_distributional_critic` — **implemented** (`ree-v3` `8e88ffc`) — unblocks `H-retention-critic` | 2026-07-18T19:00Z |
| `mech457_bc_aux_schedule` — **implemented** (`ree-v3` `9a8dbae`) — unblocks `H-retention-auxiliary-decay` | 2026-07-18T20:37Z |
| `mech457_policy_kl_anchor` — `proposed`, `ready: true` | — |
| `mech457_consummatory_act` — `proposed`, `ready: true` (most invasive; changes `action_space_size`) | — |
| `ree-v3/experiment_queue.json` — **empty, depth 0** | 2026-07-19T12:05Z |

The portfolio's gate — *"Queue nothing until at least two legs are buildable"* (§140) — is **met**. `mech457_bc_aux_schedule`'s own `blocked_note` records the threshold as met and states that "queueing remains a separate decision."

**That decision is now the live one, and it is the answer to the recurrence flag.** The campaign's next action is neither a fourth portfolio nor more substrate: it is to **queue the two unblocked retention legs together** — `H-retention-critic` and `H-retention-auxiliary-decay` — via `/queue-experiment`, under new EXQ numbers, honouring the four `measurement_requirement` constraints verbatim.

Queue them **as a pair, not singly**: GOV-FANOUT-1 exists because adjudicating a leg in isolation is how a confident-but-wrong elimination enters the frozen ledger, and the 780/781/782 cluster is the validating instance (781's elimination alone would have rested on no demonstration that competence was reachable at all).

The re-derive brake permits this. The producer-half autopsy records `re_derive_brake.fired: false` on four grounds — different question, different null, different measurement, and a positive control (20.933) that no braked autopsy possessed. This record **reads that rationale rather than re-deriving it**, and independently confirms the fourth ground from the registry.

---

## 7. Outcome, for the next cycle's overlay

**The `competence_floor` recurrence flag raised in cycle 2026-07-19a is METABOLIZED.** The re-posing was performed by `mech457_retention_portfolio_2026-07-18.md` (§161) and is verified, extended, and recorded here. Portfolio 3 changed the explanandum from acquisition to retention and the DV from terminal to trajectory; it is the discharge the flag asks for, not a further instance of what it warns against.

**Standing rules carried forward:**

- **The flag will fire again next cycle, unchanged**, because the overlay counts portfolios and portfolio 3 is permanent history. **Read it against this record before acting.** N will read 3 until a fourth portfolio is opened.
- **`convergence_class` will continue to read `circling`** for the same reason (§2 root cause), and this is expected, not a new signal.
- **If the four retention legs resolve and a fifth portfolio is proposed on the retention operationalization, treat the recurrence flag as BLOCKING** — that is the pattern it exists to catch. Portfolio 3 §169 sets this rule and this record affirms it.
- **Any new leg on this question must carry the four `measurement_requirement` constraints** (trajectory DV; a "succeeded then decayed" branch in the interpretation grid; routing on declared covariates; `substrate_not_ready_requeue` when an install did not take). V3-EXQ-780 is the standing worked example of what their absence costs.

Nothing here is promoted, demoted, or gated. MECH-457 stays candidate / v3_pending; INV-088 unchanged.
