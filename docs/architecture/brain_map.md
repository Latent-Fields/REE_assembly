---
title: REE Brain Map
parent: Architecture
nav_order: 15
---

# REE Brain Map

The brain map is a **functional analogy** visualization: it shows which
brain-inspired names in REE (`hippocampus.*`, `amygdala.*`, etc.) are backed by
claims, substrate code, and experiment evidence. It does **not** assert
biological homology or anatomical completeness.

**Read first:** [Founder ontology (E1 / E2 / E3)](founder_ontology.md) -- the
intended cerebrum / cerebellum / commitment reading and how it maps to modules.
The live map is catching up to that ontology (see **Layout intent** below).

## URLs

| URL | Purpose |
|-----|---------|
| `/brain-map` | Interactive 2D sagittal map |
| `/api/brain-map` | Live JSON aggregate (claims + evidence + queue) |

Requires `serve.py` (not `file://`).

## Layout intent (founder-aligned v1.1)

| Visual territory | Founder function | Current MVP (2026-05-19) |
|------------------|------------------|---------------------------|
| Bulk of cerebrum | **E1** perception-association matrix + goal specializations (PFC, etc.) | E1 in right-hand engineering strip; cortex regions separate |
| Cerebellum (posterior) | **E2** fast forward predictor | Ghost "cerebellum" marked out of scope; E2 in strip |
| BG / ventral forebrain | **E3** commitment & comparison | `basal_ganglia` region + policy functional analog |
| Medial temporal | Hippocampal rollouts (partner, not E2) | `hippocampus` region |

**Planned:** anatomy-forward SVG with E1 occupying cortical mass, E2 on cerebellum,
E3/BG at the gate; engineering strip retired or minimized. Data layer (`/api/brain-map`)
unchanged.

## Data model (hybrid)

| Layer | File | Role |
|-------|------|------|
| Static ontology | `brain_region_map.yaml` | Region ids, subject prefixes, SVG path ids, `ree_core` paths, pathways |
| Static layout | `brain_map_sagittal.svg` | Clickable regions (fill colors applied by the page from API) |
| Live overlay | `GET /api/brain-map` | Claim counts, implementation tier, evidence, v3_pending, queued EXQs |
| Intent | `founder_ontology.md` | How to read E1/E2/E3 vs biology (not auto-loaded by API) |

## Coverage tiers

| Tier | Meaning |
|------|---------|
| `expressed` | Implemented (full/partial) and at least one PASS experiment run |
| `claimed` | Claims exist; thin or no experimental support |
| `frontier` | Leading edge: v3_pending, queued EXQs, or open conflicts on region docs |
| `absent` | Out-of-scope ghost regions or no claims |

## Adding a region

1. Align with [founder_ontology.md](founder_ontology.md) (which function does this region serve?).
2. Add a block under `regions:` in `brain_region_map.yaml` with unique `id`,
   `subject_prefixes`, and `svg_path_ids`.
3. Add a matching `<path id="region_...">` in `brain_map_sagittal.svg`.
4. Add the prefix to `known_anatomy_prefixes` if it is anatomy-tagged in claims.
5. Run `python3 scripts/validate_brain_region_map.py` from `REE_assembly/`.
6. Reload `/brain-map` (auto-refresh every 60s).

Do **not** park E1 or E2 only in `engineering_nodes` once v1.1 layout lands -- map them
to cerebrum and cerebellum respectively.

## Phase 2 (deferred)

A Three.js clear-head shell may consume the same `/api/brain-map` payload once the
2D map is stable in daily use.

## Non-goals

- Clinical neuroanatomy accuracy
- Implied completeness of a whole brain
- Replacing the claims explorer or subsystem atlas
- Homology claims (functional analogy only)
