const fs = require('fs');

async function run() {
    console.log("✈️ Vulture Hub: Building...");
    
    const baseUrl = 'https://brightlane.github.io/skyscannerflighthub/';
    const cities = ["London", "Paris", "New York", "Tokyo", "Dubai"];
    let sitemap = '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">';

    // Create a basic Homepage so the site "wakes up"
    const indexContent = `<html><body><h1>Skyscanner Flight Hub</h1><p>Active Routes: ${cities.length}</p><a href="sitemap.xml">Sitemap</a></body></html>`;
    fs.writeFileSync('index.html', indexContent);

    cities.forEach(city => {
        const slug = `cheap-flights-to-${city.toLowerCase()}.html`;
        const content = `<html><body><h1>Flights to ${city}</h1><a href="${baseUrl}">Back</a></body></html>`;
        fs.writeFileSync(slug, content);
        sitemap += `\n  <url><loc>${baseUrl}${slug}</loc></url>`;
    });

    sitemap += '\n</urlset>';
    fs.writeFileSync('sitemap.xml', sitemap);
    console.log("✅ index.html, sitemap.xml, and pages created.");
}

run();
