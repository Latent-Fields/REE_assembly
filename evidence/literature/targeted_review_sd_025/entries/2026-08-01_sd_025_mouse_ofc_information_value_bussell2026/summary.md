# Bussell et al. (2026) - Mouse OFC represents the intrinsic value of information

According to Nature Neuroscience, Bussell, Badman, Marton, Bromberg-Martin, Abbott, Rajan and Axel (2026, [DOI](https://doi.org/10.1038/s41593-026-02377-y)) developed an odor-based information-seeking task in mice. The task separated information from water reward: one port gave advance knowledge about whether water would arrive, while another port carried the same reward probability but no advance information. Mice preferred the information port, maintained the preference across side reversals, moved to it faster, and continued to choose information even when it reduced expected water. The authors estimated the value of information as several microliters of expected water and fit choices with separate value functions for water and information. They then recorded OFC calcium activity and found population representations for predicted information and received information that were dissociable from water-value representations. The information representation scaled with the delay interval and emerged with learning. The paper provides open source data and figure-analysis code.

For SD-025, this is a strong biological update to the "information has intrinsic value" premise. The existing Gottlieb et al. 2013 entry licenses an information-seeking drive as a theoretical/computational primitive; Bussell et al. adds rodent behavioral and neural evidence that advance information can be treated as a tradeable value, not merely as a side effect of reward prediction. That matters because SD-025 is a design decision, not just a parameter knob: it claims REE should have a trajectory-scoring bias for information-seeking that is not reducible to extrinsic reward. Bussell et al. supports that high-level decision, and it sharpens the claim by showing that OFC can carry separable intrinsic-information and extrinsic-water value axes.

The mapping is not one-to-one. SD-025 places the current implemented curiosity drive on hippocampal representational density: a uniform CEM scoring term favors denser regions of the RBF map, with familiarity acting as a brake. Bussell et al. is an OFC decision-value paper, not a hippocampal density or trajectory-planning paper. It does not show that information value should be computed as local representational density, and it does not test online movement through a cognitive map. The closest REE translation is therefore not "SD-025 is biologically proven" but: a separate information-value axis is biologically plausible and can influence choice even when it trades off against water reward. SD-025 remains one particular, weaker proxy implementation of that broader primitive.

This also touches MECH-111 and MECH-314b, but only secondarily. MECH-111 claims intrinsic positive valence for curiosity/novelty; Bussell et al. supports the information-seeking half, though the task is uncertainty-resolution rather than generic surprise. MECH-314b claims an uncertainty-driven curiosity bonus; Bussell et al. supports separable information value but does not provide the missing REE substrate requirement: a per-candidate uncertainty readout that can alter E3 selection. In fact, the paper's OFC result is a useful warning against collapsing information into generic reward value. A future per-candidate MECH-314b build should preserve an information-value axis rather than hiding it inside the water/reward score.

Confidence 0.71. Source quality is high: open-access Nature Neuroscience, explicit behavior, neural population data, task manipulations, source data and analysis code. Mapping fidelity is moderate: the paper directly supports intrinsic information value and OFC separability, but SD-025's implemented density-following hippocampal mechanism is not tested. Transfer risk is moderate because this is mouse odor choice/OFC imaging, while REE's mechanism is a hippocampal CEM scoring bias in an artificial substrate.

<!-- normalized-from-record-json 2026-08-14 -->

## Availability and source identifiers (from record.json)

- Preprint DOI (`preprint_doi`): 10.1101/2023.10.13.562291
- Preprint PMID (`pubmed_preprint`): 39416043
- Preprint PMC ID (`pmcid_preprint`): PMC11482914
- Code (`code_repository`): https://github.com/jjbussell/Bussell2026InfoValue
- Data (`data_repositories`):
  - 10.5281/zenodo.20450673
  - 10.5281/zenodo.20452041
  - 10.5281/zenodo.20466860
  - 10.5281/zenodo.20470580
  - 10.5281/zenodo.20470622
  - 10.5281/zenodo.20477351
  - 10.5281/zenodo.20479276
  - 10.5281/zenodo.20480778
  - 10.25452/figshare.plus.32582997
- Secondary trigger (how this paper surfaced) (`secondary_trigger`): https://neurosciencenews.com/ofc-curiosity-information-value-neuroscience-31156/
