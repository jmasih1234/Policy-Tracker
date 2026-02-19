# Policy-Tracker

This project is a policy tracker for countries across the world, including both hemispheres. It covers foreign and domestic agendas for each country, including the greater continental USA.

## Live Preview (local server)

No installation required — just Python 3 (pre-installed on most systems):

```bash
# From the repository root:
python3 -m http.server 8080
```

Then open **http://localhost:8080** in your browser.

If you prefer Node.js:

```bash
npx serve .
```

### Features
- 🔍 Full-text search across country, policy name, and description
- 🏷️ Filter by policy type (Foreign, Domestic, Trade, Climate, Defense, Health)
- 🌐 Filter by region and status
- ↕️ Click any column header to sort
- 📊 Live summary stats (total policies, countries, active, proposed)
