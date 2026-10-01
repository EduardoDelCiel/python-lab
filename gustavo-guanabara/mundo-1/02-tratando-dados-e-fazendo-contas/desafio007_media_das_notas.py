"""
Desafio 007: Média das notas
Mundo 1 · Tratando dados e fazendo contas

Enunciado: desenvolva um programa que leia as duas notas de um aluno, calcule
e mostre a sua média.
Conceitos: float(), ordem de precedência (parênteses)
"""

PrimeiraNota = float(input("Primeira nota: "))
SegundaNota = float(input("Segunda nota: "))

# Os parênteses são obrigatórios: sem eles, a divisão aconteceria antes da soma.
Media = (PrimeiraNota + SegundaNota) / 2

print("A média é {}".format(Media))

# Jeito simplificado
print("A média é {}".format((PrimeiraNota + SegundaNota) / 2))
