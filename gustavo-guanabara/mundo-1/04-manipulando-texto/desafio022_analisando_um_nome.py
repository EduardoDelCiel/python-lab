"""
Desafio 022: Analisando um nome
Mundo 1 · Manipulando texto

Enunciado: crie um programa que leia o nome completo de uma pessoa e mostre:
  - o nome com todas as letras maiúsculas e minúsculas;
  - quantas letras ao todo (sem considerar espaços);
  - quantas letras tem o primeiro nome.
Conceitos: .upper(), .lower(), len(), .replace(), .split(), .count()
"""

Nome = input("Digite o nome completo: ")

NomeMaius = Nome.upper()
print(NomeMaius)
NomeMinus = Nome.lower()
print(NomeMinus)

total = len(Nome.replace(" ", ""))      # tira os espaços e conta o que sobrou
print(f"Total de letras: {total}")

primeiro = Nome.split()[0]              # split() separa as palavras; [0] é a primeira
print("O primeiro nome {} tem {} letras".format(primeiro, len(primeiro)))

# Jeito do Guanabara: tamanho total menos a quantidade de espaços
print("Seu nome tem {} letras".format(len(Nome) - Nome.count(" ")))
