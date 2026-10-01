"""
Desafio 023: Separando os dígitos de um número
Mundo 1 · Manipulando texto

Enunciado: faça um programa que leia um número de 0 a 9999 e mostre na tela
cada um dos dígitos separados.
Conceitos: divisão inteira (//) e resto (%)
"""

numero = int(input("Numero de 0 a 9999: "))

# Ex.: 1834 // 100 = 18 (corta os 2 últimos dígitos), e 18 % 10 = 8 (fica só o último)
milhar = numero // 1000 % 10
centena = numero // 100 % 10
dezena = numero // 10 % 10
unidade = numero // 1 % 10

print("Milhar: {}".format(milhar))
print("Centena: {}".format(centena))
print("Dezena: {}".format(dezena))
print("Unidade: {}".format(unidade))

# DICA: dividir por 1 não muda nada, então a unidade pode ser só numero % 10.
