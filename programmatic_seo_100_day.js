const fs = require("fs");
const axios = require("axios");

const OUTPUT_DIR = "./daily_100_blogs";

if (!fs.existsSync(OUTPUT_DIR)) {
  fs.mkdirSync(OUTPUT_DIR);
}

const AFFILIATE_LINK =
  "https://convert.ctypy.com/aff_c?offer_id=29465&aff_id=21885";

// -----------------------------
// KEYWORD ENGINE (expand this massively)
// -----------------------------
const keywords = Array.from({ length: 1000 }, (_, i) => {
  const routes = [
    "New York to London",
    "London to Dubai",
    "USA to Tokyo",
    "Paris to Rome",
    "Chicago to Bangkok"
  ];

  return `cheap flights ${routes[i % routes.length]} ${2026}`;
});

// -----------------------------
// AI CONTENT GENERATION
// -----------------------------
async function generateContent(keyword) {
  const prompt = `
Write a 900–1300 word SEO travel article about: "${keyword}"

Rules:
- Human tone
- Include H2 sections
- Include travel tips
- Mention flight comparison tools naturally (like Skyscanner)
- Include FAQ section
- Avoid repetition
`;

  const res = await axios.post(
    "https://api.openai.com/v1/chat/completions",
    {
      model: "gpt-4o-mini",
      messages: [
        { role: "system", content: "You are an SEO travel writer." },
        { role: "user", content: prompt }
      ],
      temperature: 0.9
    },
    {
      headers: {
        Authorization: `Bearer ${process.env.OPENAI_API_KEY}`,
        "Content-Type": "application/json"
      }
    }
  );

  return res.data.choices[0].message.content;
}

// -----------------------------
// SEO HTML WRAPPER
// -----------------------------
function wrapHTML(title, body) {
  const variations = [
    "Compare flights instantly",
    "Find cheaper airfare options",
    "Save money on your next trip",
    "Smart flight booking strategy"
  ];

  const ctaText = variations[Math.floor(Math.random() * variations.length)];

  return `
<!DOCTYPE html>
<html>
<head>
<title>${title}</title>
<meta name="description" content="Learn how to find ${title} and save money using flight comparison tools.">
</head>

<body style="font-family:Arial; max-width:850px; margin:auto; line-height:1.7;">

<h1>${title}</h1>

${body}

<hr>

<div style="text-align:center;margin:30px 0;">
  <a href="${AFFILIATE_LINK}"
     style="background:#ff6b35;color:#fff;padding:14px 24px;text-decoration:none;border-radius:8px;font-weight:bold;">
     ${ctaText} →
  </a>
</div>

<p>
Compare deals here: 
<a href="${AFFILIATE_LINK}">Search Flights</a>
</p>

</body>
</html>
`;
}

// -----------------------------
// MAIN RUNNER (100/day)
// -----------------------------
async function run() {
  console.log("Starting 100 blog generation...");

  for (let i = 0; i < 100; i++) {
    const keyword = keywords[i];

    try {
      console.log("Generating:", keyword);

      const content = await generateContent(keyword);

      const html = wrapHTML(keyword, content);

      const filename = `post-${i + 1}-${keyword
        .replace(/ /g, "-")
        .toLowerCase()
        .replace(/[^a-z0-9-]/g, "")}.html`;

      fs.writeFileSync(`${OUTPUT_DIR}/${filename}`, html);

      console.log("Saved:", filename);

      // small delay to avoid API rate limits
      await new Promise((r) => setTimeout(r, 1500));
    } catch (err) {
      console.log("Error:", err.message);
    }
  }

  console.log("DONE: 100 blogs generated");
}

run();
