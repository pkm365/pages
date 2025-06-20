import os
import re
import datetime
import html

# 根目录为当前脚本所在目录
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# 导航页输出文件名
OUTPUT = os.path.join(ROOT_DIR, "index.html")

# 需要排除的文件（不会出现在导航页中）
EXCLUDE = {
    "index.html",
    "articles.html",
    "LICENSE",
    ".gitignore",
}

# <title> 提取正则
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.IGNORECASE)


def extract_title(file_path: str) -> str:
    """从 HTML 文件读取 <title> 标签内容；若不存在则使用文件名。"""
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                match = TITLE_RE.search(line)
                if match:
                    return match.group(1).strip()
    except FileNotFoundError:
        pass
    # 回退：使用文件名去掉扩展名
    return os.path.splitext(os.path.basename(file_path))[0]


def generate_navigation():
    """生成导航页 HTML。"""
    # 收集所有 HTML 文件
    html_files = []
    for file in os.listdir(ROOT_DIR):
        if file.endswith('.html') and file not in EXCLUDE:
            file_path = os.path.join(ROOT_DIR, file)
            mtime = os.path.getmtime(file_path)
            title = extract_title(file_path)
            html_files.append({
                'path': file,
                'title': title,
                'mtime': mtime,
                'date': datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')
            })
    
    # 按修改时间倒序排序
    html_files.sort(key=lambda x: x['mtime'], reverse=True)
    
    # 生成 HTML
    nav_html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI 学习笔记导航</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 min-h-screen">
    <div class="container mx-auto px-4 py-8">
        <h1 class="text-3xl font-bold mb-8 text-center text-gray-800">AI 学习笔记导航</h1>
        <div class="bg-white rounded-lg shadow-lg p-6">
            <div class="grid grid-cols-1 gap-4">"""
    
    for file in html_files:
        nav_html += f"""
                <a href="{html.escape(file['path'])}" class="p-4 border rounded hover:bg-gray-50 transition-colors">
                    <div class="flex justify-between items-center">
                        <h2 class="text-lg font-semibold text-gray-800">{html.escape(file['title'])}</h2>
                        <span class="text-sm text-gray-500">{file['date']}</span>
                    </div>
                </a>"""
    
    nav_html += """
            </div>
        </div>
    </div>
</body>
</html>"""
    
    # 写入文件
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(nav_html)


if __name__ == "__main__":
    generate_navigation() 