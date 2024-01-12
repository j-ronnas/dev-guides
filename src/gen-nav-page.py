#!/usr/bin/env python3
import os
import glob
import markdown
from template import header
from template import footer

pages = {}
destination = "index.html"

structure = {}

with open("docs/structure.txt", 'r') as file:
    line = file.readline()
    parts = line.split(',')
    structure[parts[0]] = parts[1]

print(structure)

def toHtmlPageName(mdname):
    return mdname.split(".")[0].split("/")[1] + ".html"


if not os.path.exists('docs'):
    os.mkdir('docs')

for f in glob.iglob('book/**/*.md', recursive = True):
    with open(f, 'r') as file:
       title = file.readline()
       file_name = os.path.basename(f)
       pages[title] =  os.path.splitext(file_name)[0]


with open(os.path.join("docs", destination), 'w') as file:
    file.write(header)
    for heading in structure.keys():
        file.write("<h3>" + heading + "</h3>")
        file.write("<a href=\""+ (structure[heading]) + '.html' + "\">" + structure[heading] + "</a>")

    file.write(footer)
