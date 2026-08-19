# ree-v3 autostash-pop residue: the stash holds UNLANDED SUPERSEDING work

**Status: AWAITING USER REVIEW.**

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
