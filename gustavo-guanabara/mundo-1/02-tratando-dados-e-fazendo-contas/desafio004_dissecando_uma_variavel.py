"""
Desafio 004: Dissecando uma variável
Mundo 1 · Tratando dados e fazendo contas

Enunciado: faça um programa que leia algo pelo teclado e mostre na tela o seu
tipo primitivo e todas as informações possíveis sobre ele.
Conceitos: type(), métodos is...() de string
"""

Coisa = input("Digite algo: ")
print("O tipo primitivo desse valor é", type(Coisa))   # sempre str: o input() devolve texto
print("Só tem espaço? ", Coisa.isspace())
print("É alfabético? ", Coisa.isalpha())
print("É alfanumérico? ", Coisa.isalnum())
print("Está escrito em maiúsculas? ", Coisa.isupper())
print("Está escrito em minúsculas? ", Coisa.islower())
print("Está capitalizado? ", Coisa.istitle())

# DICA: dá para incluir também o .isnumeric() ("só tem números?"). Ele é
# muito útil para saber se o texto pode ser convertido com int().
