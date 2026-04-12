const fs = require('fs');
const path = require('path');

const rootDir = process.cwd();
const BASE_URL = 'https://brightlane.github.io/skyscanner-flight-desk/';

const CITIES = ["London", "Paris", "New York", "Tokyo", "Dubai", "Singapore", "Rome", "Bangkok", "Istanbul", "Seoul", "Barcelona", "Madrid", "Milan", "Vietnam", "Bali", "Sydney", "Toronto", "Berlin", "Amsterdam", "Athens"];
const FLIGHT_KEYS = ["cheap-flights-to-", "best-airfare-to-", "last-minute-flights-to-"];

async function runVultureEngine() {
    console.log("🚀 Vulture Engine: Starting 10K Build...");

    // Ensure templates exist
    if (!fs.existsSync('master-template.html') || !fs.existsSync('blog-template.html')) {
        console.error("❌ Missing templates! Ensure master-template.html and blog-template.html are in root.");
        process.exit(1);
    }

    const template = fs.readFileSync('master-template.html', 'utf8');
    const blogTemplate = fs.readFileSync('blog-template.html', 'utf8');
    let sitemapEntries = [];

    // 1. Generate Fleet
    CITIES.forEach(city => {
        FLIGHT_KEYS.forEach(intent => {
            for (let i = 1; i <= 5; i++) {
                const slug = `${intent}${city.toLowerCase().replace(/ /g, '-')}-${i}.html`;
                const html = template
                    .replace(/{{CITY}}/g, city)
                    .replace(/{{DATE}}/g, new Date().toUTCString())
                    .replace(/{{PRICE}}/g, `$${Math.floor(Math.random() * 400 + 150)}`);

                fs.writeFileSync(path.join(rootDir, slug), html);
                sitemapEntries.push(`${BASE_URL}${slug}`);
            }
        });
    });

    // 2. Generate Blog
    let blogPostsHtml = '';
    CITIES.slice(0, 5).forEach(city => {
        blogPostsHtml += `<div class="post"><h2>Audit: ${city}</h2><p>Live data sync active.</p><a href="cheap-flights-to-${city.toLowerCase()}-1.html">View Fares</a></div>`;
    });
    const finalBlog = blogTemplate.replace(/{{BLOG_POSTS}}/g, blogPostsHtml).replace(/{{DATE}}/g, new Date().toUTCString());
    fs.writeFileSync('blog.html', finalBlog);

    // 3. Generate Sitemap
    let xml = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">`;
    sitemapEntries.forEach(url => { xml += `\n  <url><loc>${url}</loc><priority>0.8</priority></url>`; });
    xml += `\n</urlset>`;
    fs.writeFileSync('sitemap.xml', xml);

    console.log(`✅ Build Complete. ${sitemapEntries.length} pages generated.`);
}

runVultureEngine();
