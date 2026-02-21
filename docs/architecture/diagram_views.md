# REE Three-View Diagram Bundle

This bundle keeps architecture visualization in three synchronized views:

1. `architecture_static.mmd` (C4-style static structure)
2. `architecture_typed_dataflow.mmd` (typed runtime streams/signals)
3. `episode_sequence.mmd` (single-tick temporal trace)

Shared naming contract:

- Components and stream IDs are canonicalized in `streams.md`.
- Routing source of truth for edges lives in `stream_routing.v1.yaml`.
- Edge labels are loggable stream/signal IDs.

## Local render commands

If Mermaid CLI is available (`mmdc`):

```bash
bash scripts/architecture/check_consistency.sh
bash scripts/architecture/render_diagrams.sh
```

## Update flow

1. Update `stream_routing.v1.yaml` first.
2. Mirror those changes into the `.mmd` files.
3. Render `.svg` assets.
4. Verify component IDs still match `streams.md`.

## CI behavior

- Workflow: `.github/workflows/architecture-diagrams.yml`
- On pull requests touching architecture docs/contracts: run freshness check and consistency checks.
- Freshness rule: if architecture source docs change without any triple-view diagram contract updates, CI fails.
- On pushes to `master` touching architecture docs/contracts (including merges): run freshness+consistency, render SVGs, and commit updated SVG assets back to `master`.
- Weekly rhythm: scheduled run every Monday at 16:00 UTC performs freshness+consistency and re-renders SVGs if needed.
