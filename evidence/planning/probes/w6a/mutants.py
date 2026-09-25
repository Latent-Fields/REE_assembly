"""Mutation half of the W6a test-half check: each mutant re-introduces one defect and must
turn the named contracts red. Run from the prebuild-wt sandbox (build files copied in)."""
import subprocess, sys, pathlib
root = pathlib.Path(sys.argv[1])
mem = root / "ree_core/utils/waking_trainer_world_encoder.py"
orig = mem.read_text()
MUT = {
 "M1_side_copy_preprojection": (
   [("        enc_mods: List[nn.Module] = [agent.world_obs_encoder, se.world_encoder]",
     "        import copy as _copy\n        self._wobs_copy = _copy.deepcopy(agent.world_obs_encoder)\n        enc_mods: List[nn.Module] = [se.world_encoder]"),
    ("        self._encoder_named = named\n",
     "        named += [('side_copy.' + n, p) for n, p in self._wobs_copy.named_parameters()]\n        self._encoder_named = named\n"),
    ("agent.world_obs_encoder(ow)],", "self._wobs_copy(ow)],")],
   ["w6a_03_group", "w6a_04"]),
 "M2_detached_chain": (
   [("        z = self.sensed_z_world(recs)\n        return self.objective(z, recs)",
     "        z = self.sensed_z_world(recs).detach()\n        return self.objective(z, recs)")],
   ["w6a_03_group", "w6a_04", "w6a_06_w6a"]),
 "M3_heads_draw_global_rng": (
   [("        with torch.random.fork_rng(devices=[]):\n            torch.manual_seed(int(seed) + 70)\n",
     "        if True:\n")],
   ["w6a_02"]),
 "M4_no_outside_grad_restore": (
   [("    restore_outside_grads = True", "    restore_outside_grads = False")],
   ["w6a_03_group", "w6a_03b"]),
}
res = {}
for name, (subs, must_fail) in MUT.items():
    s = orig
    for a, b in subs:
        assert s.count(a) == 1, (name, a[:60])
        s = s.replace(a, b)
    mem.write_text(s)
    try:
        for k in must_fail:
            r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider",
                                "tests/contracts/test_w6a_world_encoder_member.py", "-k", k],
                               cwd=root, capture_output=True, text=True)
            last = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr[-200:]
            res[(name, k)] = (r.returncode != 0, last)
            print("%-28s %-14s %s  | %s" % (name, k, "RED (ok)" if r.returncode else "GREEN (BLIND!)", last), flush=True)
    finally:
        mem.write_text(orig)
# control: unmutated all green
r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider",
                    "tests/contracts/test_w6a_world_encoder_member.py"], cwd=root, capture_output=True, text=True)
print("CONTROL unmutated:", r.stdout.strip().splitlines()[-1])
print("ALL MUTANTS CAUGHT:", all(v[0] for v in res.values()))
