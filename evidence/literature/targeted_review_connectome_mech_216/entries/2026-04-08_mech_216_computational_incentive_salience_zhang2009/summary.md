# Zhang et al. 2009: A Neural Computational Model of Incentive Salience

Zhang, Berridge and colleagues formalise the incentive salience hypothesis into an
explicit computational model that can be tested against neural data. The model's core
is elegant: wanting (W_m) is computed as the product of a learned cached value
(V_hat, from temporal-difference learning) and a current neurobiological state
parameter (kappa). The kappa parameter is the key innovation -- it acts as a gain
control that modulates motivational output without rewriting the learned
associations, allowing the same CS to trigger intense wanting when hungry and
negligible wanting when sated.

For MECH-216, this model provides the closest existing computational framework to
what is being proposed. E1 schema activations that predict resource encounters are
the REE analog of V_hat: learned representations that cache predictive information
about the environment. The VALENCE_WANTING field is the analog of W_m: the
motivational signal that guides approach behaviour. And drive_level (SD-012) is the
analog of kappa: the physiological state that modulates how strongly a predictive
signal translates into wanting. The proposed mechanism -- E1 schema activation above
threshold seeds VALENCE_WANTING at the current z_world position -- is structurally
identical to the Zhang model's W_m(s) = kappa * V_hat(s).

The model was validated against ventral pallidum (VP) neural recordings in rats
performing Pavlovian conditioned approach. VP neurons showed firing patterns
consistent with the model's predictions: CS-triggered activity that scaled with both
the learned association strength and the current motivational state. This neural
validation is encouraging for MECH-216, though the mapping from VP firing to E1
schema readout is imprecise -- E1 is an LSTM-based predictor, not a pallidal nucleus.

The primary caveat is dimensional: Zhang's V_hat is a scalar value per state, while
E1's schema activation is implicit in a high-dimensional LSTM hidden state. MECH-216
requires a readout mechanism that converts E1's high-dimensional schema activation
into a scalar wanting-seeding signal. The Zhang model's clean scalar structure does
not address the challenges of this readout. Additionally, the kappa modulation in
REE (via drive_level) is not yet fully functional -- SD-012 experiments have
consistently failed to produce z_goal values above threshold. If the state modulator
does not work, the learned prediction alone may not be sufficient to generate
meaningful wanting gradients.
