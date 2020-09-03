#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#from array import array

#def kuningatar(heppa,nn,sopimattomat):

# def heppahyokkaus(heppa,nn):
#     #Tämä antaa listana indeksit hepan mahdollisille hyökkäysruuduille, kun nn on ruudukon sivun pituus.
#     #yla1,yla2,vas1,vas2, ala1,ala2,oik1,oik2

#     yla1 = (heppa-2*nn-1) # 0            =yläkerran vas
#     yla2 = (heppa-2*nn+1) #1             = yläkerran oik
#     vas1 = (heppa-nn-2)   #2 =vas ylä
#     vas2 = (heppa+nn+-2)  #3 =vas ala
#     ala1 = (heppa+2*nn-1) #4             = alakerran vas
#     ala2 = (heppa+2*nn+1) #5             = alakerran oik   
#     oik1 = (heppa-nn+2)   #6 =oik ylä
#     oik2 = (heppa+nn+2)   #7  =oik ala
    
#     return [yla1,yla2,vas1,vas2,ala1,ala2,oik1,oik2]

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
    print(popperit)
    for poppaukset in popperit:
        #print(poppaukset)
        heppakoordi.pop(poppaukset)
    
    return heppakoordi

    
    


def testaa(heppa,poyta,nn):

    laskin = 0
    
    # Hepan moovit
    # Hepan ruutu varattu
    #poyta[heppa] = 0
    #print(poyta)
    #Hepan hyökkäysruudut
    hepanhyokimys(heppa,nn)
    

    #for paikat in poyta.keys():
    #    if paikat[0] == 0:
    #        print(paikat)
        #print (avain,arvo)
    

    

#     #erikoistapaukset reunoilla
#     ignoorauslista = [False]*8
#     if heppa<s0_ind[0]:             #yläreunan liikkeet ei mahdollisia
#         ignoorauslista[0] = True    #reuna 1 ruudun päässä -> poista ylä
#         ignoorauslista[1] = True
#     elif heppa<s0_ind[1]:
#         ignoorauslista[0] = True    #heppa reunalla ->poista ylä + sivu ylät
#         ignoorauslista[1] = True    
#         ignoorauslista[2] = True    
#         ignoorauslista[6] = True
#     elif heppa>=s0_ind[nn-2]:       #alareunan liikkeet ei mahdollisía
#         ignoorauslista[4] = True    #reuna 1 ruudun päässä -> poista ala
#         ignoorauslista[5] = True
#     elif heppa>s0_ind[nn-1]:
#         ignoorauslista[4] = True    #heppa reunalla -> posta ala + sivu alat
#         ignoorauslista[5] = True
#         ignoorauslista[3] = True    
#         ignoorauslista[7] = True
#     #print(s0_ind[1],s0_ind[2],s0_ind[nn-2],s0_ind[nn-1])
#     s_pera=s0_ind                           # tokavika sarake
#     for ii in range(len(s_pera)):
#         s_pera[ii] = s_pera[ii]+nn-1  
#     #print(s_pera)

#     if heppa in s0_ind:              # heppa vas reunalla -> poista vas + yla ja ala 
#         ignoorauslista[2] = True
#         ignoorauslista[3] = True
#         ignoorauslista[0] = True    
#         ignoorauslista[4] = True
#     elif heppa-1 in s0_ind:         #heppa vas yhden ruudun päässä -> poista vas
#         ignoorauslista[2] = True    
#         ignoorauslista[3] = True
#     elif heppa in s_pera:           
#         ignoorauslista[6] = True    # heppa oik reunalla -> poista oik + yla ja ala
#         ignoorauslista[7] = True
#         ignoorauslista[1] = True    
#         ignoorauslista[5] = True
#     elif heppa+1 in s_pera:
#         ignoorauslista[6] = True    # heppa oik reunalla yhden ruudun päässä -> poista oik
#         ignoorauslista[7] = True

#     # määrittele sopimattomat paikat kun heppa paikassa heppa eli heppa ja mahdolliset ruudut x0-24
#     heppa_uhkaa = heppahyokkaus(heppa,nn)

#     #määrittele sopimattomat paikat kun heppa paikassa heppa ja sijoitetaan kuningatarta
#     # heppa
#     poyta[heppa]=0

#     #hepan hyökkäysmahkut
#     for ii in range(len(ignoorauslista)):
#         if ignoorauslista[ii] == False:
#             print(heppa,heppa_uhkaa[ii])
#             #poyta[heppa_uhkaa[ii-1]]=0

#     #print(poyta)
#     print('kierros')
    return


def count(nn):

    #handlataan liian pienet kentät joissa ei ollenkaan paikkoja
    if nn<=3:
        return 0

    # Tehdaan dictionary
    pelipoyta = {}
    koordinaatit=[]
    

    #Indeksointi 
    # Ajatellaan koordinaatit ihan normi koordinaatteina (x,y) ja kasvaa isompaan päin eli oikealle ja ylös
    for ii in range(nn):                   
        for jj in range(nn):
            koordinaatit.append((ii, jj))
    #print(koordinaatit,len(koordinaatit))

    
    for ind in koordinaatit:
        pelipoyta[ind] = 1          # Alustetaan kaikki potenttiaalisiksi paikoiksi 
                                    # arvot 1 = mahdollinen, 0 = ei mahdollinen
    
    #print(pelipoyta)

    # Seuraavaksi testataan mitkä paikat oikeasti sopivat
    laskin=0
    for indeksi in range(1):   #len(koordinaatit)):
        testaa(koordinaatit[indeksi],pelipoyta,nn)  
    #print(laskin)

 
    

if __name__ == "__main__":
    #print(count(3)) # 0
    print(count(4)) # 40
    #print(count(5)) # 184
    