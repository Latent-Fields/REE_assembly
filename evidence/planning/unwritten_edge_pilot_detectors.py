#!/opt/local/bin/python3
"""Read-only nomination/extraction for the 2026-09-20 pilot, never an adjudicator.

Run with --base /Users/dgolden/REE_Working --output /path/to/scratch.json.
Only --output is written. No registry, code, queue or generated snapshot is changed.
"""
import argparse
import ast
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml


def reachable(start, reverse):
    seen, todo = set(), list(start)
    while todo:
        node = todo.pop()
        if node in seen:
            continue
        seen.add(node)
        todo.extend(reverse.get(node, []))
    return seen


def status_class(raw):
    # Completion of the implementation is not completion of validation.
    text = str(raw or '').strip().lower()
    if text in {'done', 'implemented', 'resolved', 'closed', 'complete', 'completed'}:
        return 'complete'
    if re.match(r'^(done|implemented|resolved|closed|completed)(?:\b|_)', text):
        return 'completion_prefix_review_required'
    if re.match(r'^(proposed|pending|candidate|blocked|open|in_progress|in-progress|probe_queued)\b', text):
        return 'not_complete'
    return 'unknown'


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--base', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    ap.add_argument('--allowed-node', action='append', default=[], help='Explicit node ID cleared by the manual re-pose pre-check; omit for ranking only')
    args = ap.parse_args()
    base, assembly = args.base, args.base / 'REE_assembly'
    sys.path.insert(0, str(assembly / 'scripts'))
    from check_closure_drift import parse_plan_frontmatter
    files = {}

    def read(path):
        raw = path.read_bytes()
        files[str(path.relative_to(base))] = hashlib.sha256(raw).hexdigest()
        return raw.decode()

    claims = yaml.safe_load(read(assembly / 'docs/claims/claims.yaml'))
    byclaim = {c['id']: c for c in claims}
    queue = json.loads(read(assembly / 'evidence/planning/substrate_queue.json'))['queue']
    front = read(assembly / 'docs/CURRENT_FRONT.md')
    nodes, plans, duplicate_ids = {}, [], []
    for path in sorted((assembly / 'evidence/planning').glob('*_plan.md')):
        fm = parse_plan_frontmatter(path)
        if not fm or 'closure_plan' not in fm:
            continue
        read(path)
        plan = fm['closure_plan']
        if not isinstance(plan, dict):
            continue
        plans.append({'id': plan.get('id'), 'generation': plan.get('generation', 'v3'), 'path': str(path.relative_to(assembly))})
        for node in plan.get('nodes', []):
            nid = node['id'] if ':' in node['id'] else str(plan['id'])+':'+node['id']
            if nid in nodes:
                duplicate_ids.append(nid)
            nodes[nid] = dict(node, id=nid, _plan=plan.get('id'), _generation=plan.get('generation', 'v3'), _path=str(path.relative_to(assembly)))
    if duplicate_ids:
        raise ValueError(f'Duplicate node IDs: {duplicate_ids}')
    revnode, revclaim, unresolved = defaultdict(set), defaultdict(set), []
    for node in nodes.values():
        for dep in (node.get('depends_on') or []):
            if dep not in nodes and str(node['_plan'])+':'+dep in nodes:
                dep = str(node['_plan'])+':'+dep
            if dep in nodes:
                revnode[dep].add(node['id'])
            else:
                unresolved.append({'node': node['id'], 'reference': dep})
    for c in claims:
        for dep in (c.get('depends_on') or []):
            revclaim[dep].add(c['id'])
    excluded = {'done', 'closed', 'parked', 'parked_indefinite', 'deferred', 'deferred_v4', 'deferred_v5'}
    ranks = []
    for nid, node in nodes.items():
        if node['_generation'] != 'v3' or str(node.get('status', '')).lower().replace(' ', '_') in excluded:
            continue
        downstream = {x for x in reachable([nid], revnode) - {nid} if nodes[x]['_generation'] == 'v3'}
        seeds = {c for x in downstream | {nid} for c in nodes[x].get('unblocks_claims', []) if c in byclaim}
        claim_desc = reachable(seeds, revclaim) - seeds
        direct = set(node.get('unblocks_claims', []))
        ids = sorted(direct | {nid}, key=len, reverse=True)
        pattern = re.compile(r'(?<![\w:-])(?:' + '|'.join(map(re.escape, ids)) + r')(?![\w:-])')
        routes = [c['id'] for c in claims if pattern.search(str(c.get('what_would_answer', '')))]
        front_match = bool(pattern.search(front))
        ranks.append({'id': nid, 'downstream_nodes': len(downstream), 'downstream_claims': len(claim_desc), 'live_front': int(front_match), 'what_would_answer_routes': len(routes), 'downstream_node_ids': sorted(downstream), 'seed_claim_ids': sorted(seeds), 'downstream_claim_ids': sorted(claim_desc), 'route_claim_ids': routes, 'status': node.get('status'), 'path': node['_path']})
    ranks.sort(key=lambda x: (-x['downstream_nodes'], -x['downstream_claims'], -x['live_front'], -x['what_would_answer_routes'], x['id']))
    selected = [r['id'] for r in ranks[:8]]
    fields = ['title', 'status', 'unblocks_claims', 'depends_on', 'blocking_on', 'blocking_external', 'resume_condition', 'awaiting', 'assembly_status', 'revisit_after', 'owner_exq', 'live', 'phase', 'question_id']
    summaries = {n: {k: nodes[n][k] for k in fields if k in nodes[n]} for n in selected}
    if not args.allowed_node:
        result = {'ranking': ranks, 'selected': selected, 'selected_nodes': summaries, 'unresolved_closure_dependencies': unresolved, 'input_sha256': files}
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2, default=str)+'\n')
        print(json.dumps([{k:r[k] for k in ['id','downstream_nodes','downstream_claims','live_front','what_would_answer_routes','status']} for r in ranks[:8]], indent=2))
        return
    assert set(args.allowed_node) <= set(selected), 'Allowed nodes must be in the frozen top eight'
    absent = re.compile(r'does\s+not\s+exist|no[\s-]+consumer|never[\s-]+read|not[\s-]+yet[\s-]+built|must[\s-]+be[\s-]+built|no[\s-]+instrument', re.I)
    d3 = []
    for c in claims:
        for field in ['what_would_answer', 'evidence_quality_note']:
            text = str(c.get(field, ''))
            for m in absent.finditer(text):
                d3.append({'claim': c['id'], 'field': field, 'offset': m.start(), 'match': m.group(), 'context': text[max(0,m.start()-180):m.end()+260]})
    d4 = [{'sd_id': q['sd_id'], 'status_class': status_class(q.get('status')), 'raw_status': q.get('status'), 'unblocks_claims': q.get('unblocks_claims', []), 'title': q.get('title')} for q in queue if q.get('depends_on_unresolved') == [] and status_class(q.get('status')) != 'complete']
    d1, parse_errors = [], []
    for path in sorted((base / 'ree-v3/ree_core').rglob('*.py')):
        source = read(path)
        try:
            tree = ast.parse(source)
        except SyntaxError as e:
            parse_errors.append({'path': str(path.relative_to(base)), 'error': str(e)})
            continue
        for fn in ast.walk(tree):
            if not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            stores, loads = defaultdict(list), set()
            for n in ast.walk(fn):
                if isinstance(n, ast.Name):
                    if isinstance(n.ctx, ast.Store): stores[n.id].append(n.lineno)
                    if isinstance(n.ctx, ast.Load): loads.add(n.id)
            for name in sorted(stores.keys() - loads):
                if name.startswith('_'): continue
                d1.append({'path': str(path.relative_to(base)), 'function': fn.name, 'name': name, 'lines': stores[name]})
    claim_pattern = re.compile(r'\b(?:MECH|ARC|SD|INV|Q|GOV|IMPL)-[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*\b')
    # Exact joins; unresolved references are retained, never silently considered done.
    completed = defaultdict(list)
    for kind, population, key in [('claim', claims, 'id'), ('substrate', queue, 'sd_id'), ('closure', list(nodes.values()), 'id')]:
        for item in population:
            sc = status_class(item.get('status'))
            if sc in {'complete','completion_prefix_review_required'}:
                completed[item[key]].append({'registry':kind,'raw_status':item.get('status'),'status_class':sc})
    completed_pattern = re.compile(r'(?<![\w:-])(?:'+'|'.join(map(re.escape,sorted(completed,key=len,reverse=True)))+r')(?![\w:-])')
    extract = {}
    for nid in args.allowed_node:
        owned = [byclaim[c] for c in nodes[nid].get('unblocks_claims', []) if c in byclaim]
        rows = []
        for c in owned:
            rows.append({k: c[k] for k in ['id','title','status','implementation_phase','epistemic_category','what_would_answer','evidence_quality_note','depends_on','location'] if k in c})
        gates = [(f'node.{f}', str(nodes[nid].get(f, ''))) for f in ['blocking_on','resume_condition','blocking_external','awaiting']]
        gates += [(c['id']+'.'+f, str(c.get(f,''))) for c in owned for f in ['what_would_answer','evidence_quality_note']]
        stale = []
        prose_refs = []
        for field, text in gates:
            for m in claim_pattern.finditer(text):
                target = m.group()
                prose_refs.append({'field': field,'target': target,'registered_claim': target in byclaim})
            for m in completed_pattern.finditer(text):
                target=m.group()
                stale.append({'field':field,'target':target,'status':completed[target],'context':text[max(0,m.start()-140):m.end()+200]})
        owned_ids = {c['id'] for c in owned}
        extract[nid] = {'claims':rows,'D2_complete_reference_hits':stale,'D3_hits':[h for h in d3 if h['claim'] in owned_ids],'D4_related':[h for h in d4 if set(h['unblocks_claims']) & owned_ids], 'D6_prose_references':prose_refs}
    now = subprocess.check_output(['date','-u','+%Y-%m-%dT%H:%M:%SZ'], text=True).strip()
    result = {'schema_version':'unwritten_edge_pilot_extraction/v1','generated_utc':now,'method':'preregistered plan; raw nominations only, no adjudication','repo_heads':{r:subprocess.check_output(['git','-C',str(base/r),'rev-parse','HEAD'],text=True).strip() for r in ['REE_assembly','ree-v3']},'counts':{'claims':len(claims),'substrate_entries':len(queue),'all_closure_nodes':len(nodes),'v3_closure_nodes':sum(n['_generation']=='v3' for n in nodes.values()),'eligible_v3_nodes':len(ranks),'D3_claims':len({h['claim'] for h in d3}),'D3_hits':len(d3),'D4_not_exact_complete_empty_dependencies':len(d4),'D1_unread_local_names':len(d1)},'status_classes':dict(Counter(status_class(q.get('status')) for q in queue)),'ranking':ranks,'selected':selected,'selected_nodes':summaries,'unresolved_closure_dependencies':unresolved,'D1_global':d1,'D1_parse_errors':parse_errors,'D3_global':d3,'D4_global':d4,'selected_extraction':extract,'input_sha256':files}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2,default=str)+'\n')
    print(json.dumps({'counts':result['counts'],'selected_ranks':[{k:r[k] for k in ['id','downstream_nodes','downstream_claims','live_front','what_would_answer_routes','status']} for r in ranks[:8]],'positive_control_D3':any(h['claim']=='MECH-092' for h in d3),'positive_control_D1':[h for h in d1 if h['name']=='replay_trajs'],'unresolved_closure_dependencies':len(unresolved),'D1_parse_errors':parse_errors},indent=2))


if __name__ == '__main__':
    main()
