"""
Desafio 034: Aumento por faixa salarial
Mundo 1 · Condições

Enunciado: escreva um programa que pergunte o salário de um funcionário e
calcule o valor do seu aumento. Para salários superiores a R$1.250,00,
calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
Conceitos: if/else, porcentagem
"""

Salario = float(input("Qual o seu salario? "))

if Salario <= 1250:
    Salario = Salario + (Salario * 0.15)
    print("Salario ajustado é {}".format(Salario))
else:
    Salario = Salario + (Salario * 0.10)
    print("Salario ajustado é {}".format(Salario))

# DICA: como no desafio 031, o print é igual nos dois caminhos e pode ficar
# uma vez só, depois do if/else.
