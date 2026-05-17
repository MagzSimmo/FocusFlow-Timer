"""
Booked Wild YouTube Automation — Central Configuration

HOW TO USE:
- The SOP below is already populated from your workflow document.
- Flip UPLOAD_PRIVACY to "public" only when Colin approves.
- Add your own logo.png and font.ttf to youtube_automation/assets/
"""

# ── Channel Identity ──────────────────────────────────────────────────────────

CHANNEL_NAME = "Booked Wild"
CHANNEL_HANDLE = "@BookedWild"
CHANNEL_DESCRIPTION = (
    "Booked Wild helps independent hospitality operators win more direct bookings, "
    "reduce OTA dependency, and build a guest experience that keeps people coming back. "
    "Practical strategy for hotel owners, operators, and hospitality businesses. "
    "New video every day."
)
CHANNEL_KEYWORDS = [
    "direct bookings", "hotel marketing", "hospitality operator",
    "reduce OTA commission", "hotel revenue", "Booked Wild",
    "Deep Insight Audit", "independent hotel", "direct booking strategy",
    "hospitality marketing", "hotel direct", "OTA dependency"
]

# ── Upload Settings ───────────────────────────────────────────────────────────

UPLOAD_PRIVACY = "private"          # → "public" when Colin approves
VIDEO_CATEGORY_ID = "27"            # Education
VIDEO_LANGUAGE = "en"
BASE_TAGS = [
    "direct bookings", "hotel marketing", "hospitality operator",
    "reduce OTA", "hotel revenue", "Booked Wild", "Deep Insight Audit",
    "independent hotel", "direct booking strategy", "hospitality tips"
]

# ── Video Format ──────────────────────────────────────────────────────────────

VIDEO_RESOLUTION = (1920, 1080)
VIDEO_FPS = 24
THUMBNAIL_RESOLUTION = (1280, 720)

IMAGES_PER_VIDEO = 4                # Gemini Imagen calls per video (0 = Pillow-only, free)

BACKGROUND_COLOR = (15, 20, 35)     # deep navy
ACCENT_COLOR = (255, 107, 53)       # Booked Wild orange
TEXT_COLOR = (255, 255, 255)

FONT_PATH = "youtube_automation/assets/font.ttf"
FONT_SIZE_TITLE = 80
FONT_SIZE_HEADING = 64
FONT_SIZE_BODY = 46
FONT_SIZE_CITATION = 28
TEXT_PADDING = 100

# ── AI Models ─────────────────────────────────────────────────────────────────

CLAUDE_TOPIC_MODEL = "claude-haiku-4-5"
CLAUDE_SCRIPT_MODEL = "claude-sonnet-4-6"
GEMINI_RESEARCH_MODEL = "gemini-1.5-flash"
GEMINI_IMAGE_MODEL = "imagen-3.0-generate-002"

# ── Deep Insight Audit CTA ────────────────────────────────────────────────────

AUDIT_CTA_URL = "https://www.bookedwild.com/audit/deep-insight"
AUDIT_CTA_TEXT = (
    "If you want to understand exactly where your property is losing direct bookings, "
    "start with a Deep Insight Audit. "
    f"Find out more at {AUDIT_CTA_URL}"
)

# ── Topic Seeds (hospitality / direct bookings) ───────────────────────────────

TOPIC_SEEDS = [
    "why independent hotels pay too much OTA commission and what to do about it",
    "how to convert lookers into direct bookers on your hotel website",
    "the real cost of relying on Booking.com and Expedia",
    "how to build a direct booking offer guests can't get on OTAs",
    "what the Deep Insight Audit reveals about your booking funnel",
    "why most hotel websites lose bookings before the guest even checks availability",
    "how to use email to turn past guests into repeat direct bookers",
    "the difference between a hotel that grows and one that just survives",
    "how to audit your own property for direct booking gaps",
    "what hospitality operators get wrong about their OTA listing",
    "how to write a hotel offer that actually converts",
    "the hidden cost of a poorly positioned hotel brand",
    "how guest experience drives direct booking loyalty",
    "why your best guests are booking through OTAs and how to change that",
    "how to build a rate strategy that protects your direct channel",
    "what a high-converting hotel booking page actually looks like",
    "how to make your hospitality offer clear, specific, and compelling",
    "the most common audit findings in hotel direct booking strategies",
    "how to reduce cancellations on direct bookings",
    "why hospitality operators need a direct booking strategy before a marketing strategy",
    "how to use Google to drive direct bookings without a big budget",
    "what data your hotel should be tracking every month",
    "how to build guest trust that makes OTAs irrelevant",
    "the case for owning your guest relationship end to end",
    "how operators grow revenue without adding more rooms",
]

# ── Booked Wild SOP ───────────────────────────────────────────────────────────

BOOKED_WILD_SOP = """
BOOKED WILD — BRAND AND CONTENT STANDARDS

AUDIENCE
Independent hospitality operators: hotel owners, B&B and guesthouse operators, boutique
venues, and hospitality businesses seeking to reduce OTA dependency and grow direct bookings.
They are experienced operators, not marketers. They are sceptical of hype and want
practical, evidence-based guidance.

COMMERCIAL FOCUS
Booked Wild's primary offer is the Deep Insight Audit — a structured review of a
hospitality operator's direct booking performance, positioning, and funnel.
Every article should support the case for the audit or a related Booked Wild service.
CTA URL: https://www.bookedwild.com/audit/deep-insight

TONE
- UK English throughout (spelling, idiom, punctuation)
- Direct and practitioner-led — written as if by someone who has worked in hospitality
- No marketing waffle, no fluff, no filler
- Short sentences. Paragraphs of 2–3 sentences maximum.
- Confident but not arrogant
- Evidence-based — claims must be supported by citations or acknowledged as general practice
- Never condescending; the reader is a professional

ARTICLE STRUCTURE
1. meta title (50–60 characters, search-optimised)
2. meta description (140–155 characters, includes a search-relevant phrase)
3. slug (lowercase, hyphenated)
4. H1 (matches or closely echoes meta title)
5. Question-based H2s (the operator's own question — practical, specific)
6. Direct-answer opening sentence for each H2 section
7. Body (evidence-backed, short paragraphs)
8. Embedded citations (appear beside the claim they support)
9. CTA section — Deep Insight Audit
10. Sources list

BANNED CONTENT
- Invented or uncited statistics
- Phrases like "significantly increase bookings", "dramatically boost revenue",
  "guaranteed results", "proven to increase conversions", "top-ranked"
- Ranking or revenue guarantees of any kind
- Generic SEO advice not specific to hospitality
- Thin claims without evidence
- AI-sounding filler ("In today's competitive landscape...", "It's no secret that...")
- Passive voice where active is possible

SOURCE QUALITY RULES
Accept:
- Official research (STR, CBRE, Phocuswire, Skift, TravelClick)
- Hospitality / travel trade publications
- Operator case studies with named sources
- Academic or industry research papers
- Booked Wild's own audit findings (framed as internal data)

Reject:
- Weak listicles and thin marketing blogs
- Unsupported SEO claims
- Generic AI-generated content used as a source
- Social media posts without primary source

QC STANDARDS (score each out of 10)
- No invented statistics: all stats are cited
- No unsupported performance claims
- No ranking/revenue/booking guarantees
- Citations appear beside the claims they support
- Source quality meets the above standard
- CTA is correct and links to the audit page
- Tone matches Booked Wild — UK English, direct, practitioner-led
- Markdown is clean (no broken formatting, no double spaces)
- Article does not duplicate existing Booked Wild website content
- Article supports the Deep Insight Audit commercial priority
"""

# ── File Paths ────────────────────────────────────────────────────────────────

UPLOAD_LOG_PATH = "youtube_automation/logs/upload_log.json"
ASSETS_DIR = "youtube_automation/assets"
LOGO_PATH = "youtube_automation/assets/logo.png"
