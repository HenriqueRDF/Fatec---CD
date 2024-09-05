# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 22:20:01 2023

@author: Henrique Freitas
"""

import numpy as np
import matplotlib.pyplot as plt

def plotar_grafico_cosseno():
    x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
    y = np.cos(x)
    plt.plot(x, y)
    plt.title('Gráfico da Função Cosseno')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

plotar_grafico_cosseno()
