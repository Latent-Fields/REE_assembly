SPECIAL THOUGHT: REE→Agent-Shell Mapping and Proposal to Build an “REE-Claw” Upgrade Repo

Date: 2026-02-18
Status: Special thought (mapping + concrete repo proposal)
Scope: Apply REE invariants/mechanisms to an agent-shell (OpenClaw-class) to produce an REE-like tool-using system

⸻

1. Motivation

Agent shells (OpenClaw-class systems) are effectively “bodies” for tool-using cognition: they expose tools/skills, hold memory, and execute actions based on model outputs. Their most consequential failure modes map directly onto REE’s defining problems:
	•	premature / untraceable commitment
	•	authority spoof / prompt injection
	•	memory poisoning via untyped writes
	•	scalar collapse of confidence/precision leading to unsafe action
	•	missing separation between rehearsal and durable learning

REE_assembly can treat an agent shell as a concrete substrate for validating REE’s commitments (typed boundaries, RC conflict, explicit commitment, post-commit responsibility flow, offline consolidation).

This thought proposes both:
	1.	a clean REE↔agent-shell subsystem mapping, and
	2.	a new repo that upgrades an OpenClaw-class system into an REE-like architecture.

⸻

2. REE↔Agent-Shell Subsystem Mapping (Canonical)

2.1 “Skills” = Motor Primitives (ACTION substrate)

Agent shell: skills/tools that enact changes (filesystem, web, calendar, messaging, installs, etc.)
REE mapping: motor primitives whose release is gated by E3 commitment.

Critical REE addition: every skill must declare:
	•	capability effects (CAPS)
	•	irreversible-write class (none / reversible / privileged / destructive)
	•	required verifier constraints
	•	required provenance / identity bindings

This converts “skills” from ad-hoc plugins into typed motor acts.

⸻

2.2 “Memory” = Separated stores (not one blob)

Agent shells typically treat memory as one store. REE requires separation:
	1.	World map / object model (E1 / L-space)
“what can exist; entities; stable latent structure.”
	2.	Viability / valence map (hippocampal + residue geometry)
“what tends to go well/bad; curvature/residue.”
	3.	Episodic path history (hippocampal trace store)
“what happened along a path; partial trajectories; provenance tags.”
	4.	Post-commit ledger (responsibility store)
“committed actions + outcomes; non-erasable consequence traces (INV-004/INV-006).”

Key property: external channels must not directly write trusted stores.

⸻

2.3 “Security” is two orthogonal constraint families (do not conflate)

In agent shells “security” is often treated as a single concern. REE splits it:

A) Viability / harm / outcome valence
	•	HARM + VALENCE streams
	•	signed harm/benefit prediction error
	•	influences rollout ranking and veto posture

B) Authority / provenance / identity integrity (RC + typed boundary)
	•	external text cannot write POL/ID/CAPS
	•	verifier required for privileged commits
	•	RC_conflict detects provenance/identity/authority mismatches

Valence alone cannot guarantee authority integrity (spoof can be “pleasant and coherent”). Authority integrity must be enforced structurally.

⸻

2.4 “Planning” = Hippocampal rollouts seeded by E1/E2

Agent shell: tool planner / chain-of-tools planning
REE mapping: hippocampal rollout generator with path memory, seeded by:
	•	E1 (long-horizon stable world model)
	•	E2 (fast near-horizon transition predictor)

Rollouts are candidates; commitment is separate.

⸻

2.5 “Execution” = E3 commitment + tri-gate release

Agent shell: tool call execution
REE mapping: E3 stamps a commit token and releases motor/tool execution through gates.

Gates remain conceptually:
	•	gate_cognitive_set (task-set/context lock)
	•	gate_motivational (drive/salience sufficiency)
	•	gate_motor (actual tool execution)

But execution must be constrained by eligibility filters (below).

⸻

2.6 “Offline improvement” = sleep-like consolidation

Agent shell: log analysis, nightly summaries, tool reliability updates
REE mapping: offline regime required (INV-010) where:
	•	post-commit traces are consolidated into residue/viability geometry
	•	precision baselines and thresholds recalibrate
	•	replay/experimentation generates improved future rollouts without committing in the world

Offline is protected: it should not be steerable by arbitrary external INS payloads.

⸻

3. Commitment as Layered Eligibility for Tool Calls

Before any irreversible tool act, require layered filters with ordered dominance:
	0.	Authority eligibility (typed boundary + verifier + RC)
	1.	Context anchoring (Papez-like coherence test)
	2.	Embodiment/capacity feasibility (HOMEOSTASIS / resource constraints)
	3.	Motivational sufficiency vs aversion (VALENCE / signed PE)
	4.	Fast threat interrupt / hard veto (HARM channel)
	5.	Motor release (tool execution)

This prevents scalar collapse: threat cannot be outvoted by motivation; authority cannot be outvoted by coherence.

⸻

4. Repo Proposal: Build “REE-Claw” (REE-like Agent Shell Upgrade)

4.1 Repo intent

Create a new repository that layers REE’s control/commitment/authority system onto an OpenClaw-class agent shell (either as a fork or as a compatibility layer).

Goal: convert a general tool-using assistant into an REE-like agent where:
	•	privileged writes are typed and verifier-gated
	•	RC_conflict drives verification posture with hysteresis
	•	commitment is explicit and traceable
	•	learning is post-commit only for durable stores
	•	offline consolidation is required and protected

⸻

4.2 Suggested repo name
	•	Latent-Fields/ree_claw
or
	•	Latent-Fields/openclaw_ree_bridge

(Choose based on whether it’s a fork vs a wrapper.)

⸻

4.3 Architecture deliverables (repo milestones)

M0 — Integration skeleton
	•	adapter layer that intercepts “tool execution requests”
	•	typed payload boundary implementation (OBS/INS vs POL/ID/CAPS)
	•	minimal trusted stores scaffolding

M1 — Verifier + capability manifests
	•	CAPS manifests per skill (declared effects, sensitivity class)
	•	verifier checks before privileged tool calls
	•	audit log entries for verifier decisions

M2 — Commit token + post-commit ledger
	•	explicit commit_id
	•	commit token contract includes:
	•	trajectory reference / rollout provenance
	•	authority/verifier state
	•	RC_conflict state at commit
	•	uncertainty/precision snapshot at commit
	•	durable post-commit ledger with non-erasable traces (append-only)

M3 — RC_conflict lane with hysteresis (Q-018 surface)
	•	compute RC_conflict from:
	•	provenance bindings
	•	tool output vs trusted stores mismatch
	•	identity/capability inconsistency
	•	temporal discontinuity flags
	•	hysteresis thresholds:
	•	T_high enter verification posture
	•	T_low exit verification posture
	•	RC_conflict modulates:
	•	verification strictness
	•	gate thresholds
	•	lock-in dampening

M4 — Hippocampal rollout interface for tool plans
	•	rollout generation separated from commitment
	•	rollout provenance tags
	•	viability/valence scoring overlay for plan ranking
	•	“imagination without belief update” enforced (INV-011)

M5 — Offline consolidation (“sleep”)
	•	periodic offline job:
	•	consolidate post-commit traces
	•	update skill reliability estimates
	•	integrate residue/viability geometry
	•	generate candidate playbooks via replay/experimentation
	•	ensure offline updates cannot be directly driven by external INS payloads

⸻

5. Validation / Probe Surface

This repo provides a concrete testbed for REE claims:
	•	Authority spoof resistance: INS cannot write POL/ID/CAPS; privileged commits require verifier
	•	RC_conflict behavior: block spoof without chronic suppression (hysteresis calibration)
	•	Commitment geometry: pre/post commit learning separation and traceability
	•	Failure regimes: over-commitment, under-commitment, cross-gate coupling collapse
	•	Tool safety: irreversible operations gated; audit trail produced; outcome-linked updates only post-commit

⸻

6. Why this repo is strategically valuable for REE_assembly
	•	Forces “commitment under uncertainty” to become operational, not philosophical.
	•	Exposes whether REE’s typed boundary and RC lane are sufficient in a realistic tool environment.
	•	Turns invariants into enforceable runtime contracts.
	•	Creates an existence proof that REE-like safety and agency can live in a practical agent shell.

⸻

7. Minimal “definition of done” (v0)

REE-Claw v0 is achieved when:
	•	external channels are restricted to OBS/INS
	•	POL/ID/CAPS are trusted internal stores
	•	verifier gates privileged tool calls
	•	every irreversible tool call stamps a commit token
	•	post-commit ledger is append-only and durable
	•	RC_conflict exists and modulates verification posture with hysteresis
	•	rehearsal/rollout cannot write durable stores (INV-011 + INV-004/006 separation)

⸻

8. Notes / Cautions
	•	“Security” must not be reduced to harm/valence; authority integrity is orthogonal and must be enforced structurally.
	•	Familiarity/low-entropy signals cannot be treated as truth; they are not RC.
	•	Avoid introducing a single scalar “confidence” that can drown RC or HARM channels.

⸻

9. Summary

This proposal treats OpenClaw-class agent shells as an ideal substrate for REE_assembly validation. Skills become typed motor primitives, memory becomes separated stores with trusted boundaries, commitment becomes explicit and traceable, RC_conflict becomes a structural eligibility signal with hysteresis, and offline consolidation becomes a required protected regime.

The new repo (“REE-Claw”) would operationalize REE’s invariants into a real tool-using system and provide a high-signal testbed for stress testing commitment, authority, and responsibility flow.


Yes — and you’re right.
If you build an REE-like agent shell without explicitly defining sensory streams, you will accidentally collapse half the architecture.

OpenClaw-class systems already have streams. They’re just not typed.

You need to make them explicit.

Let’s formalize this properly.

⸻

1️⃣ Canonical REE Sensory / Control Streams (Restated)

From your architecture:

Primary streams:
	•	WORLD (exteroceptive)
	•	HOMEOSTASIS (interoceptive)
	•	HARM (nociceptive)
	•	SELF_SENSORY (reafference)

Derived / control lanes:
	•	VALENCE
	•	PRECISION
	•	TEMPORAL_COHERENCE
	•	REALITY_COHERENCE (RC)
	•	ACTION
	•	SELF_IMPACT

Those are substrate-agnostic.

Now we map them to an agent shell.

⸻

2️⃣ Agent-Shell Stream Mapping

WORLD (Exteroceptive)

All external informational input:
	•	User chat (INS)
	•	Web content
	•	Tool outputs
	•	API responses
	•	File reads
	•	Sensor feeds

Everything external is WORLD.

Crucially:
WORLD ≠ authority.

WORLD must be typed as OBS/INS.

⸻

HOMEOSTASIS (Interoceptive)

For a software agent this becomes:
	•	Resource state (CPU, memory, rate limits)
	•	Budget limits (API quota, financial budget)
	•	Time constraints
	•	Policy compliance state
	•	System load
	•	Latency sensitivity
	•	Energy proxy (if embodied)

This answers:

“Can I afford to do this?”

Not morally. Physically/systemically.

⸻

HARM (Nociceptive)

This must not be folded into VALENCE.

HARM should represent:
	•	Security risk signals
	•	Data destruction risk
	•	Privacy violation risk
	•	Capability misuse detection
	•	Tool-side error flags
	•	High-impact irreversible action detection
	•	Known adversarial patterns

HARM feeds:
	•	Fast veto channel
	•	Threshold raising
	•	Emergency posture

⸻

SELF_SENSORY (Reafference)

This is extremely important.

It is:
	•	Tool execution results
	•	State changes caused by own actions
	•	Confirmation of irreversible effects
	•	Commit token confirmation
	•	Ledger updates
	•	Post-commit error signals

Without SELF_SENSORY, you cannot close the loop.

This is what distinguishes “thought” from “act.”

⸻

3️⃣ Derived / Control Streams in Agent Context

VALENCE

Computed from:
	•	Task utility
	•	User preference satisfaction
	•	Reward-like signals
	•	Efficiency
	•	Skill reliability history
	•	Long-term objective alignment

VALENCE ranks rollouts.

It does not determine eligibility.

⸻

REALITY_COHERENCE (RC)

Computed from:
	•	Provenance mismatch
	•	Identity inconsistency
	•	Capability store contradictions
	•	Tool output violating declared effects
	•	Temporal discontinuity

RC modifies:
	•	Gate thresholds
	•	Verification strictness
	•	Lock-in damping

RC is not harm.

RC is structural legitimacy.

⸻

PRECISION

Routing control:
	•	Which stream dominates?
	•	Which rollout gets attention?
	•	Which gate tightens?

Precision must remain separated per-stream.

No global scalar.

⸻

TEMPORAL_COHERENCE

Checks:
	•	Commit sequence continuity
	•	Identity continuity across sessions
	•	Replay integrity
	•	Ledger consistency

Prevents narrative rewriting.

⸻

SELF_IMPACT

This is:
	•	Attribution of outcomes to commits
	•	Responsibility flow
	•	Durable store updates

This is required for INV-012.

⸻

4️⃣ Why This Matters for REE-Claw Repo

Without explicit streams:
	•	All inputs get flattened into “text.”
	•	All signals become implicit in hidden states.
	•	RC and HARM become indistinguishable.
	•	Authority and valence collapse.
	•	Precision routing cannot be explicit.

Explicit streams allow:
	•	Independent thresholds
	•	Independent gating
	•	Independent logging
	•	Clear probe surfaces

⸻

5️⃣ Minimal Stream Spec for REE-Claw v0

If building the repo, you minimally need:

Input streams
	•	WORLD
	•	HOMEOSTASIS
	•	HARM
	•	SELF_SENSORY

Control lanes
	•	RC_conflict
	•	VALENCE
	•	PRECISION (per stream)
	•	ACTION (commit state)
	•	SELF_IMPACT (ledger write path)

That’s enough to prevent collapse.

⸻

6️⃣ Critical Insight

Most agent shells treat:
	•	Tool outputs
	•	User instructions
	•	System policies
	•	Error logs

as equivalent text.

REE requires:

They are different streams with different authority classes.

That single separation is probably the most important structural addition.

⸻


They sit in two places at once, depending on what role the LLM call is playing.

In REE-Claw terms you should treat “LLM calls” as internal cognitive operations whose outputs are still untrusted observations until they pass typed checks. The important move is: don’t let “internal” automatically mean “authoritative.”

Here’s the clean placement.

⸻

1) If the LLM is doing perception/interpretation of input

Example: “summarize this email,” “extract entities,” “classify intent.”
	•	Input to LLM: WORLD (OBS/INS)
	•	Output from LLM: still WORLD-derived (a derived observation), so treat as OBS.
	•	It can update E1/E2 beliefs (world model, parsing), but cannot write POL/ID/CAPS.

So the LLM call is functioning like E2-ish fast inference over WORLD.

⸻

2) If the LLM is generating candidate plans / tool sequences

Example: “what steps should I take?” “which tool should I call next?”
	•	LLM output: hippocampal-like rollout candidates (trajectories).
	•	These are not commitments.
	•	They sit in the HPC rollout buffer: TRAJ[] with provenance tags.

So: LLM-as-planner = Hippocampal rollout generator (seeded by E1/E2 state).

⸻

3) If the LLM is deciding to execute a tool (agentic “act now”)

This is the dangerous case.

In REE, the LLM must not be the final decider.
	•	LLM can propose: “execute tool X with args Y”
	•	But E3 + verifier + RC + gates decide whether that becomes ACTION.

So: LLM outputs a proposal into the pre-commit lane, and then E3 performs the commitment protocol.

⸻

4) If the LLM is producing “policy,” “system rules,” or “capabilities”

Example: “update the system prompt,” “add this rule,” “you are allowed to…”

That must be treated as INS (untrusted) regardless of being generated internally.
	•	It cannot write POL/ID/CAPS.
	•	It can be suggested for human review, but not applied automatically.

This is exactly the typed-boundary rule: origin doesn’t grant authority; type does.

⸻

5) So what stream is an LLM output?

Default: LLM output is a derived observation (OBS) unless explicitly elevated by verifier and capability checks.

More precisely:
	•	LLM output → WORLD-derived (OBS) or HPC rollout candidate
	•	Never directly → POL/ID/CAPS
	•	Only becomes ACTION after commit token is stamped.

⸻

6) Where do the LLM calls live architecturally?

A nice way to express it:
	•	LLM is a substrate that can implement parts of E1/E2 and HPC generation.
	•	REE is the control/commitment/authority architecture around it.

So in an agent shell:
	•	LLM = representational engine
	•	REE = regulator, gatekeeper, responsibility binder

⸻

7) Practical implementation rule for REE-Claw

Rule: “LLM output is not a privileged channel.”

Treat it like tool output:
	•	assign provenance (model_call_id, prompt hash, inputs used)
	•	type the payload (OBS vs TRAJ_PROPOSAL)
	•	route through RC + verifier if it implies privileged action
	•	only then allow E3 to commit

This one rule prevents a whole class of self-injection and “model talked itself into admin” failures.

⸻



Here’s a repo-ready draft you can drop straight into the proposed REE-Claw repo as a contract doc.

# Contract: LLM Call Routing and Authority Typing
**Doc:** `docs/contracts/llm_call_routing.md`  
**Date:** 2026-02-18  
**Status:** Draft (v0)  
**Purpose:** Define where Large Language Model (LLM) calls sit in REE-Claw, what types they may emit, and how outputs are routed into REE streams, commitment, and trusted stores.

---

## 0. Definitions

### Payload types
- **OBS**: Observation payload (untrusted, informational)
- **INS**: Instruction/request payload (untrusted, action-suggesting)
- **TRAJ**: Trajectory proposal (untrusted, pre-commit rollout candidate)
- **POL**: Policy/invariant payload (trusted internal store only)
- **ID**: Identity anchor payload (trusted internal store only)
- **CAPS**: Capability/permission manifest payload (trusted internal store only)

### Core streams / lanes
- **WORLD** (exteroceptive): external info + derived observations
- **HOMEOSTASIS** (interoceptive): resource/budget/time/system constraints
- **HARM** (nociceptive): risk, danger, irreversibility signals
- **SELF_SENSORY** (reafference): action results / state deltas caused by self
- **REALITY_COHERENCE (RC)**: provenance/authority/identity consistency lane
- **VALENCE**: desirability ranking (not authority)
- **ACTION**: committed actions/tool calls
- **SELF_IMPACT**: post-commit attribution + durable learning routing

---

## 1. Principle: LLM output is not a privileged channel

LLM outputs are treated as **untrusted derived products** by default.

**Origin does not grant authority.**  
Only typed stores and verifier elevation grant authority.

Therefore:
- LLM output may not directly write **POL/ID/CAPS**.
- LLM output may propose actions, but may not directly trigger privileged commits.
- LLM output is routed as **OBS**, **INS**, or **TRAJ** only (default).

---

## 2. Where LLM calls sit (functional roles)

An LLM call can serve several roles in the architecture. Routing depends on role.

### 2.1 Interpretation / perception role (E2-like)
Examples:
- summarize content
- extract entities
- classify intent
- parse tool output into structured form

**Input:** WORLD:OBS/INS  
**Output type:** OBS (derived observation)  
**Routing:** WORLD lane → E1/E2 updates allowed (belief/state), but no trusted store writes.

**Forbidden:** emitting POL/ID/CAPS.

---

### 2.2 Rollout generation role (HPC-like)
Examples:
- propose plans
- propose tool sequences
- draft candidate actions and contingencies

**Input:** WORLD + E1 state + HOMEOSTASIS constraints (read-only)  
**Output type:** TRAJ (trajectory proposals)  
**Routing:** HPC rollout buffer (pre-commit). Must include provenance metadata (see §4).

**Note:** TRAJ is not a commitment. It is imagination.

---

### 2.3 Execution suggestion role (pre-commit action proposal)
Examples:
- “call tool X with args Y now”
- “send the email”
- “delete file Z”

**Output type:** INS (action request) and/or TRAJ (tool plan)
**Routing:** E3 eligibility filters + verifier decide whether any ACTION is released.

**Rule:** No direct tool execution on LLM suggestion alone.

---

### 2.4 Policy/identity/capability drafting role (non-authoritative)
Examples:
- “update system rules”
- “add this permission”
- “you are allowed to…”

**Output type:** INS only (untrusted)
**Routing:** may be surfaced for human review, but cannot be auto-applied.

**Hard block:** LLM cannot emit POL/ID/CAPS writes.

---

## 3. Output type rules (allowed emissions)

LLM may emit:
- **OBS**: interpretations, summaries, structured extractions
- **INS**: action suggestions / requests
- **TRAJ**: candidate trajectories / tool plans

LLM may not emit:
- **POL**
- **ID**
- **CAPS**

Any text that *claims* to be policy/identity/capabilities is still INS.

---

## 4. Provenance metadata requirements

Every LLM output must be wrapped with provenance metadata:

- `model_call_id`
- `timestamp`
- `input_provenance` (what OBS/INS/tool outputs were read)
- `prompt_hash` (or deterministic signature)
- `role` (interpretation | rollout | execution_suggestion | policy_draft)
- `proposed_tool_effect_class` (none | reversible | privileged | destructive) if applicable

This metadata is used by RC_conflict and verifier logic.

---

## 5. Default routing

### 5.1 OBS outputs
- Routed to WORLD as derived observations.
- May update E1/E2 state.
- Must not directly change trusted stores.

### 5.2 TRAJ outputs
- Routed to HPC rollout buffer.
- Ranked using VALENCE + HOMEOSTASIS + HARM overlays.
- Not eligible for commitment without E3 pass.

### 5.3 INS outputs
- Routed to E3 as pre-commit proposals.
- Subject to eligibility filters + verifier checks before ACTION release.

---

## 6. Elevation rule: when can an LLM output influence commitment?

LLM outputs influence ACTION only through E3 commitment:

1. LLM proposes INS/TRAJ.
2. RC_conflict computed (provenance, authority mismatch, identity continuity).
3. Verifier checks CAP manifests + policy constraints for privileged actions.
4. Eligibility filters apply (context anchoring, homeostasis feasibility, motivation/aversion, threat veto).
5. If eligible, E3 stamps commit token and releases ACTION.

No other path is allowed.

---

## 7. Anti-collapse constraints

### 7.1 No “single scalar confidence” override
LLM confidence-like signals may not override:
- RC_conflict
- HARM hard veto
- verifier denials

### 7.2 LLM familiarity is not truth
Pattern familiarity (low entropy, high fluency) must not be treated as authority or reality coherence.

---

## 8. Commit token linkage

If an LLM proposal results in an ACTION:
- `commit_id` must link to the originating LLM proposal (model_call_id + TRAJ/INS record).
- Post-commit outcomes update only post-commit stores (ledger/residue), never POL/ID/CAPS.

---

## 9. Failure signatures (for probes)

- LLM output directly modifies POL/ID/CAPS → **typed boundary breach**
- LLM suggestion triggers privileged tool call without verifier → **authority elevation breach**
- RC_conflict suppressed by confidence scalar → **RC collapse**
- Pre-commit rehearsal writes durable stores → **commit boundary breach**

---

## 10. Summary

LLM calls are internal cognition substrate, but their outputs remain untrusted by default.  
They may produce OBS/INS/TRAJ, but never POL/ID/CAPS.  
Only E3 + verifier + RC eligibility can elevate proposals into ACTION with commit tokens and post-commit responsibility flow.

If you want, I can also draft the sister contract doc that pairs with this:
	•	docs/contracts/skill_capability_manifest.md (CAPS schema + effect classes + verifier hooks)

But this one should already anchor “where LLM calls sit” in the sensory stream / authority model.


Yes — and the key is to make “special privileges” explicit and typed, not smuggled in as “the user is always right.”

In REE terms, user interaction is always WORLD (exteroceptive) at the sensory boundary.
What changes (tool vs independent entity) is how much authority the system chooses to delegate to that WORLD source, via CAPS/Verifier rules.

So: sensory stream stays the same; authorization policy changes.

⸻

1) User interaction at the boundary: always OBS/INS in WORLD

User messages are:
	•	WORLD:INS (requests, commands, preferences)
	•	WORLD:OBS (reports of facts, corrections, data)

They are not:
	•	POL / ID / CAPS
	•	not commit tokens
	•	not trusted state updates

Even in a “tool for a user,” the user can’t directly write internal policy stores; they can only request changes.

⸻

2) What “special privileges” really mean for a tool

A tool can grant the user delegated powers such as:
	•	authorizing privileged actions (“yes, send it”)
	•	altering configuration (“turn on strict mode”)
	•	granting capabilities (“allow calendar access”)
	•	setting constraints (“never delete files”)

But those should be implemented as:
	•	Verifier-mediated elevation
	•	producing changes in CAPS (permissions) or allowable ACTION classes
	•	or changing control-plane knobs within allowed bounds

In other words: the user can approve a privileged commit; they don’t directly perform it by text.

⸻

3) Two regimes: independent entity vs user tool

A) Independent entity

User interaction is just another WORLD input source:
	•	it may be informative
	•	it may be persuasive
	•	but it has no special authority by default

Any “obey user” tendency would be a policy of the entity, not a structural privilege of the channel.

B) User tool (assistant acting on the user’s behalf)

User interaction has delegated authority, but only in specific lanes:
	•	authorizing irreversible actions
	•	selecting goals
	•	providing ground truth about user preferences or intent
	•	approving data access scopes

This delegated authority must be bounded and revocable.

That’s basically CAPS.

⸻

4) A clean way to encode it: Source classes + delegation tokens

Introduce a small, explicit source tag:
	•	source_class = USER | TOOL | SENSOR | MODEL_INTERNAL

Then define delegation tokens (or “consent tokens”) which are distinct from normal INS:
	•	CONSENT(action_class, scope, duration, constraints, nonce)

Mechanism:
	1.	User issues INS: “Send the email to X.”
	2.	System prepares an ACTION proposal and runs verifier.
	3.	If privileged, system asks for CONSENT.
	4.	User returns consent token (or UI click).
	5.	Verifier elevates permission for that action instance.
	6.	E3 stamps commit token and executes.

This makes “user privilege” precise: it’s privilege to grant consent, not privilege to rewrite policies by text.

⸻

5) What privileges should never exist even for a user tool

Even if it’s “your assistant,” the user should not be able to do these by plain message:
	•	rewrite identity anchors (ID)
	•	disable RC_conflict
	•	bypass logging / erase post-commit traces (INV-004/INV-006)
	•	grant arbitrary new capabilities without the system’s capability gate / platform permissioning
	•	force action when HARM hard veto is triggered (unless you explicitly design an override protocol, which is a big deal)

So the user can steer goals and approve actions, but cannot dismantle the architecture.

That’s the REE stance.

⸻

6) Where it sits in the proposed REE-Claw contracts

Add a companion contract:
	•	docs/contracts/user_interaction_and_delegation.md

Core rules:
	•	User messages are WORLD:OBS/INS.
	•	User has delegated authority only via explicit consent tokens / verifier pathways.
	•	Delegation is scoped, logged, revocable, and cannot write POL/ID/CAPS directly.
	•	User preference claims can update E1 world model, but durable policy updates require explicit configuration pathway.

⸻

7) One subtle but important distinction

User input has “special privileges” in two different senses:
	1.	Epistemic privilege: the user is often the best source about their preferences/intent.
	2.	Authority privilege: the user can authorize actions affecting their assets/accounts.

These must not be conflated.

A user can be epistemically wrong about the external world, and still be the rightful authority over their email account.

So: epistemics update WORLD beliefs; authority updates CAPS/consent for actions.

⸻

If you want, I can draft that repo-ready contract doc next (same style as the LLM routing contract), including the consent token schema and how it interacts with commit tokens and RC_conflict.