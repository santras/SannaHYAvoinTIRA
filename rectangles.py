#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def ala(nurkka_vy,nurkka_oa):
    # laskee alan  
    ala=abs((nurkka_vy[0] - nurkka_oa[0])*(nurkka_vy[1]-nurkka_oa[1])) 
    return ala

def onko_piste_sis(piste,nkulmio_vy,nkulmio_oa, reunalla_mukana=False):
    # onko piste nelikulmion sisällä
    onko = False

    if reunalla_mukana:
        if piste[0] <= nkulmio_oa[0] and piste[0] >= nkulmio_vy [0]:
            if piste[1] <= nkulmio_vy[1] and piste[1] >= nkulmio_oa[1] :
                onko = True
                
    else:
        if piste[0] < nkulmio_oa[0] and piste[0] > nkulmio_vy [0]:
            if piste[1] < nkulmio_vy[1] and piste[1] > nkulmio_oa[1] :
                onko = True
               
    return onko
      
def nelikulmio_sisalla(Eka_vy,Eka_oa,Toka_vy,Toka_oa):
    # Onko nelikulmio toisen sisällä (toka ekan sisällä) tai onko samat
    sisakkain= False
    if Eka_vy == Toka_vy and Eka_oa == Toka_oa:
        sisakkain = True
    
    elif Toka_oa[0]<=Eka_oa[0] and Toka_vy[0]>= Eka_vy[0]:
        if Toka_vy[1]<=Eka_vy[1] and Toka_oa[1]>= Eka_oa[1]:
            sisakkain = True

    return sisakkain  


def leikkaako(Ivy, Ioa, Pvy, Poa):
    #Leikkaako I:n sivut nelkulmion P osiin?
    leikkaa = False
    leikkaja_x=[]
    leikkaaja_y=[]
    
    if Ivy[0]<Poa[0] and Ivy[0]>Pvy[0]:
        leikkaa =True
        leikkaja_x.append(Ivy[0])
    if Ioa[0]<Poa[0] and Ioa[0]>Pvy[0]:
        leikkaa = True
        leikkaja_x.append(Ioa[0])
    if Ivy[1]<Pvy[1] and Ivy[1]>Poa[1]:
        leikkaa = True
        leikkaaja_y.append(Ivy[1])
    if Ioa[1]<Pvy[1] and Ioa[1]>Poa[1]:
        leikkaa = True
        leikkaaja_y.append(Ioa[1])

    return leikkaa, leikkaja_x, leikkaaja_y

def osittelu(Nyv, Noa,xät,yyt):
    xät.append(Nyv[0])
    xät.append(Noa[0])
    yyt.append(Nyv[1])
    yyt.append(Noa[1])
    xät = sorted(set(xät))
    yyt = sorted(set(yyt))
    Nkulmiot=[]

    for ii in range(len(xät)-1):
        for jj in range(len(yyt)-1):
            Nkulmiot.append([ (xät[ii],yyt[jj+1]),(xät[ii+1],yyt[jj]) ])

    return Nkulmiot
 

def testaa_leikkaukset(Eka_vy,Eka_oa,Toka_vy,Toka_oa, cb_testi=False, B_vy=(0,0), B_oa=(0,0)):
    # Testataan leikkaako Eka nelikulmio  Tokaa
    # Jos leikkaa, osiin jako, testaukset pikkuneliö kerrallaan onko Ekan sisällä
    # Kun kutsutaan cb_testinä, tarkistaa myös leikkaukset B:n kanssa               # EI leikkaa toista kertaa bc testissä

    Toka_ala = 0
    #print('ennen leikkausta', Eka_vy,Eka_oa,Toka_vy,Toka_oa)
    (leikkaa,leikkaajat_x,leikkaajat_y)=leikkaako(Eka_vy,Eka_oa,Toka_vy,Toka_oa)
    #print('leikkaa',leikkaa,leikkaajat_x, leikkaajat_y)
    if not leikkaa:
        #print('täällä',cb_testi,Eka_vy,Eka_oa,Toka_vy,Toka_oa)     # Tästä puuttuu leikkaukset kun ei tarvi leikata A:n ja B:n välillä mutta pitäis B:n ja C:n välillä
        if not (nelikulmio_sisalla(Eka_vy,Eka_oa,Toka_vy,Toka_oa)):
            if not cb_testi:
                Toka_ala = ala(Toka_vy,Toka_oa)
            else:
                Toka_ala = Toka_ala+testaa_leikkaukset(B_vy, B_oa, Toka_vy,Toka_oa) 
            #print('ala', Toka_ala)
    else:
        #print('nyt taalla',cb_testi,Eka_vy,Eka_oa,Toka_vy,Toka_oa,B_vy, B_oa)
        uudet_kulmiot=osittelu(Toka_vy,Toka_oa,leikkaajat_x, leikkaajat_y)
        #print('uudet kulmiot', uudet_kulmiot)
        for ii in range(len(uudet_kulmiot)):
            sisallako = False
            sisallako = nelikulmio_sisalla(Eka_vy,Eka_oa,uudet_kulmiot[ii][0],uudet_kulmiot[ii][1])
            if not sisallako:
                if not cb_testi:
                    Toka_ala = Toka_ala + ala(uudet_kulmiot[ii][0],uudet_kulmiot[ii][1])
                else:
                    #print('konfused',B_vy, B_oa,uudet_kulmiot[ii][0],uudet_kulmiot[ii][1])
                    Toka_ala = Toka_ala+testaa_leikkaukset(B_vy, B_oa,uudet_kulmiot[ii][0],uudet_kulmiot[ii][1])      
    
    return Toka_ala  



def suurimman_ulkopuolella(Avy,Aoa,Bvy,Boa,Cvy,Coa):
    # Lasketaan kahdesta muusta ne osat jotka ovat isoimman suorakulmion ulkopuolella
    
    # Testataan A ja B 
    B_ala=0
    C_ala=0
    #print(Avy,Aoa,Bvy,Boa,Cvy,Coa)

    if (nelikulmio_sisalla(Avy,Aoa,Bvy,Boa)):
        B_ala=0
    else:
        B_ala=testaa_leikkaukset(Avy,Aoa,Bvy,Boa)
    
    # Testataan A ja C
    if (nelikulmio_sisalla(Avy,Aoa,Cvy,Coa)):
        #print('test1')
        C_ala = 0
    elif (nelikulmio_sisalla(Bvy,Boa,Cvy,Coa)):
        #print('test2')
        C_ala = 0
    else:
        #print('test3')
        C_ala=testaa_leikkaukset(Avy,Aoa,Cvy,Coa,True, Bvy,Boa)

    #print(B_ala,C_ala)
    return B_ala+C_ala



def area(rec1, rec2, rec3):
    # Etsii isoimman nelikulmion ja käyttää sen alaa pohjana
    # Isoimman nelikulmion ulkopuolella oleva lisättävä ala lasketaan funktiossa
    # Käytetään kulmille tuplea (x,y)

    #piste1vy = (rec1[0],rec1[1])
    #piste1oa = (rec1[2],rec1[3])
    #piste2vy =  (rec2[0],rec2[1])
    #piste2oa =  (rec2[2],rec2[3])
    #piste3vy =  (rec3[0],rec3[1])
    #piste3oa =  (rec3[2],rec3[3])

    ala1=ala((rec1[0],rec1[1]),(rec1[2],rec1[3]))
    #print((rec1[0],rec1[1]),(rec1[2],rec1[3]))
    ala2=ala((rec2[0],rec2[1]),(rec2[2],rec2[3]))
    ala3=ala((rec3[0],rec3[1]),(rec3[2],rec3[3]))

    Yhteisala = 0

    Alat = [ala1,ala2,ala3]
    #print(Alat)
    jarjestys = sorted(range(len(Alat)), key=lambda k: Alat[k],reverse=True)
    #print(jarjestys)
    


    if jarjestys[0]== 0:
        if jarjestys[1] == 1:
            Yhteisala = ala1 + suurimman_ulkopuolella((rec1[0],rec1[1]),(rec1[2],rec1[3]),(rec2[0],rec2[1]),(rec2[2],rec2[3]),(rec3[0],rec3[1]),(rec3[2],rec3[3]))
        else:
            Yhteisala = ala1 + suurimman_ulkopuolella((rec1[0],rec1[1]),(rec1[2],rec1[3]),(rec3[0],rec3[1]),(rec3[2],rec3[3]),(rec2[0],rec2[1]),(rec2[2],rec2[3]))
    elif jarjestys[0] == 1:
        if jarjestys[1] == 0:
            Yhteisala = ala2+ suurimman_ulkopuolella((rec2[0],rec2[1]),(rec2[2],rec2[3]),(rec1[0],rec1[1]),(rec1[2],rec1[3]),(rec3[0],rec3[1]),(rec3[2],rec3[3]))
        else:
            Yhteisala = ala2+ suurimman_ulkopuolella((rec2[0],rec2[1]),(rec2[2],rec2[3]),(rec3[0],rec3[1]),(rec3[2],rec3[3]),(rec1[0],rec1[1]),(rec1[2],rec1[3]))
    else: #jarjestys[0] == 2
        if jarjestys[1] == 0:
            Yhteisala= ala3 + suurimman_ulkopuolella((rec3[0],rec3[1]),(rec3[2],rec3[3]),(rec1[0],rec1[1]),(rec1[2],rec1[3]),(rec2[0],rec2[1]),(rec2[2],rec2[3]))
        else:
            Yhteisala= ala3 + suurimman_ulkopuolella((rec3[0],rec3[1]),(rec3[2],rec3[3]),(rec2[0],rec2[1]),(rec2[2],rec2[3]),(rec1[0],rec1[1]),(rec1[2],rec1[3]))


    return Yhteisala




if __name__ == "__main__":
    
    rec1 =(-1,1,1,-1)  # vas ylänurkka, oik alanurkka
    rec2 =(0,3,2,0)
    rec3 =(0,2,3,-2)
    print(area(rec1,rec2,rec3)) # 16
    #rec1 =(-1,1,1,-1)  # vas ylänurkka, oik alanurkka
    #rec2 =(0,3,2,0)
    #rec3 =(0,2,3,-2)
   
#[0,1,2,-2]
#[-1,3,3,2]
#[-2,3,0,2]
   