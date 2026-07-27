---
title: Public Information Architecture
nav_exclude: true
---

# Public Information Architecture

**Status:** design record and implementation guide

**Scope:** the public REE GitHub Pages site, especially the path from a first
encounter to an inspectable source record.

**Research-status rule:** REE is exploratory research. Nothing on this site is
accepted peer-reviewed work, and an implementation record or an experimental
result is not scientific validation. This rule applies to every presentation
pattern described below.

## Decision

The public site should work as a layered evidence interface, not as a directory
of documents and not as a product demonstration. A reader should be able to
move through four deliberate levels without losing the distinction between
research orientation, recorded work, reviewed evidence, and source material:

```text
Home
  -> Development Map: current frontier and the shape of recorded work
    -> Lab Window: reviewed public claims and evidence
      -> Source record: claim, experiment, architecture document, or Git history
```

Each layer answers a different question:

| Layer | Reader question | Appropriate interface |
| --- | --- | --- |
| Home | What is REE, and what is its research status? | Short thesis, status disclosure, clear routes. |
| Development Map | What is live, recorded, closed, or conditional? | Frontier summary, lane rail, status filters, expandable records. |
| Lab Window | What reviewed evidence is public, and how should I interpret it? | Evidence-oriented tabs, compact summaries, record links. |
| Source record | What exactly was claimed, tested, or changed? | Existing documentation, evidence, and GitHub links. |

The earlier layer must not imply stronger evidence than the later layer can
support. In particular, status colours, counts, and diagrams describe the
state of a record; they do not measure truth, programme completion, safety, or
clinical utility.

## What Has Landed

The Development Map is now the public orientation layer between the landing
page and the detailed record. It is generated from public source records and
contains:

- the current frontier and recorded gate;
- a five-lane programme view with native expandable records;
- explicit active, closed-record, and planned/conditional states;
- direct links from individual records to the Lab Window;
- the Roadmap as the preserved dated operational archive.

The Roadmap now links to the Development Map at its top. The map is intentionally
not a progress bar or a schedule: it represents record states and conditional
future shape without inventing certainty.

## Audit Findings

### 1. Home is strong but omits the current-research route

The home page makes the programme and its exploratory status visible in the
first viewport. Its strongest calls to action currently lead toward a
derivation and the Lab Window. A reader looking for the present state of the
research has to infer that the Lab Window is the right choice.

**Improvement:** give the Development Map a first-viewport route, labelled for
its purpose, alongside the derivation and Lab Window. Keep the research-status
disclosure in the same visual field.

### 2. The Development Map needs a deliberate navigation home

The map is linked from the Roadmap and is directly reachable by URL, but it is
not yet represented in the generated left navigation. That makes the route
easy to miss when a reader arrives through Architecture, Research Status, or a
search result.

**Improvement:** make the Development Map the reader-facing planning entry in
the navigation, and make the Roadmap its clearly named operational archive.
This must be implemented in `docs/apply_nav_frontmatter.py`, then regenerated;
manual frontmatter edits alone will be overwritten by that source of truth.

### 3. The Lab Window has useful detail but a visible freshness gap

The public explorer is a strong read-only evidence surface: it withholds future
work, shows only reviewed material, and makes its scope clear. At this audit
(2026-07-27), its checked-in public index was dated 2026-06-15 and reported one
pending review, while the current repository review record reported 11 pending
items. This is a reader-facing accuracy problem even though the more recent
work is deliberately withheld.

**Improvement:** treat the public export as a reviewed publication artifact.
On every documentation pass, compare its generated timestamp and safe aggregate
counts with the current evidence index. Run the exporter and its safety checks
when a refresh is due, inspect the redaction report, and publish only after the
existing human redaction decision. If publication is deferred, expose the
export's generation date plainly rather than leaving it to look current.

The Lab Window should also receive a compact bridge back to the Development Map:
"For the current public research shape, open the Development Map." It must not
reveal future tests, queues, or unreviewed run identities.

### 4. Visualizations are attractive entry points but need interpretive framing

The Visualizations page has recognisable previews for the Brain Map and
Fishtank, yet a reader must still infer what each view can establish and where
its data came from. The page should be a guided instrument index rather than a
gallery.

**Improvement:** give each visualization a shared instrument profile:

- the specific question it helps inspect;
- what is represented and what is not;
- source/data timestamp and static-versus-live status;
- a direct path to the relevant claims/evidence records;
- a short limitation statement appropriate to the tool.

These should be compact labelled fields, not more explanatory paragraphs or
marketing-style cards.

### 5. Architecture pages remain document-first

The architecture overview is rich but is primarily a long linear explanation.
It should remain a full reference, but readers need a quick structural picture
before entering sections such as E1, E2, E3, memory, harm, commitment, and
governance.

**Improvement:** add a compact clickable system map ahead of the long narrative.
Each component should open or jump to its section and offer links to its public
claim/evidence context. The map must describe computational roles, never imply
anatomical validation.

### 6. Dense operational archives should remain archives

The Roadmap's dated snapshots are valuable provenance, but they are not a good
first reading experience. The solution is not to condense, erase, or rewrite
them. The solution is a clear handoff from reader-facing summaries to the
archive, with dates and source context preserved.

## Interface Rules

1. **Overview before inventory.** Start with a bounded visual summary, then let
   a reader open lanes, records, or source documents.
2. **Use familiar disclosure controls.** Native `details` elements, tabs,
   filters, labelled links, and anchors are preferred to a custom interaction
   framework. A control must retain a stable size and visible selected state.
3. **Represent uncertainty directly.** Use labels such as active,
   provisional, closed record, planned/conditional, weakened, and reviewed.
   Do not collapse them into a green/red success scale.
4. **Make every summary traceable.** A count, state, or diagrammed component
   should lead to an inspectable public record wherever that exposure is safe.
5. **Make the data age visible.** Generated pages show a source date when their
   data are a snapshot. Staleness must not be hidden by a polished interface.
6. **Do not expose protected operational information.** Public Explorer scope,
   redaction review, and withholding of future-stage/unreviewed work remain
   hard constraints.
7. **Retain a persistent research-status cue.** The no-acceptance disclosure
   belongs in the home, public headers/footers, and pages that may be shared
   independently.

## Staged Delivery Plan

### Stage A: Connect the existing public surfaces

- Add a Development Map route on the home page.
- Update the generated navigation source so Development Map is the visible
  planning entry and Roadmap is the operational archive.
- Add the safe Development Map bridge from the Lab Window.
- Confirm that all three routes retain the research-status disclosure.

**Primary files:** `docs/index.md`, `docs/apply_nav_frontmatter.py`,
`docs/development_map.md`, `docs/roadmap.md`, and the public explorer shell.

### Stage B: Restore the public-evidence freshness contract

- Compare the public explorer snapshot against its canonical source records on
  every documentation update.
- Regenerate with `scripts/export_public_explorer.py --check` only inside the
  established redaction-review process.
- Add or preserve a visible export date and a safe aggregate freshness cue.
- Never publish the redaction report or names/details of unreviewed work.

**Primary files:** `scripts/export_public_explorer.py`,
`scripts/public_explorer_README.md`, `docs/public_explorer/data/`, and
`docs/public_explorer/`.

### Stage C: Turn visual tools into interpretable instruments

- Add the shared instrument profile to the Visualizations index.
- Link Brain Map components and Fishtank examples to safe public records.
- Display the static snapshot date or clearly state that a view is a local
  browser replay.

**Primary files:** `docs/visualizations.md`, `docs/brain_map/`,
`docs/fishtank/`, and `scripts/build_site_visualizations.py`.

### Stage D: Add architecture-level progressive disclosure

- Design a component map for the Architecture overview.
- Give each component a one-line role, a document anchor, and safe evidence
  links.
- Keep the full document as the authoritative narrative rather than duplicating
  it inside the diagram.

**Primary files:** `docs/architecture/overview.md`, its page assets, and the
public claims/evidence routes.

## Documentation-Routine Integration

The `/update-docs` routine and any agent making a public documentation update
must read this design record before deciding that a change is documentation-only.
It is a required impact review, not a suggestion to redesign every page.

For each update, the agent must answer these questions in its completion note:

1. Did the canonical record change in a way that changes a reader's current
   orientation, public counts, status labels, or route to detail?
2. Does the Development Map need regeneration or a check run?
3. Is the Lab Window export older or materially inconsistent with the safe
   aggregate state? If so, was a redaction-reviewed refresh proposed, performed,
   or deliberately deferred?
4. Does a generated visualization or its instrument profile need rebuilding?
5. Did navigation, a visible data timestamp, research-status disclosure, or a
   source link become stale?

The routine must not automatically publish Public Explorer data. Its redaction
report is a human review gate by design. An agent may prepare and validate a
candidate export, but it needs the established review decision before landing a
public data refresh.

For any staged public-interface implementation, verify the deployed page at
desktop and mobile widths, exercise its interactive controls, and check that
the document has no horizontal overflow or obscured content.

## Completion Criteria

A public reader should be able to do each of the following without being sent
through dense prose first:

1. Learn that REE is exploratory research with no peer-reviewed acceptance.
2. Find the current frontier and distinguish recorded work from conditional
   future work.
3. Reach a reviewed public evidence record from a summary without seeing
   withheld operational detail.
4. Understand what a visualization is capable of showing before opening it.
5. Reach the full operational archive when provenance or daily context is
   needed.

## Non-Goals

- Turning research state into a product-readiness score or release promise.
- Replacing the detailed Roadmap archive with a simplified narrative.
- Automatically publishing a public explorer refresh without redaction review.
- Treating prototype, implementation, or experiment activity as peer-reviewed
  validation.
