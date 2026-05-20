# Booked Wild Automation System — Review Document
**Prepared for:** Colin Harrison & Nigel Simmonds
**Date:** May 2026
**Session:** Initial build review and multi-platform planning

---

## 1. What We Built

A fully automated content pipeline that runs daily on GitHub Actions:

```
Topic (Claude Haiku)
  → Research (Gemini Flash)
  → Script/Article (Claude Haiku)
  → Video (MoviePy + Edge TTS)
  → Upload (YouTube Data API v3)
```

All code lives at: `github.com/nigel-sketch/Youtube-Automation-`

---

## 2. Current Status — YouTube Pipeline

| Component | Status | Notes |
|---|---|---|
| Topic generation | ✅ Working | Claude Haiku, avoids recent topics |
| Research | ⚠️ Degraded | Gemini free tier quota hit — using fallback |
| Script writing | ✅ Working | QC scores 8-9/10, strong Booked Wild voice |
| Voiceover | ✅ Working | Edge TTS, British female voice, free |
| Video assembly | ✅ Working | 1920x1080, 15-20 min render |
| Background images | ❌ Pending | Need images uploaded to assets/ folder |
| Thumbnail | ⚠️ Partial | YouTube channel needs phone verification |
| Auto-upload | ✅ Working | Uploads as private, logs to upload_log.json |
| Daily schedule | ⏸️ Paused | Pending review and image fix |

**Sample videos produced:**
- "How Do I Leave GetYourGuide Without Losing All My Bookings?"
- "Why ChatGPT Recommends Your Competitor's Lodge (Not Yours)"
- "How Can I Get My B&B Featured in AI Travel Searches Before Competitors Steal My Guests?"

---

## 3. Cost Breakdown

| Service | Plan | Monthly Cost |
|---|---|---|
| Anthropic API (Claude) | Pay per use | ~£1–3/month (daily videos) |
| Google AI Studio (Gemini) | Free tier | £0 (hitting limits) |
| Edge TTS (Microsoft) | Free | £0 |
| GitHub Actions | Free tier | £0 |
| YouTube Data API | Free | £0 |
| **Total** | | **~£1–3/month** |

---

## 4. What Needs Fixing Before Relaunch

| Priority | Fix | Effort |
|---|---|---|
| High | Upload background images to assets/ folder | 30 mins |
| High | Verify YouTube channel phone number (thumbnails) | 5 mins |
| Medium | Upgrade Gemini to paid tier for research | £20/month |
| Low | Switch script model back to Sonnet if quality drops | 5 mins |

---

## 5. Multi-Platform Expansion Plan

### LinkedIn
- **Format:** Long-form article (800–1200 words) + short post teaser
- **Tone:** Ally & Mentor voice (from Booked Wild Brand Voice Guide)
- **Output:** Article markdown + post copy + 3 hashtags
- **Effort to build:** Low — reuse existing script writer, adjust prompt
- **Automation:** Publish via LinkedIn API (requires app approval)

### Instagram
- **Format:** Carousel (5-7 slides) + caption (150 words max) + hashtags
- **Tone:** Rewilding Evangelist — punchy, visual, emotional
- **Output:** Slide text for each panel + caption copy
- **Effort to build:** Medium — need image generation for carousel panels
- **Automation:** Publish via Instagram Graph API (requires Facebook Business account)

### Facebook
- **Format:** Short post (100–150 words) linking to YouTube video
- **Tone:** Storytelling Host — warm, case-study led
- **Output:** Post copy + link preview
- **Effort to build:** Low — wrap YouTube upload with Facebook post
- **Automation:** Facebook Graph API — straightforward

### Reddit
- **Format:** Community post (r/Hospitality, r/SmallBusiness, r/TravelHacking)
- **Tone:** Completely different — no selling, genuine contribution, value first
- **Output:** Post title + body (no CTA, no product mention)
- **Effort to build:** Low — separate prompt, strict no-sell rules
- **Automation:** Reddit API (PRAW library) — easy to implement
- **Risk:** Reddit bans promotional accounts — needs genuine community tone

### TikTok / YouTube Shorts
- **Format:** 60-second vertical video
- **Content:** Pull key stat from the article, 3-line hook, quick answer
- **Effort to build:** Medium — requires vertical crop + subtitle burn-in
- **Automation:** TikTok API (restricted, requires business account)

---

## 6. Recommended Platform Priority

| Order | Platform | Why |
|---|---|---|
| 1 | YouTube (fix & relaunch) | Already built, highest authority signal |
| 2 | LinkedIn | B2B audience, direct reach to operators, easy to build |
| 3 | Facebook | Low effort, same content as YouTube description |
| 4 | Instagram | Medium effort, good for visual brand building |
| 5 | Reddit | Low cost, high trust — but needs careful tone |

---

## 7. Proposed Architecture for Multi-Platform Pipeline

```
Claude generates:
  - article_markdown (YouTube video script)
  - linkedin_article (long form)
  - linkedin_post (short teaser)
  - instagram_caption + slide_texts[]
  - facebook_post
  - reddit_post (no CTA version)

Pipeline publishes to each platform in sequence.
All content from one daily topic — one AI run, five platforms.
```

Estimated additional build time: **2–3 days** for LinkedIn + Facebook.
Instagram + Reddit: **additional 1–2 days each**.

---

## 8. Questions for Colin

1. Which platforms are priority — LinkedIn first or all at once?
2. Is the current Booked Wild voice guide sufficient for all platforms, or do we need platform-specific tone docs?
3. Budget for Gemini paid tier (research quality improvement)?
4. Approval workflow — stay private until Colin reviews, or auto-publish?
5. Do we want a weekly digest email summarising what was published?

---

*Document generated by Claude Code — Booked Wild Automation Review, May 2026*
