# Thought Intake: Temporary Coordinated Representational Transformations

- **Date processed:** 2026-09-03
- **Raw thought:** `docs/thoughts/2026-09-03_temporary_coordinated_representational_transformations.md`
- **Session:** thought-routing-20260903 (novelty audit drafted by a Sonnet subagent; reviewed and landed by the session)
- **Companion thoughts, same date:** `2026-09-03_ree_as_predictive_sensorimotor_transformation.md` (processed as the lens page `docs/architecture/lens_predictive_sensorimotor_transformation.md`), `2026-09-03_claim_rotation_dual_view_claim_matrix.md` (registered GOV-ROTATE-1)

## Verbatim core proposal

> Information being present in a representation is not the same as that information being present in the form required by the computation currently being performed.

> REE decision competence depends not only on preservation of relevant information in its predictive representations, but on temporary coordinated transformations that make task-, context- and candidate-relevant relationships readily usable by action-selection machinery. Goal representations are one subset of a broader class of directive structures capable of biasing these transformations.

> Poor behaviour despite strong generic decoding may track failure of decision-time behavioural separability more closely than failure of raw information preservation.

Written against V3-EXQ-978 (FAIL/mixed on INV-088, MECH-457): the directional resource-field head learned its target and did not change foraging competence, while direction was already linearly decodable from `z_world` (R2 0.71 sense-time, 0.86 encoder-path). The thought names three readings 978 leaves open -- A information loss (weakened), B consumer/readout/learning failure, C representational mismatch -- and states that 978 does not separate B from C.

## What's new vs. existing REE docs/claims (novelty table)

| Thread (source section) | Existing coverage (claim IDs, `claims.yaml`) | Verdict |
|---|---|---|
| **"Conditional behavioural accessibility" as the target, not maximal decodability** (§6, §12 first paragraph) | MECH-516 (argmax collapse: graded upstream value destroyed at a categorical consumer boundary before it reaches selection) · MECH-517 (interface-before-representation ordering: "a representation improvement is undetectable through a collapsing interface") · MECH-518 (one tensor, two masters: shared search-geometry budget contention) | **Already-owned.** This is not a refinement — it is the *same claim* under different vocabulary. MECH-517's title is a paraphrase-level match for the source's "information being present in a representation is not the same as that information being present in the form required by the computation currently being performed" (§0). B's proposed "Experiment 1: frozen-latent simple action reader" (§9) is structurally the B-vs-C discriminator the hypothesis brief already names as owed for V3-EXQ-978. No new claim; a 978-adjudicating session should cite MECH-516/517/518, not mint a sibling. |
| **"Directive structures" as a superclass of goals — persistent/transient structures (threats, rules, obligations, uncertainty, social commitments) that bias the representation-to-action transformation, of which goals are one instance** (§3–4) | SD-032a / MECH-261 (`SalienceCoordinator`: a discrete `operating_mode` vector over 4 named modes gates writes/retrieval) · SD-035 (amygdala BLA/CeA: `mode_prior`/`fast_prime` bias mode selection under threat specifically) · SD-057 / MECH-345 / MECH-346 (`IncentiveTokenBank`: object-bound `wanting[k]` biases which z_goal pointer forms) · ARC-133 (individuation by usefulness relative to goals **and** harm **and** interoceptive state — already broader than goals alone, but an individuation criterion, not a transformation-biasing superclass) | **Adjacent-but-distinct, not a child of MECH-516–521.** Checked against the prior read's specific claim that this thread is a refinement of the ARC-133/MECH-516..521 cluster: it is **not** — none of MECH-516/517/518/519/520/521 is about a class of persistent biasing structures; they are about interface collapse (516–518), epistemic-value carriers (519), representational anti-collapse (520), and perceptual slot occupancy (521). The real neighbours are SD-032a/MECH-261/SD-035/SD-057, and those cover the *function* (something other than an explicit goal object biasing retrieval/salience/candidate generation) only as several separately-scoped, already-built special cases — a 4-mode coordinator, a threat-specific amygdala bias, an object-bound token. Nothing registers the **unifying abstraction** ("directive structures" as an open superclass of which goals are one member) B proposes. Does not clear the bar for a new claim on its own merits (see Verdict below) — B's own §11 non-degeneracy self-check ("alternative views merely paraphrase claims without changing experimental reasoning") applies directly: the abstraction generates no falsifiable prediction beyond what SD-032a/MECH-261/SD-035 already test piecemeal. |
| **The core TCRT mechanism itself: `R_(t,a) = T(S_t, D_t, a)`, a temporary, candidate/context-conditioned reorganisation of a rich substrate rather than a single fixed decision representation** (§2, §11, final formulation §13) | MECH-359 (candidate-differentiated affect vector: "for proto-affect to carve behaviour it must carry per-candidate range, not merely per-tick magnitude" — a scalar added equally to all K candidates cannot change an argmax) · ARC-065 GAP-A (`candidate_summary_source="e2_world_forward"`, landed: per-candidate action-conditioned summaries built specifically because candidates were collapsing to a shared, context-blind representation) · MECH-516/517/518 (interface-collapse family, above) · ARC-134 (dynamic perceptual regranularisation — grain, not per-candidate content, but the same "fixed unit is wrong" argument) · MECH-267 (mode-conditioned horizon-depth/noise-scale modulation of CEM search) | **Already-owned, near-exhaustively.** MECH-359's title is a formal restatement of `R_(t,a)` for the affect sub-case (a candidate-conditioned transform of substrate content, `a` explicit in the notation). ARC-065 GAP-A is a *built* instance of exactly the mechanism B's Experiment 3 (§9, "candidate-conditioned representation") asks for. The `S_t, D_t, a -> R_(t,a)` notation itself is not registered anywhere, but notation is not a claim; the substantive assertion (decision-relevant representation is temporarily and conditionally composed, not read off one fixed store) is covered by the claims listed. |
| **"Protected channels" design warning — representational flexibility must not become motivated blindness; harm/nociceptive, viability, hard safety/veto, severe-uncertainty, large-PE, and agency/control-loss signals need privileged, non-suppressible access** (§7) | SD-021 (descending modulation: `z_harm_s` attenuated under commitment, `z_harm_a` explicitly **not** attenuated — an existing precedent for an unsuppressible channel) · MECH-091 (urgency interrupt: `z_harm_a` norm above threshold un-gateably releases commitment) · MECH-138 (dFMC/pre-SMA cancel-window veto pathway) · MECH-036 (other-harm hard-veto threshold) · SD-010/SD-011 (dual nociceptive streams, the substrate the above sit on) | **Adjacent-but-distinct.** REE already has several de-facto protected/unsuppressible channels (SD-021's asymmetric attenuation, MECH-091's un-gateable interrupt, MECH-138's veto pathway) but no claim names "protected channel" as a *general design category* the way B frames it, and none of the existing mechanisms is stated as a instance of a named general principle. This is exactly the shape the task brief anticipated ("may map to existing harm/veto claims") — confirmed. Not a new empirical claim (B itself calls it "a design warning," not a testable proposition, §7) — a documentation cross-reference, not a `claims.yaml` entry. |

## Verdict

**Nothing survives as genuinely new.** Every thread in the section 12
candidate hypothesis is either (a) already registered near-verbatim
(conditional behavioural accessibility ≈ MECH-517), (b) already covered by a
built mechanism under different vocabulary (the TCRT transform itself ≈
MECH-359 + ARC-065 GAP-A), or (c) a design caution rather than a falsifiable
proposition, already exemplified by existing un-suppressible channels
(protected channels, SD-021/MECH-091/MECH-138). The one thread with no direct
existing claim ("directive structures" as a superclass) fails B's own §11
non-degeneracy bar rather than clearing it: it would restate SD-032a +
MECH-261 + SD-035 + SD-057 under one name without adding a falsifiable
prediction none of them already tests.

**No `claims.yaml` entry is drafted.** Per the task's fallback branch, the
proposed action is a one-paragraph *notes* addendum on ARC-133, not a new
claim.

## Key formulations (verbatim, load-bearing)

> A universal `z_world` that is required to make every useful variable immediately readable by every downstream process risks becoming an increasingly near-lossless vector rather than a useful predictive substrate.

> The useful target may not be maximal universal decodability. It may be **conditional behavioural accessibility**.

> representational flexibility must not become motivated blindness.

> a successful simple reader would be a useful result, not a disappointment.

## Affected existing claims

Cross-referenced only; no status, confidence, evidence, or dependency edit on any of them: MECH-516, MECH-517, MECH-518 (interface-collapse family; MECH-517 is a near-verbatim match for the thought's opening distinction), MECH-359 and ARC-065 GAP-A (the candidate-conditioned transform, built), ARC-133 (a notes-only source cross-reference appended this pass, recording that the audit found the thought's content already owned), SD-032a/MECH-261, SD-035, SD-057 (the piecemeal built instances of what the thought calls directive structures), SD-021, MECH-091, MECH-138 (existing unsuppressible channels, the thought's protected-channel warning). INV-088 and MECH-457 (978's own claims) are untouched: their disposition belongs to the 978 autopsy.

## Candidate claims -- REGISTERED this pass

None. Every thread is already registered near-verbatim (conditional behavioural accessibility = MECH-517), already covered by a built mechanism under other vocabulary (R_(t,a) = T(S_t, D_t, a) = MECH-359 + ARC-065 GAP-A), or a design caution rather than a falsifiable proposition (protected channels). The one uncovered thread, directive structures as a superclass of goals, fails the thought's own section 11 non-degeneracy bar: it would restate SD-032a + MECH-261 + SD-035 + SD-057 under one name without a prediction none of them already tests. This is a complete ingestion pass, not an empty one.

## Next steps

1. **The experimental content is routed to the V3-EXQ-978 failure autopsy**, owned at the time of this intake by session autopsy-outstanding-20260903 (artifact path `evidence/planning/failure_autopsy_V3-EXQ-978_2026-09-03.md`, pending). That session was handed a hypothesis brief covering: the B-vs-C question; that the thought's Experiment 1 (frozen-latent simple reader) has already run twice with a PPO reader (948 latent arm 0.5 res/ep, 978 OFF arm 0.267, both 0/3 vs the 1.0 floor) while the supervised oracle-adapter variant has not, and is the cheapest B-vs-C discriminator; that the thought's Experiment 4 (geometry change without information gain) competes with the driver's pre-registered next step (shape b, side-channel the raw field around `z_world`); and that the D0-D5 tracing chain maps onto ARC-130's audit projection (see the lens page). The autopsy, not this intake, decides the routing; /governance ratifies it.
2. **Claim rotation trial.** GOV-ROTATE-1 names the 978 autopsy as its first held-out trial; the outcome (did rotating INV-088 into transformation coordinates produce a smaller or more discriminating next experiment) is to be recorded on GOV-ROTATE-1 once the autopsy lands.
3. **Left unregistered, deliberately:** the `R_(t,a) = T(S_t, D_t, a)` notation (notation is not a claim); the protected-channel design category (a documentation cross-reference at most, when `docs/architecture/selection_relevant_representation.md` or the harm-stream docs are next edited); the directive-structures superclass (fails non-degeneracy; revisit only if a prediction is found that SD-032a/MECH-261/SD-035/SD-057 do not already test).
4. **Literature:** none owed; the thought cites no external sources.
