#!/usr/bin/python2
# -*- coding: utf-8 -*-
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
#potrzebne do wygenerowania spiewnik.toc

out = open("all.tex", "w")
out.write("""\\documentclass{book}
\\usepackage[chordbk]{songbook}
\\usepackage[T1]{polski}
\\usepackage[utf8]{inputenc}
\\usepackage{hyperref}
\\usepackage{latexsym,fancyhdr}

\\makeTitleContents
\\begin{document}

""")

for f in files:
    if not f.endswith(".txt"):
        continue
    g = open('songs/' + f, 'r')
    out.write(g.read())
out.write("""\\newcommand{\\RelDate}{29 marca 2013}
\\newcommand{\\RevDate}{\\today}

\\font\\myTinySF=cmss8    at  8pt
\\font\\myHugeSF=cmssbx10 at 25pt
\\renewcommand{\\CpyRtInfoFont}{\\tiny\\myTinySF}
\\newcommand{\\myTitleFont}{\\Huge\\myHugeSF}
\\newcommand{\\mySubTitleFont}{\\large\\sf}
%%%
% Define fonts to use in the headers and footers of the songbook.
%%%
\\newcommand{\\LHeadFont}{\\normalsize}            % = cmr12  at 12pt
\\newcommand{\\CHeadFont}{\\normalsize\\rm}         % = cmr12  at 12pt
\\newcommand{\\RHeadFont}{\\normalsize}            % = cmr12  at 12pt
\\newcommand{\\LFootFont}{\\scriptsize}            % = cmr8   at  8pt
\\newcommand{\\CFootFont}{\\tiny\\myTinySF}         % = cmss8  at  8pt
\\newcommand{\\RFootFont}{\\scriptsize}            % = cmr8   at  8pt

%%%
% Turn on and define fancy page heading/footing definition.
%%%
\\pagestyle{fancy}

\\addtolength{\\headwidth}{\\marginparsep}
\\addtolength{\\headwidth}{\\marginparwidth}
\\renewcommand{\\footrulewidth}{0.4pt}
\\lhead{\\LHeadFont Śpiewnik}
       \\chead{\\CHeadFont Spis treści}
       \\rhead{\\RHeadFont\\RelDate}

       \\cfoot{\\CFootFont Skompilowano:  \\RevDate}
       \\rfoot{\\RFootFont Sygi}

%%%
% Index entries command definition.
%%%
\\renewcommand{\\item}{\\par\\hangindent=40pt}
\\renewcommand{\\subitem}{\\par\\hangindent=40pt \\hspace*{20pt}}
\\renewcommand{\\subsubitem}{\\par\\hangindent=40pt \\hspace*{30pt}}

%%%
% Begin the Table Of Contents.
%%%
{\\parindent 10pt
  {\\myTitleFont --- Indeks ---}}\\par
\\vskip 30pt

\\input{spiewnik.toc}

\\end{document}
\\bye
""")
out.close()
os.system('pdflatex all.tex')
