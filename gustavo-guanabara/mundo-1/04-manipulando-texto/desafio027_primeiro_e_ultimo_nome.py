"""
Desafio 027: Primeiro e último nome
Mundo 1 · Manipulando texto

Enunciado: faça um programa que leia o nome completo de uma pessoa, mostrando
em seguida o primeiro e o último nome separadamente.
Conceitos: .split(), índices, len()
"""

Nome = input("Digite seu nome: ").strip().split()     # vira uma lista de palavras

print("Primeiro nome: {}".format(Nome[0]))
print("Último nome: {}".format(Nome[len(Nome) - 1]))
print("Quantidade de nomes: {}".format(len(Nome)))

# DICA: índice negativo conta a partir do fim, então Nome[-1] é o mesmo que
# Nome[len(Nome) - 1].
