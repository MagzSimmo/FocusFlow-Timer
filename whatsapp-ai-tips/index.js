require("dotenv").config();
const express = require("express");
const cron = require("node-cron");
const twilio = require("twilio");
const fs = require("fs");
const path = require("path");
const tips = require("./tips");

const {
  TWILIO_ACCOUNT_SID,
  TWILIO_AUTH_TOKEN,
  TWILIO_WHATSAPP_NUMBER,
  PORT = 3000,
  DAILY_SEND_HOUR = "9",   // 24-hour, server local time
  DAILY_SEND_MINUTE = "0",
} = process.env;

if (!TWILIO_ACCOUNT_SID || !TWILIO_AUTH_TOKEN || !TWILIO_WHATSAPP_NUMBER) {
  console.error(
    "Missing required env vars: TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_WHATSAPP_NUMBER"
  );
  process.exit(1);
}

const client = twilio(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN);
const SUBSCRIBERS_FILE = path.join(__dirname, "subscribers.json");

// ── Subscriber helpers ────────────────────────────────────────────────────────

function loadSubscribers() {
  try {
    return JSON.parse(fs.readFileSync(SUBSCRIBERS_FILE, "utf8"));
  } catch {
    return [];
  }
}

function saveSubscribers(subscribers) {
  fs.writeFileSync(SUBSCRIBERS_FILE, JSON.stringify(subscribers, null, 2));
}

function findSubscriber(subscribers, phone) {
  return subscribers.find((s) => s.phone === phone);
}

function normalisePhone(raw) {
  // Strip non-digits then ensure E.164 format; keep any leading +
  return raw.startsWith("+") ? raw : `+${raw.replace(/\D/g, "")}`;
}

// ── Message sending ───────────────────────────────────────────────────────────

function formatTip(tip) {
  return (
    `*Day ${tip.day}/30 — ${tip.title}*\n\n` +
    `${tip.body}\n\n` +
    `_Reply *STOP* to unsubscribe at any time._`
  );
}

async function sendTip(phone, tip) {
  await client.messages.create({
    from: `whatsapp:${TWILIO_WHATSAPP_NUMBER}`,
    to: `whatsapp:${phone}`,
    body: formatTip(tip),
  });
}

async function sendWelcome(phone) {
  const body =
    `👋 *Welcome to AI Tips for Beginners!*\n\n` +
    `You'll receive one friendly AI tip per day for 30 days — no jargon, no tech experience needed.\n\n` +
    `Your first tip arrives tomorrow morning. Can't wait? Reply *NOW* to get Day 1 right now!\n\n` +
    `_Reply *STOP* at any time to unsubscribe._`;

  await client.messages.create({
    from: `whatsapp:${TWILIO_WHATSAPP_NUMBER}`,
    to: `whatsapp:${phone}`,
    body,
  });
}

async function sendDailyTips() {
  const subscribers = loadSubscribers();
  const today = new Date().toISOString().split("T")[0];

  for (const subscriber of subscribers) {
    if (subscriber.paused) continue;

    const tip = tips[subscriber.dayIndex];
    if (!tip) {
      console.log(`${subscriber.phone} has completed all 30 tips.`);
      continue;
    }

    try {
      await sendTip(subscriber.phone, tip);
      subscriber.dayIndex += 1;
      subscriber.lastSent = today;
      console.log(`Sent Day ${tip.day} to ${subscriber.phone}`);
    } catch (err) {
      console.error(`Failed to send to ${subscriber.phone}:`, err.message);
    }
  }

  saveSubscribers(subscribers);
}

// ── Cron scheduler ────────────────────────────────────────────────────────────

const cronExpression = `${DAILY_SEND_MINUTE} ${DAILY_SEND_HOUR} * * *`;
cron.schedule(cronExpression, sendDailyTips, { timezone: "UTC" });
console.log(`Daily tips scheduled at ${DAILY_SEND_HOUR}:${String(DAILY_SEND_MINUTE).padStart(2, "0")} UTC`);

// ── Express webhook (handles inbound WhatsApp messages from Twilio) ────────────

const app = express();
app.use(express.urlencoded({ extended: false }));
app.use(express.json());

// Twilio sends POST to this webhook when a user messages your WhatsApp number.
// Configure this URL in your Twilio console under:
//   Messaging → Senders → WhatsApp Senders → [your number] → Sandbox settings
//   "When a message comes in" → https://<your-domain>/webhook
app.post("/webhook", async (req, res) => {
  const from = req.body.From; // e.g. "whatsapp:+447700900000"
  const body = (req.body.Body || "").trim().toUpperCase();

  if (!from) return res.sendStatus(400);

  const phone = from.replace("whatsapp:", "");
  const subscribers = loadSubscribers();
  const existing = findSubscriber(subscribers, phone);

  if (body === "STOP") {
    if (existing) {
      existing.paused = true;
      saveSubscribers(subscribers);
      console.log(`Unsubscribed: ${phone}`);
    }
    return res.sendStatus(200);
  }

  if (body === "START" || body === "JOIN" || body === "YES") {
    if (existing && !existing.paused) {
      // Already subscribed — do nothing
      return res.sendStatus(200);
    }
    if (existing && existing.paused) {
      existing.paused = false;
      saveSubscribers(subscribers);
    } else {
      subscribers.push({
        phone,
        dayIndex: 0,
        joinedAt: new Date().toISOString(),
        lastSent: null,
        paused: false,
      });
      saveSubscribers(subscribers);
    }
    try {
      await sendWelcome(phone);
    } catch (err) {
      console.error(`Welcome message failed for ${phone}:`, err.message);
    }
    return res.sendStatus(200);
  }

  if (body === "NOW") {
    if (!existing || existing.paused) return res.sendStatus(200);
    const tip = tips[existing.dayIndex];
    if (tip) {
      try {
        await sendTip(phone, tip);
        existing.dayIndex += 1;
        existing.lastSent = new Date().toISOString().split("T")[0];
        saveSubscribers(subscribers);
      } catch (err) {
        console.error(`On-demand tip failed for ${phone}:`, err.message);
      }
    }
    return res.sendStatus(200);
  }

  // Unknown message — send a help reply
  await client.messages.create({
    from: `whatsapp:${TWILIO_WHATSAPP_NUMBER}`,
    to: `whatsapp:${phone}`,
    body:
      "Hi! 👋 Here's what you can say:\n• *JOIN* — start receiving daily AI tips\n• *NOW* — get today's tip immediately\n• *STOP* — unsubscribe",
  });

  res.sendStatus(200);
});

// ── Admin endpoints ────────────────────────────────────────────────────────────

// GET /subscribers — list all subscribers (protect this in production!)
app.get("/subscribers", (req, res) => {
  res.json(loadSubscribers());
});

// POST /send-now — manually trigger the daily batch send
app.post("/send-now", async (req, res) => {
  try {
    await sendDailyTips();
    res.json({ ok: true, message: "Daily tips sent." });
  } catch (err) {
    res.status(500).json({ ok: false, error: err.message });
  }
});

// POST /add-subscriber — manually add a subscriber (E.164 phone number)
app.post("/add-subscriber", async (req, res) => {
  const { phone } = req.body;
  if (!phone) return res.status(400).json({ error: "phone required" });

  const normalised = normalisePhone(phone);
  const subscribers = loadSubscribers();

  if (findSubscriber(subscribers, normalised)) {
    return res.status(409).json({ error: "Already subscribed." });
  }

  subscribers.push({
    phone: normalised,
    dayIndex: 0,
    joinedAt: new Date().toISOString(),
    lastSent: null,
    paused: false,
  });
  saveSubscribers(subscribers);

  try {
    await sendWelcome(normalised);
  } catch (err) {
    console.error("Welcome failed:", err.message);
  }

  res.json({ ok: true, phone: normalised });
});

app.listen(PORT, () => {
  console.log(`WhatsApp AI Tips service running on port ${PORT}`);
});
