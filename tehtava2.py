#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
from time import time
import array
import math

def main(nn):
    alku = time()
    count = 0
    
    aa=[0]*(nn)

    for ii in range(2,nn+1):
        if aa[ii-1] == 0:
            count+=1
            for jj in range((ii*2),nn+1,(ii)):
                aa[jj-1]=1
    loppu = time()
    print('Alkulukuja:',count, 'Suoritus:',loppu-alku,'s')

    #     count+=1
    #     for jj in range(3,ii):
    #         if ii%jj == 0:
    #             prime = False
    #             break
    #     if prime:
    #         count+=1
    # loppu = time()
    # print('Alkulukuja:',count, 'Suoritus:',loppu-alku,'s')


if __name__ == '__main__':
    main(int(sys.argv[1]))