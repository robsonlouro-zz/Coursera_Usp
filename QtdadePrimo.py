# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 09:38:14 2020

@author: robso
"""
def ePrimo(x):
    fator = 2
    if x == 2:
        return True
    while x % fator != 0 and fator < x/2:
        fator = fator + 1
    if x % fator == 0:
        return False
    else:
        return True


n = int(input("Digite um numero inteiro: "))
primo = 0
while n > 0:
    if ePrimo(n) == True:
        primo = primo + 1
    n = n-1

print(primo)
    
    