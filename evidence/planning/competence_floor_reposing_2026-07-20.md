# `competence_floor` — re-posing record (GOV-FANOUT-1 recurrence, cycle 2026-07-20b)

- **Generated:** 2026-07-20T16:29:18Z
- **Session:** `musing-einstein-c80816` — "competence_floor re-pose (GOV-FANOUT-1 recurrence, cycle 2026-07-20b)"
- **Trigger:** `check_hypothesis_space_integrity.py` — "Fan-out recurrence (N>=3 portfolios, ACTIONABLE): 1 — `[recurrence] competence_floor`"; plus `convergence.convergence_class == "circling"`, `families_fresh: []` in `hypothesis_space.v1.json`
- **Claims:** MECH-457 (candidate / v3_pending), INV-088 — **this record promotes nothing, demotes nothing, gates nothing.** Routing and framing only.
- **Registry writes:** **NONE.** `hypothesis_space_registry.v1.json` has a single producer, `/failure-autopsy` Step 9b; governance is derive-only over it. Every registry delta in §6 is *routed*, not applied.
- **Supersedes in scope, not in content:** `competence_floor_reposing_2026-07-19.md`. That record stands; §1 below states precisely which of its conclusions the new evidence overturns and which it leaves intact.

---

## Headline

**The 2026-07-19 re-pose was right about the disease and wrong about one of the two patients.** It bifurcated the question into Q1 (*retention*, on `raw_view`) and Q2 (*installability*, on `z_world`), and recommended splitting the qid accordingly. Q1 survives intact and has since been half-answered. **Q2 does not survive: it is not a scientific question, it is a bug report.**

V3-EXQ-737a (confirmed 2026-07-20) and V3-EXQ-728 independently establish that in the driver family carrying this entire campaign, the P0/P1 warmup has **no optimizer group covering `latent_stack`** — 0 of 61 tensors move, 0 of 4 `world_encoder` tensors move, bit-identical. `z_world` is a **frozen random projection at initialisation**, not a prediction-trained representation. Q2 asks why imitation fails to install on a learned representation that was never learned.

The single most consequential fact this exposes is larger than Q2:

> **Every `z_world` arm in all 16 legs of this campaign has been evidentially void.** Each leg was designed as a two-representation adjudication (`z_world` × `raw_view`); the `z_world` half could not express any manipulation, so it returned "flat" for every lever regardless of truth. The campaign has been a **one-representation campaign reported as a two-representation campaign** for sixteen legs.

That is the same structural pathology the 2026-07-19 record identified in the terminal-only DV — *a measurement architecture that manufactures nulls at a constant rate, independent of the science* — recurring on the **arm** axis instead of the **DV** axis. **Naming these as one failure class, and gating against it, is the substance of this re-pose.**

**Refused: portfolio 4. Refused: a same-question letter re-queue. Refused: re-opening the closed families** (§3 — the defect *strengthens* the one elimination it touches, and the other two are carried by defect-free arms).

---

## 1. What changed since the 2026-07-19 record

| fact | as at | effect on the 07-19 record |
|---|---|---|
| `H-bc-prior` split three ways at the `/failure-autopsy` Step 8 gate | 2026-07-19T15:14:23Z | **D5 applied.** alive 5 → 4 |
| Registry `title` re-posed off the falsified "stuck below the floor" presupposition | — | **D1 applied** |
| V3-EXQ-788 **PASS** — distributional critic retains 1.839 vs 0.525 scalar | 2026-07-20 | Q1's live gate **discharged**; `H-retention-critic` decided |
| V3-EXQ-789 **FAIL** — auxiliary succeeded then decayed on all three schedules | 2026-07-20 | `H-retention-auxiliary-decay` **eliminated** |
| `mech457_policy_kl_anchor` built (`ree-v3` `399b17caed`), **V3-EXQ-792 queued** | 2026-07-20 | `H-retention-consolidation` alive and in flight |
| **V3-EXQ-737a confirmed: no optimizer group covers `latent_stack`** | 2026-07-20T15:30:07Z | **overturns the 07-19 §5a Q2 framing and its D6 recommendation** |
| V3-EXQ-728 independently confirms (0/4 world_encoder, 0/61 latent_stack, 3/3 seeds) | — | second strike; not a one-driver artefact |
| `sd_zworld_warmup_optimizer_group` created — priority 1, `ready: true`, `pending_implementation` | 2026-07-20 | the owed resolution |

The 07-19 record's **standing rules carry forward unchanged**: the flag fires every cycle because the overlay counts portfolios and portfolio 3 is permanent history; `convergence_class` will keep reading `circling` because it partitions on intervention **locus** and is blind to a change of **explanandum**; the four `measurement_requirement` constraints bind every future leg. This record adds a fifth (§4, **R2**).

---

## 2. Blast radius of the defect — measured, not assumed

`_lib/mech457_fanout.py` is imported by **every** MECH-457 leg driver from V3-EXQ-747 through V3-EXQ-792, and its `warmup_zworld` calls `x734._train_all_on_agent` — the function with no `latent_stack` optimizer group. The exposure is therefore campaign-wide, not confined to the x734/737 family named in the autopsy title.

Two scoping facts keep this from being a general invalidation, and both cut the same way:

- **`raw_view` arms are structurally unaffected.** They never touch the encoder. Every `raw_view` reading in the campaign stands.
- **The defect does not explain the competence floor.** V3-EXQ-737a's `ppo_raw_obs` control arm has *no encoder at all* and still reaches only **0.567**, against a `local_view_greedy` of **48.05** from the identical view and an oracle of **57.2**. A path that cannot suffer this defect fails anyway.

**So the encoder defect is not a rescue.** It does not absolve the campaign's nulls and it must not be read as one. What it does is void half of every leg's design while leaving the load-bearing half intact.

**The guard is now wired.** `assert_world_encoder_trained` was lifted into `experiments/_lib/zworld_encoder_guard.py` (`ree-v3` `9f72532`) and is called from `warmup_zworld`, so fanout-based legs are instrumented going forward. 737a's own learning is the reason this matters: *"A detection guard is worth nothing until a driver calls it."*

---

## 3. Do the closed families need re-opening? — **NO, on three different grounds**

This is the question the governance note routes here, and a blanket answer would be wrong. The correct test is per-family: **did the eliminating run's decisive arm touch the encoder?**

| family | leg | eliminated by | decisive arm | verdict |
|---|---|---|---|---|
| `representation` | `H-rep` | V3-EXQ-747/748/749 | `z_world` **+ BC = 32.72** vs `raw`+BC 20.93 | **stands *a fortiori*** — see below |
| `world` | `H2-reward-coupling` | V3-EXQ-771 | treatment at the floor on **both** reps; `raw` arm defect-free | **stands** — carried by the `raw` arm alone |
| `instrumentation` | `H3-credit-horizon` | V3-EXQ-772 | treatment at the floor on **both** reps; `raw` arm defect-free | **stands** — carried by the `raw` arm alone |

**`world` and `instrumentation`: closed on evidence, not on the defect.** Both eliminations rest on a treatment arm sitting at the ~0–1 floor with readiness met (`local_view_greedy` 48–55, oracle 57–61) and `non_degenerate: true`. The `raw_view` half is defect-free and independently at the floor, so the conclusion never needed the `z_world` half. The `z_world` half is retrospectively uninformative; the verdict is not.

**`representation`: the defect *strengthens* the elimination rather than undermining it.** `H-rep` asserted that a prediction-trained `z_world` is action-inadequate. It was eliminated because `z_world`+BC reached **32.72**, *beating* `raw`+BC at 20.93. If that `z_world` was a frozen random projection, then a **random** projection carried behavioural cloning to 32.72 — a stronger refutation of "this representation cannot support competent action" than the original reading, not a weaker one. Re-opening on that basis would be backwards.

**But the elimination's *label* is now wrong, and that is where the real finding is.** What was actually falsified is:

> *"a random 250→d projection is action-inadequate"*

not

> *"a prediction-trained `z_world` is action-inadequate."*

**The second proposition has never been tested — not once in sixteen legs.** The family does not need re-opening; a question inside it has never been opened at all (§5, **R4**).

**One honesty caveat, stated rather than buried.** The 747/748/749 exposure is inferred from the shared `mech457_fanout` → `_train_all_on_agent` import path, and was directly *measured* only on the 780/737a/728 paths. The inference is strong and the direction of the conclusion is defect-robust either way — but it should be **confirmed by the guard on the first post-`sd_zworld_warmup_optimizer_group` retest**, not treated as settled here.

---

## 4. The re-posed operationalization

The old design asked, on every leg: *"does this lever lift competence — on `z_world` and on `raw_view`?"* Four changes:

### R1 — Drop `z_world` from the adjudicating design until the substrate lands

Until `sd_zworld_warmup_optimizer_group` is implemented, a `z_world` arm is a **null-generator**: it cannot express any manipulation, so it returns flat for every lever whether or not the lever works. Including one does not add a representation contrast; it adds a guaranteed null that reads as evidence and inflates apparent rival-exhaustion.

Adjudicate on `raw_view` alone, and **say so in the design** rather than shipping a two-arm design whose second arm is known-void.

### R2 — The guard is a **precondition**, not an observation (fifth `measurement_requirement`)

Any leg that does carry a `z_world` arm **must** call `assert_world_encoder_trained` and, on a fire, route `substrate_not_ready_requeue` for that arm — **never** a scientific verdict. 737a's handling is the worked example, and its second learning states the design rule exactly: record the confound under `recorded_preconditions` per-arm rather than gating the whole run, so the unaffected control stays readable.

This joins the four constraints the 2026-07-19 record made binding (trajectory DV; an explicit "succeeded then decayed" branch; routing on declared covariates; `substrate_not_ready_requeue` when an install did not take).

### R3 — Q2 is **withdrawn as a hypothesis and re-posed as a build**

"Why does the imitation pathway fail to install on `z_world` (0/3) while installing on `raw_view` (3/3)?" is answered: **because there is no `z_world`.** Per `work_graph_debt_vocabulary.md` this is a debt **reclassification**, and a favourable one:

> `complex (probe-gated)` → **`complicated (buildable)`**

Nothing unknown remains at that node. It is owed to `sd_zworld_warmup_optimizer_group` (priority 1, `ready: true`, unblocks MECH-457 / INV-088 / Q-002), route `/implement-substrate`. **It must not be carried as a live hypothesis leg**, because doing so re-imports execution backlog into the discrimination denominator — the exact padding the `fanout_growth_note` warns against.

**This withdraws the 07-19 record's D6** (split the qid into retention and installability questions). D6 was correct given what was known on 07-19; the installability half is no longer a question to split *to*.

### R4 — The fresh axis the defect exposes

Sixteen legs, `families_fresh: []`. The fresh territory was never going to be found by adding a seventeenth rival — and this is the re-pose proper:

> **Does prediction-training `z_world` confer any advantage over a random projection of the same dimensionality?**

This has genuine novelty the campaign has not had:

- It carries a **measured baseline, not a hypothetical one.** A random projection is not a strawman here — it is what has been running, and it scored 32.72 under BC. The control condition has been executing as the treatment for the whole campaign.
- It is **decisive in both directions.** If prediction-training does not beat a random projection, the entire `z_world` pathway is dispensable for competence and INV-088's differentiation programme is reframed. If it does, the campaign has sixteen legs of `z_world` readings to re-interpret against a substrate that can finally express them.
- It is **not portfolio 4.** It is one question, of a shape the question has never taken — asked *about the instrument*, not about another candidate mechanism. It becomes askable only *after* `sd_zworld_warmup_optimizer_group` lands, which makes the build the live gate rather than a rival.

**Live gate after this re-pose:** V3-EXQ-792 (`H-retention-consolidation`) in flight settles Q1's remaining anti-aliased locus; `sd_zworld_warmup_optimizer_group` is the critical path for everything `z_world`.

---

## 5. What was refused

| refused | ground |
|---|---|
| **Portfolio 4** | GOV-FROZEN-1 on N=3 recurrence: enumerating rivals on an unchanged framing is the denominator-side twin of re-running a braked experiment harder. `mystery (known data)` debt — reframe, do not gather. |
| **A same-question letter re-queue** (769b-style: more capacity / config / budget) | The re-derive brake has fired seven times on this axis. Nothing here re-opens it. |
| **Re-opening `world` and `instrumentation`** | Both eliminations are carried by defect-free `raw_view` arms with readiness met and `non_degenerate: true` (§3). |
| **Re-opening `representation`** | The defect strengthens `H-rep`'s elimination *a fortiori* — a random projection reached 32.72 under BC (§3). What is owed is a *new* question (R4), not a re-opening. |
| **Reading the encoder defect as a rescue for the campaign's nulls** | `ppo_raw_obs` has no encoder and still reaches 0.567 against a 48.05 anchor (§2). |
| **Minting a `retention` or `instrument` axis to move the `circling` score** | `axis_families` partitions on intervention locus; gerrymandering it to dodge an unfavourable verdict is what `_provenance_caveat` guards against. The 2026-07-18 portfolio and the 2026-07-19 record both declined this; so does this record. |
| **Editing `hypothesis_space_registry.v1.json`** | Single producer is `/failure-autopsy` Step 9b; governance is derive-only. §6 routes, it does not apply. |

---

## 6. Registry deltas — ROUTED, not applied

Continuing the 07-19 D-series. Route through a `/failure-autopsy` session.

| # | delta | status / basis |
|---|---|---|
| D1 | re-pose `title` off the falsified presupposition | **APPLIED** 2026-07-19 |
| D5 | split `H-bc-prior` | **APPLIED** 2026-07-19T15:14:23Z |
| D6 | split the qid into retention + installability questions | **WITHDRAWN** — §4 R3; the installability half is a build, not a question |
| D7 | record on `H-retention-auxiliary-decay` that it is **eliminated** (V3-EXQ-789) and on `H-retention-critic` that it is **decided** (V3-EXQ-788 PASS, retains 1.839) | §1; `failure_autopsy_mech457-retention-portfolio_2026-07-20` |
| D8 | annotate the `z_world` half of every leg 747→789 as **evidentially void** — instrument defect, not evidence. Do **not** re-open the families (§3); the annotation records *why* the `z_world` readings must not be re-consumed | §2, §3 |
| D9 | add the guard precondition (§4 R2) as a fifth `measurement_requirement` on this question | §4 R2 |
| D10 | refresh `decision.live_gate` — still reads "H-retention-critic + H-retention-auxiliary-decay, queued AS A PAIR ... not yet queued". Both have since **run and resolved**; the live gate is now V3-EXQ-792 plus `sd_zworld_warmup_optimizer_group` | stale |
| D11 | refresh `synthesis` — its "SECOND, UNOWNED explanandum" paragraph reads the `z_world` 0/3 install as an open scientific question; it is a known defect with an owner | stale, §4 R3 |
| D12 | register R4 (§4) as the question's fresh axis once the substrate lands — **one leg, not a portfolio** | §4 R4 |

**Discriminator documentation** (not a map edit, and re-stated from 07-19 because it was not actioned): record in `axis_families._purpose` or the integrity report narrative that `convergence_class` partitions on **locus only** and is blind to a change of **explanandum** *or of instrument validity*, so a legitimate re-pose that keeps its loci scores `circling`. Without this, §3 is re-litigated every cycle.

---

## 7. RETRACTED — a stale-read false alarm raised by this record

**An earlier draft of this section reported that `REE_assembly` `8727483520` had dropped its `claims.yaml` edit and that the false "open routing decision" text was still live. That was WRONG, and it is retracted here rather than deleted.**

The correction had **already landed**, in `4a05ff2c0c` at 2026-07-20T17:28:05+01:00 — **four minutes before this record's own commit `c5bd4441ce` (17:32:02), and `4a05ff2c0c` was that commit's base.** The claim was false at the moment it was published, using content this session already had.

**Cause: a stale read, not a stale repo.** `docs/claims/claims.yaml` was read once at ~16:30, when HEAD *was* `8727483520` and the observation *was* accurate. It was never re-read before being written up an hour later, during which another session landed the fix. Re-reading a high-contention governance file immediately before asserting its content is the same discipline `CLAUDE.md` already mandates before *editing* one; this record shows the rule binds **reporting** as well as writing, because a false report of a governance defect costs another session's time to disprove.

**The diagnosis was also wrong about the mechanism, and the true one is worth recording.** This was attributed to the pathspec / dropped-path hazard. It was not. Per `4a05ff2c0c`'s own message, `8727483520` ran its edit in an `&&` chain behind a `git pull` that **failed**, so the edit never executed and the commit captured an unchanged `claims.yaml` while carrying a message describing the intended change. That is a distinct hazard from the ones documented in `CLAUDE.md`: not a commit that drops a declared path, but **a commit whose message overstates its content because an earlier link in an `&&` chain failed silently**. The `ree_commit.py` intent-record machinery does not catch it — there was no intent to declare, because the edit never happened. `git show --stat` does catch it, which is the standing backstop.

**What actually stands, verified in HEAD:** the note carries a complete `CORRECTION 2026-07-20` block; `H-retention-consolidation` is ALIVE, built at `ree-v3` `399b17caed`, queued as V3-EXQ-792 (pending); only `H-retention-auxiliary-decay` is eliminated. The block's generalised principle — *"A leg is eliminated by ITS OWN adjudicated result, never by a sibling's"* — is consistent with, and independently supports, §5 of this record.

---

## 8. Outcome, for the next cycle's overlay

**The `competence_floor` recurrence flag raised in cycle 2026-07-20 is METABOLIZED by re-posing, not by enumeration.** N stays 3; no portfolio was opened.

- **The flag will fire again next cycle, unchanged**, and `convergence_class` will keep reading `circling`. Both are expected. Read them against this record and `competence_floor_reposing_2026-07-19.md` before acting.
- **The critical path is a BUILD, not an experiment:** `sd_zworld_warmup_optimizer_group` (priority 1, ready) → `/implement-substrate`. Until it lands, every `z_world` arm is a null-generator (R1) and must be omitted or guard-gated (R2).
- **Escalation rule, carried forward and now armed twice over:** if the retention legs resolve and a portfolio 4 is proposed on an unchanged framing, treat the recurrence flag as **BLOCKING**. That is the pattern it exists to catch.
- **Standing lesson, stated as one class:** this campaign has now twice adjudicated against an instrument that could only return nulls — the terminal-only DV (16 legs, diagnosed 2026-07-19) and the untrained `z_world` encoder (16 legs, diagnosed 2026-07-20). A null from an instrument that cannot express the manipulation is not weak evidence; it is **no evidence**, and it is indistinguishable from strong evidence at the point of consumption. **Verify that the instrument can express the manipulation before the null is scored, not after the third portfolio.**

Nothing here is promoted, demoted, or gated. MECH-457 stays `candidate` / `v3_pending`; INV-088 unchanged.
