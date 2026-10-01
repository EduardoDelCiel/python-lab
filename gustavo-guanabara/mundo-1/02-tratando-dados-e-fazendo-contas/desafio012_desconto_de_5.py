"""
Desafio 012: Desconto de 5%
Mundo 1 · Tratando dados e fazendo contas

Enunciado: faça um algoritmo que leia o preço de um produto e mostre seu novo
preço, com 5% de desconto.
Conceitos: porcentagem
"""

Preco = float(input("Qual o preço do produto? "))

Desconto = Preco - (Preco * 0.05)      # 5% = 5/100 = 0.05

print("O novo preço é {}".format(Desconto))

# DICA: essa variável guarda o preço novo, e não o valor do desconto.
# Um nome como NovoPreco deixaria isso claro para quem lê o código.
