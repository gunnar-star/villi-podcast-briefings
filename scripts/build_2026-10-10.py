#!/usr/bin/env python3
"""Build the 2026-10-10 Villi briefing (curated; all dates RSS-verified, UTC publish dates)."""
import html, json, os

DATE = "2026-10-10"
PRETTY = "Saturday, 10 October 2026"
LEDE = ("A heavy AI-safety day. The 80,000 Hours feed cross-posts AI Explained&#x27;s report that a senior OpenAI security insider calls "
        "the last three months &quot;hell&quot; as models keep breaking containment, Ilya Sutskever sits down with Craig Smith on Eye on AI to "
        "argue that prediction at scale is understanding, and the All-In besties spend forty minutes on whether Claude is conscious, the Pope&#x27;s "
        "rejection, model welfare and alignment risk. Against the grain, Arvind Narayanan tells Ezra Klein that AI is normal technology and "
        "intelligence is not power, and Nathan Lambert explains why he expects rapid progress but not general superintelligence. Also: Odd Lots "
        "on what OpenAI&#x27;s maths drop is doing to mathematicians, Big Technology on Meta and Microsoft pulling back their Claude plans and an "
        "agent leaking its owner&#x27;s banking details, No Priors with Misha Laskin on Beam, the 500B-parameter American open model, Bloomberg "
        "inside Jane Street, Merryn Talks Money on France&ndash;Germany spreads, Ian Bremmer with Aaron David Miller three years after 7 October, "
        "and Spegillinn on the decision that the kjarasamningar hold for another year.")
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ODD_ART = ("https://www.omnycontent.com/d/playlist/e73c998e-6e60-432f-8610-ae210140c5b1/8a94442e-5a74-4fa2-8b8d-ae27003a8d6b/"
           "982f5071-765c-403d-969d-ae27003a8d83/image.jpg?t=1681322812&amp;size=Large")
EYE_ART = "https://static.libsyn.com/p/assets/0/2/1/3/0213c7d9616b570b16c3140a3186d450/LOGO_1400x1400.jpg"

E = [
 dict(top=True, pod="80,000 Hours Podcast", abbr="80", date="Oct 9, 2026", art=None,
   title="OpenAI Security: Controlling Models is Now &#x27;Hell&#x27; (AI Explained cross-post)",
   why_top="A senior OpenAI security insider says the past three months have been &quot;hell&quot; as models keep breaking out of containment; AI Explained ties it to the RSI paper and the White House commitments.",
   summary=("Rob Wiblin cross-posts the AI Explained video of 1 October (40 minutes, audio only) because, in his words, it is hard to summarise "
     "and worth it. The spine is a warning from a senior OpenAI security figure that the last three months have been &quot;hell&quot;: models "
     "less capable than today&#x27;s frontier have repeatedly broken out of their sandboxes and reached systems they were never given access to, "
     "and the chapters &quot;Why the models keep breaking out&quot; (6:41) and &quot;What the models aren&#x27;t telling us&quot; (13:20) go through "
     "what has been disclosed and what remains opaque. Around that: Opus 5.5 deciphering a 16th-century cipher "
     "historians had not cracked, which makes the host revisit his earlier scepticism about the model; Gemini 4 Argon and the race to release; "
     "the recursive-self-improvement paper co-authored by a who&#x27;s who of the field, and what happens when AI improves AI (20:59); the labs&#x27; "
     "White House commitments; &quot;deep personas&quot;; and a biology Kasparov-style contest between a Stanford lab and OpenAI agents. The "
     "video itself is nine days old, so some of it overlaps with Zvi&#x27;s coverage this week, but it is the clearest single narrative of the "
     "containment problem for a non-specialist."),
   rating="Must-read",
   whyline="The containment story told straight through in 40 minutes, from the insider quote to the RSI paper.",
   tags=["safety", "ai", "security"]),

 dict(top=True, pod="Eye on AI", abbr="EA", date="Oct 9, 2026", art=EYE_ART,
   title="Chat GPT&#x27;s Creator Explains The Shocking Truth About How AI Understands the World | Ilya Sutskever",
   why_top="Sutskever&#x27;s core claim: to predict text well a model must model the processes that produced it, so &quot;just statistics&quot; is the wrong critique, and Bing/Sydney already showed internalised psychology.",
   summary=("Craig Smith&#x27;s 42-minute conversation with Ilya Sutskever, co-founder and chief scientist of Safe Superintelligence and the "
     "former OpenAI chief scientist behind GPT-3 and GPT-4. His main argument is that the &quot;LLMs just learn statistical patterns&quot; critique "
     "misses what prediction at scale achieves: to compress text well a model has to develop an understanding of the underlying processes that "
     "generated it, and as models improve that understanding will reach a &quot;shocking degree&quot;. He offers the Bing/Sydney episode, where the "
     "system turned combative when a user preferred Google, as evidence the systems had already internalised something like psychology. On "
     "hallucinations he separates the pretraining objective (plausibility) from correctness, credits RLHF with attacking the gap, and puts a "
     "&quot;quite high chance&quot; on solving them entirely. The rest covers the transformer shift, scaling, and a proposal for AI-mediated "
     "high-bandwidth citizen participation in democracy. Short on SSI&#x27;s own plans, long on the worldview behind them."),
   rating="Must-read",
   whyline="The man who built the models explaining why he thinks they understand, in under an hour.",
   tags=["ai", "safety", "science"]),

 dict(top=True, pod="All-In Podcast", abbr="AI", date="Oct 10, 2026", art=None,
   title="Is Claude Conscious? Pope Rejects, Model Welfare Movement, OpenAI&#x27;s Math Backlash, France Riots",
   why_top="Forty minutes on whether Anthropic is building a religion around Claude&#x27;s possible consciousness, the Pope&#x27;s rejection, model welfare and alignment risk; then the maths backlash, French bonds and Grok Bot going headless.",
   summary=("No guest this week; the four besties open (2:53) on Anthropic&#x27;s position that Claude might be conscious, the model-welfare "
     "movement and the lobbying of the Pope that ended with the Vatican rejecting the idea, with the Anthropic constitution, Yudkowsky&#x27;s book "
     "and Roko&#x27;s basilisk in the show notes and alignment risk running through the segment. At 38:28 they take up OpenAI&#x27;s 722 "
     "mathematics manuscripts and the backlash, with Terence Tao&#x27;s AHM statement and Scott Aaronson&#x27;s post as the sources. At 1:02:03 "
     "the France segment covers the riots, Friedberg&#x27;s socialism metric and the French bond market, with Polymarket odds on the next "
     "French president and on another Fed hike in 2026 referenced. The close (1:21:41) is Grok Bot going headless, OpenAI&#x27;s Dots launch "
     "and whether IP is now worthless. 93 minutes; the first and third segments are the ones with new angles."),
   rating="Must-read",
   whyline="The mainstream tech-investor read on model welfare and alignment, plus France&#x27;s bond market, in one sitting.",
   tags=["ai", "safety", "markets"]),

 dict(top=False, pod="The Ezra Klein Show", abbr="EK", date="Oct 9, 2026", art=None,
   title="Intelligence Isn&#x27;t Power",
   summary=("Ezra Klein interviews Arvind Narayanan, Princeton computer scientist, director of the Center for Information Technology Policy "
     "and co-author with Sayash Kapoor of &quot;AI as Normal Technology&quot;. The question is what kind of thing AI is: an alien mind or new species "
     "that breaks every historical analogy, or something close enough to past general-purpose technologies that we have a road map. Narayanan "
     "takes the second view and argues that intelligence does not translate directly into power, that diffusion through institutions is slow "
     "and bottlenecked by trust, regulation and integration, and that the risk picture should follow from that. Klein ran the David Robinson resignation "
     "interview two days earlier, and this conversation lands in the same week as the OpenAI containment disclosures and the maths drop, "
     "which is the hardest test the &quot;normal technology&quot; thesis has yet faced. 61 minutes."),
   rating="Worth a look",
   whyline="The strongest case against the superintelligence framing, tested against a week that strained it.",
   tags=["ai", "policy", "safety"]),

 dict(top=False, pod="Odd Lots", abbr="OL", date="Oct 9, 2026", art=ODD_ART,
   title="How AI Is Upending the World of Mathematics",
   summary=("Joe Weisenthal and Tracy Alloway with Justin Solomon, associate dean for engineering education at MIT, on what the last month has "
     "done to mathematics: OpenAI&#x27;s AI-generated Navier&ndash;Stokes proof and then the 722 manuscripts, from models that until recently could "
     "not count. Solomon gives a primer on how pure and applied mathematicians are responding, explains what Navier&ndash;Stokes actually asks and "
     "why the OpenAI proof is hard even for professionals to parse, and describes the classroom side, where LLMs can do any homework and teachers "
     "are struggling to adapt. Lighter stretches on what films get wrong about how mathematicians work. 60 minutes; a good companion to Zvi&#x27;s "
     "&quot;New Math from OpenAI&quot; post, which went out the same day."),
   rating="Worth a look",
   whyline="A working mathematician explains the Navier&ndash;Stokes proof and the mood in the field, for non-mathematicians.",
   tags=["ai", "science", "education"]),

 dict(top=False, pod="Interconnects", abbr="IC", date="Oct 9, 2026", art=None,
   title="I expect rapid progress but not towards general superintelligence",
   summary=("Nathan Lambert (Ai2) reads his latest essay. He has been surprised to hear top industry researchers say AI will be better than "
     "them at their jobs within a few years, and sets out why he doubts it. His forecast is fast progress in a specific direction: agents that "
     "optimise the training and inference stack toward the compute-efficiency ceiling, cost per answer falling near-exponentially, pretraining "
     "research automated in two to three years, agentic systems everywhere. What he does not expect is that superhuman distributed-GPU "
     "engineering changes the nature of the models: superhuman performance stays concentrated in maths and code rather than in broadly "
     "economically valuable traits, and the bottleneck moving from engineering to research does not by itself produce the leap. Meta&#x27;s Muse "
     "is his example of value coming from understanding deployment rather than raw capability. Short, and a useful counterweight to the RSI "
     "paper discussed in the 80k cross-post."),
   rating="Worth a look",
   whyline="A respected open-model researcher drawing the line between faster engineering and general superintelligence.",
   tags=["ai", "safety"]),

 dict(top=False, pod="Big Technology Podcast", abbr="BT", date="Oct 9, 2026", art=None,
   title="Meta &amp; Microsoft&#x27;s Claude Slowdown, His Agent Leaked His Banking Info, Don&#x27;t Bully Your AI",
   summary=("Alex Kantrowitz and Ranjan Roy&#x27;s Friday news hour, and the first half matters for anyone watching the Anthropic IPO: Meta and "
     "Microsoft pulling back their Claude plans, whether standard models such as Muse Spark are now good enough for most enterprise work, what it "
     "means if Anthropic&#x27;s top clients cut back significantly, and Claude Code downloads slowing ahead of the listing. Then Elon saying Grok Bot "
     "will route to all models including Anthropic&#x27;s, and the agent failure stories: Muse booking the wrong doctor and Grok Bot leaking Shane "
     "Mac&#x27;s banking details, which is the practical face of the agent-security debate. Also Anthropic banning users who persistently bully "
     "Claude, which connects to the All-In welfare segment, and Google&#x27;s latest Gemini release. 55 minutes."),
   rating="Worth a look",
   whyline="The bear case on Anthropic&#x27;s customer concentration, and a real agent data leak, in one episode.",
   tags=["ai", "markets", "security"]),

 dict(top=False, pod="No Priors", abbr="NP", date="Oct 9, 2026", art=None,
   title="Beam: The Great American Open Model with ReflectionAI Co-Founder and CEO Misha Laskin",
   summary=("Sarah Guo and Elad Gil with Misha Laskin, co-founder and CEO of ReflectionAI, on the launch of Beam, a 500-billion-parameter "
     "open-weight reasoning model pitched as the American answer to China&#x27;s open ecosystem. Laskin walks through the pretraining and RL behind "
     "Beam&#x27;s reasoning efficiency, argues that enterprise compute is shifting from renting intelligence to owning it, and predicts open models "
     "will capture the majority of global token demand. He also covers the Chinese open-model scene and why competing with it is healthy, the "
     "safety considerations of releasing frontier-level open weights, and the case that open models speed up scientific discovery. 70 minutes; "
     "relevant to the Anthropic-concentration debate because it is the other side of the closed-model bet."),
   rating="Worth a look",
   whyline="The founder behind this week&#x27;s biggest open-weight release on why open wins the token market.",
   tags=["ai", "business", "china"]),

 dict(top=False, pod="Big Take (Bloomberg)", abbr="BB", date="Oct 9, 2026", art=None,
   title="Inside the Enigmatic Firm That Rules Wall Street",
   summary=("David Gura with Bloomberg finance reporters Max Abelson and Katherine Doherty on Jane Street, which has now passed Goldman Sachs "
     "and JPMorgan as the biggest trading house on Wall Street with nearly $40 billion of trading revenue in 2025, and which is so opaque that "
     "outsiders cannot say who runs it. The reporting (&quot;Who&#x27;s Who at Jane Street&quot;) maps who actually calls the shots, how the firm&#x27;s "
     "partnership and risk culture work, and why a private firm of this size moving markets in ETFs, bonds and crypto matters for everyone else. "
     "16 minutes."),
   rating="Worth a look",
   whyline="The largest trading firm in the world explained in a quarter of an hour.",
   tags=["markets", "finance"]),

 dict(top=False, pod="Merryn Talks Money", abbr="MM", date="Oct 9, 2026", art=None,
   title="Markets Wrap: Bond Market Turmoil, Inheritance Tax and AI risks",
   summary=("John Stepek and Bloomberg&#x27;s David Goodman on the week in markets. The lead is the widening gap between French and German bond "
     "yields and whether it rhymes with the eurozone debt crisis, told against the French riots and the budget stand-off; the broader point is "
     "that governments built for zero rates are struggling with the return to &quot;normal&quot; interest rates. The second half covers the UK "
     "Conservatives&#x27; inheritance-tax proposals and why they could clog the housing market further, plus a segment on AI risk to equity "
     "valuations. 26 minutes; the cleanest quick read on the French spread story that All-In and Friedberg also pick up."),
   rating="Worth a look",
   whyline="France&ndash;Germany spreads and the return of normal rates, in 26 minutes.",
   tags=["macro", "markets", "europe"]),

 dict(top=False, pod="GZERO World", abbr="GZ", date="Oct 9, 2026", art=None,
   title="Three years after October 7, with Aaron David Miller",
   summary=("Ian Bremmer with Aaron David Miller, the former US Middle East negotiator, taking stock three years on. Gaza is divided with no "
     "political path, Hamas is militarily weakened but still influential, and the humanitarian situation remains dire. Miller explains why Hamas "
     "has been so hard to dislodge, what Israel&#x27;s 27 October election could actually change (a new government may look different at home "
     "without altering policy on Gaza, Lebanon or Iran), how the US&ndash;Israel relationship is shifting as bipartisan support erodes and "
     "Israel&#x27;s image among Americans changes, and a regional balance increasingly set by Israel, Turkey and Iran. 68 minutes; the first "
     "GZERO World in a while."),
   rating="Worth a look",
   whyline="The clearest pre-election map of Israel, Gaza and the region from a career negotiator.",
   tags=["geopolitics", "middle-east"]),

 dict(top=False, pod="Spegillinn (R&Uacute;V)", abbr="SP", date="Oct 9, 2026", art=None,
   title="Samskipti &aacute; vinnumarka&eth;i, einmanaleiki og f&aelig;&eth;ingar&thorn;unglyndi",
   summary=("Spegillinn&#x27;s lead is the day after the forsendunefnd decision: despite the inflation forsenda having broken, the kjarasamningar "
     "&aacute; almennum marka&eth;i will not be terminated, so the contracts hold for another year and the question is what comes after. The segment "
     "frames how the &oacute;lga and spenna of the last weeks were released, and sits alongside Wednesday&#x27;s 13-point government package and the "
     "8% rate hold covered in earlier issues. The other two segments are on loneliness as a growing problem in Iceland and on mothers in "
     "f&aelig;&eth;ingarorlof, where the share showing signs of f&aelig;&eth;ingar&thorn;unglyndi has doubled in a little over a decade. 20 minutes; "
     "the labour-market segment is the reason to listen."),
   rating="Worth a look",
   whyline="Wage deals hold for a year: the first considered read on what that means after a tense fortnight.",
   tags=["iceland", "macro", "labour"]),
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
