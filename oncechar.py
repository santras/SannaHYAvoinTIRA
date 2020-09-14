#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
from time import time

def count(ss):
    setti = list(set (ss))
    pituudet = {}
    for ii in range (len(setti)):
        pituudet[setti[ii]] = 0

    #print(pituudet)
    laskin = 1
    for ii in range(len(ss)):
        if ii == (len(ss)-1):
            #print('vika kierros')
            if pituudet[ss[ii]]<= laskin:
                    pituudet[ss[ii]] =laskin
        else:
            if ss[ii] == ss[ii+1]:
                laskin +=1
            else:
                #print(pituudet[ss[ii]])
                if pituudet[ss[ii]]<= laskin:
                    pituudet[ss[ii]] =laskin
                laskin = 1
        
    print(pituudet)
    


if __name__ == "__main__":
    #print(count("aaa")) # 6
    print(count("abbbcaa")) # 11
    #print(count("abcde")) # 5