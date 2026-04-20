# Uddin 2015 -- Salience processing and insular cortex function

## What the paper did

A *Nature Reviews Neuroscience* review synthesising the state of knowledge on the insular cortex's role in salience processing. Uddin integrates fMRI, anatomical connectivity, and clinical neuropsychiatric evidence to argue that the anterior insula is the central integrative hub of the salience network. It has distinct subdivisions with functionally different roles -- ventral anterior insula for affective/interoceptive salience, dorsal anterior insula for cognitive-control salience -- but its overall function is to detect behaviourally relevant stimuli across modalities and coordinate neural resources accordingly.

Atypical engagement of specific insular subdivisions within the SN is identified as a feature of many neuropsychiatric disorders including autism spectrum disorder, anxiety disorders, addiction, and frontotemporal dementia. The clinical framing is consistent with Menon 2011's triple-network model but zooms in specifically on the insular contribution to SN function.

## Why this matters for SD-032a

SD-032a's SalienceCoordinator has an explicit multimodal-aggregation interface. The `update_signal(name, value)` API accepts `aic_salience` (from SD-032c interoceptive detection), `pcc_stability` (from SD-032d attention-balance), and `pacc_autonomic` (from SD-032e slow write-back), and the coordinator aggregates these with the dACC bundle components into per-mode affinity logits that are softmax-normalised into the operating_mode vector. This multimodal-aggregation pattern is exactly the insular role Uddin describes.

The biological license is cleaner here than for Sridharan alone. Sridharan 2008 establishes that the SN is causally upstream of mode switching; Uddin 2015 establishes *what the SN actually integrates*: multimodal saliency signals spanning interoception, cognitive control, and attentional partition. The latter licenses SD-032a's architectural choice to read from all five cingulate subdivisions rather than treating any one as the primary coordinator input.

## Limitations and caveats

The review does not specify a computational form for the aggregation. Uddin articulates that the insula integrates; she does not say whether integration is linear, multiplicative, gated, or softmax-normalised. ree-v3's softmax-over-affinity-logits is a design choice that survives translation but is not biologically constrained by this paper. Anyone wanting to test whether the softmax rule is specifically the right aggregation form would need to look to different literature -- likely computational modelling work on attentional selection (Daw, Niv, etc.) that is not within this pull's scope.

The clinical framing is secondary to REE. Atypical insular engagement in autism or anxiety maps onto human subjective experience and behavioural phenotypes; it does not translate directly onto substrate-level failure signatures for ree-v3. The substrate signatures listed in SD-032a ("ablation forcing operating_mode to fixed external_task abolishes mode switching without affecting within-mode computations") are operationally defined in ree-v3 terms; Uddin does not give us a procedure to convert "aberrant insular engagement in anxiety" into a predicted ree-v3 failure.

There is also a subtle caveat about subdivisions. Uddin identifies ventral anterior insula (affective) and dorsal anterior insula (cognitive control) as functionally distinct. ree-v3's SD-032c is a single AIC-analogue; the ventral/dorsal distinction is not yet architecturally instantiated. This is a recognised simplification for the minimum-viable substrate; if V3-EXQ-446 or downstream experiments show that single-AIC is insufficient, the parent SD-032 doc flags the subdivision-split as a future refinement.

## Confidence reasoning

0.80 is the right calibration. Source quality 0.85 (NRN review from a leading SN theorist; widely cited). Mapping fidelity 0.75 (the integrative-hub role transfers cleanly; the specific aggregation rule is unconstrained). Transfer risk 0.30 (architectural mapping from human insular anatomy to ree-v3 substrate is plausible; clinical-dysfunction mapping is weaker).

Together with Sridharan 2008 (causal directionality), Goulden 2014 (methodological replication), and Menon 2011 (triple-network organising frame), Uddin 2015 fills the remaining biological gap for SD-032a by specifying *what the coordinator integrates* -- multimodal saliency signals spanning interoception, cognitive control, and attentional partition. The four papers together license SD-032a's architecture at the level of subsistence grounding: there is a biological substrate, it has a coordinator role, the role is causally upstream of mode switching, and the coordinator aggregates across modalities. The specific computational form remains an ree-v3 design decision that V3-EXQ-446 will evaluate on its own terms.
