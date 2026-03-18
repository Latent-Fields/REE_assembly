# Literature Summary: 2026-03-17_cerebellar_forward_model_wolpert1998

- Scope: Cerebellar forward models for efference copy prediction and reafference cancellation.
- Claim linkage:
  - `MECH-098` (encoder reafference cancellation — cerebellum is the biological instantiation of the forward model component)
  - `MECH-095` (TPJ agency comparator — cerebellar forward model generates the "expected reafference" that TPJ comparator subtracts)
- Direction: supports
- Confidence: 0.80
- Key finding: The cerebellum implements paired forward and inverse models (MOSAIC architecture). Forward models receive efference copies of motor commands via the pontocerebellar pathway and predict the resulting sensory reafference. Output via dentate nucleus → VL thalamus → motor/premotor cortex closes the loop. Subsequent TMS and fMRI work confirmed: cerebellar activity is reduced for self-generated vs externally generated stimulation — direct evidence of reafference cancellation.
- REE relevance: The E2_self prediction head is REE's forward model equivalent. The reafference cancellation pathway (cerebellum → thalamus → premotor → PPC) is the biological instantiation of the coupling MECH-098 requires: predicted self-change must inform z_world encoding to cancel perspective shift. The cerebellum-to-PPC pathway via thalamus is the efference copy route that MECH-098 adds to the encoder architecture.
- Caveat: Framework paper from 1998; subsequent MOSAIC refinements exist. Core claim of cerebellar forward models is now well-supported empirically but exact implementation details remain debated.
