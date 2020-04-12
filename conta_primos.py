# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 09:38:14 2020

@author: robso
"""
def n_primos(x):
    fator = 2
    y = x
    primo = 1
    cont = 0
    
    while y > 2:
        
        while fator < x:
            if y % fator == 0:
                cont = cont + 1
            fator = fator + 1
        y = y-1
        fator = 2
        if cont == 1:
            primo = primo + 1
        cont = 0
    return primo

n = 0
while n < 2:
    n = int(input("Digite um numero inteiro: "))


print(n_primos(n))
    
    