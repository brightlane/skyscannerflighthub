const fs = require('fs');
const path = require('path');

async function runVulture() {
    const baseUrl = 'https://brightlane.github.io/skyscanner-flight-desk/';
    const cities = ["London", "Paris", "New York", "Tokyo", "Dubai"];
    let sitemap = '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">';

    cities.forEach(city => {
        const slug = `cheap-flights-to-${city.toLowerCase()}.html`;
        const content = `<html><body><h1>Flights to ${city}</h1><p>Live Audit: ${new Date().toUTCString()}</p></body></html>`;
        fs.writeFileSync(slug, content);
        sitemap += `<url><loc>${baseUrl}${slug}</loc></url>`;
    });

    sitemap += '</urlset>';
    fs.writeFileSync('sitemap.xml', sitemap);
    console.log("✅ Build complete.");
}
runVulture();
