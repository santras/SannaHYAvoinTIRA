#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#import sys
#from time import time


def calculate(ss):

    #  Jotta olisi vuoroin 0 ja 1 voi olla joko 0101... tai 1010...
    parittomat = 0  # parittomat 1:ä
    parilliset = 0  # parilliset 1:ä
                         
    for ii in range(len(ss)):
        if ii%2 != 0:   # jonon pariton jäsen
            if ss[ii] != 1:
                parittomat += 1
            else:
                parilliset += 1
        else:           # jonon parillinen jäsen
            if ss[ii] != 1:
                parilliset += 1
            else:
                parittomat += 1

    return (min(parilliset,parittomat))
    


if __name__ == "__main__":
    print(calculate("1010")) # 0
    print(calculate("1111")) # 2
    print(calculate("10010001")) # 3