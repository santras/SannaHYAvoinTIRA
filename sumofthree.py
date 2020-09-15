
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


def count_uus2(nn):             ## Tässä kökköä
    
    tekstina = []
    laskin = 0

    for ii in range (nn-3,math.floor(nn/3),-1): 
        toinen_luku= (nn-ii-1)
            
           # return laskin
        print(1,toinen_luku,ii)
        tekstina.append(str(1)+' '+str(toinen_luku)+' '+str(ii))
        for jj in range (toinen_luku,1,-1):
            if (nn-jj-ii) >= jj:
                break
            if jj == nn-jj-ii:
                continue
            #print(nn-jj-ii,jj)
            laskin +=1
            tekstina.append(str(nn-jj-ii)+' '+str(jj)+' '+str(ii))
            if ii < jj:
                return tekstina 

    return tekstina    

def count4 (nn):
    laskin = 0

    for ii in range (nn-3,math.floor(nn/3),-1):    
        #print('iso',ii)
        toinen_max = (nn-ii-1)
        for jj in range(toinen_max,1,-1):
            #print('toka',jj)
            eka=nn-jj-ii
            #print('eka',eka)
            #print(eka,jj,ii)
            if eka >= jj:
                break
            if jj >= ii:
                continue
            #print(eka,jj,ii)
            laskin += 1 

    return laskin


def count(nn):

    kaytetyt = []
    tekstina = []
    laskin = 0

    for ii in range (1,nn):
        for jj in range (1,nn):
            kolmas = nn -ii -jj
            
            if ii != jj and kolmas != ii and kolmas != jj and kolmas >0:                   
                #print (sorted([ii,jj, kolmas]))
                #print ((sorted([ii,jj, kolmas])[1]))
                if sorted([ii,jj, kolmas]) not in kaytetyt :
                    kaytetyt.append(sorted([ii,jj,kolmas]))
                    jutut = sorted([ii,jj,kolmas])
                    stringi = str(jutut[0])+' '+str(jutut[1])+' '+str(jutut[2])
                    tekstina.append(stringi)
                    #print(stringi)
                    laskin += 1
                   

    #print (kaytetyt)
    #tekstina_uus = count_uus2(nn)
    #print(tekstina_uus)
    #for ii in range(len(tekstina)):
    #    if tekstina[ii] not in tekstina_uus:
    #        print ('puuttuu',tekstina[ii])
    #print(len(tekstina_uus),len(tekstina))
    count4(nn)
    #print(tekstina)

    return laskin


if __name__ == "__main__":
    print(count4(8)) # 2
    print(count4(30)) # 61
    print(count4(1337)) # 148296