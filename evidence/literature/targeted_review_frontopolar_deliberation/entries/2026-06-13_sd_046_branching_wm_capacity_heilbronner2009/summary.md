# Heilbronner & Pollmann 2009 -- Branching capacity is WM-bounded, not structurally capped at two

**Claims:** SD-046, MECH-265
**Direction:** mixed (weakens strict structural-2, supports load-bounded N=2-4)
**Confidence:** 0.55

## What the paper did

Heilbronner & Pollmann took Koechlin & Hyafil's headline claim -- that there is a *structural* limit allowing recursive branching between only two tasks -- and tested it directly. They independently varied working-memory load and the number of recursive branching steps. The result: participants **successfully branched between up to four tasks**, provided WM load was kept low. The two-task ceiling is therefore not a hard architectural property; the limiting factor is **working-memory capacity**. They also found that retaining task-*sets* and task-*contents* contributed *additively* to difficulty, and argued this favours models in which WM and executive function are tightly interactive rather than separate modules.

## Findings relevant to the claims

This paper is the bridge between the L1 (frontopolar branching) and L3 (capacity) layers of the GDL-8 node -- it is what reconciles Koechlin's "limit of two" with Cowan's "about four":

- **SD-046 (slot count N).** The Koechlin entry, read strictly, would cap SD-046 at N = 2. Heilbronner & Pollmann show that is too conservative: the real bound is WM-capacity-governed and reaches ~4 under low load, which lands exactly on the roadmap's "n = 2-4 plausibly" and on Cowan's ~4. So the synthesis across the three L1/L3 papers is: SD-046's slot count is a *capacity-bounded, load-sensitive* number in the 2-4 range, not a free parameter (Cowan), not a hard structural 2 (this paper correcting Koechlin), and possibly better idealised as a shared resource than discrete slots (Bays & Husain).
- **MECH-265 (relative-importance monitoring across the active set).** The number of goals that can be monitored in parallel is itself capacity-bounded and load-sensitive. The monitor's effective fan-out is a function of per-goal representational cost -- which feeds directly into a design caution below.

## Limitations and caveats

The most useful caveat is a design warning for SD-046. Branching capacity *degrades with load*, and task-set + task-content load additively. SD-046 proposes slots that each carry a rich bundle -- per-slot z_goal, drive coupling, age, persistence -- plus (via SD-028) a task-set/template. That is a high per-slot load. Heilbronner & Pollmann predict that an SD-046 holding 4 such heavy slots will **not** realise 4 effective branches; the nominal slot count and the effective branch count come apart as per-slot load rises. The honest consequence: SD-046's N should be read as an *effective* capacity that shrinks as slots get richer, not a fixed structural number.

On evidence weight: this is a single-lab behavioural study (source_quality 0.7), not a Science/Neuron flagship, and it measures human task-branching rather than agent goal-maintenance. Its role is to *adjudicate* the branching-limit question the Koechlin entry raised -- refining that caveat (raising the ceiling, conditioning it on load) rather than independently grounding the SD-046 substrate.

## Confidence reasoning

Smaller study, but a clean, directly-on-point manipulation (independently varying WM load and branching depth is exactly the right design to test "structural vs capacity"). Held to 0.55: source_quality 0.7, mapping_fidelity 0.6 (refines the bound and ties it to load), transfer_risk 0.38. Marked mixed -- it weakens the strict structural-2 reading while supporting the load-bounded 2-4 design. Promotes nothing.
