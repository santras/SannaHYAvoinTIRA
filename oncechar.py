#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
from time import time


def slowcount(ss):

    nn = len(ss)
    apu =

    for ii in range(nn):
        print('ii',ii)
        if ii != nn-1:
            if ss[ii] != ss [ii+1]:
                print(ii)
                continue
        for jj in range ():
            #print('jj',jj)

            #if ii != jj and ss[jj] !=ss[jj+1]:
            #    print('ei sama')
            #print(ss[ii:jj+1])
            #if ss[ii] != ss[jj]: #and ss[jj] == ss[jj-1]:
            #    print(ss[ii:jj])
            #else:
            #    print(ss[ii:jj])



def count(ss):
    setti = list(set (ss))
    pituudet = {}
    for ii in range (len(setti)):
        pituudet[setti[ii]] = 0

    #print(pituudet)
    laskin = 1
    summaus = 0
    for ii in range(len(ss)):
        if ii == (len(ss)-1):
            #print('vika kierros')
            if pituudet[ss[ii]]<= laskin:
                    pituudet[ss[ii]] =laskin
        else:
            if ss[ii] == ss[ii+1]:
                laskin +=1
                summaus = summaus + laskin 
            else:
                #print(pituudet[ss[ii]])
                if pituudet[ss[ii]]<= laskin:
                    pituudet[ss[ii]] =laskin
                laskin = 1
        
    print(pituudet)
    


if __name__ == "__main__":
    #print(count("aaa")) # 6
    print(slowcount("abbbcaa")) # 11
    #print(count("abcde")) # 5