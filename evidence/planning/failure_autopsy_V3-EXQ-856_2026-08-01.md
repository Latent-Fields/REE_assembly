# Failure Autopsy: V3-EXQ-856 (SD-087 harm-surprise PE fingerprint)

**Generated:** 2026-08-01T14:08:00Z
**Run:** `v3_exq_856_sd087_harm_surprise_pe_fingerprint_20260801T124431Z_v3`
**Queue ID:** V3-EXQ-856
**Claim IDs:** SD-087 (first-ever evidence run for this claim)
**Status:** confirmed
**Read alongside:** `failure_autopsy_V3-EXQ-857_2026-08-01.md` (the driver's own designated follow-up)

## 1. Facts

**Design.** SD-087's own falsifier: re-runs the V3-EXQ-664 affective fingerprint as a two-arm raw-warmup experiment (ARM_OFF: `harm_surprise_pe_enabled=False`, the 664 default; ARM_ON: `harm_surprise_pe_enabled=True`, SD-020's precision-weighted PE target). Tests whether flipping the SD-020 flag reduces the "664 saturation-and-inversion signature" (sub-floor within-episode CoV of z_harm_a, AND inverted mode-ordering shelter>avoid).

**Outcome:** FAIL. `non_degenerate: true`. Label: `sd087_falsified_signature_survives_flag_flip`.

**Criteria:**
- `off_reproduces_664_signature` (load-bearing): **PASS** — 2/3 seeds show the signature in ARM_OFF.
- `on_reduces_signature` (load-bearing): **FAIL** — ARM_ON ALSO shows the signature (2/3 seeds).

**Non-degeneracy check:** `pe_differentiated: 1.0` — the manipulation demonstrably took: `mean_harm_obs_ema` moved from 0.0 (OFF) to 0.0245 (ON), confirming the PE branch genuinely trains against a different target. `mean_cov_z_harm_a` barely moved: 0.00706 (OFF) vs 0.00742 (ON) — both far below the 0.05 saturation floor.

## 2. Claim-layer mapping

SD-087 (candidate, no `epistemic_category` set prior to this — first evidence). Title: *"SD-020's stable reading is scoped to the flag-on configuration and does not describe default-trained agents."* This is a narrower scoping observation on its face — but the driver's PASS condition ("SD-087 upheld") requires the flag, when flipped, to actually fix the 664 signature, testing an implicit stronger causal hypothesis built on top of the scoping claim.

## 3. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | SD-087's own falsifier, first-ever run, tested fairly |
| Biological reference | not load-bearing | substrate-internal wiring question |
| Prerequisites | present | manipulation confirmed to take (harm_obs_ema differentiated) |
| Implementation | complete | clean two-arm design matching 664 |
| Environment | adequate | same env as 664 |
| Measurement | clean, not a close call | both criteria unambiguous (2/3 vs 2/3, same signature both arms) |
| Integration | coupled | PE branch engages, but doesn't touch the CoV/inversion readout |
| Scale | adequate | 3 seeds, clean signature reproduction |

## 4. What this weakens, and what it doesn't

This result does **not** falsify SD-087's literal, narrower claim — that SD-020's own validation (V3-EXQ-324b) was scoped to a flag-on configuration and doesn't describe default (flag-off) agents. That remains true regardless of this run's outcome (ARM_OFF's clean reproduction of the 664 signature is, if anything, consistent with default agents behaving differently from SD-020's validated setup).

What this **does** weaken is the stronger, implicit causal hypothesis the falsifier was built to test: that simply flipping the flag on an already-raw-warmup-trained agent reproduces SD-020's validated benefit. It doesn't — the signature survives the flag flip even though the flag demonstrably changes the training target. This relocates the explanation for the 664 signature away from "just turn the flag on" and toward either (a) the flag needing to be set from the *start* of training (not applied post-hoc), or (b) the defect living in the encoder or environment rather than this specific training-target choice — exactly the fork the driver's own docstring names, handing off to Q-086/V3-EXQ-857.

## 5. Learning extracted

1. Confirming a flag genuinely engages (via a clean, differentiated proxy metric) while the hypothesized downstream effect stays flat is a clean, informative dissociation — not a substrate-readiness problem.
2. SD-087's literal scoping claim and the stronger causal hypothesis built on top of it should be scored separately — this run only speaks to the latter.
3. The 856→857 handoff (PE-target hypothesis → environment hypothesis) is a well-designed falsifier chain, though 857 itself could not complete its half (see companion autopsy).

## 6. Routing

**Evidence direction: `weakens`** (confirmed, matches self-route, scoped to the causal-flag-flip hypothesis rather than SD-087's literal scoping text).

**Routing: `/queue-experiment`** — no new experiment needed from this autopsy directly (the driver already queued its own designated follow-up, V3-EXQ-857), but recommend a further redesign once V3-EXQ-857's own precondition failure (see companion autopsy) is resolved: a version of 856 that sets the flag from the *start* of training (not raw-warmup-then-flip) would cleanly test the remaining "needs to be set from training start" hypothesis.

Re-derive brake: 0 prior `substrate_ceiling` autopsies for SD-087 (first-ever run) — does not fire.
