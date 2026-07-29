# `experiments/` bare-name cross-module imports — corpus sweep and residual worklist

**Generated** 2026-07-29T08:15Z · **Session** `dazzling-taussig-f58f4c` (worktree)
**Worked example / fix of record** ree-v3 [`73407e22e1`](https://github.com/Latent-Fields/ree-v3/commit/73407e22e1)
(`experiments/goal_stream_stages_sd054.py` + `tests/contracts/test_goal_stream_env_seed_determinism.py`)
**Origin** noticed while wiring `--env-seed` through the SD-054 goal-stream drivers (ree-v3 `28eaea56d0`);
the knob work itself is complete and landed — this is a separate latent defect found during verification.

> **One line.** A bare-name cross-module import inside a module under `experiments/` resolves only when
> `experiments/` is itself on `sys.path`. **Nothing is broken in production** — that condition always holds
> under direct script execution, which is how `experiment_runner.py` invokes drivers. The exposure is to
> *anything that imports by the package path*: contract tests, tooling, and any future driver.
> **The corpus is in far better shape than the raw count suggests: exactly TWO modules are actually
> defective.** The corpus already carries the correct remedy in three other places — this doc's job is to
> name the two that lack it, and to stop a future session "fixing" 204 import sites that do not need it.

---

## 1. The defect, and why production never sees it

Python resolves a bare `from scaffolded_sd054_onboarding import X` only if `experiments/` is on `sys.path`.
Two ways that happens:

- **Direct script execution** — `sys.path[0]` is the script's own directory. `experiment_runner.py` runs every
  driver this way, so `experiments/` is always present. This is why the defect is invisible in production.
- **An explicit `sys.path` insert** in the importing module (the remedy — §4).

Neither holds under `import experiments.<mod>` from the repo root, so the bare import raises
`ModuleNotFoundError`.

### 1a. The second consequence, which is the dangerous one

When **both** spellings are used in one process — a test that puts `experiments/` on `sys.path` and then
imports a driver by the package path — `scaffolded_sd054_onboarding` and
`experiments.scaffolded_sd054_onboarding` become **two distinct module objects with separate module-level
state**. A monkeypatch applied to one is invisible to the other.

This was **measured, not theorised**. Before `73407e22e1`, in a process shaped like
`tests/contracts/test_goal_stream_env_seed_determinism.py`:

```
gs bare id     : 4431425072
gs package id  : 4527395664
SAME OBJECT?   : False
```

The test monkeypatched `gs` while `d622` ran the other copy. It did not *break* only because the live
patches target `ree_core.environment.causal_grid_world.CausalGridWorldV2` by string path, which has a
single identity. That is luck, not a property of the arrangement.

---

## 2. The corpus measurement (AST scan, ree-v3 `a01c797860`)

| Quantity | Count |
|---|---|
| bare-name cross-module import **sites** under `experiments/` | **204** |
| package-spelled import sites | **1619** |
| modules under `experiments/` containing ≥1 bare-name local import | **162** |
| …of those, **also** imported somewhere via the package spelling | **7** |
| …of those 7, **genuinely defective** | **2** |

So bare-name is a real minority pattern (~11%), **but it is only a defect where the two spellings meet.**
The 155 modules imported *only* bare-name are fine and must be left alone.

---

## 3. Status table — the 7 dual-spelled modules, each verified individually

Verified by running `python3 -c "import experiments.<mod>"` from the ree-v3 root, one module per process.

| Module | Bare import site | Status | Why |
|---|---|---|---|
| `experiments/_lib/goal_pipeline_tier1.py` | `:41` → `_harness` | ❌ **BROKEN** | module-level, **no** `sys.path` insert. `ModuleNotFoundError: No module named '_harness'`. Dual-spelled 25 bare / 4 package. |
| `experiments/_lib/baselines/stageh_strict_goal_isolation.py` | `:56` → `scaffolded_sd054_onboarding` | ❌ **BROKEN** | module-level, **no** `sys.path` insert. `ModuleNotFoundError`. |
| `experiments/_lib/probe_warmup.py` | `:155,162` | ✅ correct | inserts repo root + `experiments/` + `_lib/` at `:152-153` **before** the bare imports, and `:145` documents exactly why. |
| `experiments/_lib/baselines/maturation_curriculum.py` | `:146` | ✅ correct | `sys.path` insert at `:122-123`. |
| `experiments/v3_exq_603p_...diagnostic.py` | `:87` | ✅ correct | `sys.path` insert at `:78-81` (repo root **and** `experiments/`). |
| `experiments/_lib/arm_fingerprint.py` | `:478` → `_harness` | ✅ deliberate | lazy, inside `try: from experiments import _harness / except: try: import _harness`. Package spelling tried **first**. |
| `experiments/pack_writer.py` | `:641` → `_lib.manifest_core` | ✅ deliberate | same shape, docstring says so: *"across the several ways experiment scripts put experiments/ on sys.path"*. |

**Correction to an earlier reading of this sweep.** A first pass reported "2 confirmed + 5 latent". That was
wrong and the error was one of aggregation: it classified by *AST line position* without checking whether the
module had already put `experiments/` on `sys.path`, and without opening the two lazy sites. Three of the five
already carry the remedy and two are deliberate fallbacks. **The residual worklist is 2 modules, not 7.**

> The two `try/except` sites are the one place option (b) below is *correct*: they are lazy, they try the
> package spelling first, and their whole purpose is tolerating unknown caller `sys.path` states. They still
> inherit the two-identities caveat (§1a) — worth knowing, not worth changing.

---

## 4. The fix, and the one part that is load-bearing

Adopt the **package** spelling, and add a `sys.path` insert so it resolves however the module was loaded:

```python
_REPO_ROOT = str(Path(__file__).resolve().parent.parent)   # adjust .parent depth per nesting
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from experiments.<mod> import <names>   # noqa: E402
```

**The insert is not decoration.** Without it you trade one broken load order for the other: the package
spelling alone fails under `cd experiments && python3 -c "import <mod>"`. Note `_lib/baselines/` is two levels
below `experiments/` — get the `.parent` count right and *verify it*, do not eyeball it.

This is the same idiom `v3_exq_622_goal_stream_staged_sd054.py:44` already uses, and the same one the three
✅-correct rows above already carry.

### Why not the alternatives

- **(b) `try/except ImportError` covering both spellings** — clears the `ModuleNotFoundError` but deliberately
  leaves both spellings reachable, so the identity foot-gun stays armed, and *which* identity you get becomes
  dependent on `sys.path` order at first import. That is the least debuggable form of the same bug. (Correct
  only for the two intentionally-lazy sites in §3.)
- **(c) corpus-wide rewrite of all 204 sites** — no behaviour gain, a very large diff across ~1194
  mostly-frozen historical drivers, and it fights the pre-existing `validate_experiments --strict` backlog.
  **Do not do this.** 155 of the 162 modules are single-spelled and correct as they stand.

---

## 5. Residual worklist

Both items are `complicated (buildable)` — no unknown, no probe needed.

| # | Path (absolute) | Action |
|---|---|---|
| 1 | `/Users/dgolden/REE_Working/ree-v3/experiments/_lib/goal_pipeline_tier1.py:41` | `_harness` → `experiments._harness` + repo-root `sys.path` insert |
| 2 | `/Users/dgolden/REE_Working/ree-v3/experiments/_lib/baselines/stageh_strict_goal_isolation.py:56` | `scaffolded_sd054_onboarding` → `experiments.scaffolded_sd054_onboarding` + insert (**two** levels up) |

Item 1 has **29 import sites** (25 bare + 4 package); treat it as the higher-blast-radius change and run the
**full** suite for it (bare `remote_pytest.sh`, no args). Item 2 has one importer.

### STOP-CHECK before starting

```bash
BASE=/Users/dgolden/REE_Working
cd $BASE/ree-v3
# STOP if BOTH now import clean -- the work is already done.
/opt/local/bin/python3 -c "import experiments._lib.goal_pipeline_tier1"
/opt/local/bin/python3 -c "import experiments._lib.baselines.stageh_strict_goal_isolation"
# STOP if exit 3 -- another session owns these files right now.
/opt/local/bin/python3 $BASE/scripts/task_claim.py check --resources \
  ree-v3/experiments/_lib/goal_pipeline_tier1.py \
  ree-v3/experiments/_lib/baselines/stageh_strict_goal_isolation.py
```

### Verification protocol (per module touched)

```bash
# BOTH load orders must exit 0, and neither may introduce a cycle
cd /Users/dgolden/REE_Working/ree-v3             && /opt/local/bin/python3 -c "import experiments.<mod>"
cd /Users/dgolden/REE_Working/ree-v3/experiments && /opt/local/bin/python3 -c "import <mod>"
```

Then, in one process, import the module **both** ways and assert `sys.modules[bare] is sys.modules[pkg]`
(or that only one spelling loaded at all); smoke `--help` on a sample of importing drivers
(`grep -rn --include="*.py" "<mod>" .../experiments | grep -v __pycache__`); and run contracts **on a cloud
worker, never the laptop**:

```bash
/Users/dgolden/REE_Working/scripts/remote_pytest.sh tests/contracts -q   # full suite, no args, for item 1
```

Land on `ree-v3` → `main`:
`/opt/local/bin/python3 /Users/dgolden/REE_Working/scripts/ree_commit.py --repo ree-v3 --push -m "..." -- <paths>`.
`experiments/` carries a pre-existing `validate_experiments --strict` backlog on several historical drivers;
if the pre-commit gate blocks, confirm HEAD fails **identically** before reaching for `--no-verify`.

---

## 6. Optional hardening (not owed)

Nothing currently prevents a new dual-spelled module from regressing this. A `validate_experiments.py`
author-time lint could flag *a bare-name cross-module import in a module that is also imported package-spelled
somewhere, and that lacks a `sys.path` insert above it* — which is exactly the §3 predicate, and would have
found both residual items automatically. Scoped that way it fires on 2 files today, so it would land green.
Recorded as an option; **not** a blocker for §5.
