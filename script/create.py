#!/usr/bin/python2

import os

files = os.listdir('songs')

files.sort()
#tutaj mozna zrobic odpowiednie sortowanie files

out = open('spiewnik.tex', 'w')

out.write("""\\documentclass{book}
\\usepackage[chordbk]{songbook}
\\usepackage[T1]{polski}
\\usepackage[utf8]{inputenc}
\\usepackage{hyperref}

\\makeTitleContents
\\begin{document}

""")

for f in files:
    if not f.endswith(".txt"):
        continue
    g = open('songs/' + f, 'r')
    out.write(g.read())

out.write("""\\end{document}
""")

out.close()

os.system('pdflatex spiewnik.tex')
os.system('pdflatex toc.tex\n')

