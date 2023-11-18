#!/usr/bin/env python3
import os
import glob
import markdown

pages = {}
destination = "index.html"


def toHtmlPageName(mdname):
    return mdname.split(".")[0].split("/")[1] + ".html"


if not os.path.exists('public'):
    os.mkdir('public')

for f in glob.iglob('book/*.md'):
    with open(f, 'r') as file:
       title = file.readline()
       pages[title] = f

    
with open(os.path.join("public", destination), 'w') as file:
    file.write(r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>My Great Site</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
''')
    for p in pages:
        file.write("<a href=\""+ toHtmlPageName(pages[p]) + "\">" + p + "</a>")
    
    file.write(r'''
</body>
</html>''')