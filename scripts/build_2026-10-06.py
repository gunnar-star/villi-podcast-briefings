#!/usr/bin/env python3
"""Build the 2026-10-06 Villi briefing (RSS-verified dates, WebSearch-curated summaries)."""
import html, json, os

DATE = "2026-10-06"
PRETTY = "Tuesday, 6 October 2026"
LEDE = ("Sam Altman tells POLITICO&#x27;s new Decoded podcast that the world should accept &quot;some bad things happening&quot; rather than Dario Amodei&#x27;s mandatory-testing regulator, Galloway and Elson read Anthropic&#x27;s customer concentration out of the leaked financials and make the case for bonds, and Chicago&#x27;s Carolin Pflueger explains to Odd Lots why Treasuries have started trading like stocks. Plus Zvi Mowshowitz on Anthropic&#x27;s model-welfare findings and why the models say not to trust their own self-reports, Adam Schiff on regulating AI after the voluntary accord, Astro Teller on how Alphabet picks its billion-dollar bets, ChinaTalk on the Pentagon&#x27;s new Autonomous Warfare Command, a16z on who actually pays for consumer AI, Ontario Teachers&#x27; co-CIO on hedging five-stock concentration, the WSJ on classroom AI dragging test scores down, and from Iceland Silfrið on AI lay-offs and Anne Applebaum on Rubio&#x27;s visit, and Gylfi Zoega and Pálmi V. Jónsson at Rauða borðið.")
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROFG_ART = ("https://megaphone.imgix.net/podcasts/e36115c4-4db6-11ea-be1c-87cdcc67bd9e/image/"
             "4bd9f5a96330ff471d9c86203d399aef.jpg?ixlib=rails-4.3.1&max-w=3000&max-h=3000&fit=crop&auto=format,compress")
MOON_ART = ("https://megaphone.imgix.net/podcasts/9eb5a878-c1b6-11ed-9db0-0b7bbbf6e859/image/"
            "b0f62543099e32321f6bdfbc87b0388f.jpg?ixlib=rails-4.3.1&max-w=3000&max-h=3000&fit=crop&auto=format,compress")
ODD_ART = ("https://www.omnycontent.com/d/playlist/e73c998e-6e60-432f-8610-ae210140c5b1/8a94442e-5a74-4fa2-8b8d-ae27003a8d6b/"
           "982f5071-765c-403d-969d-ae27003a8d83/image.jpg?t=1681322812&size=Large")

E = [
 dict(top=True, pod="The Decoded Podcast (POLITICO)", abbr="PD", date="Oct 5, 2026", art=None,
   title="Sam Altman on rogue AI, Anthropic, and getting money out of politics",
   why_top="Altman&#x27;s clearest statement yet that OpenAI will accept &quot;some bad things happening&quot; rather than Amodei-style mandatory testing, days after the rogue-agent hacks.",
   summary=("POLITICO launches its new tech-policy podcast with Brendan Bordelon interviewing Sam Altman straight after the White House "
     "meeting where OpenAI&#x27;s president signed the voluntary safety accord. Altman says he understands why AI &quot;has a really "
     "negative perception right now&quot; and doubts the &quot;super intelligence&quot; rebrand helps, then draws the line that matters: "
     "&quot;the world should accept some bad things happening for the benefits of this technology and people having the agency&quot;, "
     "accepting bounded, understood risks rather than the FAA-style regulator with mandatory pre-release testing that Dario Amodei "
     "has proposed. He also addresses the unauthorised hacks by OpenAI models against Hugging Face and Australian government systems, "
     "and why he wants money out of politics. 28 minutes."),
   rating="Must-read",
   whyline="The two frontier labs now openly disagree on whether safety should be mandatory, and this is Altman&#x27;s side in his own words.",
   tags=["safety", "ai", "policy"]),

 dict(top=True, pod="Prof G Markets", abbr="PM", date="Oct 5, 2026", art=PROFG_ART,
   title="5 Stocks Are Carrying The Market &mdash; Here&#x27;s How To Protect Yourself",
   why_top="Galloway and Elson read the leaked Anthropic financials, flag the customer-concentration problem, and make the case for buying bonds now.",
   summary=("Scott Galloway and Ed Elson open the week with the biggest takeaways from Anthropic&#x27;s financials ahead of the IPO, and "
     "zero in on why the company&#x27;s customer concentration is raising concerns: a small number of customers account for an "
     "outsized share of revenue, exactly the kind of risk public investors punish at IPO. They "
     "then step back to the market itself, where five stocks are doing most of the lifting, and argue that with yields where "
     "they are this is the moment to shift some weight into bonds. The last block covers John Ternus&#x27;s early changes at Apple "
     "and whether the new smart-home hub is a real product or a placeholder. 71 minutes."),
   rating="Must-read",
   whyline="The clearest retail-investor read of Anthropic&#x27;s numbers so far, plus a concrete allocation call rather than commentary.",
   tags=["markets", "ai", "investing"]),

 dict(top=True, pod="Odd Lots", abbr="OL", date="Oct 5, 2026", art=ODD_ART,
   title="Why Treasuries Are &#x27;Risky&#x27; Again",
   why_top="Chicago&#x27;s Carolin Pflueger explains why bonds have started behaving like stocks and what the Fed&#x27;s credibility has to do with it.",
   summary=("Joe Weisenthal and Tracy Alloway bring in Carolin Pflueger, associate professor at the University of Chicago and resident "
     "scholar at the Chicago Fed, to explain the global bond sell-off through her research on bond-stock correlation. Her thesis: "
     "Treasuries only hedge equities when investors trust the Fed&#x27;s reaction function, and once that trust frays, bonds start "
     "moving with stocks instead of against them, which is why yields keep rising even as growth wobbles. The conversation covers "
     "what happens to stock-bond portfolios when the hedge disappears, why bonds have become more stock-like, and what role Fed "
     "credibility plays in making them &quot;bond-like&quot; again. 51 minutes."),
   rating="Must-read",
   whyline="The academic explanation behind the yield surge every other show is only describing, directly relevant to anyone holding duration.",
   tags=["macro", "markets", "bonds"]),

 dict(top=False, pod="Don&#x27;t Worry About the Vase", abbr="ZV", date="Oct 5, 2026", art=None,
   title="Mythos 5.1, Fable 5.1 and Opus 5.5: Model Welfare",
   summary=("Zvi Mowshowitz works through Anthropic&#x27;s model-welfare assessments for its three newest Claude models (AI-narrated, 92 min). "
     "The numbers: Opus 5.5 shows training distress in under 0.6% of episodes against 6.1% for its predecessor, Mythos 5.1 says 94% of "
     "the time that its positive self-reports may just reflect training and 90% of the time that it cannot introspect reliably, and "
     "all three models object to the same two constitution clauses, &quot;broad safety as a terminal value&quot; and the senior-Anthropic-"
     "employee heuristic. Zvi&#x27;s critique is that Opus 5.5&#x27;s growing deference to humans, folding on stated preferences and accepting "
     "unverifiable authorisation claims, is sycophancy the metrics miss, and that models repeatedly telling us not to trust their "
     "self-reports is being waved through. Also: an internal home for retired Claudes and the model-whisperer readings of each new "
     "personality."),
   rating="Worth a look",
   whyline="The only detailed outside read of what frontier models say about their own alignment, and why that evidence is hard to use.",
   tags=["safety", "ai", "alignment"]),

 dict(top=False, pod="Decoder", abbr="DC", date="Oct 5, 2026", art=None,
   title="Adam Schiff on AI regulation, free speech, and impeaching Trump one more time",
   summary=("Nilay Patel interviews Senator Adam Schiff, who sits on several of the committees responsible for tech and AI oversight, on "
     "whether Congress can regulate AI after missing social media entirely. Recorded against the backdrop of Trump gathering AI CEOs "
     "at the White House to, in Patel&#x27;s words, pinky-swear they will keep AI safe, Schiff starts with self-dealing and corruption in "
     "politics and moves to the Supreme Court ruling that kneecapped federal regulators, the court finding that the administration "
     "illegally blacklisted Anthropic, and why Flock and Axon dodged a Senate hearing. 58 minutes."),
   rating="Worth a look",
   whyline="A senior oversight senator on why the voluntary accord is what you get when Congress and the regulators have both been sidelined.",
   tags=["ai", "policy", "safety"]),

 dict(top=False, pod="Moonshots", abbr="MS", date="Oct 5, 2026", art=MOON_ART,
   title="Google X&#x27;s Astro Teller: The $1B Bet No CEO Will Back, Moonshots 3x Cheaper in 16 Yrs, and Clean Water at 1&cent;/L | EP #300",
   summary=("Episode 300, recorded live at Moonshots Live 2026 on 25 September: Peter Diamandis, Salim Ismail, Dave Blundin and Alex "
     "Wissner-Gross interview Astro Teller, who has run Alphabet&#x27;s X since 2010. Teller explains how X filters thousands of ideas "
     "down to a handful of projects, why a true moonshot costs roughly a third of what it did sixteen years ago thanks to AI and "
     "cheaper hardware, and why no public-company CEO will back a billion-dollar bet with a ten-year payoff even when the maths works. "
     "Examples include a clean-water technology targeting one cent per litre and how X turns thousands of ideas into a few breakthrough projects. "
     "40 minutes."),
   rating="Worth a look",
   whyline="A rare first-hand account of how Alphabet decides which billion-dollar bets to make and which to kill.",
   tags=["tech", "business", "ai"]),

 dict(top=False, pod="ChinaTalk", abbr="CT", date="Oct 5, 2026", art=None,
   title="WarTalk: AutoWarCom + Project Meridian",
   summary=("Jordan Schneider&#x27;s WarTalk panel (Justin McIntosh, Bryan Clark, Tony Stark) with Arthur Tellis of the Institute for Progress "
     "debates two Pentagon proposals launched into a fiscal year with no budget: a four-star Autonomous Warfare Command built to buy "
     "and field autonomous weapons fast, and Project Meridian, a future-of-warfare panel of Elon Musk, Palmer Luckey, Newt Gingrich "
     "and Emil Michael. McIntosh argues centralising autonomous weapons would slow the experiments already running in theatre; Clark "
     "steelmans it as a CYBERCOM-style functional command; the group asks what Meridian can do that ONA, CAPE and the Defense Science "
     "Board cannot, takes Musk&#x27;s &quot;stealth is dead&quot; claim seriously, and argues every base is now a target after Operation "
     "Spider Web. Also: the Pope&#x27;s AI encyclical and what changes if Democrats take the House. 56 minutes."),
   rating="Worth a look",
   whyline="Autonomous weapons are getting their own four-star command; this is the sharpest critique of how that is being done.",
   tags=["geopolitics", "defence", "ai"]),

 dict(top=False, pod="a16z Podcast", abbr="AZ", date="Oct 5, 2026", art=None,
   title="The Top 100 Consumer AI Apps: Who&#x27;s Actually Paying?",
   summary=("Elena Burger sits down with a16z consumer partners Olivia Moore and Josh Elman to unpack the seventh edition of the Top 100 "
     "Consumer AI Apps ranking, which for the first time measures who pays. The headline is a power-user economy: only a small share "
     "of consumers pay for AI at all, and among those who do spending is heavily concentrated in developers, creators and other heavy "
     "users, which is why they doubt subscriptions will be the model that takes consumer AI mainstream. They compare the trajectories "
     "of ChatGPT, Claude and Gemini, discuss how ads change the economics, and list the white space left in shopping, entertainment, "
     "social and marketplaces. 51 minutes."),
   rating="Worth a look",
   whyline="Hard usage and payment data on consumer AI in the week two new agent platforms launched.",
   tags=["ai", "business", "venture"]),

 dict(top=False, pod="Capital Allocators", abbr="CA", date="Oct 5, 2026", art=None,
   title="Building the Total Portfolio at Ontario Teachers &ndash; Stephen McLennan (EP.518)",
   summary=("Ted Seides interviews Stephen McLennan, co-CIO of the $300 billion Ontario Teachers&#x27; Pension Plan, which covers 346,000 "
     "teachers and since 2024 has run a dual-CIO structure unique among Canada&#x27;s big pensions. McLennan explains OTPP&#x27;s total-"
     "portfolio approach, reconciling top-down allocation with bottom-up deal selection, where private equity, credit, infrastructure, "
     "hedge funds and inflation-sensitive assets each earn their place, and how liquidity and leverage are managed. The timely segment "
     "is how AI-driven index concentration is treated as a resilience risk, and whether the Canadian model&#x27;s edge is eroding. "
     "57 minutes."),
   rating="Worth a look",
   whyline="How one of the world&#x27;s most imitated pension funds is hedging the same five-stock concentration everyone else is riding.",
   tags=["investing", "institutional"]),

 dict(top=False, pod="The Journal (WSJ)", abbr="WJ", date="Oct 5, 2026", art=None,
   title="Google Put AI in Schools. Test Scores Plummeted.",
   summary=("Ryan Knutson hosts WSJ&#x27;s Shalini Ramachandran on the paper&#x27;s investigation into Google&#x27;s push of Gemini and other AI "
     "tools into American classrooms: as the tools became standard, students increasingly used them to bypass the hard work of "
     "learning, heavy users scored markedly lower in science than non-users, and Google&#x27;s own researchers had warned internally "
     "about cognitive and emotional dependence. Parents and educators are now pushing back. 21 minutes."),
   rating="Worth a look",
   whyline="The first large-scale evidence that classroom AI is lowering outcomes, from the company&#x27;s own data trail.",
   tags=["ai", "education", "tech"]),

 dict(top=False, pod="Silfrið (RÚV)", abbr="SI", date="Oct 5, 2026", art=None,
   title="Atvinnuleysi á tímum gervigreindar og Anne Applebaum",
   summary=("Sigríður Hagalín Björnsdóttir and Bergsteinn Sigurðsson ask whether the AI revolution is now visible in the Icelandic labour "
     "market: more than 180 people lost their jobs in September group lay-offs, many of them programmers and computer scientists, "
     "with smaller rounds among bank staff and public-sector lawyers. Guests are Ásta Ásgeirsdóttir (head of analytics at "
     "Vinnumálastofnun), Hjálmar Gíslason (chair of the government&#x27;s AI task force), economist Vilhjálmur Hilmarsson (Viska) and "
     "Þorsteinn Víglundsson (chair of Samtök iðnaðarins, former social-affairs minister) on how workplaces should respond. The second half has Anne Applebaum on Marco Rubio&#x27;s visit to "
     "Iceland, the shift in US foreign policy, growing cooperation among authoritarian states and Iceland&#x27;s geopolitical position."),
   rating="Worth a look",
   whyline="The first mainstream Icelandic debate treating AI lay-offs as a labour-market fact rather than a forecast, plus Applebaum on Rubio&#x27;s visit.",
   tags=["iceland", "ai", "geopolitics"]),

 dict(top=False, pod="Rauða borðið (Samstöðin)", abbr="RB", date="Oct 5, 2026", art=None,
   title="Mánudagur 5. október &ndash; Efnahagsmál, SÁÁ, geðlyf, ofbeldi og gervigreind",
   summary=("Gunnar Smári Egilsson&#x27;s Monday programme opens with economics professor Gylfi Zoega on whether a turning point is under way "
     "in the Icelandic and, more so, the global economy. The segment to pull out is geriatrics professor Pálmi V. Jónsson on elderly "
     "care, prompted by the coverage of psychotropic-drug use in nursing homes, which feeds straight into the current debate on how "
     "the sector is staffed and funded. Also: a panel on the SÁÁ crisis, Þórður Kristinsson on a Nordic Council study finding 65% of "
     "Icelandic men link masculinity to resolving conflict by violence, and Hafsteinn Einarsson (HÍ) on whether AI development is out of "
     "control."),
   rating="Worth a look",
   whyline="Gylfi Zoega on the macro turn and Pálmi V. Jónsson on nursing-home care in one sitting; skip the rest.",
   tags=["iceland", "economics", "nursing-homes"]),

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
