#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 11:05:05 2019

@author: robson.legramante
Exercícios 2 - FizzBuzz parcial, parte 1
Receba um número inteiro na entrada e imprima

Fizz

se o número for divisível por 3. 
Caso contrário, imprima o mesmo número que foi dado na entrada.
"""

num = int(input("Digite um número:"))
res = num % 3
if (res == 0):
    print("Fizz")
else:
    print(num)