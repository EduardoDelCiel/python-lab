"""
Desafio 010: Conversor de moedas
Mundo 1 · Tratando dados e fazendo contas

Enunciado: crie um programa que leia quanto dinheiro uma pessoa tem na
carteira e mostre quantos dólares ela pode comprar.
Conceitos: float(), divisão
"""

# Cotação usada (29/09/2026): 1 dólar = 5,23 reais

Carteira = float(input("Quanto de dinheiro vc tem na sua carteira? "))

CarteiraDolar = Carteira / 5.23

print("Voce atualmente tem {} reais e pode comprar {} dolares".format(Carteira, CarteiraDolar))

# Jeito simplificado
print("Voce atualmente tem {} reais e pode comprar {} dolares".format(Carteira, Carteira / 5.23))

# Outra forma: com 2 casas decimais, como se escreve dinheiro.
# Com R$ 100 o resultado sai 19.12 em vez de 19.12045889101338.
print("Com R$ {:.2f} você pode comprar US$ {:.2f}".format(Carteira, Carteira / 5.23))
