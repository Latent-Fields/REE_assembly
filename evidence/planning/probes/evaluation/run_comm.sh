#!/bin/bash
cd "$(dirname "$0")"
for s in "$@"; do echo "=== COMM_s$s $(date -u +%H:%M:%S)"; /opt/local/bin/python3 evaluation_edge_probe.py --seed $s --tiebreak 1 --comm 1 --force-gate 0 --arms E1_FULL,E2_FULL_EVAL,E4_FULL_SHUF --out results/COMM_s$s.json > logs/COMM_s$s.log 2>&1; grep -E "wrote|Trace|Error" logs/COMM_s$s.log | cut -c1-300; done
echo "COMM ALL DONE $(date -u +%H:%M:%S)"
