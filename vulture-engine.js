const fs = require('fs');
const path = require('path');

const rootDir = process.cwd();
const BASE_URL = 'https://brightlane.github.io/skyscanner-flight-desk/';

const CITIES = ["London", "Paris", "New York", "Tokyo", "Dubai", "Singapore", "Rome", "Bangkok", "Istanbul", "Seoul"];
const FLIGHT_KEYS = ["cheap-flights-to-", "best-airfare-to-"];

async function runVultureEngine() {
    console.log("🚀 Starting Vulture Sync...");

    // TEMPLATE CHECK
    const requiredFiles = ['master-template.html', 'blog-template.html'];
    requiredFiles.forEach(file => {
        if (!fs.existsSync(file)) {
            console.error(`❌ ERROR: ${file} is missing from the root folder!`);
            process.exit(1);
        }
    });

    const template = fs.readFileSync('master-template.html', 'utf8');
    const blogTemplate = fs.readFileSync('blog-template.html', 'utf8');
    let sitemapEntries = [];

    // 1. GENERATE PAGES
    CITIES.forEach(city => {
        FLIGHT_KEYS.forEach(intent => {
            const slug = `${intent}${city.toLowerCase().replace(/ /g, '-')}.html`;
            const html = template
                .replace(/{{CITY}}/g, city)
                .replace(/{{DATE}}/g, new Date().toUTCString())
                .replace(/{{PRICE}}/g, `$${Math.floor(Math.random() * 300 + 200)}`);

            fs.writeFileSync(path.join(rootDir, slug), html);
            sitemapEntries.push(`${BASE_URL}${slug}`);
        });
    });

    // 2. GENERATE BLOG
    let blogPosts = '';
    CITIES.slice(0, 3).forEach(city => {
        blogPosts += `<div class="post"><h2>Audit: ${city}</h2><a href="cheap-flights-to-${city.toLowerCase()}.html">View</a></div>`;
    });
    const finalBlog = blogTemplate.replace(/{{BLOG_POSTS}}/g, blogPosts).replace(/{{DATE}}/g, new Date().toUTCString());
    fs.writeFileSync('blog.html', finalBlog);

    // 3. GENERATE SITEMAP (This creates the URL you need)
    let xml = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">`;
    xml += `\n  <url><loc>${BASE_URL}</loc><priority>1.0</priority></url>`;
    sitemapEntries.forEach(url => {
        xml += `\n  <url><loc>${url}</loc><priority>0.8</priority></url>`;
    });
    xml += `\n</urlset>`;
    fs.writeFileSync('sitemap.xml', xml);

    console.log("✅ Engine finished. Pages, Blog, and Sitemap created.");
}

runVultureEngine();
