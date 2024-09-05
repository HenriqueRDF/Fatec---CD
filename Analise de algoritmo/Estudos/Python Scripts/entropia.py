# -*- coding: utf-8 -*-
"""
Created on Wed May 31 23:54:36 2023

@author: Henrique Freitas
"""
import math
from collections import Counter

def calcular_entropia(dados):
    contagem = Counter(dados)
    total_valores = len(dados)
    probabilidades = [contagem[valor] / total_valores for valor in contagem]
    entropia = -sum(p * math.log2(p) for p in probabilidades if p > 0)
    return entropia

def calcular_entropia_maxima(dados):
    total_valores_distintos = len(set(dados))
    entropia_maxima = math.log2(total_valores_distintos)
    return entropia_maxima

dados = [1, 3, 7, 15, 23, 44, 13, 16, 35, 41, 42, 47, 1, 9, 17, 30, 31, 44, 6, 23, 25, 33, 34, 47, 6, 16, 21, 24, 26, 45, 1, 19, 22, 32, 39, 45, 9, 12, 35, 44, 47, 48, 1, 4, 5, 16, 38, 50, 6, 11, 12, 14, 15, 18, 4, 6, 10, 42, 47, 48]
entropia = calcular_entropia(dados)
entropia_maxima = calcular_entropia_maxima(dados)
print("Entropia:", entropia)
print("Entropia Máxima:", entropia_maxima)



