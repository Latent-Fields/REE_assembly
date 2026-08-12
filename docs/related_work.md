---
title: Related Work
nav_order: 9
---

# Related Latent-Fields Work

<div class="ree-doc-intro">
  <p class="ree-eyebrow">Research programme map</p>
  <p class="ree-doc-lead">REE Assembly is one part of the Latent-Fields public research record. The projects below have different purposes and maturity; their labels are intentionally explicit.</p>
</div>

<div class="ree-project-grid">
{% for project in site.data.public_projects %}
  <article class="ree-project-card">
    <div class="ree-project-card-topline">
      <p class="ree-project-status">{{ project.status }}</p>
      <a class="ree-project-repo" href="https://github.com/{{ project.repository }}">Repository</a>
    </div>
    <h2>{{ project.name }}</h2>
    <p>{{ project.summary }}</p>
    <p class="ree-project-note">{{ project.note }}</p>
    <div class="ree-project-links">
      <a href="https://github.com/{{ project.repository }}">Open source record</a>
      {% if project.website != "" %}<a href="{{ project.website }}">Open project site</a>{% endif %}
    </div>
  </article>
{% endfor %}
</div>

The organisation-level public site is being established as the shared front door.
Until then, repository links remain the canonical source for project-level history
and implementation detail.
