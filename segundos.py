#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 09:14:25 2019

@author: robson.legramante
"""
seg  = int(input("Por favor, entre com o número de segundos que deseja converter: "))
min  = seg // 60
seg  = seg % 60
hora = min // 60
min  = min % 60
dia  = hora // 24
hora = hora % 24
print(dia,"dias,",hora,"horas,",min,"minutos e",seg,"segundos.")
