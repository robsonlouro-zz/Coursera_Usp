#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 12:04:26 2020

@author: robson.legramante

fatores primos e multiplicidade 
"""
n = int(input('Digite um numero inteiro > 1 '))
fator = 2
mult = 0
while n > 1:
    
    while n % fator == 0:
        mult = mult + 1
        n = n/fator
    if mult > 0:
        print('Fator: ',fator, 'e a multiplicidade é: ',mult)
    fator = fator + 1
    mult = 0
        
  