# -*- coding: cp1252 -*-
def jako_tasan(n):
    """Laskee luvun, joka voidaan jakaa tasan kaikilla luvuilla 1-n"""
    x, y, = 1, 0
    lopeta = False
    tulos = 0
    
    while True:

        y = y + n 

        for x in range(1, n+1):
            if y%x != 0:
                break
        else:
            tulos = y
            break
        
    #Palautetaan tulos
    return tulos
