# Rule Inventory Decidability Spike

**Chip:** `chip-20260818-rule-inventory-decidability-spike`
**Date:** 2026-08-19
**Verdict: TRACTABLE FOR SPOT-CHECKS, NOT TRACTABLE AS A CORPUS-WIDE MECHANICAL PASS.**

Ten adversarially-chosen CLAUDE.md rules were classified by real evidence
(grep, git log, git blame, live hook-file checks, small measurement scripts)
rather than by inspection alone. All ten reached a classification — the (D)
rate is not the blocker. The blocker is **cost and shape**: each rule needed
a *different* evidence source (a hook file's presence, a GitHub Action's
effect on `git branch -r`, a corpus-wide grep with a hand-picked character
set, a `git log -S` search, a timestamp-correlation script), so no batching
or template evidence-gathering procedure applies across rules. One rule
(timestamp discipline) does not have a single classification at all — it
splits by *write-path*, which means "classify this rule" is sometimes an
ill-posed question, not merely a hard one. See "Recommendation" at the end.

---

## Method

For each rule: state what evidence would decide it, go get that evidence,
record classification + confidence + time + whether I changed my mind
mid-analysis. Evidence-gathering was interactive/adaptive per rule (see
transcript); the closest thing to a "time" figure is the number of distinct
tool calls (greps/git-log queries/scripts) it took to reach a defensible
verdict, which is the real driver of wall-clock cost.

Classification legend:
- **(A) CODE-ENFORCED** — a script/hook/test already makes violation
  impossible or loud.
- **(B) ADHERED WITHOUT ENFORCEMENT** — measurably followed, no mechanism.
  Leave alone.
- **(C) VIOLATED** — real, evidenced violation exists. Only these are
  candidates for new enforcement, and even then subject to the restraint
  precedent (GOV-HELDOUT-1, `ref_move_guard.py`'s narrow predicate).
- **(D) UNDECIDABLE** — no artifact exists that could settle it either way.

## Steward overlap check (done first, per the brief)

Read `.claude/skills/steward/SKILL.md` in full before starting. **No
overlap.** Steward's ~20 chips and 8 detectors (D-001/002/006/007/008/010/
101/102) all target `claims.yaml`, `evidence/planning/*_plan.md`
`closure_plan` frontmatter, the governance-flag registry, and live git
divergence state — i.e. the *scientific claims registry*, not the standing
prose rules in `CLAUDE.md`/`SKILL.md` files. Nothing in Steward reads or
classifies CLAUDE.md rule text. This spike is not duplicate work, and the
boundary is: Steward = claims/governance-artifact hygiene; this spike =
standing-instruction-prose hygiene. They could share a *pattern*
(detector-per-defect-class, tiered escalation, suppressions) if a future
session ever builds a rules inventory, but no code or data is shared today.

---

## Per-rule table

| # | Rule (CLAUDE.md location) | Evidence sought | Evidence found | Class | Tool calls | Confidence | Mind changed? |
|---|---|---|---|---|---|---|---|
| 1 | `reference-transaction` hook blocks destructive ref moves (`git update-ref`/`reset --hard origin/*`) | Hook file present + actually wired; installed where the rule says it should/shouldn't be | `scripts/git-hooks/reference-transaction` + `scripts/ref_move_guard.py` exist, 21 tests cited. **But on THIS box (`ree-cloud-4`, a cloud worker)** `.git/hooks/reference-transaction` and `pre-push.local` are **both absent** — confirmed by direct `ls`. This matches CLAUDE.md's own instruction ("do NOT install on the hub or cloud workers") — not a gap, a documented exclusion. | **A** (scoped: Mac only, verified absent here by design) | 3 | High | No |
| 2 | `chip_ledger.py record` refuses (`die()`, exit 2) unless `--prompt` literally contains `[chip_ref: ...]` | `die(` call gated on `marker not in args.prompt` | Found at `scripts/chip_ledger.py:1993-2000`: hard `die()` with no bypass flag. Confirmed via source read, not just doc claim. | **A** (clean) | 2 | High | No |
| 3 | Trunk-only / no standing branches, enforced by `enforce-single-branch.yml` (REE_assembly, ree-v1-minimal) | Workflow file present; live effect on `origin` branch list | `REE_assembly/.github/workflows/enforce-single-branch.yml` exists. `git -C REE_assembly branch -r` shows **exactly 2 remote refs**: `origin/master` and `origin/live-status` (the documented force-push exception) — no stray feature/PR branches survive on origin, which is what the Action is supposed to guarantee. `ree-v3` and this umbrella repo (`REE_Working`) have **no such workflow** — confirmed by `find .github/workflows`. `ree-v1-minimal` isn't cloned on this box so could not be directly checked. | **A** for REE_assembly (measured), **N/A-by-design** for ree-v3 (documented exception), **absent** for the umbrella (no workflow found at all — CLAUDE.md doesn't actually claim one exists for the umbrella, so this is consistent, not a gap) | 4 | High for REE_assembly; Medium for the umbrella (absence-of-evidence) | No |
| 4 | Clinical-hours provenance guard blocks personal-identity commits/pushes Mon-Thu 09:00-17:00 / Fri 09:00-14:00 Dublin | Guard hook present on the Mac; explicitly absent on hub/cloud by stated mechanism reason (would wedge phase3 writers / metaworker) | Text confirms hook is `install_commit_guard.sh`-installed, Mac-only, deliberately excluded from `ree-worker-*`/`ree-cloud-*`. This session is itself running on `ree-cloud-4` — consistent with rule 1's direct hook-absence finding above (same install path). | **A** (Mac), **N/A-by-design** (cloud) | 1 (reused rule-1 evidence) | High | No |
| 5 | "Always get the actual current UTC time... never estimate" (Timestamps section) | Two write-paths: (a) `TASK_CLAIMS.json` `claimed_at`, written by `task_claim.py`; (b) `WORKSPACE_STATE.md` entry headers, hand-typed by the session prose | (a) `task_claim.py`'s `open`/`renew` compute `claimed_at` internally (script-side `utc_now()`), so **the session cannot get this one wrong even if it tried** — the rule is moot/enforced by construction for this path. (b) Correlated the last 5 `WORKSPACE_STATE.md`-touching commits' entry-header timestamp against the commit's own `%aI`: deltas were 0.4-1.6 minutes, 0/5 mismatches >1h. This is real adherence with **no code checking it** — nothing validates a hand-typed header against the clock. | **SPLIT: A for path (a), B for path (b)** — one rule, two classifications, genuinely not one answer | 5 | High for (a); Medium-High for (b) (n=5 spot sample, not exhaustive) | **Yes** — started assuming this was a clean (B) example, discovered mid-analysis that one write-path is actually code-enforced |
| 6 | "Claim-first, edit-last": chip prompts instruct the spawned session to open `TASK_CLAIMS.json` as its first action | Whether spawned sessions reliably comply | **CLAUDE.md self-documents a confirmed failure**, verbatim, at the exact section this instruction lives in: "Confirmed 2026-08-10: a real spawned session did not open its `TASK_CLAIMS.json` claim despite the instruction being present in its prompt. Nothing checks that a spawned session actually ran the claim command." This is the rule's own text admitting no enforcement and a real incident. | **C** (already adjudicated by the document itself; I only needed to confirm the passage exists and is not qualified away elsewhere) | 1 | High | No |
| 7 | ASCII-Only in Python Output: no em-dash/arrow/× /…/≈ in anything reaching stdout/stderr | Corpus-wide scan for the banned characters inside `print(`/f-string lines across `scripts/`, `ree-v3/`, `REE_assembly/` | Wrote a small script scanning all 2333 tracked `.py` files: **91 candidate violations**, overwhelmingly in `ree-v3/experiments/v3_exq_*.py` driver scripts (em-dashes in markdown-summary f-strings and progress prints), oldest from 2026-03-18 (rule already existed by the repo's 2026-03-25 init commit, so these were violations from day one of the rule, not pre-existing legacy). Re-ran restricted to files touched since 2026-08-01: **3 more, still nonzero**, though those three are arguably markdown-file content rather than terminal stdout (scope ambiguity in the rule's own text: "any text that reaches stdout/stderr" vs. f-strings written to a `.md` file — not the same channel). No lint anywhere enforces this; only 6 of 2333 files self-assert `.isascii()` on their own narrow output. | **C** (real, repeated, ongoing at low rate; not merely historical) | 6 | High for existence of violations; Medium for whether the 3 recent ones are in-scope (channel ambiguity in the rule text itself) | **Yes** — initially expected either clean adherence or a handful of old hits; the 91-count and the 3 post-Aug-1 hits were both larger/more current than expected |
| 8 | "Never put a scratch/one-off Python script in `/tmp`" | Whether this recurs beyond the one motivating incident | `grep` for the incident text finds exactly the one write-up (2026-08-18, `ree-cloud-5`, `/tmp/inspect.py` shadowing stdlib). No second incident found in `WORKSPACE_STATE.md` or CLAUDE.md. No lint/hook checks where scratch files get written — cannot exist as a general check (a hook can't know intent from a path alone). | **D** (leaning B) — one clean incident with no counter-evidence of recurrence is consistent with "now adhered" but is statistically indistinguishable from "hasn't happened to bite again yet"; sample size of 1 is not enough to call it (B) with the same confidence as rule 5(b)'s n=5 | 2 | Low-Medium | No |
| 9 | "Task Completion Verification": don't mark a todo/task complete until the actual output is verified | Any artifact that would show a premature "done" declaration | **None exists by construction.** `TodoWrite` state is not persisted to git, is not logged anywhere durable, and does not survive past the session that used it. There is no historical corpus to grep. This is not "hard to find evidence" — it is a rule whose only enforceable trace would be a live harness feature (e.g. a hook diffing todo state against file mtimes), which doesn't exist, and whose only textual trace in git is other rules citing near-misses in prose (e.g. the `/session-land` "satisfying the summary is not the same as running the skill" passage) — suggestive, not decisive, and about a *different* rule. | **D** (structurally, not just practically, undecidable from available evidence) | 2 | High confidence *in the undecidability itself* | No |
| 10 | "Narrow Edits Only": never run a full index/registry regen for a single-field change | Recurrence of the ~1200-file incident that motivated the rule; existence of the suggested `--only`/targeted mode | Found the cited incident is the *only* one in `WORKSPACE_STATE.md`'s ~734 lines mentioning "regen" (checked for repeat "N files instead of" phrasing — none). Checked the primary example script name from the rule's own "How to apply" (`build_experiment_indexes.py`, actual path `REE_assembly/evidence/experiments/scripts/build_experiment_indexes.py`): it does have `--index-only`, but that flag skips *categories* of derived output (backlog/proposals/gap-register), not a true single-field/single-entry regen — so the rule's own suggested mitigation is only a partial match to what it recommends checking for. | **D** (one incident, no recurrence data, and the rule's own suggested verification step is itself only partially true of its own headline example) | 4 | Medium | No |

---

## D-rate and disagreement risk

- **(D) count: 3 of 10 (30%)** — rules 8, 9, 10. One of those (9) is
  D by *structure* (no artifact could ever exist), not by insufficient
  digging — that distinction matters for a corpus-wide pass, because rule 9's
  kind of D is unfixable with more effort, while rule 8's and 10's kind might
  resolve with a longer observation window.
- **1 of 10 rules doesn't have a single classification (rule 5)** — it
  splits A/B by write-path. This is arguably a fourth failure mode beyond
  A/B/C/D: **rules whose "classify me" question is ill-posed** because the
  same prose instruction is enforced differently depending on which code
  path a session goes through to act on it. A corpus-wide inventory would
  need to decide, per rule, whether it even applies to write-paths uniformly
  before classifying — that decision itself takes investigation.
- **I changed my mind mid-analysis on 2 of 10 (20%)**: rule 5 (assumed clean
  B, found a split), rule 7 (assumed clean/rare, found real ongoing
  violations at meaningfully higher count than expected). Both times the
  correction came from *actually running a script* rather than reading
  prose or grepping for keywords — i.e., confidence from inspection alone
  would have been wrong 2/10 times in this sample.

## Timing signal

No rule was answerable from a single grep. The cheapest (rules 2, 6) took
1-2 targeted tool calls because the evidence was already stated verbatim
in the source or in CLAUDE.md's own self-documentation. The most expensive
(rule 7) took 6 calls including writing and running two small Python scripts
against the full tree, and produced a genuinely surprising, previously-
unmeasured number (91 + 3). **Nothing amortized across rules** — each
needed its own evidence *source* (a hook file, a GitHub Action's live effect,
a `die()` call site, a corpus character scan, a `git log -S`, a timestamp
correlation script), not just its own grep pattern. Extrapolating: a
corpus-wide pass over CLAUDE.md's full rule set (order ~50-100 distinct
imperative statements, on this session's own earlier crude line count) at
this observed per-rule cost is many hours of investigative work, not a
sweep a detector could run in seconds — the opposite of Steward's detector
model, where `run_detectors.py` is "~0.5-2s" precisely because each
detector's evidence source is fixed code shape, not open-ended git
archaeology.

## Restraint check against precedent

None of the (C) findings here license a new hook by themselves:

- **Rule 6 (claim-first-edit-last)** already has a documented, deliberately
  code-level fix path in progress ("`chip_ledger.py record` (or `spawn_task`
  itself) should open the claim on the spawning session's behalf" — stated
  in CLAUDE.md itself as the durable fix, not yet built). This spike adds
  no new information beyond confirming the passage is accurate; it is not a
  new finding to route anywhere.
- **Rule 7 (ASCII-only)** is a genuine new measurement (the 91+3 count did
  not previously exist anywhere in the repo) and *is* a plausible detector
  candidate — but per the restraint precedent ("a check that fires on
  ordinary work gets disabled") any such lint would need to resolve the
  scope ambiguity found above (stdout/stderr only, vs. any f-string
  regardless of destination) before it could be written narrowly enough not
  to false-positive on legitimate markdown-generation code. **Not building
  it here** — this is a probe, and per the brief a promote-worthy defect
  class is "chip it," not "build it inline." Recorded as a finding, not
  actioned.

## The RAG objection — does this evidence support or contradict it?

**Nuances it, does not contradict it.** The objection's claim is that
retrieval keyed on a reader's query cannot surface a rule for a hazard the
reader hasn't conceived of, so tripwires must stay unconditionally loaded.
Rule 6 is direct evidence *for* a related but distinct point the objection
doesn't make explicitly: **unconditional loading is necessary but not
sufficient.** The claim-first instruction is not merely loaded — in the
headless-chip case it is injected as the literal first line of the spawned
session's prompt, maximally salient — and it still gets skipped in a
confirmed instance. That is a compliance failure, not a surfacing failure,
and no retrieval strategy (RAG or otherwise) fixes a compliance failure;
only code-level enforcement does (which CLAUDE.md's own text proposes for
this exact rule). So: the objection's core argument (retrieval can't surface
unconceived hazards) stands unrefuted by this sample — nothing here tested
it directly, since all 10 rules were already known to the sessions that hit
them. What this spike adds is a second, independent reason (beyond
surfacing) that a subset of rules need to graduate from prose to code
regardless of how the corpus is organized: prose compliance is not
guaranteed even when prose is always in context.

## Recommendation

**Do not run a corpus-wide inventory.** The per-rule cost (multiple
tool calls, a bespoke evidence source each time, real risk of a wrong
snap judgment — 2/10 changed mid-analysis here) means a full pass over
CLAUDE.md's ~50-100 imperative statements would cost many hours and would
not compress into a lint/detector the way Steward's claims-registry
detectors do, because CLAUDE.md rules are heterogeneous in *what kind of
evidence would decide them* (git history, live hook files, GitHub Actions,
corpus scans, self-referential incident text, or — for a real fraction —
nothing at all). A cheaper, higher-value alternative: **spot-check
adversarially chosen rules opportunistically** (as this spike did), and
specifically **flag any rule found to be (C) VIOLATED with a real, bounded
count** (like rule 7's 91+3) as a candidate for the existing `/failure-
autopsy` or Steward `promote` pathway, rather than building a standing
classification system. The (D) rate and the split-classification case (rule
5) are themselves the strongest argument against a mechanical inventory:
a meaningful fraction of rules cannot be settled by more grepping, and at
least one demonstrates that "one rule = one classification" is sometimes
false on its face.
