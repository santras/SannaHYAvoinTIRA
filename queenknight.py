#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from array import array

#def kuningatar(heppa,nn,sopimattomat):

def heppahyokkaus(heppa,nn):
    #Tämä antaa listana indeksit hepan mahdollisille hyökkäysruuduille, kun nn on ruudukon sivun pituus.
    #yla1,yla2,vas1,vas2, ala1,ala2,oik1,oik2

    yla1 = (heppa-2*nn-1) # 0            =yläkerran vas
    yla2 = (heppa-2*nn+1) #1             = yläkerran oik
    vas1 = (heppa-nn-2)   #2 =vas ylä
    vas2 = (heppa+nn+-2)  #3 =vas ala
    ala1 = (heppa+2*nn-1) #4             = alakerran vas
    ala2 = (heppa+2*nn+1) #5             = alakerran oik   
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
    #print(s0_ind[1],s0_ind[2],s0_ind[nn-2],s0_ind[nn-1])
    s_pera=s0_ind                           # tokavika sarake
    for ii in range(len(s_pera)):
        s_pera[ii] = s_pera[ii]+nn-1  
    #print(s_pera)

    if heppa in s0_ind:              # heppa vas reunalla -> poista vas + yla ja ala 
        ignoorauslista[2] = True
        ignoorauslista[3] = True
        ignoorauslista[0] = True    
        ignoorauslista[4] = True
    elif heppa-1 in s0_ind:         #heppa vas yhden ruudun päässä -> poista vas
        ignoorauslista[2] = True    
        ignoorauslista[3] = True
    elif heppa in s_pera:           
        ignoorauslista[6] = True    # heppa oik reunalla -> poista oik + yla ja ala
        ignoorauslista[7] = True
        ignoorauslista[1] = True    
        ignoorauslista[5] = True
    elif heppa+1 in s_pera:
        ignoorauslista[6] = True    # heppa oik reunalla yhden ruudun päässä -> poista oik
        ignoorauslista[7] = True

    # määrittele sopimattomat paikat kun heppa paikassa heppa eli heppa ja mahdolliset ruudut x0-24
    heppa_uhkaa = heppahyokkaus(heppa,nn)

    #määrittele sopimattomat paikat kun heppa paikassa heppa ja sijoitetaan kuningatarta
    # heppa
    poyta[heppa]=0

    #hepan hyökkäysmahkut
    for ii in range(len(ignoorauslista)):
        if ignoorauslista[ii] == False:
            print(heppa,heppa_uhkaa[ii])
            #poyta[heppa_uhkaa[ii-1]]=0

    #print(poyta)
    print('kierros')
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
        #print('kierros')
    #print(ekat_ind)
    
    
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
    