#!/usr/bin/python2
import sys, os, re
if len(sys.argv) != 2:
    print "Uzycie: ./rename nazwa_pliku"
    sys.exit(0)

f = open(sys.argv[1], 'r')
g = open(sys.argv[1] + '.txt', 'w')
name = os.path.basename(sys.argv[1])

(autor, tytul) = name.split('--')
autor = re.sub('_', ' ', autor)
tytul = re.sub('_', ' ', tytul)

for line in f.readlines():
    if (line.find('\\begin{song}') != -1):
        line = re.sub('Autor', autor, line)
        line = re.sub('Tytul', tytul, line)
    g.write(line)
