#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def kuvauskierros(kuvaus): 
    laskin = 1  # laskin alkuasetukseen joka kuvauskierroksella
    uusi=''

    if len(kuvaus) == 1:
        return str(laskin)+str(kuvaus)  # jos yhden pitunen
    else:
        for ii in range(len(kuvaus)):   
            if ii+1 == len(kuvaus): # jos vika lisättävä
                uusi = uusi+str(laskin)+str(kuvaus[ii])
            else:
                if kuvaus[ii] == kuvaus[ii+1]: # seuraava sama
                    laskin+=1
                else:
                    uusi=uusi+str(laskin)+str(kuvaus[ii])
                    laskin = 1 
        return uusi



def generate(nn):
    kuvaus='1'
    for ii in range(nn-1):
        kuvaus = kuvauskierros(kuvaus)
    return(kuvaus)
    

if __name__ == "__main__":
    
    print(generate(1)) # 1
    print(generate(2)) # 11
    print(generate(3)) # 21
    print(generate(4)) # 1211
    print(generate(5)) # 111221
    print(generate(6)) # 312211  lisays
