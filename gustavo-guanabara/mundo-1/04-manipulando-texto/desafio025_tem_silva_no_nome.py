"""
Desafio 025: Tem "Silva" no nome?
Mundo 1 · Manipulando texto

Enunciado: crie um programa que leia o nome de uma pessoa e diga se ela tem
"SILVA" no nome.
Conceitos: operador in, .lower(), .strip()
"""

Nome = input("Digite seu nome: ").strip()
print("Seu nome tem Silva? {}".format("silva" in Nome.lower()))

# DICA: o `in` procura o texto em qualquer lugar, então "Silvana" e "Silvano"
# também dão True. Para procurar só a palavra inteira:
#   "silva" in Nome.lower().split()
