# -*- coding: utf-8 -*-

import numpy as np

# Solicita ao usuário para inserir os valores da matriz
print("Insira os valores da matriz 4x4:")
matriz = np.zeros((4, 4))
for i in range(4):
    for j in range(4):
        matriz[i, j] = float(input(f"Digite o valor para o elemento ({i+1}, {j+1}): "))

# Calcula a determinante da matriz usando a função det do NumPy
det = np.linalg.det(matriz)

# Arredonda a determinante para 2 casas decimais
det = round(det, 2)

# Imprime a determinante da matriz arredondada na tela
print(f"A determinante da matriz é: {det}")