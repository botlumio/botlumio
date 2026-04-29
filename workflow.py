# ============================================================
# LUMIOBOT — Full System Workflow
# AI Knowledge Extraction Bot
# ============================================================
# Website  : https://lumiobot.fun
# Telegram : https://t.me/ailumio_bot
# GitHub   : https://github.com/botlumio/botlumio
# X        : https://x.com/Zhenya718
# Token    : Coming soon on https://kickstart.easya.io/
# ============================================================

WORKFLOW = {

    # ─────────────────────────────────────────────────────────
    # PRODUCT INFO
    # ─────────────────────────────────────────────────────────
    "product": {
        "name"         : "Lumiobot",
        "tagline"      : "AI Knowledge Extraction Bot",
        "description"  : "AI-powered Telegram bot that extracts pure knowledge from any YouTube video or web article.",
        "version"      : "1.0.0",
        "status"       : "live",
        "website"      : "https://lumiobot.fun",
        "telegram_bot" : "https://t.me/ailumio_bot",
        "github"       : "https://github.com/botlumio/botlumio",
        "twitter"      : "https://x.com/Zhenya718",
        "founder"      : "https://x.com/Zhenya718",
        "token_launch" : "https://kickstart.easya.io/",
    },

    # ─────────────────────────────────────────────────────────
    # STEP 1 — USER INPUT
    # ─────────────────────────────────────────────────────────
    "step_1_user_input": {
        "actor"      : "User",
        "channel"    : "Telegram (@ailumio_bot)",
        "action"     : "Sends a YouTube URL or article/web URL",
        "validations": [
            "Is it a valid URL?",
            "Is the domain reachable?",
            "Is the content type supported?",
        ],
        "on_invalid" : "Return error message with usage instructions",
    },

    # ─────────────────────────────────────────────────────────
    # STEP 2 — INPUT CLASSIFIER
    # ─────────────────────────────────────────────────────────
    "step_2_classifier": {
        "actor"          : "Input Classifier",
        "purpose"        : "Detect content type and route to correct extractor",
        "routes"         : {
            "youtube" : "YouTube Transcript API extractor",
            "article" : "Web scraper / article parser",
            "pdf"     : "PDF parser (coming soon — Q2 2026)",
            "audio"   : "Whisper AI transcriber (coming soon — Q3 2026)",
        },
        "on_unknown_type": "Return unsupported content message to user",
    },

    # ─────────────────────────────────────────────────────────
    # STEP 3 — CONTENT EXTRACTION
    # ─────────────────────────────────────────────────────────
    "step_3_extraction": {
        "actor"  : "Content Extractor",
        "routes" : {
            "youtube": {
                "tool"    : "YouTube Transcript API",
                "process" : "Fetch full transcript by video ID",
                "fallback": "Return error if transcript is disabled or video is private",
                "status"  : "live",
            },
            "article": {
                "tool"    : "Web scraper (BeautifulSoup / Playwright)",
                "process" : "Fetch HTML, strip ads/nav/footer, extract main body text",
                "fallback": "Return error if page is paywalled or unreachable",
                "status"  : "live",
            },
            "pdf": {
                "tool"    : "PDF parser (PyMuPDF / pdfplumber)",
                "process" : "Extract raw text from all PDF pages",
                "fallback": "Return error if PDF is scanned-only or password protected",
                "status"  : "coming soon — Q2 2026",
            },
            "audio": {
                "tool"    : "Whisper AI",
                "process" : "Transcribe audio file or podcast episode to text",
                "fallback": "Return error if file format unsupported or too large",
                "status"  : "coming soon — Q3 2026",
            },
        },
        "output": "Raw text content",
    },

    # ─────────────────────────────────────────────────────────
    # STEP 4 — CONTENT PROCESSING
    # ─────────────────────────────────────────────────────────
    "step_4_content_processing": {
        "actor" : "Content Processor",
        "steps" : [
            "Count tokens in raw text",
            "Chunk content if > 8,000 tokens",
            "Detect language",
            "Strip irrelevant boilerplate and noise",
            "Normalize whitespace and encoding",
        ],
        "output": "Clean, chunked text ready for AI pipeline",
    },

    # ─────────────────────────────────────────────────────────
    # STEP 5 — AI PIPELINE
    # ─────────────────────────────────────────────────────────
    "step_5_ai_pipeline": {
        "actor"  : "AI Pipeline",
        "model"  : "LLM (Claude / GPT-4)",
        "prompt" : "Structured knowledge extraction prompt",
        "schema" : {
            "title"         : "str   — title of the content",
            "read_time"     : "str   — estimated read time vs original duration",
            "summary"       : "str   — 3–5 sentence paragraph summary",
            "key_points"    : "list  — 3–7 bullet key insights",
            "main_takeaway" : "str   — single most important conclusion",
        },
        "output" : "Structured JSON object",
    },

    # ─────────────────────────────────────────────────────────
    # STEP 6 — OUTPUT FORMATTER
    # ─────────────────────────────────────────────────────────
    "step_6_output_formatter": {
        "actor"  : "Output Formatter",
        "builds" : [
            "TITLE        — content title",
            "READ TIME    — estimated vs original duration",
            "SUMMARY      — concise paragraph",
            "KEY POINTS   — bullet list of insights",
            "MAIN TAKEAWAY— single conclusion line",
        ],
        "format" : "Plain text formatted for Telegram (Markdown)",
        "output" : "Final Telegram message string",
    },

    # ─────────────────────────────────────────────────────────
    # STEP 7 — DELIVERY
    # ─────────────────────────────────────────────────────────
    "step_7_delivery": {
        "actor"   : "Telegram Bot",
        "action"  : "Send formatted message back to user",
        "extras"  : [
            "Log extraction event to database",
            "Increment user daily usage counter",
            "Check if user has exceeded free tier limit",
        ],
        "on_limit": "Prompt user to upgrade to Pro plan",
    },

    # ─────────────────────────────────────────────────────────
    # STEP 8 — USAGE CONTROL
    # ─────────────────────────────────────────────────────────
    "step_8_usage_control": {
        "actor": "Usage Manager",
        "tiers": {
            "free": {
                "price"   : "$0/mo",
                "limit"   : "10 extractions per day",
                "features": [
                    "YouTube videos",
                    "Web articles",
                    "Basic structured output",
                    "English only",
                ],
            },
            "pro": {
                "price"   : "$9/mo",
                "limit"   : "Unlimited extractions",
                "features": [
                    "YouTube videos",
                    "Web articles",
                    "PDF documents",
                    "Full structured output",
                    "Q&A mode on content",
                    "Priority processing",
                ],
            },
            "team": {
                "price"   : "$29/mo",
                "limit"   : "Unlimited — up to 10 users",
                "features": [
                    "Everything in Pro",
                    "Team knowledge base",
                    "Audio & podcast support",
                    "API access",
                    "Priority support",
                ],
            },
        },
    },

    # ─────────────────────────────────────────────────────────
    # STEP 9 — ERROR HANDLING
    # ─────────────────────────────────────────────────────────
    "step_9_error_handling": {
        "actor"  : "Error Handler",
        "errors" : {
            "invalid_url"         : "URL is malformed or unreachable",
            "unsupported_type"    : "Content type not yet supported",
            "transcript_disabled" : "YouTube video has no transcript available",
            "private_video"       : "YouTube video is private or unlisted",
            "paywall_detected"    : "Article is behind a paywall",
            "ai_timeout"          : "AI pipeline took too long to respond",
            "rate_limit_exceeded" : "User has exceeded daily free tier limit",
            "token_overflow"      : "Content too large — chunking applied automatically",
        },
        "strategy": "Return friendly Telegram message with reason and suggestion",
    },

    # ─────────────────────────────────────────────────────────
    # ROADMAP
    # ─────────────────────────────────────────────────────────
    "roadmap": {
        "march_2026"   : {"feature": "Public launch — YouTube & article extraction",     "status": "completed"},
        "april_2026"   : {"feature": "Pro & Team subscription tiers",                    "status": "in progress"},
        "may_2026"     : {"feature": "PDF document support",                             "status": "planned"},
        "june_2026"    : {"feature": "Interactive Q&A mode on extracted content",        "status": "planned"},
        "august_2026"  : {"feature": "Audio & podcast extraction via Whisper AI",        "status": "planned"},
        "october_2026" : {"feature": "Personal knowledge base — save & search extracts", "status": "planned"},
        "december_2026": {"feature": "Public API + integrations (Notion, Obsidian, Slack)", "status": "planned"},
    },

    # ─────────────────────────────────────────────────────────
    # TECH STACK
    # ─────────────────────────────────────────────────────────
    "tech_stack": {
        "bot_framework"    : "python-telegram-bot",
        "youtube"          : "youtube-transcript-api",
        "web_scraping"     : "BeautifulSoup4 / Playwright",
        "pdf_parsing"      : "PyMuPDF / pdfplumber (coming soon)",
        "audio_transcription": "OpenAI Whisper (coming soon)",
        "ai_model"         : "Claude / GPT-4",
        "database"         : "PostgreSQL / SQLite",
        "hosting"          : "VPS / Railway / Render",
        "language"         : "Python 3.11+",
    },

    # ─────────────────────────────────────────────────────────
    # TEAM
    # ─────────────────────────────────────────────────────────
    "team": {
        "Zhenya718"     : {"role": "Founder & Lead Dev",    "twitter": "https://x.com/Zhenya718"},
        "hiro_nakamura"  : {"role": "AI Engineer",           "location": "Tokyo, Japan"},
        "axel_lindqvist" : {"role": "Product & Design",      "location": "Stockholm, Sweden"},
        "yuki_tanaka"    : {"role": "Backend Engineer",      "location": "Osaka, Japan"},
    },

}


# ─────────────────────────────────────────────────────────────
# FLOW DIAGRAM (ASCII)
# ─────────────────────────────────────────────────────────────
FLOW_DIAGRAM = """
USER (Telegram)
    |
    | sends URL
    v
INPUT VALIDATOR
    |-- invalid URL ──> return error
    |
    v
INPUT CLASSIFIER
    |-- youtube  ──> YouTube Transcript API
    |-- article  ──> Web Scraper
    |-- pdf      ──> PDF Parser       (coming soon)
    |-- audio    ──> Whisper AI       (coming soon)
    |
    v
CONTENT PROCESSOR
    - token count
    - chunking
    - cleaning
    |
    v
AI PIPELINE (LLM)
    - structured prompt
    - JSON schema output
    |
    v
OUTPUT FORMATTER
    - title / read time / summary / key points / takeaway
    |
    v
TELEGRAM DELIVERY
    |
    v
USAGE MANAGER
    - log event
    - check tier limit
    - upsell if exceeded
"""


if __name__ == "__main__":
    import json
    print(json.dumps(WORKFLOW, indent=4))
    print(FLOW_DIAGRAM)
