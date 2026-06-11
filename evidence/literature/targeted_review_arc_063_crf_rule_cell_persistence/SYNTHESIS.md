# Targeted review — ARC-063 CRF rule-cell persistence: how are differentiated PFC rule/task-set representations MAINTAINED across input-absent epochs?

- **Review slug:** `targeted_review_arc_063_crf_rule_cell_persistence`
- **Generated (UTC):** 2026-06-11T07:21:11Z
- **Routed by:** confirmed `failure_autopsy_V3-EXQ-666_2026-06-11` (load-bearing finding: differentiation and persistence are in tension; once e2_world_forward delivers a differentiated pool, per-rule availability does not accumulate under sparse matching, so `crf_frac_active` collapses to 0.016).
- **Claim grounded:** ARC-063 (rule-apprehension architectural slot, strong reading — distributed CandidateRule field with tolerance-gated availability). Informs MECH-309 / ARC-062 readiness.
- **Status:** lit-pull only. Gates the downstream `/implement-substrate` session (`sd_id_suggested: crf-availability-maintenance`). NO substrate code, NO claims.yaml/manifest/substrate_queue edits in this session.

---

## The fork (as posed by the autopsy)

> When a rule cell is narrowly (selectively) tuned and therefore matches/fires only on a small fraction of inputs, what sustains its "availability" between matches?
>
> **(A) persistent-firing maintenance** — sustained delay-period activity / recurrent-attractor dynamics (Goldman-Rakic; Wang) → the fix is a sustained-activity term that holds CRF availability across context-absent ticks; **vs**
> **(B) activity-silent / synaptic maintenance** (Stokes 2013; Lundqvist 2016) → the `crf_frac_active` "active fraction" readout is itself biologically questionable; rules are silently maintained and reactivated, which changes the readiness READOUT, not just the credit dynamics.

---

## Verdict: **B, with a bounded role for A.** The available pool is held activity-silently; only the engaged rule fires.

The modern primate-WM literature does not split cleanly down the A/B line the autopsy drew — it has largely **converged on B for the maintenance of unselected items**, with A surviving as the mechanism for the *one item currently being acted on*. The decisive shift is Lundqvist, Herman & Miller (2018), whose whole thesis is that the "persistent spiking" picture is an artifact of trial-and-time averaging: on single trials activity is **sparse and bursty**, and between bursts the memory is carried by **short-term synaptic plasticity — "impressions left in the network."** Stokes (2015) makes the same point from the human/dissociation side (memory decodable while neurons are silent; delay firing waxes and wanes with task relevance). Mongillo, Barak & Tsodyks (2008) supply the implementable mechanism: calcium-mediated synaptic facilitation maintains a memory **without spiking**, decaying slowly and refreshed by **occasional, low-rate** activity. Funahashi (1989) and Compte/Wang (2000) — the fork-A anchors — remain valid but bounded: they show sustained firing maintains the **single engaged memorandum**, and Compte/Wang explicitly bound persistent-firing maintenance to **one capacity-limited bump**, which cannot scale to holding a differentiated pool of 10–16 rules.

Crucially, **fork A and fork B are not mutually exclusive** — they are the two halves of one system. The engaged rule reverberates (A); the available-but-unselected pool sits in the silent synaptic store (B) and reactivates on probe. This maps exactly onto the CRF's structure: at most a few rules are *matched-and-selected* per tick (these can carry a sustained term), while the differentiated *pool* must remain available across thousands of context-absent ticks (this must be silent).

### Why this is the right call for the CRF specifically

The CRF's V3-EXQ-666 failure is the *textbook* prediction of the activity-silent literature. Once differentiation is real (ARM_2: 10–16 distinct rules, pairwise distance 1.71), each rule matches a narrow context slice and is unselected almost always. The current `availability` is an activity-dependent EMA that **decays every tick** (`mature_availability_decay = 0.001`) and is refreshed only on match, so between sparse matches it erodes toward the retire floor and `crf_frac_active` collapses to 0.016 — *worse* than the undifferentiated legacy (0.125). That is precisely "averaged activity hides sparse-but-maintained coding" (Lundqvist) and "a metric that counts only active ticks misreads a maintained-but-silent item as absent" (Stokes). The autopsy's hypothesis — that fork B "would change the readiness readout, not just the credit dynamics" — is **confirmed by the literature**.

---

## Concrete recommendation for the CRF maintenance mechanism

The downstream `/implement-substrate` session (new substrate_queue entry `crf-availability-maintenance`) should implement **both** prescriptions below. They are independent and both are load-bearing; doing only one will not lift the gate.

### 1. Maintenance: make availability an activity-decoupled, slowly-decaying synaptic trace (fork B / Mongillo)

A minted, differentiated rule's availability should be a **maintained property** that persists across context-absent ticks *without the rule firing*:

- **Decouple decay from elapsed ticks.** The offending term is the per-tick `mature_availability_decay` that erodes availability whether or not the rule's context ever recurs. Replace it with a **maintenance floor / long-horizon decay**: once a differentiated rule is minted, its availability must not fall below a maintenance level for a long, deliberately-set horizon (a "synaptic impression"). Decay should be driven by **interference/capacity** (a new, very-similar rule overwriting the slot) — not by silence.
- **Refresh on sparse match, do not require continuous activity.** Mongillo's "occasional refresh at a low rate" *is* the CRF's sparse-match regime; a rule that matches rarely is the case facilitation is built for. Keep crediting availability on match; just stop punishing the gaps.
- **Set the maintenance horizon as a free parameter, not the biological constant.** Biology's facilitation time constant is ~1 s; the CRF must survive inter-match gaps of hundreds–thousands of ticks. Import the *form* (silent, slow, sparse-refresh), set the *horizon* to the measured typical inter-match interval in the differentiated regime.

### 2. Readout: replace/supplement `crf_frac_active` with a maintained-pool metric (the autopsy's "changes the readout" branch — CONFIRMED)

`crf_frac_active` (fraction of ticks with an active rule) measures *read-out*, not *maintenance*, and is exactly the averaged-activity artifact Lundqvist warns against. Add a **maintained/available-pool readout**:

- `crf_pool_available` (or `crf_frac_maintained`) = the number/fraction of *differentiated* rules whose maintained availability **would clear threshold if their context recurred** — independent of whether that context is present this tick. This is the biologically-faithful "is the rule still in the silent store?" question.
- The **CRF-readiness gate should be re-stated on the maintained pool**, e.g. "≥2 differentiated rules (pairwise distance > 0.1) are simultaneously *maintained-and-reactivatable*" — rather than `crf_frac_active >= 0.30`. The 0.30 active-fraction floor is the wrong target for a sparsely-matching differentiated pool and should not survive into the 666-successor diagnostic unchanged.
- Optionally keep "active-on-match efficiency" as a *separate secondary* readout (it is informative, just not the persistence criterion).

### 3. (Secondary, optional) A sustained-activity term for the engaged rule only (fork A / Funahashi, Compte/Wang)

For the ≤ few rules that are *matched-and-selected* on a tick, a short reverberation term (hold availability elevated for a window after firing) is biologically licensed and cheap. This is **not** the fix for the pool problem — do not let it substitute for (1) — but it models the engaged-rule half of the system and pairs naturally with Mongillo's "strong facilitation → reactivation bursts."

---

## What to carry into the substrate session / 666-successor diagnostic

- The maintenance mechanism is **activity-silent synaptic trace** (prescription 1), **and** the readiness readout must change (prescription 2). The autopsy's fork resolves to B; the "redefine the readout" branch is the correct one, not merely a credit-dynamics tweak.
- The 666-successor CRF-readiness diagnostic should gate on a **maintained-pool** metric, not `crf_frac_active >= 0.30`. Re-using the old gate would re-fail a substrate that is actually working as biology prescribes.
- Adopt `crf_context_from_e2_world_forward` as the mature-regime differentiation default (already confirmed by 666 ARM_2; this review does not disturb that).
- Set the availability maintenance horizon empirically from the typical inter-match gap in the differentiated regime — not from the biological ~1 s constant.

## Debate balance (the verdict is adopted, not declared settled)

Fork B is adopted as the maintenance model for the *pool* because that is where the convergent weight of evidence — and the most-relevant evidence for a sparsely-matched selective cell — lies. But the persistent-activity camp's rebuttal is live: Constantinidis et al. 2018 ("Persistent Spiking Activity Underlies Working Memory", the back-to-back point to Lundqvist's counterpoint in the same *J Neurosci* issue) holds that delay-period spiking *is* the carrier and that rhythmic-/synaptic-only accounts are inconsistent with the primate data. The directive set above is deliberately **robust** to that dispute: it adopts the activity-silent *form* without asserting the neuroscience is closed, and because the engaged-rule sustained term (A) and the silent-pool trace (B) are complementary, the CRF carries both. Notably, even the persistent camp defends *trial-/time-averaged* elevation (not continuous single-cell firing) and concedes a maintained item need not be read out every moment — so the operative conclusion for REE (`crf_frac_active`, an *instantaneous* fraction, is the wrong readout for a sparsely-matched pool) survives regardless of which side of the firing-vs-silent debate prevails.

## Evidence base (6 entries, all ARC-063)

| Entry | Fork | Direction | Conf | Role |
|---|---|---|---|---|
| Funahashi, Bruce & Goldman-Rakic 1989 (J Neurophysiol) | A | supports | 0.74 | Existence proof: selective PFC delay-period maintenance of the engaged item. |
| Compte, Brunel, Goldman-Rakic & Wang 2000 (Cereb Cortex) | A | mixed | 0.70 | Recurrent-attractor mechanism for A — *and* bounds it to one capacity-limited bump (cannot hold a differentiated pool). |
| Constantinidis, Funahashi, Lee, Murray, Qi, Wang & Arnsten 2018 (J Neurosci) | A | mixed | 0.62 | Pole-A position piece (2018 point–counterpoint): persistent spiking is the carrier; the live rebuttal that keeps the fork from being declared closed. Supports the maintenance class; argues against the silent-only reading. |
| Stokes 2015 (Trends Cogn Sci) | B | supports | 0.76 | Activity-silent framework; memory retained while silent → `crf_frac_active` is the wrong readout. |
| Mongillo, Barak & Tsodyks 2008 (Science) | B | supports | 0.78 | Implementable mechanism: synaptic facilitation, silent + slow + sparse-refresh = the CRF maintenance primitive. |
| Lundqvist, Herman & Miller 2018 (J Neurosci) | adjudication | supports | 0.75 | "Delay activity yes, persistent activity maybe not": sparse bursts + synaptic impressions; averaging hides maintained-but-silent coding. |

**Anchors already covered in sibling dirs (not duplicated here):** Frank 2006 / Frank 2001 / Cavanagh 2011 (`targeted_review_tolerance_gated_rule_availability`); Wallis & Miller 2001, Bongard 2010, Mante-adjacent mixed-selectivity Rigotti 2013 (`targeted_review_arc_062_rule_apprehension`); Wallis 2001 abstract-rule coding (`targeted_review_candidate_rule_field_representation`). This review deliberately scopes to the *maintenance* question those dirs did not address.
