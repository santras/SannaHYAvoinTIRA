#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def count(sana):
    setti = set(sana)

    for ii in range(0,len(sana)-1): 

        for jj in range (len(sana),ii+1,-1):
            lyhyempi=sana[ii:jj]
            setti.add(lyhyempi)

    return len(setti)



if __name__ == "__main__":
    
    print(count("aaa")) # 3
    print(count("abc")) # 6
    print(count("saippuakauppias")) # 110
