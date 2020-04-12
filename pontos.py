#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 12:04:02 2019

@author: robson.legramante

Receba 4 números na entrada, um de cada vez. Os dois primeiros devem 
corresponder, respectivamente, às coordenadas x e y de um ponto 
em um plano cartesiano. Os dois últimos devem corresponder, 
respectivamente, às coordenadas x e y de um outro ponto no mesmo plano.

Calcule a distância entre os dois pontos. Se a distância for maior 
ou igual a 10, imprima

longe

na saída. Caso o contrário, quando a distância for menor que 10, imprima

perto

Dica: lembre-se que a fórmula da distância para dois 
pontos num plano cartesiano é a seguinte:\
d(x,y) = raiz((x1-x2)quadrado + (y1-y2)quadrado)


"""
import math as m
x1 = float(input("x1:"))
y1 = float(input("y1:"))
x2 = float(input("x2:"))
y2 = float(input("y2:"))

dist = m.sqrt(pow(x1-x2,2)+pow(y1-y2,2))
if (dist >= 10):
    print("longe")
else:
    print("perto")