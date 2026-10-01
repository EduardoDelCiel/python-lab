"""
Desafio 009: Tabuada
Mundo 1 · Tratando dados e fazendo contas

Enunciado: faça um programa que leia um número inteiro qualquer e mostre na
tela a sua tabuada.
Conceitos: multiplicação, .format()
"""

Numero = int(input("Numero que deseja saber a tabuada? "))

x1 = Numero * 1
x2 = Numero * 2
x3 = Numero * 3
x4 = Numero * 4
x5 = Numero * 5
x6 = Numero * 6
x7 = Numero * 7
x8 = Numero * 8
x9 = Numero * 9
x10 = Numero * 10

print("Tabuada {}".format(x1))
print("Tabuada {}".format(x2))
print("Tabuada {}".format(x3))
print("Tabuada {}".format(x4))
print("Tabuada {}".format(x5))
print("Tabuada {}".format(x6))
print("Tabuada {}".format(x7))
print("Tabuada {}".format(x8))
print("Tabuada {}".format(x9))
print("Tabuada {}".format(x10))

# Simplificado
print("Tabuada {}".format(Numero * 1))
print("Tabuada {}".format(Numero * 2))
print("Tabuada {}".format(Numero * 3))
# Assim por diante....

# Outra forma: mostrando a conta inteira, como numa tabuada de verdade (7 x 3 = 21)
print("-" * 12)
print("{} x 1 = {}".format(Numero, Numero * 1))
print("{} x 2 = {}".format(Numero, Numero * 2))
print("{} x 3 = {}".format(Numero, Numero * 3))
print("{} x 4 = {}".format(Numero, Numero * 4))
print("{} x 5 = {}".format(Numero, Numero * 5))
print("{} x 6 = {}".format(Numero, Numero * 6))
print("{} x 7 = {}".format(Numero, Numero * 7))
print("{} x 8 = {}".format(Numero, Numero * 8))
print("{} x 9 = {}".format(Numero, Numero * 9))
print("{} x 10 = {}".format(Numero, Numero * 10))
print("-" * 12)

# No Mundo 2, com o laço for, essas 10 linhas viram só 2.
