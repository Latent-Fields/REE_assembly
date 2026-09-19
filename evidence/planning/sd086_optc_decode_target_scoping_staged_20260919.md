# SD-086 option C -- decode-target scoping, and why the design is STOPPED for one decision

**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml (or any other registry). No experiment was queued.**

- Session: `metaworker-science-20260919-sd086-optc-target-scoping` (headless)
- Chip: `chip-proposal-exp-1222-paced` | Claim: **SD-086** | Proposal: **EXP-1194** (`EVB-1666`)
- Recorded: 2026-09-19T04:55:00Z
- User decision being executed: 2026-09-19T04:48:56Z -- "QUEUE SD-086's OPTION C NOW, with the
  rank-2 limit stated", using the decode target and noise-band rule "exactly as that staged doc
  and SD-086's `what_would_answer` give them; anything they leave open that changes what is
  measured is a `kind:decision` chip -- stop there."

---

## 1. Why this stops

Both load-bearing design parameters are **unspecified** in every source the decision named.

**(a) The decode TARGET.** SD-086 has **no `what_would_answer` field at all** (checked in
`claims.yaml`; it has `falsifier`, `scope_note`, `depends_on`, `live_status`). Its
`non_degeneracy_precondition`, quoted verbatim in the 2026-09-18 staged doc section 1, gives a
**disjunction**:

> a linear decode of **behavioural mode or harm-event status** from `z_harm_a` must clear a floor

Option C (section 6) re-specifies the **criterion** -- vector vs norm -- and is silent on which
horn of that disjunction to decode. The same document's own sections 5/6 establish that the
choice is consequential: option A (hazard-context median split) is "a monotone function of the
encoder's own dominant input channel -- near-tautological", and option B (harm-event status) has
"no balanced threshold ... without inventing one, and the threshold sets the decode's difficulty
and hence the verdict". "Behavioural mode" is never operationalised anywhere.

**(b) The noise-band rule.** "beyond the cross-seed noise band" has no operational definition in
the staged doc. SD-086's `falsifier` does give a shape -- "a margin scaled on the SD of the delta
plus an absolute floor" -- but with no constants, and it describes the **downstream trained-head
two-arm experiment**, not this decode.

**(c) The proposal does not supply them either.** `EXP-1194` / `EVB-1666` carries only procedural
`acceptance_checks` ("at least 2 additional runs with distinct seeds", pack validates, result
links to claims) and `require_pre_registered_thresholds: false`.

So this session stopped at the design step and raised one decision chip, rather than choosing.

## 2. What was measured anyway, so the decision is not blind

Read-only scoping probe, 3 seeds, on an encoder trained by the landed P0h stage at its adopted
default (floor 0.1, `harm_surprise_pe_enabled`; `p0h_readiness_met` asserted TRUE on every seed).
Held-out linear readout (50/50 time split, ridge 1e-6) from the 16-d vector and from the scalar
norm, to each candidate target:

| candidate target | vector R^2 | norm R^2 | margin | per-seed margin |
|---|---|---|---|---|
| `hazard_at_agent` (the norm's known partner) | 0.9995 | 0.6471 | **+0.352** | +0.248 / +0.334 / +0.474 |
| `resource_at_agent` (the 2nd structural d.o.f.) | 0.9982 | 0.1992 | **+0.799** | +1.304 / +0.352 / +0.741 |
| per-tick `harm_exposure` | 0.3334 | -0.0085 | **+0.342** | +0.186 / +0.402 / +0.438 |
| JOINT `hazard` + `resource` (2 d.o.f. at once) | 0.9988 | 0.4231 | **+0.576** | +0.776 / +0.343 / +0.608 |

### Three readings that matter for the decision

**(i) Every candidate clears, so the target choice does not flip the DIRECTION -- only the
margin (2.3x spread, +0.34 to +0.80).** That is reassuring about robustness and awkward about
gate value: option C as written looks close to a foregone conclusion *now that the encoder
trains*. It is still a real measurement, but a reader should not treat it as a stiff test.

**(ii) Training the encoder MOVED information out of the magnitude.** The 2026-09-18 staged doc
measured `corr(||z_harm_a||, hazard_EMA) = 0.9885` (R^2 ~ 0.977) on the FROZEN random projection.
On the P0h-trained encoder the norm's hazard R^2 is **0.647**, while the vector's is 0.9995. So
P0h training redistributed information from pure magnitude into direction -- which is SD-086's
thesis, arriving from an unexpected direction. It also means the "the norm already decodes the
same signal" objection that sank the original precondition is **specific to the untrained
encoder** and does not carry over.

**(iii) `resource_at_agent` is where the norm is principledly blind (0.199 vs 0.998).** That is
exactly what rank 2 predicts: one scalar cannot carry two independent scalars. It is the sharpest
contrast -- and for that reason also the most cherry-pickable.

## 3. The rank-2 limit, to be stated wherever this lands

`harm_obs_a` is structurally rank 2: `causal_grid_world.py` ~3033-3038 writes `hazard_at_agent`
into dims `[:25]` and `resource_at_agent` into dims `[25:]`. So `z_harm_a` carries at most **2
independent d.o.f. about the world**, whatever it is trained on, and a weak vector-over-norm
margin must not be over-read. Full treatment:
`evidence/planning/harm_obs_a_rank2_scoping_staged_20260918.md`.

Note the interaction with (iii): the rank-2 fact is simultaneously the *ceiling* on this result
and the *reason* a vector-over-norm margin should exist at all. A design that decodes only ONE
scalar is measuring inside the norm's reach; the JOINT target is the one that uses the ceiling
rather than fighting it.

## 4. Honest limit of section 2

This probe is a scratch, read-only characterisation -- 3 seeds, a plain ridge fit, no manifest, no
pre-registered thresholds. It is **not** a substitute for the queued run, and it does not create
evidence for SD-086. But it does mean the queued run's likely outcome is already visible, which is
information the user should have *before* paying for it.

## 5. Reproduction

`ree-v3/scratch_optc/probe_targets.py` under this session's worktree (throwaway, not committed);
the table above is its output. Encoder trained via `experiments/_lib/zharm_a_p0_warmup.py`
(ree-v3 `78397036`) at its adopted defaults.
