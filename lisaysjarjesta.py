#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#import sys
from time import time
from random import shuffle

def jarjesta(aa,bb):
    if aa == bb:
        return
    kk = (aa+bb)//2
    jarjesta(aa,kk)
    print(aa,kk,kk+1,bb)
    jarjesta(kk+1,bb)
    lomita(aa,kk,kk+1,bb)

def lomita(a1,b1,a2,b2):
    aa = a1
    bb = b2
    for ii in range(aa,bb-1):
        if a2 > b2 or (a1 <= b1 and jarjestettava[a1] <= jarjestettava[a2]):
            apulista[ii] = jarjestettava[a1]
            a1 += 1
        else:
            apulista[ii] = jarjestettava[a2]
            a2 += 1
    for ii in range (aa,bb):
        jarjestettava[ii] = apulista[ii]


def lomitusjarjesta(lista):
    global jarjestettava  # tehdään näistä globaaleja muuttujia 
    global apulista
    jarjestettava = lista
    #print(jarjestettava)
    apulista = [0]*len(lista)
    jarjesta(0,len(lista))
    print(jarjestettava)   ################Tulee pelkkää nollaa,köh köh

    

    



def alusta(nn):
    # Ensin alusta lista random luku*nn
    # ajanotto + jarjesta-kutsu
    # palauta nn, aika
    lista = []
    for ii in range(1,nn+1):
        lista.append(ii)
    shuffle(lista)
    print(lista)
    alku = time()
    lomitusjarjesta(lista)
    loppu = time()
    print(jarjestettava)
    return (nn, loppu - alku)

if __name__ == "__main__":
    print(alusta(10))
    #print(alusta(1000))
    #print(alusta(10000))
    #print(alusta(100000))
   
    