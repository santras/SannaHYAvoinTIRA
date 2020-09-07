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
      
def nelikulmio_sisalla(Eka_vy,Eka_oa,Toka_vy_Toka_oa):
    #onko samat
    #onko sisäkkäin Toka Ekan sisällä
    sisakkain= False
    if Eka_vy == Toka_vy and Eka_oa == Toka_oa:
        sisakkain = True
    
    elif Toka_oa[0]<=Eka_oa[0] and Toka_vy[0]>= Eka_vy[0]:
        if Toka_vy[1]<=Eka_vy[1] and Toka_oa[1]>= Eka_oa[1]:
            sisakkain = True

    return True    



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

def leikkaako(Ivy, Ioa, Pvy, Poa):
    #Leikkaako I:n sivut nelkulmion P osiin?
    leikkaa = False
    leikkaja_x=[]
    leikkaaja_y=[]
    #print('jei',Ivy[0], Ioa[0], Pvy[0],Poa[0])
    #print('jei2',Ivy[1], Ioa[1], Pvy[1],Poa[1])
    
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
        #print('ii',ii)
        for jj in range(len(yyt)-1):
            #print(jj)
            Nkulmiot.append([ (xät[ii],yyt[jj+1]),(xät[ii+1],yyt[jj]) ])
    

    return Nkulmiot
    #print(Nkulmiot, xät,yyt, len(Nkulmiot))

def suurimman_ulkopuolella(Avy,Aoa,Bvy,Boa,Cvy,Coa):
    #Leikkaako A:n sivut pienempää nelikulmiota?
        # Jos ei onko se isomman sisässä vai ulkopuolella?  Paitsi että ulkona voi olla niin että leikkaa?
            # Jos ulkona -> lisää kokonaan ala
            # Jos sisällä -> älä lisää mitään
        # Jos leikkaa -> Pistä pienempi osiin ja katso osille edellinen (osia 2-4)
    # C:lle tarkista sekä B:n että A:n leikkaukset
    
    # Testataan A ja B 
    B_ala=0
    C_ala=0

    (leikkaa,leikkaajat_x,leikkaajat_y)=leikkaako(Avy,Aoa,Bvy,Boa)
    if not leikkaa:
        #print('hep')
        # onko B A:n sisällä?
        if not (onko_piste_sis(Bvy,Avy,Aoa)):   # Tämä pistettä - onko sama kuin kulmio?
            B_ala=ala(Bvy,Boa)
    else:
        uudet_kulmiot=osittelu(Bvy,Boa,leikkaajat_x, leikkaajat_y)
        for ii in range(len(uudet_kulmiot)):
            #print(uudet_kulmiot[ii][0],uudet_kulmiot[ii][1])
            sisallako = False
            sisallako = onko_piste_sis(uudet_kulmiot[ii][0],Avy,Aoa,True)
            if sisallako:
                sisallako = onko_piste_sis(uudet_kulmiot[ii][1],Avy,Aoa,True)
            if not sisallako:
                B_ala=B_ala+ala(uudet_kulmiot[ii][0],uudet_kulmiot[ii][1])

    #print(B_ala)

    #Testataan A ja C (ja sitten B ja C)

    (leikkaa,leikkaajat_x,leikkaajat_y)=leikkaako(Avy,Aoa,Cvy,Coa)
    if not leikkaa:
        #print('hep')
        # onko C A:n sisällä?
        if not (onko_piste_sis(Cvy,Avy,Aoa)):   # Tämä pistettä - onko sama kuin kulmio?
            C_ala=ala(Cvy,Coa)
    else:
        uudet_kulmiot=osittelu(Cvy,Coa,leikkaajat_x, leikkaajat_y)
        for ii in range(len(uudet_kulmiot)):
            #print(uudet_kulmiot[ii][0],uudet_kulmiot[ii][1])
            sisallako = False
            sisallako = onko_piste_sis(uudet_kulmiot[ii][0],Avy,Aoa,True)
            if sisallako:
                sisallako = onko_piste_sis(uudet_kulmiot[ii][1],Avy,Aoa,True)
            if not sisallako:
                C_ala=C_ala+ala(uudet_kulmiot[ii][0],uudet_kulmiot[ii][1])


    print(C_ala)




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
    jarjestys = sorted(range(len(Alat)), key=lambda k: Alat[k],reverse=True)
    #print(jarjestys, Alat)


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
           # print('taal')
            Yhteisala= ala3 + suurimman_ulkopuolella((rec3[0],rec3[1]),(rec3[2],rec3[3]),(rec2[0],rec2[1]),(rec2[2],rec2[3]),(rec1[0],rec1[1]),(rec1[2],rec1[3]))


    return Yhteisala




if __name__ == "__main__":
    rec1 = (-1,1,1,-1)  # vas ylänurkka, oik alanurkka
    rec2 = (0,3,2,0)
    rec3 = (0,2,3,-2)
    print(area(rec1,rec2,rec3)) # 16

    #Test report
    #Test failed when given the following input:
    #[-1,2,2,-1]
    #[-1,2,2,-1]
    #[-1,2,2,-1]
    #Expected output:
    #9
    #Your output:
    #27