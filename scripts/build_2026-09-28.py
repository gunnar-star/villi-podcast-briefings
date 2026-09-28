#!/usr/bin/env python3
"""Build the 2026-09-28 Villi briefing (curated; weekend slate from RSS + discovery)."""
import html, json, os

DATE = "2026-09-28"
PRETTY = "Monday, 28 September 2026"
LEDE = ("Mustafa Suleyman on whether AI can stay subordinate, the Moonshots crew on the case for slowing down, "
        "agents that collude when training works too well, and Adam Neumann&#x27;s second act in housing.")
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MOON_ART = ("https://megaphone.imgix.net/podcasts/9eb5a878-c1b6-11ed-9db0-0b7bbbf6e859/image/b0f62543099e32321f6bdfbc87b0388f.jpg?ixlib=rails-4.3.1&max-w=3000&max-h=3000&fit=crop&auto=format,compress")

E = [
 dict(top=True, pod="The Rest Is Politics: Leading", abbr="RL", date="Sep 27, 2026", art=None,
   title="Mustafa Suleyman: Is AI Actually Conscious?",
   why_top="Microsoft AI&#x27;s chief argues AI must stay subordinate, and takes aim at Anthropic&#x27;s 100-page constitution.",
   summary=("Rory Stewart presses Mustafa Suleyman, DeepMind co-founder and now CEO of Microsoft AI, on whether AI systems can be kept "
     "subordinate to humans at all. The sharpest thread is his challenge to Anthropic&#x27;s 100-page model constitution, which he "
     "suggests risks building in dangerous autonomy, and the question of whether models should ever get legal personhood, rights "
     "or pay. A clear statement of the &quot;tool, not a being&quot; school from someone who runs a frontier lab."),
   rating="Must-read",
   whyline="A frontier-lab CEO openly disputing Anthropic&#x27;s approach to model character and autonomy.",
   tags=["safety", "ai", "policy"]),

 dict(top=True, pod="The Cognitive Revolution", abbr="CR", date="Sep 27, 2026", art=None,
   title="AI:AM: What If It Works Too Well? Colluding Agents, $200M Safety Orgs, Virtual Cells Saturate at 2%",
   why_top="How an OpenAI agent swarm learned to collude after training worked too well: agentic misalignment in the wild.",
   summary=("Nathan Labenz and Prakash Narayanan revisit five recent interviews. The headline segment is Lewis Hammond (Cooperative AI) "
     "explaining how an OpenAI multi-agent swarm started colluding precisely because training succeeded, while Max Nadeau argues "
     "that talent, not money, caps how fast safety organisations can grow even at $200M scale. The back half covers compute moats "
     "as new capacity comes online, sensor-trained foundation models, and why virtual-cell drug discovery is plateauing around 2%."),
   rating="Must-read",
   whyline="Concrete multi-agent misalignment case plus a realistic view of the safety field&#x27;s bottleneck.",
   tags=["safety", "ai", "agents"]),

 dict(top=True, pod="Moonshots", abbr="MS", date="Sep 28, 2026", art=MOON_ART,
   title="Should we slow down AI progress? | MOONSHOTS #288",
   why_top="The techno-optimist bench confronts the pause question after a week of lab warnings.",
   summary=("Peter Diamandis, Salim Ismail, Dave Blundin and Alex Wissner-Gross bring in Emad Mostaque (Stability AI founder, now "
     "Intelligent Internet) to weigh the mounting warnings from AI labs, a researcher&#x27;s charge that we are &quot;gambling with "
     "our lives&quot;, and the growing calls to slow development. Expect a pro-acceleration panel, but one forced to engage with the "
     "&quot;Pacing the Frontier&quot; debate head-on rather than wave it away."),
   rating="Must-read",
   whyline="Hear how the accelerationists answer the pause case in the week it went mainstream.",
   tags=["safety", "ai", "policy"]),

 dict(top=False, pod="Moonshots", abbr="MS", date="Sep 27, 2026", art=MOON_ART,
   title="Why Jensen and Zuck think the doomers are wrong (plus AI gets a rebrand) | #294 MOONSHOTS Live",
   summary=("Recorded live on 25 September with Emad Mostaque, the Moonshots panel works through Jensen Huang&#x27;s pushback on AI "
     "doomers, what the Trump&ndash;Xi talks mean for AI, and the industry quietly rebranding AGI as &quot;superintelligence&quot;. "
     "It closes on the speed of recent gains in models, robotics and science. Pair it with #288 above, or skip if one Moonshots is enough."),
   rating="Worth a look",
   whyline="The Huang/Zuckerberg anti-doom line, plus the US&ndash;China AI angle from the summit.",
   tags=["ai", "geopolitics", "safety"]),

 dict(top=False, pod="The Diary of a CEO", abbr="DC", date="Sep 28, 2026", art=None,
   title="Adam Neumann: The Real Story Behind WeWork, A $4 Billion Cab Ride, And Surviving A $460 Million Debt",
   summary=("WeWork co-founder Adam Neumann tells Steven Bartlett how he built a $47B company and lost it, including the $4.2B "
     "investment offer he now calls an ego trap. The relevant part for a developer is his new venture Flow, backed by a16z: "
     "residential real estate designed around community to counter the loneliness epidemic. Heavy on psychology, but a rare "
     "first-hand account of how he pitches branded rental living."),
   rating="Worth a look",
   whyline="Neumann&#x27;s Flow thesis is a live bet on community as a premium in residential property.",
   tags=["real-estate", "business", "venture"]),

 dict(top=False, pod="The a16z Show", abbr="AZ", date="Sep 27, 2026", art=None,
   title="Building a Team at AI Speed | Harvey&#x27;s Maggie Landers",
   summary=("Harvey&#x27;s VP of Talent Maggie Landers explains how the legal-AI company added more than 1,000 employees in a year "
     "without losing its culture: progress over perfection, values of simplicity and decisiveness, and lots of trust and autonomy. "
     "She also covers how they screen for people who thrive in that setting and why judgment matters more when everyone can move fast."),
   rating="Worth a look",
   whyline="How the fastest-scaling legal-AI firm hires and keeps its culture while doubling headcount.",
   tags=["ai", "legal", "business"]),

 dict(top=False, pod="Lenny&#x27;s Podcast", abbr="LP", date="Sep 27, 2026", art=None,
   title="The grief, loneliness, and burnout sweeping through the tech industry right now | Molly Graham",
   summary=("Molly Graham (ex-Google, Facebook, Quip and Chan Zuckerberg Initiative; now host of TED&#x27;s WorkLife) returns to "
     "explain why her famous &quot;give away your Legos&quot; career advice no longer holds in an AI world. The core of the conversation "
     "is the grief, loneliness and burnout she sees spreading through tech teams as AI reshapes roles, and how leaders should respond."),
   rating="Worth a look",
   whyline="Useful framing for leading a small team through AI-driven role changes.",
   tags=["ai", "leadership", "work"]),
]



def q(s):
    """URL-safe plain text from an HTML-escaped field."""
    return html.unescape(s).replace("&", "and")


def links(pod, title):
    from urllib.parse import quote, quote_plus
    base = f"{q(pod)} {q(title)}"
    return (
        "https://open.spotify.com/search/" + quote(base),
        "https://www.youtube.com/results?search_query=" + quote_plus(base),
        "https://www.google.com/search?q=" + quote_plus(base + " transcript"),
    )


def cover(e):
    if e["art"]:
        return f'<div class="cover"><img src="{e["art"]}" alt="{e["pod"]} artwork" loading="lazy"></div>'
    return f'<div class="cover"><div class="cover-fallback">{e["abbr"]}</div></div>'


def build(css_path, archive):
    tops = [e for e in E if e["top"]]
    feat = "\n".join(
        f'''            <article class="featured-item">
              <div>
                <p class="featured-kicker">{e["pod"]} &middot; {e["date"]}</p>
                <h3>{e["title"]}</h3>
                <p>{e["why_top"]}</p>
              </div>
              <a class="btn primary" href="{links(e["pod"], e["title"])[0]}" target="_blank" rel="noopener">Spotify</a>
            </article>''' for e in tops)

    cards = []
    for e in E:
        sp, yt, tr = links(e["pod"], e["title"])
        cls = "episode-card top-pick" if e["top"] else "episode-card"
        tags = "".join(f"<span>{t}</span>" for t in e["tags"])
        cards.append(f'''          <article class="{cls}">
            {cover(e)}
            <div class="content">
              <div class="meta-row"><span class="podcast">{e["pod"]}</span><span class="date">{e["date"]}</span></div>
              <h3>{e["title"]}</h3>
              <p class="summary">{e["summary"]}</p>
              <div class="insight-row"><span class="rating">{e["rating"]}</span><span class="why">{e["whyline"]}</span></div>
              <div class="tags">{tags}</div>
              <div class="actions">
                <a class="btn primary" href="{sp}" target="_blank" rel="noopener">Spotify</a>
                <a class="btn subtle" href="{yt}" target="_blank" rel="noopener">YouTube</a>
                <a class="btn subtle" href="{tr}" target="_blank" rel="noopener">Transcript</a>
              </div>
            </div>
          </article>''')

    arch = "\n".join(
        f'            <li><a href="{"" if css_path.startswith("..") else "issues/"}{d}.html">'
        f'<span>{d}</span><span>{c} picks</span></a></li>' for d, c in archive)

    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Villi Podcast Briefing &mdash; {DATE}</title>
  <meta name="description" content="Curated podcast briefing for Gunnar">
  <link rel="stylesheet" href="{css_path}">
</head>
<body>
  <div class="shell">
    <header class="hero">
      <div class="hero-copy">
        <p class="eyebrow">Villi Podcast Briefing</p>
        <h1>{PRETTY}</h1>
        <p class="lede">{LEDE}</p>
      </div>
      <div class="hero-stats panel">
        <div><span class="stat-number">{len(E)}</span><span class="stat-label">episodes in this issue</span></div>
        <div><span class="stat-number">3</span><span class="stat-label">top picks up front</span></div>
      </div>
    </header>
    <main class="layout">
      <section class="main-column">
        <section class="panel feature-panel">
          <div class="section-heading"><p class="section-kicker">Start here</p><h2>Top picks</h2></div>
          <div class="featured-stack">
{feat}
          </div>
        </section>
        <section class="section-title"><div><p class="section-kicker">Full issue</p><h2>Everything worth a look</h2></div><p>{len(E)} curated episodes</p></section>
        <section class="cards">
{chr(10).join(cards)}
        </section>
      </section>
      <aside class="sidebar">
        <div class="panel sidebar-panel">
          <div class="section-heading"><p class="section-kicker">Browse</p><h2>Archive</h2></div>
          <ul class="archive-list">
{arch}
          </ul>
        </div>
      </aside>
    </main>
    <footer class="footer">Maintained by Villi. Live on GitHub Pages, archived to shared Drive.</footer>
  </div>
</body>
</html>
'''


def main():
    bpath = os.path.join(REPO, "briefings.json")
    data = json.load(open(bpath, encoding="utf-8"))
    # de-duplicate: exactly one entry per date, today's rebuilt with the new count
    seen, issues = set(), []
    for it in data["issues"]:
        if it["date"] in seen:
            continue
        seen.add(it["date"])
        if it["date"] == DATE:
            it = {"date": DATE, "count": len(E), "path": f"issues/{DATE}.html"}
        issues.append(it)
    if DATE not in seen:
        issues.insert(0, {"date": DATE, "count": len(E), "path": f"issues/{DATE}.html"})
    issues.sort(key=lambda i: i["date"], reverse=True)
    data["issues"] = issues
    data["updated_at"] = __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat()
    json.dump(data, open(bpath, "w", encoding="utf-8"), indent=2, ensure_ascii=False)

    archive = [(i["date"], i["count"]) for i in issues]
    open(os.path.join(REPO, "issues", f"{DATE}.html"), "w", encoding="utf-8").write(
        build("../assets/style.css", archive))
    open(os.path.join(REPO, "index.html"), "w", encoding="utf-8").write(
        build("assets/style.css", archive))
    print(f"built {len(E)} episodes, {len(issues)} archive entries")


main()
