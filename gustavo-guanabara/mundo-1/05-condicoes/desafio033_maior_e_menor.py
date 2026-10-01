"""
Desafio 033: Maior e menor de três números
Mundo 1 · Condições

Enunciado: faça um programa que leia três números e mostre qual é o maior e
qual é o menor.
Conceitos: condições aninhadas, operador and
"""

n1 = float(input("Numero 1: "))
n2 = float(input("Numero 2: "))
n3 = float(input("Numero 3: "))

# Jeito longo: condições aninhadas (um if dentro do outro)
if n1 >= n2 and n1 >= n3:
    if n2 > n3:
        print("N1 {} é o maior numero e N3 é o menor numero {}".format(n1, n3))
    else:
        print("N1 {} é o maior numero e N2 é o menor numero {}".format(n1, n2))
else:
    if n2 >= n3 and n2 >= n1:
        if n3 > n1:
            print("N2 {} é o maior numero e N1 é o menor numero {}".format(n2, n1))
        else:
            print("N2 {} é o maior numero e N3 é o menor numero {}".format(n2, n3))
    else:
        if n3 > n1 and n3 > n2:
            if n2 > n1:
                print("N3 {} é o maior numero e N1 é o menor numero {}".format(n3, n1))
            else:
                print("N3 {} é o maior numero e N2 é o menor numero {}".format(n3, n2))


# Jeito curto
# CORREÇÃO: a versão anterior errava quando o 2º e o 3º números eram iguais
# (e diferentes do 1º). Ela perguntava se o n2 era menor que o n1 E menor que
# o n3. Com 5, 3 e 3, nem o n2 nem o n3 passavam no teste (3 < 3 é falso), e o
# menor ficava 5. Com 1, 5 e 5 acontecia o mesmo com o maior, que ficava 1.
# A solução é comparar cada número só com o menor (ou maior) encontrado até
# agora. Assim a repetição deixa de ser problema.
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

print("O maior valor digitado foi {}".format(maior))
print("O menor valor digitado foi {}".format(menor))

# CORREÇÃO: no fim do arquivo havia uma linha `maior = n1` solta, que tinha
# sobrado e não fazia nada. Foi removida.
