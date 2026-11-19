"""Build one ID paper page from a spec module.

Usage: python -I build.py <spec.py> [<spec.py> ...]
Writes papers/<slug>/{paper.json,index.html,storyboard.md,video.vtt} in the site repo,
plus scratchpad/build/out/<slug>.props.json (video props) and <slug>.card.html (index card).
Every number's source_quote, every figure caption and every MUST-INCLUDE excerpt must
appear in the PDF text, and every literal number left in the prose must appear in the PDF too.
"""
import json, re, sys, html, runpy, pathlib

HERE = pathlib.Path(__file__).resolve().parent
SITE = pathlib.Path(r"C:\Users\yalci\OneDrive\Documents\SSS logos and files and stuff\Website test 1")
TXT = HERE.parent / "txt"
OUT = HERE / "out"; OUT.mkdir(exist_ok=True)
BASE = (SITE / "papers/oviva-2019/index.html").read_text(encoding="utf8")

def norm(s):
    s = s.replace("·", ".").replace("\u2212", "-").replace("\u2013", "-").replace("\u2014", "-")
    s = re.sub(r"[^\x20-\x7e]", "", s)
    s = re.sub(r"[\s\-]+", "", s)
    return s.lower()

def fmt(n, html_mode=True):
    v = n["value"]
    if v is None:
        return "\u26a0 data needed"
    s = f"{v:.{n['decimals']}f}" if n.get("decimals") is not None and isinstance(v, (int, float)) else str(v)
    if isinstance(v, (int, float)) and abs(v) >= 10000 and n.get("commas", True):
        s = f"{v:,}" if n.get("decimals") is None else f"{v:,.{n['decimals']}f}"
    if s.startswith("-"):
        s = ("&minus;" if html_mode else "\u2212") + s[1:]
    return s + (n.get("unit") or "")

def build(spec_path):
    S = runpy.run_path(spec_path)["SPEC"]
    slug = S["slug"]
    pdf = (TXT / f"{S['pdf']}.txt").read_text(encoding="utf8", errors="replace")
    P = norm(pdf)
    errs = []
    by = {}
    numbers = []
    for n in S["numbers"]:
        n = dict(n)
        n.setdefault("unit", ""); n.setdefault("arm", None); n.setdefault("ci_low", None); n.setdefault("ci_high", None)
        n.setdefault("source", "paper"); n.setdefault("status", "VERIFIED")
        if norm(n["source_quote"]) not in P:
            errs.append(f"QUOTE NOT IN PDF [{n['id']}]: {n['source_quote'][:90]}")
        if len(n["source_quote"]) > 300:
            errs.append(f"QUOTE >300 chars [{n['id']}]")
        if n["id"] in by: errs.append(f"DUP id {n['id']}")
        by[n["id"]] = n; numbers.append(n)
    for f in S["figures"]:
        if norm(f["caption"]) not in P: errs.append(f"CAPTION NOT IN PDF [{f['id']}]")
        for r in f["number_ids"] + ([f["margin_id"]] if f.get("margin_id") else []):
            if r not in by: errs.append(f"BAD REF {f['id']} -> {r}")
        for g in f.get("groups", []):
            for r in g["ids"]:
                if r not in by: errs.append(f"BAD REF {f['id']} -> {r}")
    for ex, sec in S["must_include"]:
        if norm(ex) not in P: errs.append(f"MUST-INCLUDE NOT IN PDF: {ex[:80]}")

    def render(text, html_mode=True):
        def rep(m):
            i = m.group(1)
            if i not in by:
                errs.append(f"BAD TOKEN {i}"); return "??"
            v = fmt(by[i], html_mode)
            return f"<b>{v}</b>" if html_mode else v
        return re.sub(r"\{\{n:([\w]+)\}\}", rep, text)

    # literal numbers in prose (outside tokens) must appear in the PDF text
    def check_literals(label, text):
        t = re.sub(r"\{\{n:[\w]+\}\}", " ", text)
        t = re.sub(r"<[^>]+>", " ", t)
        t = re.sub(r"&[a-z]+;", " ", t)
        for m in re.finditer(r"(?<![\w.])\d[\d,]*(?:\.\d+)?", t):
            num = m.group(0).replace(",", "")
            if num.rstrip(".") and norm(num) not in P.replace(",", ""):
                errs.append(f"LITERAL {num} in {label} not in PDF")
            elif len(num) >= 2 and not re.search(r"(?<![\d.])" + re.escape(num) + r"(?![\d])", pdf.replace(",", "").replace("·", ".")):
                errs.append(f"LITERAL {num} in {label} not found as a standalone number")

    sec = S["sections"]
    texts = {"background": sec["background"], "conclusions": sec["conclusions"], "limitations": sec["limitations"],
             "practice_impact": sec["practice_impact"], "one_liner": S["one_liner"]}
    for k, v in sec["methods"].items(): texts["methods." + k] = v
    for i, r in enumerate(sec["results"]):
        if isinstance(r, str): texts[f"results.{i}"] = r
    for h in S["hero"]: texts["hero." + h[0]] = h[1]
    for k, v in texts.items(): check_literals(k, v)

    # ---------- paper.json ----------
    strip = lambda t: re.sub(r"<[^>]+>", "", t)
    results_plain = " ".join(strip(r) for r in sec["results"] if isinstance(r, str))
    M = sec["methods"]
    pj = {
        "slug": slug, "topic": S["topic"], "one_liner": S["one_liner"], "one_liner_plain": S["one_liner_plain"],
        "arms": S.get("arms", {}),
        "citation": {"title": S["title"], "short_name": S["short_name"], "authors": S["authors"], "journal": S["journal"],
                     "year": S["year"], "volume_pages": S["volume_pages"], "pmid": S["pmid"], "doi": S["doi"],
                     "pubmed_url": f"https://pubmed.ncbi.nlm.nih.gov/{S['pmid']}/", "doi_url": f"https://doi.org/{S['doi']}"},
        "sections": {"background": strip(sec["background"]),
                     "methods": {k.lower().replace(" ", "_"): strip(v) for k, v in M.items()},
                     "results": results_plain, "conclusions": strip(sec["conclusions"]),
                     "limitations": strip(sec["limitations"]), "practice_impact": strip(sec["practice_impact"])},
        "numbers": numbers,
        "figures": S["figures"],
        "hero_findings": [{"number_id": h[0], "figure_id": h[2] if len(h) > 2 else None, "headline": strip(render(h[1], False))} for h in S["hero"]],
        "must_include_map": [{"excerpt": e, "section": s} for e, s in S["must_include"]],
    }
    if errs:
        print(f"== {slug}: {len(errs)} problem(s)")
        for e in errs: print("  ", e)
        return False
    d = SITE / "papers" / slug; d.mkdir(parents=True, exist_ok=True)
    (d / "paper.json").write_text(json.dumps(pj, indent=1, ensure_ascii=False) + "\n", encoding="utf8")

    # ---------- index.html ----------
    cite_short = f"{S['short_name']} ({S['journal']} {S['year']})"
    head_end = BASE.index("<style>")
    head = BASE[:head_end]
    reps = {
        'content="The OVIVA trial (NEJM 2019): oral antibiotics were noninferior to IV for bone and joint infection. Video and charts from the published trial."': f'content="{S["seo_desc"]}"',
        "OVIVA Trial (NEJM 2019): Oral vs IV for Bone &amp; Joint": S["seo_title"],
        "/papers/oviva-2019/": f"/papers/{slug}/",
    }
    for a, b in reps.items():
        assert a in head, a
        head = head.replace(a, b)
    style = BASE[head_end:BASE.index("</head>")]
    tail = BASE[BASE.index('<footer class="site-footer"'):]
    cur = '<a href="/papers/oviva-2019/" aria-current="page"><span class="pix" data-pix="notepad"></span><span class="label">OVIVA</span></a>'
    assert cur in tail
    tail = tail.replace(cur, f'<a href="/papers/{slug}/" aria-current="page"><span class="pix" data-pix="notepad"></span><span class="label">{S["taskbar_label"]}</span></a>')

    R = lambda t: render(t, True)
    related = "".join(f'<a class="btn btn-sm" href="{u}">{t}</a>' for u, t in S.get("related", []))
    related += '<a class="btn btn-sm" href="/seasoning-lab/">Seasoning Lab: ID learning corner</a>'
    stats = "\n".join(f'    <div class="stat"><b>{fmt(by[h[0]])}</b><span>{render(h[1], True).replace("<b>", "").replace("</b>", "")}</span></div>' for h in S["hero"])

    def figure(f):
        return (f'  <figure data-figure="{f["id"]}"><h3>{f["title"]}</h3><div class="chart-box"><canvas aria-label="{html.escape(f["alt"])}" role="img"></canvas></div>\n'
                f'   <figcaption>&ldquo;{html.escape(f["caption"])}&rdquo; Recreated from data reported in {cite_short}.</figcaption>\n'
                f'   <details><summary>Data table</summary><table class="data"></table></details></figure>\n')
    figs = {f["id"]: f for f in S["figures"]}
    placed = set(); res = []
    for r in sec["results"]:
        if isinstance(r, str): res.append(f"  <p>{R(r)}</p>\n")
        elif "quote" in r:
            if norm(r["quote"]) not in P: errs.append("RESULTS QUOTE NOT IN PDF")
            res.append(f'  <blockquote>&ldquo;{html.escape(r["quote"])}&rdquo; &mdash; the paper</blockquote>\n')
        elif "fig" in r: res.append(figure(figs[r["fig"]])); placed.add(r["fig"])
    for f in S["figures"]:
        if f["id"] not in placed: res.append(figure(f))
    rows = "".join(f"<tr><th>{k}</th><td>{R(v)}</td></tr>" for k, v in M.items())
    note = f'\n  <p style="margin-top:12px">{R(sec["methods_note"])}</p>' if sec.get("methods_note") else ""
    win = lambda name, icon="notepad": f'<div class="titlebar"><span class="pix t-icon" data-pix="{icon}"></span><span class="t-text">{name}</span></div>'
    body = f'''<body>

<a href="#main" class="skip-link">Skip to content</a>

<main class="wrap narrow" id="main" tabindex="-1">
<div class="pp">
 <section class="window"><div class="titlebar"><span class="pix t-icon" data-pix="folder"></span><span class="t-text">{slug}.paper</span><span class="t-btns"><span class="t-btn t-min" aria-hidden="true"></span><span class="t-btn t-max" aria-hidden="true"></span><button type="button" class="t-btn t-close" aria-label="Close"></button></span></div>
  <div class="win-body">
   <h1>{S["h1"]}</h1>
   <p class="cite">{S["authors"]} <i>{S["journal"]}</i> {S["year"]};{S["volume_pages"]}. PMID {S["pmid"]}</p>
   <div class="btn-row"><a class="btn btn-primary" href="https://pubmed.ncbi.nlm.nih.gov/{S["pmid"]}/" target="_blank" rel="noopener">Read on PubMed</a><a class="btn" href="https://doi.org/{S["doi"]}" target="_blank" rel="noopener">DOI</a><a class="btn" href="/papers/">Landmark ID papers, visualized</a></div>
   <div class="btn-row more-links">{related}</div>
  </div></section>

 <section class="window hero">{win("highlights.mp4", "play")}
  <div class="win-body">
   <video src="video.mp4" poster="poster.jpg" controls muted playsinline preload="metadata"><track kind="captions" src="video.vtt" srclang="en" label="English" default></video>
   <div class="stats" style="margin-top:14px">
{stats}
   </div>
  </div></section>

 <section class="window reveal">{win("background.txt")}<div class="win-body"><h2>Background</h2><p>{R(sec["background"])}</p></div></section>

 <section class="window reveal">{win("methods.txt")}<div class="win-body"><h2>Methods</h2>
  <table>{rows}</table>{note}
  </div></section>

 <section class="window reveal">{win("results.xls")}<div class="win-body"><h2>Results</h2>
{"".join(res)} </div></section>

 <section class="window reveal">{win("conclusions.txt")}<div class="win-body"><h2>Conclusions</h2><p>{R(sec["conclusions"])}</p><h2>Limitations</h2><p>{R(sec["limitations"])}</p><h2>What changed in practice</h2><p>{R(sec["practice_impact"])}</p></div></section>

 <p class="cite paper-source">Source: {S["authors"]} {S["title"]}. <i>{S["journal"]}</i> {S["year"]};{S["volume_pages"]}. doi:{S["doi"]}. Figures recreated from published data. Educational summary, not medical advice.</p>
</div>

'''
    if errs:
        print(f"== {slug}: {len(errs)} problem(s)"); [print("  ", e) for e in errs]; return False
    (d / "index.html").write_text(head + style + "</head>\n\n" + body + tail, encoding="utf8")

    # ---------- video props, storyboard, captions ----------
    fps = 30; T_TITLE, T_WHO, T_FIND, T_OUT = 120, 165, 180, 180
    vo = [(T_TITLE, S["vo_title"]), (T_WHO, render(S["vo_who"], False))]
    for h in S["hero"]: vo.append((T_FIND, render(h[3] if len(h) > 3 else h[1], False)))
    vo.append((T_OUT, render(S["vo_outro"], False)))
    props = {
        "citation": pj["citation"], "topic": S["topic"],
        "who": {"big": fmt(by[S["who_id"]], False), "label": strip(render(S["who_label"], False)), "design": S["who_design"]},
        "findings": [{"value": by[h[0]]["value"], "unit": by[h[0]].get("unit") or "", "decimals": by[h[0]].get("decimals"),
                      "status": by[h[0]]["status"], "headline": strip(render(h[1], False)),
                      "bars": [{"label": lab, "value": by[i]["value"], "unit": by[i].get("unit") or "", "decimals": by[i].get("decimals"),
                                "role": (S.get("arms", {}).get(by[i]["arm"]) if by[i]["arm"] else None) or ("intervention" if k == 0 else "comparator")}
                               for k, (i, lab) in enumerate(h[4])] if len(h) > 4 and h[4] else None}
                     for h in S["hero"]],
        "outro": strip(render(S["video_outro"], False)),
        "timing": {"title": T_TITLE, "who": T_WHO, "finding": T_FIND, "outro": T_OUT},
    }
    (OUT / f"{slug}.props.json").write_text(json.dumps(props, ensure_ascii=False, indent=1), encoding="utf8")
    def ts(fr):
        s = fr / fps; return f"{int(s//3600):02d}:{int(s%3600//60):02d}:{s%60:06.3f}"
    t = 0; cues = []; sb = []
    names = ["Title window pops open on the teal desktop", "Who was studied: enrollment counter"] + \
            [f"Hero finding {i+1}: counter ticks up" + (" with animated comparison bars" if len(h) > 4 and h[4] else "") for i, h in enumerate(S["hero"])] + \
            ["\"What changed\" card + citation"]
    ids = ["-", S["who_id"]] + [", ".join([h[0]] + ([x[0] for x in h[4]] if len(h) > 4 and h[4] else [])) for h in S["hero"]] + ["-"]
    for k, (dur, line) in enumerate(vo):
        cues.append(f"{k+1}\n{ts(t)} --> {ts(t+dur)}\n{line}\n")
        sb.append(f"| {k+1} | {t//fps}-{(t+dur)//fps}s | {names[k]} | {ids[k]} | \"{line}\" |")
        t += dur
    (d / "video.vtt").write_text("WEBVTT\n\n" + "\n".join(cues), encoding="utf8")
    (d / "storyboard.md").write_text(f"""# Storyboard: {S['short_name']} ({S['year']})
Format: 1920x1080 · 30 fps · {t//fps} s · style: site palette, Pixelify Sans numbers, window-frame "pop-up" transitions.

| # | Time | Visual (deterministic) | On-screen numbers (number ids) | Voiceover / caption |
|---|------|------------------------|--------------------------------|-----------|
""" + "\n".join(sb) + f"""

Rules: every number = paper.json value; primary vs secondary end points labeled as in the paper.

## B-roll prompts (optional, AI generator; NO text, numbers, or charts)
""" + "\n".join(f'- "{b}"' for b in S.get("broll", [])) + f"""
- No AI b-roll was used in the rendered video; all scenes are deterministic data visuals.

## Render notes
- Rendered with Remotion 4 (`PaperVideo` composition, 1920x1080, 30 fps, {t} frames) from `paper.json`; hero findings come from `paper.json.hero_findings`.
- Captions in `video.vtt` follow the lines above; no voiceover audio (video ships muted/autoplay-safe).
- Poster: frame 60 (title scene).
""", encoding="utf8")
    props["frames"] = t
    (OUT / f"{slug}.props.json").write_text(json.dumps(props, ensure_ascii=False, indent=1), encoding="utf8")

    card = f'''        <a class="window card" data-slug="{slug}" data-topic="{S["topic"].replace("&", "&amp;")}" data-year="{S["year"]}" href="/papers/{slug}/">
  <div class="titlebar"><span class="pix t-icon" data-pix="folder"></span><span class="t-text">{S["short_name"]}.paper</span></div>
  <img src="/papers/{slug}/poster.jpg" alt="{S["short_name"]} video thumbnail" loading="lazy">
  <div class="win-body"><span class="tag">{S["topic"].replace("&", "&amp;")}</span><h3>{S["short_name"]} ({S["year"]})</h3><p>{S["title"]}</p><p><b>{render(S["one_liner"], True).replace("<b>", "").replace("</b>", "")}</b></p></div>
 </a>
'''
    (OUT / f"{slug}.card.html").write_text(card, encoding="utf8")
    print(f"OK {slug}: {len(numbers)} numbers, {len(S['figures'])} figures, {t//fps}s video")
    return True

if __name__ == "__main__":
    ok = all([build(p) for p in sys.argv[1:]])
    sys.exit(0 if ok else 1)
