"""
Desafio 031: Preço da passagem
Mundo 1 · Condições

Enunciado: desenvolva um programa que pergunte a distância de uma viagem em
km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até
200 km e R$0,45 para viagens mais longas.
Conceitos: if/else, operador <=
"""

Kms = float(input("Quantos km tem a viagem? "))

if Kms <= 200:
    Preco = Kms * 0.50
    print("A viagem custa R$ {}".format(Preco))
else:
    Preco = Kms * 0.45
    print("A viagem custa R$ {}".format(Preco))

# DICA: o print é igual nos dois caminhos. Dá para deixar no if/else só o que
# muda (o cálculo) e escrever o print uma vez só, depois do if/else.
