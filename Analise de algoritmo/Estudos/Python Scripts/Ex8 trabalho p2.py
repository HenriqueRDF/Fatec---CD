# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 22:19:48 2023

@author: Henrique Freitas
"""

import random

def simular_jogadas_dado():
    jogadas = []
    for _ in range(3):
        valor = random.randint(1, 6)
        jogadas.append(valor)

    return jogadas

jogadas = simular_jogadas_dado()

print("As jogadas do dado foram:", jogadas)
