/**
 * claim-tooltips.js
 *
 * Finds all claim ID references (MECH-069, ARC-021, INV-003, etc.) in page text,
 * wraps them in <span class="claim-ref"> elements, and shows a hover tooltip card
 * with the claim type, subject, and status from claims.json.
 */

(function () {
  'use strict';

  const CLAIM_RE = /\b(INV|ARC|MECH|Q|IMPL|D)-\d{3}[a-z]?\b/g;
  const SKIP_TAGS = new Set(['CODE', 'PRE', 'SCRIPT', 'STYLE', 'A', 'HEAD']);
  const DATA_URL = document.currentScript
    ? new URL('../data/claims.json', document.currentScript.src).href
    : '/REE_assembly/assets/data/claims.json';

  let claims = {};       // id → {type, subject, status}
  let tooltip = null;    // the floating div
  let hideTimer = null;

  // ── Type labels ────────────────────────────────────────────────────────────
  const TYPE_LABEL = {
    invariant:                'invariant',
    architectural_commitment: 'architectural commitment',
    mechanism_hypothesis:     'mechanism hypothesis',
    open_question:            'open question',
    implementation_note:      'implementation note',
    design_decision:          'design decision',
  };

  // ── Subject formatting ─────────────────────────────────────────────────────
  function formatSubject(subject) {
    if (!subject) return { domain: '', topic: '' };
    const parts = subject.split('.');
    const domain = parts[0].replace(/_/g, ' ');
    const topic  = parts.slice(1).join(' › ').replace(/_/g, ' ') || domain;
    return { domain, topic };
  }

  // ── Build tooltip HTML ─────────────────────────────────────────────────────
  function buildTooltipHTML(id, claim) {
    const { domain, topic } = formatSubject(claim.subject);
    const typeLabel = TYPE_LABEL[claim.type] || claim.type.replace(/_/g, ' ');
    const statusClass = 's-' + (claim.status || 'unknown').replace(/[^a-z]/g, '');

    return `
      <div class="ct-header">
        <span class="ct-id">${id}</span>
        <span class="ct-type">${typeLabel}</span>
      </div>
      <div class="ct-topic">${topic}</div>
      <div class="ct-meta">${domain}<span class="ct-status ${statusClass}">${claim.status || '?'}</span></div>
    `.trim();
  }

  // ── Position tooltip near element ─────────────────────────────────────────
  function positionTooltip(el) {
    const rect = el.getBoundingClientRect();
    const vw   = window.innerWidth;
    const vh   = window.innerHeight;
    const tw   = Math.min(320, vw - 16);

    let left = rect.left;
    let top  = rect.bottom + 6;

    // Don't overflow right edge
    if (left + tw > vw - 8) left = vw - tw - 8;
    // Don't overflow bottom; flip above if needed
    if (top + 120 > vh) top = rect.top - 6 - 100;

    tooltip.style.left    = left + 'px';
    tooltip.style.top     = top  + 'px';
    tooltip.style.maxWidth = tw  + 'px';
  }

  // ── Show / hide ────────────────────────────────────────────────────────────
  function showTooltip(el) {
    clearTimeout(hideTimer);
    const id    = el.dataset.id;
    const claim = claims[id];
    if (!claim) return;

    tooltip.innerHTML = buildTooltipHTML(id, claim);
    tooltip.dataset.type = claim.type || '';
    positionTooltip(el);
    tooltip.style.display = 'block';
  }

  function hideTooltip() {
    hideTimer = setTimeout(() => { tooltip.style.display = 'none'; }, 80);
  }

  // ── Text node replacement ──────────────────────────────────────────────────
  function processTextNode(node) {
    const text = node.nodeValue;
    if (!CLAIM_RE.test(text)) return;
    CLAIM_RE.lastIndex = 0;

    const frag = document.createDocumentFragment();
    let last = 0;
    let match;

    while ((match = CLAIM_RE.exec(text)) !== null) {
      if (match.index > last) {
        frag.appendChild(document.createTextNode(text.slice(last, match.index)));
      }
      const span = document.createElement('span');
      span.className   = 'claim-ref';
      span.dataset.id  = match[0];
      span.textContent = match[0];
      // Only add interactivity if we actually have data for this claim
      if (claims[match[0]]) {
        span.addEventListener('mouseenter', () => showTooltip(span));
        span.addEventListener('mouseleave', hideTooltip);
      }
      frag.appendChild(span);
      last = CLAIM_RE.lastIndex;
    }

    if (last < text.length) {
      frag.appendChild(document.createTextNode(text.slice(last)));
    }

    node.parentNode.replaceChild(frag, node);
  }

  function isSkippedAncestor(node) {
    let n = node.parentNode;
    while (n && n !== document.body) {
      if (SKIP_TAGS.has(n.tagName)) return true;
      n = n.parentNode;
    }
    return false;
  }

  function walkAndReplace(root) {
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode(node) {
        if (isSkippedAncestor(node)) return NodeFilter.FILTER_REJECT;
        if (CLAIM_RE.test(node.nodeValue)) { CLAIM_RE.lastIndex = 0; return NodeFilter.FILTER_ACCEPT; }
        return NodeFilter.FILTER_SKIP;
      }
    });

    const nodes = [];
    let n;
    while ((n = walker.nextNode())) nodes.push(n);
    // Process in reverse so replacements don't invalidate the walker
    for (let i = nodes.length - 1; i >= 0; i--) processTextNode(nodes[i]);
  }

  // ── Bootstrap ──────────────────────────────────────────────────────────────
  function init() {
    tooltip = document.createElement('div');
    tooltip.id = 'claim-tooltip';
    document.body.appendChild(tooltip);

    // Target the main content area only (avoid nav/sidebar re-processing)
    const main = document.querySelector('main, article, .main-content, #main-content, body');
    walkAndReplace(main || document.body);
  }

  // Fetch claim data then initialise once DOM is ready
  fetch(DATA_URL)
    .then(r => r.ok ? r.json() : Promise.reject(r.status))
    .then(data => {
      claims = data;
      if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
      } else {
        init();
      }
    })
    .catch(err => console.warn('[claim-tooltips] Could not load claims.json:', err));

})();
