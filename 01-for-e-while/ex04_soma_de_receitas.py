"""
Exercício 04 — Soma das receitas
Módulo 01 · for e while

Objetivo: somar todos os valores de uma lista de receitas.

Conceitos: acumulador, for, atribuição composta (+=)
Teoria: README.md desta pasta → "Acumulador"
"""

valores = [10, 20, 30, 40, 50]

soma = 0                        # acumulador: começa em zero
for numero in valores:
    soma += numero              # a cada volta, junta mais um valor

print(f"A soma total das receitas é: {soma}")

# Dica: o Python já tem isso pronto → sum(valores) também dá 150.
