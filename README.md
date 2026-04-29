# 🔆 LUMIOBOT

> **Extract pure knowledge from any YouTube video or article — in seconds.**

![Status](https://img.shields.io/badge/STATUS-LIVE-c8ff00?style=flat-square&labelColor=080808)
![Platform](https://img.shields.io/badge/PLATFORM-TELEGRAM-c8ff00?style=flat-square&labelColor=080808)
![License](https://img.shields.io/badge/LICENSE-MIT-c8ff00?style=flat-square&labelColor=080808)
![Version](https://img.shields.io/badge/VERSION-1.0.0-c8ff00?style=flat-square&labelColor=080808)

---

## WHAT IS LUMIOBOT?

Lumiobot is an AI-powered Telegram bot that transforms any YouTube video or article URL into a clean, structured knowledge summary — in under 10 seconds.

Stop watching 47-minute videos to find 3 key insights. Send the link. Get the knowledge. Done.

```
$ lumio extract https://youtube.com/watch?v=...
✓ Transcript fetched · 18,200 tokens
✓ AI analysis complete · 4.2 sec
→ 5 key insights extracted — ready.
```

---

## LIVE DEMO

👉 **[t.me/ailumio_bot](https://t.me/ailumio_bot)** — Try it free on Telegram  
🌐 **[lumiobot.fun](https://lumiobot.fun)** — Official website

---

## FEATURES

| Feature | Status |
|---|---|
| YouTube video extraction | ✅ LIVE |
| Web article extraction | ✅ LIVE |
| Structured output (title, summary, key points, takeaway) | ✅ LIVE |
| PDF document extraction | 🔜 Coming May 2026 |
| Interactive Q&A on content | 🔜 Coming June 2026 |
| Audio & podcast transcription | 🔜 Coming August 2026 |
| Personal knowledge base | 🔜 Coming October 2026 |
| Public API | 🔜 Coming December 2026 |

---

## $LUMIO TOKEN

🚀 **Coming soon on [kickstart.easya.io](https://kickstart.easya.io/)**

Stay tuned for the official $LUMIO token launch. More details to be announced.

---

## OUTPUT FORMAT

Every extraction returns a clean, structured response:

```
🔆 LUMIOBOT — Knowledge Extract

📌 Title: [Title of the content]
⏱ Est. read time: [X min read]

📝 SUMMARY
[2-3 paragraph summary]

💡 KEY POINTS
▶ Point 1
▶ Point 2
▶ Point 3
▶ Point 4
▶ Point 5

🎯 MAIN TAKEAWAY
[The single most important insight]

🔗 Source: [original link]
─────────────────────
🔆 Knowledge extracted by Lumiobot · lumiobot.fun
```

---

## TECH STACK

```
Bot Framework     →  python-telegram-bot
Transcript API    →  youtube-transcript-api
Web Extraction    →  Jina AI Reader
AI Processing     →  Claude API (Anthropic)
Automation        →  n8n
Hosting           →  Railway / VPS
```

---

## QUICK START

### 1. Clone the repo
```bash
git clone https://github.com/botlumio/botlumio.git
cd botlumio
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set environment variables
```bash
cp .env.example .env
```

Edit `.env`:
```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
ANTHROPIC_API_KEY=your_anthropic_api_key
JINA_API_KEY=your_jina_api_key
```

### 4. Run the bot
```bash
python bot.py
```

---

## ENVIRONMENT VARIABLES

| Variable | Required | Description |
|---|---|---|
| `TELEGRAM_BOT_TOKEN` | ✅ | From [@BotFather](https://t.me/BotFather) |
| `ANTHROPIC_API_KEY` | ✅ | From [console.anthropic.com](https://console.anthropic.com) |
| `JINA_API_KEY` | ✅ | From [jina.ai](https://jina.ai) |
| `MAX_DAILY_FREE` | ❌ | Free tier daily limit (default: 10) |
| `LOG_LEVEL` | ❌ | Logging level (default: INFO) |

---

## PROJECT STRUCTURE

```
botlumio/
├── bot.py              # Main bot entry point
├── handlers/
│   ├── youtube.py      # YouTube extraction handler
│   ├── article.py      # Web article handler
│   └── commands.py     # Telegram commands (/start, /help)
├── ai/
│   ├── extractor.py    # AI extraction pipeline
│   └── formatter.py    # Output formatter
├── utils/
│   ├── transcript.py   # YouTube transcript fetcher
│   └── scraper.py      # Web content scraper
├── requirements.txt
├── .env.example
└── README.md
```

---

## ROADMAP 2026

```
✅ MARCH 2026          Public launch — YouTube & article extraction live
🚀 APRIL 29, 2026      $LUMIO TOKEN LAUNCH — live today on kickstart.easya.io
🔄 APRIL 2026          Pro & Team subscription tiers
○  MAY 2026            PDF & document support
○  JUNE 2026           Interactive Q&A mode
○  AUGUST 2026         Audio & podcast extraction
○  OCTOBER 2026        Personal knowledge base
○  DECEMBER 2026       Public API & integrations
```

---

## PRICING

| Plan | Price | Extractions |
|---|---|---|
| Free | $0/mo | 10/day |
| Pro | $9/mo | Unlimited |
| Team | $29/mo | Unlimited (10 users) |

---

## THE TEAM

| Name | Role | Location |
|---|---|---|
| [@Zhenya718](https://x.com/Zhenya718) | Founder & Lead Dev | — |
| Hiro Nakamura | AI Engineer | Tokyo, Japan 🇯🇵 |
| Axel Lindqvist | Product & Design | Stockholm, Sweden 🇸🇪 |
| Yuki Tanaka | Backend Engineer | Osaka, Japan 🇯🇵 |

> The team listing (apart from the founder) is currently a placeholder while we
> finalize public profiles for the rest of the crew.

---

## CONTRIBUTING

Contributions are welcome — please read [CONTRIBUTING.md](./CONTRIBUTING.md)
and our [Code of Conduct](./CODE_OF_CONDUCT.md) before opening a PR.

```bash
# Fork the repo
# Create your feature branch
git checkout -b feature/your-feature

# Commit your changes
git commit -m 'feat: add your feature'

# Push and open a PR
git push origin feature/your-feature
```

---

## SECURITY

We take security seriously. **Do not** open public issues for vulnerabilities.

- Read the full [Security Policy](./SECURITY.md)
- Report privately via [GitHub Security Advisories](https://github.com/botlumio/botlumio/security/advisories/new)
- Or DM the founder on X: [@Zhenya718](https://x.com/Zhenya718)

This repository is hardened with:

- 🔐 **CodeQL** static analysis on every push/PR ([workflow](./.github/workflows/codeql.yml))
- 🕵️ **Gitleaks** secret scanning ([workflow](./.github/workflows/secret-scan.yml))
- 🤖 **Dependabot** weekly dependency & GitHub Actions updates ([config](./.github/dependabot.yml))
- 📝 Issue, PR, and security templates under [`.github/`](./.github)

---

## LINKS

| | |
|---|---|
| 🤖 Telegram Bot | [t.me/ailumio_bot](https://t.me/ailumio_bot) |
| 🌐 Website | [lumiobot.fun](https://lumiobot.fun) |
| 𝕏 Official X | [@Zhenya718](https://x.com/Zhenya718) |
| 👤 Founder X | [@Zhenya718](https://x.com/Zhenya718) |
| 🚀 Token Launch | [kickstart.easya.io](https://kickstart.easya.io/) — Coming soon |
| 🔐 Security | [SECURITY.md](./SECURITY.md) |

---

## LICENSE

MIT © 2026 Lumiobot — [lumiobot.fun](https://lumiobot.fun)

---

<div align="center">

**🔆 FROM ANY LINK TO PURE KNOWLEDGE — IN SECONDS.**

[lumiobot.fun](https://lumiobot.fun) · [@Zhenya718](https://x.com/Zhenya718) · [t.me/ailumio_bot](https://t.me/ailumio_bot)

</div>
