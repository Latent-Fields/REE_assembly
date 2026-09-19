# Proposal minter "backfill" tier -- design, and why it was NOT built (staged 2026-09-19)

Recorded 2026-09-19T10:43:17Z by session `elated-chandrasekhar-4a6e6a`, Part 3 of
`chip-20260918-proposal-minter-feasibility-gate-and-backfill-tier`. Companion to
`proposal_minter_feasibility_gate_replay_20260919.md` (Parts 1-2, landed).

USER DIRECTION 2026-09-18: "...and **perhaps** make a low priority task type for those minted
which are not needed to progress the frontier". The chip scoped it: *implement if Part 2's data
supports a clean frontier test, otherwise report the design and stop*, and *if the frontier
test turns out ambiguous, raise a `kind: decision` chip rather than choosing silently*.

**Status: NOT IMPLEMENTED. The frontier test is ambiguous, and every available definition
demotes the work that has actually been productive.** Decision chip raised:
`chip-20260919-minter-scope-decisions-falsifier-carveout-and-frontier-test`.

## The measurement

The chip's frontier test: a proposal progresses the frontier if its claim is on the live path
in `docs/CURRENT_FRONT.md` / `closure_status`, or is a transitive dependency of a node that is.

1. **`CURRENT_FRONT.md` does not name claims.** Its live path is four EXQ ids (V3-EXQ-1010,
   -1008, -1002, -1006) and one hypothesis-space question (`zworld_actor_adequacy_locus`). There
   is no claim set to test membership of without a further, unstated mapping.
2. **`closure_status` and its loader disagree on what a node is.** `closure_status.md` reports
   108 nodes (98 non-deferred, 34 remaining). `audit_retest_staleness.load_plan_nodes` -- the
   one existing programmatic reader of the same `closure_plan` frontmatter -- returns 418,
   with un-normalised statuses (`in_progress` and `in-progress`, `upstream_blocked` and
   `upstream-blocked`).
3. **The answer swings by an order of magnitude with the definition.** Over the 68 `proposed`
   experimental items whose claim has a falsifier (i.e. what FILTER E leaves):

   | frontier definition | frontier claims | of the 68 mintable proposals |
   |---|---|---|
   | claim in `unblocks_claims` / `cross_plan_link` of an ACTIVE node (open / in_progress / partial / assembling) | 82 | **2** |
   | ... of any REMAINING node (adds blocked / upstream_blocked) | 231 | **3** |
   | ACTIVE, plus transitive `depends_on` | 356 (30% of all claims) | **19** |
   | REMAINING, plus transitive `depends_on` | 522 (45% of all claims) | **28** |

   The transitive walk is the same dense graph that sank Part 2's substrate-debt signal.
4. **The decisive check: 5 of the 6 named successes are off-frontier under EVERY definition.**
   SD-077 (V3-EXQ-1040), SD-074 (784a), SD-106 (1041), SD-082 (1046), SD-098 (1055) -- only
   MECH-482 (964b) is on it. A backfill tier built on any of these tests would have minted the
   most productive proposals of 2026-09-15..18 as low priority, behind a cap of 3.

So the available frontier signal measures "is this claim wired into a closure plan's
frontmatter", which is a property of plan bookkeeping, not of scientific leverage.

## Why it matters less than it did on 2026-09-18

After FILTER E + F the live pool is **15 eligible proposals** (8 already chipped, 7 deferred
by the cap), down from 58. The flood the tier was meant to absorb is closed at the source. A
tier's job now would be ORDERING 15 items, which `_mint_rank` already does.

## The design, if a usable frontier test is supplied

Constraints found while reading the code -- each is a way the tier would have re-created the
flood if built naively:

- **No `priority` field exists on a chip.** `chip_ledger.py record` takes `--kind`
  (work/decision), `--urgency`, `--origin`, `--model`. The registry is coordinator-authoritative
  (DB primary key, hub materializer), so a new field is a hub-side schema change, not a
  one-file edit. Cheapest marker that needs no schema change: a distinct chip_ref infix,
  `chip-proposal-backfill-<id>`.
- **That ref still starts with `chip-proposal-`**, so `count_open_proposal_chips` would count it
  against the FRONTIER cap. The count must split: frontier pool excludes `-backfill-`, backfill
  pool counts only it, each with its own `topup_allowance` (frontier floor 10, backfill cap 3).
- **RED-verdict exclusion must not apply to the backfill count.** `count_open_proposal_chips`
  drops RED chips from the count -- correct for the frontier, and exactly the mechanism that
  turned RED-marking into a mint trigger (e701ecb56 -> the 94 -> 212 flood). For backfill, a
  RED chip must KEEP holding its slot until resolved, or "mark RED -> slot frees -> mint
  another" recurs inside the tier. This is the non-negotiable guard the chip names, and it is
  the opposite rule from the frontier pool's.
- **A title prefix CANNOT demote a chip -- the dispatcher must read the tier explicitly.**
  `dispatch_candidate_order.py` classifies a chip as science-authoring if its title opens with
  "queue " (`SCIENCE_TITLE_ACTION_PATTERN`, line 630) **or merely contains a claim/EXP id**
  (`SCIENCE_ID_PATTERN`, line 603), and the queue-starvation PREEMPT promotes that whole class
  (misfire history at lines 295-350). Any honest backfill title names its claim, so
  "Backfill (low priority): MECH-123 -- ..." is STILL promoted over everything whenever the
  queue starves -- the precise inversion of "low priority". The chip's "distinct title prefix so
  a human can tell them apart" is fine for humans; for the machine the tier needs an explicit
  demotion rule in `dispatch_candidate_order.py` keyed on the `-backfill-` ref infix, sorted
  below the science tier and EXEMPT from the starvation preempt, with a test against that
  module's own classifier rather than a judgement by eye. That is a second claimed file and a
  GOV-HELDOUT-1 check on the dispatcher's tiering, which is another reason this was not folded
  into a "perhaps".
- **Mint order:** frontier always first in `_mint_rank`; backfill minted only when the frontier
  pool is at/above its floor or has nothing eligible.
- **Tests the chip requires:** backfill never exceeds its cap; marking a backfill chip RED frees
  neither a frontier slot nor a backfill slot; frontier ranks first; plus the dispatcher-demotion pin above.

## What would make the frontier test clean

Any ONE of: (a) `generate_current_front.py` emits a machine-readable `frontier_claims` list
beside the prose (it already derives the live path; the claim ids behind V3-EXQ-1010 etc. are
one join away); (b) the user names the frontier as a short explicit claim list, maintained by
`/governance`; (c) frontier := claims with a `recommended_next` / fanout entry in the
hypothesis-space registry's ALIVE hypotheses. Each would need the same replay: it must put the
2026-09-15..18 successes ON the frontier, or explain why they were not.
