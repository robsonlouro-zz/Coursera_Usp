# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 15:20:23 2020

@author: robso
"""

def minmax(temperaturas):
    print("A tempratura minima no periodo foi de ",minimo(temperaturas),"C")
    print("A tempratura maxima no periodo foi de ",maximo(temperaturas),"C") 


def minimo(temp):
    x = 0
    menor = temp[0]
    while x < len(temp):
        if menor > temp[x]:
            menor = temp[x]
        x = x+1
    return menor
        
def maximo(temp):
    x = 0
    maior = temp[0]
    while x < len(temp):
        if maior < temp[x]:
            maior = temp[x]
        x = x+1
    return maior

def testaMinima():
    print("inicio")
    temp = [0]
    if minimo(temp) != 0:
        print("Erro para 0")

    temp = [3,2,1]
    if minimo(temp) != 1:
        print("Erro para 3,2,1")
        
    print("Fim")
    
minmax([-15,0,34,23])