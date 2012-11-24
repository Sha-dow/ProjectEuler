# -*- coding: cp1252 -*-
def fibonacci(n):
    """Palauta n:n ensimmäisen parillisen fibonaccin luvun summa"""
    a, b = 1, 2
    z, x, c = 2, 0, 0
    tulos = 0

    print(a)
    
    #Silmukka, jonka sisällä termit lasketaan
    while x <= n - 2:

        #Lasketaan fibonaccin sarjan seuraava termi
        c = a+b 
        a = b
        b = c

        #tulostetaan termi näytölle
        print(a)

        #jos luku on suurempi kuin 4 000 000 keskeytetään
        if a >= 4000000:
            break
            
        #Tarkistetaan termin parillisuus, jos parillinen niin lisätään tulokseen
        if a%z == 0:
            tulos = tulos + a

        #Kasvatetaan silmukkafunktion arvoa yhdellä
        x += 1
    #Palautetaan tulos
    return tulos
