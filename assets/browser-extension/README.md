# PKM365 Publisher Browser Extension

A browser extension to quickly publish HTML content from Claude Artifacts, Gemini Canvas, or any web page to your GitHub Pages site.

## Features

- 📤 One-click publishing from any web page
- 🤖 Auto-detects page title and category
- 🎯 Auto-fills filename based on title
- ✨ Works with Claude Artifacts and Gemini Canvas
- 📋 Copies published URL to clipboard
- 🚀 Simple and lightweight

## Installation

### Chrome / Edge / Brave

1. Download this entire `browser-extension` folder
2. Open your browser and go to:
   - **Chrome**: `chrome://extensions/`
   - **Edge**: `edge://extensions/`
   - **Brave**: `brave://extensions/`

3. Enable **Developer mode** (toggle in top right)

4. Click **"Load unpacked"**

5. Select the `browser-extension` folder

6. The extension icon should appear in your toolbar!

### Firefox

1. Download this folder
2. Go to `about:debugging#/runtime/this-firefox`
3. Click **"Load Temporary Add-on"**
4. Select the `manifest.json` file from this folder

**Note**: Firefox requires signing for permanent installation. For temporary use, this method works fine.

## How to Use

### Method 1: From Claude Artifacts

1. Create your HTML page in Claude Artifacts
2. Click the **PKM365 Publisher** extension icon
3. Review the auto-detected title and category
4. Modify filename if needed
5. Click **"Publish Content"**
6. Done! The URL is copied to your clipboard

### Method 2: From Gemini Canvas

1. Create your HTML page in Gemini Canvas
2. Click the extension icon
3. Enter filename (auto-suggested from title)
4. Click "Publish"
5. Done!

### Method 3: From Any Web Page

1. Navigate to any page you want to publish
2. Click the extension icon
3. The entire page HTML will be captured
4. Enter filename and publish

## What Happens When You Publish?

1. ✅ Extension captures the current page HTML
2. ✅ Auto-detects the page title
3. ✅ Categorizes based on keywords
4. ✅ Sends to N8N webhook
5. ✅ N8N commits to GitHub repository
6. ✅ GitHub Actions regenerates navigation
7. ✅ Content appears on GitHub Pages (1-2 minutes)
8. ✅ URL copied to clipboard

## Configuration

By default, the extension is configured for:
- **N8N Webhook**: `https://n8n.pkm365.com/webhook/content-publisher`
- **GitHub Pages**: `https://pkm365.github.io/pages`
- **GitHub Repo**: `pkm365/pages`

To customize for your own setup:
1. Open `popup.js`
2. Modify the `CONFIG` object:
```javascript
const CONFIG = {
  webhookUrl: 'YOUR_N8N_WEBHOOK_URL',
  pagesUrl: 'YOUR_GITHUB_PAGES_URL',
  githubOwner: 'YOUR_GITHUB_USERNAME',
  githubRepo: 'YOUR_REPO_NAME'
};
```
3. Reload the extension

## Icons

The extension requires icon files. Create simple icons or use placeholders:

- `icon16.png` (16x16px)
- `icon48.png` (48x48px)
- `icon128.png` (128x128px)

You can use any image editor or online icon generator to create these.

**Quick placeholder icons**: Use emoji-to-png generators with the 📤 emoji.

## Permissions Explained

- **activeTab**: To read the HTML content of the current tab
- **clipboardWrite**: To copy the published URL to clipboard
- **host_permissions (n8n.pkm365.com)**: To send content to your N8N webhook

## Troubleshooting

### Extension not working?

1. Check browser console (F12) for errors
2. Verify N8N webhook is accessible
3. Check permissions in extension settings
4. Try reloading the extension

### Content not publishing?

1. Check network tab for failed requests
2. Verify webhook URL is correct
3. Test with the web form: https://pkm365.github.io/pages/publish.html
4. Check N8N workflow is running

### Published page not showing?

1. Wait 1-2 minutes for GitHub Actions
2. Check GitHub Actions tab for build status
3. Verify file was committed to repository
4. Check the index: https://pkm365.github.io/pages

## Privacy

- Extension only runs when you click it
- No background processes or tracking
- Only sends data to your configured N8N webhook
- No data collected or stored

## Development

To modify the extension:

1. Edit the files (`popup.html`, `popup.js`, `manifest.json`)
2. Go to extensions page
3. Click "Reload" on the PKM365 Publisher extension
4. Test your changes

## Publishing to Chrome Web Store (Optional)

To publish this extension publicly:

1. Create a developer account at [Chrome Web Store](https://chrome.google.com/webstore/devconsole)
2. Add proper icons (required)
3. Add screenshots
4. Fill in store listing details
5. Submit for review

## License

MIT License - See main repository LICENSE file

## Support

Issues? File at: https://github.com/pkm365/pages/issues
