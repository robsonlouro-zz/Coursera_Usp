# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 10:43:19 2020

@author: robso
"""

larg = int(input("Digite a largura: "))
alt = int(input("Digite a altura: "))
while alt > 0:
    print("#" * larg)
    alt = alt - 1