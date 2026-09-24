#!/bin/bash
cd "$(dirname "$0")"
for s in "$@"; do echo "=== SPLIT_s$s $(date -u +%H:%M:%S)"; /opt/local/bin/python3 eval_split_probe.py --seed $s --out results/SPLIT_s$s.json > logs/SPLIT_s$s.log 2>&1; grep -E "^SPLIT|wrote|Trace|Error" logs/SPLIT_s$s.log | cut -c1-600; done
echo "SPLIT ALL DONE $(date -u +%H:%M:%S)"
