"""Contract tests for sync_v3_results.build_runpack_docs environment projection.

WHY THIS EXISTS. The pack manifest's `environment` block -- {env_id, env_version,
dynamics_hash, reward_hash, observation_hash, config_hash, tier} -- exists to
answer "did these two runs execute the same environment?". Until 2026-09-17 this
converter hardcoded a literal asserting env_id "ree.causal_grid_world_v3" /
env_version "3.0.0" / tier "causal_grid_world_v3" with all four content hashes
"unknown", for EVERY pack it built, regardless of the environment the run used.
So did the other writer (ree-v3 experiments/pack_writer.DEFAULT_ENVIRONMENT).

Measured across REE_assembly/evidence/experiments on 2026-09-17: 1752 of the 1826
packs carrying an environment block asserted exactly that literal -- including
runs whose config was in fact CausalGridWorldV2 -- and no CausalGridWorldV3 has
ever existed (ree_core.environment.causal_grid_world defines one class,
CausalGridWorld; CausalGridWorldV2 is an alias factory setting
use_proxy_fields=True). The V3-EXQ-1036 failure autopsy surfaced it.

Two jobs, and they are opposite in direction:

1. THE DEFAULT ASSERTS NOTHING. With no environment on the flat, every field is
   "unknown". An asserted-but-wrong env_id is worse than an absent one because it
   reads as recorded provenance -- the same reason source_repo.commit keeps ""
   rather than "unknown" (test_sync_v3_results_source_repo.py). The block is still
   EMITTED rather than omitted, because REE_assembly
   scripts/generate_experiment_profile.py reports `environment.<field> ==
   "unknown"` as a named provenance gap; omitting it would make the gap invisible.

2. A REAL BLOCK IS CARRIED. This converter cannot DISCOVER an environment -- it
   materialises a pack from a flat manifest, possibly on the hub days after the
   run, having never constructed the environment. Only the producer can identify
   it (ree-v3 pack_writer.environment_for(env)), so the converter's only job is
   transport. Today no flat carries a usable block, so this carry has no
   measurable effect; it is the ONLY channel by which the producer-side fix can
   ever reach a pack, and without it that fix dies at the flat manifest.

Run directly:  python test_sync_v3_results_environment.py
Or via pytest:  pytest test_sync_v3_results_environment.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from sync_v3_results import build_runpack_docs  # noqa: E402

ENV_FIELDS = (
    "env_id", "env_version", "dynamics_hash",
    "reward_hash", "observation_hash", "config_hash", "tier",
)

# The exact literal this converter emitted before 2026-09-17, pinned by VALUE so
# the regression cannot return under a paraphrase.
FABRICATED = {
    "env_id": "ree.causal_grid_world_v3",
    "env_version": "3.0.0",
    "tier": "causal_grid_world_v3",
}

REAL = {
    "env_id": "ree.causal_grid_world",
    "env_version": "causal_grid_world/v1",
    "dynamics_hash": "4e8e3931183d",
    "reward_hash": "71dc5209a8cb",
    "observation_hash": "4f8eefa53cb2",
    "config_hash": "87c003aa6cae",
    "tier": "proxy_fields",
}


def _flat(**extra):
    base = {
        "run_id": "v3_exq_9999_probe_20260917T101112Z_v3",
        "status": "PASS",
        "timestamp_utc": "20260917T101112Z",
        "claim_ids_tested": ["MECH-999"],
    }
    base.update(extra)
    return base


def _env(flat):
    manifest, _, _ = build_runpack_docs(flat, "v3_exq_9999_probe")
    return manifest["environment"]


def test_absent_environment_asserts_nothing():
    env = _env(_flat())
    assert env == {f: "unknown" for f in ENV_FIELDS}, env


def test_the_fabricated_literal_is_gone():
    env = _env(_flat())
    for field, bad in FABRICATED.items():
        assert env[field] != bad, (
            "%s is back to the pre-2026-09-17 hardcoded value %r, which asserted "
            "a non-existent environment class for every pack" % (field, bad)
        )


def test_real_environment_is_carried_verbatim():
    assert _env(_flat(environment=dict(REAL))) == REAL


def test_partial_environment_merges_field_by_field():
    """A flat carrying only some fields contributes those; the rest stay honestly
    "unknown" rather than the whole block vanishing."""
    env = _env(_flat(environment={"env_id": "ree.causal_grid_world",
                                  "config_hash": "abc123abc123"}))
    assert env["env_id"] == "ree.causal_grid_world"
    assert env["config_hash"] == "abc123abc123"
    assert env["dynamics_hash"] == "unknown"
    assert env["tier"] == "unknown"


def test_blank_and_none_values_are_not_assertions():
    env = _env(_flat(environment={"env_id": "   ", "tier": None,
                                  "config_hash": "abc123abc123"}))
    assert env["env_id"] == "unknown"
    assert env["tier"] == "unknown"
    assert env["config_hash"] == "abc123abc123"


def test_malformed_environment_is_ignored():
    for bad in ("not-a-dict", [], None, 7):
        env = _env(_flat(environment=bad))
        assert env == {f: "unknown" for f in ENV_FIELDS}, bad


def test_carried_values_are_stringified():
    env = _env(_flat(environment={"config_hash": 12345}))
    assert env["config_hash"] == "12345"


def test_carry_does_not_mutate_the_caller_flat():
    """build_runpack_docs is a pure projection; the coordinator reuses the flat
    dict it was handed (sync_daemon._materialize_runpacks)."""
    supplied = dict(REAL)
    flat = _flat(environment=supplied)
    _env(flat)
    assert supplied == REAL
    assert flat["environment"] == REAL


def test_converter_literal_matches_pack_writer_default():
    """The two writers must agree byte-for-byte on the honest default.

    They diverging is how one of them came to be the only place the fabrication
    lived. Skipped, not failed, where ree-v3 is not importable -- remote_pytest.sh
    stages ree-v3 only, so this test's home is the REE_assembly side and the
    cross-repo import is a bonus check on the Mac.
    """
    for candidate in (
        Path(__file__).resolve().parents[4] / "ree-v3",
        Path("/Users/dgolden/REE_Working/ree-v3"),
    ):
        if (candidate / "experiments" / "pack_writer.py").is_file():
            sys.path.insert(0, str(candidate))
            from experiments.pack_writer import DEFAULT_ENVIRONMENT  # noqa: E402
            assert DEFAULT_ENVIRONMENT == _env(_flat()), (
                "pack_writer.DEFAULT_ENVIRONMENT and this converter's literal "
                "have drifted apart"
            )
            return
    print("SKIP test_converter_literal_matches_pack_writer_default (ree-v3 absent)")


if __name__ == "__main__":
    import traceback

    failures = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"PASS {name}")
            except Exception:
                failures += 1
                print(f"FAIL {name}")
                traceback.print_exc()
    print(f"\n{'OK' if not failures else str(failures) + ' FAILURE(S)'}")
    sys.exit(1 if failures else 0)
