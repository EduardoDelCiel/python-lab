"""
Desafio 035: Dá para formar um triângulo?
Mundo 1 · Condições

Enunciado: desenvolva um programa que leia o comprimento de três retas e diga
ao usuário se elas podem ou não formar um triângulo.
Conceitos: operador and com três condições
"""

n1 = float(input("Reta 1: "))
n2 = float(input("Reta 2: "))
n3 = float(input("Reta 3: "))

# Cada lado precisa ser menor que a soma dos outros dois.
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print("É possível formar um triângulo")
else:
    print("Não é possível formar um triângulo")
