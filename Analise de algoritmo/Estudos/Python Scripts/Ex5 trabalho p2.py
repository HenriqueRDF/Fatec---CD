# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 22:19:17 2023

@author: Henrique Freitas
"""
numeros_pares = list(range(2, 21, 2))
numeros_impares = list(range(1, 20, 2))
soma_numeros = [a + b for a, b in zip(numeros_pares, numeros_impares)]
print("Números pares:", numeros_pares)
print("Números ímpares:", numeros_impares)
print("Soma dos valores correspondentes:", soma_numeros)
