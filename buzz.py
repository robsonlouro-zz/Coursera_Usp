#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 11:08:18 2019

@author: robson.legramante
Exercícios 3 - FizzBuzz parcial, parte 2
Receba um número inteiro na entrada e imprima

Buzz

se o número for divisível por 5. 
Caso contrário, imprima o mesmo número que foi dado na entrada.
"""

num = int(input("Digite um número:"))
res = num % 5
if (res == 0):
    print("Buzz")
else:
    print(num)
