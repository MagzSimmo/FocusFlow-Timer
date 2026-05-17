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
    "Booked Wild helps independent travel businesses get found by AI, book guests direct, "
    "and stop losing margin and customer data to OTAs. "
    "Practical strategy for hotels, guesthouses, tour operators, boutique venues, "
    "and independent travel operators who want to own their bookings. "
    "New video every day."
)
CHANNEL_KEYWORDS = [
    "direct bookings", "independent travel business", "OTA dependency",
    "AI visibility", "hotel marketing", "tour operator marketing",
    "Booked Wild", "Deep Insight Audit", "direct booking strategy",
    "reduce OTA commission", "travel business marketing", "get found by AI"
]

# ── Upload Settings ───────────────────────────────────────────────────────────

UPLOAD_PRIVACY = "private"          # → "public" when Colin approves
VIDEO_CATEGORY_ID = "27"            # Education
VIDEO_LANGUAGE = "en"
BASE_TAGS = [
    "direct bookings", "OTA dependency", "independent travel business",
    "AI visibility", "hotel marketing", "tour operator", "Booked Wild",
    "Deep Insight Audit", "direct booking strategy", "travel business"
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
    # OTA dependency and commission pain
    "why independent travel businesses are being taxed twice by invisibility and commission",
    "the real cost of OTA commission that most operators never calculate",
    "how to stop renting demand and start owning your bookings",
    "what you lose when a guest books through an OTA instead of direct",
    "why your best guests are booking through Booking.com and how to stop it",
    "the margin leak every independent operator needs to fix first",
    "how to build a direct booking offer OTAs cannot compete with",

    # AI visibility
    "why AI search is changing how travellers find independent properties",
    "how to get your travel business cited by ChatGPT and Google AI",
    "what AI visibility means for independent tour operators and hotels",
    "why travellers trust AI recommendations over OTA listings",
    "how to make your property findable by AI before your competitors do",
    "the difference between ranking on Google and being cited by AI",
    "why most independent travel websites are invisible to AI search",

    # Direct booking ownership and website conversion
    "how to convert website visitors into direct bookings without a big budget",
    "why most travel business websites lose bookings before the guest books",
    "what a high-converting direct booking page actually looks like",
    "how to build a rate strategy that protects your direct channel",
    "how to use email to turn past guests into repeat direct bookers",
    "the data every independent operator should be tracking each month",
    "how to reduce OTA dependency without killing your occupancy",

    # Deep Insight Audit and Booked Wild method
    "what a Deep Insight Audit reveals about your direct booking funnel",
    "the most common direct booking gaps found in independent travel businesses",
    "how to audit your own business for AI visibility and direct booking gaps",
    "why fixing your booking funnel beats spending more on marketing",
    "how independent operators grow revenue without adding more capacity",
]

# ── Booked Wild SOP ───────────────────────────────────────────────────────────

BOOKED_WILD_SOP = """
BOOKED WILD — BRAND AND CONTENT STANDARDS
(Source of truth: company docs provided by Colin. Update when full MD files are loaded.)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CORE POSITIONING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Primary positioning:
Booked Wild helps independent travel businesses get found by AI, book guests direct,
and stop losing margin and customer data to OTAs.

Secondary (sharpest version):
Independent travel businesses are being taxed twice: first by invisibility, then by
commission. Booked Wild fixes both.

Alternative sharp version:
Booked Wild helps independent travel operators stop renting demand, get cited by AI,
and turn more travellers into direct bookings they actually own.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AUDIENCE — ICPs
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Primary ICP: Independent travel business owners and operators.
Includes: hotel owners, guesthouse/B&B operators, boutique property owners,
independent tour operators, activity and experience providers, boutique venues.

They are NOT: large hotel chains, OTAs, travel agencies, or corporate travel buyers.

Operator profile:
- Running an independent or small-group travel/hospitality business
- Frustrated by OTA commission eating margin (typically 15–25%)
- Losing customer data and repeat bookings to OTA intermediaries
- Struggling with AI/search visibility — not being found the way guests now search
- May have a website that doesn't convert well
- Experienced operators, not marketers — sceptical of hype, want practical guidance
- Want to own their guest relationship end to end

Main commercial pains:
1. OTA dependency — paying commission on bookings they should own
2. AI/search invisibility — not being found when travellers use AI to plan trips
3. Direct booking conversion — website visitors not booking direct
4. Customer data loss — guest data stays with the OTA, not the operator
5. Margin erosion — commission + weak positioning = shrinking returns
6. Renting demand — relying on OTA traffic rather than building owned demand

Buying triggers:
- Commission costs are rising or feeling unsustainable
- A guest asked how they found them and it was via an OTA
- They've noticed AI tools recommending competitors but not them
- Their direct booking share is falling or stagnant
- They're ready to invest in their own channel but don't know where to start

Fears:
- Spending on marketing that doesn't convert
- Losing visibility entirely if they reduce OTA presence
- Being left behind as AI changes how guests search and book
- Not knowing where the leaks in their funnel actually are

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
COMMERCIAL FOCUS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Primary offer: Deep Insight Audit
A structured review of an independent travel business's direct booking performance,
AI/search visibility, positioning, and funnel.
CTA URL: https://www.bookedwild.com/audit/deep-insight

Every article and video should support one or more of these commercial priorities:
- The case for a Deep Insight Audit
- OTA dependency as a solvable problem
- AI visibility as a competitive advantage
- Direct booking ownership as the goal
- Booked Wild's method as the path

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TONE AND VOICE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- UK English throughout (spelling, idiom, punctuation — not US English)
- Direct and practitioner-led — written for experienced operators, not beginners
- No marketing waffle, no filler, no hype
- Short sentences. Paragraphs of 2–3 sentences maximum.
- Confident but never arrogant
- Evidence-backed — every claim is cited or framed as general practice
- Never condescending — the reader runs a real business

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTICLE STRUCTURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. meta title (50–60 characters, search-optimised)
2. meta description (140–155 characters, search-relevant phrase included)
3. slug (lowercase, hyphenated)
4. H1 (matches or closely echoes meta title)
5. Question-based H2s (the operator's own question — specific, practical)
6. Direct-answer opening sentence for each section
7. Body (evidence-backed, short paragraphs, 80–120 words per section)
8. Inline citations beside each supported claim
9. Deep Insight Audit CTA: https://www.bookedwild.com/audit/deep-insight
10. Sources list
11. Note for Colin (not for publication — QC summary and score)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BANNED CONTENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Never write:
- Invented or uncited statistics
- "Significantly increase bookings / revenue / conversions"
- "Dramatically boost", "guaranteed results", "proven to increase", "top-ranked"
- Revenue, ranking, or booking guarantees of any kind
- Vague SEO advice not specific to travel/hospitality
- AI-sounding filler ("In today's competitive landscape...", "It's no secret that...")
- Passive voice where active is possible
- US English spelling

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SOURCE QUALITY RULES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Accept:
- Official research: STR, Phocuswire, Skift, CBRE, TravelClick, Siteminder, AirDNA
- Hospitality and travel trade publications
- Named operator case studies
- Academic or industry research papers
- Booked Wild's own audit findings (framed as internal data)

Reject:
- Weak listicles and thin marketing blogs
- Unsupported SEO claims
- Generic AI-generated content used as a source
- Social media posts without a named primary source

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QC STANDARDS (score out of 10)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Pass / fail checks:
✓ No invented statistics — all stats cited inline
✓ No unsupported performance claims
✓ No ranking / revenue / booking guarantees
✓ Citations appear beside the claims they support
✓ Sources meet quality standard above
✓ CTA links to https://www.bookedwild.com/audit/deep-insight
✓ UK English throughout
✓ Tone is direct, practitioner-led, no filler
✓ Markdown is clean
✓ Article does not duplicate existing Booked Wild website content
✓ Article supports at least one commercial priority

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT IS STILL MISSING — LOAD THESE FILES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The following Booked Wild source-of-truth MD files have not yet been loaded.
Upload them to update this config with full accuracy:

  Brand Identity.md
  Tours and Products.md
  Ideal Customer.md          ← most important for ICP accuracy
  FAQs and Responses.md
  Voice and Messaging.md
  Brand Context.md
  Brand Voice Guide.md
  Content Standards.md
  Product Offerings.md

Until these are loaded, the ICP, tone, and product details above are based on
positioning notes from the Priority 1 audit doc and Draft-Friday one-pager.
"""

# ── File Paths ────────────────────────────────────────────────────────────────

UPLOAD_LOG_PATH = "youtube_automation/logs/upload_log.json"
ASSETS_DIR = "youtube_automation/assets"
LOGO_PATH = "youtube_automation/assets/logo.png"
