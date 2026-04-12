const fs = require('fs');
const path = require('path');

const rootDir = process.cwd();
const BASE_URL = 'https://brightlane.github.io/skyscanner-flight-desk/';

// Minimal city list for testing to ensure it goes green
const CITIES = ["London", "Paris", "New York", "Tokyo", "Dubai"];
const FLIGHT_KEYS = ["cheap-flights-to-"];

async function runVultureEngine() {
    console.log("🚀 Vulture Sync Starting...");
    
    // Check for templates
    if (!fs.existsSync('master-template.html') || !fs.existsSync('blog-template.html')) {
        console.error("❌ Templates missing. Upload master-template.html and blog-template.html");
        process.exit(1);
    }

    const template = fs.readFileSync('master-template.html', 'utf8');
    const blogTemplate = fs.readFileSync('blog-template.html', 'utf8');
    let sitemapEntries = [];

    CITIES.forEach(city => {
        FLIGHT_KEYS.forEach(intent => {
            const filename = `${intent}${city.toLowerCase()}.html`;
            const html = template.replace(/{{CITY}}/g, city).replace(/{{DATE}}/g, new Date().toUTCString());
            fs.writeFileSync(path.join(rootDir, filename), html);
            sitemapEntries.push(`${BASE_URL}${filename}`);
        });
    });

    // Sitemap Generation
    let xml = `<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">`;
    sitemapEntries.forEach(url => { xml += `<url><loc>${url}</loc></url>`; });
    xml += `</urlset>`;
    fs.writeFileSync('sitemap.xml', xml);

    console.log("✅ Sitemap and pages generated.");
}
runVultureEngine();
