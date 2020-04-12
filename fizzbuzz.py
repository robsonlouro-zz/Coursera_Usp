#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 11:09:25 2019

@author: robson.legramante
Exercícios 4 - FizzBuzz parcial, parte 3
Receba um número inteiro na entrada e imprima

FizzBuzz

na saída se o número for divisível por 3 e por 5. 
Caso contrário, imprima o mesmo número que foi dado na entrada.
"""

num = int(input("Digite um número:"))
res3 = num % 3
res5 = num % 5
if (res3 == 0 and res5 == 0):
    print("FizzBuzz")
else:
    print(num)