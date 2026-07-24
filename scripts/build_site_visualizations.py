#!/usr/bin/env python3
"""Generate static GitHub Pages copies of the Brain Map and Fishtank visualizations.

The live pages (``brain_map.html``, ``fishtank_viz.html``) are served by
``serve.py`` and depend on two dynamic API endpoints:

  * ``GET /api/brain-map``      -> serve.py:read_brain_map()  (pure function of static files)
  * ``GET /api/fishtank/logs``  -> glob of evidence/experiments/**/*_episode_log.json

This script derives static, baseurl-relative copies into ``docs/`` so the
visualizations work on the published Jekyll site (latent-fields.github.io/REE_assembly)
with no backend:

  docs/brain_map/index.html            <- brain_map.html, data URLs rewritten
  docs/assets/data/brain_map.json      <- snapshot of /api/brain-map
  docs/fishtank/index.html             <- fishtank_viz.html, data URLs rewritten
  docs/assets/fishtank/<run>.json      <- curated showcase episode logs (copied)
  docs/assets/fishtank/fishtank_runs.json <- static run index (shape of /api/fishtank/logs)

The brain plane SVGs and 3D JSON already live under docs/architecture/ and are
reused as-is. The live pages remain the single source of truth -- re-run this
script after editing them.

Re-runnable and idempotent. ASCII-only stdout (Windows cp1252 safe).
"""

import importlib.util
import json
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent  # REE_assembly/
DOCS = REPO / "docs"

# serve.py does `import graceful_timeout` at module scope; that module lives in
# REPO, not scripts/. Running this file as `python3 scripts/build_site_visualizations.py`
# puts scripts/ (not REPO) at sys.path[0], so serve.py's import fails unless REPO
# is on sys.path before it is loaded via spec_from_file_location below.
sys.path.insert(0, str(REPO))

# Curated showcase runs (experiment dir names). Small, built to be watched.
# Deliberately excludes the 16-37 MB ablation logs (223 minimal_vertebrate, 483*).
SHOWCASE_RUNS = [
    "v3_exq_471_best_agent_fishtank_showcase",
    "v3_exq_524_reef_fishtank_showcase",
    "v3_exq_475_sd036_decay_unlocks_exq471",
    "v3_exq_223a_toroidal_minimal_vertebrate",
]

# Human-friendly labels for the run picker (keyed by experiment dir name).
RUN_LABELS = {
    "v3_exq_471_best_agent_fishtank_showcase": "Best agent (EXQ-471 showcase)",
    "v3_exq_524_reef_fishtank_showcase": "Reef navigation (EXQ-524 showcase)",
    "v3_exq_475_sd036_decay_unlocks_exq471": "SD-036 decay unlock (EXQ-475)",
    "v3_exq_223a_toroidal_minimal_vertebrate": "Toroidal minimal vertebrate (EXQ-223a)",
}


def _replace(text, old, new, label, exact=None):
    """Replace ``old`` with ``new``, asserting the occurrence count.

    ``exact`` -- if given, require precisely that many occurrences; otherwise
    require at least one. Fails loudly so a future edit to a source page that
    moves a fetch breaks the build instead of silently shipping a broken page.
    """
    n = text.count(old)
    if exact is not None:
        if n != exact:
            raise SystemExit(
                "REWRITE ERROR [%s]: expected %d occurrence(s) of %r, found %d"
                % (label, exact, old, n)
            )
    elif n < 1:
        raise SystemExit(
            "REWRITE ERROR [%s]: expected >=1 occurrence of %r, found 0"
            % (label, old)
        )
    print("  rewrite [%s]: %d occurrence(s)" % (label, n))
    return text.replace(old, new)


def build_brain_map():
    print("Brain Map:")
    # 1. Snapshot /api/brain-map by importing serve.read_brain_map().
    spec = importlib.util.spec_from_file_location("ree_serve", REPO / "serve.py")
    serve = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(serve)
    payload = serve.read_brain_map()
    n_regions = len(payload.get("regions") or [])
    if n_regions == 0:
        raise SystemExit("BRAIN ERROR: read_brain_map() returned 0 regions")
    out_json = DOCS / "assets" / "data" / "brain_map.json"
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")
    print("  wrote %s (%d regions, %d engineering nodes)"
          % (out_json.relative_to(REPO), n_regions, len(payload.get("engineering_nodes") or [])))

    # 2. Derive docs/brain_map/index.html from brain_map.html.
    src = (REPO / "brain_map.html").read_text(encoding="utf-8")
    # 2a. Data source: API -> static snapshot.
    src = _replace(
        src,
        'fetch("/api/brain-map?t=" + Date.now(), { cache: "no-store" })',
        'fetch("../assets/data/brain_map.json", { cache: "no-store" })',
        "brain api -> static json", exact=1,
    )
    # 2b. Header + inspector links: serve.py routes -> published static targets.
    #     Do the founder link before the broad /docs/architecture rule so it
    #     resolves to the Jekyll-built .html, not the raw .md.
    src = _replace(src,
                   'href="/docs/architecture/founder_ontology.md"',
                   'href="../architecture/founder_ontology.html"',
                   "brain founder-ontology link", exact=1)
    src = _replace(src, 'href="/explorer.html"', 'href="../public_explorer/"',
                   "brain header explorer link", exact=1)
    src = _replace(src, 'href="/closure"', 'href="../closure_dashboard.html"',
                   "brain header closure link", exact=1)
    # Inspector "Docs" list -> GitHub blob so any repo-relative path resolves.
    src = _replace(src,
                   "'<li><a href=\"/' + esc(d)",
                   "'<li><a href=\"https://github.com/Latent-Fields/REE_assembly/blob/master/' + esc(d)",
                   "brain inspector doc links -> github", exact=1)
    # Inspector claim links -> public explorer (anchor harmless if unsupported).
    src = _replace(src, 'href="/explorer.html#claim-', 'href="../public_explorer/#claim-',
                   "brain inspector claim links -> public explorer", exact=1)
    # 2c. Remaining static asset fetches (3D JSON + plane SVGs), now exactly 2.
    src = _replace(src, '"/docs/architecture/', '"../architecture/',
                   "brain static asset fetches -> ../architecture", exact=2)
    out_html = DOCS / "brain_map" / "index.html"
    out_html.parent.mkdir(parents=True, exist_ok=True)
    out_html.write_text(src, encoding="utf-8")
    print("  wrote %s" % out_html.relative_to(REPO))


def build_fishtank():
    print("Fishtank:")
    fish_dir = DOCS / "assets" / "fishtank"
    fish_dir.mkdir(parents=True, exist_ok=True)
    exp_root = REPO / "evidence" / "experiments"

    # 1. Copy curated showcase logs + build the static run index.
    logs_index = []
    for run in SHOWCASE_RUNS:
        run_dir = exp_root / run
        matches = sorted(run_dir.glob("*_episode_log.json"), reverse=True)
        if not matches:
            print("  WARNING: no episode log for %s -- skipping" % run)
            continue
        src_log = matches[0]  # most recent, mirrors /api/fishtank/logs ordering
        dst_log = fish_dir / (run + ".json")
        shutil.copyfile(src_log, dst_log)
        kb = dst_log.stat().st_size // 1024
        stem = src_log.stem.replace("_episode_log", "")
        logs_index.append({
            "experiment": run,
            "run": stem,
            "label": RUN_LABELS.get(run, run),
            # page lives at docs/fishtank/index.html -> assets is one level up.
            "path": "../assets/fishtank/" + run + ".json",
        })
        print("  copied %s (%d KB)" % (dst_log.relative_to(REPO), kb))

    if not logs_index:
        raise SystemExit("FISHTANK ERROR: no showcase logs copied")
    index_path = fish_dir / "fishtank_runs.json"
    index_path.write_text(json.dumps({"logs": logs_index}, indent=2), encoding="utf-8")
    print("  wrote %s (%d runs)" % (index_path.relative_to(REPO), len(logs_index)))

    # 2. Derive docs/fishtank/index.html from fishtank_viz.html.
    src = (REPO / "fishtank_viz.html").read_text(encoding="utf-8")
    src = _replace(src,
                   "fetch('/api/fishtank/logs')",
                   "fetch('../assets/fishtank/fishtank_runs.json')",
                   "fishtank api -> static index", exact=1)
    # Picker "Watch": stay on this page, just set ?log=.
    src = _replace(src,
                   "window.location.href = '/fishtank_viz.html?log=' + encodeURIComponent(path);",
                   "window.location.href = '?log=' + encodeURIComponent(path);",
                   "picker watch -> relative ?log", exact=1)
    # In-app browse: path is already page-relative in the static index.
    src = _replace(src,
                   "fetch('/' + path).then(r => r.json()).then(data => loadData(data))",
                   "fetch(path).then(r => r.json()).then(data => loadData(data))",
                   "browse fetch -> relative path", exact=1)
    # ?log= handler: use the (page-relative) value as-is.
    src = _replace(src,
                   "const url = logPath.startsWith('/') ? logPath : '/' + logPath;",
                   "const url = logPath;",
                   "?log handler -> relative path", exact=1)
    out_html = DOCS / "fishtank" / "index.html"
    out_html.parent.mkdir(parents=True, exist_ok=True)
    out_html.write_text(src, encoding="utf-8")
    print("  wrote %s" % out_html.relative_to(REPO))


def build_progress():
    """Snapshot serve.read_progress() (the Scientific Progress Dashboard payload)
    to docs/assets/data/progress.v1.json for the static Pages mirror. read_progress()
    is a pure read of the committed hypothesis_space.v1.json -- no server bind. The
    payload is derive-only; this mirror never re-weights closure."""
    print("Progress dashboard:")
    spec = importlib.util.spec_from_file_location("ree_serve_progress", REPO / "serve.py")
    serve = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(serve)
    payload = serve.read_progress()
    out_json = DOCS / "assets" / "data" / "progress.v1.json"
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")
    if payload.get("empty"):
        print("  wrote %s (EMPTY -- run build_hypothesis_space.py first)"
              % out_json.relative_to(REPO))
    else:
        n = payload.get("needles", {})
        print("  wrote %s (build=%s%% prove=%s%% surviving=%s/%s ready=%s)"
              % (out_json.relative_to(REPO),
                 round((n.get("build", {}).get("fraction_built") or 0) * 100, 1),
                 n.get("prove", {}).get("closure_pct"),
                 n.get("narrow", {}).get("total_surviving"),
                 n.get("narrow", {}).get("total_initial"),
                 n.get("decide", {}).get("ready")))


def main():
    print("Building static site visualizations into docs/ ...")
    build_brain_map()
    build_fishtank()
    build_progress()
    print("Done.")


if __name__ == "__main__":
    main()
