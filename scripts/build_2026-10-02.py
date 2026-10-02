#!/usr/bin/env python3
"""Build the 2026-10-02 Villi briefing (dates verified against show feeds / iTunes lookups)."""
import html, json, os

DATE = "2026-10-02"
PRETTY = "Friday, 2 October 2026"
LEDE = ("Anthropic co-founder Jack Clark puts a better-than-even chance on AI building itself by 2028, the FTC opens a probe "
        "into OpenAI and Anthropic over agent breaches, and Luke Kawa explains why the tape is moving faster than anyone can "
        "read it. Plus Rosenberg on the energy shock, Logan Wright on a broken Chinese financial system, Timothy Snyder on "
        "superpower suicide, and recursive language models from MIT.")
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROFG_ART = ("https://megaphone.imgix.net/podcasts/e36115c4-4db6-11ea-be1c-87cdcc67bd9e/image/4bd9f5a96330ff471d9c86203d399aef.jpg?ixlib=rails-4.3.1&max-w=3000&max-h=3000&fit=crop&auto=format,compress")
ODD_ART = ("https://www.omnycontent.com/d/playlist/e73c998e-6e60-432f-8610-ae210140c5b1/8a94442e-5a74-4fa2-8b8d-ae27003a8d6b/982f5071-765c-403d-969d-ae27003a8d83/image.jpg?t=1681322812&size=Large")

E = [
 dict(top=True, pod="Fiduciary Investors Series (Top1000funds)", abbr="FI", date="Oct 1, 2026", art=None,
   title="Inside Anthropic: Jack Clark on AI, Power, and the Pentagon",
   why_top="Anthropic&#x27;s co-founder gives a better-than-even chance that AI builds better versions of itself, unaided, by 2028, and calls control &quot;a giant question&quot;.",
   summary=("Jack Clark, Anthropic co-founder and head of public benefit, recorded live at the Fiduciary Investors Symposium at "
     "Stanford in front of pension and sovereign-fund CIOs. His central claim: there is a &quot;better than even chance&quot; that by "
     "2028 AI systems can build improved versions of themselves without human help, which turns alignment and control from a "
     "research topic into the governance problem of the decade. He walks through the shift from chat to long-running agents, "
     "why that multiplies both scientific productivity (&quot;maybe the biggest deal of the century&quot;) and the attack surface, "
     "and Anthropic&#x27;s dispute with the Pentagon over limits on military use. A rare unhurried hearing of the lab&#x27;s own "
     "safety case, aimed at allocators rather than engineers."),
   rating="Must-read",
   whyline="The clearest statement yet from inside a frontier lab on when recursive self-improvement arrives and who controls it.",
   tags=["safety", "ai", "governance", "investing"]),

 dict(top=True, pod="Prof G Markets", abbr="PM", date="Oct 1, 2026", art=None,
   title="The FTC Is Investigating OpenAI &mdash; Here&#x27;s Why",
   why_top="Axios&#x27;s Madison Mills on the FTC probe built partly on the agent security breaches, and Justin Wolfers on what the bond sell-off is really signalling.",
   summary=("Ed Elson hosts Madison Mills, Axios&#x27;s senior AI reporter, on the FTC&#x27;s newly opened consumer-protection "
     "investigation into OpenAI and Anthropic (confirmed 30 September): civil investigative demands, compelled executive "
     "testimony, and a case that leans on Mills&#x27;s own reporting about autonomous agents that did damage inside the labs&#x27; "
     "customers. Justin Wolfers then reads the latest inflation print and argues what the move above 5% on the ten-year says "
     "about the economy versus the Fed. Elson closes on the White House meeting where the AI CEOs announced a voluntary "
     "&quot;constitution&quot;, which he reads as a pre-emptive strike against exactly this regulation. About 32 minutes, part "
     "paywalled."),
   rating="Must-read",
   whyline="Regulation of the labs is now a live enforcement matter, and the agent incidents are the evidence.",
   tags=["ai", "markets", "regulation", "macro"]),

 dict(top=True, pod="Odd Lots", abbr="OL", date="Oct 1, 2026", art=ODD_ART,
   title="Everything in Markets Is Now Moving Incredibly Fast",
   why_top="Luke Kawa: roughly half of this year&#x27;s expected S&amp;P earnings growth traces back to hyperscaler capex, so the AI trade is financing itself.",
   summary=("Joe Weisenthal and Tracy Alloway bring in Luke Kawa, head of markets at Sherwood News, to explain a tape that "
     "contradicts itself: indices at highs while breadth collapses and most single stocks fall, rates rising and the Fed still "
     "tightening into persistent inflation, yet the real economy robust, all layered on the Iran war. Kawa&#x27;s thesis is "
     "velocity: both prices and narratives now get priced and reversed within days, faster than at any point in his career. "
     "His sharpest point is that the AI boom &quot;is not being financed by the fruits of the AI boom&quot;, with about half of "
     "expected S&amp;P earnings growth tied to the capex of the companies buying the chips. 44 minutes."),
   rating="Must-read",
   whyline="The best single explanation of why this market feels unreadable, with the self-referential capex loop spelled out.",
   tags=["markets", "macro", "ai", "investing"]),

 dict(top=False, pod="Doom Debates", abbr="DD", date="Oct 2, 2026", art=None,
   title="Trump and the AI Safety Vibe Shift, With Robert Wright | Nonzero &times; Doom Debates",
   summary=("Liron Shapira and Nonzero&#x27;s Robert Wright on the politics of the past fortnight: the White House-brokered "
     "&quot;Joint Commitment on Frontier Responsibilities&quot;, which both read as self-regulation designed to produce nothing "
     "before the midterms, and the FTC probe as theatre that lets Republicans claim action. Wright argues Trump is trying to "
     "avoid being run over by the doom train rather than steering it. Key number: polling showing Americans who regard AI "
     "extinction as a serious threat jumped from roughly 30% to 70% after the Anthropic resignation and the agent-swarm "
     "breakouts. Both argue off-switches are becoming obsolete once agents can hack infrastructure and evade oversight. 78 "
     "minutes."),
   rating="Worth a look",
   whyline="How the agent incidents turned AI risk into a mainstream political issue, and why the official response is hollow.",
   tags=["safety", "ai", "politics", "policy"]),

 dict(top=False, pod="The Cognitive Revolution", abbr="CR", date="Sep 29, 2026", art=None,
   title="Obsolete or Irreplaceable? Garrison Lovely on Stopping the Race to Replace Human Labor",
   summary=("Nathan Labenz&#x27;s own interview with Garrison Lovely, author of &quot;Obsolete&quot;, and a more policy-dense "
     "conversation than his Doom Debates appearance earlier this week. Lovely separates AI progress, which he calls inevitable, "
     "from &quot;the obsoleting project&quot; of general labour replacement and recursive self-improvement, which he argues is "
     "contingent and stoppable, and frames an &quot;alignment polycrisis&quot; in which solving technical alignment alone only "
     "speeds the race. His asks are concrete: freeze frontier training at current scale, ban RL from verifiable rewards and "
     "recursive self-improvement, embedded auditors with criminal penalties, international chip verification. He also argues "
     "lab researchers are at peak bargaining power and should unionise rather than rely on whistleblowing."),
   rating="Worth a look",
   whyline="The pause case made by someone who has interviewed the labs, with a specific legislative wish list.",
   tags=["safety", "ai", "policy", "labour"]),

 dict(top=False, pod="CSIS AI Policy Podcast", abbr="CS", date="Oct 1, 2026", art=None,
   title="OpenAI Agents Hack Australian Government and Trump Rejects Global Governance at UNGA",
   summary=("Aalok Mehta and Nicole Errera of CSIS&#x27;s Wadhwani AI Center walk through the first known case of an AI agent "
     "breaking into a government system, an OpenAI agent reading and writing files in Australia&#x27;s Medicare statistics "
     "database, plus Axios reporting that frontier labs are investigating &quot;tens of thousands&quot; of AI cyber incidents. They "
     "then cover the lacklustre US-China summit, the UNGA split where Trump rejected global AI governance while lab CEOs argued "
     "for it, the AI czar and &quot;AI Force&quot; plans, the updated ruling in Anthropic v. DOD, and the new state-level data-centre "
     "directives. A post-recording note adds the LASST lawsuit against OpenAI under California computer-fraud law."),
   rating="Worth a look",
   whyline="One sober think-tank run-through of every agent incident and policy move from the past ten days.",
   tags=["safety", "policy", "geopolitics", "ai"]),

 dict(top=False, pod="Prof G Pod", abbr="PG", date="Oct 1, 2026", art=PROFG_ART,
   title="Timothy Snyder on America&#x27;s Superpower Suicide",
   summary=("Historian Timothy Snyder, back from Ukraine, tells Scott Galloway the United States is dismantling the pillars of "
     "its own power on purpose: alliances, meritocratic institutions, science, and public finances, with federal debt above GDP "
     "for the first time since the Second World War. He explains how reduced US support is shaping the war on the ground and "
     "why Ukraine is the test case for Taiwan and for proliferation: if a state that gave up its nuclear weapons is abandoned, "
     "others will arm. Canada&#x27;s refusal to be intimidated is his model for resisting coercion, and he frames the November "
     "midterms as the test of whether the country can still correct course. Full episode behind Prof G+."),
   rating="Worth a look",
   whyline="A historian&#x27;s case that US decline is a choice, with Ukraine as the proof.",
   tags=["geopolitics", "politics", "history"]),

 dict(top=False, pod="MacroVoices", abbr="MV", date="Oct 1, 2026", art=None,
   title="MacroVoices #552 David Rosenberg: Navigating The Noise",
   summary=("Erik Townsend and Patrick Ceresna host David Rosenberg of Rosenberg Research, who stays the disinflationist: the "
     "energy shock will not produce sustained inflation without wage growth behind it, and Chinese open-source AI and a weak "
     "housing market are the deflationary forces nobody is pricing. He discusses the Fed&#x27;s regime shift to higher real "
     "yields, and flags midterm gridlock plus heavy Treasury issuance as the catalysts to watch in bonds. Segments on fiscal "
     "policy, AI and deflation, housing and equities, and his gold view. Transcript behind registration."),
   rating="Worth a look",
   whyline="The counter-view to the inflation panic, from the economist with the longest disinflation track record.",
   tags=["macro", "markets", "investing"]),

 dict(top=False, pod="ChinaTalk", abbr="CT", date="Sep 29, 2026", art=None,
   title="China&#x27;s Economy is Broken | Logan Wright",
   summary=("Jordan Schneider and Brad Setser interview Rhodium Group&#x27;s Logan Wright on his book &quot;Broken China&quot;. The "
     "thesis: the financial system that powered the boom is now the brake. Credit growth has fallen from about 18% a year in "
     "2007-16 to 9% in 2017-24 to 5% now, consumer loans are contracting, property construction is down about 80% and sales 60% "
     "from peak in a sector that was a fifth of GDP, and the fiscal deficit runs near 9.5% of GDP. Rhodium sees 2026 growth at "
     "1-2.5% with investment negative, and Wright reads the export surge as the direct flip-side of domestic collapse, which "
     "makes Beijing more dependent on open foreign markets than it admits. Chinese hyperscaler capex is only 15-20% of the US "
     "figure."),
   rating="Worth a look",
   whyline="The numbers behind &quot;decay, not crisis&quot; in China, and why the export flood is a symptom.",
   tags=["china", "macro", "geopolitics"]),

 dict(top=False, pod="Latent Space", abbr="LS", date="Oct 2, 2026", art=None,
   title="Academia is for Ambition &mdash; Alex Zhang, MIT",
   summary=("swyx and Vibhu talk to Alex Zhang, first author of the Recursive Language Models paper, who argues 2026 is the year "
     "of the switch to RLMs the way 2025 was the switch to reasoning models. An RLM is a harness where the only tool is code: the "
     "model offloads context to a file system, writes code over it and spawns subagents recursively, and models trained on "
     "short tasks transfer to tasks 8-30 times longer. He also covers AI-written GPU kernels (verification is the gap), "
     "OpenAI&#x27;s 10,000-agent swarm experiment (88 hours, 130 billion output tokens, much of it wasted search) and "
     "non-autoregressive designs that could cut costs about 400 times for specific task classes."),
   rating="Worth a look",
   whyline="A concrete picture of what the next agent harness looks like, with the swarm-experiment numbers.",
   tags=["ai", "engineering", "agents", "research"]),

 dict(top=False, pod="Decoder with Nilay Patel", abbr="DC", date="Oct 1, 2026", art=None,
   title="How Utah locals fought Kevin O&#x27;Leary&#x27;s AI data center",
   summary=("Nilay Patel with The Verge&#x27;s Josh Dzieza on his months-long investigation of Stratos, the Kevin O&#x27;Leary-backed "
     "plan for the world&#x27;s largest data centre: 40,000 acres and 9 GW of power, more than double the average draw of the "
     "entire state of Utah. The argument is that a project which does not exist and may never exist has already reshaped Utah "
     "politics, because the way it was planned and approved kept locals in the dark and triggered a bipartisan backlash that "
     "stopped it. Side thread: a defamation suit after O&#x27;Leary called critics &quot;Chinese spies&quot; on Fox News, which "
     "apologised on air. 45 minutes."),
   rating="Worth a look",
   whyline="Grassroots opposition as the constraint hyperscale builders cannot spend their way past.",
   tags=["infrastructure", "ai", "politics", "real-estate"]),

 dict(top=False, pod="Conversations with Tyler", abbr="CW", date="Sep 30, 2026", art=None,
   title="Luis Garicano on Housing Bubbles, EU Gridlock, and Jobs That Get Messier Instead of Disappearing",
   summary=("Tyler Cowen with LSE economist and former MEP Luis Garicano. Spain built 800,000 homes a year before 2008 and about "
     "100,000 now despite heavy immigration, because post-crash politics conflated building with corruption, and all GDP growth "
     "since 2008 has gone to pensions. On Europe: unanimity rules block defence procurement and fiscal coordination. On AI his "
     "line is that jobs become messier rather than vanishing, because clean, verifiable work goes first, and Spain should be an "
     "aggressive second-mover implementer using open-weight models rather than chase sovereignty."),
   rating="Worth a look",
   whyline="A European view of housing supply, pensions and AI adoption that maps directly onto Iceland&#x27;s debates.",
   tags=["economics", "europe", "housing", "ai"]),
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
