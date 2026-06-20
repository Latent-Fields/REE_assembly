# MECH-443 / MECH-444 — CDQ-005 decide-to-build, GO / NO-GO / KEEP-DEFERRED record (2026-06-20)

**Author:** session `mech443-444-phaseA-falsifier-adjudicate-20260620T1206Z`. **Time:** 2026-06-20T12:06Z.
**Status changed:** none. **Code built:** none. **`ceiling_decision: deferred` markers:** both LEFT IN PLACE (see §4).

This is the chip-requested GO / NO-GO / KEEP-DEFERRED record for the CDQ-005 MuZero/EfficientZero *reanalyze*
import. It does **not** re-derive the adjudication — that was done rigorously on 2026-06-19 in
[`mech_443_444_decide_to_build_2026-06-19.md`](mech_443_444_decide_to_build_2026-06-19.md). This doc **reconciles**
that packet's `(b)/(c)` verdicts to the chip's three-state vocabulary and confirms the disposition stands.

---

## 1. Verdict

| claim | 2026-06-19 packet verdict | chip three-state verdict | meaning |
|---|---|---|---|
| **MECH-443** priority_weighted_replay_write_selection | **(b) DESIGN GAP** — buildable on the landed MECH-319 write primitive; route one go/no-go non-degeneracy probe first | **GO** | The campaign is authorized to *proceed*: its first concrete step is the rule-layer non-degeneracy probe (chip Phase B1 == packet §2.4-Q1), which can itself still flip 443 to defer if the readout is degenerate. Behavioural payoff (Phase B2) is sequenced behind the MECH-439 conversion-ceiling lift (689a chain). |
| **MECH-444** staleness_gated_target_refresh_on_replay_write | **(c) DON'T-BUILD-yet** | **KEEP-DEFERRED** | Blocked behind MECH-443 being built + keeping, AND a target-recompute primitive that does not yet exist; biology is analogy-only. No action this cycle. |

**GO does not mean "build now."** MECH-443's GO is a GO to the *gated* campaign whose entry gate (Phase B1) is a
cheap diagnostic. The behavioural leg (Phase B2) is hard-gated on 689a lifting the ceiling; if 689a does not lift
it, B2 stays blocked and MECH-443/444 stay `pending_retest` (chip's own instruction — do not run a guaranteed
monostrategy FAIL).

## 2. Load-bearing biology divergence (per biology_before_formal_definitions)

Treated as load-bearing, not a caveat — carried verbatim into both claims' new `what_would_answer` fields:

- **MECH-443:** MuZero/EfficientZero prioritized replay keys priority on value-prediction error. The hippocampal
  biology (Mattar & Daw 2018 gain × need; **Carey et al. 2019** counterweight) says priority is the *value of the
  update*, and replay can bias **away** from the currently-preferred outcome. A REE import that equates priority
  with reward magnitude or committed-policy value is therefore biologically **falsified** — the divergence is the
  discriminator, encoded in the falsifier.
- **MECH-444:** reanalyze recomputes a *value target* in a learned model. No recording demonstrates a literal
  recompute-then-write hippocampal operation; the biological warrant is the Mattar gain term + Olafsdottir
  generative preplay, by analogy only. A null falsifies the **engineering import**, not the replay biology. This
  divergence is exactly why 444 is the more speculative leg and stays KEEP-DEFERRED.

## 3. What this changes vs the 2026-06-19 packet

Nothing in the adjudication — it confirms it. The two concrete additions this cycle (Phase A of the chip):
1. **`what_would_answer` fields** added to MECH-443 and MECH-444 in `claims.yaml` (the embedded FALSIFIER prose
   distilled into a crisp support-vs-falsify discriminator with the non-degeneracy pre-gate and the ceiling-gating
   of the committed variant made explicit).
2. **This GO / KEEP-DEFERRED record**, linked from CDQ-005.

## 4. Marker disposition — both `ceiling_decision: deferred` stay (claims.yaml status untouched)

The chip permits removing the marker only "when the campaign is authorized AND unblocked," coordinated with the GO.
The campaign is authorized (443 = GO) but **not unblocked**, and there is **no routing home**:

1. **689a has NOT landed.** As of 2026-06-20T12:06Z it is `status=claimed` on DLAPTOP-4.local and **running**
   (live runner PID 12572, ~15h52m elapsed, heartbeat `state=running, current_exq=V3-EXQ-689a`; no results row in
   the coordinator DB). Per the heartbeat-stale rule it is alive — not touched. Until it lands and is adjudicated
   for ceiling-lift, the campaign is blocked.
2. **No `substrate_queue` entry references MECH-443 or MECH-444** (grep = 0). Per packet §5, removing the marker
   without simultaneously creating a routing home re-flags the claim as a genuine orphan every Step-6a-v
   substrate-ceiling audit cycle. Marker removal must coincide with minting the Phase B1 probe's queue entry +
   a substrate_queue routing home.

**Removal trigger (for a later session):** MECH-443's Phase B1 non-degeneracy probe is queued via
`/queue-experiment` (the routing home), at which point remove MECH-443's marker as part of that queueing.
MECH-444's marker stays until MECH-443 is built and keeps.

## 5. Next actions (gated — do not execute until 689a lands)

- **Poll 689a** to a terminal manifest (coordinator DB results row + `evidence/experiments/` manifest), then
  adjudicate whether it **lifts** the ARC-062 conversion ceiling (an ARC-062 retest converts diversity to
  committed action; realised committed first-action entropy range no longer pinned at 0.0).
- **Phase B1** (rule-layer write-path non-degeneracy probe, ceiling-independent readout) via `/queue-experiment` —
  run after 689a lands to avoid a low-value rep-only "supports" while the ceiling is down.
- **Phase B2** (behavioural payoff) — ONLY if 689a lifted the ceiling. Else record, keep `pending_retest`, re-defer.
- **MECH-444** — hold. Re-open only after MECH-443 is built and keeps + a recompute primitive is scoped.
