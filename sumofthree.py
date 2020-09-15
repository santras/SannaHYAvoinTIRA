
#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#import sys
#from time import time



def count_ei(nn):                       # isoin on max puolet
    luku_pikkuset = 1
    laskin = 1

    for ii in range (nn):
        kolmas = nn - (luku_pikkuset * 2 + 1)
        print (luku_pikkuset, luku_pikkuset+1, kolmas)
        if kolmas <= (luku_pikkuset +1):
            return laskin
        else:
            laskin += 1
            luku_pikkuset += 1 

def count(nn):

    kaytetyt = []
    laskin = 0

    for ii in range (1,nn):
        for jj in range (1,nn):
            kolmas = nn -ii -jj
            #print (ii,jj, kolmas)
            if ii != jj and kolmas != ii and kolmas != jj and kolmas >0:                    # luvut eri järjestyksessä pitäis passata mutta jotain vikaa seuraavassa
                print (sorted([ii,jj, kolmas]))
                if sorted([ii,jj, kolmas]) not in kaytetyt :
                    kaytetyt.append(sorted([ii,jj,kolmas]))
                    laskin += 1
                    #print(ii,jj,kolmas)

    
    return laskin


if __name__ == "__main__":
    #print(count(8)) # 2
    print(count(30)) # 61
    #print(count(1337)) # 148296