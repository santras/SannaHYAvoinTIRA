#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from time import time

def fibo(nn,rundi):

    #print(nn,rundi)
    rundi +=1

    if nn <= 1:
        return nn,rundi    
    else:
        (fibot1, rundi) = fibo(nn-1, rundi)
        (fibot2, rundi) = fibo(nn-2, rundi)
        return (fibot1 + fibot2, rundi)
    




if __name__ == "__main__":

    alku = time()    
    luku = 40
    kertaa = 0
    fibonacci = (fibo(luku,kertaa))
    loppu = time()
    print('fibo',luku,fibonacci,loppu-alku)
