---
closure_plan:
  id: global_workspace_jlens
  title: "Global Workspace + J-lens (SD-064 access channel)"
  owner_claim: SD-064
  registered: 2026-07-08
  last_updated: 2026-07-10
  scope_claims: [SD-064, SD-027, MECH-254, MECH-191, MECH-089, MECH-287, SD-037, MECH-007]
  sibling_plans: [conversion_ceiling_campaign, behavioral_diversity_isolation]
  retrofit_note: "closure_plan frontmatter RETROFITTED 2026-07-09 (session frosty-thompson-d8f490; frontmatter-only, PROMOTES NOTHING, no claims.yaml/queue touch). Before this the plan carried no closure_plan block, so it was one of the two plans invisible to the closure map (flagged in closure_status.md 'Plans WITHOUT closure_plan frontmatter') even though its Experiment A (V3-EXQ-723) had already run. Snapshot regen (generate_closure_snapshot.py) left to the next governance cycle -- the shared REE_assembly checkout currently holds other sessions' uncommitted derived closure_status/closure_drift churn, so this session lands the plan .md only and does not regenerate/commit snapshots."
  nodes:
    - id: "global_workspace_jlens:A"
      title: "Experiment A -- REE-native J-lens dispositional readout (does REE have a J-space?)"
      status: blocked
      severity: load-bearing
      live:
        as_of: "2026-08-08"
        from: "failure_autopsy_grandfathered-r6-closure-sweep_2026-08-08"
        verdict: "non_contributory/measurement_gap"
        next: "routing=governance-note-only"
        brake: "fired"
        needs_review: false
      join:
        bears_on: []
        scope_claims: ["SD-064", "SD-027", "MECH-254", "MECH-191", "MECH-089", "MECH-287", "SD-037", "MECH-007"]
      unblocks_claims: [SD-064, MECH-191]
      depends_on: []
      blocking_external: ["observation-encoding competence build (V3-EXQ-732-localized H2_observation_interface_unlearnable) -- owned by the competence cluster / f_dominance_conversion_ceiling / ree_ai_design_critique_plan WS-1; Experiment A's J-lens re-read shares this dependency and cannot license compact-vs-diffuse until it lands"]
      cross_plan_link: ["conversion_ceiling_campaign:CAMPAIGN", "behavioral_diversity_isolation:GAP-I"]
      last_updated: 2026-07-10
      reconcile_2026_07_10: "RE-GATED (governance-apply of failure_autopsy_V3-EXQ-723a_2026-07-10, session relaxed-shannon-ba3a53; PROMOTES/DEMOTES/WEIGHTS NOTHING). V3-EXQ-723a (the 723 supersession that FIXED 723's non-discriminative gates -- concentration control now non-degenerate frac_dims_90_random ~0.94, criteria_non_degenerate all True) returned no_compact_workspace_diffuse: the load-bearing concentration_discriminative FAILED (0/3 ready seeds; concentration_ratio ~0.80 > 0.50 ceiling). That diffuse read is a TRUSTWORTHY MEASUREMENT of THIS substrate but is CONFOUNDED as a workspace verdict: 723a reads the same competence-limited all-ON substrate (V3-EXQ-714 config) that 719a/724/732 flagged, foraging 0.158 res/ep (< 1.0 floor) with a weak action-predictive signal (bal_acc 0.47 vs null 0.29); 732 localized the root to H2_observation_interface_unlearnable. A near-monostrategy incompetent policy and a genuinely-diffuse workspace are INDISTINGUISHABLE from this readout -> compact-vs-diffuse UNRESOLVED. Consequence: does NOT weaken SD-064 (stays candidate/v3_pending, evidentially UNTESTED in V3 -- NOT a resolved negative, NOT evidence-for the SD-027-original pluralist reading); does NOT greenlight the GATE-B / SD-027 Experiment-B access-gate build. 4th diagnostic (719a->724->732->723a) to bottom out on the same V3 competence floor -- convergent root. Re-read exempt only on a COMPETENT substrate (add an explicit competence readiness precondition: forage >= floor on a majority of seeds) or a different-mechanism redesign (new EXQ / different claim_ids). Node stays blocked; resumes when the observation-encoding competence build lands."
      completion_note: "V3-EXQ-723 RAN 2026-07-09 (v3_exq_723_jlens_dispositional_readout_diagnostic_20260709T151028Z_v3; experiment_purpose=diagnostic, claim_ids=[], evidence_direction=non_contributory, EXCLUDED from governance scoring -- PROMOTES NOTHING). Post-hoc ridge readout z_t -> committed_class_{t+H} + SVD J-space on the existing all-ON substrate (identical to V3-EXQ-714/719a); NO new mechanism. Self-route = compact_action_coupled_subspace_present on 3/3 seeds: action predictable above the 200-permutation label null (primary bal-acc 0.504 vs null p95 0.363), J-space dim ~2 capturing 0.9 energy, jspace_activity_fraction ~0.00028 (<< the 0.10 compactness ceiling), predictive_retention ~1.006 (>= 0.80 floor -- the compact subspace loses none of the full-state predictive power), broadcast-report proxy available on all seeds. READING (HYPOTHESIS, not a verdict): REE has a compact, action-coupled, broadcast-aligned latent subspace -- the J-space analogue of Anthropic's 2026 finding -- which RAISES the SD-064 prior and, per the plan's own pre-registered sequencing, is the evidence that JUSTIFIES spending the SD-027 V3 boundary-gate retrofit build (node GATE-B) that unlocks the Experiment B falsifier. Caveat carried (LOAD-BEARING): absolute action-predictability is modest (0.50 balanced accuracy over 5 committed classes) -- the signal is above-null but weak, and 'compact' is measured over that weak signal. CONFOUND: 723 read the same all-ON substrate that V3-EXQ-719a showed is competence-limited (forages below floor; state->commitment MI barely above floor), so a compact J-space and an impoverished near-monostrategy policy look alike from this readout. This is why GATE-B is gated on competence-localization first (user-agreed 2026-07-09; see the GATE-B decision_live note) rather than proceeding on the A-positive alone. Diagnostic routed to /failure-autopsy for adjudication; SD-064 stays candidate/v3_pending."
    - id: "global_workspace_jlens:GATE-B"
      title: "SD-027 / MECH-254 V3 boundary top-k access-gate build (use_boundary_access_gate, no-op-default)"
      status: open
      severity: high
      live:
        as_of: "2026-08-08"
        from: "failure_autopsy_grandfathered-r6-closure-sweep_2026-08-08"
        verdict: "non_contributory/measurement_gap"
        next: "routing=governance-note-only"
        brake: "fired"
        needs_review: false
      join:
        bears_on: []
        scope_claims: ["SD-064", "SD-027", "MECH-254", "MECH-191", "MECH-089", "MECH-287", "SD-037", "MECH-007"]
      unblocks_claims: [SD-064, SD-027, MECH-254]
      depends_on: ["global_workspace_jlens:A"]
      blocking_external: ["competence-localization: V3-EXQ-724 (queued) + a competent all-ON substrate -- see cross_plan_link"]
      cross_plan_link: ["behavioral_diversity_isolation:GAP-I", "conversion_ceiling_campaign:CAMPAIGN"]
      decision_live: "DECISION SURFACED 2026-07-09 but GATED (user-agreed sequencing): Experiment A (723) returned compact_action_coupled_subspace_present -- the plan's pre-registered trigger for the retrofit build -- BUT 723 read the SAME all-ON substrate that V3-EXQ-719a (2026-07-08, failure_autopsy_V3-EXQ-719a_2026-07-08) showed is competence-limited (forages 0.065/0.0/0.455 resources/ep, below the 1.0 floor; debiased state->commitment MI clears floor on only 1/3 seeds). That confound weakens A: the ~2-dim / 0.0003-activity 'compactness' may partly reflect a near-monostrategy policy with little action-predictive structure to capture, not a genuine broadcast bottleneck. USER-AGREED (2026-07-09): LOCALIZE COMPETENCE FIRST (V3-EXQ-724 competence-localization diagnostic, already queued, brake-exempt) before spending the SD-027 gate build. A J-space read on a COMPETENT agent is a much cleaner Experiment-A baseline, and the same competence gap is what Experiment B's integration-DV needs to be non-vacuous. So GATE-B does NOT proceed on the A-positive alone; it resumes once competence is localized + a competent all-ON substrate exists. The build when it happens: /implement-substrate V3 top-k selection gate over the E1/E2 -> E3 forwarding path (use_boundary_access_gate flag, byte-identical OFF), top-k over active z_world/z_self components per heartbeat, WITH a hard ablation mode (k -> all / gate disabled) for the MECH-254 four-cell factorial. SD-027 is otherwise v4-scoped; this is the optional fixed-k V3 retrofit the SD-027 evidence_quality_note names but never queued. Status open (not assembling -- not under construction; correctly gated behind competence-localization)."
      last_updated: 2026-07-10
      reconcile_2026_07_10: "The A-positive that this decision was surfaced on is SUPERSEDED. V3-EXQ-723 (compact_action_coupled_subspace_present) -> V3-EXQ-723a (RAN 2026-07-10, supersedes 723, fixed the non-discriminative gates) now returns no_compact_workspace_diffuse, CONFOUNDED by the competence floor (failure_autopsy_V3-EXQ-723a_2026-07-10). So the pre-registered build trigger is NOT met: compact-vs-diffuse is UNRESOLVED, not positive. This does not change the routing (localize competence first) but removes the standing 'A came back positive' justification -- GATE-B is now gated by BOTH an unresolved Experiment A AND the observation-encoding competence build. Do NOT greenlight the SD-027/MECH-254 access-gate build. Node A re-read on a competent substrate is the prerequisite that re-supplies (or falsifies) the trigger."
    - id: "global_workspace_jlens:B"
      title: "Experiment B -- workspace-ablation cliff (cliff vs graceful degradation; the SD-064 falsifier)"
      status: blocked
      severity: load-bearing
      live:
        as_of: "2026-08-08"
        from: "failure_autopsy_grandfathered-r6-closure-sweep_2026-08-08"
        verdict: "non_contributory/measurement_gap"
        next: "routing=governance-note-only"
        brake: "fired"
        needs_review: false
      join:
        bears_on: []
        scope_claims: ["SD-064", "SD-027", "MECH-254", "MECH-191", "MECH-089", "MECH-287", "SD-037", "MECH-007"]
      unblocks_claims: [SD-064, SD-027, MECH-254]
      depends_on: ["global_workspace_jlens:GATE-B"]
      cross_plan_link: ["conversion_ceiling_campaign:CAMPAIGN", "behavioral_diversity_isolation:GAP-I"]
      blocking_external: ["global_workspace_jlens:GATE-B (SD-027 V3 top-k access gate not built -- a gate-ablation experiment today would self-route substrate_not_ready, the '642 trap')"]
      resume_condition: "Resume ONLY after GATE-B builds + smoke-tests the SD-027/MECH-254 V3 top-k access gate. Then queue the MECH-254 four-cell factorial {gate off, gate only, template only, both on} in a task that REQUIRES multi-step committed-action integration (the conversion-ceiling / committed-action-diversity surface is the natural fit -- that DV is already the ceiling-bound one; cross-linked). DV = integrative competence + committed-action diversity; test for a CLIFF (integrative cognition -> ~0, reactive/automatic intact) vs GRACEFUL degradation. Cliff => SD-064 (genuine workspace); graceful => the SD-027-original pluralist / redundant-distributed-pathway reading. This is the sharpest SD-064 test and the direct port of Anthropic's ablation result."
      last_updated: 2026-07-09
    - id: "global_workspace_jlens:MECH-191"
      title: "MECH-191 cross-architecture legibility unblock check (does A's dispositional readout resolve the tonic-channel gap?)"
      status: open
      severity: low
      live:
        as_of: "2026-08-08"
        from: "failure_autopsy_grandfathered-r6-closure-sweep_2026-08-08"
        verdict: "non_contributory/measurement_gap"
        next: "routing=governance-note-only"
        brake: "fired"
        needs_review: false
      join:
        bears_on: []
        scope_claims: ["SD-064", "SD-027", "MECH-254", "MECH-191", "MECH-089", "MECH-287", "SD-037", "MECH-007"]
      unblocks_claims: [MECH-191]
      depends_on: ["global_workspace_jlens:A"]
      note: "MECH-191 (cross-architecture signal legibility) is substrate-blocked because REE's functional channels are TONIC (instantaneous channel value is not a legibility map). Experiment A's dispositional readout -- 'which latent states are dispositionally coupled to future committed action' -- is exactly a legibility instrument reading disposition-toward-output rather than instantaneous value, so it is a candidate unblock. Follow-on confirmation task, not load-bearing for SD-064 closure; open pending someone checking whether the 723 J-space readout resolves MECH-191's tonic-channel problem."
  deferred_or_external:
    - note: "Experiment B ultimately resolves SD-064, which is v3_pending. If the SD-027 V3 top-k retrofit (GATE-B) is judged not worth building in V3, both GATE-B and B convert to deferred (SD-027 is otherwise v4-scoped) and SD-064 stays v3_pending into V4. Kept as open/blocked v3 nodes for now because the plan pre-registers the v3 retrofit as the intended unblock path -- but note (2026-07-10) A's read is now CONFOUNDED/UNRESOLVED, not positive (V3-EXQ-723a superseded the 723 positive with a competence-floor-confounded diffuse read), so the retrofit build has no live trigger until Experiment A is re-run on a competent substrate."
---

# Global Workspace + J-lens: design note

Owner claim: **SD-064** (REE instantiates a global-workspace-like access channel).
Related: SD-027 (selection gate, reframed), MECH-254 (top-k impl), MECH-089
(packaging), MECH-287 (broadcast queue), SD-037 (broadcast override),
MECH-007 (attention fragmentation), MECH-191 (cross-architecture signal legibility).
Registered: 2026-07-08. Status: candidate / v3_pending. **PROMOTES NOTHING.**

---

## 0. Why this doc exists

Anthropic's J-space / Jacobian-lens result (2026,
<https://www.anthropic.com/research/global-workspace>) found that a large,
capable model — under **no** design pressure to have one — spontaneously grew a
compact internal structure that behaves like a Global Workspace: a **few dozen
concepts at a time, < 10% of internal activity**, that is (a) **reportable**,
(b) **causally load-bearing for multi-step reasoning** (ablate it and multi-step
reasoning collapses to ~0 while fluency / sentiment / MCQ survive), and (c)
**bypassed by automatic processing**.

That is convergent evidence that a *capacity-limited, reportable,
integration-central broadcast channel* is an **attractor** for capable sequence
models. REE builds one on purpose (on biological grounds); Claude grew one. This
note banks the insight as a claim and lays out the two experiments that would
turn it from convergent analogy into REE-internal evidence.

Two framing points, kept honest throughout:

- **Access, not phenomenal.** Anthropic explicitly claim *access*-consciousness
  (Block's sense: globally available for report and control), **not** phenomenal
  consciousness. SD-064 makes the same access-functional claim only.
- **The J-lens is imperfect.** It captures single-token concepts, the entry
  mechanism is unknown, and the workspace they measured evolves over a single
  forward pass. REE's analogue is **recurrent / temporally extended** — arguably
  *closer* to Baars' actual (temporal) theatre than Claude's frozen snapshot.

---

## 1. The claim, and the hedge it retires

SD-027 established a capacity-limited **selection-for-broadcast gate** at the
E1/E2 → E3 boundary (pulvinar–TRN analogue), feeding MECH-089 theta-gamma
packaging, feeding E3. Its note said REE is *"distinct from global workspace
theory in that SD-027 does NOT commit to a single global workspace."*

**That hedge conflates two different things.** It reads GWT as requiring a
*unitary selector* — which MECH-007 ("attention must be fragmented across
control axes") rightly forbids. But GWT requires no unitary attender:

> GWT's backstage is a **fragmented population of specialists**; the workspace
> is a narrow **broadcast bus** over them, not a homunculus. A capacity-limited
> bus that fragmented processors write-compete into and read-broadcast from is
> *fully consistent with* MECH-007.

So REE does not merely *tolerate* a global workspace. Its
**selection (SD-027) + packaging (MECH-089) + broadcast (MECH-287 / SD-037)**
stack already *is* one, at the access-functional level. SD-064 owns that
commitment. SD-027 stays valid as the selection stage; MECH-007 is reconciled,
not violated.

### Explanatory pairing worth keeping in view
The psychosis / thought-broadcasting substrate claim (self-attribution
contamination) is the **same channel read from the opposite end**: SD-064 says
workspace content is *legible-for-broadcast to the system*; the psychosis claim
models an agent experiencing its *own* workspace content as *externally
attributed / broadcast*. A single mechanism, two readings — a nice internal
consistency check for both claims.

---

## 2. Experiment A — REE-native J-lens dispositional readout (RUNNABLE NOW)

**Question:** Does REE have a J-space? I.e. is there a **compact, reportable,
action-coupled** subspace of the latent state that (a) occupies a small fraction
of total activity and (b) is causally central to committed/integrative action —
the REE analogue of Anthropic's finding?

**Why runnable now:** this is a *post-hoc readout* over an existing trained
all-ON agent. It needs **no new substrate** — no SD-027 gate, no config flag. It
is a measurement, not a mechanism change. That makes it a clean **diagnostic**
(non_contributory, PROMOTES NOTHING).

**The REE J-lens — the port of Anthropic's method.** Their lens asks, per output
token: *what internal activation is this disposed to make the model emit later?*
REE has an explicit **action head**, so the natural port is:

> For each committed action class `c`, find the latent-state direction most
> **dispositionally predictive of committing `c` some horizon `H` later**.

Concretely, over a logged all-ON rollout (per-tick latent state `z_t` — the
E1/E2/E3 stack — and executed committed_class `c_{t+H}`):

1. Fit a linear dispositional map `J: z_t -> P(committed_class_{t+H})` (multinomial /
   ridge), for a small horizon set `H ∈ {1, 3, 5}`. `J`'s row space is the
   **REE J-space** — the directions in latent state that "vote" for future
   committed action.
2. **Compactness (the < 10% test):** what fraction of `z`-activity variance lies
   in the J-space (top-k singular directions of `J` capturing ≥ 90% of its
   action-predictive power)? Report `jspace_dim` and
   `jspace_activity_fraction`. Anthropic: few dozen dims, < 10%.
3. **Reportability proxy:** REE has no natural-language report head, so use the
   **broadcast substrate as the report analogue** — is J-space content
   preferentially what MECH-287 broadcasts / what SD-037 override reweights?
   Correlate per-tick J-space occupancy with broadcast-event emission.
4. **Automatic-bypass contrast:** does a *reactive* DV (single-step obstacle
   avoidance / immediate reward capture) load on the J-space, or is it
   J-space-independent? GWT predicts reactive behaviour bypasses the workspace.

**DVs:** `jspace_dim`, `jspace_activity_fraction`,
`action_pred_auc@H` (J-space vs full-state vs shuffled-null),
`broadcast_jspace_alignment`, `reactive_dv_jspace_dependence`.

**Readiness gate (self-route, never a verdict):** need ≥ N committed-action
transitions per class per seed for the map to be estimable (mirror the
V3-EXQ-719a MI-estimability floor pattern); else
`substrate_not_ready_requeue`. Shuffle-null (≥ 200x) + p95 for the AUC.

**Reading:**
- Compact + broadcast-aligned + reactive-independent → **positive J-space
  existence**; raises the SD-064 prior and *motivates the SD-027 V3 gate
  retrofit* that unlocks Experiment B.
- Diffuse / no compact action-coupled subspace → evidence *against* a single
  workspace, *for* the SD-027-original pluralist reading. Either way it is
  informative and cheap.

**Feeds MECH-191** (cross-architecture signal legibility, currently
substrate-blocked because functional channels are tonic): the dispositional
readout is exactly a *legibility instrument* — "which latent states are
dispositionally coupled to future committed action" is a legibility map REE
lacked. A working REE J-lens is a candidate unblock for MECH-191's tonic-channel
problem: it reads disposition-toward-output rather than instantaneous channel
value.

---

## 3. Experiment B — workspace-ablation cliff (SUBSTRATE-BLOCKED)

**Question:** Is the selection-for-broadcast channel a *genuine workspace* — i.e.
does ablating it produce a **cliff** (integrative/multi-step cognition → ~0,
reactive/automatic behaviour intact) rather than **graceful degradation**?

This is the sharpest test and the direct port of Anthropic's ablation result. It
is also the discriminator between SD-064 (cliff) and the SD-027-original
pluralist reading (graceful degradation via redundant distributed pathways).
MECH-254 already sketches the factorial: `{gate off, gate only, template only,
both on}`.

**Why blocked:** the SD-027 boundary gate is **not implemented in V3**. There is
no `sd027` / access-gate code in `ree-v3/ree_core`; SD-027 is v4-scoped with an
*optional* fixed-k top-k retrofit that was never built ("Not queuing an EXQ yet",
SD-027 evidence_quality_note). A gate-ablation experiment today would self-route
`substrate_not_ready` — the "642 trap" (a substrate-ceiling verdict self-routed
on an unbuilt substrate). **Do not queue it yet.**

**Prerequisite (the unblock):** an `/implement-substrate` build of the SD-027 /
MECH-254 **V3 top-k selection gate** — a `use_boundary_access_gate` flag
(no-op-default, byte-identical OFF) over the E1/E2 → E3 forwarding path, top-k
over active `z_world`/`z_self` components per heartbeat, with a hard ablation
mode (k → all, i.e. gate disabled) for the factorial. Once built + smoke-tested,
Experiment B becomes: run the MECH-254 four-cell factorial in a task that
*requires* multi-step committed-action integration (the conversion-ceiling /
committed-action-diversity surface is the natural fit — that DV is already the
one that has been ceiling-bound), DV = integrative competence + committed-action
diversity, and test for a **cliff vs graceful** ablation profile.

**Recommended sequencing:** run **A** first. A positive J-space result is the
evidence that justifies spending the retrofit build on **B**; a negative result
saves the build.

---

## 4. Caveats carried on SD-064

- **Access ≠ phenomenal.** SD-064 is access-functional only. No claim about
  experience.
- **Convergence ≠ confirmation.** The Anthropic result raises a prior; it is not
  REE evidence. Only Experiments A/B are.
- **REE is recurrent; Claude's J-space was single-pass.** This is a *divergence
  that favours REE* for the GWT analogy (temporal broadcast is the actual
  theatre), but it also means the readout must be computed *across* heartbeats,
  not within one forward pass.
- **Legibility is dual-use.** The eval-awareness / hidden-goal findings in the
  Anthropic work (suppressing "fake"/"fictional" patterns restored a
  previously-resisted harmful behaviour) are a reminder that a working REE J-lens
  is also a safety instrument relevant to the SENT-*/GOV-* ethics perimeter — a
  workspace legible to an interpreter is legible to an auditor.

---

## 5. Status ledger

| Item | State | Next |
|------|-------|------|
| SD-064 registered | done (candidate, v3_pending) | — |
| SD-027 cross-ref | done (non-destructive reframe note) | — |
| Experiment A (J-lens readout) | queued via /queue-experiment | needs a runner |
| Experiment B (ablation cliff) | design-only, substrate-blocked | needs SD-027 V3 gate retrofit (/implement-substrate) THEN queue; gate on A positive |
| MECH-191 unblock | hypothesised | confirm if A's dispositional readout resolves the tonic-channel legibility gap |
