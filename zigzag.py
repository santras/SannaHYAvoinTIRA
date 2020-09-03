#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from time import time


def create(nn):
    oik_lista = [1]
    vas_lista = []

    if nn == 1:
        return [nn]

    for ii in range(2,nn+1):
        #print(ii)
        if ii % 2 == 0:
            oik_lista.append(ii)
        else:
            vas_lista.append(ii)

    vas_lista = list(reversed (vas_lista))
    #print(vas_lista)

    return (vas_lista+oik_lista)


if __name__ == "__main__":
    alku = time()
    print(create(1)) # [1]
    print(create(2)) # [1,2]
    print(create(3)) # [3,1,2]
    print(create(4)) # [3,1,2,4]
    print(create(5)) # [5,3,1,2,4]
    loppu = time()
    print('Suoritus:',loppu-alku,'s')