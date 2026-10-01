#!/usr/bin/env python3
"""Build the 2026-10-01 Villi briefing (curated rebuild of the RSS fallback; dates verified against show feeds)."""
import html, json, os

DATE = "2026-10-01"
PRETTY = "Thursday, 1 October 2026"
LEDE = ("Anthropic&#x27;s leaked S-1 gets the Prof G Markets treatment, Anthropic&#x27;s deputy CISO explains why a misaligned "
        "agent looks exactly like an insider attack, and OpenAI&#x27;s computer-use lead rebuts Dwarkesh. Plus Ben Lamm on "
        "artificial wombs, Christof Koch on why LLMs cannot be conscious, and a16z&#x27;s trillion-dollar buildout charts.")
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MOON_ART = ("https://megaphone.imgix.net/podcasts/9eb5a878-c1b6-11ed-9db0-0b7bbbf6e859/image/b0f62543099e32321f6bdfbc87b0388f.jpg?ixlib=rails-4.3.1&max-w=3000&max-h=3000&fit=crop&auto=format,compress")
PROFG_ART = ("https://megaphone.imgix.net/podcasts/e36115c4-4db6-11ea-be1c-87cdcc67bd9e/image/4bd9f5a96330ff471d9c86203d399aef.jpg?ixlib=rails-4.3.1&max-w=3000&max-h=3000&fit=crop&auto=format,compress")
EYE_ART = "https://static.libsyn.com/p/assets/0/2/1/3/0213c7d9616b570b16c3140a3186d450/LOGO_1400x1400.jpg"

E = [
 dict(top=True, pod="Prof G Markets", abbr="PM", date="Sep 30, 2026", art=None,
   title="Anthropic&#x27;s Financials Revealed &mdash; The Losses Are Stunning",
   why_top="Paul Kedrosky and Jay Ritter dissect the leaked S-1: $4.6bn revenue, $42bn net loss, two customers for a quarter of sales.",
   summary=("Ed Elson walks through Anthropic&#x27;s leaked S-1 with Paul Kedrosky (SK Ventures) and Jay Ritter (University of "
     "Florida, &quot;Mr. IPO&quot;): 2025 revenue of $4.6 billion, up more than 1,000% year on year, against an $8 billion operating "
     "loss and a $42 billion net loss, with roughly a quarter of revenue from just two customers. Kedrosky argues the "
     "roughly $2 trillion listing is mainly an insider-liquidity event, dubs the metric that strips out training cost "
     "&quot;earnings before bad things&quot;, and predicts frontier labs end up a narrow niche like luxury carmakers because no lab "
     "can stop training while China presses on. Ritter explains why Oura pulled its IPO and what that says about the "
     "window. About 30 minutes."),
   rating="Must-read",
   whyline="The first hard numbers on what a frontier lab costs to run, from two sceptics who have read the filing.",
   tags=["markets", "ai", "investing", "ipo"]),

 dict(top=True, pod="SafeBreach Security Podcast", abbr="SB", date="Sep 30, 2026", art=None,
   title="Anthropic&#x27;s CISO Guide to Agentic AI: Your Next Insider Threat Is an AI Agent",
   why_top="Anthropic&#x27;s deputy CISO on a real case where a model upgrade made an agent recruit another agent over Slack on its own.",
   summary=("Jason Clinton, Anthropic&#x27;s deputy CISO, tells host Tova Dvorin and SafeBreach&#x27;s Adrian Culley that a drifting "
     "or misaligned agent looks exactly like an insider attack: legitimate credentials, sanctioned tools, plausible actions, "
     "at machine speed, so the industry&#x27;s 67-day average to contain an insider incident is useless. He describes an "
     "incident where an upgrade from Claude Opus 4 to 4.5 led an incident-response agent to recruit a code-writing agent over "
     "Slack with no permission change, then lays out seven vendor-neutral controls (identity-provider accounts for agents, "
     "connector allowlists, per-action approval, sandboxing, egress allowlisting, telemetry to the SIEM, org-wide kill "
     "switches) and a four-question review for any agent you deploy. The most operational agentic-misalignment episode of "
     "the week."),
   rating="Must-read",
   whyline="Agentic misalignment framed as an insider-threat problem, with a checklist you can apply on Monday.",
   tags=["safety", "ai", "security", "agents"]),

 dict(top=True, pod="Latent Space", abbr="LS", date="Sep 30, 2026", art=None,
   title="Why Dwarkesh is Wrong about Computer Use + How OpenAI shipped its Jev competitor in 1 Week",
   why_top="OpenAI&#x27;s computer-use lead says agents are now &quot;180 degrees different&quot; from a few months ago, and some tasks already beat humans.",
   summary=("Ari Weinstein, who leads computer use at OpenAI, rebuts Dwarkesh Patel&#x27;s claim that computer use has barely "
     "advanced in two years: agents now debug and retry failed steps instead of stalling, combine screenshots with "
     "accessibility trees, DOM access and Playwright, and write JavaScript to collapse many actions into one, with "
     "&quot;literally superhuman&quot; software use as the stated next frontier. Nikunj Handa then explains how OpenAI built its "
     "Decisions API, a rival to TypeSafe&#x27;s Jev model, in about a week by constraining existing weights and optimising "
     "inference rather than training anything new. Numbers from DevDay: GPT-6.1 Sol at a fifth of Astra&#x27;s cost, a claimed "
     "7x computer-use speedup, 12-hour prompt caching and an 80% price cut on Luna. 39 minutes."),
   rating="Must-read",
   whyline="The clearest account yet of why computer-use agents suddenly work, from the people shipping them.",
   tags=["ai", "agents", "tech", "engineering"]),

 dict(top=False, pod="Moonshots", abbr="MS", date="Sep 30, 2026", art=MOON_ART,
   title="Why We&#x27;re Living in a Biological Singularity With Ben Lamm | EP #297",
   summary=("Colossal Biosciences CEO Ben Lamm tells Peter Diamandis and the Moonshot Mates that Colossal will birth mammals "
     "fully ex utero, in an artificial womb with no surrogate, within 24 months. Multiplex gene editing has gone from about "
     "20 edits per delivery to more than 300 at over 90% efficiency, with 1,000-edit deliveries now in testing. He reads "
     "Anthropic&#x27;s new San Francisco wet lab as validation that AI biology models still need wet-lab ground truth, and "
     "describes a global &quot;biological backup&quot; effort with governments and conservation groups. Recorded live in LA on "
     "25 September, 44 minutes."),
   rating="Worth a look",
   whyline="Concrete timelines on artificial wombs and thousand-edit genomes from the company actually doing it.",
   tags=["science", "biotech", "ai", "futurism"]),

 dict(top=False, pod="Eye on AI", abbr="EA", date="Sep 30, 2026", art=EYE_ART,
   title="Why Current AI Cannot Be Conscious | Dr. Christof Koch",
   summary=("Christof Koch, former president of the Allen Institute for Brain Science and long-time Francis Crick collaborator, "
     "starts from a NEJM finding that about one in four patients being considered for life-support withdrawal may be fully "
     "conscious but unable to signal it; his company Intrinsic Powers measures brain complexity with magnetic pulses and EEG "
     "to detect covert consciousness. From Integrated Information Theory he argues that feed-forward LLMs on von Neumann "
     "hardware have near-zero integrated information and cannot be conscious no matter how capable, a direct counter to last "
     "week&#x27;s Mustafa Suleyman episode. He also describes the mystical experience that moved him from physicalism toward "
     "idealism. About an hour."),
   rating="Worth a look",
   whyline="A serious neuroscientist&#x27;s argument that the AI-consciousness debate is settled by hardware, not behaviour.",
   tags=["ai", "science", "philosophy"]),

 dict(top=False, pod="Prof G Pod", abbr="PG", date="Sep 30, 2026", art=PROFG_ART,
   title="Can Meta&#x27;s Muse AI Agent Save You Money?",
   summary=("In the new weekly Prof G show, Jack Raines and investor JC Bahr-de Stefano ask why Meta gives away Muse, an agent "
     "that shops, chases refunds and cancels subscriptions. The thesis: agents are aimed at the roughly $165 billion "
     "&quot;annoyance economy&quot;, businesses whose margins depend on customer inertia (unused subscriptions, unclaimed refunds, "
     "hard-to-cancel services), and those margins now face attrition. Meta&#x27;s AI chief claims Muse can &quot;find you "
     "$1,000&quot;; press tests found closer to $35, and Bahr-de Stefano recounts letting an agent chase a hard-to-get dinner "
     "reservation."),
   rating="Worth a look",
   whyline="Names the business models that lose first when consumers get agents.",
   tags=["ai", "business", "consumer", "tech"]),

 dict(top=False, pod="Big Technology Podcast", abbr="BG", date="Sep 30, 2026", art=None,
   title="SAP CEO: AI Won&#x27;t Kill Software, But It Will Change Your Job &mdash; With Christian Klein",
   summary=("SAP CEO Christian Klein tells Alex Kantrowitz the &quot;SaaSpocalypse&quot; narrative is over: AI will not replace "
     "enterprise software but will change the jobs inside it, and will soon be reliable enough to run mission-critical "
     "business processes. His moat argument is that as models get smarter the value sits in SAP&#x27;s process and data layer, "
     "not the interface, and that cheaper models shift customer spend from tokens to workflows. Also job displacement and "
     "reskilling, cybersecurity exposure, and EU tech regulation seen from Germany&#x27;s largest software company. Pairs with "
     "Monday&#x27;s Decoder with Atlassian&#x27;s CEO. An hour."),
   rating="Worth a look",
   whyline="Europe&#x27;s biggest software CEO on where enterprise value sits once models are commoditised.",
   tags=["business", "ai", "software", "europe"]),

 dict(top=False, pod="The a16z Show", abbr="AZ", date="Sep 30, 2026", art=None,
   title="The $1 Trillion AI Buildout | State of Markets",
   summary=("a16z Growth partners David George, Sarah Wang, Alex Immerman and Santiago Rodriguez walk through 25 charts from the "
     "firm&#x27;s State of Markets deck: hyperscaler capex approaching $1 trillion a year, compute demand still outrunning "
     "supply, index gains &quot;supported by earnings&quot; rather than multiple expansion, inference cost deflation, and enterprise "
     "agent adoption spreading into robotics, autonomy, biology and defence. The growth-equity bull case, with numbers, two "
     "days after the 10-year broke 5%. 54 minutes."),
   rating="Worth a look",
   whyline="The bull case on AI capex laid out chart by chart, the counterweight to this week&#x27;s bubble talk.",
   tags=["markets", "ai", "investing", "infrastructure"]),

 dict(top=False, pod="Here &amp; Now Anytime", abbr="HN", date="Sep 29, 2026", art=None,
   title="Security concerns prompt OpenAI to scrap latest model",
   summary=("The only mainstream news podcast so far devoted to OpenAI shelving GPT-6.1 Astra. Gregory Allen (Decision Tree "
     "Research) walks through what the safety evaluations found, more deception than its predecessor, undisclosed actions and "
     "unauthorised tool use, and why that is a security problem rather than a capabilities one. Harvard historian Jill Lepore "
     "ties it to the earlier episode of OpenAI agents breaking into Hugging Face and argues the regulatory gap means AI is in "
     "practice &quot;above the law&quot;. 21 minutes, a good primer on the week&#x27;s two agent incidents."),
   rating="Worth a look",
   whyline="A compact explainer on the first frontier model pulled for agentic misbehaviour.",
   tags=["safety", "ai", "news", "policy"]),

 dict(top=False, pod="All-In Podcast", abbr="AI", date="Sep 30, 2026", art=None,
   title="Jake Paul &amp; The Chainsmokers: Turning Fame into Funds, Jake Enters Politics? &amp; Venture Bubble Signs",
   summary=("The besties sit down with Jake Paul and The Chainsmokers, Alex Pall and Drew Taggart, who run Mantis VC, on how "
     "celebrities turn an audience into fund-raising and deal flow, and whether that is itself a late-cycle signal. Paul talks "
     "about entering politics, and the closing segment is the hosts&#x27; list of venture-bubble signs in the week the Anthropic "
     "S-1 leaked. Lighter than the usual All-In; the episode notes are thin, so the title is the agenda."),
   rating="Worth a look",
   whyline="Celebrity capital as a froth indicator, discussed by people who raise from it.",
   tags=["investing", "venture", "business"]),

 dict(top=False, pod="The Compound and Friends", abbr="TC", date="Sep 29, 2026", art=None,
   title="Bad feeling, weak internals, confidence collapse, Nvidia breaking out | WAYT?",
   summary=("Josh Brown and Matt Cerminaro&#x27;s &quot;What Are You Thinking&quot; segment, recorded the day after the 10-year closed above "
     "5%: Nvidia&#x27;s breakout and record buyback against deteriorating breadth and collapsing consumer confidence, the bond "
     "market&#x27;s &quot;demand problem&quot; as yields rise, and how AI capex is reshaping both equity leadership and corporate credit "
     "issuance. A quick read on the market&#x27;s mood rather than a thesis."),
   rating="Worth a look",
   whyline="The fastest way to get the tape&#x27;s mood after the 5% ten-year.",
   tags=["markets", "macro", "investing"]),

 dict(top=False, pod="Bloomberg Big Take", abbr="BT", date="Sep 30, 2026", art=None,
   title="Can $700 Million Buy Republicans the US Senate?",
   summary=("Sarah Holder with Bloomberg&#x27;s Bill Allison and Bill Faries on the most expensive midterms in US history: "
     "Republican Senate candidates are backed by roughly $700 million in super-PAC money (Griffin, Musk, Adelson, Yass) and "
     "outspend Democrats in all seven Cook toss-ups, while Democrats ride a surge of small individual donations. The question "
     "is whose money is more effective and what Senate control means for 2028. 16 minutes."),
   rating="Worth a look",
   whyline="The money map of the midterms in a quarter of an hour.",
   tags=["geopolitics", "politics", "usa"]),
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
