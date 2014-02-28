# -*- coding: cp1252 -*-
def checkIfPalindrome(candidate):
    if ((len(candidate) % 2) == 0):
        start = candidate[:int(len(candidate)/2)]
    else:
        start = candidate[:int((len(candidate)/2)+1)]

    start = start[::-1]
    if (candidate.endswith(start)):
        return True
    else:
        return False

def palindrome(n):
    """Largest palindrome made from the product of two n-digit numbers"""
    number = ""
    largest = 0
    
    for i in range(n):
        number += "9"

    for i in range(int(number)+1):
        for l in range(int(number)+1):
            if (i*l) > largest:
                if checkIfPalindrome(str(i*l)):
                    largest = (i*l)
    return(largest)
