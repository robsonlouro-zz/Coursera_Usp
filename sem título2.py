# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 18:43:17 2020

@author: robso
"""
def remove_repetidos(lista):
    li = []
    x = 0
    while x < len(lista):
        y = 0
        while y < len(lista):
            if lista[x] != lista[y]:
                del(lista[y])
            y = y + 1
        x = x + 1
    return lista


print(remove_repetidos([7,3,33,12,3,3,3,7,12,100]))