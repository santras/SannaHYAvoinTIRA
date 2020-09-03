#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
from time import time
import array
import math

def check(nn):
    
    onnekas = False
    lista_nn = [numero for numero in str(nn)]
    yhteen = 0
    for numero2 in lista_nn:
        yhteen = yhteen + int(numero2)
    if yhteen % 7 == 0:
        onnekas = True
    return onnekas
    

if __name__ == "__main__":
    alku = time()
    print(check(14)) # False
    print(check(16)) # True
    print(check(123)) # False
    print(check(777)) # True
    print(check(9999999)) # True
    loppu = time()
    print('Suoritus:',loppu-alku,'s')