---
nav_exclude: true
---

# REE Triple-View Diagram Bundle

This bundle keeps architecture visualization in three synchronized views:

1. `architecture_static.mmd` / `architecture_static.svg` (component structure)
2. `architecture_typed_dataflow.mmd` / `architecture_typed_dataflow.svg` (typed runtime streams/signals)
3. `episode_sequence.mmd` / `episode_sequence.svg` (single-tick temporal trace)

## Explorer Integration

The Claims Explorer exposes this as `View -> Triple View` in:

- `docs/claims/explorer.html`

The triple view includes:

- current-epoch claim overlays,
- conflict and gap badges on nodes/edges,
- tooltip summaries and clickable inspector tabs (`Claims`, `Conflicts`, `Needs / Gaps`).

## Shared Contract

- Components and stream IDs are canonicalized in `streams.md`.
- Routing source of truth for edges lives in `stream_routing.v1.yaml`.
- Edge labels are loggable stream/signal IDs.
- Changes to architecture contract artifacts (including `hook_registry.v1.json`) require an explicit triple-view freshness review.

## Local Commands

If Mermaid CLI is available (`mmdc`):

```bash
bash scripts/architecture/check_consistency.sh
bash scripts/architecture/render_diagrams.sh
```

## Update Flow

1. Update `stream_routing.v1.yaml` (and relevant architecture contracts/docs) first.
2. Mirror routing/structure changes into the `.mmd` sources.
3. Run `bash scripts/architecture/check_consistency.sh`.
4. Render `.svg` assets with `bash scripts/architecture/render_diagrams.sh`.
5. If view behavior changed, update `docs/claims/explorer.html` and this guide.

## CI Behavior

- Workflow: `.github/workflows/architecture-diagrams.yml`
- On pull requests touching architecture docs/contracts: run freshness and consistency checks.
- Freshness rule: if architecture source docs/contracts change without triple-view maintenance files changing, CI fails.
- On pushes to the default branch touching architecture docs/contracts: run freshness+consistency, render SVGs, and commit updated SVGs.
- Weekly rhythm: scheduled run every Monday at 16:00 UTC performs freshness+consistency and re-renders SVGs if needed.
