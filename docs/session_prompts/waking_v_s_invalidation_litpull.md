# Waking-Phase Online V_s Invalidation Literature Pull

> Created: 2026-04-22
> Origin: V3-EXQ-475 result -- SD-036 GABA decay + MECH-279 PAG freeze gate are
> both firing (5-6 freeze releases per seed across eval), but the agent re-commits
> ~12x per release and stays in freeze for 1000/1000 eval steps. The endogenous
> driver is the hippocampal proposer pulling trajectories from the original
> avoid-anchor; SD-036 decay can't break the cycle without an upstream anchor
> invalidation signal. MECH-284 (V_s residual schema staleness accumulator) and
> MECH-269 anchor-reset criteria were registered to fill exactly this gap but are
> still v3_pending.

## Prompt

/lit-pull Online (waking-phase) signals that invalidate, downweight, or replace a
schema / cognitive map / hippocampal place-cell anchor when the world departs from
what the schema predicts -- specifically the question of what tells the brain that
an existing anchor is *no longer the right anchor*. The architectural question is
narrow: V_s (regional verisimilitude) currently updates only via offline replay
(MECH-285 sleep priority); we need the waking-phase counterpart that lets V_s drop
online when the agent is repeatedly surprised by mismatches between the anchored
schema's predictions and observed outcomes. This is distinct from (a) replay
*content* (Pfeiffer & Foster 2013 already established that sequences start at
current location and progress to goal -- see targeted_review_connectome_mech_269/),
(b) episode encoding for later replay, and (c) extinction learning of stimulus-outcome
associations. The target is the *invalidation signal itself* -- what computational or
neurobiological signal triggers an online schema downweight.

Target claims to inform / extend:

- **MECH-284** (V_s residual schema staleness accumulator -- runtime reverse readout
  of V_s; currently registered v3_pending without operational definition of the
  staleness signal)
- **MECH-269** (anchor selection by regional verisimilitude; the architecture has
  reset criteria sketched in `hippocampal_anchor_selection.md` "Anchor reset criteria"
  but no biological grounding for the runtime signals)
- **MECH-272** (state-gated routing -- waking is anchor-dominant; the lit-pull may
  refine this to "anchor-dominant *until invalidation threshold crossed*, then probe-
  dominant for a transient re-anchoring window")
- Possibly new MECH for the online invalidation signal itself (parallel to MECH-285
  for offline replay priority)

## Specific neurobiological systems to cover

1. **Dopamine prediction error as invalidation signal (Schultz lineage)**
   - Schultz, Dayan & Montague 1997; Schultz 1998/2016 reviews
   - Specifically: phasic dips on omission as candidate for "anchor invalid here"
   - Recent: dopamine RPE in the dorsomedial striatum vs ventral striatum -- model-
     based vs model-free distinction (Daw & Tobler 2014)

2. **Lateral habenula / negative reward prediction error**
   - Matsumoto & Hikosaka 2007 (LHb encodes negative RPE)
   - Bromberg-Martin & Hikosaka 2011 (LHb in prediction failure / disappointment)
   - Whether LHb signal could function as a broadcast invalidation signal vs being
     locally restricted to RPE pathways

3. **OFC as state representation / cognitive map and inferred-state updating**
   - Wilson et al 2014 (OFC encodes state in a partially observable task)
   - Stalnaker, Cooch & Schoenbaum 2015 (OFC and Pavlovian outcome inference)
   - Gardner, Schoenbaum & Gershman 2018 (OFC and inferred outcomes; latent state)
   - The candidate: OFC representational change *during waking* as the substrate
     for online anchor invalidation, parallel to hippocampal replay during sleep

4. **Hippocampal pattern separation under high interference**
   - Yassa & Stark 2011 (DG/CA3 pattern separation)
   - Reagh & Yassa 2014 (mnemonic similarity / lure discrimination as proxy for
     schema interference signal)
   - Whether DG remap rate could function as an upstream signal that "the current
     anchor is being interfered with"

5. **Latent cause / latent state inference (computational frame)**
   - Gershman & Niv 2010, Gershman 2017 (latent state inference; structure learning)
   - Specifically: Gershman, Blei & Niv 2010 (extinction as inference of new latent
     cause, not erasure of old) -- direct architectural model for "invalidate the
     current schema by inferring a new latent cause"
   - Niv 2019 review on learning task representations

6. **Extinction and reconsolidation literature, narrowly framed**
   - Bouton 2004 (extinction as new learning) -- baseline
   - Quirk & Mueller 2008 (vmPFC and extinction); Milad & Quirk 2002 (IL cortex)
   - Reconsolidation literature (Nader et al 2000) only insofar as it speaks to
     online schema *updating* under reactivation -- not the labile-window mechanics

7. **Locus coeruleus / norepinephrine as global novelty / surprise signal**
   - Aston-Jones & Cohen 2005 adaptive gain theory
   - Sara & Bouret 2012 (LC and orienting/reset response)
   - Whether LC phasic burst on prediction failure could function as an
     "invalidate current attentional/anchoring frame" broadcast signal -- candidate
     biological substrate for MECH-284 staleness accumulator's *trigger event*

## Architectural questions the lit-pull should help answer

1. **Local vs broadcast.** Is the invalidation signal local to the affected schema
   (e.g. OFC representational change for the specific state) or a broadcast reset
   signal (e.g. LC norepinephrine burst, LHb negative-RPE)? The architectural
   reading needs both: a broadcast trigger (MECH-284 *event*) plus a local
   accumulator (MECH-284 *state*). The lit-pull should clarify which biology
   provides which role.

2. **Single failure vs accumulation.** Does a single prediction failure suffice to
   invalidate an anchor, or does the biology accumulate failures over a window
   before triggering reset? Clinical phenomenology (perseveration; the difficulty
   of changing one's mind despite repeated counter-evidence) suggests
   accumulation; but acute orienting responses to single salient violations
   suggest single-event capability. The architectural reading currently expects
   accumulation (consistent with MECH-284 as an *accumulator*) but the lit-pull
   should test this.

3. **Proportional vs threshold.** Does invalidation produce a graded V_s
   downweight proportional to the failure magnitude, or does it cross a
   threshold and trigger discrete re-anchoring? Both have biological precedent;
   the architectural commitment matters because graded downweight is compatible
   with continuous mode arbitration while threshold re-anchoring requires a
   discrete "transition out of anchored state" event (which MECH-272 currently
   does not specify).

4. **Coupling to replay priority (MECH-285).** When a waking-phase invalidation
   fires, is the affected schema flagged for *that night's* replay priority, or
   is the runtime invalidation independent of the offline reverse readout? The
   former predicts a sleep-pressure signal that scales with daytime invalidation
   load; the latter predicts independence. Clinical observation: high-distress /
   high-mismatch days produce both intrusive next-day cognition AND elevated REM%
   (or fragmented sleep), consistent with coupling -- but the lit-pull should
   surface this directly.

5. **Failure modes.** Where in the biology can the invalidation signal *fail*?
   - LC dysfunction: would predict perseveration / inability to shift away from
     a stale schema (clinical: ASD restricted-interest patterns? OCD?)
   - LHb dysfunction: would predict failure to register negative outcomes
     (clinical: depression's blunted RPE; or alternatively, hyperactive LHb in
     learned helplessness as *over*-invalidation of agency-anchors)
   - OFC lesion: would predict inability to update inferred state (Bechara,
     Damasio gambling task; or anchor-locked behaviour as in catatonia subtype II)
   - Failure in the accumulator integration step: would predict V3-EXQ-475's
     phenotype directly -- repeated brief releases from freeze (single events
     register) but no durable invalidation (accumulator never crosses threshold).

## Output structure

Standard `targeted_review_*/` format. Suggested directory:
`evidence/literature/targeted_review_waking_v_s_invalidation/`

Per-paper records as usual. After the pull, write a short SYNTHESIS.md flagging:
- Which architectural question(s) each paper addresses
- The current best candidate biological substrate for the broadcast invalidation
  *trigger* (LC vs LHb vs OFC vs DA dip)
- The current best candidate substrate for the local *accumulator* (OFC
  representational change vs hippocampal DG remap vs latent-cause inference in
  vmPFC)
- Which of the five questions remain underdetermined and need additional pulls
- Whether the evidence supports registering a new MECH for the online
  invalidation event (separate from MECH-284 the accumulator), and if so, draft
  proposed claim text

Estimated scope: ~10-15 papers, single session.

## Notes for the agent doing the pull

- The user is a consultant psychiatrist; clinical mappings (perseveration, OCD,
  depression's blunted RPE, ASD restricted interests, learned helplessness as
  over-invalidation) are valuable framings.
- Pfeiffer & Foster 2013 and Dragoi & Tonegawa 2011/2013 are already pulled in
  `targeted_review_connectome_mech_269/` -- do not re-pull; cite where relevant.
- The exemplar that motivated this pull is V3-EXQ-475 (re-run of EXQ-471 with
  SD-036 enabled): freeze releases occurred but re-commits dominated, indicating
  the agent has SD-036 decay and MECH-279 freeze exit but no online anchor
  invalidation signal driving the hippocampal proposer to remap.
- Connect to existing REE memory entries on regional verisimilitude (MECH-269),
  V_s bidirectional signal (MECH-283/284/285), and state-gated routing (MECH-272).
  The hypothesised online invalidation mechanism is a candidate fourth claim in
  the V_s cluster -- a runtime *trigger* whose accumulator is MECH-284.
- Be alert to evidence that the invalidation signal is *not* a separable
  mechanism but is instead implicit in the existing replay machinery (e.g. waking
  SWR replays serving the same role as sleep SWR replays). If so, MECH-269
  anchor-reset becomes a re-statement of MECH-285 in waking-state rather than a
  new mechanism -- this would simplify the architecture.
