"""Write a Booked Wild article/script using Claude, following the full SOP workflow."""

import json
import time

import anthropic

from . import config

_SYSTEM = f"""You are the Booked Wild article agent. You write content for independent
hospitality operators — hotel owners, guesthouse operators, boutique venues — who want
to reduce OTA dependency and grow direct bookings.

You follow the Booked Wild brand and content standards exactly:

{config.BOOKED_WILD_SOP}

You never invent statistics. Every claim is either cited or explicitly framed as
general practice. You write in UK English. You do not use filler phrases.
Your articles support the Deep Insight Audit at {config.AUDIT_CTA_URL}
"""

_RESPONSE_SCHEMA = """{
  "meta_title": "string (50-60 chars, search-optimised)",
  "meta_description": "string (140-155 chars, includes a search-relevant phrase)",
  "slug": "string (lowercase, hyphenated, e.g. direct-booking-strategy-hotels)",
  "youtube_title": "string (max 70 chars, curiosity-driven, suitable for YouTube)",
  "youtube_description": "string (150-200 words for YouTube — includes H2 topics, CTA URL, hashtags)",
  "tags": ["hospitality", "direct bookings", "...up to 10 tags"],
  "article_markdown": "string (full article — see structure below)",
  "qc_score": "integer 1-10",
  "qc_notes": "string (note for Colin — what passed, what to check, any soft claims)"
}

article_markdown structure:
# H1 Title
## Question H2 — opening problem or hook
[direct-answer opening sentence. Body 80–120 words. Citation beside any stat.]
## Question H2 — first insight
[direct-answer opening sentence. Body 80–120 words.]
## Question H2 — second insight
[direct-answer opening sentence. Body 80–120 words.]
## Question H2 — practical step or operator action
[direct-answer opening sentence. Body 80–120 words.]
## Ready to find your direct booking gaps?
[Deep Insight Audit CTA — 40–60 words. Include URL: """ + config.AUDIT_CTA_URL + """]
## Sources
- [Source 1]
- [Source 2]
---
*Note for Colin — not for publication*
[Brief QC summary: what claims are cited, any areas to check, QC score rationale]"""


def write_script(topic: str, research_pack: str, api_key: str) -> dict:
    """
    Return a dict matching the schema above.
    article_markdown follows the full Booked Wild SOP article format.
    qc_notes contains the agent's self-assessment for Colin's review.
    """
    user_prompt = (
        f"Write a Booked Wild article and YouTube video script on this topic:\n\n"
        f"**{topic}**\n\n"
        f"Research pack — incorporate these facts naturally with inline citations:\n"
        f"{research_pack}\n\n"
        f"Requirements:\n"
        f"- Follow the Booked Wild SOP exactly (UK English, direct tone, no filler)\n"
        f"- Question-based H2s — the operator's own question\n"
        f"- Direct-answer opening sentence for each section\n"
        f"- Cite every stat inline, beside the claim\n"
        f"- No invented statistics. No revenue/ranking/booking guarantees.\n"
        f"- CTA must link to: {config.AUDIT_CTA_URL}\n"
        f"- Sources must meet Booked Wild source quality rules\n"
        f"- Self-QC: score the article out of 10 and leave a note for Colin\n\n"
        f"Respond with valid JSON matching this schema:\n{_RESPONSE_SCHEMA}"
    )

    client = anthropic.Anthropic(api_key=api_key)

    for attempt in range(3):
        try:
            response = client.messages.create(
                model=config.CLAUDE_SCRIPT_MODEL,
                max_tokens=2500,
                system=_SYSTEM,
                messages=[{"role": "user", "content": user_prompt}],
            )
            raw = response.content[0].text.strip()

            if raw.startswith("```"):
                raw = raw.split("```")[1]
                if raw.startswith("json"):
                    raw = raw[4:]

            result = json.loads(raw.strip())

            # Log QC score so it's visible in GitHub Actions output
            qc_score = result.get("qc_score", "?")
            qc_notes = result.get("qc_notes", "")
            print(f"[script_writer] QC score: {qc_score}/10")
            if qc_score and int(qc_score) < 7:
                print(f"[script_writer] WARNING — low QC score. Notes: {qc_notes}")

            return result

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
