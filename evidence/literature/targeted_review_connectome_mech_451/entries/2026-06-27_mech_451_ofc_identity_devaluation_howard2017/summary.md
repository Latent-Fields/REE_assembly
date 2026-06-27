# Identity-specific OFC reward representations modulated by devaluation (Howard & Kahnt, 2017)

**Claim under test:** MECH-451 — the intermediate channel-granularity falsifier. This paper is the best available biological match to the *separately-learnable* property the claim hinges on, via the "OFC-devaluation" finer channel.

## What the paper did

Howard and Kahnt scanned humans with fMRI and used multivariate pattern analysis (MVPA) during selective sensory-specific satiety: subjects ate one of two value-matched food outcomes to satiety, devaluing it while leaving the other intact. The question was whether OFC carries an outcome-*identity*-specific representation that can be updated independently for one outcome, or whether it tracks a single general value that would move for both.

## Key finding relevant to the claim

After devaluation, choices shifted away from the sated outcome *only*, and the lateral posterior OFC reward-identity pattern was selectively altered for that outcome while the non-sated outcome's pattern was retained. Critically, functional connectivity between identity-specific OFC and general-value vmPFC predicted individual differences in how much each subject's choices changed. So OFC holds a representation *finer* than a compressed scalar — outcome-specific, separately and independently updatable by state — and dissociable from the general value code in vmPFC.

"Separately and independently updatable by state" is the closest biological cousin to MECH-451's "separately-learnable channel" that this literature offers. It is direct evidence that finer, identity-specific representation supports goal-directed behavioural flexibility, which is the spirit of the falsifier.

## Mapping to REE

The mapping is good but not airtight, in two ways. First, "separately-updatable representation" is a cousin of "separately-learnable gating input," not the same thing — the paper shows OFC patterns *change* with devaluation, not that a downstream *learner* benefits from receiving them as a distinct channel. Second, and more pointedly, the finer OFC signal had to route *through* vmPFC general-value coding to influence choice (the connectivity-predicted-choice-change result). That is a funnel into a shared value bottleneck — structurally the very conversion-ceiling architecture MECH-451 is trying to characterise. Finer information exists upstream but must reconvert through a common value node to reach action.

## Caveats and confidence

Correlational human fMRI: it establishes that the finer channel exists and is independently updatable, and that its coupling to the value node tracks behaviour, but it cannot show causation in the "exposing a finer channel improves conversion" direction. I have logged it **supports** with the highest mapping_fidelity of the MECH-451 set (0.62) and confidence 0.62, with the vmPFC-bottleneck funnel recorded as a failure signature — it is simultaneously the best support for separability and a reminder that separability upstream does not guarantee conversion downstream.
