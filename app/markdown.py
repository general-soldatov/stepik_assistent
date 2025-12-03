import re

def markdown_to_html(markdown: str):
    # Преобразование заголовков
    html = re.sub(r'^(#{1,6})\s*(.*?)\s*#*$', lambda m: f"<h{len(m.group(1))}>{m.group(2)}</h{len(m.group(1))}>", markdown, flags=re.MULTILINE)
    html = re.sub(r'  ', r'\n', html, flags=re.MULTILINE)

    # Преобразуем маркированные списки
    html = re.sub(r'^\* (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    html = re.sub(r'(<li>.+</li>)', r'<ul>\1</ul>', html, flags=re.DOTALL)

    # Замена изображения на img элемент
    html = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1">', html)

    # Преобразуем блоки кода
    html = re.sub(r'```math\n(.*?)\n```', r'<span class="math-tex">\(\1\)</span>', html, flags=re.DOTALL)
    html = re.sub(r'```(.*?)\n(.*?)\n```', r'<pre><code class="language-\1">\2</code></pre>', html, flags=re.DOTALL)

    # Преобразуем ссылки
    html = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', html)

    # Преобразуем блоки цитат
    html = re.sub(r'^>(.+)$', r'<blockquote><p>\1</p></blockquote>', html, flags=re.MULTILINE)

    # Выделить жирным курсивом (три звезды)
    html = re.sub(r'\*\*\*([^*]+)\*\*\*', r'<strong><em>\1</em></strong>', html)

    # Выделить жирным (две звезды)
    html = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', html)

    # Выделить курсивом (одна звезда)
    html = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', html)

    # Оформление элемента кода (обратные апострофы)
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)

    # Преобразование параграфов
    html = re.sub(r'^(?!<h|<ul|<ol|<li|<pre|<blockquote|<table|<tr|<td)(.*?)$', r'<p>\1</p>', html, flags=re.MULTILINE)

    # Преобразование нумерованных списков
    html = re.sub(r'<p>\d+\.\s*(.*)</p>', r'<li>\1</li>', html, flags=re.MULTILINE)
    html = re.sub(r'</p>\n<li>', r'</p>\n<ol>\n<li>', html, flags=re.MULTILINE)
    html = re.sub(r'</li>\n<p>', r'</li></ol>\n<p>', html, flags=re.MULTILINE)

    return html
