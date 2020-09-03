#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from array import array

def heppahyokkaus(heppa,nn,hepan_s0ind):
    # Tämä antaa listana indeksit hepan ruuduille, kun nn on ruudukon sivun pituus.
    # Lisäksi tämä antaa boolean listan ovatko liikket mahdollisia.
    # yla1,yla2,vas1,vas2, ala1,ala2,oik1,oik2
   
    #print(heppa,nn,hepan_s0ind)

    yla1 = (heppa-2*nn-1)
    yla2 = (heppa-2*nn+1)
    vas1 = (heppa-nn-2)
    vas2 = (heppa+nn+-2)
    ala1 = (heppa+2*nn-1)
    ala2 = (heppa+2*nn+1)
    oik1 = (heppa-nn+2)
    oik2 = (heppa+nn+2)
    
    liikkeet = [yla1,yla2,vas1,vas2,ala1,ala2,oik1,oik2]
    onko_laudalla = [True]*8
    print(liikkeet)
    
    for ii in range(len(liikkeet)):
        #print(ii)
        if liikkeet[ii]<0:                             # ylilaudan
            #print('heps',ii)
            onko_laudalla[ii] = False  
        elif liikkeet[ii]>(nn*nn-1):                    # alilaudan
            onko_laudalla[ii] = False
        if ii in [2,3,6,7]:
            if (liikkeet[2]<hepan_s0ind-nn): # vasen sivu, ylä
                print(ii,liikkeet[2],liikkeet[ii],hepan_s0ind-nn)
                onko_laudalla[2] = False
            elif (liikkeet[3]<hepan_s0ind+nn): # vasen sivu, ala
                onko_laudalla[3] = False
            elif (liikkeet[6]>hepan_s0ind-1): # oikea sivu, ylä
                onko_laudalla[6] = False
            elif liikkeet[7]>hepan_s0ind+nn-1: # oikea sivu, ala
                onko_laudalla[7] = False
   #print(liikkeet, onko_laudalla)

# def hepparuudut(paikka,s0_ind,nn):
#     if paikka >= s0_ind[2] : # eli ei kahdella ekalla rivillä  # TARKISTA INDEKSIT!
#         if paikka <=s0_ind[nn-3]: # ei kahdella vikalla rivillä
#             #JOTAIN
#         elif paikka <=s0_ind[nn-2]: # tokavikarivi
#             #JOTAIN     
#         else:                       # vikarivi
#             #JOTAIN
#     elif



def testaa(heppa,poyta,s0_ind,nn):

    laskin=0
    # määrittele sopimattomat paikat kun heppa paikassa heppa eli heppa ja mahdolliset ruudut x0-24

    #testaa loput paikoista sopiiko vai ei + laske sopivien määrä
    return laskin


def count(nn):

    paikat=array('I',[1]*nn*nn)     # nn*nn matriisi pötkönä

    # ekan sarakkeen indeksit
    ekat_ind=[]
    for ii in range(nn): 
        ekat_ind.append(ii*nn)
    print(ekat_ind)
    
    #testataan eri paikat ratsulle
    laskin=0
    for testipaikka in range(len(paikat)):
        #print(testipaikka)
        laskin=laskin+testaa(testipaikka,paikat,ekat_ind,nn)  # testataan eri paikat kuningattarelle
        #laskin+=1
    #print(laskin)

 
    

if __name__ == "__main__":
    print(heppahyokkaus(4,3,3)) # 0
    #print(count(4)) # 40
    #print(count(5)) # 184
    