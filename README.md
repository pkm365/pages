# PKM365 Knowledge Base

Personal knowledge management site with automated content publishing, hosted on GitHub Pages.

**Live Site:** https://pkm365.github.io/pages

## Overview

This repository serves as a dynamic knowledge base for AI learning notes, technical documentation, project management insights, and various technical topics. Content is automatically organized and published through multiple channels.

## Features

- **Automated Navigation Generation**: Python script automatically categorizes and indexes content
- **Multiple Publishing Methods**:
  - Direct Git commits
  - N8N webhook automation
  - Browser bookmarklet (one-click from Claude Artifacts/Gemini Canvas)
  - Browser extension
- **Auto-categorization**: Content automatically organized by keywords
- **GitHub Pages Hosting**: Automatic deployment via GitHub Actions
- **Responsive Design**: Mobile-first design with Tailwind CSS

## Repository Structure

```
/home/user/pages/
├── content/              # All HTML content files
├── assets/              # Static assets
│   ├── css/            # Custom stylesheets
│   ├── js/             # Custom scripts
│   └── images/         # Images, icons
├── scripts/            # Automation scripts
│   ├── generate_nav.py
│   └── update_and_push.bat
├── workflows/          # N8N workflow definitions
│   ├── content_publish.json
│   └── content_publish_fixed.json
├── docs/               # Documentation
├── .github/            # GitHub Actions workflows
├── config.json         # Configuration file
├── index.html          # Auto-generated navigation page
└── publish.html        # Publishing form
```

## Content Categories

Content is automatically categorized based on keywords:

- **AI & Machine Learning**: AI, attention, dotproduct, framework, model, LLM, transformer
- **Industrial & Business Strategy**: Platform, TEIM, root mode, business operations
- **Project Management**: CCPM, QG, quality-kanban, simulation, delivery
- **Health & Wellness**: Sleep, tryptophan, nutrition, health
- **Other Topics**: Uncategorized content

## Publishing Content

### Method 1: Direct Git Workflow

```bash
# 1. Add your HTML file to content/ directory
cp your-file.html content/

# 2. Generate navigation
python scripts/generate_nav.py

# 3. Commit and push
git add .
git commit -m "Add new content"
git push origin main
```

### Method 2: N8N Webhook

POST to `https://n8n.pkm365.com/webhook/content-publisher` with:

```json
{
  "htmlContent": "<html>...</html>",
  "fileName": "your-file.html"
}
```

The workflow automatically:
1. Receives the content
2. Commits to GitHub
3. Triggers navigation regeneration
4. Deploys to GitHub Pages

### Method 3: Browser Bookmarklet (Recommended for Claude Artifacts/Gemini Canvas)

1. Drag the bookmarklet to your browser's bookmark bar
2. Open Claude Artifacts or Gemini Canvas with your HTML
3. Click the bookmarklet
4. Content is automatically published!

See [Publishing Guide](docs/PUBLISHING.md) for detailed instructions.

### Method 4: Browser Extension

Install the browser extension for seamless publishing from any webpage.

## Local Development

### Prerequisites

- Python 3.x
- Git

### Setup

1. Clone the repository:
```bash
git clone https://github.com/pkm365/pages.git
cd pages
```

2. Generate navigation:
```bash
python scripts/generate_nav.py
```

3. Open `index.html` in your browser to view locally

### Testing

```bash
# Generate navigation and verify
python scripts/generate_nav.py
python -m http.server 8000

# Visit http://localhost:8000
```

## CI/CD Pipeline

GitHub Actions automatically:

1. **On Push to Main**:
   - Checkout repository
   - Setup Python 3.x
   - Run `scripts/generate_nav.py`
   - Deploy to GitHub Pages

2. **Manual Dispatch**: Can be triggered manually from GitHub Actions tab

## Configuration

### config.json

```json
{
  "webhookUrl": "https://n8n.pkm365.com/webhook/content-publisher",
  "githubOwner": "pkm365",
  "githubRepo": "pages",
  "pagesUrl": "https://pkm365.github.io/pages",
  "maxFileSize": 1024,
  "maxRequestsPerHour": 50,
  "version": "2.0-mvp",
  "paths": {
    "content": "content",
    "assets": "assets",
    "scripts": "scripts",
    "workflows": "workflows",
    "docs": "docs"
  }
}
```

## Technology Stack

- **Frontend**: HTML5, Tailwind CSS, Chart.js
- **Backend**: Python 3.x
- **Automation**: N8N, GitHub Actions
- **Hosting**: GitHub Pages
- **Version Control**: Git

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - See [LICENSE](LICENSE) file for details

## Version

Current version: **2.0-mvp**

## Support

For issues or questions:
- GitHub Issues: https://github.com/pkm365/pages/issues
- N8N Instance: https://n8n.pkm365.com

## Roadmap

- [ ] Enable security features (webhook secret, rate limiting)
- [ ] Add search functionality
- [ ] Implement dark mode
- [ ] Add analytics
- [ ] Create content templates
- [ ] Enhance categorization with metadata

---

Generated with automated tooling. Last updated: 2025-10-22
