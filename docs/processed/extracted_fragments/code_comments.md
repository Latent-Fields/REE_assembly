# Extracted Fragments: Code Comments and Docstrings

These excerpts are preserved verbatim from code files that include REE-related descriptive text.

---

## src/cathedral.py (README template excerpt)

Source: `src/cathedral.py` lines 35-55

~~~
# REE Cathedral (Executable Reference)

This repository is an executable scaffold for the **Reflective-Ethical Engine (REE)**.
The canonical architecture is defined in `REE_CORE.md` (copied from your spec repo).

What runs here:
- an explicit online loop (sense → latent update → rollout candidates → score → select → act → update residue)
- a persistent residue field (dent geometry)
- mirror-modelling-based other-harm contribution
- offline “sleep” consolidation (dent compression + precision recalibration)

## Quickstart
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
python examples/run_toy.py
pytest -q
```
~~~

---

## src/cathedral.py (module docstring excerpt)

Source: `src/cathedral.py` lines 82-87

~~~
"""REE executable scaffold.

The goal is not to claim biological realism, but to provide
a faithful, runnable implementation of the loop specified in `REE_CORE.md`.
"""
~~~
