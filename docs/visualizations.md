---
title: Visualizations
nav_order: 13
---

# Visualizations

Two interactive views into the REE substrate. Both run entirely in your browser
from static snapshots of the project data -- no server required.

> **A note for readers.** These are research instruments, not curated explainers.
> The brain map reflects computational roles named after neuroscience, not
> anatomical claims; the fishtank replays raw agent episodes from experiment
> runs. Interpretive, per-run commentary will be added over time (see
> *Interpretive notes* below). For now, treat them as a window onto how the
> system is actually built and how trained agents actually behave.

<div style="display:flex;flex-wrap:wrap;gap:24px;margin-top:24px">

  <div style="flex:1 1 300px;border:1px solid #d0d7de;border-radius:10px;overflow:hidden">
    <a href="{{ '/brain_map/' | relative_url }}" style="text-decoration:none;color:inherit">
      <img src="{{ '/architecture/brain_map_sagittal_static.svg' | relative_url }}"
           alt="REE brain map preview"
           style="width:100%;display:block;background:#0d1117"/>
    </a>
    <div style="padding:14px">
      <h3 style="margin:0 0 6px">Brain Map</h3>
      <p style="margin:0 0 12px;font-size:14px;color:#57606a">
        Computational roles laid out across three co-registered MNI planes plus a
        rotatable 3D view. Each region is annotated with its claims, substrate
        implementation status, and experiment evidence. Click a region to inspect.
      </p>
      <a href="{{ '/brain_map/' | relative_url }}"
         style="display:inline-block;padding:8px 16px;background:#0969da;color:#fff;border-radius:6px;text-decoration:none;font-size:14px">
        Open Brain Map &nearr;</a>
    </div>
  </div>

  <div style="flex:1 1 300px;border:1px solid #d0d7de;border-radius:10px;overflow:hidden">
    <a href="{{ '/fishtank/' | relative_url }}" style="text-decoration:none;color:inherit">
      <img src="{{ '/assets/img/fishtank_preview.svg' | relative_url }}"
           alt="REE fishtank preview"
           style="width:100%;display:block;background:#0d1117"/>
    </a>
    <div style="padding:14px">
      <h3 style="margin:0 0 6px">Fishtank</h3>
      <p style="margin:0 0 12px;font-size:14px;color:#57606a">
        An animated replay of a trained agent navigating its environment --
        seeking food, evading hazards -- with its internal vitals, affect, and
        cognition traced step by step. Pick a showcase run, or drag in your own
        episode log.
      </p>
      <a href="{{ '/fishtank/' | relative_url }}"
         style="display:inline-block;padding:8px 16px;background:#0969da;color:#fff;border-radius:6px;text-decoration:none;font-size:14px">
        Open Fishtank &nearr;</a>
    </div>
  </div>

</div>

## Interpretive notes

*Coming soon.* Curated, plain-language commentary on what each showcase run
demonstrates and how to read the brain-map coverage tiers will be added here.
