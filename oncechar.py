#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
from time import time

def count(ss):
    setti = list(set (ss))
    pituudet = {}
    for ii in range (len(setti)):
        pituudet[setti[ii]] = 0

    print(pituudet)
    laskin = 1
    for ii in range(len(ss)):
        if ii == (len(ss)-1):
            #print('vika')
        else:

            if ss[ii] == ss[ii+1]:
                laskin +=1
                #print('kierros')
            else:
                print(pituudet[ss[ii]])
                #if pituudet[ii]<= laskin
                laskin = 1
        

    


if __name__ == "__main__":
    print(count("aaa")) # 6
    #print(count("abbbcaa")) # 11
    #print(count("abcde")) # 5