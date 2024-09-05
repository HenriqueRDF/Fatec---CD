# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 22:19:24 2023

@author: Henrique Freitas
"""

def calcular_medias_algoritmos_alunos(alunos, notas):
    try:
        if len(alunos) != len(notas):
            raise ValueError("O número de alunos e notas não coincide.")
        medias = []
        for i in range(len(alunos)):
            nota = notas[i]
            if nota < 0 or nota > 10:
                raise ValueError("As notas devem estar entre 0 e 10.")
            medias.append(nota)
        return medias
    except ValueError as error:
        print(f"Erro: {error}")
        return None
