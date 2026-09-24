#!/bin/bash
cd "$(dirname "$0")"
for s in "$@"; do echo "=== TB_s$s $(date -u +%H:%M:%S)"; /opt/local/bin/python3 evaluation_edge_probe.py --seed $s --tiebreak 1 --force-gate 0 --arms E1_FULL,E2_FULL_EVAL,E4_FULL_SHUF --out results/TB_s$s.json > logs/TB_s$s.log 2>&1; grep -E "wrote|Trace|Error" logs/TB_s$s.log | cut -c1-200; done
echo "TB ALL DONE $(date -u +%H:%M:%S)"
