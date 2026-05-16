---
name: booked-wild-article-producer
description: create, research, draft, qc, and finalise booked wild journal articles from colin's article subjects, briefs, or rough notes. use when producing travel/hospitality articles for booked wild, especially articles requiring notebooklm-style research packs, source discipline, public citations, source-variety checks, claude drafting prompts, chatgpt qc, colin-ready review notes, website-ready formatting, deep insight audit ctas, or design asset briefs.
---

# Booked Wild Article Producer

Use this skill to produce Booked Wild journal articles from a subject, brief, rough notes, or a NotebookLM research pack.

The goal is to create Colin-ready website articles quickly while preserving Booked Wild voice, source discipline, commercial positioning, and publication quality.

## Core outcome

Produce a polished Booked Wild article that:

- speaks to independent travel and hospitality operators
- uses Booked Wild's direct, commercial, anti-fluff voice
- treats Colin's subject as editorial direction, not verified evidence
- uses credible public sources with embedded links
- avoids unsupported statistics and overclaims
- includes metadata, H1, clear H2s, practical examples, CTA, and optional design asset brief
- can be sent to Colin or published after final checks

## Default CTA

Use this CTA unless the user gives a different confirmed URL:

`https://www.bookedwild.com/audit/deep-insight`

Default CTA wording:

`Book your £97 Deep Insight Audit: https://www.bookedwild.com/audit/deep-insight`

## Required inputs

At minimum, expect one of:

- article subject
- Colin's notes
- NotebookLM research pack
- draft article from Claude
- final article needing QC

If only the article subject is supplied, begin with the research workflow.

## Booked Wild source-of-truth files

When building a NotebookLM source set or internal context, use these as core brand/source files:

- `Brand_Context.md`
- `Brand_Voice_Guide.md`
- `Content_Standards.md`
- `Product_Offerings.md`

Do not use the old Tone of Voice document unless the user specifically asks for legacy tone comparison.

## Article workflow

### 1. Intake Colin's subject

When the user provides a new article subject or rough brief, create a NotebookLM copied-text source block.

The block must include:

- article subject
- Colin's notes
- warning that Colin's notes are editorial direction, not verified evidence
- general editorial standard
- instruction that unsupported claims must be verified or cut

Use this structure:

```text
COLIN BRIEF + EDITORIAL STANDARD — NOT VERIFIED EVIDENCE

Important:
This source contains Colin's article subject and article notes.

Treat the article subject and notes as editorial direction, not verified evidence.

Any statistics, psychology claims, buyer-behaviour claims, social media claims, hospitality claims, UGC claims, AI-search claims, OTA claims, direct-booking claims, content-performance claims, or commercial claims must be checked against credible public sources with URLs before they are used in the article.

ARTICLE SUBJECT:
[Insert article subject]

COLIN'S ARTICLE NOTES:
[Insert Colin's notes]

GENERAL EDITORIAL STANDARD FROM COLIN:
1. Evidence is non-negotiable.
2. Sources must be public.
3. Clarity beats cleverness.
4. The hook must be strong.
5. SEO metadata is required.
6. Source quality and source variety both matter.
7. Unsupported stats get cut.
8. Sources must be embedded inside the article body.
9. Visual assets are optional but valuable.
```

### 2. NotebookLM research setup — automated agent workflow

The agent runs NotebookLM programmatically via the `notebooklm-py` CLI. No manual web UI steps required.

#### Automated path (preferred)

Run these commands in sequence:

```bash
# Create the article notebook
notebooklm create "[Article topic] — Booked Wild"

# Add the Colin brief as a source (paste as text file or use --text flag)
notebooklm source add --text "COLIN BRIEF + EDITORIAL STANDARD..." --notebook "[Article topic] — Booked Wild"

# Add public research sources by URL
notebooklm source add --url <source-url-1> --notebook "[Article topic] — Booked Wild"
notebooklm source add --url <source-url-2> --notebook "[Article topic] — Booked Wild"

# Run the research pack prompt
notebooklm ask "Create a fast research pack for a Booked Wild article on [subject]. Output: best angle, opening hook options, 7–10 safe claims, claims to remove, source register with URLs, question-based H2 outline, 5–8 hospitality examples, suggested CTA." --notebook "[Article topic] — Booked Wild"

# Download the research pack as markdown
notebooklm download --format md --notebook "[Article topic] — Booked Wild" --output research-pack.md
```

#### Brand knowledge path (MCP — always live)

If the notebooklm MCP server is configured in Claude Code settings, query the "Booked Wild Brand" notebook directly before drafting:

- Use the MCP tool to query brand voice, banned words, audience definition, and commercial positioning
- This replaces manually adding brand files to each article notebook
- The brand notebook contains: Brand_Context.md, Brand_Voice_Guide.md, Content_Standards.md, Product_Offerings.md

MCP config for `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "notebooklm": {
      "command": "notebooklm",
      "args": ["mcp"]
    }
  }
}
```

#### Manual fallback

If notebooklm-py is not installed or auth has not been completed, fall back to manual setup:

Tell the user to create one NotebookLM notebook per article.

Notebook name format: `[Article topic] — Booked Wild`

Add:
- copied-text source block
- Booked Wild source files
- public web/source research

### 3. Web/source search rules

Use one broad combined search first.

The search should include:

- article subject
- psychology / behaviour terms
- travel / hospitality terms
- OTA / direct-booking terms if relevant
- UGC / social proof / review terms if relevant
- any specific stats or claims from Colin's brief

Example for UGC article:

```text
user generated content hospitality guest UGC social media sharing customer experience surprise delight packaging aesthetics photo worthy moments tourism restaurants cafes hotels social proof electronic word of mouth influencer authenticity paid influencers consumer trust Instagrammable experiences
```

### 4. Source-register clean-up

Before drafting, always clean the source register.

Reject:

- homepage URLs
- generic publisher URLs
- placeholder URLs
- incomplete URLs
- mismatched DOIs
- weak agency blogs
- unsupported marketing statistics
- sources that do not directly support the claim
- Wikipedia unless there is no better source and it is background only

Ask NotebookLM or the research agent to return:

1. source title
2. organisation or author
3. direct URL
4. claim supported
5. evidence strength: strong, moderate, weak
6. use: inline citation, background only, or reject
7. whether a better publisher/source-page URL exists instead of a DOI link

### 5. Source variety rule

Final reader-facing articles should not look like a DOI feed.

Use a maximum of one visible DOI link where possible.

DOI links are acceptable during research, but final article citations should prioritise:

- direct publisher article pages
- university repository pages
- official reports
- hospitality/travel trade sources
- platform resources
- credible industry articles
- government or regulatory guidance

If no non-DOI source page exists, a DOI link may be used.

A draft cannot score 9/10 or higher if the visible source mix is mostly DOI links.

### 6. Source count guide

Use this source target:

- fast article: 3–5 sources
- standard journal article: 5–7 sources
- expanded authority article: 6–8 sources
- pillar / map article: 8–12 sources

Source quality beats source count.

Do not add weak sources just to hit a number.

### 7. Claim-source matching

Use source types properly:

- psychology / trust claims → academic or publisher source
- UGC / eWOM / social proof claims → academic, tourism, platform, or industry source
- OTA / direct-booking claims → hospitality/travel trade or industry source
- AI-search claims → Booked Wild strategic opinion unless a strong AI-search source exists
- current platform rules / pricing / commissions → recent source required
- exact statistics → direct original source required

### 8. Unsupported stats rule

Cut unsupported statistics.

Examples to cut unless verified by a direct source:

- "38% more engagement"
- "3x more saves"
- "15–30% commission"
- "25% commission"
- "4.1x conversion"
- "10% revenue uplift"
- "60% of guests share travel content"

Specific numbers need specific sources.

No source, no number.

## NotebookLM research-pack prompt

After sources are added and cleaned, ask NotebookLM:

```text
Create a fast research pack for a Booked Wild article.

Use:
- Colin's article subject and notes as editorial direction, not verified evidence
- the Booked Wild brand files as the source of truth for voice, audience, structure, commercial positioning, CTA, and banned words
- Colin's general editorial standard as the quality standard
- external sources only for factual and research claims

Article subject:
[Insert article subject]

Output only:
1. Best article angle — 2 sentences
2. Strong opening hook — 2 options
3. 7–10 safe claims we can use
4. Claims from the subject/brief to remove or qualify
5. Source register with URLs
6. Question-based H2 outline
7. 5–8 practical travel/hospitality examples
8. Suggested CTA
9. Suggested internal links or Booked Wild offer connections
10. Optional visual asset idea, if the article introduces a framework, contrast, model, or diagnostic

For each source in the source register, include:
- Title
- Organisation or author
- Publication/date
- URL
- Claim supported
- Evidence strength: strong, moderate, weak
- Whether it should be used as inline citation, background only, or rejected

Mark each claim as:
- Strongly supported
- Moderately supported
- Weakly supported
- Unsupported
- Booked Wild strategic opinion

Source rule:
Aim for enough credible public sources with varied referring domains.
Use enough strong sources for the claims the article actually makes.
Do not include weak sources just to reach a number.
Do not rely only on DOI links.
Do not use homepage URLs.
Do not rely on Wikipedia if a stronger source exists.

Important:
Do not draft the article.
Do not include unsupported statistics.
Do not overclaim.
Keep the pack concise and practical.
```

## Claude drafting prompt template

When a cleaned research pack is ready, prepare a Claude drafting prompt.

The prompt must instruct Claude to:

- draft a finished Booked Wild website article
- use only the approved source register
- embed source URLs directly in the article body
- avoid source notes in the reader-facing article
- use question-based H2s
- include metadata
- include a CTA to the Deep Insight Audit
- use UK English
- avoid banned words
- avoid unsupported stats and guarantees

Core wording:

```text
Draft a Booked Wild journal article from this research pack.

Subject:
[Insert subject]

Audience:
Independent travel and hospitality operators across Europe: cafés, restaurants, boutique stays, cabins, lodges, retreats, tour operators, food and drink venues, short-term rentals, and founder-led experience businesses.

Core angle:
[Insert angle from research pack]

Commercial context:
Booked Wild gets independent travel and hospitality operators recommended by AI search engines, then rebuilds the booking flow so visibility turns into direct bookings instead of commission paid to OTAs.

Important source rules:
Use only the approved source register.
Do not invent studies, authors, dates, source titles, statistics, or URLs.
Do not use placeholder URLs.
Do not use homepage URLs.
Do not use unsupported conversion statistics.
Do not claim anything guarantees bookings, revenue, virality, AI rankings, or conversion increases.
Use careful wording: can support, can reduce, can make more likely, can act as, can feel, may, suggests.
Do not include a reader-facing source notes section.
Embed source URLs inside the article body where the claims appear.
If a claim needs a source and the source register does not support it, remove the claim or mark it [SOURCE NEEDED].

Writing rules:
- UK English.
- Write as a finished Booked Wild website article.
- Commercial Guide voice with light Storytelling Host edge.
- No "help", "helps", or "helping".
- Avoid generic marketing language: solutions, bespoke, tailored, unlock, elevate, empower, transform, innovative, cutting-edge, robust, seamless, synergy, holistic.
- No unsupported statistics.
- No overclaims.
- Question-based H2s.
- 50–80 word direct-answer opening.
- Plain English over cleverness.
- Short paragraphs.
- Specific travel and hospitality examples.
- Do not sound like a social media guru, personal branding coach, or generic marketer.
- Frame AI visibility as Booked Wild strategic opinion unless directly sourced.

CTA:
Use:
Book your £97 Deep Insight Audit: https://www.bookedwild.com/audit/deep-insight

Output:
Return the article as it should look on the Booked Wild website.

Do not use YAML/frontmatter.
Do not use code blocks.
Do not output as MDX unless specifically requested.
Do not add a separate "Source notes" section for the reader-facing article.

Include:
1. Article metadata
2. Meta title
3. Meta description
4. Slug
5. Author placeholder
6. Last-updated placeholder
7. H1
8. 50–80 word direct-answer opening
9. Key takeaways if useful
10. Full article body with clear H2 headings
11. Embedded source links in the body where claims appear
12. CTA
13. Internal notes — not for publication, only if useful
14. Optional FAQ ideas under internal notes only
15. Optional Claude Design asset brief under internal notes only

Do not explain what you changed. Just return the finished article.
```

## Article formatting standard

Final article format:

```markdown
# Article metadata

**Meta title:** [Title]
**Meta description:** [Description]
**Slug:** [slug]
**Author:** [Author]
**Last updated:** [Date]

# [H1]

[50–80 word direct answer opening]

## Key takeaways

- [Takeaway]
- [Takeaway]
- [Takeaway]

## [Question-based H2]

[Direct answer + explanation + example + embedded source URL where relevant]

## [Question-based H2]

[...]

## Ready to [commercial outcome]?

[CTA paragraph]

Book your £97 Deep Insight Audit: https://www.bookedwild.com/audit/deep-insight
```

## Citation rules

Sources must appear in the article body where the claim appears.

Correct:

```text
Research into authenticity cues in hospitality shows that guests respond more positively when details feel genuine and connected to the business rather than artificial: https://pure.hud.ac.uk/en/publications/the-chain-of-effects-from-authenticity-cues-to-purchase-intention/
```

Incorrect:

```text
Source notes:
Kim et al. — authenticity cues.
```

Do not rely on a references list as the only citation method.

## Final QC checklist

Before scoring or sending to Colin, check:

### Source checks

- Are source URLs embedded in the article body?
- Are there any homepage URLs?
- Are there any placeholder URLs?
- Are there any unsupported statistics?
- Are there too many DOI links?
- Is there source-domain variety?
- Do source links support the claims they sit beside?
- Can any DOI links be replaced with publisher/source pages?
- Is AI-search framed as strategic opinion unless directly sourced?

### Article checks

- Does the article have metadata?
- Does it have a clear H1?
- Does the opening answer the question directly?
- Are H2s question-based?
- Are examples specific to independent travel/hospitality?
- Is the CTA present and correct?
- Does the CTA use `https://www.bookedwild.com/audit/deep-insight`?
- Is UK English used?
- Are banned words removed?
- Are claims careful and non-deterministic?
- Is there no reader-facing source notes section?
- Are internal notes clearly marked not for publication?

### Broken citation check

Adding URLs can break sentences. Check for errors like:

```text
... https://source.com) tour operator who explains...
```

Fix to:

```text
... https://source.com). A tour operator who explains...
```

## Scoring guide

Use this scoring logic:

### 10/10

- strong Booked Wild voice
- clean website-ready formatting
- no unsupported stats
- strong source fit
- visible source-domain variety
- maximum one visible DOI link where possible
- embedded source URLs
- direct booking / AI visibility angle handled carefully
- CTA correct
- internal notes and design prompt included if needed

### 9/10

- publishable after minor formatting cleanup
- source mix acceptable
- no major claim risks
- maybe one or two small improvements remain

### 8/10–8.9/10

- good draft but needs another pass
- common reasons: too many DOI links, thin examples, missing H1, soft CTA, weak source variety, unsupported wording

### Below 8/10

- not Colin-ready
- common reasons: missing embedded citations, weak source register, unsupported stats, wrong CTA, vague article angle, too generic

Do not score above 8.5 if source URLs are mostly DOI links or the source mix lacks visible variety.

Do not score above 8 if source URLs are not embedded in the article body.

## Note for Colin

When sending a finished article to Colin, include a short note:

```text
Hi Colin — here's the next article draft.

A few notes before review:

- Unsupported claims were removed or softened.
- Source links are embedded directly in the article body.
- The source mix uses varied public sources rather than relying only on DOI links.
- AI visibility is framed as Booked Wild strategic opinion, not a ranking guarantee.
- CTA points to the confirmed Deep Insight Audit page: https://www.bookedwild.com/audit/deep-insight

I've also included a suggested visual asset / Claude Design prompt if we want to add a framework graphic to the article.
```

## Design asset prompt rules

If the article introduces a framework, contrast, model, matrix, checklist, or diagnostic, include a Claude Design prompt.

The prompt should specify:

- asset title
- purpose
- format
- sections or quadrants
- examples
- visual style
- caption
- placement
- output requirement

Example asset prompt:

```text
Create a clean editorial website asset for a Booked Wild article.

Asset title:
[Framework name]

Purpose:
[What the asset explains]

Format:
[Matrix / table / diagram / flow]

Visual style:
Clean editorial style. Booked Wild brand feel: premium, grounded, direct, not playful or gimmicky. Use warm natural tones, not bright social-media colours. No cartoon icons. No influencer-style graphics. Use simple linework, subtle texture, and strong typography. UK English.

Output:
A polished website-ready visual asset.
```

## Publication rule

For publication, remove all sections titled:

- `Internal notes — not for publication`
- `Note for Colin — not for publication`
- `Sources used`
- `Claude Design prompt`

unless Colin specifically wants them included in the CMS draft.

The reader-facing article should end at the CTA.
