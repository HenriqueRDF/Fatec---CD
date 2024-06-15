# -*- coding: utf-8 -*-
import numpy as np

# Solicita ao usuário para inserir os valores da matriz
print("Insira os valores da matriz (separados por vírgula e espaço):")
valores = input().split(", ")
dimensao = int(np.sqrt(len(valores)))
matriz = np.array([float(valores[i]) for i in range(len(valores))]).reshape(dimensao, dimensao)

# Calcula a determinante da matriz usando a função det do NumPy
det = np.linalg.det(matriz)

# Imprime a determinante da matriz na tela
print(f"A determinante da matriz é: {det}")