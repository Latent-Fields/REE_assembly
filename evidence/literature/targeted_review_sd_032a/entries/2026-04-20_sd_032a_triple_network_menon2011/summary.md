# Menon 2011 -- Triple network model of psychopathology

## What the paper did

This is an authoritative theoretical review in *Trends in Cognitive Sciences* that formalises the "triple network model" of large-scale brain dysfunction. Menon synthesises fMRI, resting-state, and clinical neuroimaging literature circa 2011 to argue that three networks -- the salience network (SN; AIC + dACC), the central executive network (CEN; lateral prefrontal and posterior parietal), and the default mode network (DMN; medial prefrontal and posterior cingulate) -- form a tightly-coupled architecture whose aberrant access, engagement, or disengagement is a transdiagnostic signature across schizophrenia, depression, anxiety, dementia, and autism.

The central theoretical move is that the SN is not merely another network but the *coordinator* of the other two. Saliency mapping -- identifying which internal or external events warrant attentional reconfiguration -- is the SN's job, and triggering the CEN/DMN switches is how that coordination expresses itself. Psychopathologies in this frame are not primarily deficits of CEN or DMN alone; they are deficits in the salience-driven coordination between them.

## Why this matters for SD-032a

SD-032a's architectural choice -- a dedicated coordinator substrate whose job is to aggregate signals and emit `operating_mode` + `mode_switch_trigger` -- is a direct adoption of the triple-network frame. Menon 2011 is the canonical statement of why that architectural separation matters: the coordinator is load-bearing; collapsing it into either CEN or DMN loses the transdiagnostic invariant that psychopathologies share. If SD-032a's ablation experiment (V3-EXQ-446) shows that removing the coordinator produces no coherent failure mode, the Menon frame is not being instantiated.

The mapping is clean on the architectural axis: SalienceCoordinator reads from subdivisions (dACC bundle, drive_level, offline-state) and emits a mode vector that gates downstream writes via MECH-261. What the mapping cannot do is transfer the *psychopathological* content directly. Menon's frame is organised around human clinical disorders -- schizophrenia, depression, anxiety -- whereas ree-v3 failure modes are operationally defined at substrate level (stuck in one mode, oscillating between modes, failing to aggregate across subdivisions). These are plausibly homologous but not identical.

## Limitations and caveats

Three worth flagging. First, this is a theoretical review, not primary empirical data. The weight it carries is as an organising frame that has since been tested extensively (Sridharan 2008, Goulden 2014, and many others) -- but Menon 2011 is the frame, not a falsification target in itself. Second, the psychopathological framing is clinical and human; ree-v3 substrate failures are computational. Translating "schizophrenia = aberrant DMN engagement" into "ree-v3 substrate signature X" is not licensed by this paper directly. Third, Menon's treatment of the SN's internal computation is at the architectural level -- it says the SN coordinates, not *how*. The softmax-over-affinity aggregation rule in SD-032a's implementation is a design choice, not something Menon specifies.

The REE four-mode extension (external_task, internal_planning, internal_replay, offline_consolidation) goes beyond Menon's triple-network vocabulary. CEN and DMN do not map cleanly onto that finer grain. Internal_replay and offline_consolidation in particular require additional grounding from the hippocampal and sleep literature already pulled into the parent SD-032 directory (Carr, Jadhav & Frank 2011; Tambini & Davachi 2019; Frankland & Bontempi 2005).

## Confidence reasoning

0.78 reflects the balance between high source quality (authoritative review from the theorist who coined the triple network model) and moderate transfer risk (clinical → computational mapping is architectural, not mechanistic). Source quality 0.85, mapping fidelity 0.75, transfer risk 0.35. The paper is the right foundational scaffold for SD-032a's existence; it does not constrain the implementation details. Treat it as "the reason SD-032a is a substrate and not just a method inside dACC" rather than "the specification of how SD-032a should compute."

Together with Sridharan 2008 (causal role) and Goulden 2014 (DCM replication), Menon 2011 forms a coherent biological license for the coordinator architecture. The three papers answer, respectively: (a) is there a coordinator? (b) is the coordinator finding robust to methodological variation? (c) is the coordinator architecture load-bearing for transdiagnostic function? The answers are yes, yes, and yes.
