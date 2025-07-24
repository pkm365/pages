import os
import re
import datetime
import html

# --- Configuration ---

# Root directory is the script's directory
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Output file for the navigation page
OUTPUT_FILE = os.path.join(ROOT_DIR, "index.html")

# Files to exclude from the navigation page
EXCLUDE_FILES = {
    "index.html",
    "LICENSE",
    ".gitignore",
    "publish.html",  # 发布表单页面，通过按钮访问，不在导航中显示
}

# Regex to extract the <title> tag content
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.IGNORECASE)

# --- Categorization Logic ---

# Define categories and their associated keywords (case-insensitive)
CATEGORIES = {
    "AI & Machine Learning": ["ai", "attention", "dotproduct", "framework", "model", "llm", "transformer", "neural", "智能"],
    "Industrial & Business Strategy": ["工业", "企业", "组织", "模式", "转型", "platform", "teim", "root mode", "商业", "业务"],
    "Project Management": ["项目", "qg", "ccpm", "质量", "simulation", "管理", "交付"],
    "Health & Wellness": ["睡眠", "tryptophan", "食物", "健康", "营养"],
}
UNCATEGORIZED_LABEL = "Other Topics"

def get_category(title: str) -> str:
    """Assigns a category to a file based on its title."""
    lower_title = title.lower()
    for category, keywords in CATEGORIES.items():
        if any(keyword in lower_title for keyword in keywords):
            return category
    return UNCATEGORIZED_LABEL

# --- Core Functions ---

def extract_title(file_path: str) -> str:
    """Extracts the <title> content from an HTML file, falling back to the filename."""
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            match = TITLE_RE.search(content)
            if match:
                return match.group(1).strip()
    except FileNotFoundError:
        pass
    return os.path.splitext(os.path.basename(file_path))[0]

def generate_navigation_page():
    """Scans for HTML files, categorizes them, and generates a new navigation page."""
    print("Starting navigation page generation...")
    
    # 1. Collect and categorize all HTML files
    categorized_files = {category: [] for category in CATEGORIES}
    categorized_files[UNCATEGORIZED_LABEL] = []

    for filename in os.listdir(ROOT_DIR):
        if filename.endswith('.html') and filename not in EXCLUDE_FILES:
            file_path = os.path.join(ROOT_DIR, filename)
            mtime = os.path.getmtime(file_path)
            title = extract_title(file_path)
            category = get_category(title)
            
            file_info = {
                'path': filename,
                'title': title,
                'mtime': mtime,
                'date': datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')
            }
            categorized_files[category].append(file_info)

    # Sort files within each category by modification time (newest first)
    for category in categorized_files:
        categorized_files[category].sort(key=lambda x: x['mtime'], reverse=True)

    # 2. Generate the HTML content
    html_content = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI 学习笔记导航</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        .card-hover-effect {
            transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
        }
        .card-hover-effect:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        }
        .category-title {
            font-size: 1.75rem;
            font-weight: 700;
            color: #1e3a8a; /* Dark Blue */
            padding-bottom: 0.5rem;
            border-bottom: 3px solid #3b82f6; /* Lighter Blue */
            margin-bottom: 2rem;
        }
    </style>
</head>
<body class="bg-slate-50 min-h-screen">
    <header class="bg-gradient-to-r from-blue-600 to-indigo-700 text-white shadow-lg">
        <div class="container mx-auto px-4 py-12 text-center">
            <h1 class="text-4xl md:text-5xl font-bold">AI 学习笔记导航</h1>
            <p class="mt-4 text-lg opacity-90">探索人工智能、项目管理和技术洞察的知识库</p>
        </div>
    </header>

    <!-- Quick Publish Section -->
    <div class="bg-gradient-to-r from-green-500 to-blue-500 py-6">
        <div class="container mx-auto px-4 text-center">
            <a href="publish.html" class="inline-flex items-center bg-white text-gray-800 font-bold py-3 px-6 rounded-full shadow-lg hover:shadow-xl transform hover:scale-105 transition-all duration-200">
                <span class="text-2xl mr-2">✍️</span>
                <span>发布新内容</span>
                <span class="text-xl ml-2">→</span>
            </a>
            <p class="text-white text-sm mt-2 opacity-90">快速发布HTML内容到GitHub Pages</p>
        </div>
    </div>

    <main class="container mx-auto px-4 py-10 space-y-12">
'''

    # Define the order of categories to display
    category_order = list(CATEGORIES.keys()) + [UNCATEGORIZED_LABEL]

    for category in category_order:
        files = categorized_files[category]
        if not files:
            continue

        html_content += f'''
        <section>
            <h2 class="category-title">{html.escape(category)}</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
'''
        for file_info in files:
            html_content += f'''
                <a href="{html.escape(file_info['path'])}" class="block bg-white rounded-lg p-6 card-hover-effect border border-slate-200">
                    <div class="flex justify-between items-start mb-4">
                        <span class="text-2xl">📄</span>
                        <span class="text-xs font-semibold bg-slate-200 text-slate-600 px-2 py-1 rounded-full">{file_info['date']}</span>
                    </div>
                    <h3 class="text-xl font-bold text-slate-800 mb-2">{html.escape(file_info['title'])}</h3>
                    <p class="text-blue-600 font-semibold text-sm">查看详情 &rarr;</p>
                </a>'''
        
        html_content += '''
            </div>
        </section>
'''

    html_content += '''
    </main>

    <footer class="text-center py-6 mt-8">
        <p class="text-sm text-slate-500">由 generate_nav.py 自动生成</p>
    </footer>
</body>
</html>'''

    # 3. Write the new HTML to the output file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Successfully generated navigation page at: {OUTPUT_FILE}")


if __name__ == "__main__":
    generate_navigation_page() 