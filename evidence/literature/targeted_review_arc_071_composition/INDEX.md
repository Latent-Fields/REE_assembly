# INDEX -- ARC-071 policy.composition_via_repeated_grounding

**Pull commissioned:** 2026-05-10 from the policy_primitive_granularity architectural family registration session.
**Companion pull (deferred):** ARC-070 decomposition-on-prediction-failure (sibling slot under ARC-069 parent).
**Date:** 2026-05-10. **Entries:** 9.

## Entries

| Entry ID | Paper | Year | Verdict it informs | Direction | Confidence |
|---|---|---|---|---|---|
| 2026-05-10_arc_071_striatal_chunking_graybiel1998 | Graybiel, "The basal ganglia and chunking of action repertoires" | 1998 | R1 trigger, R2 substrate | supports | 0.84 |
| 2026-05-10_arc_071_habits_evaluative_brain_graybiel2008 | Graybiel, "Habits, rituals, and the evaluative brain" | 2008 | R1 evaluative gating, R5 dynamics | supports | 0.78 |
| 2026-05-10_arc_071_dls_dms_habit_yinknowlton2006 | Yin & Knowlton, "The role of the basal ganglia in habit formation" | 2006 | R3 LOAD-BEARING (transition mechanism for MECH-163) | supports | 0.83 |
| 2026-05-10_arc_071_dual_operator_chunk_dynamics_smithgraybiel2013 | Smith & Graybiel, "A dual operator view of habitual behavior" | 2013 | R3 causal evidence, R5 chunk dynamics | supports | 0.86 |
| 2026-05-10_arc_071_motor_chunking_fmri_wymbs2012 | Wymbs et al., "Differential recruitment of putamen / frontoparietal cortex during motor chunking" | 2012 | R2 multi-substrate phase-dependent | supports | 0.79 |
| 2026-05-10_arc_071_visuomotor_chunk_size_sakai2003 | Sakai, Kitaguchi, Hikosaka, "Chunking during human visuomotor sequence learning" | 2003 | R5 outcome-consistency threshold + chunk size | supports | 0.74 |
| 2026-05-10_arc_071_hierarchical_options_botvinick2009 | Botvinick, Niv, Barto, "Hierarchically organized behavior" | 2009 | R4 chunks-of-chunks recursion | supports | 0.72 |
| 2026-05-10_arc_071_options_framework_sutton1999 | Sutton, Precup, Singh, "Between MDPs and semi-MDPs: Options framework" | 1999 | R4 formal analog, options structure | supports | 0.72 |
| 2026-05-10_arc_071_sleep_replay_motor_consolidation_albouy2013 | Albouy, King, Maquet, Doyon, "Hippocampus and striatum: sleep-related motor consolidation" | 2013 | R6 SAFETY-CRITICAL (MECH-094 gating) | weakens | 0.78 |

## Verdict-by-verdict source mapping

| Verdict | Primary sources | Secondary sources |
|---|---|---|
| R1 trigger primary | Graybiel 1998, Graybiel 2008 | Sakai 2003 |
| R2 substrate locus (multi or single) | Wymbs 2012, Smith & Graybiel 2013 | Yin & Knowlton 2006, Graybiel 1998 |
| R3 LOAD-BEARING transition mechanism for MECH-163 | Yin & Knowlton 2006, Smith & Graybiel 2013 | Graybiel 2008 |
| R4 chunks-of-chunks recursion | Botvinick / Niv / Barto 2009, Sutton / Precup / Singh 1999 | -- |
| R5 outcome-consistency threshold + chunk dissolution | Smith & Graybiel 2013, Sakai 2003 | Graybiel 2008 |
| R6 SAFETY-CRITICAL real-vs-imagined chunking write path | Albouy 2013 | Smith & Graybiel 2013 |

See `synthesis.md` for adjudicated verdicts and lit_conf computation.
