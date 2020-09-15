
#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#import sys
#from time import time



def count(nn):
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




if __name__ == "__main__":
    print(count(8)) # 2
    #print(count(30)) # 61
    #print(count(1337)) # 148296