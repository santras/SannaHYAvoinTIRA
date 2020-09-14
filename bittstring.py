#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#import sys
#from time import time


def calculate(ss):

    #  Jotta olisi vuoroin 0 ja 1 voi olla joko 0101... tai 1010...
    alkaa_nollasta = 0  # parilliset indeksit 0:aa [0,2,4...], parittomat 1:stä [1,3,5 ...]
    alkaa_ykkosesta = 0  # parittomat indeksit 0:aa [1,3,5...], parilliset 1:stä [0,2,4...]
                         
    for ii in range(len(ss)):
        #print('ii,luku',ii, ss[ii],ii%2)
        if ii%2 == 0:   # parilliset indeksit
            #print('parillinen indeksi')
            if ss[ii] == '0':         
                alkaa_ykkosesta += 1
                #print('alkaa_ykkosesta muuttuu')
            else:                   # parillinen =0
                alkaa_nollasta += 1
                #print('alkaa_nollasta muuttuu')
        else:           # parittomat indeksit
            #print('pariton indeksi')
            if ss[ii] == '0':         # pariton = 1
                alkaa_nollasta += 1
                #print('alkaa_nollasta muuttuu')
            else:                   # pariton =0
                alkaa_ykkosesta += 1
                #print('alkaa_ykkosesta muuttuu')
        #print('----------------')

    return (min(alkaa_nollasta,alkaa_ykkosesta))
    


if __name__ == "__main__":
    print(calculate("1010")) # 0
    print(calculate("1111")) # 2
    print(calculate("10010001")) # 3