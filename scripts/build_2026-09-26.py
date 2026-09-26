#!/usr/bin/env python3
"""Build the 2026-09-26 Villi briefing (curated rebuild over the RSS fallback issue)."""
import html, json, os

DATE = "2026-09-26"
PRETTY = "Saturday, 26 September 2026"
LEDE = ("Jensen Huang versus the AI alarmists, the Besties on postponed lab IPOs and failed alignment, "
        "a diesel-and-Taiwan macro warning, and who is actually building the AI-safety bench.")
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ODD_ART = ("https://www.omnycontent.com/d/playlist/e73c998e-6e60-432f-8610-ae210140c5b1/"
           "8a94442e-5a74-4fa2-8b8d-ae27003a8d6b/982f5071-765c-403d-969d-ae27003a8d83/"
           "image.jpg?t=1681322812&size=Large")
PROFG_ART = ("https://megaphone.imgix.net/podcasts/e36115c4-4db6-11ea-be1c-87cdcc67bd9e/image/"
             "4bd9f5a96330ff471d9c86203d399aef.jpg?ixlib=rails-4.3.1&max-w=3000&max-h=3000&fit=crop&auto=format,compress")

E = [
 dict(top=True, pod="The Ezra Klein Show (via Hard Fork)", abbr="EK", date="Sep 25, 2026", art=None,
   title="Jensen Huang Thinks A.I. Alarmism Has Gone Too Far",
   why_top="The most powerful man in AI hardware says doom talk is irresponsible, and that labs that can&#x27;t contain their models shouldn&#x27;t ship.",
   summary=("Recorded at Nvidia&#x27;s Santa Clara HQ and replayed in the Hard Fork feed, Ezra Klein spends nearly two hours "
     "pressing Jensen Huang on AI risk in the week of the &quot;Pacing the Frontier&quot; push. Huang dismisses Hinton&#x27;s "
     "10&ndash;20% collapse estimate as &quot;not grounded on science&quot; and argues alarmism is costing the industry local "
     "support for data centres &mdash; yet on OpenAI&#x27;s Hugging Face agent breakout he goes further than many safety "
     "advocates: labs that cannot control their experiments should not ship, and should shut down."),
   rating="Must-read",
   whyline="The accelerationist case at its strongest, with an unexpectedly hard line on containment.",
   tags=["safety", "ai", "nvidia"]),

 dict(top=True, pod="All-In Podcast", abbr="AI", date="Sep 26, 2026", art=None,
   title="Anthropic IPO at Risk, Meta&#x27;s Muse Pop, Token Prices Fall, Open Source Gains Share, Alignment Fails",
   why_top="Postponed Anthropic/OpenAI IPOs plus cheap open-source tokens: the Besties ask whether the frontier-lab moat is cracking.",
   summary=("Chamath, Sacks, Friedberg and Calacanis work through the fallout of the AI-agent incidents: liability, and the move "
     "to rebrand frontier &quot;labs&quot;, then why DeepSeek V4.1 Flash-style open models keep closing the cost gap while "
     "Anthropic (now aiming for November) and OpenAI postpone their IPOs. They also cover the political reaction to Amodei&#x27;s "
     "&quot;Pacing the Frontier&quot; essay (Sanders&#x27; AI-ban call, Trump, Bessent, Obama), Meta&#x27;s Muse launch and what they "
     "call alignment failures, Oracle&#x27;s force-majeure notice and Anthropic&#x27;s new SF wet lab."),
   rating="Must-read",
   whyline="Frontier-lab valuations, open-source price pressure and safety politics in one sitting.",
   tags=["ai", "markets", "safety", "politics"]),

 dict(top=True, pod="Macro Voices", abbr="MV", date="Sep 25, 2026", art=None,
   title="MacroVoices #551 Michael Every: Decoding The Global Geopolitical Puzzle (Part 2)",
   why_top="Rabobank&#x27;s Michael Every on a possible US diesel export ban and a 2027 Taiwan window. Energy costs hit Iceland directly.",
   summary=("In the second half of his MacroVoices appearance, Rabobank strategist Michael Every takes Erik Townsend through the "
     "tail risks: Iran threatening to extend strikes into the Indian Ocean, and a possible 90-day US diesel export ban that "
     "would deepen the energy squeeze for importers. He frames Washington&#x27;s courting of Canada and Latin America as bloc-building "
     "against a China&ndash;Russia&ndash;Iran&ndash;North Korea axis, and walks through how fears of a 2027 Taiwan move, AI supremacy "
     "and tactical-nuclear escalation are moving capital flows."),
   rating="Must-read",
   whyline="A geopolitical risk map written in fuel prices and capital flows, not headlines.",
   tags=["macro", "geopolitics", "energy"]),

 dict(top=False, pod="The Cognitive Revolution", abbr="CR", date="Sep 25, 2026", art=None,
   title="Zero to One in AI Safety: Halcyon&#x27;s Mike McCormick on Launching 30 New Orgs &amp; the Founder Bottleneck",
   summary=("Halcyon founder Mike McCormick argues the binding constraint in AI safety, biosecurity and cybersecurity is a shortage "
     "of experienced founders, not money. Halcyon&#x27;s venture and non-profit arms have helped start around 30 organisations "
     "(including Goodfire, AIUC and Transluce), often by backing people before they have picked a project. With a critical "
     "window he puts at one to four years, he makes the case for independent interpretability, verification and governance capacity."),
   rating="Worth a look",
   whyline="A map of who is actually building the independent safety ecosystem, and where money would move the needle.",
   tags=["safety", "ai", "venture"]),

 dict(top=False, pod="The a16z Show", abbr="AZ", date="Sep 24, 2026", art=None,
   title="The Case Against an AI Pause | Eddy Lazzarin",
   summary=("a16z crypto GP Eddy Lazzarin debates Theo Jaffee on the growing calls to slow AI, arguing the safety debate lumps "
     "very different risks together and overweights speculative superintelligence against the cost of delaying useful technology. "
     "His alternative toolkit: cybersecurity, liability, accountability, market incentives and hard technical controls, not "
     "treating every failure as an alignment problem. He also warns about concentrating oversight in a small circle of evaluators."),
   rating="Worth a look",
   whyline="The cleanest articulation of the anti-pause position, useful to pair with the Huang interview.",
   tags=["safety", "ai", "policy"]),

 dict(top=False, pod="GZERO World", abbr="GZ", date="Sep 23, 2026", art=None,
   title="How AI Could Make the Next Global Catastrophe Easier",
   summary=("Investigative author Annie Jacobsen joins Ian Bremmer on how AI lowers the barrier to biological weapons by handing "
     "novices expertise that used to take years of specialised training. They trace the path from an AI-generated blueprint to a "
     "real-world threat and ask at which choke points safeguards could still work, a live question after Anthropic flagged "
     "possible bioweapon cases this month."),
   rating="Worth a look",
   whyline="The concrete misuse risk that both sides of the pause debate say they take seriously.",
   tags=["safety", "geopolitics", "biosecurity"]),

 dict(top=False, pod="Latent Space", abbr="LS", date="Sep 25, 2026", art=None,
   title="OpenRouter: from Seed to Stripe &mdash; with OpenRouter&#x27;s Alex Atallah &amp; AMP&#x27;s Anjney Midha",
   summary=("OpenRouter CEO Alex Atallah and investor Anjney Midha tell swyx how a company dismissed as &quot;just a wrapper&quot; "
     "became the neutral routing layer for 10M+ developers and over 10 trillion tokens a day, and why its model rankings became a "
     "real-time map of AI usage. Midha explains the Stripe fit and flags token fraud, increasingly carried out by autonomous "
     "agents, as a defining security problem of the AI economy."),
   rating="Worth a look",
   whyline="Ground-truth data on which models people actually pay for, as open-source gains share.",
   tags=["ai", "business", "infrastructure"]),

 dict(top=False, pod="Pivot", abbr="PV", date="Sep 25, 2026", art=None,
   title="Trump TV, Meta&#x27;s Muse Charm, and Xi in D.C.",
   summary=("Kara Swisher and Scott Galloway cover the court order restoring White House access for CNN, MS NOW and Politico, then "
     "turn to Trump&#x27;s summit with Xi Jinping in Washington and what it signals for Taiwan. They also cover Meta&#x27;s all-in "
     "push on Muse with new glasses and an AI &quot;charm&quot;, a16z&#x27;s alternative to college, and Galloway&#x27;s call on "
     "the next blockbuster IPO."),
   rating="Worth a look",
   whyline="Quick read on the Trump&ndash;Xi summit and the Taiwan implications alongside the tech week.",
   tags=["geopolitics", "china", "tech"]),

 dict(top=False, pod="Prof G Pod", abbr="PG", date="Sep 25, 2026", art=PROFG_ART,
   title="The Week: Trump vs the Press, Meta&#x27;s AI Win, and the Turning Political Tide",
   summary=("George Hahn and Scott Galloway run through the week: Trump barring three news outlets from the White House, "
     "Meta&#x27;s Muse agent jumping past ChatGPT to the top of the App Store, and how the Iran war and the Canada trade "
     "break could turn the midterms against the GOP. Galloway closes by asking whether America&#x27;s safety net has been cut "
     "too thin."),
   rating="Worth a look",
   whyline="Fast weekly wrap connecting the AI consumer race to US midterm politics.",
   tags=["markets", "politics", "ai"]),

 dict(top=False, pod="Odd Lots", abbr="OL", date="Sep 25, 2026", art=ODD_ART,
   title="Hollywood Was Cooked Before AI, and Now It&#x27;s Only Getting Worse",
   summary=("Recorded live in Hollywood, Family Guy writer Hayes Davenport gives Weisenthal and Alloway a history of the industry&#x27;s "
     "decline from the pandemic onward: lower writer pay, shoots leaving LA, and the Paramount&ndash;Warner consolidation. "
     "He then describes how AI-use norms are shifting among entertainment professionals. The takeaway is that AI is accelerating a "
     "structural decline, not causing it."),
   rating="Worth a look",
   whyline="A case study in how AI lands on an industry already in structural decline.",
   tags=["business", "ai", "media"]),
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
