"""
Desafio 011: Pintando a parede
Mundo 1 · Tratando dados e fazendo contas

Enunciado: faça um programa que leia a largura e a altura de uma parede em
metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
Conceitos: float(), multiplicação e divisão
"""

Largura = float(input("Qual a largura da parede? "))
Altura = float(input("Qual a altura da parede? "))

Area = Largura * Altura
Tinta = Area / 2

print("Voce vai precisar de {} litros de tinta para pintar sua parede".format(Tinta))
