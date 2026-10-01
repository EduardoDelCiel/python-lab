"""
Desafio 013: Aumento de salário
Mundo 1 · Tratando dados e fazendo contas

Enunciado: faça um algoritmo que leia o salário de um funcionário e mostre seu
novo salário, com 15% de aumento.
Conceitos: porcentagem
"""

Salario = float(input("Qual o seu salario? "))
Aumento = Salario + (Salario * 0.15)

print("O seu salario foi reajustado para {}".format(Aumento))

# DICA: como no desafio 012, a variável guarda o salário novo, e não o aumento
# (um nome como NovoSalario seria mais claro).
# Atalho: Salario + Salario * 0.15 é o mesmo que Salario * 1.15.
