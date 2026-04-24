# Mattar & Daw 2018 -- expected value of backup as a normative replay priority

## What the paper did

Mattar & Daw propose a normative theory of memory access: at each moment, the memory that should be simulated is the one whose access most improves expected future choice quality. The quantity is formalised as EVB (expected value of backup) and decomposes into a product of two terms -- gain, the magnitude of the policy update the backup would induce, and need, the likelihood of visiting the state whose value is being updated. They derive the theory, simulate it on canonical spatial-navigation tasks, and validate the predictions against a broad range of published hippocampal replay datasets.

## Key findings relevant to MECH-285

The theory predicts that replay priority should be proportional to both gain and need, multiplied. Several previously-disparate replay phenomena -- forward replay in anticipation of choice, reverse replay after reward, preferential replay of highly-rewarded locations, replay of remote environments -- fall out of a single optimisation. The paper also shows that the priority shape under EVB is continuous in both terms: neither gain nor need is threshold-gated in the optimal policy.

## Translation to REE

MECH-285 bets that accumulated V_s staleness biases sleep-replay priority. Mattar & Daw give the normative grounding: staleness is structurally the gain term. A region whose stored model disagrees with reality is precisely a region where a backup would produce a large policy update -- gain is high. Under a well-specified EVB the biological system that pays the cost of replay ought to prioritise exactly such regions. MECH-285 is therefore not an architectural bet against the current literature; it is the prediction you would make if you read EVB seriously and asked which biological signal tracks gain.

The proportional-vs-threshold verdict also falls out. EVB is smooth in gain; the optimal priority is continuous. A threshold-gated implementation would leave utility on the table. The default MECH-285 sampler should therefore be softmax or power-weighted over accumulated staleness, not a categorical flag.

The dissociation question is more delicate. In the EVB framework, salience (which feeds the need term via reward-related visitation probability) and staleness (which feeds the gain term) are separable inputs to the same optimisation. That is compatible with two architectural readings: a single sampler taking both as inputs and producing a composite priority, or two dissociable arms (one per term) that converge downstream. Mattar & Daw do not force one reading over the other.

## Limitations and caveats

This is a normative theory. It predicts what an optimal system *should* do, not what any specific brain region *does*. The paper's empirical validation is against summary phenomenology (replay content, not priority mechanisms), so it cannot adjudicate between implementations that are both EVB-consistent. For MECH-285 the theory supports the architecture and the priority-shape default, but does not substitute for direct tests of the staleness-dissociation claim.

## Confidence reasoning

Strong theory paper, widely cited, with broad empirical compatibility. Source quality high. Mapping fidelity high -- the theory directly underwrites MECH-285's staleness-proportional priority architecture. Transfer risk low for the shape verdict, moderate for implementation specifics. Aggregate confidence 0.76.
