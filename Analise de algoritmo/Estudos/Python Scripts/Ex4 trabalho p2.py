# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 22:16:37 2023

@author: Henrique Freitas
"""

def remover_elementos_pares(lista):
    lista.sort()
    i = len(lista) - 1
    while i >= 0:
        if i % 2 == 0: 
            elemento = lista.pop(i)  
            print("Elemento removido:", elemento)
        i -= 1

    return lista


lista = ["de cinema)", "que satisfaça o contexto", "sequenciamento de listas", "para mostrar",
         "a seqüência dos", "no console", "(para quem gosta", "contida na mesma",
         "elementos da lista", "Utilizar o", "da frase", "do significado"]

elementos_pares = remover_elementos_pares(lista)
print("Elementos pares removidos:", elementos_pares)
