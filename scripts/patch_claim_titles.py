#!/usr/bin/env python3
"""
Add title fields to all claims in docs/claims/claims.yaml.
Inserts `  title: "..."` on the line immediately after each `- id: XXX` line.
Skips claims that already have a title field.
"""
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
CLAIMS_YAML = REPO_ROOT / "docs" / "claims" / "claims.yaml"

# ── Title map (all 216 claims) ──────────────────────────────────────────────
TITLES = {
    # Invariants
    "INV-001": "No explicit ethics module or moral scoring layer.",
    "INV-002": "Coherence includes temporal/phase binding, not just static metrics.",
    "INV-003": "Language emerges as functional self-representation, not a bolt-on.",
    "INV-004": "Post-commit consequence traces are persistent, not resettable.",
    "INV-005": "Harm to others contributes via mirror modelling, not symbolic rules.",
    "INV-006": "Post-commit consequence traces cannot be erased, only integrated.",
    "INV-007": "Language cannot override embodied harm sensing.",
    "INV-008": "Precision is routed and depth-specific, not global.",
    "INV-009": "Attention is precision modulation, not symbolic control.",
    "INV-010": "Offline integration exists and is required.",
    "INV-011": "Imagination must be possible without belief update.",
    "INV-012": "Responsibility arises through commitment, not prediction alone.",
    "INV-013": "Cognition is predictive, iterative, and multi-timescale.",
    "INV-014": "Representation and regulation are strictly separated.",
    "INV-015": "Ethics emerges from constraint, not optimisation.",
    "INV-016": "Stability is prioritized over maximal performance.",
    "INV-017": "Runaway behavior is a control failure, not representational.",
    "INV-018": "Agency is required; passive predictors are not REE.",
    "INV-019": "Rehearsal traversal and irreversible durable write must remain separated.",
    "INV-020": "Constraint stores are authority-stratified from direct observational/symbolic writes.",
    "INV-021": "Responsibility-bearing durable updates occur only at typed commit boundaries.",
    "INV-022": "Trust/precision allocation must remain heterogeneous, not a single scalar.",
    "INV-023": "Protected offline recalibration/integration regimes are structurally required.",
    "INV-024": "Offline consolidation and online commitment must remain isolated at responsibility-bearing write loci.",
    "INV-025": "Irreducible uncertainty is an epistemological constraint that cannot be engineered away.",
    "INV-026": "A self is an operational prerequisite for responsible agency.",
    "INV-027": "An external world is a structural prerequisite for grounded representation.",
    "INV-028": "Shared-world ethics requires modelling others as co-inhabitants of the same consequence space.",
    "INV-029": "Love as long-horizon care-investment is a structurally coherent agent disposition, not an add-on sentiment.",
    "INV-030": "Viability is defined relative to the agent's continuity in a shared world, not as a scalar reward.",
    "INV-031": "Functional persistence in a shared world, not abstract truth, is the operational goal of cognition.",
    # Architectural Commitments
    "ARC-001": "E1 is the persistent predictive substrate.",
    "ARC-002": "E2 is the fast forward predictor of affordances.",
    "ARC-003": "E3 selects and commits trajectories.",
    "ARC-004": "L-space is a multi-timescale latent stack.",
    "ARC-005": "Control plane routes precision and modes.",
    "ARC-006": "Entities are sparse, persistent, bindable structures.",
    "ARC-007": "Hippocampal systems store and replay paths through residue-field terrain.",
    "ARC-008": "Commitment eligibility is gated by tau, rho, and phi.",
    "ARC-009": "Language is a symbolic mediation and coordination layer.",
    "ARC-010": "Social cognition uses mirror modelling and coupling.",
    "ARC-011": "Offline integration (sleep) is required for stability.",
    "ARC-012": "E3 does not require an explicit ethical cost term.",
    "ARC-013": "Residue is persistent latent-space curvature; hippocampal paths form a cognitive map.",
    "ARC-014": "Default Mode enables safe imagination without commitment.",
    "ARC-015": "Self-impact attribution and responsibility flow are required.",
    "ARC-016": "Modes are control-plane regimes applied to shared predictive machinery.",
    "ARC-017": "Minimal stream tags with typed exteroception and explicit reality-coherence lane.",
    "ARC-018": "Hippocampus generates explicit rollouts and post-commitment viability mapping.",
    "ARC-019": "REE requires staged developmental training with explicit curriculum gates.",
    "ARC-020": "Offline consolidation is protected by typed authority/write boundaries.",
    "ARC-021": "Three BG-like cortico-striatal loops require distinct learning channels.",
    "ARC-022": "Hierarchical effect-object abstraction pipeline (E1→E2→DMN→Goal/Avoid→Hippocampus) — conflict with ARC-007/ARC-014, pending adjudication.",
    "ARC-023": "Three BG-like loops operate at characteristic thalamic heartbeat rates.",
    "ARC-024": "Harm and benefit signals have asymptotic proxy structure in world latent space.",
    "ARC-025": "Three-engine (E1/E2/E3) architecture is irreducible; no engine can be collapsed into another.",
    "ARC-026": "Love as long-horizon care investment expands under intelligence rather than being crowded out.",
    "ARC-027": "Harm stream runs as a parallel thalamic pathway independent of world latent space.",
    # Mechanism Hypotheses
    "MECH-001": "Astrocyte-aware regulatory stack mediates control-plane precision routing.",
    "MECH-002": "Precision control analogues shape cognitive regimes.",
    "MECH-003": "Precision must be tau-scoped with lossy projections.",
    "MECH-004": "Signal-to-knob wiring map for control plane.",
    "MECH-005": "Path authority and interruptibility via norepinephrine-like control.",
    "MECH-006": "Serotonin-like modulation governs representational collapse.",
    "MECH-007": "Attention must be fragmented across control axes.",
    "MECH-008": "Legacy mechanism: superseded by AA/PCM and control-channel mode framing.",
    "MECH-010": "Language emergence and bootstrapping dynamics.",
    "MECH-011": "Language and learning dynamics.",
    "MECH-012": "Language and institutions interplay.",
    "MECH-013": "Language failure modes and pathologies.",
    "MECH-014": "Minimal signalling channel requirements.",
    "MECH-015": "Trust and deception dynamics.",
    "MECH-016": "Precision recalibration during sleep.",
    "MECH-017": "Reality consolidation during sleep.",
    "MECH-018": "Residue integration during sleep.",
    "MECH-019": "Control plane shapes modes of cognition, not discrete choices.",
    "MECH-020": "Legacy mechanism: superseded by control-plane mode framing.",
    "MECH-021": "Subjective now is a control surface across temporal horizons.",
    "MECH-022": "Hippocampal systems inject hypotheses gated by control plane.",
    "MECH-023": "Responsibility is geometric and path-dependent.",
    "MECH-024": "Selfhood, personality, and ethics converge structurally.",
    "MECH-025": "Action mode prioritizes short-horizon, high-precision, responsibility-linked control.",
    "MECH-026": "Ready vigilance primes restraint under high sensitivity without action.",
    "MECH-027": "Pathological modes reflect mis-tuned control-plane regimes.",
    "MECH-028": "Ethical behavior depends on mode transitions and learning preservation.",
    "MECH-029": "Reflective/DMN mode supports moral simulation via gated replay.",
    "MECH-030": "Sleep modes consolidate learning and ethical residue across regimes.",
    "MECH-031": "Derived social tags and empathy coupling via control-plane knobs.",
    "MECH-032": "OTHER_SELFLIKE detection is biased toward high recall to avoid empathy false negatives.",
    "MECH-033": "E2 forward-prediction kernels seed hippocampal rollouts.",
    "MECH-034": "Viability mapping updates are distinct from residue curvature updates.",
    "MECH-035": "VALENCE is vector-valued and ranked without scalar collapse.",
    "MECH-036": "Other-harm triggers veto only under high-certainty catastrophic outcomes.",
    "MECH-037": "Papez-like loop provides provenance gating and reality filtering.",
    "MECH-038": "Arcuate-like sequence-to-motor channel nudges language emergence.",
    "MECH-039": "Modes are stable regions in control-channel space, not separate modules.",
    "MECH-040": "Safety baseline and volatility are distinct control channels for arousal/readiness.",
    "MECH-041": "Affective expression broadcasts control-plane regime to reduce social prediction load.",
    "MECH-042": "Telemetry exposure channels report internal control-plane state for diagnostics.",
    "MECH-043": "Dopamine-like modulation of precision-weighting for unsigned prediction errors.",
    "MECH-044": "Hippocampal systems participate in relational binding and comparison.",
    "MECH-045": "Object-file-like buffers provide minimal entity persistence across time.",
    "MECH-046": "Amygdala analogue updates control-plane mode priors from fast salience classification.",
    "MECH-047": "Pre-commitment mode manager commits with hysteresis and switching costs.",
    "MECH-048": "mu/kappa stability overlays modulate mode entropy and switching pressure.",
    "MECH-049": "Temporal phase compartmentalisation preserves ethical constraint independence.",
    "MECH-050": "Functional locality supports attribution without requiring anatomical columns.",
    "MECH-051": "Oxytocin/vasopressin analogues modulate relational topology and mode priors.",
    "MECH-052": "Prolactin analogue stabilises care-investment persistence.",
    "MECH-053": "Habenula-like aversive PE gate suppresses commitment under negative spikes.",
    "MECH-054": "Signed harm/benefit prediction-error precision channels remain distinct.",
    "MECH-055": "Affective channel separation keeps hedonic tone, valence, and signed PE distinct.",
    "MECH-056": "Residue should constrain trajectories before distorting core representations.",
    "MECH-057a": "Committed action sequences suppress new precision updates until execution completes.",
    "MECH-057b": "Hippocampal sequence completion must be verified before candidates are eligible for E3 selection.",
    "MECH-058": "Slow target-anchor dynamics stabilize E1/E2 representations via functional rate separation.",
    "MECH-059": "Confidence channel (uncertainty-derived precision) must remain distinct from residual error.",
    "MECH-060": "Pre-commit simulation and post-commit realized-error channels must stay responsibility-distinct via write-boundary enforcement.",
    "MECH-061": "Commit-boundary token reclassifies pre-commit vs post-commit error routing.",
    "MECH-062": "E3 uses coordinated tri-loop gating (motor, cognitive-set, motivational) as the pre-commit eligibility layer.",
    "MECH-063": "Control plane retains orthogonal tonic/phasic axes rather than collapsing into one scalar.",
    "MECH-064": "Typed authority/control-store separation blocks direct exteroceptive writes into policy and identity stores.",
    "MECH-065": "Reality-coherence conflict lane modulates loop precision and commitment thresholds before execution lock-in.",
    "MECH-066": "Pre-commit and post-commit channels may share representations but must stay separated at durable write boundaries.",
    "MECH-067": "A machine-checkable phase/store/actor permission matrix is required to enforce commit-boundary write rules.",
    "MECH-068": "Consolidation selectivity lives in the consolidation operator, not in E1 feature basis.",
    "MECH-069": "Sensory prediction error, motor-sensory error, and harm/goal error are incommensurable and cannot be collapsed.",
    "MECH-070": "E2 is a conceptual-sensorium motor model with a planning horizon that exceeds E1.",
    "MECH-071": "E2 harm prediction is better calibrated for agent-caused vs environment-caused transitions.",
    "MECH-072": "Foreseeable-harm gating on residue accumulation reduces false attribution without degrading harm avoidance.",
    "MECH-073": "Valence is intrinsic to hippocampal map geometry, not applied downstream — conflict with ARC-007, pending adjudication.",
    "MECH-074": "Amygdala functions as read/write head for valenced hippocampal map.",
    "MECH-075": "Basal ganglia perform dopaminergic gain/threshold setting on hippocampal attractor dynamics.",
    "MECH-076": "Residue is structural deformation of hippocampal map topology (CA3 retraction, DG neurogenesis, reconsolidation).",
    "MECH-077": "Therapeutic change equals hippocampal remapping, with modalities operating at different levels.",
    "MECH-078": "Amygdala bootstraps novel valence for unmapped hippocampal territory; anxiety disorders are systematic over-valencing.",
    "MECH-079": "Phenomenological continuous selfhood is an artefact of stable hippocampal map geometry.",
    "MECH-080": "Rollout truncation set-points as psychiatric individual differences substrate (ADHD/anxiety/OCD).",
    "MECH-081": "E2 sufficiency constraint reduces E1 effective dimensionality target.",
    "MECH-082": "Hippocampal map distortion propagates through E2 to bias E1 attentional sampling without explicit E1 retraining.",
    "MECH-083": "Acetylcholine as meta-level plasticity gain governing durable-write vs read-through.",
    "MECH-084": "Noradrenaline as attentional snap and E1/E2 sampling ratio modulator.",
    "MECH-085": "Serotonin as hippocampal map geometry parameter (rollout depth, distal value weighting) — conflict with MECH-006, pending adjudication.",
    "MECH-086": "Dopamine as trajectory selection gain plane operating downstream of landscape, state, and encoding gate.",
    "MECH-087": "Hierarchical ordering of four neuromodulatory control planes: ACh → NA → 5-HT → DA.",
    "MECH-088": "Psychiatric conditions as four-plane neuromodulatory control failures.",
    "MECH-089": "E1 updates are batched into theta-cycle summaries before reaching E3 (cross-frequency temporal packaging).",
    "MECH-090": "Beta oscillations gate E3-to-action-selection propagation, not E3 internal updating.",
    "MECH-091": "Salient events phase-reset the E3 heartbeat clock.",
    "MECH-092": "Quiescent E3 heartbeat cycles trigger hippocampal SWR-equivalent replay for viability map consolidation.",
    "MECH-093": "z_beta modulates E3 heartbeat frequency, distinct from precision-weighting.",
    "MECH-094": "Hypothesis tag is a categorical write gate separating simulation from committed residue updates; tag loss is the PTSD mechanism.",
    "MECH-095": "Temporoparietal junction (TPJ) acts as agency-detection comparator distinguishing self-caused from other-caused change.",
    "MECH-096": "Dual-stream observation routing sends exteroceptive input to both E1 and a dedicated harm detection pathway.",
    "MECH-097": "Peripersonal space geometry defines the commit locus — the spatial boundary of committed action.",
    "MECH-098": "Reafference cancellation: z_world subtracts predicted self-caused sensory change to isolate external events.",
    "MECH-099": "Visual streams use a three-pathway architecture (ventral/dorsal/frontal) for object, action, and executive routing.",
    "MECH-100": "z_world encoder requires event-type cross-entropy auxiliary loss during training.",
    "MECH-101": "z_world encoding requires reafference context to correctly attribute external vs self-caused change.",
    "MECH-102": "Violence is a terminal error-correction mechanism triggered only when all other channels fail.",
    "MECH-103": "E1 performs multimodal exteroceptive fusion across sensory modalities before feeding E2.",
    # Open Questions
    "Q-001": "What mechanisms produce entity emergence and binding?",
    "Q-002": "What is the appropriate spatial resolution for R(x,t)?",
    "Q-003": "Should R(x,t) be scalar or vector?",
    "Q-004": "How to calibrate tau_R relative to E1/E2?",
    "Q-005": "Can sleep anneal or reset R(x,t)?",
    "Q-006": "Is ethics developmental rather than additive?",
    "Q-007": "Do universal expressions map to stable control-channel regimes?",
    "Q-008": "Legacy: resolved in favor of valence/mu-kappa separation with calibration follow-up.",
    "Q-009": "Legacy: resolved via bounded care-override policy with hard catastrophic other-harm veto.",
    "Q-010": "Legacy: separation question resolved into MECH-055.",
    "Q-011": "Legacy: resolved by placing diversity-floor control in pre-commit/offline sampling.",
    "Q-012": "Can latent predictive world models stay agentically stable without explicit REE-like control constraints?",
    "Q-013": "Can deterministic JEPA plus derived dispersion match explicit stochastic uncertainty heads for REE precision routing?",
    "Q-014": "Do JEPA invariances hide ethically relevant distinctions in REE attribution contexts?",
    "Q-015": "What is the smallest commit-boundary token that still supports reliable multi-timescale attribution?",
    "Q-016": "What arbitration policy best resolves tri-loop gate conflicts without coupling collapse?",
    "Q-017": "What is the minimal orthogonal control-axis subset that preserves observed regime separations?",
    "Q-018": "What RC-conflict threshold calibration blocks authority spoofing without chronic over-suppression?",
    "Q-019": "Three-gate vs single-gate BG architecture: are the three cortico-striatal loops anatomically distinct or convergent?",
    "Q-020": "Does ARC-007's no-value-computation constraint survive MECH-073 (valence intrinsic to hippocampal map)?",
    # Implementation Notes
    "IMPL-001": "Glossary of canonical REE terms.",
    "IMPL-002": "Repository metadata and contribution process.",
    "IMPL-003": "Minimum instantiation specification.",
    "IMPL-004": "Legacy REE overview summary.",
    "IMPL-005": "Failure mode taxonomy.",
    "IMPL-006": "Legacy migration mapping.",
    "IMPL-007": "Legacy refactor final output summary.",
    "IMPL-008": "Program phases, repository roles, and phase-gate criteria.",
    "IMPL-009": "Wiring notes and cross-reference summary.",
    "IMPL-010": "Android world environment contract.",
    "IMPL-011": "Toy world environment contract.",
    "IMPL-012": "Toy world scoring functions.",
    "IMPL-013": "Documentation operating procedure and prompts.",
    "IMPL-014": "Documentation change history.",
    "IMPL-015": "Legacy architecture overview.",
    "IMPL-016": "Trajectory selection detail for E3.",
    "IMPL-017": "Conflict index and resolution entry point.",
    "IMPL-018": "Claim index and navigation.",
    "IMPL-019": "Self-first, social-later developmental testing order heuristic.",
    "IMPL-020": "Formal JEPA/REE terminology alignment glossary for interoperability.",
    "IMPL-021": "Hybrid JEPA/REE architecture diagram contract and rendering checklist.",
    "IMPL-022": "JEPA-like E1/E2 representation-reference contract (inputs, outputs, knobs, failure gates).",
    "IMPL-023": "REE-v2 representation-interface-first spec and phase gate.",
    "IMPL-024": "v2 REE-first canonical wording policy with JEPA interface translation.",
    "IMPL-025": "Cross-version hook surface contract and registry.",
    # Design Decisions
    "SD-001": "CEM-based trajectory search belongs in HippocampalModule, not E2.",
    "SD-002": "E1 associative prior must be wired into HippocampalModule for terrain-informed rollout search.",
    "SD-003": "Self-attribution via counterfactual E2: causal signature = E2(z_t, a_actual) minus E2(z_t, a_counterfactual).",
    "SD-004": "Action objects as hippocampal map backbone, enabling long-horizon planning beyond step-level trajectories.",
    "SD-005": "z_gamma split into z_self (E2 motor-sensory domain) and z_world (E3/Hippocampus domain).",
    "SD-006": "E1, E2, and E3 run at characteristic rates (async multi-rate) rather than lockstep.",
    "SD-007": "ReafferencePredictor provides perspective-corrected world latent by subtracting self-caused sensory change.",
    "SD-008": "LatentStack EMA alpha for z_world must be >= 0.9 to preserve event responsiveness.",
    "SD-009": "z_world encoder requires event-type cross-entropy auxiliary loss during training.",
    "SD-010": "HARM stream is a dedicated sensory pathway separate from z_world processing.",
}


def main():
    text = CLAIMS_YAML.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    output = []
    i = 0
    patched = 0
    skipped_already = 0

    while i < len(lines):
        line = lines[i]
        # Match a claim list entry line: "- id: XXX"
        m = re.match(r'^- id:\s+(\S+)', line)
        if m:
            claim_id = m.group(1)
            output.append(line)
            i += 1

            # Check if the next non-blank line is already `  title:`
            # We'll look ahead a few lines
            already_has_title = False
            lookahead = i
            while lookahead < len(lines) and lookahead < i + 8:
                ll = lines[lookahead]
                if re.match(r'^\s+title:', ll):
                    already_has_title = True
                    break
                # Stop looking if we hit another claim entry or top-level key
                if re.match(r'^- id:', ll):
                    break
                lookahead += 1

            if already_has_title:
                skipped_already += 1
            else:
                title = TITLES.get(claim_id)
                if title:
                    # Escape any double quotes in title
                    title_escaped = title.replace('"', '\\"')
                    output.append(f'  title: "{title_escaped}"\n')
                    patched += 1
                else:
                    print(f"WARNING: No title for {claim_id}", file=sys.stderr)
        else:
            output.append(line)
            i += 1

    CLAIMS_YAML.write_text("".join(output), encoding="utf-8")
    print(f"Patched {patched} claims with titles ({skipped_already} already had titles).")


if __name__ == "__main__":
    main()
