"""
Desafio 005: Antecessor e sucessor
Mundo 1 · Tratando dados e fazendo contas

Enunciado: faça um programa que leia um número inteiro e mostre na tela o seu
sucessor e o seu antecessor.
Conceitos: operadores + e -
"""

Numero = int(input("Digite um numero: "))
Antecessor = Numero - 1
Sucessor = Numero + 1
print("O antecessor é {} e o sucessor é {}".format(Antecessor, Sucessor))

# Forma otimizada: faz a conta direto dentro do format(), sem criar variáveis
print("O antecessor é {} e o sucessor é {}".format(Numero - 1, Numero + 1))
