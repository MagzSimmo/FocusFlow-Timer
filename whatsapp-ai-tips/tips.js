// 30 daily AI tips written for complete beginners — plain language, actionable, friendly tone.
const tips = [
  {
    day: 1,
    title: "What even IS AI?",
    body:
      "AI (Artificial Intelligence) is software that can learn from examples and make decisions — like recognising your face to unlock your phone, or suggesting what to watch next on Netflix. It's not magic, it's just very good pattern-matching. 🤖",
  },
  {
    day: 2,
    title: "ChatGPT in one sentence",
    body:
      "ChatGPT is an AI you chat with in plain English (or your own language). You ask it anything — 'explain this email', 'write me a recipe', 'help me reply to my boss' — and it answers like a knowledgeable friend. Try it free at chat.openai.com. 💬",
  },
  {
    day: 3,
    title: "You're already using AI every day",
    body:
      "Google autocomplete, spam filters in your email, voice assistants like Siri or Google Assistant, and the 'For You' feed on TikTok — all powered by AI. You've been using it for years without realising it! 📱",
  },
  {
    day: 4,
    title: "The magic word: 'prompt'",
    body:
      "A *prompt* is simply the message you type to an AI. Better prompts = better answers. Instead of 'help me write', try 'help me write a friendly WhatsApp message to cancel a dentist appointment'. More detail = better results. ✍️",
  },
  {
    day: 5,
    title: "AI is a draft machine, not a finished product",
    body:
      "Think of AI as giving you a strong first draft — 80% done in seconds. You still review, tweak, and put your own voice in. The best results come from humans and AI working together, not one replacing the other. 🤝",
  },
  {
    day: 6,
    title: "Try this prompt right now",
    body:
      "Open ChatGPT or any AI chatbot and type exactly this:\n\n\"Explain what machine learning is like I'm 10 years old.\"\n\nGood prompts often include *who you are* or *what level* you want the answer at. Try it! 🎯",
  },
  {
    day: 7,
    title: "AI can hallucinate — and that's important to know",
    body:
      "AI sometimes confidently states wrong information. This is called 'hallucination'. Always double-check important facts (medical, legal, financial) from trusted sources. AI is great for ideas and drafts, not for facts you stake your life on. ⚠️",
  },
  {
    day: 8,
    title: "Free AI tools worth bookmarking",
    body:
      "Here are 3 free AI tools to explore:\n• ChatGPT (chat.openai.com) — general assistant\n• Google Gemini (gemini.google.com) — great with Google Docs/Gmail\n• Perplexity (perplexity.ai) — AI search with sources\n\nAll free to start. No credit card needed. 🛠️",
  },
  {
    day: 9,
    title: "The 'role' trick for better answers",
    body:
      "Tell the AI what *role* to play. Examples:\n• \"Act as a friendly nutritionist and suggest a healthy weekly meal plan.\"\n• \"Act as a primary school teacher and explain fractions simply.\"\n\nThis one trick dramatically improves the quality of answers. 🎭",
  },
  {
    day: 10,
    title: "AI for everyday tasks at home",
    body:
      "AI can help with real daily life:\n• Write a shopping list from a recipe\n• Translate a letter or document\n• Suggest gift ideas for someone's birthday\n• Draft a complaint letter to a company\n\nIt's like having a helpful assistant in your pocket. 🏠",
  },
  {
    day: 11,
    title: "What is an LLM?",
    body:
      "LLM stands for *Large Language Model* — the technology behind ChatGPT and similar tools. It was trained on billions of web pages, books, and articles, so it 'knows' a lot about the world. Think of it as a very well-read assistant. 📚",
  },
  {
    day: 12,
    title: "AI image generators — what are they?",
    body:
      "Tools like DALL-E, Midjourney, and Adobe Firefly can create images from text descriptions. Example prompt: 'a cosy coffee shop on a rainy evening, warm lighting, painting style'. Great for social media graphics, logos, and creative projects. 🎨",
  },
  {
    day: 13,
    title: "Never share private information with AI",
    body:
      "Don't type passwords, bank details, ID numbers, or sensitive personal data into AI chatbots. Your conversations may be used to improve the AI. Treat it like a public forum — useful, but not private. 🔒",
  },
  {
    day: 14,
    title: "The 'explain like I'm a beginner' trick",
    body:
      "Whenever an AI answer feels too complicated, just reply:\n\n\"Can you explain that in simpler terms?\"\n\nor\n\n\"Give me an example using everyday life.\"\n\nAI never gets annoyed at follow-up questions. Ask as many as you need. 😊",
  },
  {
    day: 15,
    title: "AI at work — where it helps most",
    body:
      "Top ways people use AI at work:\n• Writing and editing emails\n• Summarising long documents\n• Creating presentations outlines\n• Translating content\n• Brainstorming ideas\n\nYou don't need to be technical — just describe what you need. 💼",
  },
  {
    day: 16,
    title: "What is 'prompt engineering'?",
    body:
      "Prompt engineering just means writing better instructions for AI. No coding required. The skill is learning *how to ask* clearly. As AI becomes more common, this is one of the most valuable skills anyone can learn — and it's free to practise. 🧠",
  },
  {
    day: 17,
    title: "AI for learning new things",
    body:
      "AI is an incredible tutor. Try:\n• \"Teach me basic Spanish greetings and quiz me.\"\n• \"Explain how mortgages work, step by step.\"\n• \"What are the key ideas in the book Atomic Habits?\"\n\nIt's patient, available 24/7, and never makes you feel silly for asking. 📖",
  },
  {
    day: 18,
    title: "Voice AI — talking instead of typing",
    body:
      "You don't have to type! Many AI tools have voice modes:\n• ChatGPT app has a voice feature\n• Apple's Siri uses AI\n• Amazon Alexa uses AI\n\nIf typing is difficult or you just prefer talking, go voice. Same powerful AI, hands-free. 🎙️",
  },
  {
    day: 19,
    title: "AI won't steal your job — but someone using AI might",
    body:
      "Most experts agree: AI replaces *tasks*, not whole jobs. Workers who use AI to do more, faster, become more valuable. The best move is to learn to work *with* AI, not against it. Start with one small task this week. 🚀",
  },
  {
    day: 20,
    title: "Summarise anything with AI",
    body:
      "Got a long article, contract, or email thread? Paste it into ChatGPT and say:\n\n\"Summarise this in 5 bullet points.\"\n\nor\n\n\"What are the key things I need to know from this?\"\n\nInstant summary. Huge time-saver. ⚡",
  },
  {
    day: 21,
    title: "AI for health questions — use carefully",
    body:
      "AI can explain medical terms, help you understand a diagnosis, or suggest questions to ask your doctor. But it should *never* replace actual medical advice. Use it to prepare for appointments, not to self-diagnose. 🏥",
  },
  {
    day: 22,
    title: "What is 'context window'?",
    body:
      "An AI chatbot can only 'remember' what's in the current conversation. If you start a new chat, it forgets everything. This is called the *context window*. Tip: keep important chats open, or copy-paste key info back in if you start fresh. 💡",
  },
  {
    day: 23,
    title: "AI for creative writing",
    body:
      "AI is great creative fuel:\n• Stuck on a story? Ask AI to suggest what happens next.\n• Need a poem for a birthday card? Describe the person.\n• Writing a speech? Ask AI for an opening line.\n\nUse it as a creative partner, then make it your own. ✨",
  },
  {
    day: 24,
    title: "The difference between AI tools",
    body:
      "Not all AI is the same:\n• ChatGPT (OpenAI) — versatile, great writing\n• Gemini (Google) — connected to Google services\n• Claude (Anthropic) — great for long documents, careful answers\n• Copilot (Microsoft) — built into Windows & Office\n\nTry a couple and see which *feels* right to you. 🔍",
  },
  {
    day: 25,
    title: "How to spot AI-generated content",
    body:
      "AI writing often:\n• Sounds overly polished or formal\n• Uses lists and bullet points a lot\n• Starts with 'Certainly!' or 'Great question!'\n• Lacks personal opinion or lived experience\n\nIt's becoming harder to spot — which is why your *human voice* and real experiences are more valuable than ever. 👁️",
  },
  {
    day: 26,
    title: "AI accessibility tools",
    body:
      "AI is making technology more accessible:\n• Auto-captions in videos (YouTube, Zoom)\n• Screen readers powered by AI\n• Real-time translation in video calls\n• AI that describes images for visually impaired users\n\nThese tools help millions of people every day. ♿",
  },
  {
    day: 27,
    title: "The 3-step prompt formula",
    body:
      "Great prompts usually have 3 parts:\n1. *Role* — 'Act as a friendly travel agent'\n2. *Task* — 'Suggest a 5-day itinerary for Lisbon'\n3. *Format* — 'as a day-by-day list with budget tips'\n\nCombine them: 'Act as a friendly travel agent. Suggest a 5-day Lisbon itinerary as a day-by-day list with budget tips.' 🗺️",
  },
  {
    day: 28,
    title: "AI ethics — the big questions",
    body:
      "AI raises important questions society is working through:\n• Who is responsible when AI makes a mistake?\n• Can AI be biased? (Yes — it can reflect biases in training data)\n• Should AI art be protected by copyright?\n\nYou don't need all the answers — just knowing the questions makes you an informed AI user. 🌍",
  },
  {
    day: 29,
    title: "Build your own AI habit",
    body:
      "The best way to get good at using AI: use it daily for small things.\n• Draft your morning to-do list\n• Translate one thing\n• Ask one question you'd normally Google\n\nAfter 30 days you'll be amazed how natural it feels. Consistency beats perfection. 📅",
  },
  {
    day: 30,
    title: "You made it — what's next?",
    body:
      "Congratulations on 30 days of AI tips! 🎉\n\nYou now know:\n✅ What AI is and how it works\n✅ Key tools and how to use them\n✅ How to write effective prompts\n✅ When to trust AI — and when not to\n\nKeep exploring. The best way to learn AI is to keep using it. You've got this! 💪",
  },
];

module.exports = tips;
