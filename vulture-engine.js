const fs = require('fs');

async function run() {
    console.log("✈️ Vulture Test Run Starting...");
    
    const baseUrl = 'https://brightlane.github.io/skyscanner-flight-desk/';
    const cities = ["london", "paris", "new-york"];
    let sitemap = '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">';

    cities.forEach(city => {
        const fileName = `cheap-flights-to-${city}.html`;
        const content = `<html><body><h1>Flights to ${city}</h1><p>Updated: ${new Date().toISOString()}</p></body></html>`;
        fs.writeFileSync(fileName, content);
        sitemap += `<url><loc>${baseUrl}${fileName}</loc></url>`;
    });

    sitemap += '</urlset>';
    fs.writeFileSync('sitemap.xml', sitemap);
    console.log("✅ Created 3 pages and sitemap.xml");
}

run();
