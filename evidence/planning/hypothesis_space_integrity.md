# Hypothesis-Space Integrity Audit (anti-Goodhart)

Generated: 2026-07-17T17:53:19Z

GENERATED FILE -- do not edit by hand. Advisory, non-blocking sibling of `check_closure_drift.py`. It audits `hypothesis_space_registry.v1.json` + `hypothesis_space_timeseries.v1.jsonl` for the three ways the Narrow/Decide dashboard could be gamed (design rule 5). Flags are review hints, never a gate.

Audited **6** open question(s) across **1** time-series snapshot(s). **0** flag(s) raised.

## (a) Un-backed surviving-count drop (0)

_A question's surviving count fell with no adjudicated `weakens`/discrimination behind the elimination._

_None._

## (b) Post-hoc enlargement of a frozen set (0)

_The frozen initial enumeration grew, or a hypothesis was pre-registered after its own adjudicating run._

_None._

## (c) Confirmed without a passed control (0)

_A `confirmed` hypothesis lacks control_passed == true._

_None._

## (d) Elimination-bar violation (0)

_An `eliminated`/`split` hypothesis is missing part of the bar (met_elimination_bar + control_passed + non_degenerate)._

_None._

---

This audit promotes/demotes nothing. Response to any flag is a human decision at governance (the same handling as `check_closure_drift.py`).

