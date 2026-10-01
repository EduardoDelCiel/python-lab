"""
Desafio 014: Celsius para Fahrenheit
Mundo 1 · Tratando dados e fazendo contas

Enunciado: escreva um programa que leia uma temperatura digitada em graus
Celsius e a converta para graus Fahrenheit.
Conceitos: fórmula com * e +, ordem de precedência
"""

TemperaturaC = float(input("Temperatura em Celsius: "))

Fahrenheit = TemperaturaC * 1.8 + 32     # a multiplicação acontece antes da soma

print("A temperatura em Fahrenheit é {}ºF".format(Fahrenheit))
