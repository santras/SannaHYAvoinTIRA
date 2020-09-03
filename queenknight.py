#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from array import array

#def kuningatar(heppa,nn,sopimattomat):

def heppahyokkaus(heppa,nn):
    #Tämä antaa listana indeksit hepan mahdollisille hyökkäysruuduille, kun nn on ruudukon sivun pituus.
    #yla1,yla2,vas1,vas2, ala1,ala2,oik1,oik2

    yla1 = (heppa-2*nn-1) # 0
    yla2 = (heppa-2*nn+1) #1
    vas1 = (heppa-nn-2)   #2 =vas ylä
    vas2 = (heppa+nn+-2)  #3 =vas ala
    ala1 = (heppa+2*nn-1) #4
    ala2 = (heppa+2*nn+1) #5
    oik1 = (heppa-nn+2)   #6 =oik ylä
    oik2 = (heppa+nn+2)   #7  =oik ala
    
    return [yla1,yla2,vas1,vas2,ala1,ala2,oik1,oik2]
    


def testaa(heppa,poyta,s0_ind,nn):

    laskin=0

    #erikoistapaukset reunoilla
    ignoorauslista = [False]*8
    if heppa<s0_ind[0]:             #yläreunan liikkeet ei mahdollisia
        ignoorauslista[0] = True    #reuna 1 ruudun päässä -> poista ylä
        ignoorauslista[1] = True
    elif heppa<s0_ind[1]:
        ignoorauslista[0] = True    #heppa reunalla ->poista ylä + sivu ylät
        ignoorauslista[1] = True    
        ignoorauslista[2] = True    
        ignoorauslista[6] = True
    elif heppa>=s0_ind[nn-2]:       #alareunan liikkeet ei mahdollisía
        ignoorauslista[4] = True    #reuna 1 ruudun päässä -> poista ala
        ignoorauslista[5] = True
    elif heppa>s0_ind[nn-1]:
        ignoorauslista[4] = True    #heppa reunalla -> posta ala + sivu alat
        ignoorauslista[5] = True
        ignoorauslista[3] = True    
        ignoorauslista[7] = True
    print(s0_ind[1],s0_ind[2],s0_ind[nn-2],s0_ind[nn-1])

    # määrittele sopimattomat paikat kun heppa paikassa heppa eli heppa ja mahdolliset ruudut x0-24
    sopimattomat = heppahyokkaus(heppa,nn)
    print(sopimattomat)
    #määrittele sopimattomat paikat kun heppa paikassa heppa ja sijoitetaan kuningatarta
    
    return laskin


def count(nn):

    #handlataan liian pienet kentät joissa ei ollenkaan paikkoja
    if nn<=3:
        return 0

    paikat=array('I',[1]*nn*nn)     # nn*nn matriisi pötkönä

    # ekan sarakkeen indeksit
    ekat_ind=[]
    for ii in range(nn): 
        ekat_ind.append(ii*nn)
    print(ekat_ind)
    
    
    laskin=0
    for testipaikka in range(len(paikat)):
        #print(testipaikka)
        laskin=laskin+testaa(testipaikka,paikat,ekat_ind,nn)  
        #laskin+=1
    #print(laskin)

 
    

if __name__ == "__main__":
    #print(count(3)) # 0
    print(count(4)) # 40
    #print(count(5)) # 184
    