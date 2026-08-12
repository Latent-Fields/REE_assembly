---
title: Visualizations
nav_order: 16
---

# Visualizations

<div class="ree-doc-intro">
  <p class="ree-eyebrow">Visual tools</p>
  <p class="ree-doc-lead">These browser-based views make parts of the REE research record inspectable. They are research instruments and static data views, not validated demonstrations or clinical models.</p>
</div>

<div class="ree-visual-grid">
  <article class="ree-visual-card">
    <a class="ree-visual-image" href="{{ '/brain_map/' | relative_url }}">
      <img src="{{ '/architecture/brain_map_sagittal_static.svg' | relative_url }}" alt="Preview of the REE brain map.">
    </a>
    <div class="ree-visual-card-body">
      <p class="ree-eyebrow">Architecture map</p>
      <h2>Brain Map</h2>
      <p>Computational roles laid out across three co-registered MNI planes and a rotatable 3D view. Regions link to claims, implementation status, and experiment evidence.</p>
      <a class="ree-inline-action" href="{{ '/brain_map/' | relative_url }}">Open Brain Map</a>
    </div>
  </article>

  <article class="ree-visual-card">
    <a class="ree-visual-image" href="{{ '/fishtank/' | relative_url }}">
      <img src="{{ '/assets/img/fishtank_preview.svg' | relative_url }}" alt="Preview of the REE Fishtank episode viewer.">
    </a>
    <div class="ree-visual-card-body">
      <p class="ree-eyebrow">Episode viewer</p>
      <h2>Fishtank</h2>
      <p>Animated replay of recorded agent episodes with internal state, affect, and cognition traced step by step. Use a showcase run or load a compatible episode log.</p>
      <a class="ree-inline-action" href="{{ '/fishtank/' | relative_url }}">Open Fishtank</a>
    </div>
  </article>
</div>

## Reading these views

The brain map uses neuroscience-inspired computational roles; it does not claim
that the visual arrangement is an anatomical validation. The Fishtank replays
bounded experiment data. In both cases, use linked claims and source records to
evaluate what a view can, and cannot, support.
