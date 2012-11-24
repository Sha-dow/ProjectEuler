# -*- coding: cp1252 -*-
def euler(n):
    """Palauta n:n ensimmäisen 3 ja 5 jaollisen luvun summa"""
    a, b, x = 3, 5, 0
    tulos = 0
    while x <= n:
        if x%a == 0:
            tulos = tulos + x
        elif x%b == 0:
            tulos = tulos + x
        x += 1
    return tulos
