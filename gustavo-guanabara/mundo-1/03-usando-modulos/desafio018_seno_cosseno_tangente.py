"""
Desafio 018: Seno, cosseno e tangente
Mundo 1 · Usando módulos

Enunciado: faça um programa que leia um ângulo qualquer e mostre na tela o
valor do seno, cosseno e tangente desse ângulo.
Conceitos: from math import várias funções, radians(), f-string
"""

from math import sin, cos, tan, radians

Angulo = float(input("Angulo? "))

# As funções do math trabalham em radianos, por isso o radians() converte antes.
seno = sin(radians(Angulo))
# CORREÇÃO: era `cos = cos(radians(Angulo))`. Isso troca a FUNÇÃO cos por um
# número: depois dessa linha, chamar cos() de novo dá
# "TypeError: 'float' object is not callable". Nunca use o nome de uma função
# como nome de variável.
cosseno = cos(radians(Angulo))
tangente = tan(radians(Angulo))

print(f'O seno de {Angulo} é {seno:.2f}')
print(f'O cosseno de {Angulo} é {cosseno:.2f}')
print(f'A tangente de {Angulo} é {tangente:.2f}')
