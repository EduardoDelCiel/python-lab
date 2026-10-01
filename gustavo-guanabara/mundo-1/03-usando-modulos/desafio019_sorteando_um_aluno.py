"""
Desafio 019: Sorteando um aluno
Mundo 1 · Usando módulos

Enunciado: um professor quer sortear um dos seus quatro alunos para apagar o
quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo
na tela o nome do escolhido.
Conceitos: from random import choice, lista
"""

from random import choice

PrimeiroAluno = input("Primeiro aluno: ")
SegundoAluno = input("Segundo aluno: ")
TerceiroAluno = input("Terceiro aluno: ")
QuartoAluno = input("Quarto aluno: ")
ListaAluno = [PrimeiroAluno, SegundoAluno, TerceiroAluno, QuartoAluno]

AlunoEscolhido = choice(ListaAluno)     # escolhe 1 item da lista ao acaso

print(AlunoEscolhido)
