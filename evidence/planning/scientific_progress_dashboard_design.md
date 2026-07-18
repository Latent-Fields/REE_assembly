# REE Scientific Progress Dashboard — Design Proposal

*Draft — 2026-07-17. Complementary to the existing closure map; nothing here relaxes formal claim-closure standards.*

## 0. The problem, precisely

The closure map measures **epistemic closure** — claims formally promoted, falsified, or retired — weighted by `CLOSURE_STATUS_WEIGHTS` (`serve.py:1688`) over the `closure_plan:` nodes in `evidence/planning/*_plan.md`. It is deliberately conservative and should stay that way.

But in the current phase most experiments **reduce uncertainty without closing a claim**. Concrete, live example (the MECH-457 competence-floor line, 2026-07-13 → 2026-07-16):

| Run | What it did | Closure delta |
|-----|-------------|:---:|
| 747 | Ruled out *representation* as the wall (raw-view + sparse still fails) | 0 |
| 748 | Showed a dense teacher on z_world clears sparsity | 0 |
| 749 | Conjunction: needs adequate input **and** dense teacher | 0 |
| 751 | **Confirmed** the seed — success-independent novelty (RND) clears the 1.0 floor (5.22) | 0 |
| 752 | Ruled out backward credit-sweep (sub-floor) | 0 |
| 753 | Ruled out Go-Explore archive/return (sub-floor) | 0 |
| 754 | Ruled out AMIGo goal-frontier (sub-floor) | 0 |
| 755 | Ruled out explore/exploit arbitration gate (no gain over fixed RND) | 0 |

Eight experiments. **Zero** movement on the closure map. Yet the hypothesis space for "why is competence stuck below the foraging floor?" collapsed from seven candidate mechanisms to one synthesis (compose RND + credit-replay + developmental anneal → `mech457_competence_bootstrap_explorer`, now under test as V3-EXQ-765). That collapse **is** the scientific progress, and today it is invisible.

The dashboard's single job: **make uncertainty reduction visible without inflating closure.**

---

## 1. The conceptual dashboard — four independent needles + one feed

Four dimensions that move independently, plus a momentum stream. The design's thesis is that these are **orthogonal** — a healthy phase can move any subset while the others sit still, and conflating them (as a single "% done") is the exact error the closure map is being blamed for.

```
  BUILD            PROVE            NARROW              DECIDE
  Engineering      Epistemic        Hypothesis          Decision
  Completion       Closure          Space Remaining     Readiness
  ─────────        ─────────        ─────────           ─────────
  does the code    is the claim     how many rival      can a design
  exist yet?       proven?          explanations        choice legit-
                                    survive?            imately be made?
  (build ≠ proof)  (conservative,   (NEW — the          (state machine
                    unchanged)       missing signal)     per question)

                    ── SCIENTIFIC MOMENTUM ──
        every recent experiment, classified by what it MOVED
        (confirmed / ruled-out / control-repaired / measurement-
         improved / narrowed / implemented / inconclusive / underpowered)
```

Why four and not one composite: a composite index invites Goodhart (optimise the number, not the science) and re-creates the very conflation we're fixing. Keeping them separate is the anti-Goodhart move — you cannot make the closure needle move by narrowing hypotheses, and you cannot make the narrow needle move by shipping code.

### Dimension 1 — Engineering Completion ("Build")
**Question:** how much of the intended V3 architecture physically exists, independent of whether it validates?

- **Source:** `evidence/planning/substrate_queue.json` (110 items; 60 `implemented`) + SD-* claims with `epistemic_category: substrate_conditional/substrate_ceiling` + closure nodes the debt-vocabulary tags `complicated (buildable)`.
- **State machine per module:** `proposed → pending_implementation → implemented → implemented_pending_validation → validated`.
- **Headline metric:** severity-weighted fraction built (reuse `severity: load-bearing|high|medium|low` weights already on closure nodes). Plus an explicit **build–proof gap** counter: *"N modules built, M still unvalidated"* — the honest distance between "the code exists" and "the claim is proven."
- **Deliberately independent of Dimension 2.** A module can be `implemented` (Build ✔) while its claim is still `candidate/v3_pending` (Prove ✗). SD-024 da-modulated RBF density is exactly this shape: built and landed weeks before MECH-232 promoted.

### Dimension 2 — Epistemic Closure ("Prove")
**Unchanged.** A read-only mirror of `read_closure()` / `/api/closure`. Same 77.5 % weighted headline, same conservative weights, same `deferred → None` exclusion. The dashboard *embeds* the closure map; it never re-weights it. This is the guarantee that adding the new dashboard cannot soften closure.

### Dimension 3 — Hypothesis Space Remaining ("Narrow") — the new component
**Question:** for each open scientific question, how many rival explanations still survive?

Represented as a **branching tree per question**. Each hypothesis is a node with a state:

`untested · alive · eliminated · confirmed · split · dormant`

An experiment acts on the tree: `weakens` (adjudicated, control passed) → `eliminated`; `supports` → `confirmed`; a discrimination that reveals sub-cases → `split` (spawns children); `non_contributory`/`inconclusive` → node **unchanged** (correctly: an uninformative run must not shrink the space).

Worked example (real, from the fanout above) — question **"Why is competence stuck below the foraging floor?"**:

```
Q: competence-floor root  (MECH-457 / INV-088)
├── H-rep      representation insufficient        ✗ eliminated  (747, 749)
├── H-explore  needs dense teacher / exploration  ⇄ split → { sparsity-was-wall (748 ✓),
│                                                             but only 11% of ceiling }
├── H-optim    success-independent novelty (RND)  ✓ confirmed   (751 — clears 1.0 floor)
├── H-credit   backward credit-sweep              ✗ eliminated  (752)
├── H-return   Go-Explore archive/return          ✗ eliminated  (753)
├── H-curric   AMIGo goal-frontier                ✗ eliminated  (754)
└── H-arbitr   explore/exploit arbitration gate   ✗ eliminated  (755)

surviving: 1 synthesis (RND necessary, insufficient alone → compose)  ·  initial: 7  ·  reduction 6/7
```

**Metrics (principled; no fabricated precision):**
- **Surviving hypotheses** — an *integer*, the headline. Un-gameable without real discriminating experiments.
- **Reduction ratio** = eliminated ÷ pre-registered-initial, per question. Meaningful *only* because hypotheses are frozen at fan-out registration (see governance).
- **Coarse entropy proxy** `H = log₂(surviving) bits` — shown **only** when survivors are explicitly enumerated and roughly equiprobable; otherwise suppressed. We never attach invented per-hypothesis probabilities. (7→1 reads as ~2.8 bits removed on this question; that is the strongest defensible quantitative statement.)
- **Project roll-up:** total surviving hypotheses across all open questions, plotted over time — the **cumulative information-gain curve**, the chart that visibly falls while closure sits flat.

### Dimension 4 — Decision Readiness ("Decide")
**Question:** for each major architectural question, how many unknowns remain before a design decision can *legitimately* be made?

**State machine per question:**

`observation_bottleneck → prediction_rich_action_poor → discriminative_ready → decidable_now → decided`

- `observation_bottleneck` — can't even measure yet; needs a control or instrument (e.g. 750: matched-competence precondition unmet).
- `prediction_rich_action_poor` — theory is sharp, no clean discriminating experiment has run.
- `discriminative_ready` — one well-posed experiment away from a decision (e.g. the live 737 gate).
- `decidable_now` — evidence sufficient; only the human decision is outstanding.
- `decided` — folded into closure (hand-off to Dimension 2).

Each card carries a **decision distance** in the vocabulary the user asked for — *"1 successful discriminative experiment"*, *"2 additional controls"* — read directly off open fan-out legs and failed negative-controls in the autopsy stream. The evidence bar is bucketed into **deciles**, not false-precise percentages.

### Scientific Momentum feed
Every adjudicated experiment, reclassified from the binary PASS/FAIL into **what it actually moved**. Deterministic mapping (see §4). This is the section that stops treating "747 FAIL" and "a genuinely uninformative FAIL" as equivalent — 747 *ruled out the representation axis*, and the feed says so.

---

## 2. Recommended metrics (and what we deliberately refuse to compute)

| Metric | Type | Source | Goodhart guard |
|--------|------|--------|----------------|
| Severity-weighted build fraction | ratio | substrate_queue + closure severities | build ≠ proof; unvalidated sub-count shown alongside |
| Build–proof gap | integer | modules `implemented` but claim not promoted | — |
| Closure weighted % | ratio | `read_closure()` (unchanged) | conservative weights, read-only |
| Surviving hypotheses / question | integer | hypothesis_space.v1.json | elimination needs adjudicated `weakens` + passed control |
| Reduction ratio | ratio | eliminated ÷ initial, reported **both ways** | `initial_frozen_count_at_registration` is the frozen quantity, not `initial_frozen_count`; the latter may grow via **labelled** GOV-FANOUT-1 fan-out. Unlabelled/retro-padded growth = audit flag (b) |
| `log₂(surviving)` entropy proxy | bits | surviving count | shown only when enumerated & ~equiprobable |
| Cumulative surviving-hypotheses over time | time series | ledger snapshots | monotone claims audited against adjudications |
| Decision-readiness state | enum (5) | fan-out legs + autopsy | state advance requires an adjudicated event |
| Decision distance | phrase + integer | open legs / missing controls | phrased qualitatively |
| Momentum class | enum (8) | deterministic map §4 | derived, never hand-set |

**Refused (fake precision):** a single composite "progress score"; per-hypothesis posterior probabilities we can't defend; Expected Value of Information in currency-of-experiments (we *do* keep its qualitative cousin — "which axis discriminates most" — because the fan-out shape already encodes it). The user's brief explicitly licenses this refusal: *"If quantitative scoring is weak, prefer qualitative state machines."*

The one genuinely quantitative anchor we already own is the **Beta-Binomial posterior + 95 % credible interval** from `build_experiment_indexes.py` (`claim_evidence.v1.json`). CI *width* is a defensible per-claim reducible-uncertainty proxy; narrowing CI over time is a legitimate secondary momentum signal, and it is already computed — no new statistics invented.

---

## 3. Governance rules

The dashboard is a **derive-only consumer**. It has authority over nothing.

1. **Never a gate, always exits 0.** Same contract as `generate_closure_snapshot.py`. A red momentum panel never blocks a commit, a promotion, or a runner.
2. **No write-back into `claims.yaml` or the closure map.** Momentum classes, hypothesis states, and decision-readiness states are stored in a *separate* ledger (`hypothesis_space.v1.json`) and never mutate claim `status`/`live_status`. Closure conservatism is structurally protected because the new signal lives in a different file the closure pipeline never reads.
3. **Hypotheses are pre-registered.** A hypothesis enters a question's tree *before* its discriminating experiment runs — sourced from an autopsy's `fanout_recommendation` (or a manually-registered enumeration for non-fan-out questions). The registration-time denominator is **frozen** as `initial_frozen_count_at_registration` and never changes.

   **Labelled fan-out carve-out (GOV-FANOUT-1, adopted 2026-07-18).** An existing, already-adjudicated question's hypothesis set *may* legitimately grow when a GOV-FANOUT-1 discrimination portfolio enumerates new rival explanations as earlier axes are eliminated — but **only** when all three hold: **(a)** every new leg's `pre_registered_utc` precedes the `resolved_utc` of its adjudicating run (no leg is added after the evidence that adjudicates it is in) — and because `pre_registered_utc` is **self-reported and written into the registry after the fact**, a leg that appears to have been added post-resolution clears only on a **git-witnessed** `pre_registration_source` (see rule 5, buckets f/g); **(b)** the growth is recorded as a machine-readable entry in the question's `fanout_growth_events[]` naming the autopsy that opened the portfolio (`fanout_source`) and listing the added `hids`; **(c)** `initial_frozen_count_at_registration` is preserved separately so the reduction ratio can be reported **both ways**. Growth satisfying (a)–(c) is **ADVISORY** (labelled fan-out), not a violation. Growth that is unaccounted, unlabelled, or retro-padded remains a **real bucket-(b) violation**.

   **The load-bearing caveat.** A growing denominator is itself a scientific signal, and it points the *wrong* way: a campaign that keeps inventing new candidate explanations as it eliminates old ones is **failing to converge**. Because the denominator grows mostly by legs that are then eliminated, it *inflates* the headline narrowing ratio precisely when the campaign is doing worst. Labelling growth makes it auditable; it does not make it good. The Narrow dimension therefore reports surviving/original **and** surviving/current-including-fan-out — `net_narrowing_ratio` and `bits_removed_vs_registration` against the frozen registration denominator, alongside `fanout_added` and the `not_converging` flag (set whenever `fanout_added > 0`) — so the signal stays visible rather than being laundered into an improved ratio. The authoritative wording is the `labelled_fanout_growth` invariant in `hypothesis_space_registry.v1.json`; this doc mirrors it.
4. **Elimination bar = closure bar.** A hypothesis flips to `eliminated` only on an **adjudicated `weakens`** with a **passed negative control** and `non_degenerate: true`. A vacuous pass or a starved run (750-style) narrows nothing — it advances Decision Readiness *backwards* (surfaces an observation bottleneck), which is the honest reading.
5. **Anti-Goodhart audit.** A standing check (`check_hypothesis_space_integrity.py`, sibling of `check_closure_drift.py` and `check_granularity_debt_recurrence.py`) flags four buckets: **(a)** `a_unbacked_drop` — any question whose surviving-count dropped with no adjudicated `weakens` behind it; **(b)** `b_enlargement` — post-hoc enlargement of a frozen initial set (retro-padding, or `initial_frozen_count` disagreeing with the enumerated legs); **(c)** `c_confirmed_no_control` — `confirmed` nodes lacking a passed control; **(d)** `d_bar_violation` — an `eliminated`/`split` node missing the elimination bar of rule 4. Flags are advisory, printed, non-blocking; the script always exits 0.

   Four further buckets are **ADVISORY — reported in their own sections and never counted as flags**:

   - **`e_labelled_growth`** — growth of an existing question's set satisfying conditions (a)–(c) of the carve-out in rule 3. Never a bucket-(b) violation; growth failing any condition falls through to (b).
   - **`f_unverifiable` / `g_witnessed` — git-witnessed pre-registration.** `pre_registered_utc` is self-reported and written after the fact, so invariant condition (a) is trivially satisfiable by choosing a convenient earlier timestamp — *no audit reading only the registry can detect back-dating*. The witness closes this: git is asked when the claim to have pre-registered actually became **durable**, and that date is compared against the run it adjudicates. The honest case **self-clears without human adjudication** (its autopsy artifact was committed before the run resolved) → `g_witnessed`; the back-dated case cannot manufacture a commit → `unwitnessed`, which routes into bucket **(b)** as a real violation. Degenerate cases — no git history yet, wholesale file rewrite, git absent — report as the quiet `f_unverifiable` state, never as a violation.
   - **`h_fanout_recurrence` — the escalation clause (`FANOUT_RECURRENCE_N = 3`).** Conditions (a)–(c) make an *individual* growth event legitimate, but legitimacy is per-event and therefore says nothing about **recurrence**: a question can fan out indefinitely, clearing every check every time, while its denominator outruns its eliminations. When one question reaches 3 distinct labelled portfolios (keyed on `fanout_source`), an **ACTIONABLE** overlay fires — the signal being that the question may be **mis-posed**. Routing only; promotes/demotes nothing, never gates.

   **Do not read a clean advisory section as an all-clear.** That is the alarm-fatigue vector turned on the rule itself: a recurring advisory with a plausible narrative attached ("legitimate labelled fan-out") gets accepted by default. `h_fanout_recurrence` exists to close that asymmetry, and it is deliberately **not** redundant with GOV-DIAG-1 — that rule counts pure-diagnostic *no-verdict* autopsies, whereas fan-out recurrence is the opposite signature: every run reached a verdict and eliminated a leg, so the chain is invisible to the no-verdict counter by construction. A campaign can hold perfect GOV-DIAG-1 hygiene and still never converge.

   **Attribution rule for the time series.** A rise in `total_initial` between two snapshots is attributed to labelled sources landing in that window — new-question registrations plus `fanout_growth_events[]` legs. If the attributable leg count covers the rise, it is reported as advisory; any unattributed remainder is a bucket-(b) violation for the legs that enlarged the frozen denominator unlabelled.
6. **Human owns the decision.** `decidable_now → decided` is only ever set by a `decision_log.v1.jsonl` entry (actor = a person), never auto-derived. The dashboard can say "decidable," never "decided."

---

## 4. Update rules after each experiment

Runs at the **same adjudication moment** as governance (`/failure-autopsy` → `/governance`), reading the artifacts those steps already produce — no new human step.

For each newly-adjudicated run:

**Step A — classify momentum** (deterministic map):

| Signal | Momentum class |
|--------|----------------|
| `outcome PASS` + `evidence_direction supports` | **confirmed** |
| adjudicated `weakens` + control passed | **ruled out** |
| `recommended_epistemic_category measurement_test_design_defect / measurement_gap` (re-queue fixes a control) | **control repaired** |
| `measurement_degeneracy / measurement_artifact` resolved | **measurement improved** |
| `non_contributory` that eliminates a specific fan-out leg / discrimination split | **hypothesis narrowed** |
| substrate landed via `/implement-substrate` | **implementation completed** |
| `evidence_direction inconclusive` | **inconclusive** |
| `non_degenerate: false` / `precondition_unmet` / vacuous_pass | **underpowered** |

**Step B — update the hypothesis tree.** Locate the run's target hypothesis (via `queue_id`→`leg`, or `claim_ids`). Apply the state transition from §1. `split` spawns pre-registered children. `non_contributory`/`inconclusive`/`underpowered` leave the tree's *counts* untouched (they still appear in the feed).

**Step C — recompute per-question rollups.** Surviving count, reduction ratio, entropy proxy, decision-readiness state, decision distance.

**Step D — snapshot the project curve.** Append `(date, total_surviving, closure_pct, build_pct)` to the time series so the dual-line chart gains a point. This is the artifact that makes "closure flat, understanding advancing" self-documenting.

**Step E — run the anti-Goodhart audit** (§3.5), print flags.

All five steps are pure functions of files that already exist (`failure_autopsy_*.json`, manifests, `claim_evidence.v1.json`, `substrate_queue.json`, closure frontmatter). The only *new* persistent artifact is `hypothesis_space.v1.json` + its append-only time series.

---

## 5. Mock-up

Delivered as an interactive HTML dashboard (published artifact). It is populated with **real current data** — the MECH-457 competence-floor fan-out, the INV-088/089/090 ceiling/driver split, SD-024/025, the live 737/738/739 front, and MECH-232's genuine promotion — so it doubles as a validation that the four dimensions actually separate on today's project state.

Layout, top to bottom:
1. **Four-needle header** — Build / Prove / Narrow / Decide, each an independent gauge, captioned with its distinct question.
2. **Hero dual-line chart** — cumulative surviving-hypotheses (falling) over a flat closure %, captioned *"closure static — understanding advancing."*
3. **Shrinking hypothesis tree** — the live competence-floor question, seven leaves collapsing to one synthesis, colour-coded by state.
4. **Decision-readiness cards** — one per major question, state pill + evidence decile bar + decision distance.
5. **Scientific Momentum feed** — recent runs, each with its class chip and the one line of *what it moved*.

---

## 6. Coexistence with the existing closure map

- **Two pages, one nav.** New `progress.html` served exactly like `/machines` (`serve.py:5797` pattern) + `read_progress()` + `/api/progress`; a static Pages mirror under `docs/assets/data/progress.v1.json` via `build_site_visualizations.py`. Linked from the explorer "More ▾" menu next to **Closure 🧩**.
- **Closure stays the source of truth for "done."** The progress dashboard *embeds* the closure needle (Dimension 2) read-only and links out to `/closure` for the authoritative node-by-node view. Nothing in the closure pipeline changes.
- **Division of labour:**
  - *Closure map* answers **"how many claims have been completed?"** — conservative, promotion-gated, the record.
  - *Progress dashboard* answers **"how much closer are we to understanding REE?"** — includes build-without-proof and narrowing-without-closure, the leading indicator.
- **The hand-off is explicit.** When a hypothesis reaches `confirmed` and its claim clears the promotion gate, Dimension 3/4 hand it to Dimension 2 — the momentum feed's `confirmed` entry links to the closure node it eventually becomes. No double-counting: a promoted claim's hypotheses are marked `decided` and drop out of the surviving-count.
- **CURRENT_FRONT.md gains one line** — the surviving-hypothesis count on the live question — so the existing "single live front" doc points at both maps.

### Build path (if approved)
1. `scripts/build_hypothesis_space.py` → `evidence/planning/hypothesis_space.v1.json` (+ append-only time series). Derive-only, exits 0. Registered as a `closure_plan`-sibling generation `meta`, runs in `governance.sh`.
2. `read_progress()` in `serve.py` + `/api/progress` + `/progress` route (copy the 12-line `/machines` block).
3. `progress.html` (the mock-up, wired to `/api/progress`).
4. Static mirror in `build_site_visualizations.py`.
5. Anti-Goodhart audit `scripts/check_hypothesis_space_integrity.py` (sibling of `check_closure_drift.py`).

No change to `claims.yaml`, the closure weights, the evidence scorer, or any promotion gate. The new signal is strictly additive.
