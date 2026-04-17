# Wang, Monaco, Knierim 2020 -- Hippocampal Place Cells Encode Surface-Texture Boundaries

## What the paper did

Wang, Monaco, and Knierim (2020) investigated whether hippocampal place cells encode surface texture as an independent spatial feature. Rats ran on 1D circular tracks and explored 2D platforms divided into regions of different floor textures. The texture transitions were flat, presenting no physical barrier or navigational obstruction. Textures had no associated reward, odour, or explicit instruction. The question was whether the hippocampus would segment space along texture boundaries even without functional or motivational reason to do so.

## Key findings

Approximately 40% of place field edges fell at or near surface-texture boundaries, compared to a 33% chance rate. This excess was statistically significant and replicated across 1D and 2D environments. Neural population vectors showed sharper decorrelation when comparing locations across a texture boundary than within a texture region. The hippocampus treats different-texture zones as more distinct spatial environments even when the only difference is floor material. The effect emerged without explicit training, reward, or instruction.

## REE translation

This paper is the most directly relevant for SD-023's core biological claim: neutral texture features structure hippocampal spatial representations. SD-023 proposes neutral landmark objects whose gradient fields create characteristic texture variation in world_obs across spatial locations. Wang et al. (2020) demonstrates the biological precedent: even uninstructed surface textures (analogous to gradient field variation) cause hippocampal spatial maps to segment more sharply. If texture variation in a biological world model creates sharper spatial state differentiation, the same principle motivates adding gradient texture to CausalGridWorldV2 -- it gives E1's LSTM inputs that vary in a spatially structured way, supporting richer state representations across the environment.

## Limitations

The study measures spatial map segmentation, not temporal prediction. SD-023 requires that E1's LSTM uses gradient texture for temporal forward prediction (MECH-216: anticipatory wanting fires before resource proximity rises). The evidence shows texture variation creates spatial segmentation but does not directly demonstrate temporal prediction capability in an LSTM world model. The effect size is also modest: ~7 percentage points above chance.

## Confidence reasoning

High source quality (Knierim lab, Current Biology, rigorous controls). Mapping fidelity is high for SD-023's ecological principle component. Transfer risk is moderate -- the mechanism requires extension from spatial map segmentation to temporal LSTM prediction.
