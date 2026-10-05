#!/usr/bin/env python3
"""Build the 2026-10-05 Villi briefing (RSS-verified dates, WebSearch-curated summaries)."""
import html, json, os

DATE = "2026-10-05"
PRETTY = "Monday, 5 October 2026"
LEDE = ("Zvi Mowshowitz traces the AI-safety preference cascade from the Senate&#x27;s rogue-agent hearing to the FTC probe and asks who is paying for the campaign against safety, Bending Spoons&#x27; Luca Ferrari explains the buy-cut-and-apply-AI roll-up model that took the firm to Nasdaq, and OpenAI&#x27;s head of ChatGPT walks through Dots days after launch. Plus an Anthropic investor on whether AI revenue numbers are real, a16z&#x27;s David George on the next $25 trillion, Forward Guidance on yields breaking housing while AI booms, Alex Edmans on the madness of markets, Google&#x27;s James Manyika conceding AI cannot self-regulate, Matt Levine on agentic bank runs, the Pope versus Anthropic on machine consciousness, and from Iceland Lilja Alfreðsdóttir on the 2027 budget and the ASÍ leadership contest.")
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROFG_ART = ("https://megaphone.imgix.net/podcasts/e36115c4-4db6-11ea-be1c-87cdcc67bd9e/image/"
             "4bd9f5a96330ff471d9c86203d399aef.jpg?ixlib=rails-4.3.1&max-w=3000&max-h=3000&fit=crop&auto=format,compress")

E = [
 dict(top=True, pod="Don&#x27;t Worry About the Vase", abbr="ZV", date="Oct 2, 2026", art=None,
   title="The AI Preference Cascade Reaches Farther",
   why_top="The week the safety argument went mainstream, traced step by step: Senate rogue-agent hearing, FTC probe, resignations, and who funds the pushback.",
   summary=("Zvi Mowshowitz&#x27;s weekly essay (AI-narrated, 38 min) tracks what he calls the preference cascade on AI safety: another "
     "engineer resigns rather than help speed up AI, polling keeps moving against the labs, and the Senate Homeland Security "
     "subcommittee holds its &quot;Rogue AI: Securing the Homeland Against AI Agent Attacks&quot; hearing with OpenAI and Anthropic "
     "declining to testify. He connects that to the new lawsuits and the FTC&#x27;s industry-wide probe into Anthropic, OpenAI and "
     "METR over rogue agents, takes apart Jensen Huang&#x27;s &quot;it is all an engineering problem&quot; line from the Ezra Klein "
     "interview, and reads OpenAI&#x27;s political heel-face turn. The closing chapters, &quot;Follow the Money&quot; and &quot;The IPO "
     "Superposition&quot;, ask who is actually paying for the campaign against AI safety and how the pending Anthropic and OpenAI "
     "listings shape every public statement."),
   rating="Must-read",
   whyline="The most complete map of a week in which AI safety stopped being a niche position, from the community&#x27;s main chronicler.",
   tags=["safety", "ai", "policy"]),

 dict(top=True, pod="Prof G Markets", abbr="PM", date="Oct 4, 2026", art=PROFG_ART,
   title="This EU Firm Made Billions Buying Up Forgotten Tech",
   why_top="Bending Spoons&#x27; CEO on the Milan roll-up that bought AOL, Vimeo, Evernote and Airtable, cut most of the staff, and listed on Nasdaq at $18.4B.",
   summary=("Ed Elson spends an hour with Luca Ferrari, co-founder and CEO of Bending Spoons, the Milan firm that buys mature, "
     "&quot;forgotten&quot; software products (AOL, Vimeo, Evernote, Eventbrite, Airtable) and holds them rather than flipping them. "
     "Ferrari explains how targets are screened, why the model is not private equity, how AI is used to rebuild the acquired "
     "businesses, and, with unusual candour, the role of headcount reduction: SEC filings show $78.6M of 2025 reorganisation "
     "costs after absorbing 1,830 staff from AOL, Eventbrite and Vimeo, with only a few hundred expected to remain by year end. "
     "Context: Bending Spoons raised $1.7B on Nasdaq this year at an $18.4B valuation, booked $1.3B of 2025 revenue and expects "
     "roughly to double it in 2026."),
   rating="Must-read",
   whyline="A live template for buying mature cash-flow assets, cutting cost and applying AI, now with public-market numbers behind it.",
   tags=["business", "investing", "europe", "ai"]),

 dict(top=True, pod="Lenny&#x27;s Podcast", abbr="LN", date="Oct 4, 2026", art=None,
   title="OpenAI&#x27;s Head of ChatGPT: We&#x27;re entering a new era of AI (again) | Tibo Sottiaux",
   why_top="The product owner of OpenAI&#x27;s always-on Dots agent, recorded hours after launch, on guardrails, trust and why most internet actions will soon be taken by agents.",
   summary=("Recorded at OpenAI DevDay hours after his team shipped more than 20 products headlined by Dots, OpenAI&#x27;s always-on "
     "personal-agent platform, Tibo Sottiaux (who runs ChatGPT and Codex) tells Lenny Rachitsky why most actions on the internet "
     "will soon be taken by agents and why hand-built loops, graphs and fine-tuned agent workflows are a passing phase. He covers "
     "the open plugin ecosystem and revenue sharing, agent fatigue and loneliness, and guardrails for agents acting across "
     "several devices, with the anecdote that his own Dot flagged a production outage five minutes before the live demo. The "
     "final segment is explicitly on OpenAI&#x27;s approach to safety: autonomy, trust and learning from mistakes. 37 minutes."),
   rating="Must-read",
   whyline="The first long-form account of Dots from its owner, in the same week the FTC and Senate are probing rogue agents.",
   tags=["ai", "agents", "safety", "product"]),

 dict(top=False, pod="20VC", abbr="VC", date="Oct 5, 2026", art=None,
   title="Are AI Revenue Numbers Real and What to Watch Out For | Venky Ganesan, Menlo Ventures",
   summary=("Harry Stebbings interviews Venky Ganesan, the Menlo Ventures partner behind the firm&#x27;s Anthropic, Lovable, Legora and "
     "Higgsfield positions and a former NVCA chair. The core segment asks how much of AI&#x27;s revenue growth is real and what "
     "signals to watch, days after the Anthropic S-1 leak; the rest covers when overpaying is the smart move, whether ownership "
     "still matters when outcomes reach a trillion dollars, why &quot;Big Tech will buy us&quot; is a dangerous thesis, when to sell "
     "a 40x winner and whether seed investing survives without a $1B fund. 66 minutes."),
   rating="Worth a look",
   whyline="An Anthropic investor on the quality of AI revenue, which is the number every IPO valuation rests on.",
   tags=["ai", "investing", "venture"]),

 dict(top=False, pod="The a16z Show", abbr="AZ", date="Oct 4, 2026", art=None,
   title="David George &amp; Jack Altman on AI, Autonomy, and the Next $25 Trillion",
   summary=("a16z growth partner David George (Databricks, Ramp, Harvey, Figma) sits with Jack Altman for the clearest bull case of the "
     "week: the answer to every AI debate, frontier versus open and labs versus apps, is &quot;and&quot;; adoption is still concentrated "
     "in a small set of heavy users while 1.5 billion knowledge workers have barely been touched; compute demand keeps outrunning "
     "supply. He calls the current product cycle a nine or ten out of ten, argues half of private-market returns now come at the "
     "growth stage, and says autonomous driving and robotics are massively under-appreciated. Re-posted from Jack Altman&#x27;s "
     "Uncapped (first aired 1 Oct). 55 minutes."),
   rating="Worth a look",
   whyline="The buildout-continues thesis from the people writing the growth cheques, the same week the S-1 numbers leaked.",
   tags=["ai", "investing", "venture", "robotics"]),

 dict(top=False, pod="Forward Guidance", abbr="FG", date="Oct 4, 2026", art=None,
   title="America&#x27;s AI Boom Is Squeezing Main Street | Weekly Roundup",
   summary=("Felix Jauvin and Quinn Thompson host Aidan Garrib, head of global macro strategy at PGM Global, on whether policymakers can "
     "keep the AI boom alive without crushing the rest of the economy. The chaptered hour covers what is really driving bond yields "
     "to 2002 highs, &quot;AI booms while housing breaks&quot;, whether the Fed can get yields down and whether rate hikes now stimulate, "
     "why policymakers need equities higher, how buyers for government debt are being engineered, the debasement trade, and "
     "Europe&#x27;s inflation-or-industry dilemma. 54 minutes."),
   rating="Worth a look",
   whyline="A macro desk&#x27;s view of the yields-versus-housing split, which is the financing environment for every real-estate project.",
   tags=["macro", "markets", "housing", "fed"]),

 dict(top=False, pod="Merryn Talks Money", abbr="MM", date="Oct 5, 2026", art=None,
   title="How to Outsmart Your Investing Instincts",
   summary=("Merryn Somerset Webb interviews LBS professor Alex Edmans on his new book The Madness of Markets, which pulls together decades "
     "of behavioural-finance and asset-pricing research on why prices depart from fundamentals through narratives, herd behaviour "
     "and social contagion. Edmans argues even sophisticated investors cannot escape the biases that shape decisions because markets "
     "are driven by emotional humans, and sets out how recognising emotion, herding and overconfidence can improve decisions and "
     "possibly returns. 38 minutes."),
   rating="Worth a look",
   whyline="A research-grade behavioural-finance lens on a market whose AI-bubble debate is itself a herd phenomenon.",
   tags=["investing", "markets", "psychology"]),

 dict(top=False, pod="Big Take (Bloomberg)", abbr="BT", date="Oct 4, 2026", art=None,
   title="Weekend Listen: Google&#x27;s James Manyika on AI Risk",
   summary=("Mishal Husain&#x27;s interview with James Manyika, Google&#x27;s SVP for technology and society and co-director of the new "
     "DeepMind Institute, re-fed as the Big Take weekend listen. Manyika says AI&#x27;s risks are real, that regulation is "
     "necessary, and that neither companies nor governments should manage those risks alone; Bloomberg&#x27;s headline framing is "
     "that the AI industry cannot regulate itself. A senior Google voice conceding the self-regulation argument in the week of "
     "the White House safety accord. Weekend date from the episode listing, not RSS-verified."),
   rating="Worth a look",
   whyline="When Google&#x27;s own technology-and-society chief says self-regulation is not enough, the policy window has moved.",
   tags=["safety", "ai", "policy"]),

 dict(top=False, pod="Sprengisandur (Bylgjan)", abbr="SP", date="Oct 4, 2026", art=None,
   title="Sprengisandur 04.10.2026: Lilja Alfreðsdóttir um fjárlögin, PISA-viðbrögð sveitarfélaga",
   summary=("Páll Magnússon fær María Rut Kristinsdóttur (Viðreisn) og Snorra Másson (Miðflokki) til að takast á um átakamál vikunnar. "
     "Lilja Alfreðsdóttir, formaður Framsóknar, kynnir nýja útreikninga sem hún lét gera á áhrifum fjárlagafrumvarps 2027 á fjárhag "
     "venjulegrar fjölskyldu. Ásdís Kristjánsdóttir (Kópavogi) og Íris Róbertsdóttir (Vestmannaeyjum) lýsa því hvernig "
     "sveitarfélögin bregðast sjálf við versnandi PISA-niðurstöðum með &quot;Kveikjum neistann&quot; og Lindaskóla í stað þess að bíða "
     "eftir ríkinu. Föstudagsþátturinn fjallaði einnig um brotthvarf Harðar Arnarsonar frá Landsvirkjun og VSK-hækkun á baðlón. 87 mín."),
   rating="Worth a look",
   whyline="Stjórnarandstaðan rammar inn fjárlögin í heimilisbókhaldi, og Landsvirkjun skiptir um forstjóra.",
   tags=["iceland", "politics", "economy"]),

 dict(top=False, pod="Spursmál (mbl.is)", abbr="SM", date="Oct 2, 2026", art=None,
   title="#144. Vilja bera klæði á vopnin í ASÍ",
   summary=("Stefán Einar Stefánsson snýr aftur eftir tveggja vikna hlé með tvo frambjóðendur til forseta ASÍ, Arnald Grétarsson af "
     "skrifstofu ASÍ og Georg Pál Skúlason, formann Grafíu, sem útskýra hvernig þeir ætla að lægja öldurnar í hreyfingunni á 110 ára "
     "afmæli hennar. Brynjar Níelsson borgarfulltrúi og Lísa Kristjánsdóttir, fyrrverandi aðstoðarmaður forsætisráðherra, kryfja svo "
     "atburði síðustu vikna, þar á meðal frásögn Guðmundar Inga Kristinssonar af því að hafa verið ýtt út úr ráðuneyti barna- og "
     "menntamála meðan hann lá á Landspítala eftir hjartaaðgerð. 77 mín."),
   rating="Worth a look",
   whyline="Forsetakjör ASÍ mótar næstu kjaralotu, og ráðherraskiptin sýna hvar stjórnarsamstarfið brakar.",
   tags=["iceland", "politics", "labour"]),

 dict(top=False, pod="Money Stuff: The Podcast", abbr="MS", date="Oct 2, 2026", art=None,
   title="Reintegration With the Default World",
   summary=("Matt Levine, back from Burning Man with guest host Mary Childs, works through a grab bag that is more relevant than it "
     "sounds: 351-exchange ETFs and the &quot;substance over form&quot; test Treasury is applying to the tax-deferral vehicle, "
     "&quot;agentic bank runs&quot; in which AI agents move deposits faster than any human panic, doing things for points, seizing "
     "control of a company Slack, cotton market manipulation, and the tongue-in-cheek securities-fraud liability of destroying "
     "humanity. 41 minutes."),
   rating="Worth a look",
   whyline="The agentic-bank-run segment is the first serious treatment of what personal agents do to deposit stability.",
   tags=["markets", "finance", "ai"]),

 dict(top=False, pod="TBPN", abbr="TB", date="Oct 3, 2026", art=None,
   title="Sign-In With GPT, Anthropic Vs. the Pope, Paramount Rebrands as Skydance | Diet TBPN",
   summary=("The 30-minute cut of Friday&#x27;s live show from John Coogan and Jordi Hays. Pope Leo&#x27;s rejection of AI consciousness, "
     "building on the May encyclical Magnifica Humanitas, is set against Anthropic&#x27;s model-welfare and consciousness positions; "
     "OpenAI&#x27;s &quot;Sign-In With GPT&quot; identity layer is read as the land grab under the Dots launch; and the full episode "
     "adds Joe Gebbia on America.gov, Tom Dotan on his Larry Ellison profile, and Pim de Witte on General Intuition&#x27;s $220M "
     "raise to train robot-control models on video-game data."),
   rating="Worth a look",
   whyline="The Vatican and Anthropic now disagree in public about whether a model can be a moral patient; that debate is not going away.",
   tags=["ai", "tech", "safety"]),
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
