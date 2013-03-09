#!/usr/bin/python2
#format pliku do przetworzenia: kolejne linie - kolejne wiersze piosenki, poczatek zwrotki - linia z 'svv', poczatek refrenu: 'srr'. Akordy na koncu linii oznaczone xch
import re
print """\\renewcommand{\SBChordRaise}{0ex}
\\begin{song}{Tytul}{Autor}



"""

openedVerse = False
openedRef = False

while(True):
    try:
        line = raw_input()
        line = re.sub('xch', '\\hfill \\Ch{}{} \\hspace{20mm}', line)
        if (line == "svv"): #StartVerse
            if (openedVerse):
                print "\\end{SBVerse}"
                openedVerse = False
            if (openedRef):
                print "\\end{SBOpGroup}"
                openedRef = False
            line = "\\begin{SBVerse}"
            openedVerse = True
        if (line == "srr"):
            if (openedVerse):
                print "\\end{SBVerse}"
                openedVerse = False
            if (openedRef):
                print "\\end{SBOpGroup}"
                openedRef = False
            line = "\\begin{SBOpGroup}"
            openedRef = True
    except EOFError:
        break
    print line + '\n'

if (openedVerse):
    print "\\end{SBVerse}"
if (openedRef):
    print "\\end{SBOpGroup}"

print "\\end{song}"
