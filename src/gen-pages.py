#!/usr/bin/env python3
import os
import glob
import markdown
from template import header
from template import footer

if not os.path.exists('docs'):
    os.mkdir('docs')

for f in glob.iglob('book/**/*.md', recursive = True):
    with open(f, 'r') as file:
        raw = file.read()
        html = markdown.markdown(raw, extensions=['fenced_code'])

    file_name = os.path.basename(f)
    destination = os.path.join("docs", os.path.splitext(file_name)[0] + ".html")

    with open(destination, 'w') as file:
        file.write(header)
        file.write(r'''<div class="guide">''')
        file.write(html)
        file.write(r'''</div>''')
        file.write(footer)