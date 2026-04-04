# Frank & O'Reilly 2006 -- Cabergoline and Haloperidol Dissect D2 Go/NoGo: MECH-106 Mapping

**Source:** Frank, M.J., & O'Reilly, R.C. (2006). A mechanistic account of striatal dopamine function in human cognition: psychopharmacological studies with cabergoline and haloperidol. *Behavioral Neuroscience*, 120(3), 497-517. DOI: [10.1037/0735-7044.120.3.497](https://doi.org/10.1037/0735-7044.120.3.497)

---

## What the Paper Does

Where Frank 2004 uses Parkinson's patients as an indirect probe of dopaminergic asymmetry, Frank and O'Reilly 2006 tests it directly in healthy adults using selective pharmacological agents. The logic is tighter: cabergoline is a D2 agonist that at low doses acts presynaptically to suppress DA release (reducing phasic DA bursts and thus D1 activation); haloperidol at low doses blocks D2 autoreceptors, removing the presynaptic brake and augmenting phasic DA release. If the model is right, cabergoline should impair Go learning (by reducing the D1 potentiation signal from positive outcomes) and haloperidol should enhance it. Both effects are predicted by the Frank 2005 computational model.

The study finds exactly this pattern across a probabilistic reinforcement learning task, and the effects extend to working memory and attentional tasks -- pointing to a domain-general role for D2-modulated BG gating in cognitive threshold setting, not just motor response selection.

## Key Findings

The double dissociation between cabergoline and haloperidol on Go learning replicates and extends Frank 2004 using a more selective pharmacological approach. The key advance over the Parkinson's study is mechanistic specificity: the agents have known D2 selectivity, the doses are chosen to target presynaptic autoreceptors, and the healthy population removes confounds of disease-related neural compensation.

For MECH-106, the most relevant finding is that D2 tone modulation selectively affects positive-outcome learning (Go signal) rather than negative-outcome learning. Cabergoline reduces DA release, impairing the phasic burst that would normally potentiate D1 -- this is the cellular event MECH-106 maps to commit-threshold lowering. Haloperidol augments the burst, enhancing the Go signal. The reverse pattern -- D2 manipulation affecting negative-outcome learning -- is less pronounced, which is consistent with the model because negative-outcome learning operates via D2 MSN relief from DA dip, a postsynaptic mechanism not directly targeted by presynaptic autoreceptor agents. This selectivity is actually consistent with MECH-106: it shows that the positive-outcome threshold-lowering mechanism and the negative-outcome threshold-raising mechanism are pharmacologically dissociable.

The extension to working memory tasks is worth noting: the same D2-mediated gating that modulates reinforcement learning also controls what gets updated into working memory representations held in PFC via BG gating. This is directly relevant to REE's commitment architecture, where E3 commitment states involve sustained maintenance of latent representations as well as action gating.

## REE Mapping to MECH-106

The paper provides causal human evidence for the pharmacological selectivity of the asymmetric D1/D2 mechanism MECH-106 invokes. In REE terms, the cabergoline effect (reduced phasic DA -> impaired Go learning) corresponds to what would happen if positive outcomes failed to adequately lower the commit threshold -- the agent would persist at a higher threshold than warranted by the favourable outcome history. The haloperidol effect (augmented phasic DA -> enhanced Go learning) corresponds to positive outcomes being more effective at lowering the threshold than normal.

The extension to working memory gating is relevant because MECH-106's commitment hysteresis is not just about the action selection threshold but also about the persistence of the committed state in E3's representational substrate. If BG D2-modulated gating controls both action selection thresholds and WM maintenance gates, the same asymmetric modulation that affects commit entry may also affect how long the committed latent state is sustained. This is a potentially productive extension for future REE experiments.

## Limitations and Confidence Reasoning

The main limitation is pharmacological: cabergoline and haloperidol at these doses primarily affect presynaptic D2 autoreceptors, which modulate DA release. The MECH-106 mechanism as Frank 2005 specifies involves postsynaptic D2 MSN activity in the indirect pathway, which is one step downstream from what these agents directly target. Increased phasic DA (from haloperidol blocking the autoreceptor brake) should increase D1 MSN activation, consistent with Go learning enhancement -- but the pathway from presynaptic to postsynaptic effects involves additional synaptic steps not directly probed.

Additionally, the task is discrete-choice reinforcement learning, not commitment sequence management. The mapping to commit/de-commit threshold dynamics is inferential, consistent with the model but not directly tested. Confidence: 0.76, reflecting strong pharmacological support for the mechanism with a moderate mapping gap.

*Based on article retrieved from PubMed (PMID: 16768602, DOI: [10.1037/0735-7044.120.3.497](https://doi.org/10.1037/0735-7044.120.3.497)).*
