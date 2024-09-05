# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 22:21:28 2023

@author: Henrique Freitas
"""

from calcula_medias import calcular_medias_algoritmos_alunos


def main():
    alunos = []
    notas = []

    try:
        for i in range(6):
            aluno = input("Digite o nome do aluno: ")
            alunos.append(aluno)

            nota = float(input(f"Digite a nota de {aluno} em Algoritmos e Introdução a Computação: "))
            notas.append(nota)

        medias = calcular_medias_algoritmos_alunos(alunos, notas)

        if medias:
            for i in range(len(alunos)):
                print(f"Aluno: {alunos[i]} - Média: {medias[i]}")

    except ValueError as error:
        print(f"Erro: {error}")


if __name__ == '__main__':
    main()
