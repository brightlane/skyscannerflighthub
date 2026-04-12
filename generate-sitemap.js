const fs = require('fs');
const path = require('path');

const BASE_URL = 'https://brightlane.github.io/skyscanner-flight-desk/';
const rootDir = process.cwd();

function buildSitemap() {
    // 1. Find all generated HTML files (excluding system files)
    const files = fs.readdirSync(rootDir).filter(file => 
        file.endsWith('.html') && 
        !['master-template.html', '404.html', 'index.html'].includes(file)
    );

    let xml = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">`;
    
    // Add Homepage
    xml += `\n  <url>\n    <loc>${BASE_URL}</loc>\n    <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>\n    <changefreq>hourly</changefreq>\n    <priority>1.0</priority>\n  </url>`;

    // Add 10,000 sub-pages
    files.forEach(file => {
        xml += `\n  <url>\n    <loc>${BASE_URL}${file}</loc>\n    <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>\n    <changefreq>daily</changefreq>\n    <priority>0.8</priority>\n  </url>`;
    });

    xml += `\n</urlset>`;

    fs.writeFileSync(path.join(rootDir, 'sitemap.xml'), xml);
    console.log(`✅ Sitemap created with ${files.length + 1} URLs.`);
}

buildSitemap();
