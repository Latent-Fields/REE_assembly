---
title: Development Map
nav_exclude: true
---

<link rel="stylesheet" href="{{ '/assets/css/development-map.css?v=2' | relative_url }}">

<div
  id="ree-development-map"
  class="ree-development-map"
  data-source="{{ '/assets/data/development_map.v1.json' | relative_url }}"
  data-explorer="{{ '/public_explorer/' | relative_url }}"
  data-archive="{{ '/roadmap.html' | relative_url }}"
>
  <section class="development-map-hero" aria-labelledby="development-map-title">
    <p class="development-map-eyebrow">Public research record</p>
    <h1 id="development-map-title">REE Development Map</h1>
    <p class="development-map-intro">A readable projection of current questions, recorded work, and conditional future directions. It is generated from the repository's public evidence records rather than maintained as a separate narrative.</p>
    <p class="development-map-disclosure">REE is a research programme. No material presented here has been accepted for peer-reviewed publication; recorded implementation and experimental activity are not scientific validation. <a href="{{ '/research_status.html' | relative_url }}">Read the research-status note.</a></p>
  </section>

  <section class="development-map-section" aria-labelledby="frontier-title">
    <div class="development-map-section-heading">
      <p class="development-map-kicker">Present</p>
      <h2 id="frontier-title">Current frontier</h2>
    </div>
    <div id="development-map-frontier" class="development-map-loading" aria-live="polite">Loading the current repository projection.</div>
  </section>

  <section class="development-map-section" aria-labelledby="map-title">
    <div class="development-map-section-heading">
      <p class="development-map-kicker">Development record</p>
      <h2 id="map-title">Programme map</h2>
      <p>Open a lane to inspect its public records. A status is a record state, not a measure of scientific truth or programme completion.</p>
    </div>
    <div id="development-map-rail" class="development-map-rail" aria-label="Programme lanes"></div>
    <div id="development-map-controls" class="development-map-controls" aria-label="Filter development records"></div>
    <div id="development-map-tracks" class="development-map-tracks"></div>
  </section>

  <section class="development-map-section development-map-archive" aria-labelledby="archive-title">
    <div class="development-map-section-heading">
      <p class="development-map-kicker">History</p>
      <h2 id="archive-title">Operational archive</h2>
      <p>The detailed snapshots remain intact. This map provides orientation; the archive preserves the daily operational record and source context.</p>
    </div>
    <div id="development-map-archive" class="development-map-loading"></div>
  </section>

  <noscript>
    <p>This interactive map needs JavaScript. The <a href="{{ '/CURRENT_FRONT.html' | relative_url }}">current front</a> and <a href="{{ '/roadmap.html' | relative_url }}">operational archive</a> remain available without it.</p>
  </noscript>
</div>

<script src="{{ '/assets/js/development-map.js?v=2' | relative_url }}"></script>
