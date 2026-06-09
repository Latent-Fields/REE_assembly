# Failure Autopsy — V3-EXQ-657 (MECH-294 multi-content theta-burst packet substrate-readiness)

- generated_utc: 2026-06-09T19:37:27Z
- scope: single
- status: confirmed
- target run_id: v3_exq_657_mech294_multi_content_theta_packet_readiness_20260609T190708Z_v3
- queue_id: V3-EXQ-657 (claim_ids=[], experiment_purpose=diagnostic, evidence_direction=non_contributory)
- manifest verdict: FAIL, label `substrate_not_ready_requeue` (self-routed at G1)
- routing (user-confirmed 2026-06-09): `/queue-experiment` scoped fix -> V3-EXQ-657a (supersedes 657). NO substrate (ree_core) change. NO claims.yaml change. MECH-294 stays candidate / v3_pending; 2026-04-26 governance hold stands until 657a PASSes.

## 1. Facts (no interpretation)

4 arms x 3 seeds (42/43/44), real CausalGridWorldV2, packet wired READ-ONLY
(`theta_packet_compose_into_e3_bias=False`) so the action stream is identical
across arms for a matched seed (only the binding-mode transform of the sealed
packet differs).

| Arm | completeness_frac | vintage_het_frac | mean_coherence (42/43/44) |
|---|---|---|---|
| ARM_0_OFF | 0.0 (n_packets=0; packet off) | 0.0 | 0.0 / 0.0 / 0.0 |
| ARM_1_JOINT | 1.0 | **0.0** | 0.260 / 0.346 / 0.429 |
| ARM_2_ALTERNATION | 1.0 | **1.0** | 0.267 / 0.333 / 0.418 |
| ARM_3_SHUFFLED | 1.0 | **0.0** | 0.264 / 0.313 / 0.410 |

Gate results: G0 PASS (completeness), **G1 FAIL** (ARM_1 vintage_het 0/3 seeds),
non-vacuity PASS (joint-vs-shuffled matched-cycle norm-L1 = 0.357/0.294/0.482, all
> 1e-3 floor), C1 FAIL (0/3), C2 FAIL (0/3). The verdict `_evaluate()`
short-circuits at the first failing non-degeneracy gate, so the manifest label is
the G1-fail reading ("the MECH-269b V_s vintaging is inert on this run").

Failed criteria: an **absolute / non-degeneracy gate (G1)** short-circuited the
verdict; the **discrimination criteria (C1, C2)** also failed (computed but not
reached in the routing). Two coupled defects.

## 2. Claim-layer mapping

- MECH-294 (`theta_burst.multi_content_joint_packet`): candidate, v3_pending,
  implementation_phase v3. The 2026-04-26 governance hold requires a substrate-side
  test that discriminates joint-within-cycle binding from Kay-2020 cross-cycle
  alternation. V3-EXQ-657 is claim-free (claim_ids=[]) — it does NOT weight
  MECH-294 confidence; it is the readiness gate that, on PASS, unblocks the
  behavioural-evidence successor. So this FAIL cannot and does not weaken MECH-294;
  it is a diagnostic that failed to deliver an interpretable readiness verdict.
- claim_ids accuracy: correct (empty by design — readiness diagnostic).

## 3. Biological-reference triage

Not the load-bearing axis here (the failure is a diagnostic instrumentation
artifact, not a mechanism question). For completeness: the joint-packet claim's
references (Kay et al. 2020 theta content-packets; MECH-269/269b per-stream
verisimilitude) are intact and unimplicated. The substrate faithfully renders
both the joint and the Kay-alternation regimes (that is exactly what the diagnostic
was built to compare). No formal-import divergence; no lit-pull commission.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | 657 is claim-free; cannot express/falsify MECH-294. Readiness gate only. |
| Biological reference | clear | Joint + alternation regimes both faithfully rendered; not implicated. |
| Dependency prerequisites | present | use_per_stream_vs=True wired; MECH-269 V_s populated before observe. |
| Implementation completeness | complete | Substrate correct. Contract C3 proves V_s-hold fires (V_s=0.1<0.4 -> snapshot substituted, stale, n_distinct_vintages>=2); 968 contracts pass. ARM_2 het=1.0 proves snapshot/hold/age machinery runs in the agent loop. |
| Environment adequacy | adequate-but-quiescent | 40-step stable forced-benefit run keeps every stream's V_s >= 0.4 (seeded 1.0, EMA tau 0.1), so the V_s-threshold hold path is never naturally exercised in JOINT mode. Not a defect of the substrate. |
| Measurement adequacy | **under-instrumented / misleading** | (a) G1 measured on ARM_1_JOINT demands vintage heterogeneity, a SECONDARY property the verisimilar regime correctly does not produce, and short-circuits the verdict. (b) `_coherence()` = mean pairwise cosine over 4 streams, L2-normalised, truncated to common dim 16 — discards magnitude (the signal norm-signature captures), computes cross-cosine between different semantic latent spaces (regime-stable, binding-mode-blind). Under read-only-first there is NO behavioural readout (action stream identical across arms), so the blind cosine is the only C1/C2 signal. |
| Integration adequacy | coupled | Packet seals at E3 boundary, exposed as agent.last_theta_packet; read-only. |
| Scale / capacity | adequate | n_packets 16-20/cell sufficient for the structural readouts. |

**Recommended epistemic_category:** none applied to MECH-294 (claim untouched). The
657 manifest is a diagnostic-instrumentation FAIL: the substrate is ready; the
readout was blind. Recommended manifest handling: leave 657 non_contributory and
mark `evidence_direction: "superseded"` AFTER 657a runs (per supersession policy).

## 5. The two defects (confirmed)

**Defect 1 — G1 vintage-inert = gate-design bug (NOT wiring, NOT substrate-ceiling).**
`per_stream_vs` is wired into `observe()` (agent.py:3489), populated in `sense()`
(agent.py:3201) before `_e1_tick`. The V_s-threshold hold path is proven by
contract C3. ARM_2 alternation het=1.0 proves the hold/age machinery. ARM_1 het=0
is the CORRECT verisimilar-regime behaviour of joint binding (all streams current),
not a failure. G1-on-the-joint-arm tests a property the regime does not elicit and
blocks the primary result.

**Defect 2 — C1/C2 coherence-blind = metric bug (the metric, not the substrate, is
the blocker).** The substrate produces structurally-distinct packets across all
three modes (non-vacuity 0.29-0.48; activation-smoke structural dist joint-vs-alt
17.9 / joint-vs-shuf 44.6). The cosine `_coherence()` cannot see it: per-seed
deltas ~0.007 << margin 0.05. Confirmed the pre-autopsy hypothesis (a diagnostic's
interpretation.label can lie via a vacuous metric) — here non-vacuity passed
structurally while C1/C2 failed on the blind coherence readout.

## 6. Learning extracted

1. Under `theta_packet_compose_into_e3_bias=False` (read-only-first), behavioural
   readouts (proposer first-action / E3 committed-class distributions) are dead
   discriminators — the action stream is identical across arms by construction. A
   read-only readiness gate's C1/C2 MUST be packet-structure metrics. The 657
   cosine "consistency score" was a behavioural-flavoured proxy that, stripped of
   magnitude and computed across heterogeneous latent spaces, carries no
   binding-mode signal.
2. A vintage-heterogeneity gate measured on the JOINT arm conflates "the V_s
   vintaging MACHINERY is live" (true; proven by C3 + ARM_2) with "joint-mode
   packets show heterogeneous vintages on this run" (false by design in the
   verisimilar regime). The machinery check must exercise the V_s-threshold hold
   path directly (forced-low-V_s probe), not demand a regime-dependent emergent
   property.
3. The norm-signature L1 distance is the discriminator the substrate's structure
   actually supports; the non-vacuity gate already used it successfully. C1/C2
   should be built on it, not on cosine.

## 7. Repair pathway (user-confirmed)

Route: `/queue-experiment` -> **V3-EXQ-657a** (alphabetic suffix; same scientific
question, corrected instrumentation), `supersedes: V3-EXQ-657`. Scoped to the
diagnostic experiment script only — no `ree_core` change, no claims.yaml change.

657a corrections (both user-confirmed):
- **C1/C2 readout:** read-only structural separability. C1 = matched-cycle
  structural distance (component-norm-signature L1) joint-vs-alternation; C2 =
  joint-vs-shuffled; each required > a discrimination margin AND > the within-joint
  cross-seed baseline. Corroborating conjunctive readout: cross-stream norm
  covariation (joint co-varies same-cycle; shuffled draws decorrelated cross-cycle).
  Manifest framing made explicit: readiness = the three binding modes are
  non-degenerate AND structurally separable; "co-binding carries DOWNSTREAM signal"
  is the behavioural successor's job (compose ON), per memo S5/S7.3.
- **G1 fix:** G1 passes iff BOTH (a) a deterministic forced-low-V_s probe drives one
  stream's V_s < hold (0.4) and confirms the JOINT packet substitutes the snapshot +
  marks the component stale (directly exercises MECH-269b V_s consumption in joint
  mode), AND (b) ARM_2 alternation het > 0 on >= 2/3 seeds (machinery live in the
  agent loop).

This does NOT force a pass: 657a still FAILs if the structural distances do not
exceed the cross-seed baseline (modes genuinely indistinguishable) or if the
forced-low-V_s probe does not hold (V_s consumption broken).

No `recommended_substrate_queue_entry` (action: none) — the substrate is correct;
the repair is entirely in the diagnostic.

## 8. Draft evidence_quality_note (governance applies; do NOT write here)

For the 657 manifest at the post-657a governance walk:
"V3-EXQ-657 FAILed on diagnostic instrumentation, not on the substrate. G1
(vintage heterogeneity, measured on the joint arm) demanded a secondary property
the verisimilar regime correctly does not produce (V_s never dropped below the 0.4
hold floor on the stable run); the V_s-hold path is proven by contract C3 and by
ARM_2 alternation het=1.0. C1/C2 failed because the cosine coherence readout is
binding-mode-blind (discards magnitude; cross-cosine over heterogeneous latent
spaces) while the substrate produces structurally-distinct packets (non-vacuity
norm-L1 0.29-0.48). Superseded by V3-EXQ-657a (corrected readout). Mark
evidence_direction: superseded after 657a runs."
