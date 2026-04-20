# Task Inbox

Use this as the low-friction capture surface.

- Add new work as `- [ ] task`.
- Mark complete as `- [x] task` (exact same text).
- `run_governance_cycle.py` syncs this file into `manual_carryover_items.v1.json` automatically.
- Completed checkbox lines are removed automatically on sync (use `--no-prune-completed` to keep them).

## Tasks

- Add tasks below this line using checkbox format.

- [ ] Lit-pull (SD-033a, A1 alternative): does biological lateral PFC produce trajectory-specific top-down bias, or a uniform state-dependent gain? Landing choice is per-candidate bias; alternative is uniform scalar. Miller & Cohen 2001, Mansouri 2020, and any trajectory-conditional evaluation literature. See `docs/architecture/sd_033a_lateral_pfc_analog.md` section A1.
- [ ] Lit-pull (SD-033a, A2 alternative): how is the lateral-PFC rule-bias projection shaped by learning, and on what training signal? Landing choice is frozen-random with zeroed last Linear; alternative is trained head via phased protocol. Targets the training-dependent emergence signature (iv) in SD-033 spec. See `docs/architecture/sd_033a_lateral_pfc_analog.md` section A2.
- [ ] Lit-pull (SD-033a, A3 alternative): is rule persistence in biological lateral PFC recurrent-activity-based (spiking persistence, Mansouri 2020) or synaptic-hold-based (short-term plasticity / silent synapses)? Landing choice is gate-modulated EMA; alternatives are GRU recurrence or synaptic-hold. See `docs/architecture/sd_033a_lateral_pfc_analog.md` section A3.
- [ ] Lit-pull (SD-033 governance plan, SD-034 closure operator): OFC/ACC sequence-completion cells (Rich & Shapiro 2009; Schuck 2016); post-completion refractory period on re-entry; task-set disengagement dynamics (Collins & Frank 2014). Targets: what biological signal releases commitment and imposes a temporary No-Go on the just-completed rule_state? On completion, revisit `evidence/planning/sd033_governance_plan.md`.
- [ ] Lit-pull (SD-033 governance plan, MECH-266 asymmetric mode hysteresis): BG direct/indirect pathway asymmetries; tonic DA hysteresis (Cools 2008; Collins & Frank 2014); Schmitt-trigger biology in decision thresholds. Targets: do enter and exit thresholds on an operating mode differ, and by how much per mode? On completion, revisit `evidence/planning/sd033_governance_plan.md`.
- [ ] Lit-pull (SD-033 governance plan, MECH-267 mode-conditioned hippocampal proposals): state-dependent replay content (Pfeiffer & Foster 2013; Olafsdottir 2018); goal-directed replay bias; task-set-conditioned replay. Targets: does hippocampal trajectory proposal depend on current operating mode / task-set in addition to world-state? On completion, revisit `evidence/planning/sd033_governance_plan.md`.
- [ ] Lit-pull (SD-033 governance plan, MECH-268 dACC conflict saturation): habituation of dACC error signals (Bryden 2019); EVC saturation dynamics (Shenhav 2016); repeated-identical-outcome adaptation. Targets: does dACC conflict / prediction-error signal cap or habituate under repeated identical outcomes? On completion, revisit `evidence/planning/sd033_governance_plan.md`.
