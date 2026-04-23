const axios = require("axios");
const fs = require("fs");

// =====================
// CONFIG
// =====================
const OPENAI_KEY = process.env.OPENAI_API_KEY;

const AFFILIATE =
  "https://convert.ctypy.com/aff_c?offer_id=29465&aff_id=21885";

// WordPress (optional)
const WP_ENABLED = false;
const WP_URL = "https://your-site.com/wp-json/wp/v2/posts";
const WP_USER = "user";
const WP_PASS = "app_password";

// Social (optional)
const SOCIAL = {
  x: false,
  telegram: false,
  telegramToken: "",
  telegramChatId: ""
};

// =====================
// KEYWORDS (simple batch)
// =====================
const keywords = [
  "cheap flights from USA to Europe 2026",
  "Skyscanner travel hacks 2026",
  "best time to book flights",
  "how to find cheap airfare online"
];

// =====================
// AI WRITER
// =====================
async function generateBlog(keyword) {
  const prompt = `
Write a 900–1200 word SEO blog.

Topic: ${keyword}

Rules:
- Human tone
- Use headings
- Add travel tips
- Include FAQ section
- Mention flight comparison tools naturally
`;

  const res = await axios.post(
    "https://api.openai.com/v1/chat/completions",
    {
      model: "gpt-4o-mini",
      messages: [
        { role: "system", content: "You are an SEO travel writer." },
        { role: "user", content: prompt }
      ],
      temperature: 0.8
    },
    {
      headers: {
        Authorization: `Bearer ${OPENAI_KEY}`
      }
    }
  );

  return res.data.choices[0].message.content;
}

// =====================
// AFFILIATE INJECTION
// =====================
function addAffiliate(content) {
  return `
${content}

<hr>

<p><a href="${AFFILIATE}">
<b>👉 Compare live flight deals here</b>
</a></p>
`;
}

// =====================
// SAVE FILE
// =====================
function saveHTML(title, content) {
  const file =
    title.replace(/ /g, "-").toLowerCase().replace(/[^a-z0-9-]/g, "") +
    ".html";

  const html = `
<!DOCTYPE html>
<html>
<head>
<title>${title}</title>
<meta name="description" content="${title} travel guide">
</head>
<body style="font-family:Arial;max-width:800px;margin:auto;line-height:1.6">
<h1>${title}</h1>
${content}
</body>
</html>
`;

  fs.writeFileSync(file, html);
  return file;
}

// =====================
// WORDPRESS PUBLISH
// =====================
async function publishWP(title, content) {
  const auth = Buffer.from(`${WP_USER}:${WP_PASS}`).toString("base64");

  await axios.post(
    WP_URL,
    {
      title,
      content,
      status: "draft"
    },
    {
      headers: {
        Authorization: `Basic ${auth}`
      }
    }
  );
}

// =====================
// SOCIAL POST FORMAT
// =====================
function socialText(title, url) {
  return `✈️ ${title}

Find cheap flights instantly:
${url}

Save money on travel 💰`;
}

// =====================
// TELEGRAM POST
// =====================
async function postTelegram(text) {
  await axios.post(
    `https://api.telegram.org/bot${SOCIAL.telegramToken}/sendMessage`,
    {
      chat_id: SOCIAL.telegramChatId,
      text
    }
  );
}

// =====================
// MAIN ENGINE
// =====================
async function run() {
  console.log("🚀 SEO system started");

  for (let i = 0; i < keywords.length; i++) {
    const keyword = keywords[i];

    try {
      console.log("Generating:", keyword);

      // 1. AI blog
      let content = await generateBlog(keyword);

      // 2. affiliate injection
      content = addAffiliate(content);

      // 3. save file
      const file = saveHTML(keyword, content);

      console.log("Saved:", file);

      // 4. optional wordpress
      if (WP_ENABLED) {
        await publishWP(keyword, content);
      }

      // 5. social post
      const url = `https://yourdomain.com/${file}`;
      const post = socialText(keyword, url);

      if (SOCIAL.telegram) {
        await postTelegram(post);
      }

      console.log("Posted social:", keyword);

      // delay
      await new Promise((r) => setTimeout(r, 2000));
    } catch (err) {
      console.log("Error:", err.message);
    }
  }

  console.log("DONE");
}

run();
