"""
Desafio 015: Aluguel de carro
Mundo 1 · Tratando dados e fazendo contas

Enunciado: escreva um programa que pergunte a quantidade de km percorridos por
um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o
preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.
Conceitos: int() e float() juntos, expressão com parênteses
"""

KmRodados = float(input("Quantos km rodados? "))
DiasAlugado = int(input("Quantos dias o carro foi alugado? "))

PrecoFinal = (KmRodados * 0.15) + (DiasAlugado * 60)

print("O valor total é {}".format(PrecoFinal))
