#!/usr/bin/python2
import sys, os
if len(sys.argv) != 3:
    print "Uzycie: ./allConverter plikdoprzerobienia Autor--Tytul_piosenki"
    sys.exit(0)

os.system("./convert.py < " + sys.argv[1] + " > " + sys.argv[2])
os.system("./rename.py " + sys.argv[2])
