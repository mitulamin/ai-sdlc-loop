(function () {
  "use strict";

  function initTables() {
    var tables = document.querySelectorAll("table.sortable");
    Array.prototype.forEach.call(tables, function (table) {
      var heads = table.querySelectorAll("thead th");
      Array.prototype.forEach.call(heads, function (th, col) {
        var label = th.textContent;
        th.textContent = "";
        var btn = document.createElement("button");
        btn.type = "button";
        btn.textContent = label;
        th.appendChild(btn);
        btn.addEventListener("click", function () {
          var dir = th.getAttribute("aria-sort") === "ascending" ? "descending" : "ascending";
          sortBy(table, col, th.getAttribute("data-type"), dir);
          Array.prototype.forEach.call(heads, function (h) { h.removeAttribute("aria-sort"); });
          th.setAttribute("aria-sort", dir);
        });
      });
    });
  }

  function cellValue(row, col, type) {
    var cell = row.children[col];
    var raw = cell.getAttribute("data-sort");
    if (raw === null) raw = cell.textContent.trim();
    if (type === "num") {
      var n = parseFloat(raw);
      return isNaN(n) ? 0 : n;
    }
    return raw.toLowerCase();
  }

  function sortBy(table, col, type, dir) {
    var body = table.tBodies[0];
    var rows = Array.prototype.slice.call(body.rows);
    var sign = dir === "ascending" ? 1 : -1;
    rows.sort(function (a, b) {
      var x = cellValue(a, col, type), y = cellValue(b, col, type);
      if (x < y) return -sign;
      if (x > y) return sign;
      return 0;
    });
    rows.forEach(function (r) { body.appendChild(r); });
  }

  // A .filters block with data-table="<id>" and data-noun="<plural>" filters that table's rows.
  // Its search box has data-q, each select has data-attr="<name>" and matches the row's data-<name>
  // (several values split by "|"), and its reset button has data-reset. The state is kept in the
  // URL query so a filtered view can be shared.
  function initFilters() {
    var blocks = document.querySelectorAll(".filters[data-table]");
    Array.prototype.forEach.call(blocks, function (block) {
      var table = document.getElementById(block.getAttribute("data-table"));
      if (!table) return;
      var q = block.querySelector("[data-q]");
      var selects = Array.prototype.slice.call(block.querySelectorAll("select[data-attr]"));
      var reset = block.querySelector("[data-reset]");
      var count = document.querySelector("[data-count]");
      var noun = block.getAttribute("data-noun") || "rows";
      var rows = Array.prototype.slice.call(table.tBodies[0].rows);

      function apply() {
        var terms = q.value.toLowerCase().split(/\s+/).filter(Boolean);
        var shown = 0;
        rows.forEach(function (row) {
          var text = row.textContent.toLowerCase();
          var ok = terms.every(function (t) { return text.indexOf(t) !== -1; });
          selects.forEach(function (sel) {
            if (!ok || !sel.value) return;
            var have = (row.getAttribute("data-" + sel.getAttribute("data-attr")) || "").split("|");
            if (have.indexOf(sel.value) === -1) ok = false;
          });
          row.hidden = !ok;
          if (ok) shown++;
        });
        count.textContent = shown === rows.length ? rows.length + " " + noun : shown + " of " + rows.length + " " + noun;
        var params = new URLSearchParams();
        if (q.value) params.set("q", q.value);
        selects.forEach(function (sel) {
          if (sel.value) params.set(sel.getAttribute("data-attr"), sel.value);
        });
        var qs = params.toString();
        if (window.history && history.replaceState) {
          history.replaceState(null, "", location.pathname + (qs ? "?" + qs : "") + location.hash);
        }
      }

      var params = new URLSearchParams(location.search);
      q.value = params.get("q") || "";
      selects.forEach(function (sel) {
        sel.value = params.get(sel.getAttribute("data-attr")) || "";
        if (sel.selectedIndex === -1) sel.value = "";
      });

      q.addEventListener("input", apply);
      selects.forEach(function (sel) { sel.addEventListener("change", apply); });
      reset.addEventListener("click", function () {
        q.value = "";
        selects.forEach(function (sel) { sel.value = ""; });
        apply();
      });
      apply();
    });
  }

  initTables();
  initFilters();
})();
