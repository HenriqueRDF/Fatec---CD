# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 21:36:42 2023

@author: Henrique Freitas
"""

def calcular_media(nome, notas):
    media = sum(notas) / len(notas)
    if media >= 5:
        return (nome, True)
    else:
        return (nome, False)

alunos = []
notas_alunos = []

for _ in range(10):
    nome = input("Digite o nome do aluno: ")
    alunos.append(nome)
    notas = []
    for disciplina in ["História", "Matemática", "Português", "Geografia", "Ciências"]:
        nota = float(input(f"Digite a nota de {disciplina} para {nome}: "))
        notas.append(nota)
    notas_alunos.append(notas)

for i in range(len(alunos)):
    aluno = alunos[i]
    notas = notas_alunos[i]
    resultado = calcular_media(aluno, notas)
    print(f"Aluno: {resultado[0]} - Aprovado: {resultado[1]}")
