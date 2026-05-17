"""
Booked Wild YouTube Automation — Central Configuration

Fill in BOOKED_WILD_SOP with your full Standard Operating Procedure before running.
Flip UPLOAD_PRIVACY to "public" when Colin approves publishing.
"""

# ── Channel Identity ──────────────────────────────────────────────────────────

CHANNEL_NAME = "Booked Wild"
CHANNEL_HANDLE = "@BookedWild"
CHANNEL_DESCRIPTION = (
    "Booked Wild delivers daily B2B sales tactics for founders and sales reps "
    "who want to fill their pipeline with cold outreach, nail their ICP, and "
    "convert conversations into revenue. New video every day."
)
CHANNEL_KEYWORDS = [
    "B2B sales", "cold outreach", "lead generation", "ICP",
    "value proposition", "sales prospecting", "Booked Wild",
    "B2B marketing", "sales tips", "cold email"
]

# ── Upload Settings ───────────────────────────────────────────────────────────

UPLOAD_PRIVACY = "private"          # → "public" when Colin approves
VIDEO_CATEGORY_ID = "27"            # Education
VIDEO_LANGUAGE = "en"
BASE_TAGS = [
    "B2B sales", "cold outreach", "lead generation", "ICP",
    "value proposition", "Booked Wild", "sales tips", "cold email",
    "B2B marketing", "sales prospecting"
]

# ── Video Format ──────────────────────────────────────────────────────────────

VIDEO_RESOLUTION = (1920, 1080)
VIDEO_FPS = 24
THUMBNAIL_RESOLUTION = (1280, 720)

IMAGES_PER_VIDEO = 4                # Gemini Imagen calls per video (set 0 = Pillow-only, free)

# Background colour used when Gemini images are disabled
BACKGROUND_COLOR = (15, 20, 35)     # deep navy
ACCENT_COLOR = (255, 107, 53)       # Booked Wild orange #FF6B35
TEXT_COLOR = (255, 255, 255)

FONT_PATH = "youtube_automation/assets/font.ttf"
FONT_SIZE_TITLE = 80
FONT_SIZE_HEADING = 64
FONT_SIZE_BODY = 46
FONT_SIZE_CITATION = 28
TEXT_PADDING = 100

# ── AI Models ─────────────────────────────────────────────────────────────────

CLAUDE_TOPIC_MODEL = "claude-haiku-4-5"          # cheapest, just picks a topic
CLAUDE_SCRIPT_MODEL = "claude-sonnet-4-6"         # quality script writing
GEMINI_RESEARCH_MODEL = "gemini-1.5-flash"        # search grounding
GEMINI_IMAGE_MODEL = "imagen-3.0-generate-002"    # slide background images

# ── Content Seeds ─────────────────────────────────────────────────────────────

TOPIC_SEEDS = [
    "cold email subject lines that actually get replies",
    "how to define your ICP in 30 minutes",
    "pain points vs. triggers: what B2B buyers really respond to",
    "value proposition frameworks for SaaS and service businesses",
    "multi-touch cold outreach sequences that convert",
    "LinkedIn DM strategies for B2B prospecting",
    "why most cold emails fail (and how to fix yours)",
    "how to research a prospect before reaching out",
    "objection handling in cold outreach",
    "how to write a follow-up email that doesn't annoy",
    "building a lead list that actually converts",
    "personalisation at scale in cold email campaigns",
    "call-to-action formulas that book more meetings",
    "how to nail the first line of a cold email",
    "the psychology behind B2B buying decisions",
    "how to position your offer for a cold audience",
    "outreach metrics every sales rep should track",
    "the difference between a prospect and a lead",
    "how to identify decision-makers in a target company",
    "subject line A/B testing for cold outreach",
    "why your reply rate is low and what to do about it",
    "how to use case studies in cold outreach",
    "building credibility with a cold prospect",
    "how often to follow up without burning bridges",
    "turning a cold reply into a booked call",
]

# ── Booked Wild SOP ───────────────────────────────────────────────────────────
# Paste your full Standard Operating Procedure here.
# Claude uses this as the voice and methodology guide for every script.

BOOKED_WILD_SOP = """
[PASTE YOUR BOOKED WILD SOP HERE]

Include:
- Your ICP definition framework
- Cold outreach methodology and principles
- Tone guide (UK English, direct, practitioner-led)
- Banned words / phrases
- CTA template
- Article structure conventions
- Any brand voice rules

Until this is filled in, Claude will default to a professional UK English
B2B sales educator tone.
"""

# ── File Paths ────────────────────────────────────────────────────────────────

UPLOAD_LOG_PATH = "youtube_automation/logs/upload_log.json"
ASSETS_DIR = "youtube_automation/assets"
LOGO_PATH = "youtube_automation/assets/logo.png"
