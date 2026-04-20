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
