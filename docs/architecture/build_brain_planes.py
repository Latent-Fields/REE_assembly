#!/usr/bin/env python3
"""Generate the three co-registered brain-plane SVGs (sagittal / coronal / axial)
for the REE brain map.

2026-06-06 rebuild: the three backdrops are now slices of ONE template volume
(TemplateFlow tpl-MNI152NLin2009cAsym, res-01, 1 mm, ICBM 152) cut at fixed
voxel indices. Because the planes share a single voxel grid, the views are
co-registered by construction -- coronal/axial share the left-right (X) voxel
count and coronal/sagittal share the superior-inferior (Z) voxel count, so the
orthographic projection in brain_map.html lines up to the pixel.

Each region is defined ONCE as an ellipsoid in MNI millimetre space and
projected into every plane it is shown in, so a structure's position is
consistent across all three views (real orthographic tracing, not three
independently-placed drawings). `planes` curates which views a region appears
in; the (cx, cy, rx, ry) of each blob is computed from the 3D centre.

  Run:  /opt/local/bin/python3 build_brain_planes.py

Functional analogy, not homology -- colours/coverage are applied by the page.
"""
import os
import json
import base64

HERE = os.path.dirname(os.path.abspath(__file__))

# brain hull ellipsoid (MNI mm) used by the 3D view as anatomical context
HULL = {"center": [0, -17, 12], "semi": [72, 90, 64]}

# --- volume geometry (MNI152 1 mm, RAS+, affine is identity + translation) ---
# voxel index = mm + OFF along each axis: i = x+96 (R), j = y+132 (A), k = z+78 (S)
NX, NY, NZ = 193, 229, 193
OFF = (96, 132, 78)
# fixed voxel index sliced for each plane (sagittal x=0, coronal y=-18, axial z=+6)
SLICE_VOX = {"sagittal": 96, "coronal": 114, "axial": 84}
SLICE_MM = {"sagittal": ("x", 0), "coronal": ("y", -18), "axial": ("z", 6)}

CREDIT = "MNI152 template (TemplateFlow / ICBM 152), co-registered slices"
PLANES = {
    "sagittal": {"img": "brain_sagittal.jpg", "w": NY, "h": NZ,
                 "label": "Sagittal (x=0)", "credit": CREDIT},
    "coronal":  {"img": "brain_coronal.jpg",  "w": NX, "h": NZ,
                 "label": "Coronal (y=-18)", "credit": CREDIT},
    "axial":    {"img": "brain_axial.jpg",    "w": NX, "h": NY,
                 "label": "Axial (z=+6)", "credit": CREDIT},
}

GHOST = {"ghost_insula", "ghost_language", "ghost_cerebellum"}

# large diffuse fields kept faint so they don't swamp the discrete nuclei
OPACITY = {"astrocyte": 0.38, "default_mode": 0.55, "harm_stream": 0.65}

# Region model -- one ellipsoid in MNI mm: (x, y, z, rx, ry, rz).
# x:+right  y:+anterior  z:+superior. `bilateral` mirrors the blob across x=0
# (two blobs in coronal/axial; they coincide on the midline-sagittal slice).
# `planes` = curated coverage; positions are projected from the 3D centre so
# the same structure lands at consistent coordinates in every view it shows in.
REGIONS = {
    "pfc":            {"planes": ["sagittal", "axial"],            "blob": (0, 52, 8, 34, 16, 22)},
    "motor":          {"planes": ["sagittal", "coronal", "axial"], "blob": (10, -22, 58, 12, 14, 12), "bilateral": True},
    "cingulate":      {"planes": ["sagittal", "coronal", "axial"], "blob": (0, 8, 26, 8, 42, 16)},
    "default_mode":   {"planes": ["sagittal", "coronal", "axial"], "blob": (0, -48, 30, 12, 38, 28)},
    "astrocyte":      {"planes": ["sagittal", "coronal", "axial"], "blob": (0, -12, 18, 42, 52, 46)},
    "basal_ganglia":  {"planes": ["coronal", "axial"],             "blob": (22, 4, 4, 11, 15, 13), "bilateral": True},
    "thalamus":       {"planes": ["sagittal", "coronal", "axial"], "blob": (9, -18, 8, 8, 12, 9), "bilateral": True},
    "sleep":          {"planes": ["sagittal", "coronal"],          "blob": (0, -6, -8, 6, 8, 8)},
    "neuromodulation": {"planes": ["sagittal", "coronal"],         "blob": (0, -28, -20, 6, 10, 12)},
    "amygdala":       {"planes": ["coronal", "axial"],             "blob": (23, -4, -18, 8, 8, 7), "bilateral": True},
    "hippocampus":    {"planes": ["coronal", "axial"],             "blob": (28, -20, -12, 9, 14, 8), "bilateral": True},
    "pag":            {"planes": ["sagittal", "coronal", "axial"], "blob": (0, -30, -8, 5, 6, 8)},
    "respiratory":    {"planes": ["sagittal", "coronal"],          "blob": (0, -40, -48, 6, 8, 9)},
    "harm_stream":    {"planes": ["coronal", "axial"],             "blob": (40, -12, 8, 8, 34, 18)},
    "tpj":            {"planes": ["coronal", "axial"],             "blob": (52, -52, 26, 12, 14, 12)},
    "peripersonal_space": {"planes": ["coronal", "axial"],         "blob": (-48, -40, 46, 12, 16, 14)},
    "visual_streams": {"planes": ["sagittal", "axial"],            "blob": (0, -90, 4, 18, 16, 22)},
    # --- ghost / out-of-scope ---
    "ghost_insula":   {"planes": ["coronal", "axial"],             "blob": (38, 4, 2, 6, 12, 16), "bilateral": True},
    "ghost_language": {"planes": ["coronal"],                      "blob": (-52, 16, 16, 10, 12, 12)},
    "ghost_cerebellum": {"planes": ["sagittal"],                   "blob": (0, -66, -32, 24, 22, 18)},
}

# draw order: diffuse fields first (painted behind), then nuclei, then ghosts
ORDER = ["default_mode", "astrocyte", "pfc", "motor", "cingulate", "tpj",
         "basal_ganglia", "thalamus", "sleep", "neuromodulation",
         "amygdala", "hippocampus", "pag", "respiratory", "harm_stream",
         "peripersonal_space", "visual_streams",
         "ghost_insula", "ghost_language", "ghost_cerebellum"]


def project(plane, blob):
    """MNI-mm ellipsoid -> (cx, cy, rx, ry) in the plane's source-pixel viewBox.

    Pixel maps (voxel i=x+96, j=y+132, k=z+78):
      sagittal: cx = NY-1-j,  cy = NZ-1-k,  (rx,ry)=(ry_mm,rz_mm)
      coronal:  cx = i,       cy = NZ-1-k,  (rx,ry)=(rx_mm,rz_mm)
      axial:    cx = i,       cy = NY-1-j,  (rx,ry)=(rx_mm,ry_mm)
    """
    x, y, z, rx, ry, rz = blob
    i, j, k = x + OFF[0], y + OFF[1], z + OFF[2]
    if plane == "sagittal":
        return (NY - 1 - j, NZ - 1 - k, ry, rz)
    if plane == "coronal":
        return (i, NZ - 1 - k, rx, rz)
    return (i, NY - 1 - j, rx, ry)  # axial


def blobs_for(region, plane):
    base = region["blob"]
    raw = [base]
    if region.get("bilateral"):
        x, y, z, rx, ry, rz = base
        raw = [(x, y, z, rx, ry, rz), (-x, y, z, rx, ry, rz)]
    out, seen = [], set()
    for b in raw:
        p = project(plane, b)
        key = (round(p[0]), round(p[1]))  # dedupe coincident bilateral (sagittal)
        if key in seen:
            continue
        seen.add(key)
        out.append(p)
    return out


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
    parts = []
    for rid in ORDER:
        region = REGIONS.get(rid)
        if not region or plane not in region["planes"]:
            continue
        parts.append(region_svg(plane, rid, blobs_for(region, plane)))
    regions_svg = "\n".join(parts)
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<!-- GENERATED by build_brain_planes.py (do not hand-edit; edit the generator + re-run).
     {plane.capitalize()} plane. Backdrop: {cfg['credit']}.
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


def regions_3d():
    """Resolved 3D region geometry (MNI mm) for the lightweight 3D view in
    brain_map.html. Each region -> one or two spheres (bilateral mirrored across
    x=0); sphere radius is the mean of the ellipsoid radii. Colours/coverage are
    applied by the page from /api/brain-map, so only geometry is emitted here."""
    out = []
    for rid in ORDER:
        region = REGIONS.get(rid)
        if not region:
            continue
        x, y, z, rx, ry, rz = region["blob"]
        r = round((rx + ry + rz) / 3.0, 1)
        centers = [[x, y, z]]
        if region.get("bilateral"):
            centers = [[x, y, z], [-x, y, z]]
        out.append({"id": rid, "ghost": rid in GHOST,
                    "opacity": OPACITY.get(rid),
                    "spheres": [{"c": c, "r": r} for c in centers]})
    return out


if __name__ == "__main__":
    for plane, cfg in PLANES.items():
        out = os.path.join(HERE, f"brain_plane_{plane}.svg")
        open(out, "w").write(build_plane(plane, cfg))
        print(f"wrote {out} ({os.path.getsize(out)//1024} KB)")
    data = {"frame": "MNI152 1mm; x=R y=A z=S (mm)", "hull": HULL, "regions": regions_3d()}
    j = os.path.join(HERE, "brain_regions_3d.json")
    open(j, "w").write(json.dumps(data, indent=1))
    print(f"wrote {j} ({len(data['regions'])} regions)")
