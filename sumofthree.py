
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
        


    return laskin      

def count(nn):

    kaytetyt = []
    laskin = 0

    for ii in range (1,nn):
        for jj in range (1,nn):
            kolmas = nn -ii -jj
            
            if ii != jj and kolmas != ii and kolmas != jj and kolmas >0:                   
                #print (sorted([ii,jj, kolmas]))
                #print ((sorted([ii,jj, kolmas])[1]))
                if sorted([ii,jj, kolmas]) not in kaytetyt :
                    kaytetyt.append(sorted([ii,jj,kolmas]))
                    laskin += 1
                   

    #print (kaytetyt)
    return laskin


if __name__ == "__main__":
    #print(count(8)) # 2
    print(count_uus(30)) # 61
    #print(count(1337)) # 148296