# -*- coding: cp1252 -*-
def fibonacci(n):
    """Palauta n:n ensimm�isen parillisen fibonaccin luvun summa"""
    a, b = 1, 2
    z, x, c = 2, 0, 0
    tulos = 0

    print(a)
    
    #Silmukka, jonka sis�ll� termit lasketaan
    while x <= n - 2:

        #Lasketaan fibonaccin sarjan seuraava termi
        c = a+b 
        a = b
        b = c

        #tulostetaan termi n�yt�lle
        print(a)

        #jos luku on suurempi kuin 4 000 000 keskeytet��n
        if a >= 4000000:
            break
            
        #Tarkistetaan termin parillisuus, jos parillinen niin lis�t��n tulokseen
        if a%z == 0:
            tulos = tulos + a

        #Kasvatetaan silmukkafunktion arvoa yhdell�
        x += 1
    #Palautetaan tulos
    return tulos
