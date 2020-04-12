# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 16:31:19 2020

@author: robso
"""
def remove_repetidos(lista):
    lis = []
    for x in lista:
        if x not in lis:
            lis.append(x)
    lis.sort()
    return lis
