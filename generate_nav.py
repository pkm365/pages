import os
import re
import datetime
import html

# 根目录为当前脚本所在目录
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# 导航页输出文件名
OUTPUT = os.path.join(ROOT_DIR, "articles.html")

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


def collect_pages():
    """收集根目录下所有 HTML 页面（排除列表除外），并返回 (mtime, filename, title) 列表"""
    pages = []
    for fn in os.listdir(ROOT_DIR):
        if not fn.lower().endswith(".html"):
            continue
        if fn in EXCLUDE:
            continue
        full_path = os.path.join(ROOT_DIR, fn)
        if not os.path.isfile(full_path):
            continue
        mtime = os.path.getmtime(full_path)
        title = extract_title(full_path)
        pages.append((mtime, fn, title))
    # 按最后修改时间倒序
    pages.sort(key=lambda x: x[0], reverse=True)
    return pages


def build_html(pages):
    """根据页面信息拼装导航页 HTML 文本"""
    rows = []
    for ts, fn, title in pages:
        date_str = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
        rows.append(
            f"            <tr>\n"
            f"                <td class=\"px-4 py-2 text-gray-600\">{date_str}</td>\n"
            f"                <td class=\"px-4 py-2\"><a class=\"text-blue-700 underline\" href=\"{html.escape(fn)}\" target=\"_blank\">{html.escape(title)}</a></td>\n"
            f"            </tr>"
        )

    rows_html = "\n".join(rows)

    return f"""<!DOCTYPE html>
<html lang=\"zh-CN\">
<head>
    <meta charset=\"UTF-8\">
    <title>文章列表 | AI Demo Pages</title>
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
    <script src=\"https://cdn.tailwindcss.com\"></script>
</head>
<body class=\"bg-slate-100 min-h-screen flex flex-col\">
    <header class=\"bg-gradient-to-r from-blue-600 to-indigo-600 text-white py-6 shadow-md\">
        <h1 class=\"text-3xl font-bold text-center\">文章列表</h1>
    </header>

    <main class=\"flex-1 container mx-auto px-4 py-8\">
        <table class=\"w-full bg-white shadow-md rounded-lg overflow-hidden\">
            <thead class=\"bg-slate-50\">
                <tr>
                    <th class=\"px-4 py-2 text-left text-gray-700\">日期</th>
                    <th class=\"px-4 py-2 text-left text-gray-700\">标题</th>
                </tr>
            </thead>
            <tbody>
{rows_html}
            </tbody>
        </table>
    </main>

    <footer class=\"text-center text-sm text-gray-500 py-4\">
        自动生成 · 运行 <code>python generate_nav.py</code> 刷新
    </footer>
</body>
</html>"""


def main():
    pages = collect_pages()
    html_content = build_html(pages)
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"[OK] 已更新 {OUTPUT}，共 {len(pages)} 篇文章。")


if __name__ == "__main__":
    main() 