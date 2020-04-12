# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 16:54:12 2020

@author: robso
"""


def soma_elementos(lista):
    cont = 0
    acum = 0
    while cont < len(lista):
        acum = acum + lista[cont]
        cont = cont +1
    return acum


print(soma_elementos([1,2,1,3,3,4,7,10]))
  
