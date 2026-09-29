"""
Exercício 08 — Contagem regressiva da promoção
Módulo 01 · for e while

Objetivo: contar de 10 até 1, com uma mensagem para segundos pares e outra
para segundos ímpares.

Conceitos: resto da divisão (%), while decrescente, range() com passo negativo
O mesmo problema resolvido de duas formas.
Teoria: README.md desta pasta → "Resto da divisão" e "range()"
"""

# Solução 1 — while
segundos = 10

while segundos > 0:
    if segundos % 2 == 0:       # resto da divisão por 2 é zero → número par
        print(f"Faltam apenas {segundos} segundos - Não perca essa oportunidade!")
    else:
        print(f"A contagem continua: {segundos} segundos restantes.")
    # MELHORIA: no original, o `-= 1` estava repetido dentro do if E do else.
    # Como acontece nos dois casos, basta uma linha fora do if/else.
    segundos -= 1

print("Aproveite a promoção agora!")

print("--- agora com for ---")

# Solução 2 — for + range(inicio, fim, passo)
# range(10, 0, -1) → 10, 9, 8, ..., 1 (o 0 não entra: o fim nunca é incluído)
for segundos in range(10, 0, -1):
    if segundos % 2 == 0:
        print(f"Faltam apenas {segundos} segundos - Não perca essa oportunidade!")
    else:
        print(f"A contagem continua: {segundos} segundos restantes.")

print("Aproveite a promoção agora!")
