"""
Desafio 030: Par ou ímpar
Mundo 1 · Condições

Enunciado: crie um programa que leia um número inteiro e mostre na tela se ele
é PAR ou ÍMPAR.
Conceitos: resto da divisão (%), if/else
"""

Numero = int(input("Digite um numero inteiro qualquer: "))

if Numero % 2 == 0:         # resto da divisão por 2 é zero → par
    print("Numero par")
else:
    print("Numero impar")
