#!/usr/bin/python2

import os

files = os.listdir('songs')

out = open('spiewnik.tex', 'w')

out.write("""\\documentclass{book}
\\usepackage[chordbk]{songbook}
\\usepackage[T1]{polski}
\\usepackage[utf8]{inputenc}

\\makeTitleContents
\\begin{document}

""")

for f in files:
    if not os.path.isfile('songs/' + f):
        continue
    g = open('songs/' + f, 'r')
    out.write(g.read())

out.write("""\\end{document}
""")

out.close()

os.system('pdflatex spiewnik.tex')
os.system('pdflatex toc.tex\n')

