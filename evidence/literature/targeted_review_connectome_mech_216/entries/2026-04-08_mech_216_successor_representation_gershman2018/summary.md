# Gershman 2018: The Successor Representation: Its Computational Logic and Neural Substrates

Gershman's review presents the successor representation (SR) as a bridge between
model-free and model-based reinforcement learning, arguing that the hippocampus
implements something like the SR: a predictive map that encodes each state in terms
of expected future state occupancy. The computational elegance is that value
computation becomes a simple inner product -- the SR provides the "where will I go"
and the reward function provides the "what is there worth," and the value follows
immediately.

The relevance to MECH-216 is indirect but substantial. If E1's LSTM-based world
model learns something analogous to the SR -- encoding z_world states in terms of
their predictive relationships to future states -- then states that reliably precede
resource encounters will have elevated predictive activity. This is the
representational foundation for MECH-216's proposal: E1 schema activations at
resource-predictive positions are high precisely because those positions have strong
successor links to reward-proximal states. The SR framework explains *why* E1 would
develop differential schema activation at approach positions versus random positions.

The paper also notes that place fields cluster around rewarded locations -- a natural
consequence of the SR's dependence on visitation frequency. In REE terms, this
predicts that E1's latent representations will be denser (more differentiated) near
resources, which in turn means that the schema activation signal available for
MECH-216's wanting-seeding mechanism will be stronger in resource-relevant regions
of z_world space. The gradient is built into the representation itself.

The limitation is that Gershman's SR is about representation, not motivation. The SR
explains why certain states carry stronger predictive signals, but it does not
address the step from "strong prediction" to "wanting." That step -- the
transformation of a predictive signal into a motivational one -- is precisely what
MECH-216 proposes, drawing on the incentive salience framework (Berridge 2012,
Zhang et al. 2009). The SR provides the representational substrate; incentive
salience provides the motivational mechanism; MECH-216 proposes that in REE, E1's
schema activation (SR-like) feeds into the serotonin module's wanting-seeding
pathway (incentive-salience-like) to produce approach behaviour before direct
resource contact.
