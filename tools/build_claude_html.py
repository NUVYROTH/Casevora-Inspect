"""把 index.html 轉成 claude.ai 版要發布的檔案（去掉外層 <html><head><body>）。

用法：python3 tools/build_claude_html.py 輸出路徑.html
"""
import re
import sys

s = open('index.html', encoding='utf-8').read()
s = re.sub(r'^\s*<!DOCTYPE html>\s*<html[^>]*>\s*<head>\s*', '', s, flags=re.I)
s = re.sub(r'<meta charset="utf-8">\s*', '', s, count=1, flags=re.I)
s = re.sub(r'<meta name="viewport"[^>]*>\s*', '', s, count=1)
s = s.replace('</head>', '', 1)
s = re.sub(r'<body[^>]*>', '', s, count=1)
s = re.sub(r'</body>\s*</html>\s*$', '', s.strip())
open(sys.argv[1], 'w', encoding='utf-8').write(s)
