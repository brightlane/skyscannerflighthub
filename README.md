# ✈️ Skyscanner Flight Desk: Vulture 10K Engine

**Skyscanner Flight Desk** is a high-performance Programmatic SEO (pSEO) platform designed to dominate 2026 travel search rankings. Powered by the **Vulture 10,000 Protocol**, this repository automates the creation and maintenance of a massive fleet of high-intent landing pages targeting global flight hubs.

## 🚀 System Architecture

* **UI Framework:** Professional "Flight Desk" design language optimized for high-ticket conversion.
* **Expansion Logic:** Node.js powered `vulture-engine.js` multiplying 100+ core hubs into 10,000 keyword-targeted URLs.
* **The Heartbeat:** GitHub Actions workflow executing **hourly** freshness updates and price synchronization.
* **Indexing:** Automated `sitemap.xml` generation with dynamic internal linking to maximize crawl budget.

## 📂 Repository Structure

| File | Role |
| :--- | :--- |
| `index.html` | The "Power Hub" - passes link juice to the 10k fleet. |
| `master-template.html` | The HTML skeleton for all generated pages. |
| `vulture-engine.js` | The master script that spawns HTML, Sitemap, and Robots.txt. |
| `.nojekyll` | Disables Jekyll processing for raw HTML speed. |
| `.github/workflows/` | The engine room (Hourly Sync automation). |

## 🛠️ Deployment Instructions

### 1. Permissions (Crucial)
To allow the Vulture Engine to save generated files back to the repository:
1.  Go to **Settings > Actions > General**.
2.  Scroll to **Workflow permissions**.
3.  Select **"Read and write permissions"** and click **Save**.

### 2. Launching the Fleet
1.  Ensure `master-template.html` is configured with your affiliate ID (21885).
2.  Navigate to the **Actions** tab.
3.  Select **Vulture 10K Sync**.
4.  Click **Run workflow**.

## 📈 SEO & Affiliate Strategy

This project leverages **Long-Tail Keywords** specifically for the 2026 global travel market.
* **Targeting:** `cheap-flights-to-{{CITY}}`, `best-airfare-to-{{CITY}}`.
* **Affiliate:** Integrated Skyscanner logic via LinkConnector (Affiliate ID: 21885).
* **Freshness:** Every page is updated hourly with a live timestamp to satisfy the "Fresh Content" ranking signal.

---
*Maintained by the Vulture 10K Protocol.*
