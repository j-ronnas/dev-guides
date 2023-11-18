#!/usr/bin/env python3
import os
import glob
import markdown

if not os.path.exists('docs'):
    os.mkdir('docs')

for f in glob.iglob('book/*.md'):
    with open(f, 'r') as file:
        raw = file.read()
        html = markdown.markdown(raw)

    file_name = os.path.basename(f)
    destination = os.path.join("docs", os.path.splitext(file_name)[0] + ".html")

    with open(destination, 'w') as file:
        file.write(r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>My Great Site</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
''')
        file.write(html)
        file.write(r'''
</body>
</html>''')