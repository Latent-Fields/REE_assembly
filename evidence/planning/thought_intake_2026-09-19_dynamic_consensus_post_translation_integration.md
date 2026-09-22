# Thought intake -- dynamic consensus as post-translation integration

- **Date processed:** 2026-09-22
- **Raw thought:** `docs/thoughts/2026-09-19_dynamic_consensus_post_translation_integration.md` (269 lines, dated 2026-09-19)
- **Session:** `compassionate-pike-fe9174-consensus` (umbrella worktree, Mac)
- **Skill:** `/thought-ingestion`
- **Registered this pass:** MECH-578, MECH-579
- **Architecture home:** `docs/architecture/dynamic_consensus_integration.md`

---

## 1. The proposal, tightly stated

The mutual-legibility programme asks how two systems with different internal representations
exchange usable information. This thought argues that framing *stops one step too early* and
asks what happens **after translation succeeds**.

> Integration can therefore be understood not as one representation being converted into
> another, nor as both systems being collapsed into a common representation, but as
> **iterative constraint satisfaction between partially mutually legible systems**.

The proposed decomposition:

```text
cross-system integration = mutual legibility + selective reciprocal coupling + agreement-dependent dynamics
```

and the process, where the terminal pair is mutually supportable rather than identical:

```text
A(t) <-> B(t) -> A(t+1),B(t+1) -> ... -> A*,B*
```

The load-bearing measurable is **agreement-dependent timescale**: `tau_agree > tau_disagree`.

> A bridge that merely transfers information need not produce this separation. A coupled
> system that actively reconciles representations should.

The thought's own epistemic status section is unusually disciplined and is honoured verbatim
in the registrations: the Javadzadeh et al. result is a *supported external observation* about
V1-LM in one task; "reciprocal selective coupling can implement consensus without
representational identity" is a *reasonable architectural inference*; the REE version is a
*hypothesis*; and whether it improves REE behaviour is an *open empirical question*. It asks to
"enter the Assembly as a thought and assay-generating hypothesis, not as an accepted REE
mechanism" -- which is exactly `status: candidate` + `substrate_conditional` + DO-NOT-BUILD.

---

## 2. What is new vs. existing REE claims

**This is an unusually strong extraction case.** Six of the thought's eight threads are already
owned, several of them almost verbatim. Saying so precisely *is* the value of this pass.

| thread in the thought | existing REE coverage | verdict |
|---|---|---|
| **Agreement-dependent timescale separation** `tau_agree > tau_disagree` under reciprocal coupling, collapsing under ablation or correspondence scramble | **Nothing.** MECH-548 is one bridge applied repeatedly (drift/gain signatures); MECH-539 is transition-geometry compatibility of a *mapping*; INV-108 forbids *training* agreement but says nothing about dynamics that *arise*. None predicts a timescale signature of reciprocal reconciliation. | **genuinely new -> registered as MECH-578** |
| **Development: dense exploratory coupling -> learned selective reciprocal coupling; pruning carves a consensus topology, not a dictionary** | MECH-362 (subtractive sparsification) is *within-system* and says nothing about what a pruned interface *means*. MECH-550 supplies the retention criterion. MECH-549 supplies the matched-final-capacity test. | **genuinely new -> registered as MECH-579** (falsifier 2 stated in MECH-549's own terms) |
| **"An interface can be legible yet dynamically pathological"** / the object is the stability of the coupled recurrent interface, not either direction's accuracy | **MECH-548**, nearly verbatim: "an interface can be statically useful yet recurrently unstable -- a bridge with one-step utility > 0 can fail repeated closed-loop application", with off-manifold compounding, semantic double-counting, and the cumulative-vs-clean-base diagnostic already registered | **already owned -> cross-ref only.** MECH-578 is distinguished from it by *directionality* |
| **No privileged global representation**; subsystems may legitimately differ in encoding, dimensionality and timescale | **ARC-139** in full, including the non-redundant prediction that rising local competence with flat-or-falling global similarity is the maturation signature, and the explicit warning not to use rising similarity as a maturation marker | **already owned -> cross-ref only** |
| **The system must know when NOT to settle**; false consensus; dominance masquerading as consensus; preserve legitimate disagreement; self-vs-other must not be forced into agreement | **INV-108** in five explicit parts -- no agreement objective may be optimised into the evaluators; convergence is diagnostic, an event over diversity; dependency provenance and disagreement history preserved; a competent dissenter retains a protected path to attention a confident majority cannot close; the target is competent non-redundant routes, not maximum diversity *or* maximum agreement. Plus **MECH-558** (vote count is not evidence count; correlated coalitions) | **already owned -> cross-ref only.** This is the single biggest extraction find in the pass |
| **Translation embedded in a recurrent process; static mappings fail in behaving systems** | MECH-539 (`good static + bad dynamic` routes to transition-geometry work) + MECH-547/MECH-548 (receiver-conditioned translation and recurrent stability) | **already owned -> cross-ref only** |
| **Consensus must be gated** -- which dimensions may couple, how strongly, when | **ARC-145**'s jurisdiction property (property 3: the exchange occurs under a routing state granting causal privilege *at that moment*) + **MECH-561** (phase as an addressing coordinate) | **already owned -> cross-ref only.** Folded into MECH-578's falsifier 2 as a precondition rather than re-registered |
| **Organism-level validation** -- a beautiful internal consensus metric is not sufficient evidence | GOV-JURIS-1 / GOV-ECOL-1 / GOV-HOTHER-1 / GOV-DELETE-1 / Q-108, from `2026-09-16_local_mechanism_success_vs_organism_level_intelligence.md` | **already owned -> cross-ref only** |

### A registry defect found in passing

INV-105's ladder has **seven** rungs. Four claims each describe themselves as adding "an
**eighth**" -- MECH-548, MECH-555, GOV-CONTRACT-3, INV-110 -- and MECH-556 describes a
"**ninth**". The ordinals are already mutually inconsistent.

MECH-578 proposes a further rung (**RECIPROCALLY RECONCILED**) and deliberately carries **no
ordinal**, saying so in its own title so that a future reader does not mistake the omission for
an oversight. **The collision is owed to `/governance`** -- it is a registry-hygiene finding,
not something this ingestion pass should adjudicate.

---

## 3. Key formulations (verbatim)

> Translation may not be the endpoint of cross-system integration.

> The goal is therefore not representational equality. It is dynamical compatibility.

> The relevant test is therefore not simply: Can A decode B? but: When A and B are reciprocally
> coupled, what states become stable? An interface can be legible yet dynamically pathological.

> A useful abstraction is a learned cross-system correspondence under a context-sensitive gate:
> the correspondence describes what can couple; the gate determines what is allowed to couple now.

> Pruning would carve not only a dictionary, but a **consensus topology**.

> Two systems can be individually competent and semantically related while still possessing
> coupling that drives them toward the wrong attractor.

> Persistent disagreement may be exactly the signal that forces remapping, counterfactual
> search, uncertainty escalation or sleep-mediated reorganisation.

> The endpoint is not a universal language. It is a system in which specialised components can
> understand enough of one another, at the right time and along the right dimensions, to
> discover when their local views can coexist -- and to retain the capacity to refuse consensus
> when they cannot.

---

## 4. Affected existing claims

**Cross-referenced only. Nothing amended; no status, confidence, category or evidence record
was touched.**

- MECH-578 -> ARC-139, INV-105, MECH-539, MECH-548, ARC-145, MECH-561, INV-108, MECH-558
- MECH-579 -> MECH-578, MECH-362, MECH-549, MECH-550, ARC-139

**Distinguished-from, with the distinction load-bearing:**

- **MECH-548 vs MECH-578** -- one bridge applied repeatedly vs two systems coupled
  reciprocally. A system can be recurrently stable (MECH-548 satisfied) with no
  agreement-dependent separation (MECH-578 false), and vice versa.
- **MECH-539 vs MECH-578** -- a property of the *mapping* vs a property of the *closed loop*.
- **MECH-362 vs MECH-579** -- a sparse weight matrix vs a map of where agreement is worth having.
- **INV-108 guards MECH-578, and does not duplicate it.** MECH-578 is a *diagnostic prediction
  about dynamics that arise*, never a licence to optimise `tau_agree`. A system trained to
  maximise the separation violates INV-108 part (i) outright. MECH-578's falsifier 3
  (false-consensus challenge) is the operational guard, and this is stated in MECH-578's own
  `notes` so the pairing cannot be lost.

---

## 5. Candidate claims -- REGISTERED this pass

Both `status: candidate`, `epistemic_category: substrate_conditional`,
`implementation_phase: v4`, `version_relevance: v4_v5`, `registered_utc: 2026-09-22`.

| id | subject | one-line |
|---|---|---|
| **MECH-578** | `representation.agreement_dependent_timescale_separation` | Reciprocally coupled subsystems show `tau_agree > tau_disagree`; three pre-registered ablations (direction, correspondence scramble at matched coupling strength, false-consensus injection) each must abolish it |
| **MECH-579** | `development.consensus_topology_carved_by_pruning` | That separation is developmentally acquired and behaviourally selective; present-at-initialisation or uniform-across-all-modes refutes it |

Per the skill, **no `what_would_answer` was drafted** -- that is `/thought-digestion`'s job.
The assays in the raw thought are recorded as falsifier *content* inside the claim titles, not
as digestion drafts.

**Assays deliberately NOT turned into separate claims:** the thought lists seven. Assays 1-3 and
5 are folded into MECH-578's falsifiers, assay 6 into MECH-579's primary prediction. Assay 4
(conflict injection -- does the organism converge correctly, stay uncertain, seek evidence, or
collapse into the higher-gain subsystem?) is **already covered by INV-108 part (iv) and
MECH-558**, and registering it would have duplicated them. Assay 7 (sleep remapping) is a
`/queue-experiment` design against MECH-540's existing sleep-recalibration corollary in
MECH-548, not a new claim -- recorded here so it is not lost.

---

## 6. Next steps

1. **OWED TO `/governance`: the INV-105 rung-ordinal collision** (section 2). Four claims claim
   an eighth rung, one a ninth. Needs adjudication, and MECH-578 is waiting on it before it can
   carry an ordinal.
2. **OWED TO `/governance`: version routing.** Both claims are `v4`/`v4_v5` per the ingestion
   default. Note that the nearest siblings are split -- MECH-548, MECH-539 and MECH-561 are all
   `implementation_phase: v3`, while ARC-139, INV-108 and MECH-558 are `v4`. MECH-578's assay 1
   (matched-magnitude perturbation, measure two decay constants) may be cheaper on existing V3
   substrate than the default assumes. **Not decided here.**
3. **Literature deliberately unverified as REE evidence.** Javadzadeh et al. 2026 was read only
   as the thought reports it. Per `feedback_lit_exp_decoupled` it strengthens no REE claim's
   confidence, and the thought's own caution -- that generalisation beyond V1-LM in one simple
   task is not established -- is carried into both claims' notes. A `/lit-pull` against MECH-578
   is a reasonable follow-on, not a prerequisite.
4. **Deliberately left unregistered:** the six "already owned" threads. A future session that
   believes one is uncovered should say which cited claim fails to cover it rather than
   re-register.

---

## 7. Digestion drafts

**None produced this pass.** Ingestion stops at `candidate`. MECH-578 and MECH-579 are live
input to the next `/thought-digestion` run.
