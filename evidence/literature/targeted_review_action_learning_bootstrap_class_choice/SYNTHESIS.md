# Class-choice synthesis — MECH-457 action-learning floor→competent gap

**Generated:** 2026-07-14T17:51:03Z
**Commissioned by:** `failure_autopsy_MECH-457-fanout-751-750_2026-07-14` (user reroute to lit-pull-first)
**Question:** V3-EXQ-751 settled the *algorithm axis* — a learned unsupervised novelty signal (RND) clears the 1.0 forage floor with no expert (5.22); ICM does not; an expert teacher is NOT necessary. But RND plateaus far below the BC expert (32.72) and the observability ceiling (48.05). **Which mechanism CLASS closes the floor→competent gap** — and does it compose with, rather than duplicate, REE's landed exploration substrate (ARC-065 structured curiosity, MECH-314, MECH-313, MECH-455, hippocampal `backward_credit_sweep`)?

12 entries across 5 classes. Metadata verified against arXiv / Nature / PubMed / JMLR / ICLR proceedings.

---

## The load-bearing finding: "more novelty" is refuted

The novelty-drive class (RND, count-based, info-gain, empowerment) buys **state coverage, not task competence.** This is one-directional across the literature:

- RND clears sparse-reward tasks **only where the environment aligns novelty with reward by construction** (Burda 2018 RND — Montezuma's new-room = progress). A sparse-pellet forager only weakly satisfies this, so **clear-the-floor-then-plateau is the textbook-predicted shape**, not an under-tuned bonus (REE: 0.2→5.22, stuck at ~16% of BC).
- The failure modes are intrinsic to the class, not fixable by scaling: **noisy-TV** (reward-agnostic coverage sinks into stochasticity — Burda 2018 Large-Scale; explains why REE's ICM arm failed at 0.22) and **detachment/derailment** (bonus consumed near start, frontier abandoned — Ecoffet 2021).
- RND ≈ a smooth pseudo-count: it is the **same class REE already owns** (ARC-065/MECH-314). Adding another member is composition-vs-duplication ≈ **duplication.**

**This validates the reroute.** The autopsy's original `create mech457_unsupervised_novelty_explorer` recommendation would have built more of a class that is expected to plateau and that REE already has.

---

## Class-choice matrix

| Class | Closes floor→competent? | Distinct from REE novelty substrate? | Buildability (small V3) | Verdict |
|---|---|---|---|---|
| **Novelty-drive** (RND/counts/EFE/empowerment) | **No** — coverage not competence; plateaus | **No — duplicates ARC-065/MECH-314** | trivial (already owned) | **Reject as the build** |
| **Memory: reverse-replay credit** (Foster&Wilson, Mattar&Daw) | Yes — efficient credit assignment | **Extends REE's existing `backward_credit_sweep`** | **cheap — wire+prioritise existing sweep** | **Top pick (highest composition)** |
| **Memory: Go-Explore archive/return** (Ecoffet 2021) | **Yes — directly fixes detachment** (>43k vs RND ~11k) | Yes — orthogonal (frontier-selection, not a reward) | moderate — archive + return (cheap in a gridworld) | **Top pick (one new subsystem)** |
| **Curriculum / goal-generation** (AMIGo, IMGEP) | **Yes — unsupervised analogue of BC**; solves MiniGrid where RND stalls | Yes — competence-directed (learning-progress ≠ novelty) | moderate — goal-proposer + goal-conditioned policy; needs goal-space | **Strong standalone** |
| **Explore/exploit mode** (Aston-Jones&Cohen, Daw) | Plausibly — via bidirectional consolidation | Yes — a meta-controller *over* exploration | **cheap — critic-utility-gated temperature scalar** | **Cheap composable adjunct** |
| **Options / skills** (Sutton'99, DIAYN, Jin&Costa) | Yes in principle (temporal abstraction) | Yes | **DIAYN heavyweight; ill-fit to small substrate** | Deprioritise (lightweight options probe only) |

---

## Recommendation (for the user; governance/queue applies)

**The gap has two sub-problems RND does not solve** — (i) reliably getting *back* to discovered reward (detachment / frontier), and (ii) *propagating credit* once reward is found. The two highest-composition, lowest-duplication moves address these using machinery REE largely already has:

1. **Extend the existing hippocampal `backward_credit_sweep`** (Foster&Wilson grounds it; Mattar&Daw supplies the priority rule): ensure it fires on the forage-reward trajectory and prioritise its updates by utility/TD-error. **Cheapest, highest-leverage, reuses landed substrate.** `complicated (buildable)`.
2. **Add a Go-Explore-style archive + return** (Ecoffet): the one genuinely new subsystem worth building, orthogonal-and-additive to the sweep, directly targeting the detachment that makes RND plateau. Cheap in a small gridworld.

**The strongest *standalone* competence-manufacturer** is the **curriculum / goal-generation** class (AMIGo) — the unsupervised analogue of what BC achieved — but it is a bigger new subsystem (goal-proposer + goal-conditioned policy) and needs a parameterizable goal space.

**Explore/exploit mode** is a cheap composable adjunct (consolidation-into-exploitation) worth folding in, not a standalone build. **Options/skills** is deprioritised — DIAYN is heaviest and worst-fitting to a small substrate.

### Two routing options
- **(A) Single highest-leverage build + test:** extend the `backward_credit_sweep` (reuses landed substrate) as the first move; escalate to Go-Explore archive/return, then curriculum, as ranked fallbacks. Matches the re-derive-brake spirit — build the cheap composable thing that reuses what exists before minting new subsystems.
- **(B) GOV-FANOUT-1 discrimination portfolio:** since ≥2 live classes plausibly close the gap, queue a small diverse portfolio — one probe per class on a different design axis (credit-extension / archive-return / goal-curriculum / mode-gate), each with a declared null — and let the winner decide the substrate. Avoids committing to the wrong class on the narrow 751 reading.

**Note on INV-088:** whichever class is built must reach *matched-competent unsupervised* policies on **both** z_world and raw 5×5 view before V3-EXQ-750's representation→diversity readout can be re-run (751 ran z_world explorer arms only).
