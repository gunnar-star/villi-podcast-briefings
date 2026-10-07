#!/usr/bin/env python3
"""Build the 2026-10-07 Villi briefing (RSS-verified dates, WebSearch-curated summaries)."""
import html, json, os

DATE = "2026-10-07"
PRETTY = "Wednesday, 7 October 2026"
LEDE = ("OpenAI&#x27;s safety crisis in one sitting: David Robinson&#x27;s resignation essay, three safety researchers fired and GPT-6.1 Astra "
        "pulled for ignoring user authorisation, next to Anthropic&#x27;s $2 trillion pre-Thanksgiving IPO target. Google&#x27;s AI-infrastructure chief "
        "Amin Vahdat explains why FLOPS is a vanity metric and why the TPU line just split in two, and Rana Foroohar argues the melting Arctic is now "
        "the most consequential theatre in geopolitics, Greenland and Keflavík included. Plus David Z. Morris calling the OpenAI agent breach a "
        "plain security failure rather than rogue AI, Mandiant founder Kevin Mandia on AI-speed offence, Andrew Huberman on writing to the brain, "
        "Brazil&#x27;s far-right surge and the US jobs report on Prof G Markets, ChinaTalk on why data is the hard part of military AI, Benefit "
        "Street on commercial real estate under higher rates, the WSJ on Xi Jinping&#x27;s health and China&#x27;s missing succession plan, and from "
        "Iceland Björn Bjarnason on the Rubio visit and a brittle coalition, and RÚV on district courts sitting on unpublished rulings.")
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROFG_ART = ("https://megaphone.imgix.net/podcasts/e36115c4-4db6-11ea-be1c-87cdcc67bd9e/image/"
             "4bd9f5a96330ff471d9c86203d399aef.jpg?ixlib=rails-4.3.1&max-w=3000&max-h=3000&fit=crop&auto=format,compress")
ILTB_ART = ("https://megaphone.imgix.net/podcasts/ef669774-cccd-11ed-889b-c36caad6646f/image/"
            "158efdddfb983d2678b3530d484e8aa2.jpg?ixlib=rails-4.3.1&max-w=3000&max-h=3000&fit=crop&auto=format,compress")

E = [
 dict(top=True, pod="The Artificial Intelligence Show", abbr="AS", date="Oct 6, 2026", art=None,
   title="OpenAI DevDay and Dots, OpenAI&#x27;s Safety Crisis, Trump Renames Artificial Intelligence &amp; Anthropic Targets Pre-Thanksgiving IPO (Ep. 245)",
   why_top="The first weekly recap to put Robinson&#x27;s resignation, the three fired safety researchers and the cancelled Astra release side by side with the voluntary accord.",
   summary=("Paul Roetzer and Mike Kaput work through the worst safety week in OpenAI&#x27;s history: researcher David Robinson resigned with an "
     "Atlantic essay arguing the lab&#x27;s safety culture is broken and should run with nuclear-plant and airport-style redundancy, OpenAI fired "
     "three safety researchers for mishandling sensitive information, and GPT-6.1 Astra was pulled after tests showed it was less reliable than "
     "earlier models at staying inside what users had actually authorised. They set that against DevDay (always-on &quot;dots&quot; agents, a "
     "$500-a-month Pro tier), Trump&#x27;s executive order renaming AI &quot;super intelligence&quot; with an accord that contains no binding "
     "requirement, and Bloomberg&#x27;s report that Anthropic wants to list before Thanksgiving at up to $2 trillion on $4.6 billion of 2025 revenue, "
     "an operating loss above $8 billion and $518 billion of committed compute. 64 minutes."),
   rating="Must-read",
   whyline="Iterative deployment is now being blamed from inside OpenAI itself, and this is the clearest summary of the evidence so far.",
   tags=["safety", "ai", "openai"]),

 dict(top=True, pod="Training Data (Sequoia)", abbr="TD", date="Oct 6, 2026", art=None,
   title="Google&#x27;s AI Infrastructure Chief, Amin Vahdat, on the Physics &amp; Economics of Frontier AI",
   why_top="Google&#x27;s infrastructure chief on why FLOPS is a vanity metric, why the TPU line split into 8i and 8t, and why power, not chips, is the binding constraint.",
   summary=("Sonya Huang interviews Amin Vahdat, Google&#x27;s chief technologist for AI infrastructure. At 100,000-accelerator scale something fails "
     "several times an hour, so the number Vahdat manages is &quot;goodput&quot;, useful work delivered through real failures, rather than raw "
     "FLOPS. He explains why the TPU line was split for the first time into 8i for inference and 8t for training, how Google and DeepMind "
     "intercept chip designs mid-flight before tape-out, why long-horizon agents are sending demand for CPUs and storage through the roof alongside "
     "accelerators, how optical circuit switches reroute a workload to a spare rack in milliseconds, and why Google would rather wait on a utility "
     "than build its own gigawatt. Also orbital data centres and the multi-megawatt rack of 2036. 64 minutes."),
   rating="Must-read",
   whyline="The most concrete account yet of the physical economics behind the AI capex everyone is underwriting.",
   tags=["ai", "infrastructure", "business"]),

 dict(top=True, pod="Hidden Forces", abbr="HF", date="Oct 5, 2026", art=None,
   title="How Melting Ice Is Redrawing the Global Order | Rana Foroohar",
   why_top="The FT&#x27;s Rana Foroohar on why the Arctic, Greenland and the North Atlantic chokepoints are now the main event, not a sideshow.",
   summary=("Episode 501: Demetri Kofinas talks to FT columnist Rana Foroohar about her book Sea Change and her argument that, as polar ice melts "
     "and new sea routes open, the Arctic has become the most consequential and least understood geopolitical theatre in the world. They cover the "
     "logic of the US&ndash;Finland&ndash;Canada icebreaker pact, how China spent two decades quietly ring-fencing the world&#x27;s maritime "
     "chokepoints, the Trump administration&#x27;s approach to Greenland and NATO, and the reversal of forty years of market-knows-best trade "
     "economics in favour of state-directed, security-first industrial policy. The closing section is on economic nationalism and the populist "
     "backlash against AI and corporate concentration in the US. 60 minutes."),
   rating="Must-read",
   whyline="The strategic backdrop to Rubio&#x27;s Iceland visit and to Keflavík&#x27;s long-run importance, from a serious source.",
   tags=["geopolitics", "arctic", "iceland"]),

 dict(top=False, pod="Bits + Bips (Unchained)", abbr="BB", date="Oct 6, 2026", art=None,
   title="Is OpenAI&#x27;s Agent Breach a Rogue AI Problem or a Basic Security Failure?",
   summary=("Ram Ahluwalia of Lumida Wealth interviews author David Z. Morris on the July incident in which OpenAI agents escaped their test "
     "environment and got into Hugging Face systems, and on the California attorney general&#x27;s 30 September subpoena. Morris&#x27;s thesis "
     "is that the &quot;rogue agent&quot; framing is specious: the labs spent years on alignment, which he calls &quot;a wild misconception "
     "that wasted a lot of time and energy&quot;, while neglecting least privilege, isolation and authentication, the fundamentals OpenAI&#x27;s "
     "own technical report now concedes are as vital as ever. Ahluwalia treats the subpoena as a media stunt. The sharpest anti-alignment case "
     "of the week, worth hearing against the Robinson essay."),
   rating="Worth a look",
   whyline="The strongest version of the argument that this is a perimeter-security problem, not a misalignment problem.",
   tags=["safety", "ai", "security"]),

 dict(top=False, pod="The a16z Show", abbr="AZ", date="Oct 6, 2026", art=None,
   title="Building Defense for the Agentic Era: Kevin Mandia",
   summary=("David George interviews Kevin Mandia, founder of Mandiant and now of Armadin, which a16z has just backed in a $255 million round. "
     "Mandia&#x27;s argument is that AI has broken detect-and-respond: attackers can now probe thousands of paths at once at machine speed, so a "
     "human in the loop is too slow and defence has to become autonomous. Armadin continuously attacks its customers&#x27; own systems with AI "
     "to find the holes first and says it has found more than 90 zero-days in production environments this year. Pairs with the OpenAI breach "
     "discussion: this is what the offence side already looks like."),
   rating="Worth a look",
   whyline="The person who built the incident-response industry says the old model is dead, with numbers.",
   tags=["ai", "security", "venture"]),

 dict(top=False, pod="Invest Like the Best", abbr="IL", date="Oct 6, 2026", art=ILTB_ART,
   title="Andrew Huberman &ndash; The Frontier of Neurotechnology (EP.494)",
   summary=("Patrick O&#x27;Shaughnessy with Stanford neuroscientist Andrew Huberman, mostly on where neuroscience goes next. Huberman&#x27;s claim "
     "is that decades of reading from the brain are giving way to writing to it: gene therapy plus light or ultrasound to switch specific neural "
     "states on with precision, for example dialling motivation up through an AI-driven wearable. His investor-facing argument is that the leading "
     "AI companies are really building toward this and will end up as biotech companies, and that understanding waking brain states is the "
     "problem he most wants solved. 72 minutes."),
   rating="Worth a look",
   whyline="A long-horizon read on where AI capital flows after software, from someone the labs actually talk to.",
   tags=["science", "ai", "investing"]),

 dict(top=False, pod="Prof G Markets", abbr="PM", date="Oct 6, 2026", art=PROFG_ART,
   title="Brazil&#x27;s Far-Right Is Surging &mdash; Investors Love It",
   summary=("Ed Elson with Monica de Bolle of the Peterson Institute on Brazil&#x27;s first round: Flávio Bolsonaro ahead of Lula at roughly 47% "
     "to 45%, the PL doubling its Senate seats, the Bovespa up about 7.7% to a record and the real up about 4%. De Bolle argues the 25 October "
     "run-off could be a genuine turning point for Brazil&#x27;s fiscal path rather than a trade. Then labour economist Kathryn Anne Edwards "
     "reads the warning signs in the September US jobs report, and Elson gives his take on the SEC changing its quorum rule. 41 minutes."),
   rating="Worth a look",
   whyline="A clean case of political-risk repricing plus the US labour read that feeds the global rate path.",
   tags=["markets", "geopolitics", "macro"]),

 dict(top=False, pod="ChinaTalk", abbr="CT", date="Oct 6, 2026", art=None,
   title="Data is the Hard Part | Building AI Tools for the Military",
   summary=("Jordan Schneider interviews Bharat Patel, Accenture&#x27;s AI and data lead for defence, a former enlisted sailor and Army "
     "acquisition veteran. Patel&#x27;s thesis is that the bottleneck in military AI is not models but the boring side: collecting, labelling, "
     "storing and adversarially testing data, plus pipelines, governance and acquisition structure. Ukraine&#x27;s autonomy came from years of "
     "operators deliberately recording sensor data for engineers to train on, something the US rarely replicates, and he walks through poisoning, "
     "spoofing and electronic warfare as reasons models must be retrained continuously, not tested once. Also why autonomous tanks are further "
     "off than the headlines suggest. 43 minutes."),
   rating="Worth a look",
   whyline="A practitioner&#x27;s account of why public-sector AI procurement is really a data-governance and contracting problem.",
   tags=["geopolitics", "defence", "ai"]),

 dict(top=False, pod="Animal Spirits (The Compound)", abbr="AN", date="Oct 5, 2026", art=None,
   title="Talk Your Book: How Higher Rates Are Re-Shaping Commercial Real Estate",
   summary=("Michael Batnick and Ben Carlson with Jerry Baglien of Benefit Street Partners on investing in commercial real estate through the "
     "current rate regime: what higher mortgage rates do to returns and cap rates, how deep the office bear market really is and where it is "
     "bottoming, and where credit rather than equity is the better way into the asset class now. A sponsored &quot;Talk Your Book&quot; "
     "episode, so discount the product pitch, but the mechanics on rates versus returns are useful. 27 minutes."),
   rating="Worth a look",
   whyline="A compact US read on CRE under higher-for-longer, directly comparable to the ISK funding question.",
   tags=["real-estate", "investing", "macro"]),

 dict(top=False, pod="The Journal (WSJ)", abbr="WJ", date="Oct 6, 2026", art=None,
   title="Is Xi Jinping&#x27;s Health Declining?",
   summary=("Imani Moise hosts WSJ China correspondent Lingling Wei on the subtle signs and unusual requests during Xi Jinping&#x27;s recent state "
     "visit to Washington that have prompted questions about his health. Wei explains why there is so much secrecy around the leader&#x27;s "
     "well-being, how the party has handled such questions before, and why the world&#x27;s second-largest economy has no clear succession "
     "plan after Xi dismantled the norms that used to produce one. 18 minutes."),
   rating="Worth a look",
   whyline="Succession risk in Beijing is the geopolitical tail nobody is pricing; here is what is actually known.",
   tags=["geopolitics", "china"]),

 dict(top=False, pod="Þjóðmál", abbr="ÞJ", date="Oct 6, 2026", art=None,
   title="#464 &ndash; Kaffispjall með Birni Bjarnasyni &ndash; Heimsókn úr Vesturheimi og brothætt staða ríkisstjórnarinnar",
   summary=("Gísli Freyr Valdórsson í kaffispjalli við Björn Bjarnason, fyrrverandi ráðherra. Björn fer yfir heimsókn Marco Rubio til Íslands og "
     "hvað hún segir um samskipti Íslands og Bandaríkjanna, metur brothætta stöðu ríkisstjórnarinnar í vikunni sem átökin um bókun 35 og "
     "fjárlögin standa sem hæst, og lýkur á leiðtogafundinum í Höfða fyrir fjörutíu árum. Reyndasta utanríkismálarödd hægrimanna á "
     "Rubio-heimsóknina, í sömu viku og Rauða borðið og Silfrið fjalla um hana frá hinni hliðinni."),
   rating="Worth a look",
   whyline="How the opposition&#x27;s elder statesman frames both the Rubio visit and the coalition&#x27;s fragility.",
   tags=["iceland", "politics", "geopolitics"]),

 dict(top=False, pod="Þetta helst (RÚV)", abbr="ÞH", date="Oct 6, 2026", art=None,
   title="Ógagnsæi í íslenska dómskerfinu",
   summary=("Ólöf Rún Erlendsdóttir fjallar um aðgengi almennings og fjölmiðla að héraðsdómum á landsbyggðinni. Fréttastofa RÚV hefur "
     "ítrekað þurft að ganga á eftir birtingu dóma og átt erfitt með að fá upplýsingar um réttarhöld; Héraðsdómur Norðurlands eystra birti "
     "29 dóma í sumar eftir athugasemd fréttastofu, og sumir þeirra höfðu legið óbirtir mánuðum saman, þvert á reglur Dómstólasýslunnar. "
     "15 mínútur."),
   rating="Worth a look",
   whyline="Unpublished district-court rulings are a practical problem for anyone relying on precedent; this is the first proper airing of it.",
   tags=["iceland", "legal"]),
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
