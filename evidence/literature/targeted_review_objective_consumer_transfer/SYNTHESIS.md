# Targeted review: objective -> consumer transfer

**Question.** What makes a representation-learning objective's gains reach a downstream action consumer?

**Why it was pulled.** `failure_autopsy_V3-EXQ-1023a_2026-09-17` (confirmed, ratified REE_assembly
`eeeb0550ed5`) scored SD-106's **biological reference layer ABSENT** while diagnosing the dominant
layer as *integration -- partially coupled*. 3.3x the P0a optimiser budget moved held-out
preservation R^2 **+0.1184** (0.7318 -> 0.8501, still rising) and consumer oracle-action agreement
**+0.0081** against a 0.1227 shortfall: an observed transfer slope of 0.068 agreement per unit R^2
against a PCA-anchored 3.4655, a **~50x** shortfall. Run as the mandatory biology precondition of
CDQ-010's Mine+Register step (CLAUDE.md *biology before formal definitions*).

**Scope boundary -- read this before extending.** This pull is about **transfer**: the relation
between an encoder objective and a consumer. It is deliberately **not** the *generic-vs-task-relevant
compression* pull, which is separately owned by the open chip
`chip-20260916-sd106-compression-litpull` and which `failure_autopsy_V3-EXQ-1023a` routes as its
PRIMARY with an explicit instruction not to spawn a second. The two are complementary: that pull asks
*what should be compressed*; this one asks *what makes any of it arrive*.

## What the five entries establish

| # | Entry | Direction | What it carries |
|---|---|---|---|
| 1 | Semedo 2019, communication subspace | supports | Downstream reads a **low-dimensional subspace distinct from the sender's dominant fluctuations**. Preserved variance is not automatically transferred variance. |
| 2 | Kaufman 2014, output-null subspace | supports | Large upstream variance can be **provably unreadable** by the consumer. Alignment, not magnitude, is what the consumer responds to. |
| 3 | Rumyantsev 2020, fidelity bounds | supports | **Information present and information used differ by a large factor** in biology. The 1023a signature is an ordinary sender-consumer shape, not a failed objective. |
| 4 | David 2012, task reward shapes RFs | supports | Biology routes the **task's reward structure into the encoder**; it does not rely on task-agnostic preservation. |
| 5 | Poort 2015, learning reshapes V1 | **mixed** | Task shaping works **and entangles**. The counterweight: `z_world` is a shared latent, so task-shaping has a price. |

## The three things this pull settles, and the one it does not

**Settles 1 -- the autopsy's reframe is biologically ordinary.** Entry 3 makes "trained hard, did not
transfer" a normal measured shape rather than an anomaly. This retrospectively supports the autopsy's
correction from *the lever is exhausted* to **the lever is not connected**.

**Settles 2 -- the deliverable had to be a MECHANISM, not another locus.** Entries 1 and 2 both
describe an interface at which adequate content fails to arrive. The frozen registry question
`zworld_actor_adequacy_locus` carries 11 legs, four confirmed, and **every one names a LOCUS at which
adequacy is lost**. None describes a transfer failure between an adequate objective and its consumer.
That shape mismatch is what the same-day GOV-HOTHER-1 `rotation` event flagged.

**Settles 3 -- alignment beats magnitude.** Entries 1 and 2 jointly ground MECH-566: the quantity a
consumer responds to is the alignment of upstream variance with its readout, not the total.

**Does NOT settle -- which of the three registered mechanisms is right.** Entry 3's own leading account
is a *sender-side* ceiling (information-limiting correlations), not a consumer-side one. Entries 1 and 2
describe hard geometric constraints, whereas REE's consumer is a *trained* MLP whose null space is soft.
Entry 4 measures encoder change but never consumer competence. **No entry discriminates MECH-566 from
MECH-567 from MECH-568** -- that discrimination is REE-side work, and each claim carries its own
falsifier for it.

## The one place the biology bounds a tempting over-read

The strongest reading of entry 1 -- *dominant-variance directions are never what transfers* -- is
**not supported, and is directly embarrassed by REE's own anchor**: PCA-32 keeps exactly the top-32
principal directions and clears the consumer bar 3/3 (0.8771 / 0.8578 / 0.8702). So the licensed claim
is the weaker one: *preserved variance is not automatically transferred variance*. What separates two
codes **at matched preserved variance** is their geometry, which is MECH-566's question and no
entry here answers it.

## Registered from this pull

`MECH-566`, `MECH-567`, `MECH-568` -- all `candidate` / `implementation_phase: v3` / `v3_pending`,
each with an explicit `what_would_answer`, all wired into `SD-106.depends_on`. Architecture stub:
`docs/architecture/objective_consumer_transfer_mechanisms.md`.
