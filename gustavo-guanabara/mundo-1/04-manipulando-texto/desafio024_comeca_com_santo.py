"""
Desafio 024: A cidade começa com "Santo"?
Mundo 1 · Manipulando texto

Enunciado: crie um programa que leia o nome de uma cidade e diga se ela começa
ou não com o nome "SANTO".
Conceitos: fatiamento [:5], .upper(), .strip(), comparação ==
"""

# MELHORIA: o .strip() tira os espaços do começo e do fim. Sem ele, quem
# digitasse " Santo André" (com um espaço antes) recebia False.
Cidade = input("Cidade: ").strip()

# [:5] pega as 5 primeiras letras; .upper() deixa tudo maiúsculo para comparar
print(Cidade[:5].upper() == "SANTO")
