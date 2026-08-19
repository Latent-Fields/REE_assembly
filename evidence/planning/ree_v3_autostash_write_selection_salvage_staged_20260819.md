# ree-v3 autostash-pop residue: the stash holds UNLANDED SUPERSEDING work

**Status: RESOLVED 2026-08-19T17:06Z. The Section 7 decisions were taken and executed the same day; `stash@{0}` is RETAINED, not integrated.** The body below is preserved verbatim as the 07:55Z record -- do not read its "UNLANDED" framing as current.

## 0. Resolution (appended 2026-08-19T17:06Z, session `holding-for-direction-540de6`)

This doc was written at **07:55Z**, ~8h BEFORE the disposition it asked for was executed. Its
headline ("the stash holds UNLANDED SUPERSEDING work") was true when written and is **no longer
current**. Section 7's two options were resolved as a **third path**, on evidence:

| Section 7 asked | What happened |
|---|---|
| 1. Land the stashed four-mode implementation + its contract? | **Partly.** `refractory` landed as an ADDITIONAL default-off mode (ree-v3 `692f852`, 15:56Z, chip `chip-20260819-contextmemory-add-refractory-mode`) -- as an ELIGIBILITY rule ORTHOGONAL to the landed `contextmemory_write_usage_balancing` SCORE rule, composing rather than replacing it. The four-mode enum was NOT adopted wholesale. |
| 2. Or revise/abandon, and drop `stash@{0}`? | **Revised, and the stash is RETAINED (not dropped).** `gumbel` was rejected on the stashed work's own measurement. |

**What landed, verified 2026-08-19T17:06Z against `origin/main`:**

- `contextmemory_write_selection` = `"argmin"` | `"refractory"`, `contextmemory_write_refractory_k`, alongside `contextmemory_write_usage_balancing` / `_usage_bias_weight` / `_usage_decay`. The stash's `contextmemory_write_usage_weight` landed under the clearer name `_usage_bias_weight`.
- `tests/contracts/test_contextmemory_write_address_selection.py` -- the contract Section 4 reports as untracked-and-unlandable **is on origin**, and is RICHER than the stashed 23: **26 tests**, including `test_refractory_preserves_content_conditioning`, `test_refractory_occupancy_is_content_determined_and_the_bias_is_not`, `test_landed_usage_balancing_is_a_fixed_cycle_and_refractory_is_not` and `test_the_conscience_bias_subsumes_the_refractory_mask_at_default_weight`. So Section 4's coupled-set (a2) concern is **discharged**: implementation and contract landed together.
- The Section 3 measurement table is recorded in `evidence/planning/contextmemory_write_selection_comparison_20260819.md` and was **independently re-verified** by `chip-20260819-contextmemory-writesel-verify-measurement` -- exact agreement on `argmin`/`refractory` cosine and Jaccard and on `gumbel` Jaccard **1.000**, with one small discrepancy on `gumbel` occupied-slot cosine (+0.7525 staged vs **+0.7325** re-measured, -0.020). The load-bearing finding is unaffected.

**Symbol containment of `stash@{0}` against `origin/main` (2026-08-19T17:06Z):** the only identifiers present
in the stash and absent from origin are `contextmemory_write_gumbel_{tau_init,tau_min,anneal_steps}`
and `contextmemory_write_usage_weight` (renamed). I.e. **the sole unlanded content is the `gumbel`
write mode** -- the mode the stash's own MEASURED WARNING says makes the bank content-blind
(cluster Jaccard **1.000**, addressing destroyed). It was dropped deliberately, on its own evidence.

**Therefore: DO NOT re-apply `stash@{0}`.** Re-applying it would re-add the rejected `gumbel`
mode, rename `_usage_bias_weight` back to `_usage_weight`, and revert the orthogonal-composition
refactor to a mutually-exclusive four-value enum -- a regression, not an integration.

**Preservation, verified 2026-08-19T17:06Z (quadruple):** `stash@{0}` intact; local tag
`stash-archive/20260819-dd4b0a4`; and **on origin** as
`ree-v3` `integration/contextmemory-write-selection-436f-salvage` -> `0d7ea5b`, whose parent is
`dd4b0a4d68` **verbatim**. So the stash content survives a `git gc` and is reachable from any box.

**Known follow-on, already owned:** `audit_stashes.py` and the hygiene tick still re-flag this
dispositioned entry as `HAND-AUTHORED CONTENT` at every session close (it did so again at this
session's close, which is how this refresh was prompted). That is tracked by the open chip
`chip-20260819-audit-stashes-suppress-dispositioned-retain` -- not re-chipped here.

---

Written by chip `chip-20260819-reev3-autostash-pop-conflict-residue`, 2026-08-19T07:55Z, on `DLAPTOP`.

---

## 1. Headline -- the dispatch brief's premise was INVERTED

The chip brief stated, as precondition 2 for clearing the residue:

> HEAD is 76cbf844 ... i.e. the work the stash residue duplicates is ALREADY LANDED AND PUSHED.

**That is false.** The stash does not duplicate what landed. It holds a **later, redesigned,
independently-measured implementation that supersedes the landed one** -- and whose own inline
measurement table says the approach that landed makes the target DV *worse*.

Nothing was lost: the conflict was cleared narrowly (`git checkout HEAD -- <2 files>`), which does
not touch the stash. But the stash **must not be dropped**, and the residue must not be read as
"stale duplicate of trunk".

`scripts/audit_stashes.py` independently grades the entry
**`HAND-AUTHORED CONTENT -- must be read by a human before anything is dropped`** (4 of 4 paths
outside the derive-only allowlist).

## 2. What is actually in each place

Subject: `ContextMemory` write-address selection, substrate_queue
`contextmemory-write-path-addressing-degeneracy` (severity `corrupting`), V3-EXQ-436e/436f follow-up.

| | **`origin/main` @ `76cbf844`** (landed) | **stash `dd4b0a4`** (UNLANDED) |
|---|---|---|
| API | `contextmemory_write_usage_balancing: bool`<br>`contextmemory_write_usage_bias_weight: float` | `contextmemory_write_selection: str` -- enum `argmin`/`refractory`/`usage`/`gumbel`<br>`contextmemory_write_refractory_k: int = 2`<br>`contextmemory_write_usage_weight`, 3x `write_gumbel_tau_*` |
| approach | single DeSieno-1988 "conscience bias" usage penalty | four selectable modes, invalid mode raises |
| methods | -- | `_select_write_slot`, `_record_write`, `last_write_index`, `occupied_slots()` |
| measurement | none inline | full 5-seed/3000-write table inline |
| contract test | none | `tests/contracts/test_contextmemory_write_address_selection.py` (23 tests) |

Diff sizes, stash vs HEAD: `config.py` +42/-61, `e1_deep.py` +46/-185 (i.e. the stash is
substantially the larger implementation).

## 3. The load-bearing scientific claim in the unlanded work

Verbatim from the stashed `config.py`:

> **MEASURED WARNING** -- `"usage"` and `"gumbel"` reach full occupancy by making the bank
> CONTENT-BLIND, so they satisfy the registered `n_occupied` floor while making the
> differentiation DV WORSE. On a 2-context stream (5 seeds, 3000 writes): mean occupied-slot
> cosine similarity (LOWER = better) legacy +0.6060, refractory k=2 +0.5919, gumbel+usage
> +0.7525; and cluster slot-set Jaccard overlap (LOWER = more context-conditioned) legacy 0.329,
> refractory k=2 0.364, gumbel+usage **1.000** (i.e. both contexts write to the SAME slots --
> addressing destroyed). Do not select `"gumbel"`/`"usage"` on the strength of the occupancy
> number alone.

The stashed work's recommended mode is **`refractory`** (the only mode that preserves
content-addressing). The landed `usage_balancing` is a **usage-penalty** mechanism -- the family
this measurement warns against. The unlanded contract pins the warning explicitly
(`test_gumbel_is_not_content_conditioned`, `test_recommended_mode_beats_noise_modes_on_context_conditioning`).

**This is a governance-relevant disposition, not a merge chore.** It is left entirely to the user.
No reconciliation was attempted.

## 4. The untracked contract test -- CLAUDE.md remedy (a2), but in the OPPOSITE direction

The brief asked whether `tests/contracts/test_contextmemory_write_address_selection.py` (untracked,
15,498 bytes, mtime 2026-08-18 23:14) is an unlanded assertion partner of the landed `76cbf844`
repair, per remedy (a2).

**It is an assertion partner -- of the STASHED implementation, not the landed one.** Measured
against the current (HEAD) tree:

```
accepts write_selection      : False
accepts write_refractory_k   : False
has occupied_slots()         : False
has last_write_index         : False
accepts write_usage_balancing: True     <- the landed API
```

23 tests collect (collection only imports the module) but every one calls the absent API.

**So it was deliberately NOT landed.** Landing it alone would put a red contract on `main` for
everyone -- the exact coupled-set breakage (a2) exists to prevent, arrived at from the other side:
here the *implementation* half is the unlanded one. The correct pairing is
stashed-implementation + this contract, landed together, and that is a user decision (see §3).

Absent from `origin/main` and from **all** of history (`git log --all` empty for the path) -- it
existed **only** as an untracked file on this one Mac, with no git object at all.

## 5. What was done

1. **Preserved first, before touching anything.** Pushed to `ree-v3`
   `integration/contextmemory-write-selection-436f-salvage` -> **`0d7ea5b`**
   (parent `dd4b0a4` = the stash commit verbatim; the salvage commit adds the untracked contract).
   Recoverable from any box now.
2. Local archive tag `stash-archive/20260819-dd4b0a4` (belt-and-braces; local-only).
3. **Cleared the residue narrowly**: `git checkout HEAD -- ree_core/utils/config.py
   ree_core/predictors/e1_deep.py`. Never `checkout -- .`, never `reset --hard`.
4. **Unstaged the `.ua/` pop residue** (`git reset -q --`, index only, worktree untouched).
   `.ua/knowledge-graph.json` + `.ua/meta.json` had been left **staged** (`M `) by the failed pop,
   byte-identical to the stash version and differing from HEAD -- i.e. armed to be landed by the
   next bare `git commit` in that shared checkout, under an unrelated message. Content is
   triple-preserved (stash, salvage branch, still on disk).
5. **Did NOT drop the stash.** `stash@{0}` is intact.

**Verified after:** no `UU`; nothing staged; `HEAD == origin/main` (ahead=0 behind=0);
`import ree_core.utils.config` and `ree_core.predictors.e1_deep` both OK; `py_compile` clean;
zero conflict markers under `ree_core/`.

Residual, by design: ` M .ua/*` (unstaged) and `?? tests/contracts/...` remain in the shared
checkout, deliberately left as-is pending §3.

## 6. Impact that was cleared

`config.py` carried conflict markers, so `import ree_core.utils.config` raised `SyntaxError`.
That blocked **every** experiment smoke test, every dry-run, and `precommit_contracts.sh` on this
Mac -- silently, with nothing auditing it. Introduced by the runner's
`git pull --rebase --autostash` at 2026-08-19T04:00:23Z; found ~3.5h later by an unrelated chip
that it had blocked.

## 7. Decisions for the user

1. **Land the stashed four-mode implementation + its contract?** (§3 says the landed approach is
   the measured-inferior one.) If yes, it is a reconciliation onto `76cbf844`, not a clean apply --
   the stash is based on `f7a6e9c`, which predates HEAD.
2. **Or revise/abandon it**, and drop `stash@{0}` -- safe now that `0d7ea5b` is on origin.
3. Either way the residue is cleared and the Mac is unblocked; neither is urgent.
