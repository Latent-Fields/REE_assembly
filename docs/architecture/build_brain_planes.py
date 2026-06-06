#!/usr/bin/env python3
"""Generate the three linked brain-plane SVGs (sagittal / coronal / axial) for the
REE brain map from a single region table.

Each region is placed in the plane(s) where it is anatomically visible; naturally
bilateral structures are rendered as symmetric L/R pairs. Region elements carry
data-region="<id>" (and namespaced ids <plane>_region_<id>) so brain_map.html can
fill / select a region across every plane it appears in.

Functional analogy only -- not biological homology. Run from this directory:
    /opt/local/bin/python3 build_brain_planes.py
Re-run after editing REGIONS / placements; commit the emitted *.svg files.
"""
import base64
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# (image file, viewBox W, viewBox H) -- image is drawn at 0,0 filling the viewBox,
# so region coords below are in source-pixel space for that plane.
PLANES = {
    "sagittal": {"img": "brain_sagittal.jpg", "w": 690, "h": 630,
                 "label": "Sagittal (midline)", "credit": "(c) O. Stollmann, Wikimedia, CC-attribution"},
    "coronal":  {"img": "brain_coronal.jpg",  "w": 600, "h": 500,
                 "label": "Coronal (thalamus)", "credit": "(c) 511KeV, Wikimedia, CC BY-SA 4.0"},
    "axial":    {"img": "brain_axial.jpg",    "w": 418, "h": 520,
                 "label": "Axial (basal ganglia)", "credit": "(c) Novaksean, Wikimedia, CC BY-SA 4.0"},
}

GHOST = {"ghost_insula", "ghost_language", "ghost_cerebellum"}

# large diffuse fields kept faint so they don't swamp the discrete nuclei
OPACITY = {"astrocyte": 0.38, "default_mode": 0.55, "harm_stream": 0.65}

# Per-region placement. value = {plane: [ (cx,cy,rx,ry), ... ]}  (>1 blob = bilateral)
# Sagittal/axial coords are in their source-pixel viewBox (anterior: sagittal=left,
# axial=top). The sagittal backdrop was re-cropped 2026-06-06 from the same
# O. Stollmann 900x900 original to include the frontal pole (now 690x630, was
# 522x560); the prior coords were shifted +90 x / +10 y to track the new window.
# CORONAL coords are kept in the legacy 420x520 layout space (image at
# x=-70 y=13 w=560 h=467) -- reused verbatim from the prior single-plane map -- and
# transformed to the 600x500 plane viewBox by _coronal_xform() at build time.
REGIONS = {
    "pfc": {
        "sagittal": [(193, 188, 78, 52)],
        "axial":    [(205, 82, 82, 44)],
    },
    "motor": {
        "sagittal": [(345, 102, 40, 28)],
        "coronal":  [(262, 98, 30, 22)],
        "axial":    [(150, 132, 36, 20), (262, 132, 36, 20)],
    },
    "cingulate": {
        "sagittal": [(306, 188, 82, 24)],
        "coronal":  [(210, 162, 48, 18)],
        "axial":    [(205, 136, 40, 20)],
    },
    "default_mode": {
        "sagittal": [(338, 245, 96, 56)],
        "coronal":  [(210, 206, 28, 56)],
        "axial":    [(205, 250, 42, 120)],
    },
    "astrocyte": {
        "sagittal": [(340, 295, 100, 92)],
        "coronal":  [(210, 262, 78, 66)],
        "axial":    [(205, 255, 112, 120)],
    },
    "basal_ganglia": {
        "coronal": [(150, 228, 26, 30), (270, 228, 26, 30)],
        "axial":   [(150, 182, 34, 40), (266, 182, 34, 40)],
    },
    "thalamus": {
        "sagittal": [(345, 315, 30, 26)],
        "coronal":  [(193, 264, 15, 16), (227, 264, 15, 16)],
        "axial":    [(180, 235, 28, 30), (238, 235, 28, 30)],
    },
    "sleep": {
        "sagittal": [(338, 348, 22, 18)],
        "coronal":  [(210, 300, 24, 18)],
    },
    "neuromodulation": {
        "sagittal": [(335, 388, 20, 22)],
        "coronal":  [(210, 345, 20, 22)],
    },
    "amygdala": {
        "coronal": [(152, 330, 15, 13), (268, 330, 15, 13)],
        "axial":   [(160, 255, 18, 16), (256, 255, 18, 16)],
    },
    "hippocampus": {
        "coronal": [(135, 360, 24, 17), (285, 360, 24, 17)],
        "axial":   [(152, 286, 28, 22), (266, 286, 28, 22)],
    },
    "pag": {
        "sagittal": [(352, 352, 18, 20)],
        "coronal":  [(210, 372, 19, 22)],
        "axial":    [(209, 276, 20, 22)],
    },
    "respiratory": {
        "sagittal": [(318, 458, 22, 16)],
        "coronal":  [(210, 430, 24, 15)],
    },
    "harm_stream": {
        "coronal": [(318, 258, 14, 46)],
        "axial":   [(320, 235, 16, 46)],
    },
    "tpj": {
        "coronal": [(314, 150, 19, 13)],
        "axial":   [(312, 330, 24, 18)],
    },
    "peripersonal_space": {
        "coronal": [(74, 252, 16, 20)],
        "axial":   [(95, 320, 20, 24)],
    },
    "visual_streams": {
        "sagittal": [(525, 285, 30, 40)],
        "axial":    [(205, 446, 60, 40)],
    },
    # --- ghost / out-of-scope ---
    "ghost_insula": {
        "coronal": [(92, 272, 14, 20), (328, 272, 14, 20)],
        "axial":   [(110, 205, 16, 30), (308, 205, 16, 30)],
    },
    "ghost_language": {
        "coronal": [(86, 208, 20, 18)],
        "axial":   [(95, 250, 22, 20)],
    },
    "ghost_cerebellum": {
        "sagittal": [(462, 426, 50, 42)],
        "coronal":  [(210, 462, 46, 17)],
    },
}


def _coronal_xform(blob):
    """legacy 420x520 layout (image at x=-70,y=13,w=560,h=467) -> 600x500 plane viewBox."""
    cx, cy, rx, ry = blob
    sx, sy = 600 / 560.0, 500 / 467.0
    return ((cx + 70) * sx, (cy - 13) * sy, rx * sx, ry * sy)


def ellipse_path(cx, cy, rx, ry):
    return (f"M {cx-rx:.1f} {cy:.1f} a {rx:.1f} {ry:.1f} 0 1 0 {2*rx:.1f} 0 "
            f"a {rx:.1f} {ry:.1f} 0 1 0 {-2*rx:.1f} 0 Z")


def region_svg(plane, rid, blobs):
    eid = f"{plane}_region_{rid}"
    cls = "brain-region ghost" if rid in GHOST else "brain-region"
    ghost_attrs = ""
    if rid in GHOST:
        ghost_attrs = (' fill="url(#ghost_hatch)" fill-opacity="0.3" '
                       'stroke="#6e7681" stroke-width="1" stroke-dasharray="4 3"')
    op = f' opacity="{OPACITY[rid]}"' if rid in OPACITY else ""
    if len(blobs) == 1 and rid not in GHOST:
        cx, cy, rx, ry = blobs[0]
        return (f'  <ellipse id="{eid}" class="{cls}" data-region="{rid}"{op} '
                f'cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}"/>')
    d = " ".join(ellipse_path(*b) for b in blobs)
    return (f'  <path id="{eid}" class="{cls}" data-region="{rid}"{ghost_attrs}{op} d="{d}"/>')


def build_plane(plane, cfg):
    img_path = os.path.join(HERE, cfg["img"])
    b64 = base64.b64encode(open(img_path, "rb").read()).decode()
    W, H = cfg["w"], cfg["h"]
    # order: diffuse fields first (painted behind), then nuclei, then ghosts
    order = ["default_mode", "astrocyte", "pfc", "motor", "cingulate", "tpj",
             "basal_ganglia", "thalamus", "sleep", "neuromodulation",
             "amygdala", "hippocampus", "pag", "respiratory", "harm_stream",
             "peripersonal_space", "visual_streams",
             "ghost_insula", "ghost_language", "ghost_cerebellum"]
    parts = []
    for rid in order:
        blobs = REGIONS.get(rid, {}).get(plane)
        if blobs:
            if plane == "coronal":
                blobs = [_coronal_xform(b) for b in blobs]
            parts.append(region_svg(plane, rid, blobs))
    regions_svg = "\n".join(parts)
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<!-- GENERATED by build_brain_planes.py (do not hand-edit; edit the generator + re-run).
     {plane.capitalize()} plane. Ghosted real MRI backdrop {cfg['credit']}.
     Functional analogy, not homology. -->
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid meet"
     role="img" aria-label="REE brain map {plane} plane">
  <defs>
    <pattern id="ghost_hatch" patternUnits="userSpaceOnUse" width="8" height="8" patternTransform="rotate(45)">
      <line x1="0" y1="0" x2="0" y2="8" stroke="#484f58" stroke-width="2"/>
    </pattern>
    <filter id="mri_ghost" x="-5%" y="-5%" width="110%" height="110%" color-interpolation-filters="sRGB">
      <feColorMatrix in="SourceGraphic" type="matrix"
        values="0 0 0 0 0.52
                0 0 0 0 0.63
                0 0 0 0 0.80
                0.30 0.59 0.11 0 0"/>
      <feComponentTransfer><feFuncA type="gamma" amplitude="1" exponent="1.8" offset="0"/></feComponentTransfer>
    </filter>
  </defs>
  <g id="anatomy_backdrop" pointer-events="none" opacity="0.8">
    <image x="0" y="0" width="{W}" height="{H}" filter="url(#mri_ghost)"
      xlink:href="data:image/jpeg;base64,{b64}" href="data:image/jpeg;base64,{b64}"/>
  </g>
{regions_svg}
</svg>
'''


def main():
    for plane, cfg in PLANES.items():
        out = os.path.join(HERE, f"brain_plane_{plane}.svg")
        open(out, "w").write(build_plane(plane, cfg))
        print(f"wrote {out} ({os.path.getsize(out)//1024} KB)")


if __name__ == "__main__":
    main()
