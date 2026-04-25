# Targeted Literature Review — SD-037 Orexin Kinetics

**Subject:** SD-037 Broadcast Override Regulator (orexin-analog), parameter anchoring
**Parameters under review:** `sustained_threat_window`, `decay_rate`, `recruitment_threshold`, `alpha_override`
**Date:** 2026-04-25
**Scope:** Parameter-anchoring lit-pull for the four scalar defaults of the SD-037 regulator. 5–15 references, biomedical literature only. PubMed via NCBI MCP; web search for review-level coverage.

---

## 1. Sources cited

| # | Citation | PMID | DOI |
|---|----------|------|-----|
| 1 | Mileykovskiy BY, Kiyashchenko LI, Siegel JM. Behavioral correlates of activity in identified hypocretin/orexin neurons. *Neuron* 2005;46(5):787–98. | [15924864](https://pubmed.ncbi.nlm.nih.gov/15924864/) | [10.1016/j.neuron.2005.04.035](https://doi.org/10.1016/j.neuron.2005.04.035) |
| 2 | Lee MG, Hassani OK, Jones BE. Discharge of identified orexin/hypocretin neurons across the sleep-waking cycle. *J Neurosci* 2005;25(28):6716–20. | [16014733](https://pubmed.ncbi.nlm.nih.gov/16014733/) | [10.1523/JNEUROSCI.1887-05.2005](https://doi.org/10.1523/JNEUROSCI.1887-05.2005) |
| 3 | Karnani MM, Schöne C, Bracey EF, et al. Role of spontaneous and sensory orexin network dynamics in rapid locomotion initiation. *Prog Neurobiol* 2020;187:101771. | [32058043](https://pubmed.ncbi.nlm.nih.gov/32058043/) | [10.1016/j.pneurobio.2020.101771](https://doi.org/10.1016/j.pneurobio.2020.101771) |
| 4 | Johnson PL, Molosh A, Fitz SD, Truitt W, Shekhar A. Orexin, stress, and anxiety/panic states. *Prog Brain Res* 2012;198:133–61. | [22813973](https://pubmed.ncbi.nlm.nih.gov/22813973/) | [10.1016/B978-0-444-59489-1.00009-4](https://doi.org/10.1016/B978-0-444-59489-1.00009-4) |
| 5 | Johnson PL, Truitt W, Fitz SD, et al. A key role for orexin in panic anxiety. *Nat Med* 2010;16(1):111–5. (panic/CO₂; cited in PMC3665356 as anchor for graded recruitment) | 19935666 | [10.1038/nm.2075](https://doi.org/10.1038/nm.2075) |
| 6 | Sakurai T. The role of orexin in motivated behaviours. *Nat Rev Neurosci* 2014;15(11):719–31. (review of intrinsic depolarisation and stress recruitment) | 25301357 | [10.1038/nrn3837](https://doi.org/10.1038/nrn3837) |
| 7 | Bassetti CLA, Adamantidis A, Burdakov D, et al. Narcolepsy — clinical spectrum, aetiopathophysiology, diagnosis and treatment. *Nat Rev Neurol* 2019;15(9):519–39. | 31324898 | [10.1038/s41582-019-0226-9](https://doi.org/10.1038/s41582-019-0226-9) |
| 8 | Dauvilliers Y, Siegel JM, Lopez R, Torontali ZA, Peever JH. Cataplexy — clinical aspects, pathophysiology and management strategy. *Nat Rev Neurol* 2014; reviewed in PMC8788644. | 24890646 | [10.1038/nrneurol.2014.97](https://doi.org/10.1038/nrneurol.2014.97) |
| 9 | Heymsfield SB, Avena NM, Baier L, et al. Hyperphagia: current concepts and future directions, proceedings of the 2nd international conference on hyperphagia. *Obesity* 2014;22 Suppl 1:S1–17. (PWS-anchored hyperphagia metrics) | 25164380 | [10.1002/oby.20646](https://doi.org/10.1002/oby.20646) |
| 10 | Crinò A, Fintini D, Bocchini S, Grugni G. Hyperphagia in Prader-Willi syndrome with obesity: From development to pharmacological treatment. *Diabetes Metab Syndr Obes* 2023;16:739–58. | 36879665 | [10.2147/DMSO.S229576](https://doi.org/10.2147/DMSO.S229576) |
| 11 | Mahler SV, Smith RJ, Moorman DE, Sartor GC, Aston-Jones G. Multiple roles for orexin/hypocretin in addiction. *Prog Brain Res* 2012;198:79–121. (high-effort recruitment; "James/Aston-Jones 2017" lineage) | 22813971 | [10.1016/B978-0-444-59489-1.00007-0](https://doi.org/10.1016/B978-0-444-59489-1.00007-0) |
| 12 | Marino RAM, McDevitt RA, Gantz SC, et al. Control of food approach and eating by a GABAergic projection from lateral hypothalamus to dorsal pons. *Proc Natl Acad Sci USA* 2020;117(15):8611–8615. | 32229573 | [10.1073/pnas.1909340117](https://doi.org/10.1073/pnas.1909340117) |

(All retrieved via PubMed; metadata-confirmed PMIDs above are returned by the PubMed MCP. PMIDs 19935666, 25301357, 31324898, 24890646, 25164380, 36879665, 22813971, 32229573 are widely cited in the surfaced PMC reviews; I have not separately metadata-verified each in this lit-pull. Treat the four metadata-confirmed core anchors — refs 1, 2, 3, 4 — as the primary spine; refs 5–12 as supporting context.)

---

## 2. Parameter anchors

### 2.1 `sustained_threat_window` (currently planned: 12 steps)

**What this controls.** Length of the rolling window over which sustained-threat magnitude is integrated to compute override drive. In SD-037 each "step" is roughly one behavioural decision.

**Biological anchor:** Mileykovskiy 2005 (PMID 15924864) and Lee/Hassani/Jones 2005 (PMID 16014733) show orexin neurons fire **transiently** to single sensory stimuli (sub-second to seconds) but show **sustained elevation across whole episodes of active waking / exploration** lasting tens of seconds to minutes. Karnani 2020 (PMID 32058043) shows sub-second locomotion-initiation bursts but with carry-over modulation across sustained foraging bouts. Johnson 2012 (PMID 22813973) reviews stressor-class sustained activation: footshock and immobilisation produce orexin recruitment that persists across the stressor episode (typically minutes in those paradigms).

The convergent picture: orexin integrates threat signal across **a behavioural episode**, not single events and not minute-scale homeostasis. If one REE step ≈ one behavioural decision (~1–3 s of real time), an integration window of ~10–20 steps (~10–60 s of integrated threat history) sits in the centre of the biological band.

**Suggested default:** 12 steps. **Confidence: medium.** The biology supports a window in the 8–25-step range; 12 is well within it. The literature does not constrain the exact value to one digit.

### 2.2 `decay_rate` (currently planned: 0.05 EMA decay)

**What this controls.** EMA smoothing on the override_signal — how fast the override authority dissipates once threat or drive falls.

**Biological anchor:** Lee/Hassani/Jones 2005 (PMID 16014733) — orexin neurons "increase firing before the end of PS and thereby herald by several seconds the return of waking and muscle tone"; firing transitions across state changes are on the order of **2–7 s** before EMG change. Mileykovskiy 2005 shows transient sensory-evoked activation (seconds-scale), with episode-level firing scaling with behavioural state. Karnani 2020 (PMID 32058043) shows sub-second initiation kinetics but slower (multi-second) population-level decay after locomotion offset. Sakurai 2014 (PMID 25301357) describes orexin neurons as intrinsically depolarised and slow to silence — recruited tonus persists beyond stimulus offset.

Crucially the override authority is **not fast like a single-spike transient**: it carries over through behavioural episodes (Mileykovskiy: "moderate and approximately equal levels of activity during grooming and eating") and falls only when the animal disengages. That maps to an EMA half-life on the order of **5–20 steps**, i.e. decay_rate roughly **0.035 to 0.13** (where decay_rate = 1 − exp(−ln 2 / half_life_steps)).

**Suggested default:** 0.05 (half-life ≈ 14 steps). **Confidence: medium.** The biological band is wide; 0.05 is within it but slightly slow. Consider 0.07 if EXQ behavioural episodes are short (~7-step half-life).

### 2.3 `recruitment_threshold` (currently planned: 0.5)

**What this controls.** Above this normalised override_signal value, drive can seed z_goal and dACC re-weighting kicks in. Below it, override is silent.

**Biological anchor:** Mileykovskiy 2005 (PMID 15924864) shows ~**5x** increase from quiet waking to active waking with **maximal** firing during exploration. Lee/Hassani/Jones 2005 (PMID 16014733): aW = 3.17 ± 0.79 Hz vs qW = 0.64 ± 0.22 Hz (~**5x ratio**, validating the Mileykovskiy claim with identified cells), with transition firing pre-empting behavioural state changes by 2–7 s. Johnson 2012 (PMID 22813973) and the panic literature (PMID 19935666) frame recruitment as **graded** with a behaviourally relevant inflection — orexin antagonists block panic-class responses but not baseline arousal. Sakurai 2014 (PMID 25301357) emphasises intrinsic depolarisation near firing threshold (positive feedback for population recruitment), consistent with sigmoidal recruitment. Mahler/Aston-Jones 2012 (PMID 22813971) shows recruitment specifically under high-effort / high-demand contingencies (e.g., reinstatement under cost), not baseline reward.

The biology is best described as **graded with an inflection** rather than a hard step. A normalised threshold at ~0.5 places the inflection in the middle of the dynamic range. Given the ~5x active/quiet ratio, the recruitment knee should sit such that quiet-waking-equivalent input produces near-zero override and active-waking-equivalent input saturates — a midpoint threshold is consistent.

**Suggested default:** 0.5. **Confidence: low–medium.** The biology supports a graded, sigmoid-like recruitment with the inflection well above baseline. 0.5 on a normalised scale is a defensible midpoint. The literature does **not** give a precise quantitative anchor — engineering judgment dominates. If anything, the panic-recruitment data argue for a slightly higher threshold (0.55–0.65) so that override is recruited only under genuinely sustained drive+threat, not transient excursions.

### 2.4 `alpha_override` (currently planned: 0.5)

**What this controls.** Multiplicative scaling of MECH-279 PAG freeze-gate threshold by override_signal: `theta_freeze_effective = theta_freeze_base * (1 + alpha_override * override_signal)`.

**Biological anchor:** This is the SD-037 spec's MECH-280 substrate prediction — orexin/LH→PAG raises the freeze threshold, biasing toward active coping. Johnson 2012 (PMID 22813973) and the PNAS prefrontal-PAG circuit work cited in the lit-pull web search show **bidirectional** modulation: orexin in LH can elevate freeze-threshold (active coping), but orexin in dPAG can also drive panic-class responses. Net effect on the **ventrolateral** (passive freeze) PAG subcolumn is permissive of escape; net effect on the **dorsolateral/dorsomedial** subcolumn is panic-promoting. Marino 2020 (PMID 32229573) shows LH GABA→peri-LC coupling that supports foraging engagement under metabolic demand — this is the active-coping override channel SD-037 names.

Quantitative anchors are **sparse**. The literature reports that orexin antagonists block panic-class active responses without abolishing baseline freezing, consistent with a multiplicative gain on the freeze threshold rather than a hard switch. Order-of-magnitude estimates of orexin-induced excitability changes in downstream targets (LC, VTA, dorsal raphe) range from 1.3x to 3x firing-rate increases for saturating doses (Sakurai 2014, PMID 25301357). Mapped onto a multiplicative scaling factor in `theta_freeze_effective = theta_freeze_base * (1 + alpha_override * override_signal)` with override_signal saturating at 1.0, alpha_override = 0.5 gives a 1.5x maximum threshold elevation, which sits at the **lower end** of the biologically reported gain band.

**Suggested default:** 0.5 (giving 1.5x max threshold elevation). **Confidence: low.** The literature constrains the *direction* and *order of magnitude* but not the precise scalar. 0.5 is conservative; 1.0 (giving 2x max) would be equally defensible and arguably more biologically central. Recommend keeping 0.5 as initial default and treating it as a parameter to sweep in the SD-037 validation factorial.

---

## 3. Validation anchors

### 3.1 PWS-analog (saturated override)

- **Caloric per-meal intake:** PWS individuals consume up to **~3x normal caloric intake at a given meal** (Heymsfield 2014, PMID 25164380; PWS Foundation review of Holland/Whittington field data). Daily totals are confounded by environmental control (locked food in clinical settings) — per-meal data is the cleaner anchor.
- **Satiety failure:** absent or markedly delayed post-prandial satiety; food-seeking persists across hours rather than minutes (Crinò 2023, PMID 36879665).
- **REE saturated-override prediction:** Approach-commit rate to consummatory targets should be **2–3x the control rate**, and post-consummation drive_level should fail to decay (i.e., no satiety break in the drive→z_goal seeding loop).

**Quantitative target for SD-037 validation:** A saturated-override arm should show **≥2x** relative increase in approach-commit rate to consummatory cues compared to the {SD-036 ON, SD-037 ON} balanced arm. Higher (3x) is consistent with the biology but a 2x floor is the more defensible target.

### 3.2 Narcolepsy/cataplexy-analog (lost override)

- **Cataplexy frequency:** highly variable, "fewer than one episode per year to **up to ~20 per day**" (Bassetti 2019, PMID 31324898; Dauvilliers 2014 PMID 24890646). In severe untreated cases multiple per day is typical.
- **Cataplexy attack duration:** humans, **seconds to ~2 min**; mouse Hcrt-/- model **15 s to 2 min, mean ~60 s** (Dauvilliers 2014 / cataplexy review PMC8788644).
- **Trigger:** strong emotion (laughter most common positive trigger, anger most common negative); **~50%** of attacks in some cohorts are spontaneous with no identifiable trigger.
- **Coupling failure signature:** drive and emotion compute normally but fail to recruit motor/coordinated behaviour. Bassetti 2019 frames this as the canonical decoupling phenotype.

**Quantitative target for SD-037 validation:** A lost-override arm should show **drive_level computing normally** (within 80–120% of control range) **AND** approach-commit rate at consummatory targets reduced to **<30% of control**, demonstrating the decoupling rather than upstream computational failure. Episodic "drop" events (transient action-selection failures during high-emotion episodes) are an additional optional signature, but are likely a stretch goal for V3 substrate granularity.

### 3.3 Honest gaps

- No quantitative anchor identified for **mean cataplexy frequency in laughter-triggered subset** vs other triggers — the literature reports presence/absence but not frequency-per-trigger ratios cleanly.
- No quantitative anchor identified for **per-step approach rate in PWS** at the timescale REE simulates — only per-meal consumption ratios.
- The 2x and 3x thresholds in §3.1 and §3.2 are derived from human caloric data and qualitative coupling-loss descriptions, not from a parametrically matched animal model — treat as **directional** rather than precision targets.

---

## 4. Counter-indications

Are any of the planned defaults **biologically counter-indicated** — i.e., would the literature say "no, do not use that value or that mechanism"?

**No outright contradictions.** The four planned defaults sit within the biologically plausible band for each parameter. Two soft cautions:

1. `recruitment_threshold = 0.5` is at the lower edge of biological defensibility. The panic/Aston-Jones lineage argues for recruitment specifically under **high-effort, sustained, biologically-significant** conditions, not generic above-midline arousal. If the SD-037 validation factorial shows excessive false-positive override recruitment (drive seeding z_goal under merely moderate threat), increase to 0.55–0.65.

2. `alpha_override = 0.5` is conservative. The biological gain band is 1.3x–3x for saturating orexin doses on downstream excitability; a 1.5x maximum threshold elevation may produce only a marginal active-coping shift. If the validation factorial shows partial freeze-rescue (override fires but does not flip the behavioural mode), increase alpha_override toward 1.0 (2x max).

The biggest **mechanistic** caveat the literature surfaces (and the SD-037 spec already names) is that orexin's effect on PAG is **subregion-specific**: dorsolateral/dorsomedial PAG promotes panic-class active responses, ventrolateral PAG is permissive of escape over freeze. SD-037's MECH-280 collapses these into a single `theta_freeze` modulator. This is acceptable for V3 (no PAG subcolumn substrate exists) but should be flagged for V4 where dual-channel PAG modulation may matter for distinguishing panic from goal-directed active coping. This is a substrate-granularity caveat, not a parameter-value caveat.

---

## 5. Bottom line for SD-037 implementation

| Parameter | Planned | Suggested | Confidence | Recommended action |
|---|---|---|---|---|
| `sustained_threat_window` | 12 steps | 12 steps | medium | keep as planned |
| `decay_rate` | 0.05 | 0.05 (band: 0.035–0.13) | medium | keep; consider 0.07 if episodes shorter than 14-step half-life |
| `recruitment_threshold` | 0.5 | 0.5 (consider 0.55–0.65) | low–medium | keep for first run; tune up if false-positive override observed |
| `alpha_override` | 0.5 | 0.5 (consider up to 1.0) | low | keep for first run; treat as a sweep parameter in validation factorial |

The four planned defaults are biologically defensible. Two (recruitment_threshold, alpha_override) are at the low/conservative end of the biological band and may need tuning upward if the SD-037 validation factorial shows under-recruitment of override authority. None are counter-indicated.

The PWS and narcolepsy/cataplexy validation anchors give the SD-037 4-arm factorial concrete quantitative targets: saturated-override arm should show **≥2x approach-commit rate**; lost-override arm should show **drive computing normally with approach-commit rate <30% of balanced arm**. These are directional rather than precision targets — do not over-fit to them.
