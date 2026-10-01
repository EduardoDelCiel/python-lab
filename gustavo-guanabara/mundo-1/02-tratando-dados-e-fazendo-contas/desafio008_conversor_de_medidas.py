"""
Desafio 008: Conversor de medidas
Mundo 1 · Tratando dados e fazendo contas

Enunciado: escreva um programa que leia um valor em metros e o exiba
convertido em centímetros e milímetros.
Conceitos: float(), multiplicação
"""

Metro = float(input("Digite o valor em metros: "))

Centimetro = Metro * 100
Milimetro = Metro * 1000

print("Distância em metros: {}m, em centímetros: {}cm, em milímetros: {}mm".format(Metro, Centimetro, Milimetro))
