#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#from array import array

def hepanhyokimys(heppa,nn):
   
    # Tehdään lista mahdollisille ruuduille
    # x-suuntaan 2 ja   y+1 /y-1
    # x-suuntaan 1 ja   y+2 /y-2
    # ed -x suuntaan
    heppakoordi = [
    ((heppa[0] + 2),(heppa[1] + 1)), 
    ((heppa[0] + 2),(heppa[1] - 1)),
    ((heppa[0] + 1),(heppa[1] + 2)),
    ((heppa[0] + 1),(heppa[1] - 2)),
    ((heppa[0] - 2),(heppa[1] + 1)),
    ((heppa[0] - 2),(heppa[1] - 1)),
    ((heppa[0] - 1),(heppa[1] + 2)),
    ((heppa[0] - 1),(heppa[1] - 2))]

    # Jätetään laudan ulkopuoliset koordinaatit pois
    popperit=[]
    for ii in range(len(heppakoordi)):
        if (heppakoordi[ii][0]<0) or (heppakoordi[ii][1]<0):   # Reunan ulkouolella olevat
            popperit.append(ii)
        elif (heppakoordi[ii][0]>nn-1) or (heppakoordi[ii][1]>nn-1):
            popperit.append(ii)

    popperit=sorted(set(popperit),reverse=True)             # Poppaillaan perästä että ei sekoiteta indeksejä
    #print(popperit)
    for poppaukset in popperit:
        #print(poppaukset)
        heppakoordi.pop(poppaukset)
    
    return heppakoordi

def kuningatar(heppa,nn):
    
    # Ei samalle riville, sarakkeeseen tai vinoriville kun heppa
    # rivillä (x) plussalle ja miinukselle
    # sarakkeella (y) plussalle ja miinukselle
    # vinorivi vas-alhaalta - oik-ylös
    # vinorivi vas-ylhäältä - oike-alas
    rouvanruudut = []
    for ii in range(-nn,+nn):                            # Tehdään ensin "ronskilla kädellä" vähän iso
        rouvanruudut.append(((heppa[0]+ii),(heppa[1])))
        rouvanruudut.append(((heppa[0]),(heppa[1]+ii)))
        rouvanruudut.append(((heppa[0]+ii),(heppa[1]+ii)))
        rouvanruudut.append(((heppa[0]-ii),(heppa[1]+ ii)))
    #print(rouvanruudut)

    # Jätetään laudan ulkopuoliset koordinaatit pois
    popperit=[]
    for ii in range(len(rouvanruudut)):
        if (rouvanruudut[ii][0]<0) or (rouvanruudut[ii][1]<0):   # Reunan ulkouolella olevat
            popperit.append(ii)
        elif (rouvanruudut[ii][0]>nn-1) or (rouvanruudut[ii][1]>nn-1):
            popperit.append(ii)

    popperit=sorted(set(popperit),reverse=True)             # Poppaillaan perästä että ei sekoiteta indeksejä
    #print(popperit)
    for poppaukset in popperit:
        #print(poppaukset)
        rouvanruudut.pop(poppaukset)
    #print(rouvanruudut)
    return rouvanruudut
    
    


def toimimattomat(nn,kierros):
    
    # Tehdaan dictionary
    poyta = {}
    koordinaatit=[]

    #Indeksointi 
    # Ajatellaan koordinaatit ihan normi koordinaatteina (x,y) ja kasvaa isompaan päin eli oikealle ja ylös
    for ii in range(nn):                   
        for jj in range(nn):
            koordinaatit.append((ii, jj))
    #print(koordinaatit,len(koordinaatit))

    #Tehdään hepan paikkaan heppa-muuttuja
    heppa = koordinaatit[kierros]
    #print(heppa)

    for ind in koordinaatit:
        poyta[ind] = 1          # Alustetaan kaikki potenttiaalisiksi paikoiksi 
                                    # arvot 1 = mahdollinen, 0 = ei mahdollinen
    

    # Hepan moovit
    # Hepan ruutu varattu
    poyta[heppa] = 0
    #print(poyta)
    #Hepan hyökkäysruudut
    heppamoovit = hepanhyokimys(heppa,nn)
    for ii in range(len(heppamoovit)):  # Tägätään hepan mahdolliset ruudut ei-potenttiialisiksi paikoiksi
        poyta[heppamoovit[ii]]=0
    
    # Sitten kuningattaren ruudut
    rouvamoovit = kuningatar(heppa,nn)
    for ii in range(len(rouvamoovit)):  # Tägätään hepan mahdolliset ruudut ei-potenttiialisiksi paikoiksi
        poyta[rouvamoovit[ii]]=0

    return sum(poyta.values())
   



def count(nn):

    #handlataan liian pienet kentät joissa ei ollenkaan paikkoja
    if nn<=3:
        return 0

    # Seuraavaksi testataan mitkä paikat oikeasti sopivat, käydään läpi yksi mahdollinen tapa laittaa ensin
    # heppa sitten kuningatar
    laskin=0
    for indeksi in range(nn*nn):
        laskin=laskin+toimimattomat(nn,indeksi)  
    #print(laskin)
    return laskin

 
    

if __name__ == "__main__":
    print(count(3)) # 0
    print(count(4)) # 40
    print(count(5)) # 184
    