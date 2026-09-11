# MECH-536 / MECH-535: the re-posed C1 -- from `period2_cycle_present` to period-agnostic CONFINEMENT

**Generated:** 2026-09-11T14:19:02Z
**Session:** `confident-panini-0cdba7` (chip `chip-20260910-merge-unfailable-criteria-redesign`, item 1)
**Discharges:** GFLAG-0233 (`evidence_discrepancy`, MECH-536 + MECH-535), open since 2026-09-08T18:41:59Z
**Ratified direction:** `governance_flag_adjudication_20260909.md` GFLAG-0233 **option 1**
("re-pose C1 onto a period-agnostic orbit criterion"), user-approved 2026-09-10
**Supersedes the successor recipe in:** `exq1007a_blocked_c1_satisfied_by_construction_20260908.md` section 5
(sections 5.1 and 5.3 stand; **5.2's named escape operator is refuted below -- section 4**)
**Claims:** MECH-536 (primary), MECH-535 (read-across). **Neither direction moves on this record.**

---

## 0. One paragraph

The incumbent primary criterion C1 is `period2_cycle_present == False`, and it is an arithmetic
identity of the manipulation: a k>=2 action latch never flips the action on consecutive steps, so
strict single-step alternation is structurally unreachable and C1 passes for every k at every
episode length. This record replaces it with **confinement** -- *did the trajectory stop visiting
new cells* -- which is period-agnostic, amplitude-agnostic, covers both of MECH-535's phenotypes
(limit cycle **and** boundary-press fixed point) in one measure, and, critically, **is not forced
by the latch**: the same k=2 latch reads confined on the direction-blind reader and not-confined on
an adequate representation. Every number below is measured against V3-EXQ-1007's own banked traces
and manifest, not argued. The measurement also **refutes one clause of the successor recipe this
record inherits** (section 4) and **changes what the successor experiment should ask** (section 6).

---

## 1. The defect, reproduced on real data

`period2_cycle_present` requires a 6-step window of strict two-cell alternation (`p[j] == p[j+2]`,
`p[i] != p[i+1]`). A k-step latch holds the decided action for k consecutive steps, so during any
hold the agent moves the same direction twice running and `p[j] != p[j+2]`. **No environment,
policy, seed or episode length can make a k>=2 latch produce strict single-step alternation.**

Measured on the V3-EXQ-1007 episode log (`..._20260907T072349Z_v3_episode_log.json`), 6 logged
episodes per arm:

| arm | `period2_cycle_present` fires |
|---|---|
| `greedy_argmax` (k=1, no latch) | **4/6** |
| `persist_k2` | **0/6** |
| `persist_k4` | **0/6** |
| `stochastic_sample` | 0/6 |

C1 passes when the detector is False, so C1 passes 6/6 on every latch arm. The criterion the run's
verdict rested on returns the same value for a latched agent that is still perfectly trapped as for
one that genuinely escaped.

## 2. The replacement: confinement

> **C1' (re-posed).** Split the episode at its midpoint. The trajectory is **confined** iff the
> second half visits **no cell the first half did not already visit**. Otherwise it **escaped**.
> If the first half is shorter than the longest period the arm's manipulation can produce, or the
> second half is shorter than `MIN_TAIL`, the episode is **UNDETERMINED** -- never "escaped".

```python
MIN_TAIL = 4

def confinement(positions, max_period):
    """True = confined, False = escaped, None = UNDETERMINED (the episode cannot carry the test)."""
    pos = [tuple(p) for p in positions]
    n = len(pos)
    tail_len = (n + 1) // 2
    head_len = n - tail_len
    if tail_len < MIN_TAIL or head_len < max_period:
        return None
    head, tail = set(pos[:head_len]), pos[head_len:]
    return len(set(tail) - head) == 0
```

`max_period` is **2k** for a latch of depth k (a k-latch re-periodises a period-2 alternation to
period 2k), 2 for an unlatched arm.

**Why this shape.** An orbit of *any* period over *any* number of cells stops producing new cells
once it closes; a boundary-press fixed point produces none at all; an escaping trajectory keeps
producing them. So one measure covers both phenotypes MECH-535's title names, with no period
parameter to be blind at and no dependence on excursion amplitude.

## 3. Both findings of GFLAG-0233 are repaired, and the second one structurally

**Finding 1 (the identity)** -- repaired by section 2, evidenced in section 5.

**Finding 2 (the reach check is blind at exactly the k it would select)** -- repaired by making the
reach requirement **scale with k**. The incumbent `bounded_orbit_period` needs `min_repeats * p`
consecutive positions (24 for period 8) and returns `None` when the episode is shorter; the old
gate read that `None` as *no orbit*, so a **longer** period got an **easier** pass. The re-posed
gate inverts that: `head_len >= max_period` means a **bigger k demands MORE episode, never less**,
and an episode that cannot support the test is `UNDETERMINED`.

> **The general rule this instance is a case of: a detector's blind spot must map to UNDETERMINED,
> never to a negative.** The old gate read absence-of-detection as evidence-of-absence; that is what
> made it "a gate selecting on its own blind spot".

Measured, on synthetic k-latched orbits at the episode lengths `persist_k4` actually produced:

| k | period | n | incumbent `bounded_orbit_period` (min_repeats 3) | re-posed C1' |
|---|---|---|---|---|
| 4 | 8 | 19 | **None** (blind) | **confined** |
| 4 | 8 | 22 | **None** (blind) | **confined** |
| 4 | 8 | 23 | **None** (blind) | **confined** |
| 4 | 8 | 40 | 8 | confined |
| 4 | 8 | **15** | None | **UNDETERMINED** (head 7 < 8) |

The bottom row is the fail-closed behaviour: too little episode to resolve a period-8 orbit is
reported as such, not as an escape.

## 4. Measured on real traces -- and one clause of the inherited recipe is REFUTED

k-scaled reach rule, V3-EXQ-1007 episode log, 6 logged episodes per arm:

| arm | max_period | confined | escaped | undetermined |
|---|---|---|---|---|
| `greedy_argmax` | 2 | **6** | 0 | 0 |
| `persist_k2` | 4 | **6** | 0 | 0 |
| `persist_k4` | 8 | **5** | 1 | 0 |
| `switch_cost` | 8 | **5** | 0 | **1** |
| `stochastic_sample` | 2 | 0 | **6** | 0 |
| `random_walk` | 2 | 0 | **6** | 0 |
| `local_view_greedy` | 2 | 0 | **6** | 0 |
| `local_view_greedy_persist_k2` | 4 | 1 | **5** | 0 |

Confirmed against all 20 episodes per cell via the manifest's arm-level incidences
(`trace.fixed_point_incidence`, `trace.mean_unique_cells`, `foraging_competence`):

| arm | fixed-point incidence (seeds 42/43/44) | mean unique cells | foraging competence |
|---|---|---|---|
| `greedy_argmax` | 0.20 / **1.00** / **1.00** | 4.45 / 5.00 / 9.75 | 0.00 / 0.25 / 0.55 |
| `persist_k2` | 0.25 / **1.00** / **1.00** | 6.05 / 4.90 / 9.70 | 0.10 / 0.25 / 0.50 |
| `persist_k4` | 0.30 / **1.00** / **1.00** | 7.55 / 4.90 / 9.70 | 0.15 / 0.25 / 0.50 |
| `switch_cost` | 0.55 / **1.00** / **1.00** | 6.60 / 4.90 / 9.65 | 0.25 / 0.25 / 0.50 |
| `stochastic_sample` | **0.00 / 0.00 / 0.00** | **26.50 / 24.85 / 24.70** | **2.05 / 1.70 / 1.90** |

**Two things follow, and both change the successor.**

**(a) `switch_cost` does NOT escape the trap.** Section 5.2 of
`exq1007a_blocked_c1_satisfied_by_construction_20260908.md` proposed `switch_cost` as the way out,
on the correct reasoning that a margin-dependent hold is not subject to the period-2k identity.
Being immune to the *identity* is not the same as *escaping the trap*: `switch_cost` is confined on
every resolvable logged episode and is a boundary-press fixed point on 55-100% of all 20 episodes
per seed. **Do not build the successor around `switch_cost` as the escape operator.**

**(b) The only arm that escapes is the one that is not a persistence operator at all.**
`stochastic_sample` is the sole arm with zero fixed-point incidence, ~4x the unique cells, and
4-8x the foraging competence. On this substrate the trap is broken by **perturbation**, not by
**persistence** -- which is exactly the contrast MECH-536's own notes flag ("GFLAG-0131's
stochastic-eval ask ... the non-biological version of the same fix; the project's brain-like-
construction principle prefers the latch").

**Also recorded, because it is load-bearing for any successor's power:** the ambitendency
two-cycle is a **seed-42-only** phenotype in this run. Seeds 43 and 44 are 100% fixed-point on
every arm. A criterion built around "the cycle" reads 2 of 3 seeds as empty; confinement reads all
three, which is the second reason to prefer it.

## 5. The non-degeneracy evidence -- the test `period2_cycle_present` could never have passed

The whole failure mode being repaired is *a criterion the manipulation satisfies by itself*. So the
replacement is only admissible with evidence that **the manipulation does not force its value**:

| comparison | same manipulation | differs in | confined |
|---|---|---|---|
| `persist_k2` | k=2 latch | direction-blind representation | **6/6** |
| `local_view_greedy_persist_k2` | k=2 latch | adequate representation | **1/6** |
| `greedy_argmax` | no latch | direction-blind representation | **6/6** |
| `local_view_greedy` | no latch | adequate representation | **0/6** |

Same latch, opposite readings. C1' is moved by the **representation** -- which is what MECH-536 is
about -- and not by the latch. Reproduced synthetically: a k=2 latch on an alternating reader reads
confined; a k=2 latch on an advancing reader reads not-confined.

**And it is not merely detecting stochasticity:** `local_view_greedy` is fully deterministic and
escapes 6/6. Determinism does not force confinement; an inadequate representation does.

### Rejected alternative, with the measurement that rejected it

**Tail excursion** (max L1 distance travelled within the tail) was the other natural period-agnostic
form, and it is **wrong for exactly the reason the incumbent was wrong** -- it scales with the
manipulation. Median tail excursion: `greedy` 0, `persist_k2` 2, `persist_k4` 3. A k-latch widens
the excursion by construction, so a bigger k would read as "more escaped" without escaping
anything. Confinement is amplitude-free by design: it asks whether the visited set *stopped
growing*, not how big it is.

### Edge shapes

All nine pass, including the two that matter most -- the perseveration shape MECH-536 predicts and
the fail-closed case:

| shape | expected | got |
|---|---|---|
| period-2 two-cell cycle (MECH-535 ambitendency) | confined | confined |
| wall-press fixed point (MECH-535 stupor) | confined | confined |
| straight run THEN boundary press (MECH-536 perseveration) | confined | confined |
| straight run still running at truncation | escaped | escaped |
| single out-and-back sweep | confined | confined |
| open-ended wander | escaped | escaped |
| confined first, escapes in the tail | escaped | escaped |
| k=4 latch at n=19 (incumbent is blind here) | confined | confined |
| k=4 latch at n=15 (head too short) | UNDETERMINED | UNDETERMINED |

## 6. What this does to MECH-536's dissociation -- the part governance should read

MECH-536's registered signature is conditional: *"adding k>=2-step action persistence removes the
two-cell cycle AND leaves resources/episode flat"* -> representational deficit; *"cycle gone +
competence rises"* -> gating deficit. **Both branches are conditioned on the cycle being gone.**

Under the incumbent C1 that antecedent is satisfied by arithmetic, so the run would have read
`supports` while the agent remained trapped. Under C1' the antecedent is **false for every
persistence operator tested**: the latch converts a period-2 cycle into a period-2k cycle, or
leaves the fixed point untouched, and the agent is confined either way.

So the honest reading of the banked data is neither branch of the dissociation. It is:

> **A fixed-k latch does not abolish the ambitendency phenotype; it re-scales its period. The
> phenotype's escape route on this substrate is perturbation, not persistence.**

MECH-536's notes assert *"Any persistence of >=2 steps on the chosen action escapes a two-cycle
trivially"*. That is true of the **period-2 signature** and false of the **trap**. This is the
sentence that propagated into the criterion, and it is the one governance should amend.

**This does not weaken MECH-536's functional claim** -- "persistence buys robustness to a degraded
representation; it does not supply direction" is, if anything, supported: the latch supplied no
direction and bought no competence (0.10-0.15 vs greedy's 0.00-0.55, tracking seed not arm).
What fails is the *discriminator's* premise, not the claim. Both claims stay `non_contributory`.

## 7. What the successor should ask (and what no longer needs a run)

**Already answered from banked data, at zero fleet cost -- do not spend a run re-measuring:**
1. Does a fixed-k latch abolish the period-2 signature? Yes, by arithmetic, at every k.
2. Does it abolish confinement? No -- `persist_k2` 6/6, `persist_k4` 5/6 confined.
3. Does `switch_cost` escape? No -- 5/5 confined, 0.55-1.00 fixed-point incidence.
4. Does competence rise under any persistence operator? No -- flat within seed.

**Genuinely open, and worth a run:** MECH-536 asks what persistence is *for* relative to
representation quality. The banked data answers that for the latch family on the direction-blind
reader and leaves the **dissociation itself** untested, because no arm satisfied the antecedent.
The successor should therefore compare **persistence against perturbation on the same frozen
policy**, scored on C1' (confinement) and competence jointly, with `local_view_greedy` as the
adequate-representation anchor -- a design with a real failing region on both axes, and with
`persist_k2`/`persist_k4` retained as a **positive control for the detector itself** (we know
analytically they re-periodise, so a C1' that reports them as escaped is broken).

That successor is `V3-EXQ-1007b`, built and queued on this record.

## 8. Provenance and carry-forward

- The V3-EXQ-1007a driver stays parked at
  `ree-v3/experiments/_scratch/v3_exq_1007a_mech536_eval_persistence_discriminator.py.blocked`.
  Its other five ratified changes are sound and are carried forward; only C1 and the reach check
  are replaced.
- `period2_cycle_present` is **retained as a reported diagnostic**, never as a criterion -- it is
  the signal that identifies the unlatched ambitendency phenotype in the first place.
- Probes are reproducible from this record's own code block; they read banked evidence and write
  nothing.
