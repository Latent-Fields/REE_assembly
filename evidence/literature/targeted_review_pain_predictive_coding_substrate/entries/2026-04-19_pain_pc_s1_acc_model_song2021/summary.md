# Song et al. 2021 -- Predictive coding model with coupled S1 and ACC populations

**Citation.** Song Y, Yao M, Kemprecos H, Byrne A, Xiao Z, Zhang Q, Singh A, Wang J, Chen ZS. Predictive coding models for pain perception. Journal of Computational Neuroscience 2021; 49(2): 107-127. [DOI](https://doi.org/10.1007/s10827-021-00780-x). (According to PubMed.)

**What they did.** Recorded LFPs simultaneously from rat S1 and ACC during evoked and spontaneous pain. Built both a phenomenological predictive-coding model (macroscopic dynamics) and a biophysical neural-mass model (mesoscopic) with S1 and ACC as two coupled populations. Fit to data from naive animals and from chronic-pain animals.

**Key finding.** The two-population model, with explicit coupling terms between S1 and ACC, reproduces key features of pain LFP dynamics -- including the expectation-dependence of perceived intensity, placebo/nocebo analogues, and the chronic-pain distortions. A single-population model does not capture this structure. The computational architecture that fits the biology is two distinct forward-prediction populations with coupling, not one unified predictor.

**What this does for the REE question.** This is the closest direct analog to the REE architecture in the literature. Their "S1 population" is the sensory-discriminative forward predictor (our E2_harm_s), their "ACC population" is the affective forward predictor (our E2_harm_a), and their coupling term is the computational analog of whether the two share substrate. Their model has distinct populations with coupling -- which is the "shared trunk with stream-specific heads" architecture, not fully independent parallel modules.

**Where Song is limited.** Rat LFP, not human. The "populations" in the neural-mass model are fit to local dynamics rather than explicitly embedded in a latent-space forward model like E2. The coupling is phenomenological. Transfer to REE's compact agent requires abstraction.

**Confidence reasoning.** High mapping fidelity because the architectural shape they validate is exactly the shape we are considering. Source quality good (peer-reviewed computational neuroscience venue with empirical grounding). Transfer risk moderate (rodent -> REE). Net confidence 0.80. This is my second-strongest entry behind Horing 2022.
