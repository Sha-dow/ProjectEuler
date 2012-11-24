# -*- coding: cp1252 -*-
def primesum(n):
    """Laskee n:ää pienempien alkulukujen summan"""

    alkuluku = 0
    luvut = []
    temp = []
    tulos = 0

    for y in range(2, 40):
        for x in range(2, y):
            if y % x == 0:
                break
        else:
            luvut.append(y)

    if n > 40:
        for y in range(40, n):
            for x in luvut:
                if y % x == 0:
                    break
            else:
                print(y)
                luvut.append(y)
                
    print'Number array created, starting to find primes'

    while len(luvut) != 0:
        
        alkuluku = luvut.pop(0)
        #print 'alkuluku'
        print alkuluku
        tulos = tulos + alkuluku

        for i in luvut[:]:
            
            if i % alkuluku == 0:
                luvut.remove(i)
                

    print 'Result:'
    #Palautetaan tulos
    return tulos
