# PHANTOM SCRAPER // HACKER EDITION

## Overview
A professional-grade web scraping application with a cyberpunk hacker aesthetic. Built with Python, Flask, and BeautifulSoup. Features advanced stealth mode, bot detection evasion, and a terminal-style interface.

## Project Structure
```
.
├── app.py                  # Flask web application with API endpoints
├── scraper/
│   ├── __init__.py         # Package exports
│   ├── config.py           # Stealth headers, user agents, detection patterns
│   └── core.py             # Advanced WebScraper class
├── templates/
│   └── index.html          # Cyberpunk web interface
├── static/
│   └── style.css           # Neon green hacker theme
├── beauty_soup.py          # BeautifulSoup example
├── regex_soup.py           # Regex parsing example
├── mech_soup.py            # MechanicalSoup example
├── main.py                 # CLI demo script
└── requirements.txt        # Dependencies
```

## Features

### Hacker-Level Capabilities
- **Stealth Mode**: Advanced headers mimicking real browsers (Sec-Fetch, Sec-Ch-Ua)
- **User-Agent Rotation**: 8 different browser identities including mobile
- **Referer Spoofing**: Randomized referrers from major search engines
- **Bot Detection Evasion**: Detects and warns about Cloudflare, CAPTCHA, rate limits
- **JavaScript/SPA Detection**: Identifies React, Angular, Vue, Next.js, Nuxt.js
- **Tech Stack Analysis**: Identifies server software, frameworks, CMS
- **Authentication Detection**: Warns when pages require login
- **Response Metrics**: Response time, content hash, content length

### Visual Interface
- **Cyberpunk Theme**: Neon green on dark with matrix grid effects
- **Scanline Animation**: CRT-style visual effects
- **Terminal Logging**: Live-style operation logs
- **Stats Dashboard**: Real-time extraction statistics
- **Export Options**: JSON and CSV data export

### API Endpoints
```
GET /api/scrape?url=<url>&stealth=true&deep_scan=false
GET /api/stats
GET /api/history?limit=10
```

## Running the Project
- The web interface runs on port 5000
- Visit the web preview to use the scraper
- Toggle options: Stealth Mode, Deep Scan, Extract Meta, Follow Links

## Dependencies
- Flask - Web framework
- BeautifulSoup4 - HTML parsing
- MechanicalSoup - Browser automation
- Requests - HTTP library
- lxml - Fast XML/HTML parser

## Environment Variables
- `SESSION_SECRET` - Flask session secret key
- `FLASK_DEBUG` - Set to 'true' for debug mode (default: false)

## Recent Changes
- November 27, 2025: HACKER EDITION upgrade
- Added cyberpunk/matrix-style UI with neon green theme
- Implemented advanced stealth mode with full browser headers
- Added bot protection detection (Cloudflare, CAPTCHA, rate limiting)
- Added JavaScript framework detection (React, Angular, Vue, etc.)
- Added tech stack identification and response metrics
- Added terminal-style operation logging
- Form toggles now control scraper behavior
