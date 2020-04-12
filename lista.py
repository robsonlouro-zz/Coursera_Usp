# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 18:27:28 2020

@author: robso
"""
n = 1
lista = []
while n != 0:
    n = int(input('Digite um numero - 0 para finalizar: '))
    lista.append(n)
cont = len(lista) - 1

for item in lista:
    print(item)
    