#!/usr/bin/env python
# -*- coding: utf-8 -*- 



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

    




if __name__ == "__main__":
    rec1 = (-1,1,1,-1)
    rec2 = (0,3,2,0)
    rec3 = (0,2,3,-2)
    print(area(rec1,rec2,rec3)) # 16