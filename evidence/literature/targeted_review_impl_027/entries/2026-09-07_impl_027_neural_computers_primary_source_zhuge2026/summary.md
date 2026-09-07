# Neural Computers (Zhuge et al., 2026) — the primary source IMPL-027 was written about

## What the paper does

Nineteen authors from Meta AI and KAUST propose *Neural Computers* (NCs): systems that "unify
computation, memory, and I/O of traditional computers in a learned runtime state." The framing is
deliberately architectural rather than incremental — the model is not an agent *acting on* a
computer, it is meant to *be* the computer. The mature form they are aiming at is the *Completely
Neural Computer* (CNC), characterised by "stable execution, explicit reprogramming, and durable
capability reuse."

The empirical content is more modest than the framing. They instantiate NCs as video models that
roll out screen frames from instructions, pixels and user actions, in CLI and GUI settings, trained
purely from collected I/O traces "without instrumented program state." The honest headline of their
own abstract is a split verdict: the models "can acquire elementary interface primitives, especially
I/O alignment and short-horizon control, while routine reuse, controlled updates, and symbolic
stability remain challenging." On arithmetic they report roughly 4% baseline accuracy and note the
models "struggled with symbolic reasoning," suggesting future architectures may need "discrete
memory modules or compositional structures."

## What this confirms in IMPL-027

The load-bearing structural claim of IMPL-027 holds. The four CNC requirements are real, are named,
and are named as the document says: Turing completeness, universal programmability, behavior
consistency, machine-native semantics. The acknowledged prototype failures the document leans on —
no reliable arithmetic, no routine reuse across contexts, no stable long-horizon behaviour, no
controlled update path — are the paper's own admissions, not a hostile reading. And the roadmap item
IMPL-027 makes most of, the call to separate inference from parameter update, is genuinely there.
So the comparison document is not built on a misreading of what the NC programme is asking for.

## What it does not confirm — and this is the part worth acting on

Four defects surfaced, and they are all in IMPL-027's *rendering* of the source rather than in its
architectural argument.

The citation is wrong twice over. IMPL-027 says "Schmidhuber et al. (2025)". The paper was submitted
7 April 2026, and Schmidhuber is the nineteenth and last author; the first author is Mingchen Zhuge.
By any normal convention this is Zhuge et al. (2026). Anchoring the et-al. on the most famous name
in the author list is an understandable slip and a bad one for a positioning document, because it is
exactly the kind of thing a technical reader arriving from the NC literature will notice first.

The provenance is secondary. IMPL-027's References section cites only a semiengineering.com trade
piece. The primary source has an arXiv identifier (2604.06425) and was reachable without difficulty.
For a document whose entire content is a close reading of one paper, carrying only trade-press
coverage is a real weakness — it is the difference between a comparison and a comparison-of-a-summary.

The dataset characterisation flatters the prototypes' supervision. IMPL-027 reports "GUIWorld: 1,510
hours" as screen-recording I/O traces. That total decomposes into about 110 hours of supervised,
goal-oriented trajectories plus about 1,400 hours of *random mouse movement*. The sum is arithmetically
right and rhetorically misleading: the task-relevant GUI supervision is roughly an order of magnitude
smaller than the figure implies. This cuts against IMPL-027's own argument, incidentally — the
prototypes fail on the four requirements with far less goal-directed data than the headline suggests,
which makes the failures weaker evidence for a structural deficit than the document treats them as.

The coverage assertion overstates. Section 2 is presented as answering "each CNC requirement," and
the claims.yaml notes for IMPL-027 assert REE "addresses all four from first principles." It answers
three. Requirement 1, Turing completeness, appears nowhere in section 2 and nowhere in the section 5
translation table. What sits in the fourth slot — section 2.2, "Long-Horizon Stability" — is a
REE-introduced category, not one of the paper's four. This is the kind of substitution that is easy to
make when the source list and the answer list are drafted at different times, and it is the one defect
here with governance consequence: the claim's notes field asserts a coverage that the document does
not deliver.

## Confidence reasoning

I set this at 0.72, direction `mixed`, and the split is the honest shape of it. Source quality is
good but not high — a serious 19-author preprint with released prototypes, unrefereed, and explicitly
programmatic about what CNCs will require. Mapping fidelity at 0.70 records the split verdict directly:
the requirement names and failure modes verify verbatim, the citation metadata and the coverage claim
do not. Transfer risk is 0.35 rather than lower because the standing hazard in a positioning document
is that shared vocabulary reads as shared evidence — "behavior consistency" appearing on both sides of
a translation table is a terminological correspondence, and IMPL-027's section 6 leans on it fairly
hard.

The thing to hold onto: none of this touches whether REE's commitment gating or phase separation are
*correct*. This paper cannot supply evidence for those and was never going to. What it can do is
constrain whether IMPL-027 is an accurate reference note, and on that the verdict is: architecturally
sound, bibliographically wrong in four specific and fixable places.
