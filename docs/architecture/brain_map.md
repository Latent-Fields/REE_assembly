# REE Brain Map

The brain map is a **functional analogy** visualization: it shows which
brain-inspired names in REE (`hippocampus.*`, `amygdala.*`, etc.) are backed by
claims, substrate code, and experiment evidence. It does **not** assert
biological homology or anatomical completeness.

## URLs

| URL | Purpose |
|-----|---------|
| `/brain-map` | Interactive 2D sagittal map |
| `/api/brain-map` | Live JSON aggregate (claims + evidence + queue) |

Requires `serve.py` (not `file://`).

## Data model (hybrid)

| Layer | File | Role |
|-------|------|------|
| Static ontology | `brain_region_map.yaml` | Region ids, subject prefixes, SVG path ids, `ree_core` paths, pathways |
| Static layout | `brain_map_sagittal.svg` | Clickable regions (fill colors applied by the page from API) |
| Live overlay | `GET /api/brain-map` | Claim counts, implementation tier, evidence, v3_pending, queued EXQs |

## Coverage tiers

| Tier | Meaning |
|------|---------|
| `expressed` | Implemented (full/partial) and at least one PASS experiment run |
| `claimed` | Claims exist; thin or no experimental support |
| `frontier` | Leading edge: v3_pending, queued EXQs, or open conflicts on region docs |
| `absent` | Out-of-scope ghost regions or no claims |

## Adding a region

1. Add a block under `regions:` in `brain_region_map.yaml` with unique `id`,
   `subject_prefixes`, and `svg_path_ids`.
2. Add a matching `<path id="region_...">` in `brain_map_sagittal.svg`.
3. Add the prefix to `known_anatomy_prefixes` if it is anatomy-tagged in claims.
4. Run `python3 scripts/validate_brain_region_map.py` from `REE_assembly/`.
5. Reload `/brain-map` (auto-refresh every 60s).

Engineering nodes (E1, E2, E3, control plane) live in `engineering_nodes` and render
in the right-hand strip, not inside the cortical silhouette.

## Phase 2 (deferred)

A Three.js clear-head shell may consume the same `/api/brain-map` payload once the
2D map is stable in daily use.

## Non-goals

- Clinical neuroanatomy accuracy
- Implied completeness of a whole brain
- Replacing the claims explorer or subsystem atlas
