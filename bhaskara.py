#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 11:16:09 2019

@author: robson.legramante

"""
import math as m

a = float(input("Digite o A:"))
b = float(input("Digite o B:"))
c = float(input("Digite o C:"))

delta = (m.pow(b,2))-(4*a*c)
if (delta > 0):
    x1=(-b+m.sqrt(delta))/(2*a)
    x2=(-b-m.sqrt(delta))/(2*a)
    if (x1 > x2):
        print("as raízes da equação são",x2,"e",x1)
    else:
        print("as raízes da equação são",x1,"e",x2)
elif (delta == 0):
    print("a raiz desta equação é",(-b+m.sqrt(delta))/(2*a))
else:
    print("esta equação não possui raízes reais")
    