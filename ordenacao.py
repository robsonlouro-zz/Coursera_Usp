#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 11:12:08 2019

@author: robson.legramante

Receba 3 números inteiros na entrada e imprima

crescente

se eles forem dados em ordem crescente. Caso contrário, imprima

não está em ordem crescente
"""

n1 = int(input("Digite o primeiro numero:"))
n2 = int(input("Digite o segundo numero:"))
n3 = int(input("Digite o terceiro numero:"))
if (n1 < n2 and n2 < n3):
    print("crescente")
else:
    print("não está em ordem crescente")