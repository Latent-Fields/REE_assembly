# MECH-479 targeted lit pull (targeted_review_connectome_mech_479)

All citations verified via PubMed metadata this session. Validator: `validate_literature.py --repo <scratch copy>` -> OK (5 records, 0 findings). (Note: `validate_literature.py` takes `--paths`, not positional args, and scopes to records under `--repo`; out-of-repo paths silently give "0 records checked", so a scratch repo copy with the schema was used.)

## Entries
- 2026-09-24_mech_479_model_free_prioritized_avoiding_harm_to_others_lockwood2020 -- weakens, 0.55 -- people lean MORE on model-free (cached) control when learning to avoid harming others than themselves (PNAS 2020, doi 10.1073/pnas.2010890117).
- 2026-09-24_mech_479_sgacc_prosocial_prediction_error_lockwood2016 -- mixed, 0.50 -- same RL algorithm for self/other, but slower for others, and a prosocial-selective sgACC prediction error (other-specific node).
- 2026-09-24_mech_479_simulation_learning_self_other_vmpfc_suzuki2012 -- mixed, 0.45 -- vmPFC self-valuation directly recruited to simulate another, but insufficient without a dmPFC/dlPFC other-action PE adjunct.
- 2026-09-24_mech_479_agent_independent_axis_choice_on_behalf_nicolle2012 -- supports, 0.45 -- executed-choice mPFC machinery is agent-independent; roles swap when choosing on a partner's behalf.
- 2026-09-24_mech_479_mtl_episodic_simulation_prosocial_intentions_gaesser2019 -- supports, 0.40 -- MTL subsystem activity predicts the boost in willingness to help from imagining helping (correlational; only RTPJ was TMS'd).

## Anchors named in the brief/claim
- Lockwood prosocial learning: verified (Lockwood et al. 2016 PNAS 113(35):9763-8). Also found the more decisive Lockwood et al. 2020 PNAS model-free paper.
- "Apps & Ramnani sgACC other-oriented": CORRECTED. Apps & Ramnani 2014 J Neurosci 34(18):6190-200 (doi 10.1523/JNEUROSCI.2701-13.2014, PMID 24790190) is about GYRAL ACC (ACCg) signalling net value of others' rewards, not sgACC. Also Apps, Green & Ramnani 2012 NeuroImage 64:1-9 (ACCg codes others' prediction errors / false beliefs). The sgACC-prosocial link is Lockwood 2016/2020. Apps papers verified but not written as entries (other-specific valuation, no planning content; would duplicate the Lockwood 2016 "other-specific node" point). Parent may add Apps & Ramnani 2014 as a weakens-same-machinery entry if wanted.
- Nicolle 2012, Suzuki 2012: verified.
- The claim's notes name no specific literature (INV-029 is registry-internal); no wrong citation found in the claim text.

## Implications for the claim TEXT
1. The biological grounding the claim implies (prosocial planning is naturally model-based/hippocampal) is contradicted in the only direct MB/MF test: Lockwood 2020 shows humans prioritise model-free control for harm-to-others learning. Suggest the notes state explicitly that MECH-479 is a COMPUTATIONAL/structural claim (1-step greedy cannot optimise another agent's integrated z_harm_a over a long horizon), not a claim that biological prosociality is predominantly model-based -- and add Lockwood 2020 as a known falsifier-risk for any "requires" reading at short horizons.
2. Falsifier refinement: the what_would_answer should require a horizon long enough that the other agent's harm is genuinely integrated over many steps; in short-horizon tasks a greedy/cached arm may match or beat the planner on other-agent harm (as in humans), which would be a design null, not a refutation.
3. Same-machinery vs distinct circuitry is mixed: executed choice looks agent-independent (Nicolle), valuation is shared-plus-adjunct (Suzuki), and prediction-error signals have other-specific nodes (Lockwood 2016 sgACC; Apps ACCg). For V4 design: planner/E3 can likely be reused over other-agent state, but other-agent benefit/harm likely needs its own value/error channel and an other-behaviour tracking channel.
4. Hippocampal link is weak and correlational (Gaesser 2019, intentions only). Suggest the claim not cite hippocampus as established for prosocial planning.

## Could not verify / not found
- No study found that directly tests multi-step trajectory planning to reduce another agent's accumulating harm vs a greedy policy, in humans, animals or ML. That gap is itself the main finding: the claim's core is untested in the literature, not just in REE.
- Did not search ML multi-agent RL (e.g. prosocial/empathic reward shaping in MARL); a V4 child-test pull should.
