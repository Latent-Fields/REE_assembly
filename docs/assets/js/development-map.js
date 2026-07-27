(function () {
  "use strict";

  var root = document.getElementById("ree-development-map");
  if (!root) return;

  var frontierRoot = document.getElementById("development-map-frontier");
  var railRoot = document.getElementById("development-map-rail");
  var controlsRoot = document.getElementById("development-map-controls");
  var tracksRoot = document.getElementById("development-map-tracks");
  var archiveRoot = document.getElementById("development-map-archive");
  var explorerUrl = root.dataset.explorer || "public_explorer/";
  var archiveUrl = root.dataset.archive || "roadmap.html";
  var activeFilter = "all";

  function element(tag, options, children) {
    var node = document.createElement(tag);
    options = options || {};
    Object.keys(options).forEach(function (key) {
      var value = options[key];
      if (key === "class") node.className = value;
      else if (key === "text") node.textContent = value;
      else if (key === "dataset") Object.keys(value).forEach(function (dataKey) { node.dataset[dataKey] = value[dataKey]; });
      else if (key === "on") Object.keys(value).forEach(function (eventName) { node.addEventListener(eventName, value[eventName]); });
      else node.setAttribute(key, value);
    });
    (children || []).forEach(function (child) { if (child) node.appendChild(child); });
    return node;
  }

  function clear(node) { while (node.firstChild) node.removeChild(node.firstChild); }
  function titleCase(value) { return String(value || "unclassified").replace(/[_-]/g, " "); }
  function claimLink(id) { return explorerUrl + "#claim-" + encodeURIComponent(id); }

  function renderMetrics(metrics) {
    var list = element("dl", { class: "development-map-metrics" });
    metrics.forEach(function (metric) {
      list.appendChild(element("div", { class: "development-map-metric" }, [
        element("dt", { text: metric.label }),
        element("dd", { text: metric.value }),
        element("p", { text: metric.detail })
      ]));
    });
    return list;
  }

  function renderQuestion(question) {
    var count = question.surviving === null || question.surviving === undefined
      ? "Not recorded"
      : question.surviving + " of " + (question.initial === null || question.initial === undefined ? "?" : question.initial) + " rivals standing";
    var body = [
      element("p", { class: "development-question-count", text: count }),
      element("p", { class: "development-question-meta", text: "Convergence: " + titleCase(question.convergence) })
    ];
    if (question.claims && question.claims.length) {
      var claims = element("p", { class: "development-question-claims" }, [element("span", { text: "Related records" })]);
      question.claims.forEach(function (id) { claims.appendChild(element("a", { href: claimLink(id), text: id })); });
      body.push(claims);
    }
    return element("article", { class: "development-question" + (question.is_hero ? " is-hero" : "") }, [
      element("p", { class: "development-question-label", text: question.is_hero ? "Lead investigation" : "Active investigation" }),
      element("h3", { text: question.title })
    ].concat(body));
  }

  function renderFrontier(data) {
    clear(frontierRoot);
    var frontier = data.frontier || {};
    frontierRoot.className = "development-map-frontier";
    frontierRoot.appendChild(element("div", { class: "development-map-frontier-summary" }, [
      element("p", { class: "development-map-live-label", text: "Live question" }),
      element("p", { class: "development-map-headline", text: frontier.headline || "The programme's live research questions are shown below." }),
      frontier.gate ? element("div", { class: "development-map-gate" }, [
        element("span", { text: "Next recorded gate" }),
        element("p", { text: frontier.gate })
      ]) : null
    ]));
    frontierRoot.appendChild(renderMetrics(data.metrics || []));
    var questionGrid = element("div", { class: "development-question-grid" });
    (frontier.questions || []).forEach(function (question) { questionGrid.appendChild(renderQuestion(question)); });
    frontierRoot.appendChild(questionGrid);
  }

  function renderRail(tracks) {
    clear(railRoot);
    tracks.forEach(function (track, index) {
      railRoot.appendChild(element("button", {
        class: "development-map-rail-node",
        type: "button",
        "aria-label": "Jump to " + track.title,
        on: { click: function () {
          var target = document.getElementById("development-track-" + track.id);
          if (target) target.scrollIntoView({ behavior: "smooth", block: "start" });
        } }
      }, [
        element("span", { class: "development-map-rail-index", text: String(index + 1).padStart(2, "0") }),
        element("span", { class: "development-map-rail-title", text: track.title }),
        element("span", { class: "development-map-rail-count", text: track.total + " records" })
      ]));
    });
  }

  function updateFilter(nextFilter) {
    activeFilter = nextFilter;
    root.dataset.statusFilter = nextFilter;
    controlsRoot.querySelectorAll("button[data-filter]").forEach(function (button) {
      button.setAttribute("aria-pressed", String(button.dataset.filter === nextFilter));
    });
    if (nextFilter !== "all") {
      tracksRoot.querySelectorAll('.development-map-node-group[data-bucket="' + nextFilter + '"]').forEach(function (group) {
        group.open = true;
      });
    }
  }

  function renderControls() {
    clear(controlsRoot);
    [["all", "All records"], ["active", "Active"], ["closed", "Closed"], ["planned", "Planned"]].forEach(function (filter) {
      controlsRoot.appendChild(element("button", {
        type: "button",
        class: "development-map-filter",
        "data-filter": filter[0],
        "aria-pressed": String(filter[0] === activeFilter),
        text: filter[1],
        on: { click: function () { updateFilter(filter[0]); } }
      }));
    });
  }

  function renderNode(node, bucket) {
    var summary = element("summary", { class: "development-map-node-summary" }, [
      element("span", { class: "development-map-status-dot " + bucket, "aria-hidden": "true" }),
      element("span", { class: "development-map-node-id", text: node.id }),
      element("span", { class: "development-map-node-title", text: node.title }),
      element("span", { class: "development-map-node-state", text: titleCase(node.status) })
    ]);
    var details = element("details", { class: "development-map-node", dataset: { bucket: bucket } }, [summary]);
    var body = element("div", { class: "development-map-node-body" });
    body.appendChild(element("dl", { class: "development-map-node-metadata" }, [
      element("div", {}, [element("dt", { text: "Record status" }), element("dd", { text: titleCase(node.status) })]),
      element("div", {}, [element("dt", { text: "Phase" }), element("dd", { text: titleCase(node.phase) })]),
      element("div", {}, [element("dt", { text: "Attention" }), element("dd", { text: String(node.attention_rank) + " / 4" })]),
      element("div", {}, [element("dt", { text: "Referenced by" }), element("dd", { text: String(node.incoming_dependencies) + " records" })])
    ]));
    if (node.depends_on && node.depends_on.length) {
      var dependencies = element("div", { class: "development-map-dependencies" }, [element("span", { text: "Depends on" })]);
      node.depends_on.forEach(function (id) { dependencies.appendChild(element("a", { class: "development-map-dependency", href: claimLink(id), text: id })); });
      if (node.additional_dependencies) dependencies.appendChild(element("span", { class: "development-map-more", text: "+" + node.additional_dependencies + " more" }));
      body.appendChild(dependencies);
    }
    body.appendChild(element("a", { class: "development-map-source-link", href: claimLink(node.id), text: "Open source record" }));
    details.appendChild(body);
    return details;
  }

  function renderTrack(track, index) {
    var article = element("article", { class: "development-map-track", id: "development-track-" + track.id, dataset: { track: track.id } });
    article.appendChild(element("header", { class: "development-map-track-heading" }, [
      element("span", { class: "development-map-track-index", text: String(index + 1).padStart(2, "0") }),
      element("div", {}, [element("h3", { text: track.title }), element("p", { text: track.summary })]),
      element("span", { class: "development-map-track-total", text: track.total + " records" })
    ]));
    var groups = element("div", { class: "development-map-node-groups" });
    track.buckets.forEach(function (bucket) {
      var group = element("details", { class: "development-map-node-group", dataset: { bucket: bucket.key } });
      if (bucket.key === "active" && bucket.count) group.open = true;
      group.appendChild(element("summary", {}, [
        element("span", { class: "development-map-status-dot " + bucket.key, "aria-hidden": "true" }),
        element("span", { text: bucket.label }),
        element("span", { class: "development-map-group-count", text: String(bucket.count) })
      ]));
      var nodes = element("div", { class: "development-map-node-list" });
      if (bucket.nodes.length) bucket.nodes.forEach(function (node) { nodes.appendChild(renderNode(node, bucket.key)); });
      else nodes.appendChild(element("p", { class: "development-map-empty", text: "No records currently projected in this state." }));
      if (bucket.more_count) nodes.appendChild(element("a", { class: "development-map-all-records", href: explorerUrl, text: "Browse " + bucket.more_count + " additional records in the Lab Window" }));
      group.appendChild(nodes);
      groups.appendChild(group);
    });
    article.appendChild(groups);
    return article;
  }

  function renderTracks(data) {
    clear(tracksRoot);
    (data.tracks || []).forEach(function (track, index) { tracksRoot.appendChild(renderTrack(track, index)); });
  }

  function renderArchive(data) {
    clear(archiveRoot);
    archiveRoot.className = "development-map-archive-content";
    var archive = data.archive || {};
    var count = archive.snapshot_count || 0;
    archiveRoot.appendChild(element("p", { class: "development-map-archive-summary", text: count + " dated status snapshots are retained in the operational archive" + (archive.latest ? ", most recently " + archive.latest : "") + "." }));
    var dates = element("div", { class: "development-map-archive-dates" });
    (archive.recent_dates || []).forEach(function (date) { dates.appendChild(element("a", { href: archiveUrl, text: date })); });
    archiveRoot.appendChild(dates);
    archiveRoot.appendChild(element("a", { class: "development-map-archive-link", href: archiveUrl, text: "Open the full operational archive" }));
  }

  function render(data) {
    renderFrontier(data);
    renderRail(data.tracks || []);
    renderControls();
    renderTracks(data);
    renderArchive(data);
    updateFilter("all");
  }

  fetch(root.dataset.source, { cache: "no-store" })
    .then(function (response) {
      if (!response.ok) throw new Error("HTTP " + response.status);
      return response.json();
    })
    .then(render)
    .catch(function () {
      frontierRoot.className = "development-map-load-error";
      frontierRoot.textContent = "The Development Map data could not be loaded. The current front and operational archive remain available from the links above.";
    });
}());
