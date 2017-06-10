#!/usr/bin/env python
import sys
import re
import os

mac = []
wek = []
w_dir = "/home/lukassz/PycharmProjects/HadoopProjects/Matrix/zadanie/macierze/fr_w/"
m_dir = "/home/lukassz/PycharmProjects/HadoopProjects/Matrix/zadanie/macierze/fr_m/"
for filename in os.listdir(w_dir):
    if filename.endswith(".txt"): 
        f = open(w_dir+filename, 'r')
        for line in f:
            digit = re.search('[0-9]', line)
            if digit is not None:
                j, v = line.rstrip('\n').split(";")
                f1 = open(m_dir + "m" + j + ".txt")
                suma = 0
                for ln in f1:
                    i, j, k = ln.rstrip('\n').split(";")
                    print str(i) + "\t" + str(int(k) * int(v))
                f1.closed
                mac.append((j, suma))
        f.closed

