#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 09:03:47 2019

@author: robson.legramante
"""
dezena = int(input("Digite um número inteiro:"))
num = (dezena // 10)
print("O dígito das dezenas é",num % 10)
