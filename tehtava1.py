#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
from time import time

def main(nn):
    alku = time()
    count = 0
    #2-n -> 3-n+1 
    for ii in range(3,nn+1):
        prime = True
        for jj in range(3,ii):
            if ii%jj == 0:
                prime = False
                break
        if prime:
            count+=1
    loppu = time()
    print('Alkulukuja:',count, 'Suoritus:',loppu-alku,'s')


if __name__ == '__main__':
    main(int(sys.argv[1]))