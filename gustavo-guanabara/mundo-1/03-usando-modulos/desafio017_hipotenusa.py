"""
Desafio 017: Hipotenusa
Mundo 1 · Usando módulos

Enunciado: faça um programa que leia o comprimento do cateto oposto e do
cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da
hipotenusa.
Conceitos: from math import hypot, formatação {:.2f}
"""

from math import hypot

CatetoOposto = float(input("Cateto oposto: "))
CatetoAdjacente = float(input("Cateto adjacente: "))

Hipotenusa = hypot(CatetoOposto, CatetoAdjacente)

print("Hipotenusa é igual a {:.2f}".format(Hipotenusa))

# DICA: o hypot() faz o teorema de Pitágoras. Sem módulo, a conta seria:
#   (CatetoOposto ** 2 + CatetoAdjacente ** 2) ** (1/2)
