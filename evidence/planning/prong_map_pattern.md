# Prong Map — a reusable pattern for parallel multi-face campaigns

- **Registered:** 2026-06-22
- **Status:** pattern spec (generic). First instance: `conversion_ceiling_prong_map.md`.
- **Companion mechanisms:** closure-node `status: assembling` (assembly_vs_closure_plan.md), substrate_queue `fallback_ladder`, arm-fingerprint baselines (arm_reuse_fingerprint_plan.md), the ARC-106 matched-stack / no-op-default build discipline.

## Why this pattern exists

Some REE problems are not one wall — they are **one surface symptom with several mechanistically-distinct loci** (the conversion ceiling is four roots sharing `committed_action_class_entropy ~ 0`; object-representation has type/token/binding pillars; sleep has several aggregation faces). Attacking them one lever at a time, serially, produces the modal failure mode of the whole machine: a 7-12x lettered-iteration burn circling one claim, each FAIL read as a verdict.

A **prong map** is a campaign-level resume primitive that lets several attack paths be **pursued in parallel, rested without nagging, composed when ready, and resurfaced cheaply** — so the campaign's real test is the *assembled* substrate, not a sequence of isolated per-lever falsifiers.

## Core concepts

### Face
A **separable attack surface**, each pinned to **exactly one module**. The modularity is the load-bearing property: prongs on *different* faces touch *different* modules, so they (a) run concurrently with zero code collision, (b) compose cleanly into a co-armed arm. Contention is *within* a face (one module, interacting levers), never across faces.

### Prong
A single lever attacking one face. Each prong carries:

| field | meaning |
|---|---|
| `face` | which attack surface |
| `module` | the one module it touches |
| `flag` | the no-op-default config flag that arms it (`use_X`) |
| `state` | lifecycle state (below) |
| `own_face_validation` | the falsifier that proves the lever works *at its own face* |
| `claim_ids` | claims it bears on |
| `baseline` | **per-prong** by default (no shared frozen baseline — see below) |
| `needs_before_run` | what must exist before its falsifier can run |

### Lifecycle states
```
design  ->  build (no-op-default, bit-identical OFF)  ->  face-validated  ->  composition-ready  ->  in-full-stack
                                                                                        |
                                                                              (or: REFUTED at own face -> dropped)
```

### Composition-readiness gate
A lever may join the full-stack matched stack **only** when all three hold:
1. built **no-op-default + bit-identical OFF** (does not perturb other prongs' baselines);
2. **validated at its own face** (its `own_face_validation` PASSed);
3. its **pairwise interaction** with already-included levers is **characterized** (no destructive cancel — interactions within a face must be measured, not assumed; the canonical trap is the conversion ceiling's Factor A x Factor B, which *cancelled*).

A prong that is **REFUTED at its own face** is dropped from the full-stack, not carried.

### Full-stack target arm — the real test
The campaign's actual test: **all composition-ready levers ON as a matched stack on both arms, sweep the one scientific variable.** This tests the hypothesis that conversion is **emergent from the assembled substrate** even when no single lever converts in isolation. PASS -> the assembled substrate works (supports the claims, closes the owning node). FAIL -> **leave-one-out ablation** to find the missing/blocking face.

## The discipline (substrate selection care points)

1. **Compose flags, don't branch code.** A prong is a flag-stack on ONE substrate, never a swapped-in build variant. Every lever is a `getattr(config, "use_X", False)` no-op-default flag.
2. **No-op-default + bit-identical OFF** on every build — the invariant that lets prong B land without perturbing prong A's baseline.
3. **Matched-stack-constants, sweep-one** within a prong (mandatory inside a crowded single-module face).
4. **Per-prong baselines** (this pattern's default): each isolation falsifier carries its own OFF arm; the full-stack arm gets its own dedicated all-stack-ON / swept-var-OFF control. **No shared frozen baseline** -> zero arm-fingerprint false-hit risk. (A shared canonical baseline is the *opposite* trade — cheaper compute, fingerprint-fragile — and is explicitly NOT used here.)
5. **Build contention serializes; run contention does not.** Two builds editing the same module serialize (one session at a time); two runs that only set different flags never collide.

## How a prong map rests and resurfaces

- **One `assembling` closure node per live prong**, under a campaign closure node. `status: assembling` is weight `None` (off the closure %, never punishes the green-board), surfaced on the **assembly-frontier** axis, restful in drift (no re-stamp nagging). Companion fields: `awaiting:` (the substrate being built), `assembly_status:` (`queued`/`in_progress`/`built`), `revisit_after:` (optional ISO date).
- **The campaign node** is the umbrella; the prong nodes are its children. The full-stack arm is itself a node (assembling until its components are composition-ready).
- **Resurfacing** = read the prong map; every prong's `state` + `needs_before_run` tells you what is runnable now, what is building, and what is blocked — without re-deriving from scattered autopsies.

## Instantiation checklist (for a new campaign)

1. Decompose the problem into **faces** (one module each).
2. Inventory **prongs** per face; assign each a lifecycle `state`.
3. Build the **composition matrix** (compose-clean across faces; characterize-required within a face — and each within-face interaction earns its **own** characterization experiment).
4. Specify the **full-stack target arm** (matched stack + swept variable + DV + its dedicated baseline + leave-one-out-on-FAIL).
5. Write the instance doc (`<campaign>_prong_map.md`) + a campaign closure plan (`<campaign>_campaign_plan.md`) with one `assembling` node per live prong.
6. Cross-ref the owning substrate_queue entry's `fallback_ladder` <-> the prong map.
