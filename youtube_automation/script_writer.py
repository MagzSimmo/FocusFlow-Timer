"""Write a Booked Wild article/script using Claude, informed by a research pack."""

import json
import time

import anthropic

from . import config

_SYSTEM = f"""You are an expert B2B sales writer for '{config.CHANNEL_NAME}'.
You produce articles that are direct, practitioner-led, and immediately actionable.

Brand SOP and voice guide:
{config.BOOKED_WILD_SOP}

Article format rules:
- UK English throughout
- No filler phrases ("In this video...", "Today we're going to...")
- Short punchy sentences
- Question-based H2 headings (the reader's own question)
- Embedded citations where research supports a claim
- Strong CTA at the end (subscribe + specific next step)
- No fluff, no padding
"""

_RESPONSE_SCHEMA = """{
  "youtube_title": "string (max 70 chars, curiosity-driven)",
  "youtube_description": "string (150-200 words, includes timestamps, CTA, hashtags)",
  "tags": ["tag1", "tag2", ...],
  "article_markdown": "string (full article in markdown, 600-800 words)"
}"""


def write_script(topic: str, research_pack: str, api_key: str) -> dict:
    """
    Return a dict with keys: youtube_title, youtube_description, tags, article_markdown.
    article_markdown is in Booked Wild format: H1, question-based H2s, CTA, Sources.
    """
    user_prompt = (
        f"Write a Booked Wild YouTube video article on this topic:\n\n"
        f"**{topic}**\n\n"
        f"Research pack (incorporate these facts naturally with citations):\n"
        f"{research_pack}\n\n"
        f"Article structure:\n"
        f"# [Title]\n"
        f"## [Question H2 — hook/problem]\n"
        f"[Body — 80-120 words]\n"
        f"## [Question H2 — first insight]\n"
        f"[Body — 80-120 words]\n"
        f"## [Question H2 — second insight]\n"
        f"[Body — 80-120 words]\n"
        f"## [Question H2 — third insight / practical step]\n"
        f"[Body — 80-120 words]\n"
        f"## What should you do next?\n"
        f"[CTA — 40-60 words, include subscribe prompt and one concrete action]\n"
        f"## Sources\n"
        f"[List sources cited]\n\n"
        f"Respond with valid JSON matching this schema:\n{_RESPONSE_SCHEMA}"
    )

    client = anthropic.Anthropic(api_key=api_key)

    for attempt in range(3):
        try:
            response = client.messages.create(
                model=config.CLAUDE_SCRIPT_MODEL,
                max_tokens=2000,
                system=_SYSTEM,
                messages=[{"role": "user", "content": user_prompt}],
            )
            raw = response.content[0].text.strip()

            # Strip markdown code fences if Claude wraps the JSON
            if raw.startswith("```"):
                raw = raw.split("```")[1]
                if raw.startswith("json"):
                    raw = raw[4:]

            return json.loads(raw.strip())

        except json.JSONDecodeError as e:
            if attempt < 2:
                user_prompt += (
                    "\n\nYour previous response was not valid JSON. "
                    "Return ONLY the JSON object, no surrounding text."
                )
                time.sleep(3)
                continue
            raise ValueError(f"Claude returned invalid JSON after 3 attempts: {e}") from e

        except anthropic.APIConnectionError:
            if attempt == 2:
                raise
            time.sleep(5 * (2 ** attempt))

        except anthropic.RateLimitError:
            time.sleep(60)

    raise RuntimeError("Failed to generate script after 3 attempts")
