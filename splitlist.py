
#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#import sys
#from time import time



def count(lista):

    ll=len(lista)
    pikkuset = []   
    isot = [0]*ll   # Alustan isot nollaksi

    for ii in range (ll):
        if pikkuset == []:
            pikkuset.append(lista[ii])
        else:
            pikkuset.append(max(pikkuset[ii-1],lista[ii]))

    for ii in range (ll-1,-1,-1):
        #print(ii)
        if ii == ll-1:
            isot[ii] = lista [ii]
        else:
            isot [ii] = min(isot[ii+1],lista[ii])

    print(lista)
    print(pikkuset)
    print(isot)
    laskuri = 0
    
    for ii in range (1,ll-1):
        if pikkuset[ii-1]<isot[ii]:
            laskuri += 1
            #print(ii)

    return laskuri



if __name__ == "__main__":
    #print(count([1,2,3,4,5])) # 4
    #print(count([5,4,3,2,1])) # 0
    print(count([2,1,2,5,7,6,9])) # 3