#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
from time import time


def count(ss):

    #print(pituudet)
    laskin = 1
    summa = 1                         # Ensimmäinen kirjain yksittäin laskettu mukaan
    for ii in range(1,len(ss)):
        if ss[ii] == ss[ii-1]:           # Onko edellinen sama
            laskin += 1                  
            summa += laskin
        else:
            summa += 1
            laskin =1
    return summa
    


if __name__ == "__main__":
    print(count("aaa")) # 6
    print(count("abbbcaa")) # 11
    print(count("abcde")) # 5