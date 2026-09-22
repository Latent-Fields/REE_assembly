# V3-EXQ-1072 -- INV-024 offline/online write-locus isolation audit

**Status:** PASS -- label: `offline_online_write_locus_isolation_holds`
**Purpose:** evidence (INV-024). Single as-named config x 5 seeds = 5 cells.

- C1 offline authority stores unmutated: **True** (worst cell 0, threshold 0)
- C2 online lineage complete AFTER first commit (LOAD-BEARING): **True** (worst cell 0, threshold 0)
- C2b whole-run lineage-less fraction (SECONDARY, not gating): False (worst cell 0.0690)
- readiness gate green: True
- durable writes audited: 1481 | after first commit: 1452 | lineage-less (whole run): 19
- closure_entry_ticks total: 0 (expected 0 -- the closure disjunct is structurally dead)

**C2 is deliberately NOT the whole-run fraction.** No E3 commit is possible before tick 5
(rv = 0.5*0.95^n against a 0.40 bar), so a harm event in a cell's first five ticks is a
structurally lineage-less write. C2 therefore scores only writes at ticks where commitment
was POSSIBLE -- testing bypass, not scheduling. C2b keeps the warm-up gap visible.

**Evidence asymmetry is registered PER HALF** -- see `evidence_asymmetry_per_half`. An
overall PASS is a contract regression-guard on the offline half (construction-guaranteed)
plus a moderate live confirmation on the online half. Do not average them, and do not read a
PASS as confirmation that isolation is architecturally necessary.

See `interpretation.closure_disjunct_untestable` for why the second lineage disjunct could
not be tested here, and `per_cell_results` for the full per-seed table with the pre/post
authority-store hash snapshots.
