# Collins & Frank 2013, "Cognitive Control over Learning" (C-TS model) -- MECH-349

## What the paper did

Collins & Frank build a Context-Task-Set (C-TS) model of how learners decide, on encountering a
context, whether an existing "task-set" (a hidden stimulus-response-outcome rule cluster) applies
or whether a genuinely new one must be created. The model is explicitly inspired by nonparametric
Bayesian clustering (a Chinese Restaurant Process / Dirichlet process prior over task-sets), and
is paired with a neurobiologically explicit frontal-cortex/basal-ganglia network model that
approximately implements the same computation, plus human behavioral experiments confirming that
people spontaneously build this kind of structure even when not cued to.

## Findings relevant to MECH-349

The CRP-based create-vs-reuse decision is stated formally: for a new context c_{n+1},
"the probability of creating a new task-set is proportional to alpha, and the probability of
reusing one of the known task-sets is proportional to the popularity of that task-set." Alpha is
explicitly a "clustering parameter," with lower values yielding more reuse and higher values
yielding more creation of new structure -- functionally the same knob role as MECH-349's
crf_mint_recurrence_threshold. Behaviorally, the paper reports that when existing task-sets fail
to explain the current context-action contingency, networks and human subjects were "more likely
to create a new task-set" (Results, C4/C5 test conditions), i.e. creation is triggered by
insufficient coverage of a recurring regularity by existing structure, not by a fixed schedule.

## How this translates to REE

MECH-349 asserts that CandidateRuleField._maybe_mint performs a non-gradient structural CREATE
event -- minting a distinct rule slot when a (context-bucket -> action-object) regularity recurs
above threshold and no existing rule's context_tag already covers it. This is architecturally the
same problem C-TS solves: decide whether the current regularity is already covered by existing
structure, and if not, instantiate new structure rather than trying to force gradient-based
adaptation of what already exists. The paper's framing of this as "the ability to build a new
task-set cluster when needed" as something that "gradient descent cannot supply" (543/598b's own
inert-equilibrium finding, in REE's vocabulary) is essentially the same argument MECH-349's notes
make for why the CandidateRuleField exists as a distinct non-gradient mechanism.

## Limitations and caveats -- why "supports" but a moderate ceiling on confidence

The trigger mechanics diverge in an important way. C-TS's creation decision is a probabilistic
Bayesian draw, re-evaluated online against a maintained posterior over ALL existing task-sets'
fit to the new context (a "popularity" comparison), whereas MECH-349's mint is a deterministic
recurrence-count threshold gated by a hard context-match test and a free-slot precondition -- a
rule-based trigger, not a Bayesian nonparametric one. More importantly, C-TS has no treatment
at all of RETIREMENT -- it never asks whether an existing task-set should be dissolved when its
regularity goes extinct, so the entire churn/selective-retirement half of MECH-349's empirical
content (the crf_maintenance_decay dynamics tested by V3-EXQ-1025, which found selective churn
rather than a treadmill) is simply not addressed by this paper. This is prior art for the CREATE
face specifically, not for MECH-349 as a whole.

## Confidence reasoning

`source_quality` 0.85 (canonical Psych Review model combining formal Bayesian structure, a
network implementation, and human behavioral validation). `mapping_fidelity` 0.55 (the
create-vs-reuse tradeoff is a clean structural match; trigger mechanics and the entire
retirement/churn dimension are not covered). `transfer_risk` 0.45 (human cognitive-control task
switching to an artificial multi-agent substrate's policy module). Aggregate confidence 0.6.

## Bearing on the novel_discovery question (searches run)

Queries run: "Collins Frank 2013 cognitive control task set creation structure learning
frontostriatal"; "Gershman Blei Niv nonparametric Bayesian latent cause learning discovering new
rules recurrence threshold"; direct extraction of the C-TS model-description section via
pdftotext (WebFetch's PDF summarizer returned nothing usable, per the known PDF-fabrication risk
-- verified by re-extracting locally and reading the CRP equations directly rather than trusting
a WebFetch summary). Verdict: MECH-349's CREATE face does NOT survive as a clean novel-discovery
candidate -- "a discrete structural creation event, triggered when existing structure fails to
cover a recurring context-action regularity, that gradient-based learning cannot itself supply"
is exactly the C-TS model's founding move, dating to at least Collins & Frank 2013 and its
Bayesian-nonparametric antecedents (Gershman, Blei & Niv; the Chinese Restaurant Process
literature more broadly). What IS still open and unaddressed in the searched literature is the
SELECTIVE CHURN / retirement dynamics MECH-349 also claims (V3-EXQ-1025's finding that decay-driven
retirement is selective rather than a treadmill) -- no prior-art analog for that half was found in
this search, and a claim restricted to that half would be a stronger novel-discovery candidate
than the CREATE face taken alone.
