#!/usr/bin/env python3
"""Villi Podcast Briefing Generator — RSS-based, no AI needed."""

import feedparser
import json
import os
import re
import html
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import quote

# ── Podcast RSS feeds ──────────────────────────────────────────────
FEEDS = {
    "Prof G Pod": {
        "url": "https://feeds.megaphone.fm/WWO6655869236",
        "tags": ["markets", "geopolitics"],
        "art": "https://megaphone.imgix.net/podcasts/e36115c4-4db6-11ea-be1c-87cdcc67bd9e/image/4bd9f5a96330ff471d9c86203d399aef.jpg?ixlib=rails-4.3.1&max-w=3000&max-h=3000&fit=crop&auto=format,compress",
        "code": "PG",
    },
    "All-In Podcast": {
        "url": "https://allinchamathjason.libsyn.com/rss",
        "tags": ["ai", "markets", "business"],
        "art": None,
        "code": "AI",
    },
    "Invest Like the Best": {
        "url": "https://feeds.megaphone.fm/investlikethebest",
        "tags": ["investing", "business"],
        "art": "https://megaphone.imgix.net/podcasts/ef669774-cccd-11ed-889b-c36caad6646f/image/158efdddfb983d2678b3530d484e8aa2.jpg?ixlib=rails-4.3.1&max-w=3000&max-h=3000&fit=crop&auto=format,compress",
        "code": "IB",
    },
    "Moonshots": {
        "url": "https://feeds.megaphone.fm/DVVTS2890392624",
        "tags": ["ai", "tech", "business"],
        "art": "https://megaphone.imgix.net/podcasts/9eb5a878-c1b6-11ed-9db0-0b7bbbf6e859/image/b0f62543099e32321f6bdfbc87b0388f.jpg?ixlib=rails-4.3.1&max-w=3000&max-h=3000&fit=crop&auto=format,compress",
        "code": "MS",
    },
    "Odd Lots": {
        "url": "https://www.bloomberg.com/feeds/podcasts/odd_lots.xml",
        "tags": ["markets", "economics"],
        "art": "https://www.omnycontent.com/d/playlist/e73c998e-6e60-432f-8610-ae210140c5b1/8a94442e-5a74-4fa2-8b8d-ae27003a8d6b/982f5071-765c-403d-969d-ae27003a8d83/image.jpg?t=1681322812&size=Large",
        "code": "OL",
    },
    "Eye on AI": {
        "url": "https://aneyeonai.libsyn.com/rss",
        "tags": ["ai"],
        "art": "https://static.libsyn.com/p/assets/0/2/1/3/0213c7d9616b570b16c3140a3186d450/LOGO_1400x1400.jpg",
        "code": "EA",
    },
    "Dwarkesh Podcast": {
        "url": "https://api.substack.com/feed/podcast/69345.rss",
        "tags": ["ai", "science"],
        "art": None,
        "code": "DW",
    },
    "Latent Space": {
        "url": "https://api.substack.com/feed/podcast/1084089.rss",
        "tags": ["ai", "tech"],
        "art": None,
        "code": "LS",
    },
    "Lex Fridman Podcast": {
        "url": "https://lexfridman.com/feed/podcast/",
        "tags": ["ai", "science", "tech"],
        "art": None,
        "code": "LF",
    },
    "No Priors": {
        "url": "https://feeds.megaphone.fm/nopriors",
        "tags": ["ai", "investing"],
        "art": None,
        "code": "NP",
    },
    "Acquired": {
        "url": "https://feeds.transistor.fm/acquired",
        "tags": ["business", "tech"],
        "art": None,
        "code": "AQ",
    },
    "Hard Fork": {
        "url": "https://feeds.simplecast.com/l2i9YnTd",
        "tags": ["ai", "tech"],
        "art": None,
        "code": "HF",
    },
    "ChinaTalk": {
        "url": "https://api.substack.com/feed/podcast/283329.rss",
        "tags": ["geopolitics", "tech"],
        "art": None,
        "code": "CT",
    },
    "Macro Voices": {
        "url": "https://feed.podbean.com/macrovoices/feed.xml",
        "tags": ["markets", "macro"],
        "art": None,
        "code": "MV",
    },
    "Capital Allocators": {
        "url": "https://tedseides.libsyn.com/rss",
        "tags": ["investing"],
        "art": None,
        "code": "CA",
    },
    "GZERO World": {
        "url": "https://feeds.megaphone.fm/gzeroworld",
        "tags": ["geopolitics"],
        "art": None,
        "code": "GZ",
    },
}

# Interest keywords for scoring relevance
INTEREST_KEYWORDS = [
    "ai", "artificial intelligence", "machine learning", "llm", "gpt", "claude",
    "anthropic", "openai", "nvidia", "gpu", "compute",
    "market", "invest", "stock", "fund", "hedge", "macro", "fed", "rate",
    "geopolit", "china", "iran", "trade war", "taiwan", "nato",
    "iceland", "ísland",
    "founder", "startup", "venture", "ipo",
    "bitcoin", "crypto", "blockchain",
    "quantum", "robotics", "autonomous",
]


def clean_html(raw):
    """Strip HTML tags and decode entities."""
    clean = re.sub(r"<[^>]+>", "", raw or "")
    clean = html.unescape(clean)
    return clean.strip()


def truncate(text, max_len=280):
    """Truncate to max_len, ending at a sentence boundary if possible."""
    if len(text) <= max_len:
        return text
    truncated = text[:max_len]
    last_period = truncated.rfind(". ")
    if last_period > max_len // 2:
        return truncated[: last_period + 1]
    return truncated.rsplit(" ", 1)[0] + "…"


def score_episode(title, summary, tags):
    """Score episode relevance based on keywords."""
    text = (title + " " + summary).lower()
    score = sum(2 for kw in INTEREST_KEYWORDS if kw in text)
    if any(t in ["ai", "markets", "investing", "geopolitics"] for t in tags):
        score += 3
    return score


def fetch_recent_episodes(days_back=3):
    """Fetch episodes from all feeds published in the last N days."""
    cutoff = datetime.now(timezone.utc) - timedelta(days=days_back)
    episodes = []

    for name, feed_info in FEEDS.items():
        try:
            print(f"  Fetching {name}...")
            feed = feedparser.parse(feed_info["url"])
            count = 0
            for entry in feed.entries[:10]:
                pub = entry.get("published_parsed") or entry.get("updated_parsed")
                if not pub:
                    continue
                pub_dt = datetime(*pub[:6], tzinfo=timezone.utc)
                if pub_dt < cutoff:
                    continue

                title = clean_html(entry.get("title", ""))
                summary = clean_html(
                    entry.get("summary", "") or entry.get("description", "")
                )
                summary = truncate(summary, 350)

                # Try to get episode artwork, fall back to feed artwork
                art = feed_info["art"]
                if not art and hasattr(feed.feed, "image") and hasattr(feed.feed.image, "href"):
                    art = feed.feed.image.href
                # Check itunes image
                if not art:
                    itunes_img = feed.feed.get("itunes_image", {})
                    if isinstance(itunes_img, dict):
                        art = itunes_img.get("href")

                ep = {
                    "podcast": name,
                    "title": title,
                    "summary": summary,
                    "date": pub_dt.strftime("%Y-%m-%d"),
                    "date_display": pub_dt.strftime("%b %d, %Y"),
                    "tags": feed_info["tags"],
                    "art": art,
                    "code": feed_info["code"],
                    "score": score_episode(title, summary, feed_info["tags"]),
                }
                episodes.append(ep)
                count += 1
            print(f"    Found {count} recent episodes")
        except Exception as e:
            print(f"  Warning: failed to fetch {name}: {e}")

    # Sort by score descending
    episodes.sort(key=lambda e: -e["score"])
    return episodes


def make_search_url(platform, podcast, title):
    """Build a search URL for Spotify/YouTube/Google."""
    q = f"{podcast} {title}"
    if platform == "spotify":
        return f"https://open.spotify.com/search/{quote(q)}"
    elif platform == "youtube":
        return f"https://www.youtube.com/results?search_query={quote(q, safe='')}"
    else:
        return f"https://www.google.com/search?q={quote(q, safe='')}+transcript"


def esc(text):
    """HTML-escape text."""
    return html.escape(text, quote=True)


def generate_html(episodes, date_str, all_issues):
    """Generate the full briefing HTML."""
    top_picks = episodes[:3]
    total = len(episodes)

    # Determine themes for the lede
    tag_counts = {}
    for ep in episodes:
        for t in ep["tags"]:
            tag_counts[t] = tag_counts.get(t, 0) + 1
    top_tags = sorted(tag_counts, key=tag_counts.get, reverse=True)[:3]
    tag_labels = {
        "ai": "AI", "markets": "markets", "geopolitics": "geopolitics",
        "business": "business", "investing": "investing", "tech": "tech",
        "macro": "macro", "science": "science", "economics": "economics",
        "iceland": "Iceland",
    }
    theme_words = [tag_labels.get(t, t) for t in top_tags]
    if len(theme_words) > 1:
        lede = f"Today&#x27;s best episodes on {', '.join(theme_words[:-1])} and {theme_words[-1]}."
    else:
        lede = f"Today&#x27;s best episodes on {theme_words[0]}."

    # Date formatting
    parts = date_str.split("-")
    dt = datetime(int(parts[0]), int(parts[1]), int(parts[2]))
    day_full = dt.strftime("%A, %d %B %Y")

    # Build featured items
    featured_html = ""
    for ep in top_picks:
        spotify = make_search_url("spotify", ep["podcast"], ep["title"])
        featured_html += f'''<article class="featured-item">
  <div>
    <p class="featured-kicker">{esc(ep["podcast"])} &middot; {ep["date_display"]}</p>
    <h3>{esc(ep["title"])}</h3>
    <p>{esc(truncate(ep["summary"], 120))}</p>
  </div>
  <a class="btn primary" href="{esc(spotify)}" target="_blank" rel="noopener">Spotify</a>
</article>'''

    # Build episode cards
    cards_html = ""
    for i, ep in enumerate(episodes):
        is_top = i < 3
        spotify = make_search_url("spotify", ep["podcast"], ep["title"])
        youtube = make_search_url("youtube", ep["podcast"], ep["title"])
        transcript = make_search_url("google", ep["podcast"], ep["title"])

        if ep["art"]:
            cover = f'<img src="{esc(ep["art"])}" alt="{esc(ep["podcast"])} artwork" loading="lazy">'
        else:
            cover = f'<div class="cover-fallback">{esc(ep["code"])}</div>'

        tags_html = "".join(f"<span>{esc(t)}</span>" for t in ep["tags"])
        rating = "Must-read" if is_top else "Worth a look"
        card_class = "episode-card top-pick" if is_top else "episode-card"

        cards_html += f'''<article class="{card_class}">
  <div class="cover">{cover}</div>
  <div class="content">
    <div class="meta-row"><span class="podcast">{esc(ep["podcast"])}</span><span class="date">{ep["date_display"]}</span></div>
    <h3>{esc(ep["title"])}</h3>
    <p class="summary">{esc(ep["summary"])}</p>
    <div class="insight-row"><span class="rating">{rating}</span></div>
    <div class="tags">{tags_html}</div>
    <div class="actions">
      <a class="btn primary" href="{esc(spotify)}" target="_blank" rel="noopener">Spotify</a>
      <a class="btn subtle" href="{esc(youtube)}" target="_blank" rel="noopener">YouTube</a>
      <a class="btn subtle" href="{esc(transcript)}" target="_blank" rel="noopener">Transcript</a>
    </div>
  </div>
</article>'''

    # Archive sidebar
    archive_html = ""
    for issue in all_issues:
        fname = issue["path"].split("/")[-1]
        archive_html += f'            <li><a href="{fname}"><span>{issue["date"]}</span><span>{issue["count"]} picks</span></a></li>\n'

    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Villi Podcast Briefing — {date_str}</title>
  <meta name="description" content="Curated podcast briefing for Gunnar">
  <link rel="stylesheet" href="../assets/style.css">
</head>
<body>
  <div class="shell">
    <header class="hero">
      <div class="hero-copy">
        <p class="eyebrow">Villi Podcast Briefing</p>
        <h1>{day_full}</h1>
        <p class="lede">{lede}</p>
      </div>
      <div class="hero-stats panel">
        <div><span class="stat-number">{total}</span><span class="stat-label">episodes in this issue</span></div>
        <div><span class="stat-number">{min(3, total)}</span><span class="stat-label">top picks up front</span></div>
      </div>
    </header>

    <main class="layout">
      <section class="main-column">
        <section class="panel feature-panel">
          <div class="section-heading"><p class="section-kicker">Start here</p><h2>Top picks</h2></div>
          <div class="featured-stack">{featured_html}</div>
        </section>

        <section class="section-title"><div><p class="section-kicker">Full issue</p><h2>Everything worth a look</h2></div><p>{total} curated episodes</p></section>
        <section class="cards">{cards_html}</section>
      </section>

      <aside class="sidebar">
        <div class="panel sidebar-panel">
          <div class="section-heading"><p class="section-kicker">Browse</p><h2>Archive</h2></div>
          <ul class="archive-list">
{archive_html}          </ul>
        </div>
      </aside>
    </main>
    <footer class="footer">Maintained by Villi. Live on GitHub Pages.</footer>
  </div>
</body>
</html>'''


def main():
    repo_dir = os.environ.get("GITHUB_WORKSPACE", ".")
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    print(f"=== Villi Podcast Briefing Generator ===")
    print(f"Date: {today}")

    # Load existing briefings index
    index_path = Path(repo_dir) / "briefings.json"
    if index_path.exists():
        with open(index_path) as f:
            index_data = json.load(f)
    else:
        index_data = {"updated_at": "", "issues": []}

    # Skip if already published today
    if any(i["date"] == today for i in index_data.get("issues", [])):
        print(f"Already published for {today}, skipping.")
        return

    # Fetch episodes
    print(f"\nFetching RSS feeds...")
    episodes = fetch_recent_episodes(days_back=3)
    print(f"\nTotal episodes found: {len(episodes)}")

    if len(episodes) < 4:
        print(f"Only {len(episodes)} episodes found, need at least 4. Skipping.")
        return

    # Cap at 12
    episodes = episodes[:12]
    print(f"Selected top {len(episodes)} episodes for briefing.\n")

    # Update index
    new_issue = {"date": today, "count": len(episodes), "path": f"issues/{today}.html"}
    index_data["issues"].insert(0, new_issue)
    index_data["updated_at"] = datetime.now(timezone.utc).isoformat()

    # Generate HTML
    issue_html = generate_html(episodes, today, index_data["issues"])

    # Write issue file
    issues_dir = Path(repo_dir) / "issues"
    issues_dir.mkdir(exist_ok=True)
    issue_path = issues_dir / f"{today}.html"
    issue_path.write_text(issue_html, encoding="utf-8")
    print(f"Wrote {issue_path}")

    # Write index.html (root copy with fixed CSS path)
    index_html = issue_html.replace('href="../assets/style.css"', 'href="assets/style.css"')
    (Path(repo_dir) / "index.html").write_text(index_html, encoding="utf-8")
    print("Updated index.html")

    # Write briefings.json
    with open(index_path, "w") as f:
        json.dump(index_data, f, indent=2)
    print("Updated briefings.json")
    print(f"\nDone! Briefing ready for {today}.")


if __name__ == "__main__":
    main()
