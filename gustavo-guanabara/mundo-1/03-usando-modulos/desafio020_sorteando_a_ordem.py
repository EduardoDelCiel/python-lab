"""
Desafio 020: Sorteando a ordem de apresentação
Mundo 1 · Usando módulos

Enunciado: o mesmo professor do desafio 019 quer sortear a ordem de
apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos
quatro alunos e mostre a ordem sorteada.
Conceitos: from random import shuffle, lista
"""

from random import shuffle

PrimeiroAluno = input("Primeiro aluno: ")
SegundoAluno = input("Segundo aluno: ")
TerceiroAluno = input("Terceiro aluno: ")
QuartoAluno = input("Quarto aluno: ")
ListaAluno = [PrimeiroAluno, SegundoAluno, TerceiroAluno, QuartoAluno]

shuffle(ListaAluno)     # embaralha a própria lista (não cria uma nova)
print(ListaAluno)
