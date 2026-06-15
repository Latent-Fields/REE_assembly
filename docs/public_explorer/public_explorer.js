/* Public REE Explorer ("Lab Window") -- static, read-only front-end.
   Vanilla JS, no dependencies. Fetches curated JSON from ./data/ and renders
   four modes: Orientation, Evidence, Mechanism map, Contribute.
   All data is pre-curated by scripts/export_public_explorer.py; this file does
   no mutation and talks to no backend. */
(function () {
  "use strict";

  var DATA = "data/";
  var store = {};          // loaded JSON blobs
  var rendered = {};       // which panels have been rendered
  var EVIDENCE_STATES = ["supported", "weakened", "mixed", "unresolved", "superseded"];

  // ---- helpers -----------------------------------------------------------
  function el(tag, attrs, children) {
    var n = document.createElement(tag);
    if (attrs) Object.keys(attrs).forEach(function (k) {
      if (k === "class") n.className = attrs[k];
      else if (k === "html") n.innerHTML = attrs[k];
      else if (k === "text") n.textContent = attrs[k];
      else n.setAttribute(k, attrs[k]);
    });
    (children || []).forEach(function (c) {
      if (c == null) return;
      n.appendChild(typeof c === "string" ? document.createTextNode(c) : c);
    });
    return n;
  }
  function esc(s) { var d = document.createElement("div"); d.textContent = s == null ? "" : s; return d.innerHTML; }
  function badge(state, label) {
    return el("span", { class: "badge " + (state || "muted"), text: label || state || "" });
  }
  function fetchJSON(name) {
    return fetch(DATA + name + "?t=" + Date.now()).then(function (r) {
      if (!r.ok) throw new Error(name + " " + r.status);
      return r.json();
    });
  }
  function panel(id) { return document.getElementById("panel-" + id); }
  function setPanel(id, node) { var p = panel(id); p.innerHTML = ""; p.appendChild(node); }

  // ---- tab handling ------------------------------------------------------
  var tabs = Array.prototype.slice.call(document.querySelectorAll('nav.tabs [role="tab"]'));
  function activate(id) {
    tabs.forEach(function (t) {
      var on = t.id === "tab-" + id;
      t.setAttribute("aria-selected", on ? "true" : "false");
      panel(t.id.replace("tab-", "")).hidden = !on;
    });
    if (!rendered[id]) { renderers[id](); rendered[id] = true; }
    if (location.hash !== "#" + id) history.replaceState(null, "", "#" + id);
  }
  tabs.forEach(function (t) {
    var id = t.id.replace("tab-", "");
    t.addEventListener("click", function () { activate(id); });
    t.addEventListener("keydown", function (e) {
      var i = tabs.indexOf(t);
      if (e.key === "ArrowRight") { tabs[(i + 1) % tabs.length].focus(); }
      if (e.key === "ArrowLeft") { tabs[(i - 1 + tabs.length) % tabs.length].focus(); }
    });
  });

  // ---- Orientation -------------------------------------------------------
  function renderOrientation() {
    var o = store.orientation || {};
    var idx = store.index || {};
    var c = idx.counts || {};
    var root = el("div");

    root.appendChild(el("h2", { text: "What is REE?" }));
    root.appendChild(el("p", { class: "lead", text: o.what_is_ree || "" }));

    var stats = el("div", { class: "stat-row" }, [
      stat(c.claims_public, "public claims"),
      stat(c.experiments_public, "reviewed experiments"),
      stat(c.mechanisms, "mechanism groups"),
      stat(idx.pending_review_count, "awaiting review")
    ]);
    root.appendChild(stats);

    root.appendChild(card("What V3 is trying to prove", o.what_v3_proves));
    root.appendChild(card("What V3 does NOT prove", o.what_v3_does_not_prove));
    root.appendChild(card("How to read the evidence", o.how_to_read_evidence));

    if (o.not_yet_inferred && o.not_yet_inferred.length) {
      var li = (o.not_yet_inferred).map(function (s) { return el("li", { text: s }); });
      var c2 = el("div", { class: "card" }, [
        el("h3", { text: "What should NOT be inferred yet" }),
        el("ul", { class: "note-list" }, li)
      ]);
      root.appendChild(c2);
    }

    var start = el("div", { class: "card" }, [
      el("h3", { text: "Start here" }),
      el("p", { html: "New to REE? Read <strong>What is REE</strong> above, then open the " +
        "<strong>Evidence</strong> tab and filter by <em>supported</em> to see what reviewed " +
        "experiments back up, or by <em>weakened</em> / <em>unresolved</em> to see the open " +
        "edges. The <strong>Mechanism map</strong> groups the architecture by cognitive function." })
    ]);
    root.appendChild(start);

    setPanel("orientation", root);
    function stat(n, l) {
      return el("div", { class: "stat" }, [
        el("span", { class: "n", text: (n == null ? "--" : String(n)) }),
        el("span", { class: "l", text: l })
      ]);
    }
    function card(h, body) {
      return el("div", { class: "card" }, [el("h3", { text: h }), el("p", { text: body || "" })]);
    }
  }

  // ---- Evidence ----------------------------------------------------------
  function renderEvidence() {
    var claims = store.claims || [];
    var experiments = store.experiments || [];
    var expByClaim = {};
    experiments.forEach(function (e) {
      (e.claim_ids || []).forEach(function (cid) {
        (expByClaim[cid] = expByClaim[cid] || []).push(e);
      });
    });

    var root = el("div");
    root.appendChild(el("h2", { text: "Evidence explorer" }));
    root.appendChild(el("p", { class: "lead", text:
      "Each claim shows the direction of its reviewed evidence. “Supported” means at " +
      "least one reviewed experiment met its pre-registered criteria — it does not mean proven. " +
      "Expand a claim to see the experiments that bear on it." }));

    var search = el("input", { type: "search", placeholder: "Search id, title, subject…", "aria-label": "Search claims" });
    var stateSel = selectFrom("All evidence states", EVIDENCE_STATES);
    var fnSel = selectFrom("All cognitive functions", uniq(claims.map(function (c) { return c.cognitive_function; })));
    var typeSel = selectFrom("All claim types", uniq(claims.map(function (c) { return c.claim_type; })));
    var controls = el("div", { class: "controls" }, [search, stateSel, fnSel, typeSel]);
    root.appendChild(controls);
    var countLine = el("p", { class: "count-line" });
    root.appendChild(countLine);
    var list = el("div");
    root.appendChild(list);
    setPanel("evidence", root);

    function apply() {
      var q = search.value.trim().toLowerCase();
      var st = stateSel.value, fn = fnSel.value, ty = typeSel.value;
      list.innerHTML = "";
      var shown = 0;
      claims.forEach(function (c) {
        if (st && c.evidence_state !== st) return;
        if (fn && c.cognitive_function !== fn) return;
        if (ty && c.claim_type !== ty) return;
        if (q && (c.id + " " + c.title + " " + c.subject).toLowerCase().indexOf(q) === -1) return;
        shown++;
        list.appendChild(claimItem(c, expByClaim[c.id] || []));
      });
      countLine.textContent = shown + " of " + claims.length + " claims";
      if (!shown) list.appendChild(el("div", { class: "empty", text: "No claims match these filters." }));
    }
    [search, stateSel, fnSel, typeSel].forEach(function (e) {
      e.addEventListener("input", apply); e.addEventListener("change", apply);
    });
    apply();
  }

  function claimItem(c, exps) {
    var head = el("summary", {}, [
      el("span", { class: "id", text: c.id }),
      el("span", { class: "title", text: c.title }),
      badge(c.evidence_state, c.evidence_state),
      el("span", { class: "sub", text: c.claim_type })
    ]);
    var body = el("div", { class: "body" });
    body.appendChild(kv("Cognitive function", c.cognitive_function));
    body.appendChild(kv("Subject", c.subject));
    body.appendChild(kv("Status", c.status + (c.limitation === "substrate" ? " (substrate-limited)" : "")));
    if (c.epistemic_stance) body.appendChild(kv("Epistemic stance", c.epistemic_stance));
    if (c.evidence) {
      var ev = c.evidence;
      body.appendChild(kv("Reviewed evidence",
        ev.supports + " support, " + ev.weakens + " weaken, " + ev.mixed + " mixed" +
        (ev.quadrant ? " · " + ev.quadrant.replace(/_/g, " ") : "")));
    }
    if (c.depends_on && c.depends_on.length) {
      var deps = el("div", { class: "kv deps" }, [el("b", { text: "Depends on: " })]);
      c.depends_on.forEach(function (d) { deps.appendChild(el("span", { class: "chip", text: d })); });
      body.appendChild(deps);
    }
    if (exps.length) {
      body.appendChild(el("div", { class: "kv" }, [el("b", { text: "Experiments bearing on this claim:" })]));
      exps.slice(0, 8).forEach(function (e) { body.appendChild(miniExp(e)); });
      if (exps.length > 8) body.appendChild(el("p", { class: "sub", text: "+" + (exps.length - 8) + " more (see Evidence list)" }));
    } else {
      body.appendChild(el("p", { class: "sub", text: "No reviewed experiment is linked to this claim yet." }));
    }
    return el("details", { class: "item" }, [head, body]);
  }

  function miniExp(e) {
    return el("div", { class: "kv" }, [
      badge(e.status, e.status.toUpperCase()), " ",
      el("span", { class: "id", text: e.id }), " ",
      el("span", { text: e.title + (e.date ? " (" + e.date + ")" : "") })
    ]);
  }

  // ---- Mechanism map -----------------------------------------------------
  function renderMechanisms() {
    var groups = store.mechanisms || [];
    var claimsById = {};
    (store.claims || []).forEach(function (c) { claimsById[c.id] = c; });

    var root = el("div");
    root.appendChild(el("h2", { text: "Mechanism map" }));
    root.appendChild(el("p", { class: "lead", text:
      "REE's mechanisms (invariants, architectural commitments, mechanism hypotheses, " +
      "substrate designs) grouped by the cognitive function they touch. Each chip shows " +
      "the claim's current evidence state." }));

    var legend = el("div", { class: "controls" }, EVIDENCE_STATES.map(function (s) { return badge(s, s); }));
    root.appendChild(legend);

    groups.forEach(function (g) {
      var members = el("div", { class: "members" });
      g.claims.forEach(function (m) {
        members.appendChild(el("span", { class: "mech-chip", title: m.title }, [
          el("span", { class: "id", text: m.id }),
          el("span", { text: shorten(m.title, 42) }),
          badge(m.state, m.state)
        ]));
      });
      root.appendChild(el("details", { class: "fn-group" }, [
        el("summary", { text: g.function + "  (" + g.count + ")" }),
        members
      ]));
    });
    setPanel("mechanisms", root);
  }

  // ---- Contribute --------------------------------------------------------
  function renderContribute() {
    var hw = store.help_wanted || {};
    var repo = hw.repo_url || "https://github.com/Latent-Fields/REE_assembly";
    var root = el("div");
    root.appendChild(el("h2", { text: "Safe ways to help" }));
    root.appendChild(el("p", { class: "lead", text:
      "REE is an open evidence programme. Outside input is welcome through the channels " +
      "below." }));

    root.appendChild(el("div", { class: "disclaimer", text:
      hw.governance_caveat || "Suggestions are reviewed before they enter governance." }));

    var grid = el("div", { class: "contrib" });
    (hw.paths || []).forEach(function (p) {
      var url = repo + "/issues/new?template=" + encodeURIComponent(p.template);
      grid.appendChild(el("div", { class: "card" }, [
        el("h3", { text: p.label }),
        el("p", { text: p.description }),
        el("a", { class: "btn", href: url, rel: "noopener", target: "_blank", text: p.label + " →" })
      ]));
    });
    root.appendChild(grid);
    setPanel("contribute", root);
  }

  // ---- small utilities ---------------------------------------------------
  function kv(k, v) { return el("div", { class: "kv" }, [el("b", { text: k + ": " }), document.createTextNode(v == null ? "" : v)]); }
  function selectFrom(allLabel, values) {
    var s = el("select");
    s.appendChild(el("option", { value: "", text: allLabel }));
    values.filter(Boolean).sort().forEach(function (v) { s.appendChild(el("option", { value: v, text: v })); });
    return s;
  }
  function uniq(a) { var seen = {}; return a.filter(function (x) { if (!x || seen[x]) return false; seen[x] = 1; return true; }); }
  function shorten(s, n) { s = s || ""; return s.length <= n ? s : s.slice(0, n - 1) + "…"; }

  var renderers = {
    orientation: renderOrientation,
    evidence: renderEvidence,
    mechanisms: renderMechanisms,
    contribute: renderContribute
  };

  // ---- boot --------------------------------------------------------------
  function fail(msg) {
    tabs.forEach(function (t) {
      var p = panel(t.id.replace("tab-", ""));
      p.innerHTML = "";
      p.appendChild(el("div", { class: "empty", text: msg }));
    });
  }

  Promise.all([
    fetchJSON("index.json"), fetchJSON("orientation.json"), fetchJSON("claims_public.json"),
    fetchJSON("experiments_public.json"), fetchJSON("mechanisms_public.json"), fetchJSON("help_wanted.json")
  ]).then(function (res) {
    store.index = res[0]; store.orientation = res[1]; store.claims = res[2];
    store.experiments = res[3]; store.mechanisms = res[4]; store.help_wanted = res[5];

    var tagline = (store.orientation && store.orientation.tagline);
    if (tagline) document.getElementById("tagline").textContent = tagline;
    if (store.index && store.index.generated_utc) {
      document.getElementById("gen-date").textContent = store.index.generated_utc.slice(0, 10);
    }
    if (store.help_wanted && store.help_wanted.repo_url) {
      document.getElementById("repo-link").href = store.help_wanted.repo_url;
    }

    var initial = (location.hash || "#orientation").slice(1);
    if (!renderers[initial]) initial = "orientation";
    activate(initial);
  }).catch(function (e) {
    fail("Could not load explorer data (" + e.message + "). If you are viewing this on " +
      "GitHub Pages, the data export may not have been published yet.");
  });
})();
