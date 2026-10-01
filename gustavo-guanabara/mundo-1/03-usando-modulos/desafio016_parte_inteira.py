"""
Desafio 016: Parte inteira de um número
Mundo 1 · Usando módulos

Enunciado: crie um programa que leia um número real qualquer pelo teclado e
mostre na tela a sua porção inteira.
Conceitos: import math, math.trunc()
"""

import math

# MELHORIA: havia também a linha `from math import trunc`, que não era usada
# (o código chama math.trunc). As duas linhas carregavam a mesma função.
# Basta escolher um dos dois jeitos de importar.

Numero = float(input("Numero real: "))

Numero = math.trunc(Numero)     # corta a parte decimal: 6.75 → 6
print(Numero)

# Outra forma: importando só a função e guardando o resultado em outra
# variável, para não perder o número digitado:
#
#   from math import trunc
#   numero = float(input("Numero real: "))
#   print("A parte inteira de {} é {}".format(numero, trunc(numero)))
