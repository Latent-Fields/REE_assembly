# Precision-Provenance Substrate Spec (SD-PP-1..4) -- interface contract

**Status:** SPECIFICATION (2026-09-22, session `compassionate-pike-fe9174`). Build authorised by
user decision 2026-09-22 ("Build full producers first, then experiment"; recommendation ledger
entry 520). This document is the contract every implementer builds against; the code must
satisfy it, not replace it.
**Motivating intake:** `evidence/planning/thought_intake_2026-09-22_behavioral_precision_provenance_and_sleep_plasticity_gain.md`
**Claims:** MECH-572 (lead), MECH-573, MECH-574, MECH-016, ARC-055, MECH-043, MECH-368/431,
MECH-284/285, MECH-269, ARC-137, INV-063.
**Experiment this unblocks:** V3-EXQ-1073 (reserved), preregistration
`evidence/planning/precision_provenance_consolidation_gain_design_20260922.md`.

---

## 0. Why these four pieces, and what the live audit found

The MECH-572 phenotype is produced on ONE path:

```
SleepLoopManager._run_cycle  (ree_core/sleep/phase_manager.py ~735-790)
  -> CrossModuleConsolidator.consolidate(module_losses={"e1","e2","e2_world"})
       fresh torch.optim.Adam per module per call, n_steps=8, lr=1e-3
  -> agent.compute_e2_world_loss(batch_size)   (ree_core/agent.py ~12515)
       idx = torch.randperm(n_pairs)[:K]
       triple (world[i], action[i+1], world[i+1]) from
       agent._world_experience_buffer / agent._action_experience_buffer
       -> e2.world_forward_contrastive_loss(min_batch_classes=1)
```

Verified 2026-09-22 against ree-v3 `a38a834`:

| Question (intake section 1.4) | Live answer |
|---|---|
| Is per-episode historical prediction precision preserved? | **No.** The buffers hold only `(z_world, action_one_hot)`. |
| Is evidence/outcome precision preserved? | **No.** No sensory/evidence precision producer exists anywhere in `ree_core` (grep empty). |
| Is episode-linked prediction error preserved? | **No.** Under the V3-EXQ-1063 configuration nothing even computes the world-forward prediction for the executed action at test time; the three paths that do (MECH-353 blocked-agency, SD-063 deficit, escape linker) are default-off. |
| Is behavioural success/failure preserved? | **No.** |
| Does any of this reach replay selection or consolidation gain? | **No.** Selection is `torch.randperm`; gain is a fresh Adam at a fixed lr. |
| Is the hippocampal AnchorSet / StalenessAccumulator / SleepReplaySampler path (the one the intake inspected) on this path? | **No.** MECH-285 Phase B is a no-op consumer feeding the SWS aggregation cluster; the weight-consolidation pass draws from the raw experience buffers. The "episodic trace" for this experiment is therefore the world experience buffer, and provenance rides alongside it. |
| Live precision producers? | E3 `running_variance` EMA (fed by the PROPOSER's predicted z_world, not `e2.world_forward`; global, state-blind). SD-063 `E2WorldUncertaintyHead` (default-off; per-(z,a) TOTAL predictive variance -- absorbs observation noise, so it cannot by itself separate model precision from evidence precision). |
| Default-on behavioural consumer of `e2.world_forward`? | **None.** `e3_selector.py`'s only reference is a docstring. Organism-level validation needs a default-off lever (MECH-314a curiosity source, MECH-353) -- registered as a necessity, not built here. |

So the three quantities the intake keeps distinct each need a producer, and the packet needs a
carrier and a consumer. Nothing here changes replay CONTENT or ORDER, the objective, E1/E2, or
the environment.

---

## 1. Package layout

```
ree-v3/ree_core/precision/__init__.py                       (exists)
ree-v3/ree_core/precision/observation_reliability.py         SD-PP-1
ree-v3/ree_core/precision/world_forward_epistemic_precision.py SD-PP-2
ree-v3/ree_core/hippocampal/replay_provenance.py             SD-PP-3
ree-v3/ree_core/sleep/provenance_gain.py                     SD-PP-4 (rule + diagnostics)
ree-v3/ree_core/sleep/cross_module_consolidation.py          SD-PP-4 (step-scale hook, trace)
ree-v3/ree_core/predictors/e2_fast.py                        SD-PP-4 (reduction= kwarg)
ree-v3/ree_core/agent.py, ree_core/utils/config.py, ree_core/sleep/phase_manager.py  (integration, single writer)
ree-v3/tests/contracts/test_sdpp1_observation_reliability.py
ree-v3/tests/contracts/test_sdpp2_world_forward_epistemic_precision.py
ree-v3/tests/contracts/test_sdpp3_replay_provenance.py
ree-v3/tests/contracts/test_sdpp4_provenance_gain.py
ree-v3/tests/contracts/test_sdpp4_consolidation_gain_consumer.py   (integration; written after wiring)
ree-v3/docs/substrate/SD-PP-1-observation-reliability.md ... SD-PP-4-...md
```

Rules binding every module (implement-substrate Key rules): every new config param defaults to
no-op; OFF is bit-identical by STRUCTURAL ABSENCE (no object built, no call made, no RNG drawn);
pure float/tensor arithmetic, **no RNG draws anywhere** in these modules; all `print()` ASCII-only;
no change to any existing default; no checkpoint / serialisation format change (packets are
runtime-only buffers, never saved); MECH-094: the recorder runs on WAKING ticks only and is
skipped when `hypothesis_tag` is set; the gain consumer is the same explicit weight-update
exception the consolidator already is (it writes no residue/anchor/memory content).

---

## 2. SD-PP-1 `precision.observation_reliability` -- evidence precision producer

**What it is.** An organism-side estimate of how reliable the exteroceptive channel is right now,
expressed both in observation units and, via the encoder gain, in z_world units. It is the
"evidence precision" of the three-way distinction. It uses ONLY the observation stream
(`obs_world` handed to `agent.sense()`) and the encoder's own `z_world` -- no env internals, no
labels, no future frames.

**Statistic.** For consecutive exteroceptive frames `o_{t-1}, o_t` (world_state, 250 elements in
CausalGridWorldV2):

```
d_t        = |o_t - o_{t-1}|                    elementwise
sigma_hat_t = median_e(d_t) / MAD_SCALE          MAD_SCALE = 0.954  (median|N(0,2s^2)| = 0.954 s)
sigma_sq_ema <- (1-a_o) sigma_sq_ema + a_o sigma_hat_t^2     a_o = obs_ema_alpha (0.2); first frame initialises
sigma_obs_sq = max(sigma_sq_ema, sigma_floor^2)              sigma_floor = 0.005 (instrument floor)
precision_obs = 1 / sigma_obs_sq
```
Measured 2026-09-22 (probe, seed 42, 300 random-action steps): clean median|d| = 0.0000 (p90 0.0000);
sigma 0.03 -> 0.0333; sigma 0.12 -> 0.1271. The statistic is cleanly separated because in a
mostly-static exteroceptive field fewer than half the elements change per frame (clean
frac_changed = 0.127), so the median is 0 without noise and ~sigma with it.

**Encoder gain (to express evidence precision in z units).**
```
kappa_t = mean_d((z_t - z_{t-1})^2) / mean_e((o_t - o_{t-1})^2)   skipped when denominator < 1e-12
kappa   <- (1-a_k) kappa + a_k kappa_t        a_k = kappa_ema_alpha (0.05); initialised to the first kappa_t; ready=False until then (kappa=1.0 while not ready)
evidence_variance_z  = kappa * sigma_obs_sq
evidence_precision_z = 1 / (evidence_variance_z + eps)      eps = 1e-9
```
LIMITATION (record in the docstring and the substrate record): kappa is measured on real motion
and applied to noise; an encoder that suppresses high-frequency jitter has a smaller gain on noise
than on motion, so `evidence_variance_z` OVER-estimates z-noise and the downstream gain is
conservative under noise. Named proxy; the per-state upgrade is a learned sensory-precision head.

**API (exact).**
```python
@dataclass
class ObservationReliabilityConfig:
    use_observation_reliability: bool = False
    obs_ema_alpha: float = 0.2
    kappa_ema_alpha: float = 0.05
    sigma_floor: float = 0.005
    mad_scale: float = 0.954
    eps: float = 1e-9

class ObservationReliabilityEstimator:
    def __init__(self, config: ObservationReliabilityConfig) -> None
    def observe_obs(self, obs_world: torch.Tensor) -> None      # [N] or [1,N]; BEFORE encode; stores detached clone as previous frame
    def observe_latent(self, z_world: torch.Tensor) -> None     # [D] or [1,D]; AFTER encode, same tick; updates kappa from the (dz, do) pair of this tick
    def on_episode_reset(self) -> None                          # drop previous frame + previous latent (no cross-episode difference)
    # read-only properties (floats): sigma_obs, sigma_obs_sq, precision_obs, kappa, evidence_variance_z, evidence_precision_z, n_frames, ready (bool)
    def snapshot(self) -> Dict[str, float]     # {"sigma_obs","sigma_obs_sq","precision_obs","kappa","evidence_variance_z","evidence_precision_z","ready"}
    def get_metrics(self) -> Dict[str, float]  # snapshot() keys prefixed "obs_reliability_" + "obs_reliability_n_frames"
```
Both observe_* calls must be no-ops on the first frame of a life/episode (nothing to difference
against). `observe_latent` before any `observe_obs` in the same tick is a no-op. No tensor with
`requires_grad` is ever stored.

**Tests (`test_sdpp1_observation_reliability.py`, pytest, seeded, fast):** (1) config default
False; (2) sigma recovery: additive N(0, s^2) on a mostly-static 250-vector at s in {0.03, 0.12}
recovers sigma_obs within 25% after 50 frames, and a clean stream sits AT sigma_floor; (3) kappa
positive and finite after >= 2 latent frames; (4) NO RNG consumption: `torch.get_rng_state()`
byte-identical before/after 100 observe calls; (5) on_episode_reset makes the next observe a
no-op; (6) evidence_precision_z falls monotonically as s rises (s in {0, 0.03, 0.12}).

---

## 3. SD-PP-2 `precision.world_forward_epistemic_precision` -- model precision producer

**What it is.** The precision of the organism's OWN world-forward model (`e2.world_forward`) about
the next z_world, separated into total predictive variance, an aleatoric part attributed to the
evidence channel (from SD-PP-1), and the EPISTEMIC remainder. Read BEFORE an outcome is observed
it is "historical model precision" (provenance); read at sleep entry it is "current model
precision". The two are the same producer at two times -- that is what makes the distinction
operational rather than nominal.

**Sources.**
- `"ema"`: global calibrated -- `v_tot` = EMA of per-dim mean squared PE of `e2.world_forward`
  over waking transitions (`pe_ema_alpha` 0.05). State-blind (as SD-063 says of the EMA class);
  always available.
- `"sd063"`: per-state -- `v_tot(z,a) = head.predictive_variance(z, a)` from the SD-063
  `E2WorldUncertaintyHead` when `head.training_ready`, else falls back to `"ema"`. The packet
  records which source served the read.
- Default config `source = "sd063_or_ema"` (per-state when ready, EMA otherwise).

**Noise split.**
```
v_noise <- EMA over ticks of (noise_gain * evidence_variance_z)     same alpha as v_tot; evidence_variance_z from SD-PP-1 (0.0 when SD-PP-1 absent)
v_epi(z,a) = max(v_tot(z,a) - v_noise, v_floor)        v_floor 1e-6 (per-dim z units)
pi_epi     = 1 / v_epi
```
`noise_gain = 2.0`, pre-registered from first principles: observation noise enters the PE through
BOTH the input (z_t) and the target (z_{t+1}), and for a near-identity head (which MECH-573 measures
the converged head to be, skill ~0) the PE noise variance is ~2x the per-frame z-noise variance.
Named assumption; recorded in the substrate record.

**API (exact).**
```python
@dataclass
class PrecisionRead:
    pi_epi: float; v_tot: float; v_ale: float; v_epi: float; source: str   # source in {"ema","sd063"}

@dataclass
class WorldForwardEpistemicPrecisionConfig:
    use_world_forward_epistemic_precision: bool = False
    source: str = "sd063_or_ema"      # "ema" | "sd063" | "sd063_or_ema"
    pe_ema_alpha: float = 0.05
    v_floor: float = 1e-6
    noise_gain: float = 2.0
    v_init: float = 1e-2              # v_tot before any observation (fresh-base residual scale, V3-EXQ-1063)

class WorldForwardEpistemicPrecision:
    def __init__(self, config, world_dim: int) -> None
    @torch.no_grad()
    def prediction_at_test(self, e2, z_prev: Tensor, a_onehot: Tensor) -> Tensor   # [1,D] detached, = e2.world_forward(z_prev[:1], a_onehot[:1])
    @torch.no_grad()
    def precision_at(self, z_prev: Tensor, a_onehot: Tensor, head=None) -> PrecisionRead   # uses CURRENT estimator state; never the outcome
    def observe_outcome(self, pred: Tensor, z_now: Tensor, evidence_variance_z: float) -> float
        # pe = mean_d((pred - z_now)^2) (float); updates v_tot EMA and v_noise EMA; returns pe
    def current_read(self) -> PrecisionRead    # global read (EMA source) -- used at sleep entry for pi_cur
    # properties: v_tot, v_noise, v_epi, pi_cur, n_obs
    def snapshot(self) -> Dict[str, float]; def get_metrics(self) -> Dict[str, float]  # prefix "wf_precision_"
```
Ordering contract: the caller calls `precision_at` BEFORE `observe_outcome` for a transition;
`observe_outcome` must not read anything but its arguments. `precision_at` with `head` given and
`head.training_ready` False falls back to the EMA read and reports `source="ema"`.

**Tests (`test_sdpp2_world_forward_epistemic_precision.py`):** (1) default False; (2) EMA maths
exact against a hand-rolled EMA on synthetic pe; (3) `v_epi` floored at `v_floor`; (4) noise split:
with evidence_variance_z = v_tot/(2*noise_gain) v_epi halves; (5) no-future-info: a
`precision_at` read taken before `observe_outcome(pe=huge)` is identical to one taken with no
observation at all, and the read AFTER differs; (6) sd063 fallback: a stub head with
`training_ready=False` yields `source="ema"`, with True yields `source="sd063"` and
`v_tot == head.predictive_variance(...)`; (7) no RNG consumption; (8) `prediction_at_test` equals
`e2.world_forward` output bitwise and carries no grad.

---

## 4. SD-PP-3 `hippocampal.replay_provenance_packet` -- carrier

**What it is.** One packet per replay-buffer entry, recorded at the moment `_e1_tick` appends the
outcome state to `agent._world_experience_buffer`, bound by INDEX to that buffer so the
consolidator can look it up for the triple it drew. Packet `p[j]` describes the transition
`(world[j-1], action[j], world[j])`; the training triple at replay index `i` is
`(world[i], action[i+1], world[i+1])`, so its packet is `p[i+1]`. Pin this alignment in a test
against the actual tensors, exactly as `test_e2_world_forward_sleep_trainer.py::test_w6` pins the
+1 offset.

**Fields (schema_version 1).**
```python
PROVENANCE_SCHEMA_VERSION = 1

@dataclass
class ReplayProvenancePacket:
    schema_version: int
    buffer_index: int            # index of the OUTCOME state in _world_experience_buffer at record time
    tick: int                    # agent step counter at record time
    provenance: str              # "real" (waking, observed). Never "reconstructed"/"simulated" here.
    pred_at_test: torch.Tensor   # [1,D] detached point prediction e2.world_forward(z_prev, a)
    pe: float                    # mean_d (pred - z_now)^2
    pi_hist: float               # epistemic precision BEFORE the outcome (PrecisionRead.pi_epi)
    v_tot_hist: float; v_ale_hist: float; precision_source: str
    evidence_variance_z: float; evidence_precision_z: float; sigma_obs: float; kappa: float; evidence_ready: bool
    surprise: float              # pi_hist * max(pe - noise_gain * evidence_variance_z, 0)   (standardised epistemic surprise at test; ~1 when calibrated)
    has_prev: bool               # False when no previous state existed (episode start) -- packet is a placeholder with pe=nan
```
**Recorder API (exact).**
```python
class ReplayProvenanceRecorder:
    def __init__(self, epistemic: WorldForwardEpistemicPrecision, reliability: Optional[ObservationReliabilityEstimator], noise_gain: float, max_len: int = 1000) -> None
    @torch.no_grad()
    def record(self, e2, z_prev: Optional[Tensor], a_onehot: Tensor, z_now: Tensor, buffer_index: int, tick: int, head=None) -> ReplayProvenancePacket
        # ORDER ENFORCED INSIDE: pred = epistemic.prediction_at_test(...); read = epistemic.precision_at(...) ; ev = reliability.snapshot() if reliability else zeros
        #                        pe = epistemic.observe_outcome(pred, z_now, ev["evidence_variance_z"])   <- only AFTER the read
        # appends to self.packets; trims to max_len (del packets[:-max_len]) -- in lockstep with the agent buffers
    packets: List[ReplayProvenancePacket]
    def get(self, index: int) -> Optional[ReplayProvenancePacket]   # by CURRENT list position (the buffers and packets are trimmed together, so positions stay aligned)
    def trim_to(self, n_keep: int) -> None
    def stats(self) -> Dict[str, float]       # n, mean/min/max of pe, pi_hist, evidence_precision_z, surprise; fraction has_prev
    def get_metrics(self) -> Dict[str, float] # prefix "replay_provenance_"
```
Memory: 1000 packets x 16 floats is trivial. No serialisation.

**Tests (`test_sdpp3_replay_provenance.py`):** (1) alignment pin (build a 6-state buffer with
distinct z, record packets in the same loop, assert `p[i+1].pred_at_test ==
e2.world_forward(world[i], action[i+1])` for every i); (2) trim lockstep (record 1005, assert
len == 1000 and `get(i)` still matches buffer position i); (3) no-future-info: `p.pi_hist` equals
the epistemic read taken immediately before `record()`; (4) surprise formula; (5) episode-start
placeholder (`z_prev=None` -> has_prev False, pe nan, no EMA update); (6) schema_version stamped.

---

## 5. SD-PP-4 `sleep.provenance_conditioned_consolidation_gain` -- consumer

**Where gain acts.** The consolidator builds a FRESH Adam per call, whose bias-corrected step is
~`lr * sign(g)` regardless of `|g|` (MECH-572). A per-transition loss weight alone is therefore
normalised away in magnitude; it changes only the DIRECTION of the step. So the gain acts in two
places, both pre-registered: (a) per-row loss weights `sum_i g_i l_i / sum_i g_i` set the
direction; (b) the module's lr for that step is scaled by `mean_i g_i`, which is what moves the
DISPLACEMENT. The liveness probe (preregistration section 9) verifies displacement is monotone in
the scale before any run. Replay content, order and count are untouched: the same `randperm`
draw, the same K rows, the same 8 steps.

**Rule family (pre-registered; constants provisional until the preregistration's freeze record).**
For row `i` with packet `p_i`, current global epistemic precision `pi_cur` (SD-PP-2 `current_read()`
at sleep entry), config `c`:
```
K_i = p_i.evidence_precision_z / (p_i.evidence_precision_z + pi_cur)                # Kalman-form write authority in (0,1): reliable evidence vs current belief
m_i = sqrt( max(p_i.pe - c.noise_gain * p_i.evidence_variance_z, 0) / c.v_ref )     # epistemic innovation MAGNITUDE (the information Adam discards); v_ref = 1e-2
r_i = min( c.reopen_max, 1 + c.surprise_beta * max(0, ln(p_i.surprise)) )           # reopen factor: HISTORICAL precision enters ONLY here, interpreting the surprise
gain_i = clip( c.gain_max * K_i * m_i * r_i , c.gain_min , c.gain_max )              # bounded
```
Properties the rule must satisfy (each is a test): reliable evidence drives stronger updating than
unreliable at matched pe (K); high current precision needs stronger evidence for a large change
(K); a reliably-falsified high-confidence prediction is NOT protected -- its gain is >= the
gain of the same contradiction under low historical precision (r >= 1, never < 1); low-confidence
prediction + noisy evidence has low write authority (K small, m small); bounded in
[gain_min, gain_max]. Historical precision never appears as a multiplier < 1.

**Modes.**
| mode | gains | purpose |
|---|---|---|
| `provenance` | rule above | ARM C |
| `provenance_nohist` | rule with `r_i = 1` | ARM C-nohist (is historical precision load-bearing? intake F1) |
| `residual_only` | `g_i = global_scale * l_i / mean_j(l_j)` (l = per-row CURRENT loss, detached; no clip) | ARM D-residual (current residual only, budget = global_scale) |
| `global` | `g_i = global_scale` | ARM D-global (matched budget, no information) |
A packet missing for a row (`get()` None or `has_prev` False) -> `g_i = 1.0` and `n_missing` counted.

**API (exact).**
```python
GAIN_MODES = ("provenance", "provenance_nohist", "residual_only", "global")

@dataclass
class ProvenanceGainConfig:
    use_provenance_conditioned_consolidation_gain: bool = False
    mode: str = "provenance"
    gain_min: float = 0.02
    gain_max: float = 2.0
    surprise_beta: float = 0.5
    reopen_max: float = 3.0
    v_ref: float = 1e-2
    noise_gain: float = 2.0
    global_scale: float = 1.0
    def __post_init__(self): validate mode in GAIN_MODES, 0 < gain_min <= gain_max, v_ref > 0, reopen_max >= 1

def compute_provenance_gains(packets: List[Optional[ReplayProvenancePacket]], pi_cur: float, per_row_loss: Optional[torch.Tensor], config: ProvenanceGainConfig) -> Tuple[torch.Tensor, Dict[str, float]]
    # returns gains [K] (float32, no grad) and a flat diagnostics dict:
    #   gain_mean, gain_min, gain_max, gain_sd, n_missing, k_mean, m_mean, r_mean, r_max, surprise_max, pi_cur, mode (as float index into GAIN_MODES)

def weighted_row_loss(per_row_loss: torch.Tensor, gains: torch.Tensor) -> torch.Tensor   # sum(g*l)/sum(g); grad flows through l only
```
**Consolidator hook (`cross_module_consolidation.py`).** `consolidate(..., module_step_scale: Optional[Dict[str, Callable[[], float]]] = None, record_trace: bool = False)`. In `_step_module`, AFTER the loss closure has run (so the closure has set the scale) and BEFORE `opt.step()`: if `name in module_step_scale`, set every `param_group["lr"] = rate * float(scale_fn())`. When `record_trace`, append `{"module", "step", "loss", "step_scale", "grad_norm"}` (grad_norm = global L2 over that module's params, computed after `backward()`) to `self._last_step_trace` (a list, cleared at each `consolidate()` call; exposed as `last_step_trace` property). Readouts added to the returned dict ONLY when a scale was supplied for that module: `step_scale_mean_<name>`, `step_scale_min_<name>`, `step_scale_max_<name>`. With both kwargs absent the method is byte-identical to today (test: the OFF path adds no keys and produces identical parameters at a pinned seed).

**`e2_fast.world_forward_contrastive_loss(..., reduction: str = "mean")`.** `"none"` returns the
per-row CE `[K]`; the degenerate early-returns keep returning a 0-d zero. `"mean"` bitwise equals
today's output (test).

**Tests (`test_sdpp4_provenance_gain.py`, rule only, no agent):** (1) bounds; (2) monotone in
evidence precision at matched pe; (3) the anti-self-sealing property (contradiction with reliable
evidence under high pi_hist gets gain >= same contradiction under low pi_hist); (4) noisy
contradiction (large pe, evidence_variance_z*noise_gain >= pe) gets gain_min; (5) `residual_only`
mean == global_scale exactly; `global` constant; (6) `provenance_nohist` <= `provenance` rowwise;
(7) missing packet -> 1.0 and counted; (8) config validation; (9) `weighted_row_loss` gradient
flows only through l; (10) consolidator: `module_step_scale` scales displacement -- at a pinned
seed with a fixed loss, max|delta| is strictly increasing over scales (0.1, 0.5, 1.0, 2.0), and
absent scale is byte-identical to today's `consolidate()`; (11) `reduction="none"` rows mean
equals `reduction="mean"` bitwise.

---

## 6. Integration (single writer: the session, after the modules land)

**Config (REEConfig, all no-op defaults, each popped in `from_dims`):**
```
use_observation_reliability=False, observation_reliability_sigma_floor=0.005, observation_reliability_obs_ema_alpha=0.2, observation_reliability_kappa_ema_alpha=0.05
use_world_forward_epistemic_precision=False, world_forward_precision_source="sd063_or_ema", world_forward_precision_pe_ema_alpha=0.05, world_forward_precision_v_floor=1e-6, world_forward_precision_noise_gain=2.0
use_replay_precision_provenance=False                      (requires the two producers ON; agent raises ValueError otherwise)
use_provenance_conditioned_consolidation_gain=False, provenance_gain_mode="provenance", provenance_gain_min=0.02, provenance_gain_max=2.0, provenance_gain_surprise_beta=0.5, provenance_gain_reopen_max=3.0, provenance_gain_v_ref=1e-2, provenance_gain_global_scale=1.0   (requires use_replay_precision_provenance AND use_sleep_world_forward_consolidation)
cross_module_consolidation_record_trace=False
```
**Data flow.**
```
env obs_world --sense()--> ObservationReliabilityEstimator.observe_obs   (before encode)
   latent_stack.encode -> z_world --> .observe_latent                     (after encode, same tick)
_e1_tick: buffers.append(z_world, action_one_hot)
   -> ReplayProvenanceRecorder.record(e2, world[-2], action[-1], world[-1], idx, tick, head=e2_world_uncertainty)
        pred_at_test / precision_at (BEFORE) / observe_outcome (AFTER) -> packet[idx]
sleep: compute_e2_world_loss draws idx -> packets[i+1] -> compute_provenance_gains(pi_cur=epistemic.current_read().pi_epi)
   -> weighted_row_loss ; agent._last_consolidation_gain = {"mean": ..., **diag}
   -> consolidate(module_step_scale={"e2_world": lambda: agent._last_consolidation_gain["mean"]}, record_trace=cfg)
   -> per-step lr = lr * mean gain ; trace -> sleep-cycle metrics (prefixed cross_module_consolidation_)
```
**Backward compat statement.** With every flag at default no object is constructed, no call is
made, no RNG is drawn, `consolidate()` receives neither kwarg, and `world_forward_contrastive_loss`
is called with its default reduction. Existing experiments run unchanged. Pinned by the integration
test (world-head parameters bitwise identical after a forced sleep cycle with all flags OFF vs the
pre-build call shape).

**Phased training.** SD-PP-2's optional SD-063 source inherits SD-063's own P0/P1/P2 discipline
(warmup, detached targets, frozen in eval). SD-PP-1/3/4 train nothing.

**MECH-094.** Recorder runs on waking ticks only (`hypothesis_tag` -> skip). Consumer is a
weight-update pass inside the existing MECH-094 explicit exception; it writes no content.

**Falsifier-runnability (3h).** EVENT: a waking behavioural test of a world-forward prediction
followed by a sleep consolidation pass -- emitted by `_e1_tick` + `SleepLoopManager` (present).
DV: across-sleep frozen-battery MSE on retention / correction batteries, plus per-step
displacement -- emitted by the V3-EXQ-1063 instrument (present) and the SD-PP-4 trace (this
build). INSTRUMENT able to move: MECH-572 measured the displacement pinned at the Adam bound in
6/6 cells; the step-scale hook is what lets it move, and SD-PP-4 test (10) is the liveness pin.
Evidence precision able to move: probe above (0.000 vs 0.127). Model precision able to move:
converged vs fresh residual differ ~1000x (V3-EXQ-1063). Runnable, pending the preregistration's
own non-degeneracy gates.

---

## 7. Substrate necessities this exercise surfaced but does NOT build (registered separately)

See `evidence/planning/precision_provenance_substrate_necessities_20260922.md` and the matching
`substrate_queue.json` rows. In one line each: (a) no default-on behavioural consumer of
`e2.world_forward` (organism-level validation path absent; shared with INV-063 leg B); (b) the
hippocampal selection path (MECH-285) is disconnected from weight consolidation (raw-buffer
`randperm`); (c) evidence-precision manipulation is a driver-level hack (`_apply_obs_noise`), not
an env lever; (d) a one-shot rule shift needs a driver poke of `_action_map`; (e) the world-forward
head sits near copy-the-input because z_world barely moves per step (identity MSE ~1e-5,
MECH-573) -- a representation-range limit on ANY consolidation experiment on this head; (f)
per-state model precision that separates epistemic from aleatoric natively (SD-063 gives total
spread only; SD-PP-2's split is by subtraction); (g) a learned sensory-precision estimator (SD-PP-1
is a frame-difference proxy); (h) optimiser-state persistence across cycles as MECH-572's own
alternative lever (not built here so the baseline reproduces the phenotype).
