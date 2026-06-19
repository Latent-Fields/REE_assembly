# MECH-443 + MECH-444 decide-whether-to-build — decision packet (2026-06-19)

**Status:**
- **MECH-443** (priority_weighted_replay_write_selection): DECISION = **(b) DESIGN GAP — buildable on the landed MECH-319 write primitive, but route one load-bearing open question first (falsifier-readout ceiling-independence + non-degeneracy); sequence any *behavioural/committed* validation behind the MECH-439 conversion ceiling.**
- **MECH-444** (staleness_gated_target_refresh_on_replay_write): DECISION = **(c) DON'T BUILD-yet — blocked behind MECH-443's build + a not-yet-existing target-recompute primitive; analogy-only biology; the more speculative leg.**

**Author:** session `mech443-444-decide-to-build-20260619T2159Z`. **Decision time:** 2026-06-19T22:00Z.
**Changes NO claim status. Builds NO code. Removes NO `ceiling_decision: deferred` marker** (see §5 for why both markers stay even under the (b) verdict). This packet is the durable resume primitive for the CDQ-005 deferred decide-whether-to-build step; it mirrors the structure/rigor of `mech_442_decide_to_build_2026-06-19.md`.

---

## 0. The question

CDQ-005 (MuZero/EfficientZero **reanalyze** intake, `REE_convergence/sources/muzero/`, COMPLETED; packet CPKT-MUZERO-REANALYZE-20260619) pulled through to two registered candidate claims that EXTEND the already-owned MECH-319 **binary** simulation-mode rule-write gate (block vs admit during ghost/replay/DMN; V3-EXQ-628 PASS/supports). Both target `arc_062_rule_apprehension:GAP-K` ("gating which replayed/imagined transitions may write to the rule layer").

- **MECH-319 owns WHETHER** the replay write channel is open (all-or-nothing).
- **MECH-443 = WHICH / HOW-STRONGLY**: when the channel is open, admitted transitions write in **graded priority order** weighted by an update-utility (surprise / value-prediction-error / coverage) proxy.
- **MECH-444 = FRESHNESS**: each admitted write's target is **recomputed against the current model before it updates the rule layer** (MuZero reanalyze), down-weighting low-drift writes.

User framing (carried from the MECH-442 packet): *if it is just to build then build away; but if there are things about the build to be decided then we need to ask convergence or lit-pull or something else.* And the load-bearing caution attached to this pair: **a graded replay-write priority INTO a rule layer that cannot yet convert diversity to committed action may be premature.** This packet adjudicates both legs against that caution.

---

## 1. Dependency-state resolution (explicit)

| dep | state today | bearing on the build |
|---|---|---|
| **MECH-319** | **provisional, `v3_pending: false`**; V3-EXQ-628 PASS. Binary gate **LANDED**: `ree-v3/ree_core/regulators/simulation_mode_rule_gate.py` (`SimulationModeRuleGate.effective_simulation_mode(...) -> bool`), wired at the `GatedPolicy.forward` + `LateralPFCAnalog.update` replay call sites. | **The substrate to build ON exists.** The `admit_writes=True` path (the 628 falsifier control) is the concrete substrate where a graded write replaces a uniform admit. ✓ |
| **MECH-094** | **stable.** | The hypothesis-tag write-gate principle both legs refine; no blocker. ✓ |
| **MECH-312** | **candidate, `v3_pending: true`, `epistemic_category: substrate_conditional`** — suppressed pending the ARC-063 rule-creator substrate (design-only 2026-06-04, NOT built); not yet experimentally tested. | **NOT a hard build blocker for the WRITE primitive.** MECH-443 grades writes to the *existing* single-vector `rule_state` EMA in `LateralPFCAnalog`, which is present and independent of the unbuilt MECH-312 multi-channel (a/b/c/d + multiplicative-gate / ARC-063) machinery. The `depends_on: MECH-312` is a lineage pointer (the rule-arbitration *layer*), not a gate on the write enrichment. **Caveat:** MECH-312 being experimentally unvalidated means the *behavioural relevance* of the rule layer is itself unproven — which folds into the conversion-ceiling concern below, not into a build-feasibility block. |
| **ARC-062 + MECH-439 conversion ceiling** | gated_policy substrate **implemented** (V3-EXQ-542a PASS), but **the rule-apprehension channel is downstream-capped by F-dominance.** V3-EXQ-654g (TODAY): C1 fully met (CRF propagation non-vacuous, `crf_frac_active` 0.58–0.94, the rule channel *reaches* the accumulator), C2 FAIL (committed-class entropy lift +0.011 nats, 0/3 seeds). Seed-44 `ARM_ON==ARM_OFF` committed distribution **byte-identical despite live CRF (frac_active 0.78)** = purest conversion-ceiling signature in the lineage. **And** 654g armed the 569i-validated top-k lever and the ceiling *still* persisted → the top-k bypass is **channel-specific (rescues GAP-A modulatory bias, does NOT transfer to the CRF `rule_state` channel)**. | **This is the load-bearing dependency.** It does NOT block building the graded write. It blocks *demonstrating value via a committed/behavioural readout*: the very channel MECH-443 writes to (CRF `rule_state`) is the one 654g showed cannot move the F-dominated argmax, AND cannot be rescued by the proven top-k bypass. Any MECH-443 falsifier resting on committed-rule entropy would self-route/null exactly like 654g. |

**Build-locus reality check (grounds "buildable now"):** `LateralPFCAnalog.update(..., gate: float in [0,1], ...)` already performs a **gate-modulated EMA**: `rule_state ~ (1 - base_eta*gate)*rule_state + base_eta*gate*source`. The per-call write **strength is already a continuous scalar** (`base_eta*gate`). MECH-443's "how strongly" is therefore a *natural* extension of an existing knob — modulate `gate`/effective-eta per admitted transition by a priority weight. By default `write_gate("sd_033a") ≈ 0.05` under `internal_replay` (replay content is normally near-frozen out); `admit_writes=True` (628) opens it. So the graded-write ablation has a concrete, present substrate. **No substrate_queue entry references MECH-443 or MECH-444** (grep = 0), confirming neither is self-implemented and neither has a routing home yet.

---

## 2. MECH-443 — priority_weighted_replay_write_selection

### 2.1 Mechanism gap over MECH-319's binary gate (one line)
MECH-319 decides *whether* a replay pass may write to `rule_state`; MECH-443 adds a **graded ordering over the admitted writes** — high-update-utility transitions write strongly, low-utility ones weakly or not at all — turning an all-or-nothing admit into a priority-weighted admit at the same `LateralPFCAnalog.update` locus.

### 2.2 Design-parameter audit (SETTLED vs OPEN)

| parameter | status | basis |
|---|---|---|
| **Priority semantics** (update-utility, NOT reward magnitude) | **SETTLED** | Mattar & Daw 2018 (gain × need / EVB; supports 0.79) fixes the *form*: priority = value-of-the-update. Carey et al. 2019 (mixed 0.62) is the load-bearing counterweight — replay biases *away* from the currently-preferred outcome, so equating priority with reward level or committed-policy value is **biologically falsified**. The claim already encodes this. |
| **Priority *proxy* on the REE substrate** (which surprise / value-PE signal scores priority) | **OPEN** | Mattar summary states it plainly: *"Gain cannot be read off the REE substrate directly; it has to be operationalized as a surprise or value-prediction-error proxy."* REE's rule layer is a parametric EMA over `rule_state`, not a tabular value function. Candidate proxies (E2 forward-PE; `rule_state`-delta magnitude; coverage/need over visited contexts) are un-disambiguated. This is the *one* genuinely open *internal* design fork. |
| **Write-strength scaling** (priority → write magnitude) | **SUBSTANTIALLY SETTLED** | The `gate`/`base_eta` EMA knob already accepts a continuous per-call strength. Mapping priority→strength (linear vs softmax-normalised) is a calibration knob decided at build, **constrained by the pre-registered matched-total-write-mass guard** (so "priority helps only by writing more" is controlled, not open). |
| **Integration locus** | **SETTLED** | Extend `effective_simulation_mode(...)` to carry a per-transition priority weight at the `LateralPFCAnalog.update` call site (claim + CPKT both name this). Concrete, present. |
| **Falsifier READOUT** — rule-arbitration retention/selectivity **vs** committed-rule entropy | **OPEN, and load-bearing** | The claim offers *both*. The **rule-layer retention/selectivity** readout is **ceiling-independent** (measured at `rule_state`, upstream of the F-dominated E3 commit; MECH-443 lives in GAP-K replay-write-gating, NOT GAP-B committed-action-conversion). The **committed-rule-entropy** readout is **ceiling-gated** (654g: this exact channel cannot move the argmax, and the top-k bypass does not reach it). Resolving which readout the falsifier rests on — and confirming it is **non-degenerate** under `admit_writes=True` on the current substrate (does admitted replay actually move `rule_state` enough that priority-ordering can out-perform uniform-admit?) — is the gating question. |

### 2.3 Dependency verdict
**Buildable now on the landed MECH-319 substrate** — the write primitive exists and already carries a continuous strength; MECH-312's unbuilt multi-channel machinery does **not** gate it; the priority *form* is settled. The build is **not** gated on MECH-312 *as a substrate*. It **is** conditionally gated on the MECH-439 conversion ceiling **only for a committed/behavioural readout** — and that channel is doubly-capped (F-dominance + top-k-bypass-doesn't-transfer, 654g). The core GAP-K falsifier (rule-layer retention/selectivity under a matched-mass control) is **orthogonal to the ceiling**, provided it is non-degenerate.

### 2.4 Recommendation — (b) DESIGN GAP
Not (a) JUST BUILD: two things are unresolved — (i) the priority-proxy choice, and (ii) the falsifier-readout / non-degeneracy question that determines whether the build is even ceiling-independent.
Not (c) DON'T-BUILD: the build is feasible on landed substrate, the design is mostly settled, and the core falsifier need not touch the conversion ceiling.

**Route (both questions are INTERNAL — lit and convergence are already discharged; do NOT re-open them):**

- **Q1 (go/no-go, cheap) — falsifier-readout spec + non-degeneracy probe.** Specify MECH-443's falsifier on the **rule-arbitration retention/selectivity** readout (NOT committed-rule entropy), and run a *cheap instrumentation diagnostic* on the existing `admit_writes=True` (628) substrate: under uniform admit, does replay move `rule_state` enough that a retention/selectivity metric varies non-degenerately across seeds? **If non-degenerate → proceed to build** the priority-weighted-admit ablation (matched-total-write-mass guard, priority = surprise-proxy). **If degenerate** (admitted replay barely moves `rule_state` on the current substrate) → MECH-443 flips to (c), blocked on a replay-write-magnitude substrate enrichment, NOT on MECH-439.
- **Q2 (sequencing) — any COMMITTED/behavioural validation of MECH-443 is sequenced BEHIND the MECH-439 F-rebalance.** 654g proved the `rule_state` channel cannot convert to committed action today and the top-k bypass does not reach it. Do not design a committed-action MECH-443 falsifier until the conversion ceiling lifts via an F-variance-share rebalance (the 689a chain), mirroring how the 485h OFC and 654g GAP-B retests were sequenced.
- **Priority-proxy fork** (Q1's build step): pick the surprise/value-PE proxy at build time from the E2 forward-PE work (DR-12 / SELF-4 adjacency) vs a `rule_state`-delta proxy; this is a build-time choice, not a blocker.

**Build trigger:** Q1 non-degeneracy probe returns non-degenerate. **Revert/abandon trigger:** Q1 degenerate → re-route to substrate enrichment; or a built ablation shows priority-weighting inert vs matched-mass uniform admit (the claim's own falsifier) → MECH-443 earns no keep.

---

## 3. MECH-444 — staleness_gated_target_refresh_on_replay_write

### 3.1 Mechanism gap over MECH-319 (one line)
On each admitted write, **recompute the target against the current model** and down-weight/skip it when it has not drifted from the stored (ghost-derived) target — the MuZero reanalyze trick, guarding the overcommitment-to-stale-ghost-weights failure MECH-319 exists to prevent from re-entering through the prioritized write channel MECH-443 opens.

### 3.2 Design-parameter audit (SETTLED vs OPEN)

| parameter | status | basis |
|---|---|---|
| **Staleness metric** (what "drift" means) | **OPEN** | Mattar & Daw's *gain* term is the biological shadow ("a backup has high gain exactly when the stored target no longer reflects what the current model would compute"), but it is *supported by analogy only* — **no recording demonstrates a literal recompute-then-write cellular operation** (the claim's own HONEST CAVEAT). The REE drift metric (||recomputed_target − stored_target|| in `rule_state` units? a value-PE delta?) is unspecified. |
| **Refresh-vs-store rule** (recompute cadence; down-weight curve) | **OPEN** | The reanalyze cadence (recompute every admitted write? sampled?) and the low-drift down-weight/skip threshold are engineering constructs with no biological pin. |
| **Integration locus** | **SETTLED-as-a-target, but the primitive does NOT exist** | Same `LateralPFCAnalog.update` path — but the current primitive writes `source` **verbatim** via EMA; a **target-recompute-and-compare step does not exist** and cannot be added without enriching the write primitive (genuine `substrate_ceiling`). |
| **Composition with MECH-443** | **SETTLED (ordering)** | `depends_on: MECH-443`; priority (443) and freshness (444) "must operate together." MECH-444 is downstream of, and gated on, MECH-443 being built. CPKT rollback condition is explicit: *"MECH-444 must not drive a build on its own."* |

### 3.3 Dependency verdict
**NOT buildable now.** Three serial blockers: (1) it composes downstream of MECH-443, whose build is itself gated on §2.4-Q1; (2) it needs a **new target-recompute-and-compare primitive** the EMA write path lacks; (3) its biological warrant is **analogy-only** (Mattar gain term + Olafsdottir generative preplay), the weakest in the CDQ-005 pair. Its falsifier *substrate* is favourable (attenuate `rule_state` drift on the 628 `admit_writes=True` lineage — a rule-layer property, more ceiling-independent than committed action), but that does not help while the upstream blockers stand.

### 3.4 Recommendation — (c) DON'T BUILD-yet
**Blocking upstream:** MECH-443 must be built and shown to keep over matched-mass uniform admit (§2.4), AND a target-recompute primitive must be scoped. **Revisit trigger:** MECH-443 built + earns its keep → then scope the recompute primitive and re-open MECH-444 against the 628 drift substrate. **Abandon trigger:** MECH-443 fails to keep, OR the recompute step shows no drift-attenuation vs stale-target writing (the claim's own falsifier).

---

## 4. Why this respects V3 primacy

Both claims `AMEND` the GAP-K replay-write locus; **neither owns or blocks any V3 closure node** (`blocks_v3_critical_path: false`; CPKT MZ-BENCH-002 = V3 closure % unchanged). This packet proposes **no** dependency from a V3 closure node onto either claim, queues **no** experiment, and changes **no** status. The §2.4-Q1 probe, if the user elects to run it, is a *diagnostic* on existing substrate, not a closure-path commitment.

---

## 5. Disposition — both `ceiling_decision: deferred` markers STAY (claims.yaml untouched)

The task permits removing a marker for a JUST-BUILD or *clean* DESIGN-GAP verdict. **Both markers are left in place**, for two concrete reasons:

1. **Removing a marker re-creates an orphan flag.** `check_substrate_ceiling_audit.py` treats a `substrate_ceiling` claim as not-orphaned only when it (a) carries `ceiling_decision: deferred`, (b) has a `substrate_queue` entry with `sd_id == claim id`, or (c) is already mapped. Neither MECH-443 nor MECH-444 has a substrate_queue entry (grep = 0). Removing the marker without simultaneously creating a routing home would revert the 2026-06-19T19:17Z park session and re-flag the claim as a genuine orphan every Step-6a-v cycle. Creating that routing home (a substrate_queue entry) is a *queue/build* action outside this packet's "change no status, build no code" remit and the user's call.
2. **MECH-443's (b) verdict is design-gap-with-a-go/no-go-probe, not build-now.** Its first routed step (§2.4-Q1) is a non-degeneracy diagnostic whose outcome can still flip the claim to (c). That is not a *clean* design-gap that has concluded in build-intent; the deferral is still live until the probe returns. MECH-444 is unambiguously (c).

This packet **is** the durable decide-to-build record the markers point at. When the user elects to act, the marker-removal should coincide with creating the routing home (the Q1 probe's queue entry for MECH-443), so the audit sees it as *mapped/routed* rather than orphaned.

---

## 6. Concrete next actions (await user confirmation before executing)

1. **(MECH-443, optional, cheap)** Run the §2.4-Q1 non-degeneracy diagnostic on the existing `admit_writes=True` (628) substrate: a rule-arbitration retention/selectivity metric under uniform admit. Non-degenerate → queue the priority-weighted-vs-uniform-admit ablation (matched-total-write-mass guard; priority = surprise-proxy NOT reward) and remove MECH-443's marker as part of that queueing. Degenerate → re-route to a replay-write-magnitude substrate enrichment.
2. **(MECH-443, committed readout)** Do NOT design a committed-action MECH-443 falsifier until the MECH-439 F-rebalance (689a chain) lifts the conversion ceiling; the `rule_state` channel is doubly-capped today (654g).
3. **(MECH-444)** Hold. Re-open only after MECH-443 is built and keeps, and after a target-recompute primitive is scoped. Marker stays.
4. **No claims.yaml / claims.json / substrate_queue edits in this packet.** CDQ-005 row updated to record the packet + verdicts.

**Disposition unchanged:** MECH-443 + MECH-444 stay `candidate / substrate_ceiling / generation:v3 / v3_pending:true / ceiling_decision:deferred`, OFF the V3 critical path, AMENDING `arc_062_rule_apprehension:GAP-K`. This packet replaces the prose *"decide-whether-to-build is a later governance step"* with concrete, routed decisions: MECH-443 = (b) buildable-after-a-go/no-go-probe, behavioural validation sequenced behind MECH-439; MECH-444 = (c) hold behind MECH-443 + a new recompute primitive.
