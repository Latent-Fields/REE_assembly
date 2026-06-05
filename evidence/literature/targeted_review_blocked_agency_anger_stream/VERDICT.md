# Verdict: boundary-violation / blocked-agency / anger as a candidate REE affect stream

**Date:** 2026-06-05
**Pull:** `targeted_review_blocked_agency_anger_stream` (proto-feelings audit chip `task_64c2e558`)
**Source audit:** `evidence/planning/thought_intake_2026-06-01_protofeelings_audit_register.md` §7
**Status:** evidence artifact + recommendation. **No `claims.yaml` / `affect_primitives.md` edits made** — registration is the user's call.
**Attribution:** Based on articles retrieved from PubMed and the philosophy-of-cognitive-science literature.

---

## The question

Is there a mechanistically distinct affect stream — a signal that an intended/expected action or an agency boundary has been **BLOCKED or COERCED** — warranting registration as a distinct REE affect primitive, separate from harm (SD-011), residue (MECH-056), and generic frustration? Or does it decompose into existing REE pieces?

## (a) Verdict: a distinct stream IS warranted — but it is two streams at two scopes, not one

**Biology before formal definitions** settles the distinctness premise. At the most basic mammalian level the brain treats anger as its own thing:

- **RAGE is a distinct primary-process emotional system** (Davis & Montag 2019), neuroanatomically dissociable from FEAR and PANIC/GRIEF — a separate command system, not a flavour of nociception or fear. Folding it into the harm register would repeat the SD-010→SD-011 *philosophy-right/mechanism-wrong* error (memory `feedback_biology_before_formal_definitions`).
- **Frustrative non-reward (FNR)** (Papini et al. 2024, the Amsel lineage) has an antecedent that is categorically *not* harm: a **negative disparity between obtained and expected reward**, generated with **zero noxious input**. It is aversive *and motivated* (retained reward-seeking via Type-2 dopamine), and its dysregulation *is* clinical irritability/anger.

So the candidate is **not reducible** to harm + residue + frustration + commitment-blocking. But the literature also shows it is **not one monolithic "anger" primitive** — it is **anger as a shared affective readout fed by two different antecedent computations at two scopes**:

| | **Stream A — blocked-agency / control-failure** | **Stream B — coercion / domination / injustice** |
|---|---|---|
| Antecedent | Intended/expected action-outcome repeatedly **blocked** (expectation/agency violation) | An **other agent** constrains the self's freedom (autonomy threat) |
| Anchor | FNR (Papini 2024); comparator model (Carruthers 2012) | Reactance (Steindl 2015); injustice/norm-violation appraisal |
| Needs other-agent model? | **No** — single-agent | **Yes** — requires modelling a coercer |
| Scope | **V3-tractable proxy** | **V4-social** |

Registering one "anger" row would mis-model this: the single-agent frustrative antecedent and the social-coercion antecedent are *different input computations* that happen to converge on the same RAGE-like readout and consumers.

## Differentiation from existing REE substrate (why it is not reducible)

- **vs harm (SD-011 / z_harm_s,un,a):** harm's antecedent is noxious contact (nociceptive pathway). Blocked-agency fires with **no noxious input** (FNR = mere reward/outcome omission). Distinct antecedent, distinct biology (RAGE circuit vs medial nociceptive pathway). They share *some* downstream consumers (both can drive withdrawal) but are distinct at the signal level.
- **vs suffering (SD-019b / z_harm_a, Q-036):** this is the sharpest dissociation, and the literature hands it to us cleanly. Suffering/learned-helplessness is the **capacity-belief-COLLAPSED** pole → *withdraw / mode-switch* (Q-036 escapability gate, already in REE). Blocked-agency/reactance is the **capacity-belief-RETAINED** pole → *energised assert / restore* (Steindl 2015: reactance is explicitly distinguished from helplessness by "maintaining the individual's sense of capacity to alter their situation"). **REE currently encodes only the withdraw pole.** The assert pole is the genuinely missing piece.
- **vs residue (MECH-056):** residue is the trace left *after an action with a moral/value cost was taken*. Blocked-agency is the opposite causal structure: an action was **prevented**. Action-taken-with-cost vs action-prevented → different antecedent, different consumer (residue → repair/avoid-recurrence; blocked-agency → assert/restore-or-decommit).
- **vs commitment-blocking (MECH-090 beta-gate):** MECH-090 is the **licit, self-imposed** gating of E3→action during a committed sequence (output blocked *by design*). Blocked-agency is an **externally-imposed, against-the-grain** block while the goal is live. Self-hold (licit) vs external-block (the new signal) — distinct.

## (b) If warranted: smallest computational form, consumers, and scope

### Smallest computational form (Stream A, V3 proxy) — `z_block` / blocked-agency
A scalar/low-dim signal layered on substrate REE **already has**:
1. **Detector (exists):** the agency comparator (SD-029) on the *action-outcome / goal channel* — intended effect predicted by the forward model (E2), realised effect diverges (Carruthers 2012: comparator mismatch = loss of agency).
2. **Antecedent (exists):** expected-vs-realised outcome disparity, where expectation is z_goal/wanting (MECH-112) — i.e. FNR's expected-minus-obtained, generalised from reward-omission to action-effect-omission.
3. **New work — the readout + two gates:**
   - integrate comparator mismatch over a window → rising `z_block` when intended action repeatedly fails;
   - **attribution gate:** mismatch attributed to *external constraint*, not own motor error;
   - **capacity gate:** fires as *assert* only while goal/capacity is **retained**; as capacity-belief falls, hand off to the suffering/withdraw pathway (z_harm_a).

This is decisively **not harm** (no noxious input) and **not suffering** (opposite controllability pole).

### Consumers it drives
- **Assert / escalate-effort / try-different** — the adaptive analogue of reactive aggression (Bertsch 2020) and reactance direct-restoration (Steindl 2015); raise drive/vigor (MECH-320), search an alternative action that restores the intended outcome. **This is the new behavioural pole REE lacks.**
- **Decommit (MECH-342)** — if assertion fails across the window, release the blocked commitment rather than escalate unboundedly; gated by the prefrontal-analogue (ARC-016 commitment-threshold). Bertsch 2020 grounds this gate (prefrontal inhibition of reactive aggression).
- **Withdraw** — *not* this stream's native consumer; it belongs to the suffering pole. Blocked-agency hands off to withdrawal only when capacity-belief collapses.
- **(V4-social) Boundary-assertion / repair / RAGE-toward-source** — Stream B only; needs an other-agent coercer (reactance, injustice appraisal). Defer.

### Scope
- **Stream A (blocked-agency / control-failure): V3-tractable now.** Single-agent proxy = "intended action repeatedly blocked by environment/constraint." Low marginal cost — reuses SD-029 + z_goal; the build is the readout + attribution + capacity gate + the assert consumer.
- **Stream B (coercion / domination / injustice): V4-social, defer.** Requires modelling an other agent as the source of restriction. Anti-domination / anti-exploitation are inherently other-agent. Cross-link to the V4 ethics cluster (`thought_intake_2026-05-31_musings_on_v4.md`).

## Recommendation (gated — user decides registration)

1. **Register Stream A** as a new `affect_primitives.md` Extension-Register row — **`blocked-agency / control-failure`** — explicitly differentiated from harm (no noxious input), suffering (opposite controllability pole), residue (action-prevented vs action-taken-with-cost), and commitment-hold (external-block vs licit self-hold). Note its detector = SD-029, expectation = MECH-112, consumers = assert (new) + decommit (MECH-342) gated by ARC-016, with hand-off to z_harm_a at capacity-collapse.
2. **Defer Stream B** (coercion/domination/injustice) to V4-social; stub it in the Extension Register as V4-deferred and cross-link the V4 ethics cluster.
3. **Do not** register a single emotion-named "anger" primitive — anger is the shared readout; the streams that feed it differ in antecedent and scope.
4. **Smallest testable V3 proxy** (for a future `/queue-experiment`, not built here): an environment that repeatedly blocks an intended, predicted-to-succeed action while harm and goal-value are held constant; measure whether a comparator-mismatch readout rises, whether it drives *assert/persist* (effort escalation / alternative-action search) distinct from the withdraw signature, and whether it dissociates from z_harm_a under matched controllability manipulation.

## Evidence summary (5 entries)

| Entry | Source | Role | Dir | Conf |
|---|---|---|---|---|
| `..._rage_distinct_primary_process_davis2019` | Davis & Montag 2019, Front Neurosci, 10.3389/fnins.2018.01025 | Distinctness premise (RAGE ≠ FEAR/PANIC/harm) | supports | 0.72 |
| `..._frustrative_nonreward_expectation_violation_papini2024` | Papini et al. 2024, J Neurosci, 10.1523/JNEUROSCI.1021-24.2024 | V3 antecedent (expected−obtained, no noxious input) | supports | 0.80 |
| `..._reactive_aggression_consumer_prefrontal_bertsch2020` | Bertsch et al. 2020, Curr Psychiatry Rep, 10.1007/s11920-020-01208-6 | Consumer + prefrontal/decommit gate; reactive≠proactive | supports | 0.74 |
| `..._psychological_reactance_autonomy_threat_steindl2015` | Steindl et al. 2015, Z Psychol, 10.1027/2151-2604/a000222 | V4-social boundary + assert-vs-helplessness split | supports | 0.62 |
| `..._comparator_sense_of_agency_carruthers2012` | Carruthers 2012, Conscious Cogn, 10.1016/j.concog.2010.08.005 | V3 detector = SD-029 comparator | supports | 0.66 |

**Convergence:** all five point the same way — anger is a distinct primary-process readout (Davis & Montag) fed in the single-agent case by a frustrative-non-reward / agency-violation computation (Papini, Carruthers) that REE can already detect (SD-029) and expect (MECH-112), with consumers (assert + prefrontal-gated decommit; Bertsch) that include a behavioural pole REE currently lacks, and a coercion/autonomy-threat extension (Steindl) that is genuinely V4-social. Note the convergence already visible in the biology: Panksepp's RAGE fires when SEEKING is **blocked**, which is exactly FNR — the two literatures describe one antecedent.
