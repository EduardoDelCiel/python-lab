"""
Desafio 028: Jogo da adivinhação
Mundo 1 · Condições

Enunciado: escreva um programa que faça o computador "pensar" em um número
inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
escolhido. O programa deverá escrever na tela se o usuário venceu ou perdeu.
Conceitos: random.randint(), if/else, ==
"""

import random

Numero = random.randint(0, 5)       # sorteia de 0 a 5 (os dois entram)

ChuteJogador = int(input("Chute um numero entre 0 e 5: "))

if Numero == ChuteJogador:
    print("Voce venceu! O numero era {}".format(Numero))
else:
    print("Voce perdeu! O numero era {}".format(Numero))
