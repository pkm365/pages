# Publishing Bookmarklet

A simple bookmarklet to quickly publish HTML content from Claude Artifacts or Gemini Canvas to your GitHub Pages site.

## Installation

1. **Create a new bookmark** in your browser (Chrome, Firefox, Edge, Safari)
2. **Name it**: "Publish to PKM365" (or any name you prefer)
3. **Set the URL** to the following JavaScript code:

```javascript
javascript:(function(){const e=document.documentElement.outerHTML;const t=document.title||'untitled';const n=prompt('Enter filename (without .html):',t.replace(/[^a-zA-Z0-9\s\-_]/g,'').replace(/\s+/g,'-').toLowerCase());if(!n)return;const o={htmlContent:e,fileName:n+'.html'};fetch('https://n8n.pkm365.com/webhook/content-publisher',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(o)}).then(r=>r.json()).then(d=>{if(d.success){alert('✅ Published successfully!\n\nFile: '+n+'.html\n\nView at: https://pkm365.github.io/pages/content/'+n+'.html');}else{alert('❌ Publish failed: '+(d.error||d.message));}}).catch(err=>{alert('❌ Network error: '+err.message);});})();
```

## Alternative: Drag and Drop Installation

### Minified Bookmarklet (Copy this entire line)

```
javascript:(function(){const e=document.documentElement.outerHTML;const t=document.title||'untitled';const n=prompt('Enter filename (without .html):',t.replace(/[^a-zA-Z0-9\s\-_]/g,'').replace(/\s+/g,'-').toLowerCase());if(!n)return;const o={htmlContent:e,fileName:n+'.html'};fetch('https://n8n.pkm365.com/webhook/content-publisher',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(o)}).then(r=>r.json()).then(d=>{if(d.success){alert('✅ Published!\n\nFile: '+n+'.html\n\nView at: https://pkm365.github.io/pages/content/'+n+'.html');}else{alert('❌ Failed: '+(d.error||d.message));}}).catch(err=>{alert('❌ Error: '+err.message);});})();
```

## How to Use

### From Claude Artifacts:

1. Create your HTML in Claude Artifacts
2. Click the **bookmarklet** in your browser toolbar
3. Enter a filename (or use the auto-suggested name)
4. Click OK
5. Done! Your content is published

### From Gemini Canvas:

1. Create your HTML in Gemini Canvas
2. Click the **bookmarklet** in your browser toolbar
3. Enter a filename
4. Click OK
5. Done!

### From Any Web Page:

1. Navigate to any web page you want to publish
2. Click the bookmarklet
3. The entire page HTML will be captured and published
4. Enter filename and confirm

## What Happens When You Click?

The bookmarklet:
1. ✅ Captures the entire HTML of the current page
2. ✅ Extracts the page title
3. ✅ Prompts you for a filename (with auto-suggested name)
4. ✅ Sends content to N8N webhook
5. ✅ Shows success/error message
6. ✅ Provides direct link to published page

## Source Code (Readable Version)

For transparency, here's the un-minified source:

```javascript
(function() {
    // Get the entire HTML of current page
    const htmlContent = document.documentElement.outerHTML;

    // Get the page title for auto-naming
    const title = document.title || 'untitled';

    // Prompt for filename with auto-suggested name
    const fileName = prompt(
        'Enter filename (without .html):',
        title.replace(/[^a-zA-Z0-9\s\-_]/g, '').replace(/\s+/g, '-').toLowerCase()
    );

    if (!fileName) return; // User cancelled

    // Prepare data
    const data = {
        htmlContent: htmlContent,
        fileName: fileName + '.html'
    };

    // Send to N8N webhook
    fetch('https://n8n.pkm365.com/webhook/content-publisher', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        if (result.success) {
            alert('✅ Published successfully!\n\n' +
                  'File: ' + fileName + '.html\n\n' +
                  'View at: https://pkm365.github.io/pages/content/' + fileName + '.html');
        } else {
            alert('❌ Publish failed: ' + (result.error || result.message));
        }
    })
    .catch(error => {
        alert('❌ Network error: ' + error.message);
    });
})();
```

## Troubleshooting

### Bookmarklet doesn't work?

1. **Check if JavaScript is enabled** in your browser
2. **Check browser console** (F12) for errors
3. **Verify N8N webhook URL** is accessible: https://n8n.pkm365.com/webhook/content-publisher
4. **Try the web form instead**: https://pkm365.github.io/pages/publish.html

### Published page not showing?

1. Wait 1-2 minutes for GitHub Pages to build
2. Check the GitHub Actions tab for build status
3. Verify file was committed to the repository
4. Check the index page: https://pkm365.github.io/pages

## Advanced: Customization

To customize the bookmarklet for your own N8N instance:

1. Open the source code above
2. Replace `https://n8n.pkm365.com/webhook/content-publisher` with your webhook URL
3. Replace `https://pkm365.github.io/pages` with your GitHub Pages URL
4. Minify the code using a JavaScript minifier
5. Add `javascript:` prefix
6. Create bookmarklet with the minified code

## Security Note

The bookmarklet sends HTML content to your N8N webhook. Make sure:
- Your webhook is secured (use webhook secrets in production)
- You trust the content you're publishing
- You review the content before clicking the bookmarklet on untrusted pages

---

**Need help?** File an issue at: https://github.com/pkm365/pages/issues
