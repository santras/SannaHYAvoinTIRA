#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def ala(nurkka_vy,nurkka_oa):  
    ala=abs((nurkka_vy[0] - nurkka_oa[0])*(nurkka_vy[1]-nurkka_oa[1])) 
    return ala

def onko_piste_sis(piste,nkulmio_vy,nkulmio_oa, reunalla_mukana=False):
    onko = False

    if reunalla_mukana:
        if piste[0] <= nkulmio_oa[0] and piste[0] >= nkulmio_vy [0]:
            if piste[1] <= nkulmio_vy[1] and piste[1] >= nkulmio_oa[1] :
                onko = True
                
    else:
        if piste[0] < nkulmio_oa[0] and piste[0] > nkulmio_vy [0]:
            if piste[1] < nkulmio_vy[1] and piste[1] > nkulmio_oa[1] :
                onko = True
                #print("hei")
    return onko
      
# def onko_nkulm_sis(An_kulmio_vy,An_kulmio_oa,Bn_kulmio_vy,Bn_kulmio_oa, reunalla_mukana=False): # Testaa onko jälkimmäinen ensimmäisen sisällä
#     n_onko = False

#     if reunalla_mukana:
#         if onko_piste_sis(Bn_kulmio_vy,An_kulmio_vy,An_kulmio_oa,True):
#             if onko_piste_sis(Bn_kulmio_oa,An_kulmio_vy,An_kulmio_oa,True):
#                 n_onko = True

#     else:
#         if onko_piste_sis(Bn_kulmio_vy,An_kulmio_vy,An_kulmio_oa,True):
#             if onko_piste_sis(Bn_kulmio_oa,An_kulmio_vy,An_kulmio_oa,True):
#                 n_onko = True
##    #return n_onko

def yhteinen(An_sis_Bpist,Bn_sis_Apist,A_pist, B_pist):
    if any(An_sis_Bpist):
        if all(An_sis_Bpist): # kokonaan sisällä
        
        elif An_sis_Bpist[]

    else:
        



def testaa (An_kulmio_vy,An_kulmio_oa,Bn_kulmio_vy,Bn_kulmio_oa):

    # Onko jomman kumman kulma toisen sisällä kokonaan?
    A_pist = [An_kulmio_vy,(An_kulmio_vy[0],An_kulmio_oa[1]), An_kulmio_oa, (An_kulmio_oa[0], An_kulmio_vy[1])]
    #print(A_pist)
    B_pist = [Bn_kulmio_vy,(Bn_kulmio_vy[0],Bn_kulmio_oa[1]), Bn_kulmio_oa, (Bn_kulmio_oa[0], Bn_kulmio_vy[1])]
    #print(B_pist)
    An_sis_Bpist = []
    Bn_sis_Apist = []

    # A nelikulmio, B pisteet
    for ii in range(len(B_pist)):
        if (onko_piste_sis(B_pist[ii],An_kulmio_vy,An_kulmio_oa)):
            An_sis_Bpist.append(True)
        else:
            An_sis_Bpist.append(False)

    # A nelikulmio, B pisteet
    for ii in range(len(A_pist)):
        if (onko_piste_sis(A_pist[ii],Bn_kulmio_vy,Bn_kulmio_oa)):
            Bn_sis_Apist.append(True)
        else:
            Bn_sis_Apist.append(False)

    #print(An_sis_Bpist, Bn_sis_Apist)
    if any(An_sis_Bpist) or any(Bn_sis_Apist):
        yhteinen(An_sis_Bpist,Bn_sis_Apist,A_pist, B_pist)

    else:
        return False, 0, (0,0),(0,0)        # onko sisäkkäin, sisäkkäin ala, sisäkkäin n_kulm


    #print([An_sis_vy,An_sis_oa,Bn_sis_vy,Bn_sis_oa])
    #if any([An_sis_vy,An_sis_oa,Bn_sis_vy,Bn_sis_oa]):
    #    print('hei')




def area(rec1, rec2, rec3):

    # TODO
    # Määrittele ja Laske ala maksimialuelle A_max= (X_max-X-min)*(Y_max-Y_min).
    # Laske yritelmän ala A_yritelmä = A_Rect1 + A_Rect2 + A_Rect3.
    # Määrittele hukka-ala A_poisto.
    # Jaa alue osapalasiin, kaikki reunat ja kaikki kulmat muodostovat pysty-vaaka viivat,
    # jotka jakavat alueen. 
    # Tee luuppi jonka sisällä testataan että onko A_max == A_yritelmä + A_poisto, ratkaisu
    # saavutettu kun ovat. Anna silloin A_yritelmä tuloksena.  
    # Testauksessa yksi kerrallan testataan onko osa-alue laatikoiden a,b,c sisällä vai ulkona.
    # Vaihtoehdot voivat olla 
    #   1) Ulkona -> Lisää alue hukkapalaan
    #   2) 1-kertaisesti sisällä -> Älä tee mitään
    #   3) 2-kertaisesti sisällä -> Ota alue pois yritelmästä kerran
    #   4) 3-kertaisesti sisällä -> Ota alue pois yritelmästä kaksi kertaa
    #---------------------------------------------
    # Toinen täysin erilainen lähtökohta
    # LÄHDE PALIKOIDEN GEOMETRIASTA LIIKKELLE
    # Palikka A:n suhde B:hen voi olla
        #   0) Toisen sisällä
        #   1) Täysin samat
        #   2) 2 Kulmaa yhdessä
        #   3) 1 Kulma yhdessä
        #   4) 1 Sivu yhdessä
        #   5) 2 Kulmaa sisällä
        #   6) 1 Kulma sissällä
        #   7) Ristikkäin
        #   8) Toistensa ulkopuolella
    # Tässä vaihtoehdossa pitäisi vertailla aika paljon onko kulmat toistensa sisällä vai ei
    # toisessa tehdään isoa luuppia jolla lasketaan melko simppeliä laskua
    # Tämä jälkimmäinen vaikuttaa haastavammalta toteuttaa, ylempi on simppeli, mutta raakaa laskemista ja voi olla
    # että siinä kuluu liikaa aikaa. Jännin olisi tietty tehdä molemmat, mutta vois tällä viikolla kyllä muutakin tehdä. 
    # Päätöksiä, päätöksiä...
    # Yritetään tätä jälkimmäistä. 
    # TODO
    # 1 Laske palikoiden alat
    # 2 Ota isoin "alustaksi" - palikka A
    # 3 Testaa onko Palikka B:n vastakkaiset kulmat sisällä/raunoilla -> molemmat sisällä 
    # -> palikka sisällä -> kokonaan B pois alasta
    # Testaa loput kaikki tosi monet kulma/sivu vaihtehdot ja mieti mitä otetaan pois kokonaisalasta
    # Sitten vaihda B:sijaan C käsittelyyn
    # Lopuksi katso kumpi isompi ja ota se alustaksi ja katso onko sillä yhteisä osia toisen kanssa jotka poistetaan myös listasta
    # Mä joko väsyn tai tää on muuten kyllä super työläs vaihtoehto, ehkä sittenkin yritän tuota ekaa vaihtoehtoa. 
    # TODO
    # No niin kolmas hybridi versio edellisitä, vielä hahmotteluasteella. Eli unohdetaan kokoala ja käytetään isointa nelikulmiota eka. 
    # Lasketaan kaikkien kolmen pinta-alat
    # Tehdään funktio onko sisällä joka toimii pisteelle ja nelikulmiolle. 
    # Ja siitä laajennus/muunnos onko samat joka testaa onko alue nelikulmion sisällä. Tämä tehdään ottamalla molemmat viistokulmapisteet 
    # ja testataan onko sisällä tai reunalla (molemmat tosi että on).
     # Ensiksi tosin pitänee testata että kumpikaan pienistä ei ole kokonaan isomman/ toisensa sisällä. 
    # Sitten otetaan suurin nelikulmio käsittelyyn. Katsotaan onko jokin viistokulmapisteistä sen sisällä, jos on nelikulmio jaetaan osiin.
    # Osat käsitellään erikseen ja katsotaan onko osa päälekkäisiä kahden toisen nelikulmion kanssa. Jos on, osat vähennetään alkuperäisestä
    # summasta. Sitten käsitellään samoin toisiksi suurin nelikulmio, mutta tällä kertaa testataan vaan kolmannen nelikulmion kanssa 
    # yhteisalueiden varalle. 
    # Viimeiseksi pitää vielä käsitellä mahdollinen ristinelikulmiotilanne. 
    # No niin nyt on ainaskin hyvä suunnitelma olemassa. 
    piste1vy = (rec1[0],rec1[1])
    piste1oa = (rec1[2],rec1[3])
    piste2vy =  (rec2[0],rec2[1])
    piste2oa =  (rec2[2],rec2[3])
    piste3vy =  (rec3[0],rec3[1])
    piste3oa =  (rec3[2],rec3[3])

    ala1=ala(piste1vy,piste1oa)
    ala2=ala(piste2vy,piste2oa)
    ala3=ala(piste3vy,piste3oa)

    Yhteisala = ala1+ala2+ala3

    #Alat = [ala1,ala2,ala3]
    #Nelikulmiot = [rec1,rec2,rec3]
    #print(Alat.index(max(Alat)))        # Indeksi isoimmalle alalle
    #print(Nelikulmiot[Alat.index(max(Alat))])  # Isoin nelikulmio


    testaa(piste1vy,piste1oa,piste2vy,piste2oa)  # 1 ja 2
    testaa(piste1vy,piste1oa,piste3vy,piste3oa)  # 1 ja 3
    testaa(piste2vy,piste2oa,piste3vy,piste3oa)  # 2 ja 3

    return Yhteisala




if __name__ == "__main__":
    rec1 = (-1,1,1,-1)  # vas ylänurkka, oik alanurkka
    rec2 = (0,3,2,0)
    rec3 = (0,2,3,-2)
    print(area(rec1,rec2,rec3)) # 16