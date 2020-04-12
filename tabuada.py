#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 11:44:17 2020

@author: robson.legramante
"""

linha = 1
coluna = 1
while linha <= 10:
    while coluna <= 10:
        print(linha, ' x ', coluna, ' = ', linha*coluna,end = '\t')
        coluna += 1
    linha +=1
    coluna = 1    
    print()    