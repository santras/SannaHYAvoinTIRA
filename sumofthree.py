
#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#import sys
#from time import time
import math



def count_uus(nn):                       # isoin min 12 max 27 (n-3) # pienin 1-8, keskim 2-14

    kerroslaskin = 1
    laskin = 0

    # 27 1,2
    # 26 1,3 (2,2)
    # 25 1,4  2,3
    # 24 1,5  2,4  (3,3)

    for ii in range (nn-3,math.floor(nn/3),-1):                     
        #print (ii)                                                  
        laskin += kerroslaskin                  # Lisätään joka kerroksella kerroslaskimen verran vaihtoehtoja laskimeen                                                    
        if ii % 2 ==0:                          # Parillisen luvun jälkeen kerroslaskuriin tulee yksi lisää                                         
            kerroslaskin += 1
        


  
def count (nn):
    laskin = 0
    laskin2 = 0
    testilaskin =0
    kerroslaskin = 1

    apu math.floor(nn/4)

    if nn%2 == 0                                                    # Alustetaan laskin puoleen väliin
        laskin = apu* (apu+1)
    else:
        laskin = math.floor((apu*(apu+1))/2) + math.floor(((apu-1)*(apu))/2)


    for ii in range (math.floor(nn/2),math.floor(nn/3),-1):    
        #print('iso',ii)
        toinen_max = (nn-ii-1)
        testilaskin += laskin2
        laskin2 = 0
        
        #if ii >= math.floor(nn/2):                  # Ensimmäisistä kerroksista löytyi kaava puoleen väliin alkiota
            #laskin += kerroslaskin
            #if ii % 2 ==0:                          # Parillisen luvun jälkeen kerroslaskuriin tulee yksi lisää                                         
            #    kerroslaskin += 1
        
        #else:
        for jj in range(toinen_max,1,-1):
            #print('toka',jj)
            eka=nn-jj-ii
            #print('eka',eka)
            #print(eka,jj,ii)
            if eka >= jj:
                print('Kerros',ii,jj,laskin2)
                break
            if jj >= ii:
                continue
            #print(eka,jj,ii)
            laskin += 1 
            laskin2 += 1

    #print('testilaskin',testilaskin)
    return laskin


if __name__ == "__main__":
    #print(count(8)) # 2
    #print(count(30)) # 61
    print(count(32))
    #print(count(50))
    #print(count(1337)) # 148296
    #print (count(663307073)) # iso testi feilas
    #print(count(5)) # Testi feilas expected 0, my answer 1