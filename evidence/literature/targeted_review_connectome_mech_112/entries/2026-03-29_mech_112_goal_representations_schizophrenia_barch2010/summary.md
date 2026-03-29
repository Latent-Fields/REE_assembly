# Barch and Dowd (2010) -- Goal representations and motivational drive in schizophrenia

**Claim tested:** MECH-112 (E3 requires a structured latent goal representation distinct from harm avoidance)

## What the paper did

Barch and Dowd set out to explain negative symptoms in schizophrenia -- avolition, anhedonia, asociality -- within a neuroscientific framework that could generate testable hypotheses. Their central insight, drawing heavily on Berridge's wanting/liking work and on prefrontal-striatal circuit research, is that negative symptoms do not primarily reflect a failure to experience pleasure. Rather, they reflect a failure to use internal representations of anticipated reward and goal states to drive behavior. Patients enjoy pleasurable experiences when they occur -- liking is intact -- but they do not initiate behavior to bring those experiences about -- wanting is impaired. The paper reviews neuroimaging and behavioral evidence and proposes that prefrontal-striatal circuits (particularly ventral PFC projections to ventral striatum/NAc) are the critical substrate for maintaining goal representations and translating them into motivational drive.

## Key findings relevant to MECH-112

The wanting/liking dissociation in schizophrenia is the key finding. Multiple studies reviewed in this paper show that when patients with schizophrenia are placed in pleasurable contexts, they rate their hedonic experience comparably to controls (intact liking). Yet their daily behavior shows dramatically reduced initiation of goal-directed activities, reduced anticipatory pleasure, and reduced effort allocation (impaired wanting/approach). This dissociation mirrors the dopamine depletion experiments in rodents, now documented in a human clinical population across multiple independent research groups.

The prefrontal-striatal framing is important for MECH-112's architectural specification: goal representations are maintained in prefrontal working memory and communicated to striatum to generate motivational drive. This maps to E3's role in REE -- E3 is the large complex that includes trajectory evaluation, commitment gating, and goal maintenance. The failure mode described (PFC goal representation fails to drive striatal approach) is exactly what MECH-112 predicts will happen when z_goal is absent: E3 can evaluate trajectories hedonically (liking, benefit_eval_head) but cannot generate approach gradients (wanting, z_goal_latent).

## REE translation

MECH-112's claim that E3 requires a distinct z_goal representation beyond harm avoidance is supported by this paper as a clinical existence proof. The schizophrenia negative symptom profile is what REE would look like without MECH-112 implemented: intact harm-avoidance (patients with primary negative symptoms are not reckless), intact hedonic evaluation at contact (liking/benefit_eval_head works), but absent prospective goal-directed approach (wanting/z_goal fails). The result is behavioral passivity and quiescence -- precisely the degenerate policy that MECH-112 is designed to prevent. The paper also provides the architectural pointer: goal representations must be maintained across temporal delay (working memory / LSTM hidden state in E1 for MECH-116) and communicated to the approach-generation system (E3/hippocampal trajectory scorer) to produce motivated behavior.

## Limitations and caveats

This is a theoretical review, not primary experimental data. The prefrontal-striatal mechanism is a hypothesis that organises heterogeneous findings but has not been definitively demonstrated as the cause of avolition. Schizophrenia is a complex disorder with multiple contributing mechanisms, and negative symptoms may have heterogeneous causes across patients. The wanting/liking dissociation in schizophrenia has been replicated but the specific mechanism (dopamine dysregulation, PFC working memory failure, effort discounting) is still debated. The clinical population may differ from a normally developing artificial agent in ways that make direct architectural analogies problematic.

## Confidence reasoning

Confidence is 0.75. Good theoretical review that maps well to MECH-112's architectural specification. The clinical existence proof is valuable -- it shows that systems with intact liking but absent wanting exist and show the predicted behavioral profile. Confidence is moderate because the paper is not primary data and the mechanistic account is hypothetical.
