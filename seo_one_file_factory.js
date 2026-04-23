const axios = require("axios");
const fs = require("fs");

// =========================
// CONFIG
// =========================
const OPENAI_KEY = process.env.OPENAI_API_KEY;

const ENABLE_WORDPRESS = false; // set true if ready
const WP_URL = "https://your-site.com/wp-json/wp/v2/posts";
const WP_USER = "your_username";
const WP_PASS = "your_app_password";

const AFFILIATE_LINK =
  "https://convert.ctypy.com/aff_c?offer_id=29465&aff_id=21885";

// =========================
// SIMPLE KEYWORD CLUSTERS
// =========================
const clusters = [
  {
    pillar: "Cheap Flights Guide",
    keywords: [
      "cheap flights from USA to Europe",
      "how to find cheap flights online",
      "best time to book flights 2026"
    ]
  },
  {
    pillar: "Skyscanner Hacks",
    keywords: [
      "Skyscanner tips and tricks",
      "how to use Skyscanner effectively",
      "Skyscanner price alerts guide"
    ]
  }
];

// =========================
// AI CONTENT GENERATOR
// =========================
async function generateArticle(keyword, pillar) {
  const prompt = `
Write a 900–1200 word SEO blog post.

Topic: ${keyword}
Cluster: ${pillar}

Rules:
- Human tone
- Include headings (H2)
- Include travel tips
- Mention flight comparison tools naturally
- Add FAQ section
- No repetition
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

// =========================
// INTERNAL LINKING (SIMPLE)
// =========================
function addAffiliateAndLinks(content) {
  return `
${content}

<hr>

<p><a href="${AFFILIATE_LINK}"><b>Compare live flight deals here</b></a></p>
`;
}

// =========================
// SAVE FILE
// =========================
function saveFile(title, content) {
  const filename =
    title.toLowerCase().replace(/ /g, "-").replace(/[^a-z0-9-]/g, "") +
    ".html";

  fs.writeFileSync(`./${filename}`, content);
  return filename;
}

// =========================
// WORDPRESS PUBLISHER (OPTIONAL)
// =========================
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
        Authorization: `Basic ${auth}`,
        "Content-Type": "application/json"
      }
    }
  );
}

// =========================
// MAIN ENGINE
// =========================
async function run() {
  console.log("SEO Factory Starting...");

  for (const cluster of clusters) {
    for (const keyword of cluster.keywords) {
      try {
        console.log("Generating:", keyword);

        let article = await generateArticle(keyword, cluster.pillar);

        article = addAffiliateAndLinks(article);

        const finalHTML = `
<!DOCTYPE html>
<html>
<head>
<title>${keyword}</title>
<meta name="description" content="${keyword} guide and travel tips">
</head>
<body style="font-family:Arial;max-width:800px;margin:auto;line-height:1.6">
<h1>${keyword}</h1>
${article}
</body>
</html>
`;

        const file = saveFile(keyword, finalHTML);

        console.log("Saved:", file);

        if (ENABLE_WORDPRESS) {
          await publishWP(keyword, finalHTML);
          console.log("Published to WordPress");
        }

        await new Promise((r) => setTimeout(r, 2000));
      } catch (err) {
        console.log("Error:", err.message);
      }
    }
  }

  console.log("DONE");
}

run();
