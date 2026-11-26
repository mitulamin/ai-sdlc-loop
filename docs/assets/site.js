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

  function initFilters() {
    var table = document.getElementById("ptable");
    if (!table) return;
    var q = document.getElementById("q");
    var cat = document.getElementById("cat");
    var src = document.getElementById("src");
    var reset = document.getElementById("reset");
    var count = document.getElementById("result-count");
    var rows = Array.prototype.slice.call(table.tBodies[0].rows);

    function apply() {
      var terms = q.value.toLowerCase().split(/\s+/).filter(Boolean);
      var shown = 0;
      rows.forEach(function (row) {
        var text = row.textContent.toLowerCase();
        var ok = terms.every(function (t) { return text.indexOf(t) !== -1; });
        if (ok && cat.value && row.getAttribute("data-cat") !== cat.value) ok = false;
        if (ok && src.value && row.getAttribute("data-sources").split("|").indexOf(src.value) === -1) ok = false;
        row.hidden = !ok;
        if (ok) shown++;
      });
      count.textContent = shown + " of " + rows.length + " principles";
      var params = new URLSearchParams();
      if (q.value) params.set("q", q.value);
      if (cat.value) params.set("cat", cat.value);
      if (src.value) params.set("src", src.value);
      var qs = params.toString();
      if (window.history && history.replaceState) {
        history.replaceState(null, "", location.pathname + (qs ? "?" + qs : ""));
      }
    }

    var params = new URLSearchParams(location.search);
    q.value = params.get("q") || "";
    cat.value = params.get("cat") || "";
    src.value = params.get("src") || "";

    q.addEventListener("input", apply);
    cat.addEventListener("change", apply);
    src.addEventListener("change", apply);
    reset.addEventListener("click", function () {
      q.value = ""; cat.value = ""; src.value = "";
      apply();
    });
    apply();
  }

  initTables();
  initFilters();
})();
