// Configuration
const CONFIG = {
  webhookUrl: 'https://n8n.pkm365.com/webhook/content-publisher',
  pagesUrl: 'https://pkm365.github.io/pages',
  githubOwner: 'pkm365',
  githubRepo: 'pages'
};

// Category mapping
const CATEGORIES = {
  "AI & Machine Learning": ["ai", "attention", "dotproduct", "framework", "model", "llm", "transformer", "neural"],
  "Industrial & Business Strategy": ["platform", "teim", "root mode", "business"],
  "Project Management": ["qg", "ccpm", "quality", "simulation", "kanban"],
  "Health & Wellness": ["sleep", "tryptophan", "nutrition", "health"]
};

// Auto-detect title and category
function autoDetectMetadata(htmlContent) {
  const titleMatch = htmlContent.match(/<title>(.*?)<\/title>/i);
  const title = titleMatch ? titleMatch[1].trim() : '';

  let category = 'Other Topics';
  const lowerTitle = title.toLowerCase();
  for (const [cat, keywords] of Object.entries(CATEGORIES)) {
    if (keywords.some(keyword => lowerTitle.includes(keyword))) {
      category = cat;
      break;
    }
  }

  return { title, category };
}

// Show status message
function showStatus(type, message) {
  const status = document.getElementById('status');
  status.className = `status ${type}`;
  status.textContent = message;
  status.style.display = 'block';

  if (type === 'success') {
    setTimeout(() => {
      status.style.display = 'none';
    }, 5000);
  }
}

// Initialize on load
document.addEventListener('DOMContentLoaded', async function() {
  const fileNameInput = document.getElementById('fileName');
  const publishBtn = document.getElementById('publishBtn');
  const publishForm = document.getElementById('publishForm');

  // Get current tab and extract HTML
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  // Inject script to get HTML
  const results = await chrome.scripting.executeScript({
    target: { tabId: tab.id },
    func: () => document.documentElement.outerHTML
  });

  const htmlContent = results[0].result;

  // Auto-detect metadata
  const metadata = autoDetectMetadata(htmlContent);

  if (metadata.title) {
    document.getElementById('detectedTitle').textContent = metadata.title;
    document.getElementById('detectedCategory').textContent = metadata.category;
    document.getElementById('detected').style.display = 'block';

    // Auto-fill filename
    const autoFileName = metadata.title
      .replace(/[^a-zA-Z0-9\s\-_]/g, '')
      .replace(/\s+/g, '-')
      .toLowerCase()
      .substring(0, 50); // Limit length

    fileNameInput.value = autoFileName;
  }

  // Handle form submission
  publishForm.addEventListener('submit', async function(e) {
    e.preventDefault();

    const fileName = fileNameInput.value.trim();
    if (!fileName) {
      showStatus('error', '❌ Please enter a filename');
      return;
    }

    publishBtn.disabled = true;
    publishBtn.textContent = '⏳ Publishing...';
    showStatus('loading', 'Publishing content to N8N...');

    try {
      const data = {
        htmlContent: htmlContent,
        fileName: fileName + '.html'
      };

      const response = await fetch(CONFIG.webhookUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-Webhook-Source': 'browser-extension'
        },
        body: JSON.stringify(data)
      });

      const result = await response.json();

      if (result.success) {
        const pageUrl = `${CONFIG.pagesUrl}/content/${fileName}.html`;
        showStatus('success', `✅ Published! View at: ${pageUrl}`);
        publishBtn.textContent = '✅ Published!';

        // Copy URL to clipboard
        navigator.clipboard.writeText(pageUrl);

        setTimeout(() => {
          publishBtn.textContent = '🚀 Publish Content';
          publishBtn.disabled = false;
        }, 3000);
      } else {
        showStatus('error', `❌ Failed: ${result.error || result.message}`);
        publishBtn.textContent = '🚀 Publish Content';
        publishBtn.disabled = false;
      }
    } catch (error) {
      console.error('Publish error:', error);
      showStatus('error', `❌ Network error: ${error.message}`);
      publishBtn.textContent = '🚀 Publish Content';
      publishBtn.disabled = false;
    }
  });
});
