# proposal_tick mass-mint: validity pass and prioritisation

Generated 2026-09-01T20:49:35Z by orchestrate-20260901-curate-r3 (/metaworker-orchestrate), at user request.

## What happened

`proposal_tick` minted **166 `chip-proposal-exp-*` chips between 20:27Z and 20:29Z**, one per
proposal recorded as V3-testable with no completed run. Each is titled "Queue experiment for
EXP-NNNN (CLAIM)", so the queue-starvation preempt in `dispatch_candidate_order.py` promotes
ALL of them into the science tier. With dispatcher leases live that would have committed the
fleet to 166 Opus `/queue-experiment` sessions overnight, on a day the account had already hit
its monthly spend limit. Dispatch was paused and the user directed a prioritisation pass
instead: take the 10 most useful now, pace the remainder over the coming week.

The FINDING is sound -- 166 untested V3 proposals is real and worth knowing. The DELIVERY is
not: one chip per registry row is ledger volume, not a research plan.

## Validity pass (all 166)

- All 166 claim ids resolve in `claims.yaml`. No orphans.
- Status: 149 `candidate`, 17 `provisional`. All genuinely untested.
- Spot-checked the top 14 against `claim_evidence.v1.json`: **0 existing runs each**, so the
  "no completed run" assertion holds where it was checked.
- **27 are NOT V3-testable** (`implementation_phase` v4/v5) despite the chips asserting they
  are. The producer's predicate does not check `implementation_phase`. These are listed
  separately below and must NOT be queued as V3 work.
- **NONE of the 166 appears in `CURRENT_FRONT.md`.** They are all off the live front. That is
  not a reason to discard them -- it is the reason they can be paced rather than rushed.

## Ranking method

Ordered by DEPENDENT COUNT: how many other claims list this claim in their `depends_on`.
A claim many others rest on is the one whose falsification propagates furthest, so testing it
buys the most information. Ties broken by phase (explicit `v3` first) and status.

**What this ranking does NOT check, and a consumer must:** whether runnable substrate exists
for each claim. That is a per-claim question `/queue-experiment` answers at authoring time
(its Step 2.5c substrate-overlap gate). A high-dependent claim with no substrate is not
actionable, and any of the 10 below may turn out that way -- that is an acceptable and
informative outcome, not a failure of the pick.

## TIER 1 -- the 10 to run now

| # | dependents | claim | phase | status | EXP | chip_ref | title |
|---|---|---|---|---|---|---|---|
| 1 | 19 | ARC-019 | - | provisional | EXP-0436 | `chip-proposal-exp-0436` | REE requires staged developmental training with explicit curriculum gates. |
| 2 | 16 | MECH-031 | - | provisional | EXP-0812 | `chip-proposal-exp-0812` | Derived social tags and empathy coupling via control-plane knobs. |
| 3 | 9 | MECH-039 | - | provisional | EXP-0824 | `chip-proposal-exp-0824` | Modes are stable regions in control-channel space, not separate modules. |
| 4 | 9 | INV-077 | - | candidate | EXP-0749 | `chip-proposal-exp-0749` | Evaluation channels are evidence-producing boundaries, not world-state affordances: no agentic subsy |
| 5 | 7 | MECH-043 | - | provisional | EXP-0829 | `chip-proposal-exp-0829` | Dopamine-like modulation of precision-weighting for unsigned prediction errors. |
| 6 | 6 | MECH-035 | - | candidate | EXP-0817 | `chip-proposal-exp-0817` | VALENCE is vector-valued and ranked without scalar collapse. |
| 7 | 6 | MECH-027 | - | provisional | EXP-0808 | `chip-proposal-exp-0808` | Pathological modes reflect mis-tuned control-plane regimes. |
| 8 | 6 | INV-086 | - | candidate | EXP-0755 | `chip-proposal-exp-0755` | goal_maintenance_feedback_necessity |
| 9 | 5 | MECH-127 | - | candidate | EXP-0876 | `chip-proposal-exp-0876` | Counterfactual other-cost-aversion activates cooperative behavior as a motivational surrogate when t |
| 10 | 5 | MECH-081 | - | candidate | EXP-0853 | `chip-proposal-exp-0853` | E2 sufficiency constraint reduces E1 effective dimensionality target. |

## TIER 2 -- paced over the coming week (129)

Withdrawn from the live ledger to keep the dispatcher on curated work. Re-mint in small
batches from this table -- highest dependents first. Do NOT re-mint all at once.

| dependents | claim | phase | EXP | chip_ref |
|---|---|---|---|---|
| 5 | MECH-065 | - | EXP-0841 | `chip-proposal-exp-0841` |
| 5 | MECH-037 | - | EXP-0820 | `chip-proposal-exp-0820` |
| 5 | INV-072 | - | EXP-0746 | `chip-proposal-exp-0746` |
| 5 | EXT-009 | - | EXP-0609 | `chip-proposal-exp-0609` |
| 5 | ARC-044 | - | EXP-0501 | `chip-proposal-exp-0501` |
| 4 | MECH-107 | v3 | EXP-0862 | `chip-proposal-exp-0862` |
| 4 | MECH-019 | - | EXP-0800 | `chip-proposal-exp-0800` |
| 4 | ARC-008 | - | EXP-0418 | `chip-proposal-exp-0418` |
| 3 | SD-077 | v3 | EXP-1214 | `chip-proposal-exp-1214` |
| 3 | SD-070 | v3 | EXP-1204 | `chip-proposal-exp-1204` |
| 3 | MECH-468 | v3 | EXP-1103 | `chip-proposal-exp-1103` |
| 3 | MECH-126 | - | EXP-0874 | `chip-proposal-exp-0874` |
| 3 | MECH-110 | v3 | EXP-0867 | `chip-proposal-exp-0867` |
| 3 | MECH-105 | v3 | EXP-0860 | `chip-proposal-exp-0860` |
| 3 | MECH-055 | - | EXP-0837 | `chip-proposal-exp-0837` |
| 3 | EXT-003 | - | EXP-0597 | `chip-proposal-exp-0597` |
| 3 | ARC-131 | v3 | EXP-0573 | `chip-proposal-exp-0573` |
| 2 | SD-090 | - | EXP-1228 | `chip-proposal-exp-1228` |
| 2 | SD-089 | - | EXP-1226 | `chip-proposal-exp-1226` |
| 2 | MECH-495 | v3 | EXP-1123 | `chip-proposal-exp-1123` |
| 2 | MECH-251 | v3 | EXP-0967 | `chip-proposal-exp-0967` |
| 2 | MECH-223 | - | EXP-0928 | `chip-proposal-exp-0928` |
| 2 | MECH-221 | v3 | EXP-0924 | `chip-proposal-exp-0924` |
| 2 | MECH-211 | - | EXP-0917 | `chip-proposal-exp-0917` |
| 2 | MECH-161 | v3 | EXP-0899 | `chip-proposal-exp-0899` |
| 2 | MECH-084 | - | EXP-0858 | `chip-proposal-exp-0858` |
| 2 | MECH-080 | - | EXP-0851 | `chip-proposal-exp-0851` |
| 2 | MECH-018 | - | EXP-0798 | `chip-proposal-exp-0798` |
| 2 | MECH-011 | - | EXP-0784 | `chip-proposal-exp-0784` |
| 2 | MECH-005 | - | EXP-0780 | `chip-proposal-exp-0780` |
| 2 | MECH-004 | - | EXP-0778 | `chip-proposal-exp-0778` |
| 2 | INV-024 | - | EXP-0711 | `chip-proposal-exp-0711` |
| 2 | INV-023 | - | EXP-0709 | `chip-proposal-exp-0709` |
| 2 | IMPL-023 | - | EXP-0677 | `chip-proposal-exp-0677` |
| 2 | ARC-120 | v3 | EXP-0557 | `chip-proposal-exp-0557` |
| 2 | ARC-073 | - | EXP-0519 | `chip-proposal-exp-0519` |
| 1 | SD-086 | v3 | EXP-1222 | `chip-proposal-exp-1222` |
| 1 | SD-071 | v3 | EXP-1206 | `chip-proposal-exp-1206` |
| 1 | MECH-469 | v3 | EXP-1105 | `chip-proposal-exp-1105` |
| 1 | MECH-464 | v3 | EXP-1099 | `chip-proposal-exp-1099` |
| 1 | MECH-327 | - | EXP-1003 | `chip-proposal-exp-1003` |
| 1 | MECH-249 | - | EXP-0963 | `chip-proposal-exp-0963` |
| 1 | MECH-248 | - | EXP-0961 | `chip-proposal-exp-0961` |
| 1 | MECH-239 | v3 | EXP-0947 | `chip-proposal-exp-0947` |
| 1 | MECH-237 | v3 | EXP-0944 | `chip-proposal-exp-0944` |
| 1 | MECH-222 | v3 | EXP-0926 | `chip-proposal-exp-0926` |
| 1 | MECH-213 | v3 | EXP-0920 | `chip-proposal-exp-0920` |
| 1 | MECH-208 | v3 | EXP-0913 | `chip-proposal-exp-0913` |
| 1 | MECH-206 | v3 | EXP-0911 | `chip-proposal-exp-0911` |
| 1 | MECH-170 | - | EXP-0905 | `chip-proposal-exp-0905` |
| 1 | MECH-162 | v3 | EXP-0901 | `chip-proposal-exp-0901` |
| 1 | MECH-160 | v3 | EXP-0897 | `chip-proposal-exp-0897` |
| 1 | MECH-159 | - | EXP-0895 | `chip-proposal-exp-0895` |
| 1 | MECH-131 | - | EXP-0878 | `chip-proposal-exp-0878` |
| 1 | MECH-125 | v3 | EXP-0872 | `chip-proposal-exp-0872` |
| 1 | MECH-082 | - | EXP-0855 | `chip-proposal-exp-0855` |
| 1 | MECH-067 | - | EXP-0845 | `chip-proposal-exp-0845` |
| 1 | MECH-066 | - | EXP-0843 | `chip-proposal-exp-0843` |
| 1 | MECH-064 | - | EXP-0839 | `chip-proposal-exp-0839` |
| 1 | MECH-034 | - | EXP-0815 | `chip-proposal-exp-0815` |
| 1 | MECH-024 | - | EXP-0806 | `chip-proposal-exp-0806` |
| 1 | MECH-017 | - | EXP-0796 | `chip-proposal-exp-0796` |
| 1 | MECH-016 | - | EXP-0794 | `chip-proposal-exp-0794` |
| 1 | MECH-015 | - | EXP-0792 | `chip-proposal-exp-0792` |
| 1 | MECH-014 | - | EXP-0790 | `chip-proposal-exp-0790` |
| 1 | MECH-003 | - | EXP-0776 | `chip-proposal-exp-0776` |
| 1 | INV-093 | v3 | EXP-0760 | `chip-proposal-exp-0760` |
| 1 | INV-092 | v3 | EXP-0758 | `chip-proposal-exp-0758` |
| 1 | INV-069 | - | EXP-0742 | `chip-proposal-exp-0742` |
| 1 | IMPL-019 | - | EXP-0675 | `chip-proposal-exp-0675` |
| 1 | IMPL-008 | - | EXP-0657 | `chip-proposal-exp-0657` |
| 1 | ARC-037 | v3 | EXP-0494 | `chip-proposal-exp-0494` |
| 0 | SD-088 | - | EXP-1224 | `chip-proposal-exp-1224` |
| 0 | SD-081 | v3 | EXP-1216 | `chip-proposal-exp-1216` |
| 0 | SD-075 | v3 | EXP-1212 | `chip-proposal-exp-1212` |
| 0 | SD-074 | v3 | EXP-1210 | `chip-proposal-exp-1210` |
| 0 | SD-033d | v3 | EXP-1176 | `chip-proposal-exp-1176` |
| 0 | MECH-530 | v3 | EXP-1153 | `chip-proposal-exp-1153` |
| 0 | MECH-494 | v3 | EXP-1121 | `chip-proposal-exp-1121` |
| 0 | MECH-474 | v3 | EXP-1110 | `chip-proposal-exp-1110` |
| 0 | MECH-470 | v3 | EXP-1107 | `chip-proposal-exp-1107` |
| 0 | MECH-426 | v3 | EXP-1079 | `chip-proposal-exp-1079` |
| 0 | MECH-384 | v3 | EXP-1045 | `chip-proposal-exp-1045` |
| 0 | MECH-328 | - | EXP-1005 | `chip-proposal-exp-1005` |
| 0 | MECH-250 | - | EXP-0965 | `chip-proposal-exp-0965` |
| 0 | MECH-247 | - | EXP-0959 | `chip-proposal-exp-0959` |
| 0 | MECH-246 | - | EXP-0957 | `chip-proposal-exp-0957` |
| 0 | MECH-234 | - | EXP-0941 | `chip-proposal-exp-0941` |
| 0 | MECH-233 | - | EXP-0939 | `chip-proposal-exp-0939` |
| 0 | MECH-227 | - | EXP-0935 | `chip-proposal-exp-0935` |
| 0 | MECH-190 | - | EXP-0907 | `chip-proposal-exp-0907` |
| 0 | MECH-167 | v3 | EXP-0903 | `chip-proposal-exp-0903` |
| 0 | MECH-157 | - | EXP-0892 | `chip-proposal-exp-0892` |
| 0 | MECH-136 | v3 | EXP-0886 | `chip-proposal-exp-0886` |
| 0 | MECH-134 | - | EXP-0884 | `chip-proposal-exp-0884` |
| 0 | MECH-133 | - | EXP-0882 | `chip-proposal-exp-0882` |
| 0 | MECH-132 | - | EXP-0880 | `chip-proposal-exp-0880` |
| 0 | MECH-115 | v3 | EXP-0870 | `chip-proposal-exp-0870` |
| 0 | MECH-109 | v3 | EXP-0865 | `chip-proposal-exp-0865` |
| 0 | MECH-079 | - | EXP-0849 | `chip-proposal-exp-0849` |
| 0 | MECH-078 | - | EXP-0847 | `chip-proposal-exp-0847` |
| 0 | MECH-050 | - | EXP-0833 | `chip-proposal-exp-0833` |
| 0 | MECH-049 | - | EXP-0831 | `chip-proposal-exp-0831` |
| 0 | MECH-042 | - | EXP-0827 | `chip-proposal-exp-0827` |
| 0 | MECH-038 | - | EXP-0822 | `chip-proposal-exp-0822` |
| 0 | MECH-028 | - | EXP-0810 | `chip-proposal-exp-0810` |
| 0 | MECH-023 | - | EXP-0804 | `chip-proposal-exp-0804` |
| 0 | MECH-021 | - | EXP-0802 | `chip-proposal-exp-0802` |
| 0 | MECH-013 | - | EXP-0788 | `chip-proposal-exp-0788` |
| 0 | MECH-012 | - | EXP-0786 | `chip-proposal-exp-0786` |
| 0 | MECH-002 | - | EXP-0774 | `chip-proposal-exp-0774` |
| 0 | INV-095 | - | EXP-0763 | `chip-proposal-exp-0763` |
| 0 | INV-063 | - | EXP-0736 | `chip-proposal-exp-0736` |
| 0 | INV-040 | v3 | EXP-0731 | `chip-proposal-exp-0731` |
| 0 | INV-022 | - | EXP-0707 | `chip-proposal-exp-0707` |
| 0 | IMPL-027 | - | EXP-0683 | `chip-proposal-exp-0683` |
| 0 | IMPL-026 | - | EXP-0681 | `chip-proposal-exp-0681` |
| 0 | IMPL-025 | - | EXP-0679 | `chip-proposal-exp-0679` |
| 0 | IMPL-016 | - | EXP-0669 | `chip-proposal-exp-0669` |
| 0 | EXT-008 | - | EXP-0607 | `chip-proposal-exp-0607` |
| 0 | EXT-007 | - | EXP-0605 | `chip-proposal-exp-0605` |
| 0 | EXT-006 | - | EXP-0603 | `chip-proposal-exp-0603` |
| 0 | EXT-005 | - | EXP-0601 | `chip-proposal-exp-0601` |
| 0 | EXT-004 | - | EXP-0599 | `chip-proposal-exp-0599` |
| 0 | EXT-002 | - | EXP-0595 | `chip-proposal-exp-0595` |
| 0 | EXT-001 | - | EXP-0578 | `chip-proposal-exp-0578` |
| 0 | ARC-121 | v3 | EXP-0560 | `chip-proposal-exp-0560` |
| 0 | ARC-061 | - | EXP-0515 | `chip-proposal-exp-0515` |
| 0 | ARC-052 | v3 | EXP-0504 | `chip-proposal-exp-0504` |

## NOT V3-TESTABLE -- do not queue as V3 work (27)

| dependents | claim | phase | EXP | chip_ref |
|---|---|---|---|---|
| 7 | MECH-278 | v4 | EXP-0976 | `chip-proposal-exp-0976` |
| 5 | MECH-300 | v4 | EXP-0988 | `chip-proposal-exp-0988` |
| 5 | MECH-228 | v4 | EXP-0937 | `chip-proposal-exp-0937` |
| 3 | MECH-299 | v4 | EXP-0986 | `chip-proposal-exp-0986` |
| 3 | MECH-274 | v4 | EXP-0971 | `chip-proposal-exp-0971` |
| 2 | ARC-031 | v4 | EXP-0473 | `chip-proposal-exp-0473` |
| 1 | MECH-296 | v4 | EXP-0980 | `chip-proposal-exp-0980` |
| 1 | MECH-145 | v5 | EXP-0888 | `chip-proposal-exp-0888` |
| 1 | INV-039 | v4 | EXP-0729 | `chip-proposal-exp-0729` |
| 1 | ARC-083 | v4 | EXP-0529 | `chip-proposal-exp-0529` |
| 1 | ARC-055 | v4 | EXP-0510 | `chip-proposal-exp-0510` |
| 0 | SD-044 | v4 | EXP-1184 | `chip-proposal-exp-1184` |
| 0 | SD-043 | v4 | EXP-1182 | `chip-proposal-exp-1182` |
| 0 | SD-041 | v4 | EXP-1180 | `chip-proposal-exp-1180` |
| 0 | MECH-301 | v4 | EXP-0990 | `chip-proposal-exp-0990` |
| 0 | MECH-298 | v4 | EXP-0984 | `chip-proposal-exp-0984` |
| 0 | MECH-297 | v4 | EXP-0982 | `chip-proposal-exp-0982` |
| 0 | MECH-255 | v4 | EXP-0969 | `chip-proposal-exp-0969` |
| 0 | MECH-243 | v4 | EXP-0955 | `chip-proposal-exp-0955` |
| 0 | MECH-242 | v4 | EXP-0953 | `chip-proposal-exp-0953` |
| 0 | MECH-241 | v4 | EXP-0951 | `chip-proposal-exp-0951` |
| 0 | MECH-240 | v4 | EXP-0949 | `chip-proposal-exp-0949` |
| 0 | MECH-226 | v4 | EXP-0933 | `chip-proposal-exp-0933` |
| 0 | MECH-224 | v4 | EXP-0930 | `chip-proposal-exp-0930` |
| 0 | MECH-218 | v4 | EXP-0922 | `chip-proposal-exp-0922` |
| 0 | MECH-146 | v5 | EXP-0890 | `chip-proposal-exp-0890` |
| 0 | ARC-082 | v4 | EXP-0527 | `chip-proposal-exp-0527` |

