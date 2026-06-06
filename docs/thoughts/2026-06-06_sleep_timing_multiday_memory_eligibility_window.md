Status: unprocessed
Source email date: 2026-03-31
Source email subject: REE timing for memory associated with sleep cycle
Source saved-item attribution: Daniel Golden
Gmail envelope sender: Eoin Mount
Current action: preserve as thought intake only
Primary source status: secondary article checked; original DOI/title identified but primary article not directly opened in intake session
Near-term relevance: offline integration / plasticity-window design compass; not REE-v3 critical path unless later linked to existing sleep/offline claims

---

# THOUGHT INTAKE: Multiday memory timing and plasticity eligibility windows

## 0. Summary claim

A saved REE email pointed to a Neuroscience News article titled "Perfect Timing for Memory Identified". The article reports a Journal of Neuroscience paper in which Aplysia sensorimotor neurons showed a critical time window for a second learning-related stimulus block. A second exposure at 24 hours enhanced long-term synaptic facilitation and long-term enhancement of neuronal excitability, while 18-hour and 32-hour intervals did not produce the same effect.

The important REE-relevant point is not the popular instruction to review material at the same time the next day. The useful architectural idea is narrower:

> plasticity may depend on temporally gated eligibility windows, not merely on repetition or total exposure.

For REE, this suggests that offline integration, replay, residue contextualisation, and memory consolidation may require explicit timing / eligibility gates rather than treating every replay or repeated exposure as equally write-capable.

---

## 1. Why this belongs in REE_assembly

This belongs in `REE_assembly` as a mechanism/open-question intake because REE already treats offline integration as a sleep analogue that consolidates and contextualises accumulated experience without bypassing waking action authority.

The possible relevance is to future design of:

- offline integration scheduling
- replay eligibility
- residue contextualisation windows
- multiday consolidation
- when repeated exposure should strengthen, weaken, or leave unchanged a latent trace
- how intrinsic molecular/cellular timer analogues might be represented computationally

This should not create a direct REE-v3 implementation task unless it later connects cleanly to existing offline-integration or plasticity-window claims.

---

## 2. Proposed classification

Likely classifications:

- **mechanism hypothesis:** repeated training/replay updates require temporally gated eligibility windows.
- **open question:** should REE distinguish replay exposure from write-eligible replay exposure?
- **architectural commitment candidate:** offline integration should include gateable timing state, not merely batch replay.

This should not be promoted directly to an invariant.

---

## 3. Relation to existing REE architecture

Potential mappings:

| Biological finding / framing | REE analogue |
|---|---|
| 24-hour second stimulus window | scheduled replay / consolidation eligibility window |
| 18h and 32h not sufficient in the reported preparation | timing-sensitive write gate, not simple exposure count |
| CREB1/CREB2 competition dynamics | competing consolidation vs repression / inhibition signals |
| intrinsic neuronal timer | local state-dependent eligibility timer inside a latent trace |
| long-term synaptic facilitation | strengthened predictive/transition pathway |
| long-term enhancement of neuronal excitability | lowered activation threshold / increased future readiness |
| multiday training | repeated offline integration cycles |

---

## 4. REE-specific hypothesis

REE may need to distinguish at least three forms of replay/re-exposure:

1. **Observation replay** — a trace is reactivated but does not write durable change.
2. **Integration replay** — a trace is contextualised or compressed but does not alter commitment authority.
3. **Eligibility-window replay** — the trace is reactivated within a timing/state window that permits durable change in future trajectory selection.

This could matter especially for residue. A harmful committed event should generate residue immediately, but the later meaning, contextualisation, and future action-landscape deformation may need time-gated integration rather than unrestricted rewriting.

Speculative computational primitive:

```text
trace_eligibility = f(time_since_event, offline_phase, arousal_state, prediction_error, residue_status, sleep_cycle_state)
```

Replay should be able to inspect a trace outside the window, but only write durable consolidation when eligibility is open.

---

## 5. Important cautions

Do not overgeneralise from Aplysia to human learning schedules.

Do not encode a literal universal 24-hour rule into REE.

Do not use this to justify simplistic productivity advice.

Do not make this a REE-v3 implementation target without first checking existing sleep/offline/plasticity claims.

The useful extraction is:

> repeated exposure may only become durable learning when the receiving substrate is in a write-eligible temporal state.

---

## 6. External anchors

Secondary article checked during intake:

- Neuroscience News, "Perfect Timing for Memory Identified". Reports a Journal of Neuroscience paper and states that a second exposure at 24 h enhanced learning-related cellular mechanisms, while shorter and longer intervals did not. https://neurosciencenews.com/24-hour-learning-interval-memory-30420/

Original research identified from the secondary article:

- Rong-Yu Liu, Yili Zhang, Roberta Calvo, Paul Smolen, and John H. Byrne. "The Right Time for a Synapse to Change: Windows and Mechanisms of Multiday Training Trials." Journal of Neuroscience. DOI: 10.1523/JNEUROSCI.1981-25.2026

Primary source still needs direct verification before claim extraction.

---

## 7. Proposed next extraction

If the primary source is verified, consider linking this to an offline-integration or plasticity-window architecture note rather than creating a new standalone subsystem immediately.

Possible future note:

```text
docs/architecture/offline_integration_eligibility_windows.md
```

Questions for that note:

- Does REE already represent replay eligibility separately from replay occurrence?
- Should offline integration have phase/state-dependent write authority?
- Can residue contextualisation be temporally gated without allowing replay to create residue?
- Should repeated exposure have different effects depending on time since last committed event?
- Is there a safe REE-v3 diagnostic for distinguishing replay activation from replay consolidation?

---

## 8. Guardrail for future agents

If a future agent tries to convert this into a literal 24-hour scheduler or human-study-timing rule, stop and reframe.

The correct near-term extraction is:

> model consolidation eligibility as state-and-time gated write authority.

The incorrect extraction is:

> add a fixed 24-hour learning interval rule to REE-v3.
