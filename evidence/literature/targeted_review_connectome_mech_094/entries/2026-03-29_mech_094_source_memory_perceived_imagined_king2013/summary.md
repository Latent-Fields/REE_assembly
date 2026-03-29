# King & Miller (2013) -- Lateral Posterior Parietal Activity during Source Memory Judgments of Perceived and Imagined Events

## What the paper did

King and Miller at UC Santa Barbara ran an fMRI study examining whether the brain uses different neural mechanisms to retrieve memories of events that were originally perceived versus originally imagined. Participants encoded objects by either looking at pictures (perception condition) or imagining pictures in response to cue words (imagination condition). At test, they judged whether each cue word had been previously encountered and, if so, whether it had been perceived or imagined. The key contrast was the neural correlates of correctly attributing an old item to perception versus to imagination -- a pure source attribution judgment.

## Key findings relevant to MECH-094

The study found a clear source-based dissociation in successful retrieval activity. Left lateral posterior parietal cortex (PPC) and dorsolateral prefrontal cortex (dlPFC) showed significantly greater activation when attributing events to perception compared to imagination. Moreover, activity in these regions was associated with successful item recognition for perceived events but not for imagined events -- the parietal and prefrontal source signals were specifically tied to the perceived-versus-imagined judgment, not to memory success in general.

This dissociation implies that the brain maintains distinct neural representations for perceived versus imagined memories, and that parietal and prefrontal circuits are specifically recruited to make source attributions -- to retrieve the tag on a memory that marks its origin as external or internal. The lateral PPC result extends prior work on parietal involvement in episodic retrieval, and the dlPFC result is consistent with its role in strategic memory search and source monitoring.

## Translation to MECH-094

MECH-094 proposes that the hypothesis tag is a categorical write gate applied during encoding: simulation signals go through the pre-commit channel, committed-outcome signals through the post-commit channel, and the tag is what routes them. The King & Miller dissociation provides the downstream neural evidence that such tagging occurs: if memories did not carry source tags (imagined vs perceived), the lateral PPC and dlPFC response at retrieval would be identical for both. The fact that they differ -- specifically, that perceived-source attribution recruits a distinct neural response -- implies that the memories carry distinct encoding-time tags that the retrieval system can read out.

In REE terms, the hypothesis tag functions like the encoding-time source label. When E3 writes residue, it must consult this tag: was this content generated from a committed action in the world (perceived-source analogue) or from internal simulation (imagined-source analogue)? The King & Miller result shows that such tags are neurally real and that prefrontal/parietal circuits are involved in reading them out. MECH-094's claim that tag loss is the PTSD mechanism gets indirect support from the logic: if the encoding-time tag is missing or degraded, the retrieval system cannot distinguish committed from simulated content, and the two channels bleed together.

## Limitations and caveats

The main limitation for MECH-094 is that the study examines retrieval-time source attribution, not encoding-time tagging. MECH-094's mechanism operates at write time, not read time. The retrieval dissociation is consistent with encoding-time tags existing, but the two processes are separable: it is possible to have encoding-time tags that leave no distinct retrieval signature, or retrieval-time discrimination without encoding-time tags.

The stimuli are neutral objects (no harm relevance), so we cannot know whether the source dissociation holds for emotionally valenced harm-related content. Harm memories are qualitatively different from neutral object memories, and the parietal/prefrontal circuits implicated might interact differently with the amygdala when valence is involved.

## Confidence reasoning

Good-quality fMRI study from an established memory laboratory. The source-based dissociation is clean and directly relevant to the function MECH-094 implements. Caveats around encoding vs retrieval timing and stimulus neutrality limit the confidence. Overall 0.68.

Based on articles retrieved from PubMed. DOI: https://doi.org/10.1016/j.neuropsychologia.2013.11.006
