# Targeted lit-pull synthesis: persistence timescale of the post-orienting approach/withdraw decision bias (SD-099)

**Pulled** 2026-08-20 (4 entries).
**Commissioning artifact**: `chip-20260820-orienting-bias-ticks-denomination` (design chip, status `open` at time of this pull) -- the design owner needs empirical grounding for the denomination of `orienting_post_override_bias_ticks` (REEConfig default 5, `ree-v3/ree_core/utils/config.py:5343`), which currently counts E3 ticks (~625ms-1.25s at `e3_steps_per_tick=10`, "Option A") versus a candidate switch to env steps (~62-125ms, "Option C").
**Author**: lit-pull session (headless, chip `chip-20260820-litpull-orienting-bias-persistence-timescale`), 2026-08-20.
**Not re-litigated**: this pull does not resolve the decision chip. The design owner decides; this document supplies evidence.

---

## Q1 (primary, absolute): how long does a resolved post-orienting decision bias subsequent action selection?

**Verdict: the evidence converges on hundreds of milliseconds to tens of seconds -- squarely supporting Option A's order of magnitude, and if anything suggesting Option A may be an under-estimate rather than an over-estimate. Nothing found lands inside Option C's 60-125ms range.**

Three independent measurements, two different labs, two different paradigms, converge:

| Source | Paradigm | Measured post-decision persistence |
|---|---|---|
| Shang et al. 2018 *Nat Commun* | Overhead looming-disc threat, mouse, single trial | Freezing bout 21-28 s after a 154-163ms detection-to-commitment latency |
| Vale, Evans & Branco 2017 *Curr Biol* | Looming threat with shelter route closed, mouse | Freezing bout 630ms (fast/urgent looming) to 7.9s (slow looming); spatial-bias persistence 4.6s after an unexpected context change |
| Resulaj et al. 2009 *Nature* | Perceptual 2AFC reach decision, human (contrast anchor, not defensive) | Post-commitment revisability window "a few hundred ms" -- the FASTEST class of biological decision dynamics surveyed, and still well above Option C's range |

The Shang 2018 and Vale 2017 numbers are not the same quantity SD-099's `score_bias` window measures -- they are freezing-STATE durations, not a specifically valence-gated approach/withdraw decision persisting across separate subsequent action-selection events -- but they are the closest available real-world analog of "how long does the defensive system, having detected and reacted to a sudden threat, remain in a state that biases what happens next." Notably, the FASTEST number found anywhere across all three sources (Vale 2017's 630ms, under maximal time pressure) sits almost exactly at Option A's own lower bound (625ms), not inside Option C's range. The Resulaj 2009 entry closes the other end: even the fastest well-characterized biological decision-commitment window in the literature (a domain unrelated to defense, included purely as a floor-calibration anchor) runs to a few hundred ms, still above Option C.

**Mapping to the decision, stated per the commissioning brief's own framework:**
- Evidence found: ~630ms to ~28s, i.e. -> **supports OPTION A** (keep E3-tick denomination, ~625ms-1.25s).
- Nothing found supports a ~60-125ms (sub-theta-cycle) reading.

## Q1b (cross-check, relative): how does the persistence compare to the orienting episode's own duration?

The Bradley 2009 review (Sokolov-lineage human psychophysiology, the same theoretical tradition SD-099's own design doc cites) places the classical orienting response's own component cascade -- cardiac deceleration, electrodermal action-readiness, cortical significance-detection -- on a multi-second time course, the same order of magnitude as the post-decision persistence numbers above, not two orders of magnitude smaller. Q1 and Q1b **agree**: both the orienting episode and the post-decision bias that follows it are seconds-scale phenomena in the biological literature surveyed. There is no disagreement between the absolute (Q1) and relative (Q1b) routes to require flagging.

## Q2 (secondary): is "persists for a fixed duration" even the right primitive?

**Partial answer, and it is a real finding, not a dodge.** The Vale 2017 entry's central result is that the biological system's defensive-strategy commitment is state-gated and rapidly reversible, not duration-gated: freeze-vs-flee strategy flipped completely within a single subsequent encounter once shelter availability (the state that produced the original bias) changed, and freezing duration itself scaled with threat urgency rather than being a fixed constant. This is evidence that a fixed tick-count may not be the most biologically faithful primitive for this SPECIFIC sub-component, independent of which magnitude is chosen. It is worth noting SD-099's own ARREST phase already avoids this trap -- it is gated by an identification-confidence accumulator, not a fixed timer, per the claim's own functional_restatement -- so the tick-count under live discussion here is specifically the narrower POST-decision bias window, not the arrest-release mechanism. Whether that narrower window should also be state-gated is a real open design question this pull surfaces but does not resolve; it was not asked to, and forcing a single duration answer here would overstate what the literature supports.

---

## Entries summary

| entry_id | source | direction | confidence | primary contribution |
|---|---|---|---|---|
| `..._looming_escape_freeze_duration_shang2018` | Shang et al. 2018 *Nat Commun* | supports | 0.66 | Primary quantitative anchor: 21-28s post-commitment freezing, mouse looming threat |
| `..._shelter_memory_freeze_duration_vale2017` | Vale, Evans & Branco 2017 *Curr Biol* | mixed | 0.60 | Second independent magnitude anchor (630ms-7.9s) + direct Q2 evidence (state-gated, not duration-gated) |
| `..._orienting_response_timecourse_bradley2009` | Bradley 2009 *Psychophysiology* | supports | 0.55 | Q1b's denominator: classical orienting-episode time course (seconds-scale, human) |
| `..._changes_of_mind_commitment_window_resulaj2009` | Resulaj et al. 2009 *Nature* | mixed | 0.45 | Floor-calibration contrast: fastest known biological decision-commitment window (few hundred ms) still exceeds Option C |

## Scope discipline (per commissioning instructions)

This is literature evidence, reported separately from experimental evidence per project convention -- it does not alone promote or demote SD-099 or any other claim, and `claims.yaml` was not touched. No code, config default, or `substrate_queue.json` entry was changed. The decision chip `chip-20260820-orienting-bias-ticks-denomination` was not resolved by this session; a pointer to this synthesis was appended to its prompt for the design owner.

## Next steps

1. Rebuild the evidence index (`build_experiment_indexes.py`) so these 4 entries appear in `evidence/literature/INDEX.md`.
2. Design owner reviews this synthesis alongside the decision chip and chooses Option A, Option C, or a third path (e.g. state-gated clear condition per the Q2 finding).
