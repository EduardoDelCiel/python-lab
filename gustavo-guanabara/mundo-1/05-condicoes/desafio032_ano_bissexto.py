"""
Desafio 032: Ano bissexto
Mundo 1 · Condições

Enunciado: faça um programa que leia um ano qualquer e mostre se ele é
bissexto.
Conceitos: operadores lógicos and e or, resto da divisão (%)
"""

Ano = int(input("Digite um ano: "))

# Bissexto: divisível por 4 e não por 100, OU divisível por 400.
if Ano % 4 == 0 and Ano % 100 != 0 or Ano % 400 == 0:
    print("Ano bissexto")
else:
    print("O ano não é bissexto")

# DICA: funciona porque o Python resolve o `and` antes do `or`. Com parênteses
# a regra fica mais fácil de ler:
#   (Ano % 4 == 0 and Ano % 100 != 0) or Ano % 400 == 0
