
#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#import sys
#from time import time



def count(ss):

    kirjaimet = []                      # kirjain[0] on viimeistä edellisin ja kirjain[1] edellisin jonon kirjain
    laskin_aiempi = 0
    laskin_uudempi = 0
    yhteen_laskin = 0
    print(ss)

    for ii in range(len(ss)) :
        if len(kirjaimet)<2:                # kaksi ensimmäistä kirjainta
            if len(kirjaimet)<1:            # ihan eka kirjain
                kirjaimet.append(ss[ii])
                laskin_aiempi +=1
                #print('eka')       
            elif ss[ii] in kirjaimet  :   # seuraava kirjain jos sama kuin edellinen
                laskin_aiempi +=1
                #print('sama kun eka')

            else:
                kirjaimet.append(ss[ii])       # nyt 2 erilaista kirjainta minijonossa
                yhteen_laskin += laskin_aiempi
                laskin_uudempi +=1
                #print('toka',ss[ii],laskin_aiempi)
                

        else:                               # seuraavat kirjaimet
            if ss[ii] in kirjaimet:         # jos sama kuin 2 edellistä
                if ss[ii] == kirjaimet[1] :  # jos sama kuin viimeisin
                    yhteen_laskin += laskin_aiempi
                    laskin_uudempi += 1
                    #print('sama kun viimeisin', ii, ss[ii], laskin_aiempi)
                    
                else:                       # jos sama kuin viimeistä edellinen
                    apu =kirjaimet[0]

                    kirjaimet [0] = kirjaimet [1] # vaihdetaan päikseen
                    kirjaimet [1] = apu
                    laskin_aiempi += laskin_uudempi
                    yhteen_laskin += laskin_aiempi
                    laskin_uudempi = 1 
                    #print ('sama kun viimeistä edellisin', ii, ss[ii], laskin_aiempi)


            else:
                kirjaimet[0] = kirjaimet [1]    # jos eri kun 2 viimeisintä
                kirjaimet [1] = ss[ii]
                laskin_aiempi = laskin_uudempi
                laskin_uudempi = 1
                yhteen_laskin += laskin_aiempi
                #print('uusi kirjain', ii, ss[ii], laskin_aiempi)

    return yhteen_laskin

if __name__ == "__main__":
    print(count("aaaa")) # 0
    print(count("abab")) # 6
    print(count("aabacba")) # 8