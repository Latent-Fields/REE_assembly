# Johnson and Redish 2007 — CA3 transiently encodes paths forward at a decision point

**Source:** Johnson A, Redish AD. *J Neurosci* 27(45):12176-89 (2007). [DOI: 10.1523/JNEUROSCI.3761-07.2007](https://doi.org/10.1523/JNEUROSCI.3761-07.2007). PMID: 17989284. PMC: PMC6673267.

## What the paper did

Johnson and Redish recorded ensembles of CA3 place cells in rats running a T-based decision task and asked a focused question: at the moment of the choice, what does the hippocampus represent? Standard place-cell decoding would say the rat's current location. Their fast-time-scale reconstruction (sub-theta-cycle bins) showed something more interesting. Just before the animal committed to a direction, the decoded position swept forward — first down one arm of the T, then the other, in a coherent sequence. The sweeps were directional (forward, not backward), task-modulated (more frequent on harder trials and after errors), and co-occurred with theta and gamma rhythms rather than the sharp-wave activity characteristic of replay.

## Key findings relevant to MECH-307 Gap 4 and consumer-side conjunction reads

Where Pfeiffer and Foster 2013 show forward-sweep activity at the *moment of goal recall* (start of a goal-directed run), Johnson and Redish show forward-sweep activity at the *moment of choice* between candidate paths. This is architecturally important for MECH-307's consumer side: the four-way conjunction predicate (signed positive surprise + anticipatory wanting + anticipatory liking + z_beta arousal at predicted-imminent location) needs to be read by downstream consumers at the moment they must decide which of several candidates to commit to. The recently-landed MECH295LikingBridge.compute_conjunction_score_bias() (ree-v3 6cd0962, queued for V3-EXQ-540 validation) does exactly this — it iterates over candidates and reads the conjunction at each candidate's predicted-imminent location.

Johnson and Redish supply the biological precedent for that per-candidate forward evaluation. At a real T-maze choice point, the rat's hippocampus genuinely projects forward down each path before committing to a direction. The conjunction-aware bridge in REE is doing the same thing in z_world space: it asks "if I were about to be at this candidate's predicted location, would the conjunction-state fire there?" before letting the candidate weight enter the score-bias computation.

## How the findings translate to REE

The paper supports the architectural shape — read forward at decision time, evaluate per-candidate — without dictating the geometric primitive. REE's candidates live in action-space (typically 4-9 discrete directions in CausalGridWorldV2), and the predicted-imminent location of each candidate is computed by E2's forward dynamics on a one-step horizon. Johnson-Redish style sweeps in REE would manifest not as place-cell sequences but as sequential probes of E2(z_t, a_candidate) for a in candidate_set. Whether these probes happen literally sequentially in time or in parallel within a single forward pass is an implementation detail; the architectural commitment is that the conjunction-state must be evaluated at *each* candidate, not only at the chosen one. This is a property of the consumer (the bridge), not of the producer (MECH-216 schema readout).

A subtle architectural point: Johnson-Redish sweeps are decision-point-specific, while Pfeiffer-Foster sweeps are goal-recall-specific. MECH-307's substrate has to support both reading patterns: write at the predicted-imminent location whenever schema_salience fires, and let consumers decide when (decision time, encoding time, replay time) to read the conjunction. The producer-consumer separation in REE makes this clean — the residue field stores conjunction signatures persistently, and consumers decide when and where to query.

## Limitations and caveats

Johnson and Redish report that forward sweeps are *transient and inconsistent* — they appear at decision points, but not at every decision, and the rate varies across animals and across training stages. This is a calibration concern for V3-EXQ-540's acceptance metric C2 (conjunction-fire-rate >= 0.10 in ARM_2 only). The biological mechanism is patchy; if the REE substrate inherits that patchiness, V3-EXQ-540's per-seed measurement of conjunction fire rate may be noisier than expected. This isn't a falsifying problem — it's a noise-floor problem that needs to be sized in the smoke run, which already showed that 6-episode dry-runs cannot exercise the metric (0 contacts, no goal seeding).

A second caveat: T-maze topology is binary (left/right). REE candidate sets are larger and the predictions are in continuous z_world. The per-candidate-read pattern should transfer (it's a loop over candidates regardless of cardinality), but the relative weight of conjunction-state vs other score-bias contributions may need tuning when the candidate set is wider.

## Confidence reasoning

I assign confidence 0.78. Source quality is high (J Neurosci, foundational, well-replicated). Mapping fidelity is moderate — the per-candidate-read architectural primitive transfers cleanly, but the maze-topology to z_world geometric translation introduces uncertainty about how directly the rat data speaks to REE behaviour. Transfer risk is slightly elevated because the patchiness Johnson and Redish report is a real calibration concern for the V3-EXQ-540 acceptance metric.

Together with Pfeiffer and Foster 2013, this paper covers Gap 4 from two complementary angles: forward-sweep at goal-recall (Pfeiffer-Foster) and forward-sweep at decision-point (Johnson-Redish). Both are needed because MECH-307's consumer side reads the conjunction in both contexts.
