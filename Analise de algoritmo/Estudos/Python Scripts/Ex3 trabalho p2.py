# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 22:06:38 2023

@author: Henrique Freitas
"""

lista = ["de cinema)", "que satisfaça o contexto", "sequenciamento de listas", "para mostrar",
         "a seqüência dos", "no console", "(para quem gosta", "contida na mesma",
         "elementos da lista", "Utilizar o", "da frase", "do significado"]
lista.sort()
dimensao = len(lista)
elementos_impares = lista[1::2]
frase_ordenada = " ".join(lista)
print("Frase ordenada:", frase_ordenada)
print("Dimensão da lista:", dimensao)
print("Elementos ímpares:", elementos_impares)
