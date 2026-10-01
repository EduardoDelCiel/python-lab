"""
Desafio 003: Soma de dois números
Mundo 1 · Tratando dados e fazendo contas

Enunciado: crie um programa que leia dois números e mostre a soma entre eles.
Conceitos: int(), operador +
"""

# int() transforma o texto digitado em número inteiro.
# Sem ele, "2" + "3" daria "23" (juntaria os textos em vez de somar).
n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))
soma = n1 + n2
print("A soma dos dois numeros é igual a {}".format(soma))
