# -*- coding: utf-8 -*-
"""
Created on Wed May 31 23:54:36 2023

@author: Henrique Freitas
"""
import numpy as np

def calcular_entropia(dados):
    valores_unicos, contagem = np.unique(dados, return_counts=True)  # Obtém valores únicos e suas contagens
    probabilidades = contagem / len(dados)  # Calcula as probabilidades de cada valor
    entropia = -np.sum(probabilidades * np.log2(probabilidades + 1e-10))  # Calcula a entropia
    return entropia

def calcular_maxima_entropia(dados):
    num_valores = np.max(dados) + 1  # Obtém o número de valores distintos
    probabilidade_maxima = 1 / num_valores  # Probabilidade uniforme para cada valor
    maxima_entropia = -np.log2(probabilidade_maxima)  # Calcula a máxima entropia
    return maxima_entropia

# Dados fornecidos
bolas = np.array([1, 3, 7, 15, 23, 44, 13, 16, 35, 41, 42, 47, 1, 9, 17, 30, 31, 44, 6, 23, 25, 33, 34, 47, 6, 16, 21, 24, 26, 45, 1, 19, 22, 32, 39, 45, 9, 12, 35, 44, 47, 48, 1, 4, 5, 16, 38, 50, 6, 11, 12, 14, 15, 18, 4, 6, 10, 42, 47, 48])

entropia = calcular_entropia(bolas)
maxima_entropia = calcular_maxima_entropia(bolas)

print("Entropia:", entropia)
print("Máxima Entropia:", maxima_entropia)

