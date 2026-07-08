# Global Workspace + J-lens: design note

Owner claim: **SD-064** (REE instantiates a global-workspace-like access channel).
Related: SD-027 (selection gate, reframed), MECH-254 (top-k impl), MECH-089
(packaging), MECH-287 (broadcast queue), SD-037 (broadcast override),
MECH-007 (attention fragmentation), MECH-191 (cross-architecture signal legibility).
Registered: 2026-07-08. Status: candidate / v3_pending. **PROMOTES NOTHING.**

---

## 0. Why this doc exists

Anthropic's J-space / Jacobian-lens result (2026,
<https://www.anthropic.com/research/global-workspace>) found that a large,
capable model — under **no** design pressure to have one — spontaneously grew a
compact internal structure that behaves like a Global Workspace: a **few dozen
concepts at a time, < 10% of internal activity**, that is (a) **reportable**,
(b) **causally load-bearing for multi-step reasoning** (ablate it and multi-step
reasoning collapses to ~0 while fluency / sentiment / MCQ survive), and (c)
**bypassed by automatic processing**.

That is convergent evidence that a *capacity-limited, reportable,
integration-central broadcast channel* is an **attractor** for capable sequence
models. REE builds one on purpose (on biological grounds); Claude grew one. This
note banks the insight as a claim and lays out the two experiments that would
turn it from convergent analogy into REE-internal evidence.

Two framing points, kept honest throughout:

- **Access, not phenomenal.** Anthropic explicitly claim *access*-consciousness
  (Block's sense: globally available for report and control), **not** phenomenal
  consciousness. SD-064 makes the same access-functional claim only.
- **The J-lens is imperfect.** It captures single-token concepts, the entry
  mechanism is unknown, and the workspace they measured evolves over a single
  forward pass. REE's analogue is **recurrent / temporally extended** — arguably
  *closer* to Baars' actual (temporal) theatre than Claude's frozen snapshot.

---

## 1. The claim, and the hedge it retires

SD-027 established a capacity-limited **selection-for-broadcast gate** at the
E1/E2 → E3 boundary (pulvinar–TRN analogue), feeding MECH-089 theta-gamma
packaging, feeding E3. Its note said REE is *"distinct from global workspace
theory in that SD-027 does NOT commit to a single global workspace."*

**That hedge conflates two different things.** It reads GWT as requiring a
*unitary selector* — which MECH-007 ("attention must be fragmented across
control axes") rightly forbids. But GWT requires no unitary attender:

> GWT's backstage is a **fragmented population of specialists**; the workspace
> is a narrow **broadcast bus** over them, not a homunculus. A capacity-limited
> bus that fragmented processors write-compete into and read-broadcast from is
> *fully consistent with* MECH-007.

So REE does not merely *tolerate* a global workspace. Its
**selection (SD-027) + packaging (MECH-089) + broadcast (MECH-287 / SD-037)**
stack already *is* one, at the access-functional level. SD-064 owns that
commitment. SD-027 stays valid as the selection stage; MECH-007 is reconciled,
not violated.

### Explanatory pairing worth keeping in view
The psychosis / thought-broadcasting substrate claim (self-attribution
contamination) is the **same channel read from the opposite end**: SD-064 says
workspace content is *legible-for-broadcast to the system*; the psychosis claim
models an agent experiencing its *own* workspace content as *externally
attributed / broadcast*. A single mechanism, two readings — a nice internal
consistency check for both claims.

---

## 2. Experiment A — REE-native J-lens dispositional readout (RUNNABLE NOW)

**Question:** Does REE have a J-space? I.e. is there a **compact, reportable,
action-coupled** subspace of the latent state that (a) occupies a small fraction
of total activity and (b) is causally central to committed/integrative action —
the REE analogue of Anthropic's finding?

**Why runnable now:** this is a *post-hoc readout* over an existing trained
all-ON agent. It needs **no new substrate** — no SD-027 gate, no config flag. It
is a measurement, not a mechanism change. That makes it a clean **diagnostic**
(non_contributory, PROMOTES NOTHING).

**The REE J-lens — the port of Anthropic's method.** Their lens asks, per output
token: *what internal activation is this disposed to make the model emit later?*
REE has an explicit **action head**, so the natural port is:

> For each committed action class `c`, find the latent-state direction most
> **dispositionally predictive of committing `c` some horizon `H` later**.

Concretely, over a logged all-ON rollout (per-tick latent state `z_t` — the
E1/E2/E3 stack — and executed committed_class `c_{t+H}`):

1. Fit a linear dispositional map `J: z_t -> P(committed_class_{t+H})` (multinomial /
   ridge), for a small horizon set `H ∈ {1, 3, 5}`. `J`'s row space is the
   **REE J-space** — the directions in latent state that "vote" for future
   committed action.
2. **Compactness (the < 10% test):** what fraction of `z`-activity variance lies
   in the J-space (top-k singular directions of `J` capturing ≥ 90% of its
   action-predictive power)? Report `jspace_dim` and
   `jspace_activity_fraction`. Anthropic: few dozen dims, < 10%.
3. **Reportability proxy:** REE has no natural-language report head, so use the
   **broadcast substrate as the report analogue** — is J-space content
   preferentially what MECH-287 broadcasts / what SD-037 override reweights?
   Correlate per-tick J-space occupancy with broadcast-event emission.
4. **Automatic-bypass contrast:** does a *reactive* DV (single-step obstacle
   avoidance / immediate reward capture) load on the J-space, or is it
   J-space-independent? GWT predicts reactive behaviour bypasses the workspace.

**DVs:** `jspace_dim`, `jspace_activity_fraction`,
`action_pred_auc@H` (J-space vs full-state vs shuffled-null),
`broadcast_jspace_alignment`, `reactive_dv_jspace_dependence`.

**Readiness gate (self-route, never a verdict):** need ≥ N committed-action
transitions per class per seed for the map to be estimable (mirror the
V3-EXQ-719a MI-estimability floor pattern); else
`substrate_not_ready_requeue`. Shuffle-null (≥ 200x) + p95 for the AUC.

**Reading:**
- Compact + broadcast-aligned + reactive-independent → **positive J-space
  existence**; raises the SD-064 prior and *motivates the SD-027 V3 gate
  retrofit* that unlocks Experiment B.
- Diffuse / no compact action-coupled subspace → evidence *against* a single
  workspace, *for* the SD-027-original pluralist reading. Either way it is
  informative and cheap.

**Feeds MECH-191** (cross-architecture signal legibility, currently
substrate-blocked because functional channels are tonic): the dispositional
readout is exactly a *legibility instrument* — "which latent states are
dispositionally coupled to future committed action" is a legibility map REE
lacked. A working REE J-lens is a candidate unblock for MECH-191's tonic-channel
problem: it reads disposition-toward-output rather than instantaneous channel
value.

---

## 3. Experiment B — workspace-ablation cliff (SUBSTRATE-BLOCKED)

**Question:** Is the selection-for-broadcast channel a *genuine workspace* — i.e.
does ablating it produce a **cliff** (integrative/multi-step cognition → ~0,
reactive/automatic behaviour intact) rather than **graceful degradation**?

This is the sharpest test and the direct port of Anthropic's ablation result. It
is also the discriminator between SD-064 (cliff) and the SD-027-original
pluralist reading (graceful degradation via redundant distributed pathways).
MECH-254 already sketches the factorial: `{gate off, gate only, template only,
both on}`.

**Why blocked:** the SD-027 boundary gate is **not implemented in V3**. There is
no `sd027` / access-gate code in `ree-v3/ree_core`; SD-027 is v4-scoped with an
*optional* fixed-k top-k retrofit that was never built ("Not queuing an EXQ yet",
SD-027 evidence_quality_note). A gate-ablation experiment today would self-route
`substrate_not_ready` — the "642 trap" (a substrate-ceiling verdict self-routed
on an unbuilt substrate). **Do not queue it yet.**

**Prerequisite (the unblock):** an `/implement-substrate` build of the SD-027 /
MECH-254 **V3 top-k selection gate** — a `use_boundary_access_gate` flag
(no-op-default, byte-identical OFF) over the E1/E2 → E3 forwarding path, top-k
over active `z_world`/`z_self` components per heartbeat, with a hard ablation
mode (k → all, i.e. gate disabled) for the factorial. Once built + smoke-tested,
Experiment B becomes: run the MECH-254 four-cell factorial in a task that
*requires* multi-step committed-action integration (the conversion-ceiling /
committed-action-diversity surface is the natural fit — that DV is already the
one that has been ceiling-bound), DV = integrative competence + committed-action
diversity, and test for a **cliff vs graceful** ablation profile.

**Recommended sequencing:** run **A** first. A positive J-space result is the
evidence that justifies spending the retrofit build on **B**; a negative result
saves the build.

---

## 4. Caveats carried on SD-064

- **Access ≠ phenomenal.** SD-064 is access-functional only. No claim about
  experience.
- **Convergence ≠ confirmation.** The Anthropic result raises a prior; it is not
  REE evidence. Only Experiments A/B are.
- **REE is recurrent; Claude's J-space was single-pass.** This is a *divergence
  that favours REE* for the GWT analogy (temporal broadcast is the actual
  theatre), but it also means the readout must be computed *across* heartbeats,
  not within one forward pass.
- **Legibility is dual-use.** The eval-awareness / hidden-goal findings in the
  Anthropic work (suppressing "fake"/"fictional" patterns restored a
  previously-resisted harmful behaviour) are a reminder that a working REE J-lens
  is also a safety instrument relevant to the SENT-*/GOV-* ethics perimeter — a
  workspace legible to an interpreter is legible to an auditor.

---

## 5. Status ledger

| Item | State | Next |
|------|-------|------|
| SD-064 registered | done (candidate, v3_pending) | — |
| SD-027 cross-ref | done (non-destructive reframe note) | — |
| Experiment A (J-lens readout) | queued via /queue-experiment | needs a runner |
| Experiment B (ablation cliff) | design-only, substrate-blocked | needs SD-027 V3 gate retrofit (/implement-substrate) THEN queue; gate on A positive |
| MECH-191 unblock | hypothesised | confirm if A's dispositional readout resolves the tonic-channel legibility gap |
