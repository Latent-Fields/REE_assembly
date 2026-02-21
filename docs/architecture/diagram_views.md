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
- On pull requests touching architecture diagram files: run consistency checks only.
- On pushes to `master` touching architecture diagram files (including merges): run consistency checks, render SVGs, and commit updated SVG assets back to `master`.
