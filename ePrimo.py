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
while n > 0:
    if ePrimo(n):
        print (n, "é primo")
    else:
        print(n, "nao é primo")
    n = int(input("Digite um numero inteiro: "))
    
    