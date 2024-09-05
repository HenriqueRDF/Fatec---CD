# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 22:19:31 2023

@author: Henrique Freitas
"""
def obter_numeros():
    numeros = []
    for i in range(3):
        numero = float(input("Digite o número " + str(i+1) + ": "))
        numeros.append(numero)
    return numeros

def encontrar_menor_valor(numeros):
    menor_valor = min(numeros)
    return menor_valor

numeros = obter_numeros()
menor_valor = encontrar_menor_valor(numeros)

print("O menor valor é:", menor_valor)
