(() => {
  const data = window.TONELAB;
  if (!data || !Array.isArray(data.records)) {
    document.getElementById("summary").textContent =
      "Catalogue data did not load. Rebuild with python tools/build_master_index.py";
    return;
  }

  const labels = data.file_labels || {};
  const records = data.records;
  const els = {
    q: document.getElementById("q"),
    file: document.getElementById("file"),
    country: document.getElementById("country"),
    tradition: document.getElementById("tradition"),
    decade: document.getElementById("decade"),
    genre: document.getElementById("genre"),
    status: document.getElementById("status"),
    sort: document.getElementById("sort"),
    reset: document.getElementById("reset"),
    results: document.getElementById("results"),
    count: document.getElementById("count"),
    detail: document.getElementById("detail"),
    summary: document.getElementById("summary"),
  };

  const countries = unique(
    records.flatMap((row) => splitValues(row.country))
  );
  const files = [...new Set(records.map((row) => row.source_file))].sort();
  const traditions = unique(records.map((row) => row.musical_tradition));
  const decades = unique(records.map((row) => row.decade));
  const genres = unique(records.map((row) => row.genre));
  const statuses = unique(records.map((row) => row.verification_status));

  fillSelect(els.file, files, (value) => labels[value] || value);
  fillSelect(els.country, countries);
  fillSelect(els.tradition, traditions);
  fillSelect(els.decade, decades);
  fillSelect(els.genre, genres);
  fillSelect(els.status, statuses);

  const verified = records.filter((row) => row.verification_status === "Verified").length;
  const countriesCount = countries.length;
  els.summary.textContent =
    `${records.length} records · ${countriesCount} countries and areas · ${verified} verified · generated ${data.generated}`;

  let selectedId = new URLSearchParams(location.hash.replace(/^#/, "")).get("id");

  function apply() {
    const query = els.q.value.trim().toLowerCase();
    let rows = records.filter((row) => {
      if (els.file.value && row.source_file !== els.file.value) return false;
      if (els.tradition.value && row.musical_tradition !== els.tradition.value) return false;
      if (els.decade.value && row.decade !== els.decade.value) return false;
      if (els.genre.value && row.genre !== els.genre.value) return false;
      if (els.status.value && row.verification_status !== els.status.value) return false;
      if (els.country.value && !splitValues(row.country).includes(els.country.value)) return false;
      if (!query) return true;
      return searchBlob(row).includes(query);
    });

    const sort = els.sort.value;
    rows.sort((a, b) => {
      if (sort === "year") return String(b.year || "").localeCompare(String(a.year || "")) || cmpTitle(a, b);
      if (sort === "country") return (a.country || "").localeCompare(b.country || "") || cmpTitle(a, b);
      if (sort === "artist") return (a.artist || a.composer || "").localeCompare(b.artist || b.composer || "") || cmpTitle(a, b);
      return cmpTitle(a, b);
    });

    els.count.textContent = `${rows.length} shown`;
    els.results.innerHTML = "";
    if (!rows.length) {
      els.results.innerHTML = `<li class="empty-list">No records match these filters.</li>`;
    } else {
      const fragment = document.createDocumentFragment();
      for (const row of rows) {
        fragment.appendChild(renderRow(row));
      }
      els.results.appendChild(fragment);
    }

    const stillVisible = rows.find((row) => row.id === selectedId);
    if (stillVisible) {
      showDetail(stillVisible);
      highlight(selectedId);
    } else if (!selectedId) {
      els.detail.innerHTML = `<p class="empty-detail">Select a record to read notes and sources.</p>`;
    }
  }

  function renderRow(row) {
    const item = document.createElement("li");
    item.dataset.id = row.id;
    if (row.id === selectedId) item.classList.add("active");
    const english = row.title_english && row.title_english !== row.title_original
      ? `<p class="english">${escapeHtml(row.title_english)}</p>`
      : "";
    item.innerHTML = `
      <div class="row-top">
        <p class="title">${escapeHtml(row.title_original)}</p>
        <span class="badge ${badgeClass(row.verification_status)}">${escapeHtml(row.verification_status)}</span>
      </div>
      ${english}
      <p class="who">${escapeHtml(row.artist || row.composer || "Unknown artist")}</p>
      <p class="place">${escapeHtml([row.country, row.genre, row.year || row.decade].filter(Boolean).join(" · "))}</p>
    `;
    item.addEventListener("click", () => {
      selectedId = row.id;
      location.hash = `id=${encodeURIComponent(row.id)}`;
      highlight(row.id);
      showDetail(row);
    });
    return item;
  }

  function showDetail(row) {
    const extraLinks = splitValues(row.additional_source_urls)
      .filter((url) => /^https?:\/\//i.test(url))
      .map((url, index) => `<a href="${escapeAttr(url)}" target="_blank" rel="noopener noreferrer">Source ${index + 2}</a>`)
      .join("");
    const audio = row.audio_url
      ? `<a href="${escapeAttr(row.audio_url)}" target="_blank" rel="noopener noreferrer">Audio</a>`
      : "";
    const source = row.source_url
      ? `<a href="${escapeAttr(row.source_url)}" target="_blank" rel="noopener noreferrer">Primary source</a>`
      : "";

    els.detail.innerHTML = `
      <p class="eyebrow">${escapeHtml(labels[row.source_file] || row.source_file)} · ${escapeHtml(row.id)}</p>
      <h2>${escapeHtml(row.title_original)}</h2>
      ${row.title_english ? `<p class="english">${escapeHtml(row.title_english)}</p>` : ""}
      <dl class="kv">
        ${field("Artist", row.artist)}
        ${field("Composer", row.composer)}
        ${field("Songwriter", row.songwriter)}
        ${field("Country", row.country)}
        ${field("Region", row.region)}
        ${field("Language", row.language)}
        ${field("Genre", [row.genre, row.subgenre].filter(Boolean).join(" · "))}
        ${field("Tradition", row.musical_tradition)}
        ${field("Attribution", row.attribution_type)}
        ${field("Date", [row.year, row.decade].filter(Boolean).join(" · "))}
        ${field("Format", row.original_format)}
        ${field("Instruments", row.original_instruments)}
        ${field("Piano version", row.piano_version_exists)}
        ${field("Also associated", row.secondary_associations)}
        ${field("Batch", row.research_batch)}
      </dl>
      ${row.research_notes ? `<p class="notes">${escapeHtml(row.research_notes)}</p>` : ""}
      <div class="links">${source}${extraLinks}${audio}</div>
    `;
  }

  function highlight(id) {
    for (const item of els.results.querySelectorAll("li[data-id]")) {
      item.classList.toggle("active", item.dataset.id === id);
    }
  }

  function field(label, value) {
    if (!value) return "";
    return `<dt>${escapeHtml(label)}</dt><dd>${escapeHtml(value)}</dd>`;
  }

  els.reset.addEventListener("click", () => {
    els.q.value = "";
    for (const select of [els.file, els.country, els.tradition, els.decade, els.genre, els.status]) {
      select.value = "";
    }
    els.sort.value = "title";
    apply();
  });

  for (const el of [els.q, els.file, els.country, els.tradition, els.decade, els.genre, els.status, els.sort]) {
    el.addEventListener("input", apply);
    el.addEventListener("change", apply);
  }

  window.addEventListener("hashchange", () => {
    selectedId = new URLSearchParams(location.hash.replace(/^#/, "")).get("id");
    const row = records.find((item) => item.id === selectedId);
    if (row) {
      showDetail(row);
      highlight(row.id);
    }
  });

  apply();
  if (selectedId) {
    const row = records.find((item) => item.id === selectedId);
    if (row) {
      showDetail(row);
      highlight(row.id);
    }
  }

  function fillSelect(select, values, labelFn) {
    select.innerHTML = `<option value="">All</option>` + values.map((value) => {
      const label = labelFn ? labelFn(value) : value;
      return `<option value="${escapeAttr(value)}">${escapeHtml(label)}</option>`;
    }).join("");
  }

  function unique(values) {
    return [...new Set(values.filter(Boolean))].sort((a, b) => a.localeCompare(b));
  }

  function splitValues(value) {
    return String(value || "").split("|").map((part) => part.trim()).filter(Boolean);
  }

  function searchBlob(row) {
    return [
      row.id, row.title_original, row.title_english, row.artist, row.composer,
      row.songwriter, row.country, row.genre, row.subgenre, row.research_notes,
    ].join(" ").toLowerCase();
  }

  function cmpTitle(a, b) {
    return (a.title_original || "").localeCompare(b.title_original || "", undefined, { sensitivity: "base" });
  }

  function badgeClass(status) {
    if (status === "Verified") return "Verified";
    if (status === "Partially verified") return "Partially";
    return "Unverified";
  }

  function escapeHtml(value) {
    return String(value)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function escapeAttr(value) {
    return escapeHtml(value).replace(/'/g, "&#39;");
  }
})();
