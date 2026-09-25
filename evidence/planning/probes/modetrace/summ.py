import json, sys
for l in open(sys.argv[1]):
  d=json.loads(l)
  if len(sys.argv)>2 and not d['arm'].startswith(tuple(sys.argv[2].split(','))): continue
  print(d['arm'],d['seed'],'ticks',d['n_coord_ticks'],'eps',d['n_episodes'],'sw',d['switches_total'],'extra',d['within_life_switches_beyond_first'],'into',d.get('switch_into_counts'))
  print('  argmax',d['argmax_counts'],'cur',d['current_mode_counts'])
  print('  gap',d['ext_minus_best_other_logit'],'sal',d['sal_aggregate'],'parts',{k:v['max'] for k,v in d['sal_parts'].items()})
  print('  contrib',d['affinity_contrib_mean']); print('  dacc_pe',d['inputs']['dacc_pe'],'etd',d['inputs']['external_task_drive'],'ceamp',d['inputs']['cea_mode_prior'],'ceafp',d['inputs']['cea_fast_prime']); print('  cea',d['cea'])
