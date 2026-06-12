import re, pathlib
src = pathlib.Path("/Users/dgolden/REE_Working/REE_assembly/docs/architecture/brain_map_sagittal.svg")
dst = pathlib.Path("/Users/dgolden/REE_Working/REE_assembly/docs/architecture/brain_map_sagittal_static.svg")
svg = src.read_text(encoding="utf-8")

# Functional-family colouring (the live page overlays claim/evidence data via the API;
# this static copy uses a fixed functional palette so it renders standalone on Pages).
families = {
    "#cfe2f3": ["pfc","cingulate","motor","visual_streams","tpj","default_mode","peripersonal_space"],  # E1 cortical/association
    "#fce5b6": ["basal_ganglia","thalamus"],                                                              # E3 commitment/gate
    "#cfead0": ["hippocampus"],                                                                           # hippocampal rollout
    "#f4cccc": ["amygdala","pag","harm_stream"],                                                          # affect / harm
    "#e0d3f0": ["neuromodulation","astrocyte","respiratory","sleep"],                                     # neuromodulatory / regulatory
}
rules = [".brain-region{stroke:#5a6066;stroke-width:1;fill:#e6e6e6;}",
         ".brain-region:hover{opacity:.85;}",
         ".eng-label{font-family:-apple-system,Segoe UI,Roboto,sans-serif;}"]
for colour, regs in families.items():
    for r in regs:
        rules.append(f"#region_{r}{{fill:{colour};}}")
style = "\n  <style>\n    " + "\n    ".join(rules) + "\n  </style>"

# Insert the style block immediately after the opening <svg ...> tag.
m = re.search(r"<svg\b[^>]*>", svg)
assert m, "no <svg> open tag found"
out = svg[:m.end()] + style + svg[m.end():]
# Mark provenance.
out = out.replace("<?xml version=\"1.0\" encoding=\"UTF-8\"?>",
    "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!-- DERIVED from brain_map_sagittal.svg: self-contained static copy with a fixed functional palette for GitHub Pages (no serve.py API overlay). Regenerate: python3 scripts/build_static_brain_map.py -->", 1)
dst.write_text(out, encoding="utf-8")
print("wrote", dst.relative_to(pathlib.Path("/Users/dgolden/REE_Working/REE_assembly")), len(out), "bytes")
print("style rules:", len(rules))
