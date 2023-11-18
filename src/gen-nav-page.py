#!/usr/bin/env python3
import os
import glob
import markdown
from template import header
from template import footer

pages = {}
destination = "index.html"


def toHtmlPageName(mdname):
    return mdname.split(".")[0].split("/")[1] + ".html"


if not os.path.exists('docs'):
    os.mkdir('docs')

for f in glob.iglob('book/*.md'):
    with open(f, 'r') as file:
       title = file.readline()
       pages[title] = f

    
with open(os.path.join("docs", destination), 'w') as file:
    file.write(header)
    for p in pages:
        file.write("<a href=\""+ toHtmlPageName(pages[p]) + "\">" + p + "</a>")
    
    file.write(footer)