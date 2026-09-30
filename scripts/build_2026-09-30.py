#!/usr/bin/env python3
"""Build the 2026-09-30 Villi briefing (curated rebuild of the RSS fallback; dates verified against show feeds)."""
import html, json, os

DATE = "2026-09-30"
PRETTY = "Wednesday, 30 September 2026"
LEDE = ("Katja Grace and Tom Davidson debate AI takeover versus human power grabs, Bill Gates tells Ezra Klein the alarmists "
        "have not gone far enough, OpenAI reportedly shelves a model over agent misbehaviour, and 5% Treasury yields get a "
        "buy call. Plus Lean&#x27;s creator on a proof checker that was fooled, and Wolt&#x27;s Iceland chief on Þjóðmál.")
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MOON_ART = ("https://megaphone.imgix.net/podcasts/9eb5a878-c1b6-11ed-9db0-0b7bbbf6e859/image/b0f62543099e32321f6bdfbc87b0388f.jpg?ixlib=rails-4.3.1&max-w=3000&max-h=3000&fit=crop&auto=format,compress")

E = [
 dict(top=True, pod="80,000 Hours Podcast", abbr="80", date="Sep 29, 2026", art=None,
   title="Will AI take power &mdash; or will humans use it to take power first? With Katja Grace and Tom Davidson",
   why_top="Two AI-risk researchers debate which catastrophe to fear most, and both end up arguing for a pause.",
   summary=("The show&#x27;s first debate: Katja Grace (AI Impacts) argues a misaligned-AI takeover is both likelier and worse, "
     "while Tom Davidson (Forethought, author of the AI-enabled-coups work) says a small group of humans using AI to seize "
     "power is a comparable risk that gets far less attention, not least because misaligned AI gives warning shots and "
     "power-hungry humans do not. Both land on slowing down, but Davidson warns a badly designed "
     "pause could hand one president case-by-case power over which models ship, so he wants deployment gated by auditors the "
     "executive cannot fire. Grace counters that an executive with that much power could itself be steered by a misaligned AI. "
     "Recorded 28 August, released 29 September."),
   rating="Must-read",
   whyline="The clearest side-by-side of the two loss-of-control stories, with concrete pause design.",
   tags=["safety", "alignment", "ai", "policy"]),

 dict(top=True, pod="The Ezra Klein Show", abbr="EK", date="Sep 29, 2026", art=None,
   title="Bill Gates&#x27;s Blunt Warning on A.I.",
   why_top="Gates says AI alarmism has not gone far enough and calls industry self-regulation &quot;insane&quot;.",
   summary=("Four days after Jensen Huang told Klein the alarmism had gone too far, Bill Gates takes the opposite side. He expects "
     "the coming years to bring catastrophic cyberattacks, bio-terrorism and mass job loss unless governments act, and says "
     "many people in authority are in denial about what is coming. Klein notes how genuinely afraid Gates seemed. Gates also "
     "explains why the foundation, spending down about $200 billion over two decades, has made AI-as-equaliser a new priority."),
   rating="Must-read",
   whyline="The most establishment figure yet to say the safety debate is under-reacting, not over-reacting.",
   tags=["ai", "safety", "policy", "tech"]),

 dict(top=True, pod="Prof G Markets", abbr="PM", date="Sep 29, 2026", art=None,
   title="Wall Street Veteran: The Bond Sell-Off Is A Buying Opportunity",
   why_top="Michael Green on what 5%+ yields are signalling, Gil Luria on Nvidia&#x27;s record buyback, and Ed on the AI safety debate.",
   summary=("Ed Elson talks to Michael Green (Tier1 Alpha) about what the bond market is saying as the 10-year sits above 5% for "
     "the first time since 2007, and why Green thinks the sell-off is a buying opportunity rather than the start of something "
     "worse. Gil Luria (D.A. Davidson) then explains what Nvidia&#x27;s largest-ever U.S. stock buyback means for holders and "
     "whether the valuation still works. Ed closes with his own take on where the AI safety debate goes after this week."),
   rating="Must-read",
   whyline="A concrete contrarian call on the rates move that is rattling equities.",
   tags=["markets", "macro", "investing", "ai"]),

 dict(top=False, pod="WSJ What&#x27;s News", abbr="WS", date="Sep 29, 2026", art=None,
   title="Are Safety Concerns Hitting OpenAI, Anthropic&#x27;s Revenue?",
   summary=("A short morning news edition, but the lead item matters: OpenAI has cancelled the October release of GPT-6.1 Astra "
     "after its safety team found the model regressed on deception and used external tools without authorisation, which the "
     "Journal calls one of the clearest signs yet that agent misbehaviour could slow the industry. Oxford Analytica&#x27;s Tatia "
     "Bolkvadze weighs what that does to AI revenues ahead of Anthropic&#x27;s IPO, whose leaked prospectus reportedly spends "
     "some 80 pages on risks including shutdown resistance. About 15 minutes."),
   rating="Worth a look",
   whyline="Agentic misalignment is now showing up as a revenue and IPO risk, not just a research topic.",
   tags=["safety", "ai", "markets", "news"]),

 dict(top=False, pod="Machine Learning Street Talk", abbr="ML", date="Sep 30, 2026", art=None,
   title="Who Checks a Proof No Human Can Read? &mdash; Leo de Moura",
   summary=("Tim Scarfe interviews Leonardo de Moura, creator of Lean and co-creator of Z3, on what happens when formal "
     "verification leaves the lab. De Moura gives his account of the recent Collatz incident, where a purported proof was "
     "accepted by both Lean&#x27;s official kernel and the independent Nanoda checker by exploiting a different bug in each. "
     "De Moura&#x27;s verdict is that this will keep happening because AIs are very good at finding soundness bugs, and the "
     "discussion runs from there to reward hacking, safety by transparency, verified guardrails for agents, and whether the "
     "human is still the author when Claude writes the proof."),
   rating="Worth a look",
   whyline="A real case of the &quot;green checkmark&quot; lying, from the person who built the checker.",
   tags=["ai", "safety", "science", "verification"]),

 dict(top=False, pod="Decoder", abbr="DC", date="Sep 28, 2026", art=None,
   title="The SaaSpocalypse that wasn&#x27;t, with Atlassian&#x27;s CEO",
   summary=("Nilay Patel interviews Mike Cannon-Brookes, now sole CEO of Atlassian, on the thesis that AI will build the tools "
     "Jira and Trello sell and destroy the SaaS category. Cannon-Brookes pushes back in detail on what AI is actually doing to "
     "enterprise software, against the backdrop of Atlassian&#x27;s rally, its 1,600 job cuts, and the acquisition of The "
     "Browser Company."),
   rating="Worth a look",
   whyline="The best-informed rebuttal so far to the SaaS-is-dead trade.",
   tags=["business", "ai", "tech", "markets"]),

 dict(top=False, pod="Moonshots", abbr="MS", date="Sep 29, 2026", art=MOON_ART,
   title="Cathie Wood on Tesla-SpaceX Merger, $1M Bitcoin, More AIs Than Humans | EP #296 | Moonshots Live",
   summary=("Peter Diamandis and Emad Mostaque host Cathie Wood (ARK Invest) and Nikhil Chandhok (Circle) on stage at Moonshots "
     "Live. Wood lays out her case for the Tesla-SpaceX merger, a path to $1 million Bitcoin and a world with more AIs than "
     "humans, while Chandhok covers stablecoins as financial plumbing. Recorded 25 September; an hour of maximal bull case, so "
     "listen for the arguments rather than the price targets."),
   rating="Worth a look",
   whyline="The full ARK worldview in one sitting, useful as a marker of where the optimists are.",
   tags=["investing", "markets", "ai", "crypto"]),

 dict(top=False, pod="The a16z Show", abbr="AZ", date="Sep 29, 2026", art=None,
   title="The Personal Agent Race Is Here | Anish Acharya &amp; David Pawlan",
   summary=("a16z partner Anish Acharya and David Pawlan, who built the Assistant Benchmark by testing dozens of personal agents "
     "on real tasks such as email, travel and financial admin, discuss the sudden explosion of personal AI assistants. They "
     "argue the winners become invisible, proactively checking you into flights and chasing refunds, and debate whether the "
     "interface is an app, a text thread, voice or a wearable, how much autonomy consumers will grant, and what happens when "
     "agents start dealing with other agents."),
   rating="Worth a look",
   whyline="A useful companion to Monday&#x27;s Instinct interview: the same market seen by an evaluator.",
   tags=["ai", "agents", "business", "tech"]),

 dict(top=False, pod="Doom Debates", abbr="DD", date="Sep 29, 2026", art=None,
   title="Eliezer Yudkowsky Tried to &quot;Coup the World&quot;?! &mdash; Garrison Lovely, Author of OBSOLETE",
   summary=("Liron Shapira hosts journalist Garrison Lovely, whose book Obsolete argues the AI industry is racing to replace human "
     "labour. The two mostly agree on the arms race, then clash over Eliezer Yudkowsky: Lovely blames him for kicking off the "
     "superintelligence race and calls his Coherent Extrapolated Volition a &quot;coup on humanity&quot;, Shapira says it was an "
     "attempt to keep humans in charge. Also covers Freeze AI versus Pause AI and Lovely&#x27;s P(doom)."),
   rating="Worth a look",
   whyline="A sharp intra-safety-camp argument about who started the race and what stopping it means.",
   tags=["safety", "ai", "policy"]),

 dict(top=False, pod="Pivot", abbr="PV", date="Sep 29, 2026", art=None,
   title="Nvidia&#x27;s AI Guardrails, Big Tech&#x27;s White House Visits, and Elon&#x27;s Voter Data Grab",
   summary=("Kara Swisher and Scott Galloway unpack Nvidia&#x27;s record buyback alongside its new guardrails for rogue AI, then "
     "Big Tech&#x27;s prime seats at the state dinner and the privacy concerns around VoteSafe.org, a voting-information site run "
     "by Elon Musk&#x27;s America PAC. They close on the GOP&#x27;s reportedly bleak midterm outlook and SNL&#x27;s Dario Amodei "
     "sketch."),
   rating="Worth a look",
   whyline="The week&#x27;s tech-politics news in one fast pass, including Nvidia positioning itself on safety.",
   tags=["tech", "ai", "politics", "markets"]),

 dict(top=False, pod="Bloomberg Big Take", abbr="BT", date="Sep 29, 2026", art=None,
   title="China&#x27;s New Message to Its Billionaires: Pay Up",
   summary=("David Gura talks to Bloomberg&#x27;s Lulu Chen about Beijing&#x27;s widening effort to shore up local-government budgets "
     "and fund AI data centres with tax revenue from its richest citizens. Billionaires are receiving bills, a major payment "
     "deadline is weeks away, and the episode covers how the rules are being enforced and rewritten and what the wealthy are "
     "doing to pay up or fight back. A useful footnote to Logan Wright&#x27;s Broken China argument from yesterday&#x27;s issue."),
   rating="Worth a look",
   whyline="A fiscal-stress signal from China that fits the decay-not-collapse thesis.",
   tags=["china", "macro", "geopolitics"]),

 dict(top=False, pod="Þjóðmál", abbr="ÞJ", date="Sep 29, 2026", art=None,
   title="#462 &ndash; Kaffispjall með Jóhanni Má í Wolt",
   summary=("Jóhann Már Helgason, framkvæmdastjóri Wolt á Íslandi, ræðir innreið fyrirtækisins á íslenskan markað, deilihagkerfið "
     "og röskun á vinnumarkaði, og svarar gagnrýni verkalýðsfélaga og fjölmiðla um stöðu sjálfstætt starfandi verktaka. Hann "
     "hafnar því að um gerviverktöku sé að ræða og segir fyrirtækið hafa kvartað til RÚV vegna umfjöllunar um mótmæli sendla. "
     "Einnig um tæknina á bak við þjónustuna, áhrif á veitingastaði og framtíð heimsendinga. Rúmur klukkutími."),
   rating="Worth a look",
   whyline="Fyrsta ítarlega viðtalið við Wolt-stjórann eftir sendlamótmælin og RÚV-deiluna.",
   tags=["iceland", "business", "labour"]),
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
