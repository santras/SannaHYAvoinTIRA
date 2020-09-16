
#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#import sys
#from time import time


def count(ss):

    kirjainlaskuri = {}
    paalaskuri = 0

    for ii in range (len(ss)):
        if ss[ii] in kirjainlaskuri.keys():
            kirjainlaskuri [ss[ii]] += 1    # Lisätään yksi kirjaimen esiintyminen
            paalaskuri += kirjainlaskuri[ss[ii]]    # Lisätään kirjaimeen loppuvat osajonot
        else:
            kirjainlaskuri [ss[ii]] = 1
            paalaskuri += 1

    return paalaskuri

if __name__ == "__main__":
    print(count("aaa")) # 6
    print(count("abcd")) # 4
    print(count("ababca")) # 10