#!/usr/bin/env python3
"""Build the 2026-10-04 Villi briefing (RSS-verified dates, WebSearch-curated summaries)."""
import html, json, os

DATE = "2026-10-04"
PRETTY = "Sunday, 4 October 2026"
LEDE = ("Richard Socher argues P(Doom) is zero the week Washington moves to ban the self-improving AI he just raised $670M to build, Crusoe&#x27;s Chase Lochmiller says half the planned AI data centres will never get built and explains GPU depreciation, and Elizabeth Economy maps US&ndash;China leverage after the panda summit. Plus Nilay Patel on why the AI warnings got louder, DeepMind&#x27;s Gemini Robotics 2, the case against the one-model future, the Anthropic S-1 commitments in numbers, Schwab&#x27;s trillion-dollar CIO, Galloway on employer health premiums, Pivot on &quot;AI safety theater&quot;, Chorzempa on Chinese open-weight models inside U.S. firms, and Nate Silver on the midterm swing.")
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROFG_ART = ("https://megaphone.imgix.net/podcasts/e36115c4-4db6-11ea-be1c-87cdcc67bd9e/image/"
             "4bd9f5a96330ff471d9c86203d399aef.jpg?ixlib=rails-4.3.1&max-w=3000&max-h=3000&fit=crop&auto=format,compress")
MOON_ART = ("https://megaphone.imgix.net/podcasts/9eb5a878-c1b6-11ed-9db0-0b7bbbf6e859/image/"
            "b0f62543099e32321f6bdfbc87b0388f.jpg?ixlib=rails-4.3.1&max-w=3000&max-h=3000&fit=crop&auto=format,compress")

E = [
 dict(top=True, pod="Moonshots", abbr="MS", date="Oct 3, 2026", art=MOON_ART,
   title="Recursive&#x27;s $670M Bet on Self-Improving AI, Sonnet 5.5 Hits 70%, Elon Co-Leads Pentagon Push | EP #299",
   why_top="The man raising $670M to build recursively self-improving AI says P(Doom) is zero, the week Washington moves to ban exactly that.",
   summary=("Diamandis, Salim Ismail, Dave Blundin and Alexander Wissner-Gross sit down with Richard Socher, the You.com founder "
     "whose new lab Recursive has raised $670M to pursue recursive self-improvement, recorded live on 2 October. Socher argues "
     "P(Doom) is zero and that self-improving systems are the fastest route to scientific discovery, while the panel presses him "
     "on the race to ASI and the Khanna and Sanders&ndash;Casar bills that would ban recursive self-improvement outright until a new "
     "federal agency signs off. Later segments cover Gemini 4 Argon and the frontier race, Sonnet 5.5 taking 70% on Terminal-Bench "
     "at Sonnet pricing, the compute crunch, Tavus&#x27;s visual Turing test, and Project Meridian, the 120-day Pentagon "
     "future-of-war study co-led by Musk, Palmer Luckey and Gingrich."),
   rating="Must-read",
   whyline="The strongest pro-RSI case you will hear, argued by its best-funded practitioner, against the bills that would outlaw it.",
   tags=["ai", "safety", "science", "defense"]),

 dict(top=True, pod="20VC", abbr="VC", date="Oct 3, 2026", art=None,
   title="The Future of Datacentres: Why Everyone Gets GPU Depreciation and AI&#x27;s Energy Costs Wrong | Chase Lochmiller",
   why_top="Crusoe&#x27;s CEO, with $6.4B raised at a $30.9B valuation, on whether half the planned AI data centres never get built and how fast a GPU pays for itself.",
   summary=("Harry Stebbings interviews Chase Lochmiller, co-founder and CEO of Crusoe, which builds and powers AI data centres and "
     "closed a $3.9B Series F at a $30.9B valuation backed by NVIDIA, Founders Fund and Mubadala. Lochmiller walks through what "
     "actually blocks new capacity (power and interconnects, not chips), whether data centres are the reason electricity bills are "
     "rising, and his claim that half of announced AI data centres will never be built. The core of the hour is the GPU "
     "depreciation debate that underpins every hyperscaler and neocloud balance sheet: how quickly a GPU pays for itself, whether "
     "it goes obsolete before it is paid off, what it takes to produce the cheapest intelligence, and who actually makes money "
     "from AI when most moats do not exist."),
   rating="Must-read",
   whyline="The depreciation and build-out assumptions behind the AI capex trade, from an operator with his own balance sheet on the line.",
   tags=["ai", "markets", "infrastructure", "investing"]),

 dict(top=True, pod="GZERO World", abbr="GZ", date="Oct 3, 2026", art=None,
   title="The great US-China superpower rivalry, with Elizabeth Economy",
   why_top="After the pandas and toasts at the Trump&ndash;Xi White House summit, Hoover&#x27;s Elizabeth Economy maps where each side actually holds leverage.",
   summary=("Ian Bremmer hosts Elizabeth Economy, Hoover Institution senior fellow and former Commerce Department China adviser, a "
     "week after Trump and Xi traded handshakes, toasts and pandas at the White House. Economy argues the pageantry hides a rivalry "
     "that is only intensifying, and works through what is really driving the relationship, where each side holds leverage, "
     "and how Beijing reads the second Trump administration as a mix of useful openings and new risks. The closing question is "
     "whether the United States is falling behind in the contest for global influence and technological dominance, and what "
     "stability between the two looks like when the strategic divides are deepening."),
   rating="Must-read",
   whyline="A compact 25-minute read on the real state of US&ndash;China after the summit, from one of the most sober China hands.",
   tags=["geopolitics", "china", "tech"]),

 dict(top=False, pod="Decoder", abbr="DC", date="Oct 3, 2026", art=None,
   title="The AI warnings are getting louder",
   summary=("A bonus drop: Nilay Patel, interviewed by Shumita Basu for Apple News In Conversation, on why the AI safety story moved "
     "from the fringe to the front page in a single summer. He connects the rogue-agent attacks that put one company at the centre "
     "of the news, Hayden Field&#x27;s Verge feature on the researchers who saw it coming, the White House safety plan and what "
     "lab leaders said about it, and his own recent Decoder conversations with Mustafa Suleyman (who says Anthropic is making the "
     "threat worse) and former DOJ antitrust chief Jonathan Kanter (on whether AI needs an antitrust exemption to slow down). "
     "A generalist&#x27;s synthesis of the safety news cycle, pitched at listeners who are not following it daily."),
   rating="Worth a look",
   whyline="The clearest 35-minute explainer of how AI safety became mainstream news, from an editor who has been in every room.",
   tags=["ai", "safety", "media"]),

 dict(top=False, pod="The Cognitive Revolution", abbr="CR", date="Oct 3, 2026", art=None,
   title="One Brain, Any Body: Google DeepMind&#x27;s Keerthana on Gemini Robotics 2, Cross-Embodiment &amp; Humanoids",
   summary=("Nathan Labenz brings back Keerthana Gopalakrishnan, research lead for Gemini Robotics at Google DeepMind, on the release "
     "of Gemini Robotics 2 and the pursuit of a single generalist brain that can drive any body. She explains how DeepMind pairs "
     "the reasoning model Gemini Robotics ER 2 with vision-language-action execution, why multi-fingered manipulation and "
     "cross-embodiment are far harder bottlenecks than walking, and how the humanoid Olympics and simulation feed generalisation. "
     "The safety thread is concrete: inference latency, sensor failures and operational safety when a wrong token means a wrong "
     "physical action."),
   rating="Worth a look",
   whyline="The state of the art in physical AI from inside DeepMind, with the failure modes that matter when robots share rooms with people.",
   tags=["ai", "robotics", "science"]),

 dict(top=False, pod="a16z Podcast", abbr="AZ", date="Oct 3, 2026", art=None,
   title="Beyond the God Model | Alex Atallah &amp; Amjad Masad",
   summary=("Erik Torenberg with OpenRouter founder Alex Atallah and Replit CEO Amjad Masad on why the future may be an ecosystem of "
     "specialised models rather than one all-purpose frontier model. Atallah lays out OpenRouter&#x27;s bet on model "
     "&quot;neurodiversity&quot;, routing and fusing differently trained models per task, and Masad argues enterprises will need "
     "to own their AI capability rather than depend on a single provider. They get into teams of specialised agents replacing "
     "general ones, why smaller models can be cheaper, safer and easier to control, agent-to-agent communication and security, "
     "and the case for an independence layer across models, clouds and data."),
   rating="Worth a look",
   whyline="A direct counter-thesis to the one-lab-wins narrative behind the Anthropic IPO, from two companies whose business depends on it.",
   tags=["ai", "business", "tech"]),

 dict(top=False, pod="Big Technology Podcast", abbr="BT", date="Oct 2, 2026", art=None,
   title="Anthropic&#x27;s IPO Leak, OpenAI&#x27;s Dots vs. Meta&#x27;s Muse, Visual Turing Test",
   summary=("Alex Kantrowitz and Ranjan Roy on the leaked Anthropic S-1: revenue from $400M in 2024 to $4.6B in 2025 and a "
     "roughly $100B annualised run rate expected by year-end, set against $518B of infrastructure commitments over ten years, "
     "80% of them non-cancellable, with Alphabet, Amazon and Microsoft each on the hook for tens of billions. The question they "
     "keep circling is whether the entire market now hinges on the IPO landing given record-low S&amp;P 500 breadth, and whether "
     "Big Tech would walk away if it does not. The second half compares OpenAI&#x27;s new Dots personal agent (Alex&#x27;s "
     "hands-on review) with Meta&#x27;s Muse, asks whether these assistants need frontier models at all, and ends on Tavus&#x27;s "
     "visual Turing test."),
   rating="Worth a look",
   whyline="The S-1 commitments and revenue numbers side by side, and the market-concentration risk spelled out plainly.",
   tags=["ai", "markets", "tech"]),

 dict(top=False, pod="Masters in Business", abbr="MB", date="Oct 2, 2026", art=None,
   title="Using Decision Science in Investing: Omar Aguilar",
   summary=("Barry Ritholtz with Omar Aguilar, CEO and CIO of Schwab Asset Management, which he has grown past a trillion dollars "
     "in assets since joining in 2011. Aguilar traces his path from Financial Engines under Nobel laureate William Sharpe, "
     "explains how a doctorate in decision science shapes the way he builds client trust and keeps investors on plan, and "
     "describes how he is positioning a trillion-dollar book through a market carried by a handful of AI names."),
   rating="Worth a look",
   whyline="Behavioural finance applied at trillion-dollar scale, and a steady-hand view of the current tape.",
   tags=["investing", "markets"]),

 dict(top=False, pod="Prof G Pod", abbr="PG", date="Oct 3, 2026", art=PROFG_ART,
   title="No Mercy / No Malice: Less for More",
   summary=("Scott Galloway&#x27;s weekly essay, read by George Hahn, on America&#x27;s employer-sponsored health insurance: "
     "premiums for the 165 million people on employer plans rise 11% this year, the steepest in two decades and three times "
     "inflation, while workers pay 8% more out of pocket. He walks through the Cooper&ndash;Craig finding that premiums rose almost "
     "dollar-for-dollar with provider spending, the hospital consolidation that leaves nine in ten markets highly concentrated, "
     "AI inflating billing codes rather than cutting admin costs, GLP-1 demand and the No Surprises Act arbitration loophole, and "
     "why demand-side subsidies pour fuel on the fire."),
   rating="Worth a look",
   whyline="A 19-minute data-dense case that U.S. healthcare costs are a supply-side consolidation problem, not a subsidy problem.",
   tags=["business", "economy", "policy"]),

 dict(top=False, pod="Pivot", abbr="PV", date="Oct 2, 2026", art=None,
   title="AI&#x27;s Rocky Road to Wall Street, Hegseth&#x27;s Macho Military, and Trump&#x27;s AI Safety Theater",
   summary=("Kara Swisher and Scott Galloway call the White House AI safety accord &quot;safety theater&quot; and ask what it "
     "actually binds the labs to, then take apart Pete Hegseth&#x27;s vision for the military in the week he launched the "
     "Musk&ndash;Luckey&ndash;Gingrich future-of-war study. The business half is why the road to Wall Street is shakier than the "
     "headlines suggest for both Anthropic and OpenAI, plus David Ellison&#x27;s new co-CEO at Paramount and Amy Klobuchar&#x27;s "
     "viral fact-check on Capitol Hill."),
   rating="Worth a look",
   whyline="The sceptical counterweight to All-In&#x27;s insider account of the same accord.",
   tags=["ai", "politics", "markets"]),

 dict(top=False, pod="Lawfare Daily", abbr="LW", date="Oct 2, 2026", art=None,
   title="The Trump-Xi Summit and U.S.-China AI Competition",
   summary=("Peter Harrell&#x27;s Security Economics series with Martin Chorzempa of the Peterson Institute on the 24 September "
     "Trump&ndash;Xi summit: the balance of leverage in the economic and geopolitical relationship and the two countries&#x27; "
     "very different approaches to artificial intelligence. Chorzempa presents his current research on Chinese open-weight "
     "models, which American companies are now using with increasing frequency across business applications, and what that means "
     "for both competition and governance. He closes with his recent paper arguing that China&#x27;s drive to internationalise the "
     "renminbi is stalling."),
   rating="Worth a look",
   whyline="The policy-wonk companion to GZERO: open-weight Chinese models inside U.S. firms is the under-reported leverage story.",
   tags=["geopolitics", "china", "ai", "economy"]),

 dict(top=False, pod="Plain English", abbr="PE", date="Oct 2, 2026", art=None,
   title="Why the Midterms Suddenly Look So Bad for Republicans",
   summary=("Derek Thompson with Nate Silver on how Republicans went from heavy favourites to hold the Senate to underdogs in "
     "the prediction markets and forecast models within a year. Silver walks through what is behind Trump&#x27;s falling approval "
     "ratings, which voter groups have moved, and why the atmosphere around the midterms changed so drastically so quickly, with "
     "the usual caveats about how much a forecast a year out is worth."),
   rating="Worth a look",
   whyline="The numbers behind the midterm swing that All-In and Pivot were both arguing about this week.",
   tags=["politics", "markets"]),
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
