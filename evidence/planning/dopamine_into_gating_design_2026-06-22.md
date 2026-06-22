---
design_note:
  id: dopamine_into_gating
  title: "Learned dopamine-gated E3 gating vs the pure-arithmetic envelope (the next MECH-439 attack)"
  registered: 2026-06-22
  last_updated: 2026-06-22
  generation: v3
  status: design_proposal
  decides: "Whether the next attack on the F-dominance conversion ceiling (MECH-439) is a LEARNED, signed-RPE-driven adjustment of E3 per-channel selection weights, or another pure-arithmetic envelope lever."
  scope_claims: [MECH-439, ARC-107, MECH-448, MECH-449, MECH-447, ARC-016, MECH-260]
  proposes_claims: [MECH-BG-LEARN-1, MECH-BG-SETTLE-1]   # provisional working ids; mint via /thought-digestion intake into claims.yaml (NOT done here)
  derived_from: "basal_ganglia_assembly_map_2026-06-22.md (A.4 the learning gap; C1/C3 the recurrent-settling repair; E.3 next-steps); arc_107_selector_constitution_design_2026-06-20.md (s3, s6b); grounded against ree-v3/ree_core/predictors/e3_selector.py"
  cross_plan_home: [basal_ganglia_assembly_map, conversion_ceiling_campaign, biology_grounding_convergence_v4]
  promotes_nothing: true
---

# Learned dopamine-gated E3 gating vs the pure-arithmetic envelope

**What this is.** The design note the BG assembly map (`basal_ganglia_assembly_map_2026-06-22.md`)
§E.3 calls for: the decision on whether to attack the live F-dominance root
(MECH-439) by giving the E3 selector a **learned, dopamine-gated** adjustment of
its per-channel selection weights — versus continuing the **pure-arithmetic
envelope** campaign (MECH-447/448/449 + the modulatory-authority/route-range/
shortlist/top-k lineage).

**The decision (headline).** **Build the minimal learned-gating mechanism as the
next MECH-439 attack, COMPOSED on top of the arithmetic envelope (not replacing
it), and COUPLED to a minimal recurrent-settling step.** Keep the arithmetic
envelope as the *bounded, safety-bearing eligibility frame*; add learning as the
thing that decides *which channel's bias wins inside that frame, by experience*.
Scope the V3 build to a single signed-RPE-driven per-channel weight vector plus a
few-round settling update; defer the full BG-thalamo-cortical learned loop to V4.

This note is a **design decision + pre-registered falsifier**. It PROMOTES
NOTHING and mints no claims.yaml entry; the working claim ids in the frontmatter
are placeholders for a follow-on `/thought-digestion` intake.

---

## 1. Why this is the right next move (the argument from the failure history)

The assembly map §A.4 states the root precisely: the ARC-107 selection
*constitution* — MECH-448 eligibility envelope, MECH-449 Go/No-Go, MECH-447
conflict-grade, the modulatory-bias-selection-authority rescale — is **pure
arithmetic with no learned parameters and no gradient flow** (confirmed against
`e3_selector.py`: `_f_eligibility_envelope`, `_go_nogo_eligibility_gate`,
`_gap_scaled_commit_pick`, and the authority/route-range block are all
hand-specified regulators). Learning exists only at the **valuation** layer
(`harm_eval_head`, `benefit_eval_head`, `reality_scorer`). The *arbitration* does
not learn.

In biology the cortico-striatal weights that decide which channel wins selection
authority are themselves learned by three-factor plasticity (Hebbian
co-activation × dopaminergic RPE), with the D1-LTP / D2-LTD asymmetry. **F
monopolises 88-89% of E3 committed-selection variance (V3-EXQ-571) precisely
because there is no learned striatal weighting that can re-weight channels
through experience** — every diversity channel is a fixed-magnitude bias
competing against a fixed primary score.

The decisive evidence that *learning*, not *more arithmetic*, is the right lever
is the **shape of the campaign's own failure history** (assembly map §C1):

- Parametric tuning of the selection readout was repeatedly **falsified** —
  gain-calibration (514t), candidate-pool (569h diverse-input/flat-output),
  std-basis authority (569h 1/3).
- The only positive levers were **structural bounding** — 569i top-k shortlist
  PASS (2/3, but *thin*: 0.711 vs proposer 0.650; 689d demotion PASS 2x).
- And every structural lever then needed its **own per-channel calibration** —
  the floor dances (654h all-admit no-op; 485i/485j bespoke floor; the MECH-448
  mean-adaptive amend) are REE *rediscovering, by hand, that the right operation
  is learned relative re-weighting* rather than a fixed threshold.

"Structural bounding works, parametric tuning does not, and each structural lever
needs hand-calibration per channel" is the signature of a system that needs a
different *selection rule that learns its weights*, not a better hand-set weight.
Seven successive GAP-A/B arithmetic amends are hand-emulating one learning rule.

**Counter-position considered and rejected.** "Keep patching the envelope — it is
landing, cheap, and bit-identical-OFF." Rejected because (a) the patches compound
(every lever adds its own per-channel calibration surface), (b) the *composition*
of levers is itself now an open experiment (the conversion_ceiling_campaign:P-comp
node — MECH-448 demotion × MECH-449 Go/No-Go, V3-EXQ-699 queued — has unknown
interaction), and (c) the demotion lever's "behead the monarch" framing (divergence
B2) is itself converging back toward "learn F's weight down where the modulator
matters" (assembly map §C2). The envelope is doing, by hand and per-channel, what
one learning rule would do natively. That is the standing argument to add learning.

---

## 2. The minimal V3-tractable learned-gating mechanism (deliverable a)

### 2.1 What learns, and on what signal

A **single learned per-channel selection-weight vector** `w_chan ∈ R^C` over the
C modulatory/diversity channels that already feed the E3 accumulator
(`_modulatory_accum`: dACC SD-032b, lPFC SD-033a, OFC SD-033b, MECH-295 liking,
MECH-314 curiosity, MECH-320 vigor, MECH-341 entropy, route-range coherence, and
the primary F itself as channel 0). The composed pre-authority bias becomes a
**weighted** sum:

```
modulatory_accum = Σ_c  softplus(w_chan[c]) · channel_bias_c     # was: Σ_c channel_bias_c (w≡1)
```

`w_chan` is the one new learned object. `softplus` keeps weights non-negative
(a channel can be turned down toward zero but not sign-flipped — sign lives in the
channel's own bias). At init `w_chan` is set so `softplus(w_chan[c]) ≈ 1` for all
c → **bit-identical to the current unweighted accumulator** (the no-op-default
guarantee).

### 2.2 The teaching signal: a SIGNED RPE, explicitly distinct from ARC-016 (divergence B5)

The update is driven by a **signed dopaminergic-RPE analog** δ_t — *better/worse
than expected* — NOT by the unsigned prediction-error *variance* ARC-016 already
computes (assembly map divergence **B5**; the `e3._running_variance` precision
signal). This distinction is load-bearing and is the whole reason a new signal is
needed:

| Signal | Type | What it is in REE today | Role |
|---|---|---|---|
| ARC-016 precision (`_running_variance`) | **unsigned magnitude** | E3 world-forward PE variance | commit-threshold / precision gating |
| **δ_t (this note)** | **signed scalar** | **NOT present today** | the directional teaching term for D1-up / D2-down channel re-weighting |

An unsigned variance *cannot* tell "raise this channel's authority" from "lower
it" — it has no sign, so it cannot supply the directional credit a learned gate
needs (B5: "a category substitution that will silently block three-factor
learning"). The minimal δ_t REE can form **without new substrate**:

```
δ_t = R_t − V̂_t
  R_t = realised outcome valence of the committed action   (− harm_eval gain at the resulting state; reuse the trained valuation heads)
  V̂_t = a slow EMA baseline of R over recent commits        (the "expected" term; one scalar, leaky-integrator)
```

This is the average-reward-RPE form (cf. MECH-320's Niv-2007 EWMA, reused). It is
signed by construction (R above/below baseline), and it reuses the *already-trained*
valuation heads for R_t — so no new encoder, no new latent target, no phased
training of a head.

### 2.3 The three-factor update (Hebbian co-activation × signed RPE), with D1/D2 asymmetry

```
eligibility_c = | channel_bias_c[selected] |          # how much channel c spoke for the committed action this tick (Hebbian co-activation trace)
Δw_chan[c]    = η · δ_t · eligibility_c · asym(c, δ_t)
```

`asym` renders the D1-LTP / D2-LTD asymmetry **at the parameter level** without
needing two separate populations (the V3 simplification of divergence B4): a
positive δ_t potentiates the channels that voted for the rewarded action faster
than a negative δ_t depresses them (e.g. `asym = 1` when `sign(δ_t)·channel_vote`
agrees, `< 1` otherwise). This is the *minimal* rendering — a single signed weight
vector with asymmetric gain — not the full D1/D2 opponent split (assembly map
§A.5 item 2, A.2 "D1/D2 population split" = **MISSING**, deferred to a later build).

An **eligibility trace** over the last K ticks (decayed) credits the channels
active when an outcome arrives — the standard reverse-credit window, and the same
shape REE already uses in the ARC-063 CRF eligibility credit and the SD-058
avoidance-efficacy trace.

### 2.4 Why this is V3-tractable and safe

- **No new module surface beyond one weight vector + one baseline scalar + one
  trace.** It lives as an optional learned pre-step on the existing
  `_modulatory_accum` composition site in `select_action` / `e3_selector.select`.
- **Pure addition to a trained-substrate path**, gated `use_learned_channel_gating`
  (default False → bit-identical OFF), like every other lever in the lineage.
- **MECH-094:** the update runs only on the waking committed-selection path; a
  replay/DMN tick is a no-op (no δ_t formed, no `w_chan` write) — the standard
  simulation_mode gate.
- **Safety is inherited from the envelope** (see §3): because the learned weights
  act *inside* the F-bounded eligible set (MECH-448 envelope + MECH-449 No-Go
  already excluded clearly-harmful candidates), no learned re-weighting can
  promote a candidate the safety gate removed. This is the single most important
  reason to **compose, not replace** (§3).

---

## 3. Compose with, not replace, the arithmetic envelope (deliverable b)

**Decision: COMPOSE.** Learning sits *inside* the arithmetic eligibility frame,
not in place of it.

- **The envelope stays as the bounded eligibility + safety frame.** MECH-448
  (rank-preserving F→eligibility demotion) and MECH-449 (Go/No-Go suppression of
  unsafe/stale/perseverative/low-viability candidates) decide *who is eligible to
  compete*. These are the **safety guarantees** — a clearly-harmful or
  surround-inhibited candidate is removed from the eligible set before any learned
  weighting is applied. A learned gate must never be able to re-admit it.
- **Learning decides the within-eligible winner by experience.** `w_chan`
  re-weights the channels' votes *over the eligible set only*. This is exactly the
  biological division: the pallidal permission gate (arithmetic, F-bounded) sets
  eligibility; the learned cortico-striatal weights set which eligible channel
  wins.
- **The F-deletion lever (MECH-448 / divergence B2) is re-examined, not removed,
  once learning lands.** Assembly map §C2: the "behead the monarch" absolute
  F-deletion is a stand-in for "F's weight should be *learned down* in contexts
  where the modulator matters." With `w_chan[0]` (F's own learned weight) free,
  the system can learn to demote F *contextually* instead of deleting it by a
  hand-set floor. Prediction: once learning lands, the demotion lever either
  becomes unnecessary (learning re-weights F naturally) or reduces to a faithful
  pooled-symmetric divisive normalisation. **Do not add more absolute-floor
  letters** in the meantime (§C2 standing instruction).

Replacing the envelope was rejected: it would discard the only landed,
safety-bearing, bit-identical-OFF components of the constitution (MECH-448
provisional via 689d; MECH-449 built+validated via 689g) and re-open the safety
surface a learned gate cannot itself guarantee.

---

## 4. Coupling to the minimal recurrent-settling step (deliverable c)

The assembly map argues (§C1, §C3, and §A.5 sequencing) that learned gating and a
recurrent-settling competition are **coupled**: in biology the lateral-inhibition
weights that run the settling competition are *themselves learned*. So the two
repairs share a substrate and should be built together, minimally.

### 4.1 The minimal settling step

A **bounded iterative settling** over the eligible set before the commit —
a few rounds of mutual-inhibition updates on `_modulatory_accum` (assembly map
§C1 "strictly more than the argmin, strictly less than a full learned loop"):

```
for r in range(R):                       # R small, e.g. 2-4
    a = softmax(accum / T)               # current support over eligible candidates
    accum = accum − W_lat · a            # lateral inhibition: each candidate suppresses rivals
commit = argmin(accum)   (committed)  /  sample(softmax(accum/T))  (uncommitted)
```

This is the structural fix for divergence **B3-blend** (the additive
`_modulatory_accum` is a *blend* where biology has surround inhibition that
prevents co-activation) AND for **B1** (one-shot argmin → recurrent settling) —
the same V3 experiment addresses both (assembly map §C3 disposition). A settling
competition can *flip the attractor* a strong modulator should win, which a hard
argmin over an F-dominated score structurally cannot (§C1).

### 4.2 The coupling: the lateral-inhibition weights `W_lat` are learned by the SAME δ_t

`W_lat` (the mutual-inhibition strengths between channels/candidate classes) is
**not** hand-set. It is learned by the **same signed-RPE three-factor rule** as
`w_chan` (§2.3) — that is the literal content of "the lateral-inhibition weights
are themselves learned." Minimal V3 rendering: a low-rank or per-channel-class
`W_lat` updated by `Δ W_lat ∝ δ_t · (a_i a_j)` over the settling-step activations
(Hebbian co-activation of competing channels, gated by signed RPE). At init
`W_lat ≈ 0` → the settling step is a no-op → bit-identical OFF.

So the unified build is: **one signed RPE δ_t drives both the per-channel selection
weights `w_chan` and the lateral-inhibition weights `W_lat`; the settling step is
the few-round competition those weights parametrise.** This is the smallest object
that makes "learn to select" real in V3 while staying inside the safety envelope.

### 4.3 Sequencing

Per assembly map §A.5 the dopamine-into-gating question is the **highest-leverage**
item and bears directly on the live root. Build order:

1. **`w_chan` + δ_t** alone first (settling OFF, `W_lat=0`): isolates "does a
   learned per-channel weight convert where the fixed weight plateaus?" — the
   cleanest single-variable test.
2. **Add the settling step + learned `W_lat`** as the second factor: isolates
   "does a learned recurrent competition add lift beyond a learned static weight?"
3. They compose as a 2×2 (learned-weight × learned-settling), mirroring the
   P-comp 2×2 already in flight (V3-EXQ-699).

---

## 5. Pre-registered falsifier (deliverable d)

The discriminating question: **does learned gating convert diversity into
committed action where the arithmetic envelope plateaus** — or is there no lift?

### 5.1 Design

On the **GAP-A-ready foraging substrate** (SD-056-trained `e2.world_forward` +
ARC-065 GAP-A `candidate_summary_source=e2_world_forward` → a genuinely divergent
candidate pool; the non-vacuity precondition every conversion-ceiling experiment
now requires). 2×2 factorial, all arms carry the landed envelope (MECH-448
adaptive-floor demotion ON + MECH-449 Go/No-Go ON + modulatory-authority/top-k
shortlist constant):

| Arm | learned `w_chan`+δ_t | learned-settling (`W_lat`) |
|---|---|---|
| A0 (envelope-only control) | off | off |
| A1 | **on** | off |
| A2 | off | **on** |
| A3 | **on** | **on** |

3 seeds. `experiment_purpose=evidence`. `claim_ids=[MECH-439]` (+ the minted
learned-gating claim once registered). Supersedes nothing; new EXQ id.

### 5.2 Primary acceptance (the discriminator)

**Committed-action-class entropy must rise with learning, strict-above BOTH a
matched-noise control AND the A0 envelope-only arm, on ≥2/3 seeds**, AND the lift
must be attributable to learning:

- **C1 (conversion):** A1 (and/or A3) committed-class entropy strict-above A0 and
  above a verified-lifting matched-noise temperature control (the 569g/569h
  lesson: an entropy lift that a noise control also produces is *not* lawful
  conversion).
- **C2 (learning is load-bearing, the core discriminator):** the lift must
  **grow over training** — committed-class entropy in the second half of the run
  strictly exceeds the first half on the learning arms, and the channel weights
  `w_chan` (and `W_lat`) must have **moved** from init (‖Δw‖ > floor). A lift that
  is present from tick 0 and does not grow is *not* learned gating — it is a
  static re-weighting and should be folded back into the arithmetic lever instead.
- **C3 (RPE sign is load-bearing, falsifies B5-collapse):** an ablation arm that
  swaps the signed δ_t for the **unsigned** ARC-016 variance magnitude must
  **fail to convert** (no entropy lift / no directed `w_chan` movement). If
  unsigned variance converts just as well, the signed-RPE claim is refuted and the
  whole mechanism collapses to a precision re-weighting — route back to ARC-016,
  do not mint a new claim.

### 5.3 Non-vacuity / self-route (never a false weakening)

The run self-routes `substrate_not_ready_requeue` (NOT a MECH-439 weakening) if
any precondition is unmet: candidate pool not divergent
(`cand_world_pairwise_dist` below floor), δ_t flat (no outcome variance to learn
from), or `w_chan`/`W_lat` never move (eligibility trace never credited). A
**preconditions-met FAIL** (learning engaged, weights moved, pool divergent, but
no entropy lift over A0) is the genuine **"no lift" outcome** → routes to the V4
full-loop scope bet (§6), it does NOT falsify ARC-107 (the envelope still holds)
and does NOT promote learned gating.

### 5.4 The four-way verdict grid

| C1 conversion | C2 grows-with-training | Verdict |
|---|---|---|
| yes | yes | **learned gating converts where arithmetic plateaus** → mint + promote-toward; demotion lever re-examined (§3) |
| yes | no | static re-weighting, not learning → fold the winning static weights into the arithmetic lever; do NOT mint a learning claim |
| no | — (preconditions met) | **no lift** → MECH-439 V3-tractable space is exhausted at the selection face; escalate to the V4 full BG-thalamo-cortical loop (§6) |
| no | — (preconditions unmet) | substrate_not_ready_requeue (vacuous; fix the pool/δ_t, re-run) |

---

## 6. The scope bet: V3 minimal vs V4 full loop (deliverable e)

**Stated bet (ARC-106 zero-silent-divergence): the V3 build is the minimal learned
gate — one signed-RPE δ_t, one per-channel weight vector `w_chan`, one learned
lateral-inhibition `W_lat`, a few-round settling step — and NOT the full
BG-thalamo-cortical learned loop.** The following are explicitly deferred to V4 and
registered as named, falsifiable cuts (extending the ARC-107 §6b V4-axes table and
the assembly map §A.5 sequencing):

| Deferred axis | Why V4 | Bet to register |
|---|---|---|
| **D1/D2 population split** (two opponent populations with asymmetric dopamine gain) | the minimal rule renders the asymmetry as a parameter (`asym`), not two populations; the split is required only to *earn* the Parkinson/dyskinesia/Huntington/ICD psychiatric-failure axis (ARC-106 EARNS) | "V3 renders D1/D2 asymmetry as a single asymmetric-gain weight; the opponent-population split is V4 and is what earns the disease axis." |
| **Lateral-habenula negative-RPE drain** (assembly map A.3) | falls out of a full signed-RPE substrate; the minimal δ_t is an internal scalar, not a routed efferent drain | "V3 forms δ_t as an internal scalar; the habenula negative-RPE *output drain* is V4." |
| **Full thalamo-cortical recurrent settling loop** (extended, learned, multi-step over a real thalamus module) | V3 has no thalamus module (assembly map A.2 `thalam` = comments); the minimal settling is a few-round in-place competition, not a loop | "V3 closes the loop with a bounded in-place settling step + learned `W_lat`, not an explicit thalamo-cortical oscillation." (sharpens the existing ARC-107 §6b 'Thalamocortical recurrence' bet) |
| **TAN cholinergic plasticity-window gating** (assembly map A.2) | the TAN-pause-coincident-with-DA-burst defines the learning window; V3 uses a plain eligibility trace | "V3 uses a decayed eligibility trace as the plasticity window; the TAN-pause gate is V4." |
| **Loop segregation** (parallel motor/assoc/limbic loops; assembly map §D) | V3 collapses to one E3 selector; pulling segregation forward is conditional on the §5 falsifier leaving MECH-439 unresolved | "V3 learns one shared channel-weight vector over one collapsed arena; per-loop learned gating is V4 unless §5 returns no-lift." |

**The bet's escape hatch is the §5.4 'no lift (preconditions met)' verdict.** If
the minimal learned gate does not convert on the divergent pool with weights
demonstrably moving, that is the evidence that the *single collapsed arena* is the
binding constraint (assembly map §D hypothesis) and the V4 full-loop / loop-
segregation build is pulled forward. We do not pre-commit to V4; we pre-commit to
the falsifier that decides whether V4 is needed.

---

## 7. Disposition summary

| Question | Decision |
|---|---|
| (a) minimal V3 mechanism | one **signed-RPE** δ_t (R − EMA baseline, reusing trained valuation heads) driving a learned per-channel selection-weight vector `w_chan` via a three-factor (Hebbian × RPE) eligibility-trace update with asymmetric D1/D2-analog gain. Distinct from ARC-016 unsigned variance (B5). No new encoder, no phased training, no-op-default. |
| (b) compose vs replace | **COMPOSE** — learning re-weights *inside* the F-bounded MECH-448/449 eligibility frame (safety inherited); the envelope stays as the eligibility/safety frame; the MECH-448 F-deletion lever is re-examined once learning lands (no more floor letters meanwhile). |
| (c) settling coupling | **COUPLED** — a minimal few-round lateral-inhibition settling step whose weights `W_lat` are learned by the **same** δ_t; fixes B1 + B3-blend together; built as the second factor of a 2×2 after `w_chan` alone. |
| (d) falsifier | 2×2 (learned-weight × learned-settling) on the GAP-A divergent pool; PASS = committed-class entropy strict-above envelope-only AND matched-noise, **growing with training**, with **signed-RPE load-bearing** (unsigned-variance ablation fails); preconditions-met no-lift → escalate to V4, never a false ARC-107 weakening. |
| (e) scope bet | **V3 = minimal learned gate** (one weight vector + one `W_lat` + few-round settling); D1/D2 split, habenula drain, full thalamo-cortical loop, TAN window, loop segregation are **V4**, registered as named falsifiable cuts. |

---

## 8. Next steps (governance)

1. **Mint the claims** via `/thought-digestion` intake into `claims.yaml`: a
   learned-channel-gating mechanism (signed RPE → learned per-channel selection
   weight) and the coupled minimal-settling mechanism (learned `W_lat`), both
   `candidate` / `epistemic_category: substrate_conditional`, wired into ARC-107
   `depends_on`, each carrying the ARC-106 divergence-ledger entry + psychiatric-
   failure-mode column. (This note does NOT mint them — design decision only.)
2. **Enter the four silent divergence rows** B4/B5/B7/B8 into the ARC-106 §5 living
   ledger (assembly map §E.1) — B5 (RPE-as-unsigned-variance) is now directly
   load-bearing for this build's signed-δ_t design.
3. **Build** via `/implement-substrate` once the claims are minted: `w_chan` + δ_t
   first (settling OFF), no-op-default, contracts + bit-identical-OFF + activation
   smoke; then the learned-`W_lat` settling step as factor 2.
4. **Falsify** via `/queue-experiment`: the §5 2×2 on the GAP-A-ready substrate
   with the signed-vs-unsigned ablation arm and the matched-noise control.
5. **Hold** the D1/D2 split, habenula drain, full loop, and loop-segregation as the
   §6 V4 bets unless §5 returns preconditions-met no-lift.

---

*Companion to `basal_ganglia_assembly_map_2026-06-22.md` (§A.4 the learning gap;
§C1/§C3 the recurrent-settling repair; §E.3 this note) and
`arc_107_selector_constitution_design_2026-06-20.md` (§3 the constitution; §6b
completeness ledger + V4-axes). Grounded against
`ree-v3/ree_core/predictors/e3_selector.py`. PROMOTES NOTHING.*
