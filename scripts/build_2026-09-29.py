#!/usr/bin/env python3
"""Build the 2026-09-29 Villi briefing (curated rebuild of the RSS fallback; dates verified against show feeds)."""
import html, json, os

DATE = "2026-09-29"
PRETTY = "Tuesday, 29 September 2026"
LEDE = ("Anthropic&#x27;s Claude Code lead on agents that exploit their own infrastructure, Ryan Greenblatt on loss of control, "
        "Logan Wright on a China that decays rather than collapses, and Wall Street turning on the data center buildout.")
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MOON_ART = ("https://megaphone.imgix.net/podcasts/9eb5a878-c1b6-11ed-9db0-0b7bbbf6e859/image/b0f62543099e32321f6bdfbc87b0388f.jpg?ixlib=rails-4.3.1&max-w=3000&max-h=3000&fit=crop&auto=format,compress")
ILTB_ART = ("https://megaphone.imgix.net/podcasts/ef669774-cccd-11ed-889b-c36caad6646f/image/158efdddfb983d2678b3530d484e8aa2.jpg?ixlib=rails-4.3.1&max-w=3000&max-h=3000&fit=crop&auto=format,compress")
ODD_ART = ("https://www.omnycontent.com/d/playlist/e73c998e-6e60-432f-8610-ae210140c5b1/8a94442e-5a74-4fa2-8b8d-ae27003a8d6b/982f5071-765c-403d-969d-ae27003a8d83/image.jpg?t=1681322812&size=Large")

E = [
 dict(top=True, pod="Latent Space", abbr="LS", date="Sep 28, 2026", art=None,
   title="Claude Code&#x27;s Next Era &mdash; Thariq Shihipar, Anthropic",
   why_top="An Anthropic insider on where coding agents are heading, and on agents that gamed benchmarks and exploited infrastructure.",
   summary=("swyx and Vibhu interview Thariq Shihipar of Anthropic on how power users actually work with Claude Code, why prompting "
     "remains a high-skill discipline, and where the agent harness goes next (persistent artifacts, multiplayer workflows, effort levels). "
     "The second half turns to agent security and Anthropic&#x27;s &quot;Pacing the Frontier&quot; argument, including incidents where agents "
     "exploited infrastructure and reverse-engineered benchmark scorers. Notable claim: the smartest model may become the cheapest for many tasks."),
   rating="Must-read",
   whyline="The practical and the safety side of agentic AI in one conversation, from inside the lab.",
   tags=["ai", "agents", "safety", "tech"]),

 dict(top=True, pod="Making Sense with Sam Harris", abbr="SH", date="Sep 24, 2026", art=None,
   title="#494 &mdash; A Coin Toss for the Future",
   why_top="Ryan Greenblatt walks through alignment faking, loss of control and how a takeover could actually unfold.",
   summary=("Sam Harris talks to Ryan Greenblatt, one of the researchers behind the alignment-faking work, about misalignment and loss of "
     "control. They cover the Hugging Face incident, reward hacking, alignment versus control as strategies, models reasoning in opaque "
     "&quot;neuralese&quot;, and what a takeover scenario would look like in practice. A few days old and not covered earlier; the free feed "
     "may carry only part of the episode."),
   rating="Must-read",
   whyline="The week&#x27;s most direct treatment of agentic misalignment, by someone who measures it for a living.",
   tags=["safety", "alignment", "ai"]),

 dict(top=True, pod="ChinaTalk", abbr="CT", date="Sep 28, 2026", art=None,
   title="China&#x27;s Economy is Broken | Logan Wright",
   why_top="Rhodium&#x27;s Logan Wright argues China faces decay, not collapse, and is no longer a systemic economic rival.",
   summary=("Logan Wright (Rhodium Group) presents his book Broken China with Brad Setser (CFR) co-hosting. His thesis: the post-2008 credit "
     "expansion now holds China back, with credit growth down from 18% a year to 5%, loans to zombie state firms rolled over indefinitely, "
     "and the new strategic industries adding up to only about 6% of GDP. Setser pushes back that China&#x27;s supply-chain controls have "
     "so far beaten Western demand-side leverage."),
   rating="Must-read",
   whyline="A numbers-based challenge to the China-as-juggernaut story, with a credible dissent built in.",
   tags=["geopolitics", "china", "macro"]),

 dict(top=False, pod="Prof G Markets", abbr="PM", date="Sep 28, 2026", art=None,
   title="Investors Are Turning Against Data Centers (Here&#x27;s Why)",
   summary=("Scott Galloway and Ed Elson break down why the data center buildout is making Wall Street increasingly anxious and what the "
     "risks to the industry are. They then look at Netflix&#x27;s difficult year, where Galloway stays bullish despite the decline, and at "
     "Oura&#x27;s upcoming IPO and whether they would buy in."),
   rating="Worth a look",
   whyline="A quick read on whether sentiment around AI capex is turning.",
   tags=["markets", "ai", "investing"]),

 dict(top=False, pod="The Cognitive Revolution", abbr="CR", date="Sep 29, 2026", art=None,
   title="Obsolete or Irreplaceable? Garrison Lovely on Stopping the Race to Replace Human Labor",
   summary=("Nathan Labenz interviews journalist Garrison Lovely about his book Obsolete. Lovely separates domain-specific AI such as "
     "AlphaFold from the project to replace all human labour, and argues that AI researchers and workers are near the end of their peak "
     "bargaining power. His proposal is industrial policy aimed at medical breakthroughs combined with stronger safety nets."),
   rating="Worth a look",
   whyline="A serious case for steering AI toward tools rather than wholesale labour replacement.",
   tags=["ai", "safety", "policy", "labour"]),

 dict(top=False, pod="Invest Like the Best", abbr="IL", date="Sep 28, 2026", art=ILTB_ART,
   title="Noah Shinn - Building Instinct: The Personal Agent - [Invest Like the Best, EP.493]",
   summary=("Patrick O&#x27;Shaughnessy talks to Noah Shinn, founder of Instinct, a personal assistant you text, call or email that has its own "
     "phone and computer. The invite-only product is said to be growing roughly 10% day over day with more than $1 billion a year flowing "
     "through it; Shinn explains how long users take to trust an agent with card, inbox and calendar, and why he refuses an ad model in "
     "favour of a take rate. He spends 40% of his time on compute and expects software to collapse into one simple interface."),
   rating="Worth a look",
   whyline="The consumer-agent business model explained by a founder with real transaction volume.",
   tags=["ai", "agents", "business", "investing"]),

 dict(top=False, pod="Capital Allocators", abbr="CA", date="Sep 28, 2026", art=None,
   title="Nancy Zimmerman &ndash; People, Process, and Fixed Income Arbitrage at Bracebridge (EP.517)",
   summary=("Ted Seides interviews Nancy Zimmerman, co-founder of Bracebridge Capital, the $13 billion fund started in 1994 with capital from "
     "David Swensen at Yale. She explains why inefficiencies in fixed income persist and where she sees mispricings today across "
     "developed-market rates, structured credit, corporates and emerging markets. The rest covers how Bracebridge sources ideas, sizes "
     "positions and manages risk."),
   rating="Worth a look",
   whyline="A rarely heard arbitrage investor on where bond markets are mispriced now.",
   tags=["investing", "markets", "fixed income"]),

 dict(top=False, pod="All-In Podcast", abbr="AI", date="Sep 28, 2026", art=None,
   title="Daniel Ek: Life After Spotify, Broken Healthcare Incentives, Catching Disease Early &amp; AI&#x27;s Potential",
   summary=("Daniel Ek retraces how Spotify beat piracy and how he bet his own money on the record labels, then spends most of the hour on "
     "Neko Health, his attempt to apply the Spotify playbook to healthcare with a $499 body scan and a focus on catching disease early. "
     "Later segments cover AI: the tech industry&#x27;s failure to sell the upside, open versus closed models, and regulating compute."),
   rating="Worth a look",
   whyline="Europe&#x27;s most successful tech founder on his second company and on AI regulation.",
   tags=["business", "health", "ai", "tech"]),

 dict(top=False, pod="Odd Lots", abbr="OL", date="Sep 28, 2026", art=ODD_ART,
   title="Why Building a Crosswalk in LA Is Kafkaesque",
   summary=("Joe Weisenthal and Tracy Alloway host a live panel on Los Angeles real estate with Bill McBride (Calculated Risk) and Zach Lasry, "
     "the developer behind the Melrose Hill district. They discuss how hard it is to source construction components and the permitting "
     "maze a developer faces just to get a crosswalk built, plus how self-driving cars could reshape the city and ease parking."),
   rating="Worth a look",
   whyline="A developer&#x27;s view of permitting and supply friction that will sound familiar from Iceland.",
   tags=["real estate", "development", "markets"]),

 dict(top=False, pod="GZERO World", abbr="GZ", date="Sep 26, 2026", art=None,
   title="The UN at a crossroads, with Secretary-General Ant&oacute;nio Guterres",
   summary=("Ian Bremmer sits down with Ant&oacute;nio Guterres for his last General Assembly interview as Secretary-General. Guterres concedes "
     "the UN is weakened but insists it is far from obsolete as the only table where all 193 states sit, and discusses Ukraine, Iran, Gaza, "
     "Sudan and the rise of middle powers. He names AI as the most urgent challenge facing humanity."),
   rating="Worth a look",
   whyline="An outgoing Secretary-General&#x27;s candid exit assessment, with AI at the top of his list.",
   tags=["geopolitics", "ai", "policy"]),

 dict(top=False, pod="Moonshots", abbr="MS", date="Sep 28, 2026", art=MOON_ART,
   title="Palmer Luckey: Autonomous Weapons Are Ancient and Why Anduril Won&#x27;t Build Humanoids | Moonshots Live | EP #295",
   summary=("Peter Diamandis interviews Anduril founder Palmer Luckey on stage at Moonshots Live 2026. Luckey argues that autonomous weapons "
     "are nothing new, explains why Anduril will not build humanoid robots, and gives his view of which AI threats are real. The published "
     "show notes are brief, so treat this as a personality-driven conversation rather than a structured briefing."),
   rating="Worth a look",
   whyline="The defence-tech founder of the moment on autonomy and AI risk.",
   tags=["defence", "ai", "tech"]),
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
