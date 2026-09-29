"""
Exercício 05 — Número da receita
Módulo 03 · Strings e Regex

Objetivo: encontrar o primeiro número que aparece num texto
(ex.: "Receita 4521 do cliente" → 4521).

Conceitos: import re, raw string r'', re.findall(), \\d, quantificador +
Teoria: README.md desta pasta → "re.findall()", "Dígitos e letras" e
        "Quantificadores"
"""

import re

texto = input("Digite a sua receita: ")

# \d  → um dígito (0 a 9)
# +   → "um ou mais" do que vem antes → \d+ pega o número inteiro, não só 1 dígito
numeros = re.findall(r'\d+', texto)   # lista com TODOS os números do texto

# CORREÇÃO: o original fazia re.findall(...)[0] direto. Se o texto não tiver
# nenhum número, a lista vem vazia e o [0] quebra o programa com IndexError.
if numeros:                         # lista vazia conta como falso
    numero_receita = numeros[0]     # [0] → o primeiro número encontrado
    print(f"A receita {numero_receita} foi enviada pelo cliente")
else:
    print("Nenhum número de receita foi encontrado no texto.")
