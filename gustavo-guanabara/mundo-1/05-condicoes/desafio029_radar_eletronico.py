"""
Desafio 029: Radar eletrônico
Mundo 1 · Condições

Enunciado: escreva um programa que leia a velocidade de um carro. Se ele
ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado. A multa
vai custar R$7,00 por cada km acima do limite.
Conceitos: if/else, operador >
"""

Velocidade = float(input("Qual a velocidade do carro? "))

if Velocidade > 80:
    Velocidade = Velocidade - 80
    Multa = 7 * Velocidade
    print("Excesso de velocidade! Voce foi multado em R$ {}".format(Multa))
else:
    print("Tudo certo, chefe!")

# DICA: depois da subtração, a variável Velocidade passa a guardar o EXCESSO,
# e não mais a velocidade. Uma variável nova deixa isso mais claro:
#   excesso = Velocidade - 80
#   multa = excesso * 7
