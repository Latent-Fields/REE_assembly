# REE_OpenClaw Testbed Interface

Date: 2026-02-18  
Status: Active

## Purpose

Define the minimal interface between:

- `REE_assembly` (canonical REE claims and planning source), and
- `REE_OpenClaw` (standalone implementation/testing ground).

## Repository Roles

1. `REE_assembly`
- Owns canonical REE documentation, claims, conflicts, and thought intake.
- Produces architecture constraints and planning guidance.

2. `REE_OpenClaw` (`/Users/dgolden/Documents/GitHub/REE_OpenClaw`)
- Implements and tests REE-like authority/commitment mechanics in an OpenClaw-class shell.
- Owns runtime code, CI behavior, and test probes.

## Minimal Upstream Inputs From REE_assembly

- `docs/thoughts/2026-02-18_new_implementation_openclaw.md`
- Current canonical claim registry and subsystem docs under `docs/`
- Planning directives under `evidence/planning/` as needed

## Minimal Downstream Feedback To REE_assembly

- Probe outcomes that support/refute REE claims
- Newly observed failure modes and unresolved tensions
- Proposed claim or mechanism updates from implementation findings

## Operating Rule

Do not keep an implementation copy of `REE_OpenClaw` inside `REE_assembly`.  
`REE_assembly` is upstream docs/planning; `REE_OpenClaw` is the execution testbed.

