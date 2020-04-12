# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 10:43:19 2020

@author: robso
"""

larg = int(input("Digite a largura: "))
alt = int(input("Digite a altura: "))
alt2 = alt
cont = alt2



while alt > 0:
    if cont == alt2 or cont == 1:
        print("#" * larg)
    else:          
        print("#"," " * (larg - 4),"#")
    alt = alt - 1
    cont = cont - 1
