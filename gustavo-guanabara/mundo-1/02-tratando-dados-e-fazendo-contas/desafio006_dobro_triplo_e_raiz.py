"""
Desafio 006: Dobro, triplo e raiz quadrada
Mundo 1 · Tratando dados e fazendo contas

Enunciado: crie um algoritmo que leia um número e mostre o seu dobro, triplo
e raiz quadrada.
Conceitos: operadores * e ** (potência), raiz quadrada com ** (1/2)
"""

Numero = int(input("Digite um numero: "))
Dobro = Numero * 2
Triplo = Numero * 3
Raiz = Numero ** (1/2)      # elevar a 1/2 é o mesmo que tirar a raiz quadrada

print("O dobro do valor é {}, o triplo é {} e a raiz é {}".format(Dobro, Triplo, Raiz))

# Jeito simplificado
print("O dobro do valor é {}, o triplo é {} e a raiz é {}".format(Numero * 2, Numero * 3, Numero ** (1/2)))

# DICA: a raiz de 5 aparece como 2.23606797749979. Com {:.2f} no lugar do {}
# ela fica com 2 casas: 2.24 (veja "Formatando números" no README).
