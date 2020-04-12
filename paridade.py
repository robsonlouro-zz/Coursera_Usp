#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 11:01:55 2019

@author: robson.legramante
Exercício 1 - Par ou ímpar?
Receba um número inteiro na entrada e imprima

par

quando o número for par ou

ímpar

quando o número for ímpar.
"""

num = int(input("Digite um número:"))
if (num % 2 == 0):
    print("par")
else:
    print("ímpar")
    