#!/bin/bash
cd "$(dirname "$0")"
P=/opt/local/bin/python3
for s in "$@"; do echo "=== EVAL_s$s $(date -u +%H:%M:%S)"; $P evaluation_edge_probe.py --seed $s --out results/EVAL_s$s.json > logs/EVAL_s$s.log 2>&1; grep -E "wrote|Trace|Error" logs/EVAL_s$s.log | cut -c1-200; done
echo "EVAL ALL DONE $(date -u +%H:%M:%S)"
