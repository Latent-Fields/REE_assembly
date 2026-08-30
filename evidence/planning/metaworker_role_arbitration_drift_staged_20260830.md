# Metaworker role-arbitration drift: monitoring does not follow the restructure

**Status: AWAITING USER REVIEW**

Raised by `/metaworker-learning`, session `metaworker-learning-rolearbiter-20260830`,
2026-08-30T06:16Z (Mac, `DLAPTOP`). Sister-skill handoff point:
`.claude/skills/metaworker-repair/SKILL.md` Step 5 (2nd occurrence of the same root
cause -> stop patching, design).

**Nothing is on fire.** Verified live on `ree-cloud-4` at 2026-08-30T06:19Z:
`ree-role-arbiter.timer` enabled+active, ticking every ~2 min, and all three deployed
wrapper scripts byte-identical to their tracked `origin/main` copies. This is a
prophylactic coverage finding, not an incident report.

---

## 1. The recurrence, and why it is one root cause and not two symptoms

`scripts/ree_runner_failsafe.py` keeps a fire counter (`~/.ree_metaworker/runner_failsafe_fires`,
currently **4**) and escalates in its chip prompt on each firing. Four fires:

| # | Date | Chip | Verdict |
|---|---|---|---|
| 1 | 2026-08-18 | `chip-20260818-cloud4-runner-failsafe` | **Not an occurrence** -- deliberate tests by the session that built the failsafe; withdrawn. |
| 2 | 2026-08-20 | `chip-20260820-cloud4-runner-failsafe` | **Not an occurrence** -- deliberate fleet-wide dispatch pause after a weekly usage limit; the failsafe behaved correctly. |
| 3 | 2026-08-23 | `chip-20260823-cloud4-runner-failsafe` | **Occurrence 1.** |
| 4 | 2026-08-29 | `chip-20260829-cloud4-runner-failsafe` | **Occurrence 2.** |

Per Step 1's counting rule (same root cause, not same symptom; occurrences counted from
resolution notes, not chip existence), 2 and 2 only. That meets the default threshold of 2.

**Occurrence 1 (2026-08-23).** `decide()` inferred "the metaworker healthily owns the box"
from `ree-metaworker.timer` being active. That proxy went permanently, silently false when
the resident Dispatcher timers were retired fleet-wide (`check_metaworker_timer_state.py`:
`retired_at=2026-08-23T09:55:45Z`). The `not timer_active` branch then fired
unconditionally on every runner-down state. Fixed `REE_Working 1d1f2374` by consulting
`metaworker_role_verdict.decide()` directly instead of proxying.

**Occurrence 2 (2026-08-29).** That arbitration was relocated into
`ree-metaworker-healer.sh` on 2026-08-26 (`chip-20260825-cloud4-arbitration-into-healer`)
and inherited the Healer's **hourly** cadence -- an interval chosen to bound an unrelated
cost (the Healer pays a `claude` invocation, ~117k-token context floor, per repair cycle;
arbitration pays none). Measured over 2026-08-26 -> 2026-08-29: **0 `systemctl` start/stop
actions in ~70 hourly Healer ticks.** Every real role transition in that window was
performed instead by the 15-minute failsafe poll -- the backstop silently became the
primary. Fixed by extracting `ree-role-arbiter.{sh,service,timer}` onto its own 2-minute
cadence.

**Why one root cause.** The two mechanisms differ (a stale boolean proxy; a cadence
mismatch) but the generating condition is identical and the second was *caused by the
remediation of the first being moved*:

> The component that owns runner-ownership arbitration has been restructured three times
> (Dispatcher wrapper -> Healer block -> dedicated arbiter unit). Every purpose-built
> checker is pinned to a **named component**, so each restructure moves the load-bearing
> logic out from under the name and leaves the checker asserting something true about a
> component that no longer matters. Nothing asserts the *invariant*; the only thing that
> ever noticed was a symptom counter on a watchdog.

**The failsafe is not a sound detector for this class, and that is the argument.** In
occurrence 1 the failsafe fired within ~5 minutes of the retirement -- but it fired
*because its own predicate had broken*, restarting the runner against a possibly-healthy
metaworker, i.e. exactly the contention its documented negative control exists to prevent;
root cause then took until 2026-08-25 (~2.4 days). In occurrence 2 the failsafe did not
detect anything at all: it silently absorbed the primary's job for ~3 days. So in one case
the detector was broken by the restructure and in the other it was masking it. Neither is
detection.

**The prose already predicts occurrence 3.** `ree_runner_failsafe.py`'s current docstring
ends: "If this fires repeatedly again, check FIRST whether `ree-role-arbiter.timer` is
enabled and active on this box, and whether `~/ree_role_arbiter.log` shows it running."
The author of fix 2 correctly anticipated the next recurrence shape and wrote the
diagnostic as **advice for a future human** rather than as a check. That is the
`/failure-autopsy` MOVE-3 re-derive-brake trigger in its purest form.

---

## 2. Current coverage, measured

| Checker | Asserts about | Status |
|---|---|---|
| `scripts/check_metaworker_timer_state.py` | `ree-metaworker.timer` | Points at the **retired** dispatcher timer. |
| `scripts/check_metaworker_wrapper_deploy.py` | `ree-metaworker-dispatch.sh` **only** (`INSTALLED_PATH` is a single hardcoded string) | Does not cover `ree-metaworker-healer.sh` or `ree-role-arbiter.sh`. |
| `scripts/hygiene_routine_tick.py` | 25 sources | Neither checker above is wired into it. |
| anything | `ree-role-arbiter` | **Nothing.** Zero references repo-wide outside its own deploy files and one docstring mention. |

The arbiter's only externally visible output is `~/ree_role_arbiter.log` on the box: from
the Mac, or from origin, there is today **no way to tell whether arbitration is alive or
whether its verdict matches reality** without an interactive ssh.

---

## 3. Proposed durable fix -- three parts, and the constraint that shapes them

### The sharpest design constraint, from this session's own live measurement

`ree-role-arbiter.log` on `ree-cloud-4` shows **336 `yielding-to-experiment` verdicts and
0 transitions across ~11.5 hours (341 ticks)** as of 2026-08-30T06:19Z. That is
**correct** -- the box has held a claimed experiment throughout, so "yield" is the right
verdict every tick.

This matters because "0 actions in N ticks" is precisely the measurement that diagnosed
occurrence 2. **It is a valid forensic signal and an invalid detector.** A monitor that
asserts "the arbiter has acted recently" would false-positive continuously, right now --
and the fleet has already paid for that mistake once: the 2026-08-19 -> 08-22
orchestrator-STALE chip storm (~16 `metaworkerrepair-*-stale*` chips in ~72h, the large
majority resolved as non-fault) came from thresholds tuned against the wrong cadence. Do
not re-run that experiment.

### Part 1 -- assert the invariant, not the component

The one assertion that is true regardless of which unit implements arbitration:

> the box's actual `ree-runner` systemd state agrees with `metaworker_role_verdict.decide()`
> recomputed now, **and** some mechanism has re-evaluated it within a bounded window.

Clause (a) is cadence-agnostic and component-agnostic, so it survives the next
restructure -- which is the whole point. Clause (b) needs a freshness signal; the arbiter
currently publishes none, so this part includes a small addition: the arbiter writes a
verdict record (timestamp, verdict, action-taken-or-none) that reaches somewhere readable
off-box. Preference, to be decided at build: fold it into the existing orchestrator
heartbeat so it reaches `origin/master` and is checkable from the Mac with no ssh at all.

### Part 2 -- close the enumeration gap so the *next* wrapper is not born uncovered

Generalize `check_metaworker_wrapper_deploy.py` from one hardcoded `INSTALLED_PATH` to
**enumerate** `ree-v3/coordinator/deploy/*.sh` and check every deployed wrapper, plus a
strays scan flagging installed `/usr/local/bin/ree_*.sh` with no tracked counterpart.

This is deliberately the same fix *shape* as two existing precedents rather than a new
invention: `remote_pytest.sh --selftest` stopped checking a hardcoded list of test roots
and started enumerating every `test_*.py` in the tree, failing if any is unreachable from
the default; `audit_vendored_copies.py` pairs its `VENDOR_SETS` registry with a strays
scan for an unregistered fourth copy. Both were adopted after a hardcoded list silently
went stale.

### Part 3 -- route it, or it does not count

Wire the result into `hygiene_routine_tick.py` as a new source (Mac-gated, materiality
threshold, absence-done and `scan_ok` semantics per the file's conventions), so a finding
mints a chip. Precedent and cautionary tale in one: **source 24** (landed 2026-08-29)
exists because `daemon_code_drift.py` had been running every 3 minutes for weeks and was
**display-only** on `FLEET_STATUS.md` -- the hub `ree-runner` ran 27.4-day-old bytecode
with its DRIFT row public the whole time. Parts 1 and 2 without Part 3 reproduce exactly
that failure.

---

## 4. Held-out check (CLAUDE.md "General Rules")

Adapted as the rule requires for a tooling change rather than a wording change: would the
proposed detector have given a **different and correct** answer on cases it was not written
from? Five found; all non-degenerate (current behaviour on each is "nothing fires").

1. **`remote_pytest.sh` default test roots (2026-07-27, twice).** Collection pinned to a
   hardcoded path list the tree outgrew; a test file the default did not name was never
   run, found by accident months later. Old: green. New (Part 2's enumeration invariant):
   fails, naming the uncovered path. **Differs.**
2. **`audit_vendored_copies.py` (2026-07-22 -> 07-28).** A banner asserted "shasum over all
   three must match"; nothing verified it; the three drifted from the day the banner was
   written and stayed drifted six days, found incidentally during unrelated triage. Old:
   nothing. New (Part 2's strays scan + enumeration): named finding. **Differs.**
3. **`audit_hook_gating.py`'s latent check (2026-08-15).** The live check passed because
   the callee happened to return 0; only the structural necessary-condition test catches
   the latent case. Directly analogous: Part 1 is the live check, Part 2 the latent one,
   and this case is the evidence that **both** are needed. **Differs.**
4. **`chip-20260823-dispatch-preflight-only-checks-umbrella`.** Dispatch freshness preflight
   scoped to the umbrella while the dispatcher's correctness also depended on other repos'
   freshness -- a dispatcher could hold a stale WORKLIST. Same class: a check pinned to one
   named component while the architecture grew others. **Differs.**
5. **Hygiene tick source 24 (2026-08-29).** Detector existed, ran every 3 min, was
   display-only; 27.4-day-old bytecode ran in production with the DRIFT row public. Old:
   signal exists, no work minted. New (Part 3): chip. **Differs** -- and this is what makes
   Part 3 non-optional rather than polish.

**Negative control A -- do not read this as "replace targeted checks with generic ones."**
`chip-20260821-metaworkerrepair-cloud5-timer-nextelapse-infinity`: a narrow,
component-named checker (`check_metaworker_timer_state.py`) caught a real fault that a
generic invariant would have missed, because it encoded specific knowledge
(`NextElapseUSecMonotonic=infinity` on a timer that reports `enabled`). Part 2 **adds**
enumeration coverage beside targeted checks; it retires none of them. That checker's
now-retired subject is a flag for judgement, not an automatic deletion -- `/account-handover`
still re-enables that timer, and the checker already cross-references
`scripts/dispatcher_pauses.json`.

**Negative control B -- the false-positive shape this must not reproduce.** Stated in
full in section 3: "0 actions in N ticks" is forensics, not a predicate, and the
2026-08-19 -> 08-22 STALE chip storm is the measured cost of getting that wrong.

**Honest counterweight, per the rule.** This is prophylactic. The failsafe self-healed and
chipped on both occurrences; nothing was lost either time, and the current arbiter has been
correct for ~12h. Part 3 adds an ssh probe to a tick that already carries 25 sources; Part 2
broadens a checker that today has one narrow, well-tested job, and broadening a tested
narrow thing is how narrow tested things acquire bugs. The held-out check itself cost this
session real cycles. The case for building anyway is that the generating condition -- the
role machinery being restructured again -- is not hypothetical: it has happened three times
in seven days, and the current docstring already tells a future session which log to go read
by hand when it happens a fourth time.

---

## 5. Options for the decision chip

- **A -- build all three parts.** Highest cost, closes the class.
- **B -- Part 1 only.** The invariant + arbiter verdict publication; leaves the next
  uncovered wrapper uncovered.
- **C -- Parts 2+3 only.** Enumeration + routing, no new invariant; cheapest, catches
  deploy drift but not "arbitration is alive and consistent".
- **D -- hold.** Record the finding, do not build. Defensible: nothing is currently broken.
