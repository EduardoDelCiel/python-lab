"""
Exercício 01 — Nome do produto em minúsculas
Módulo 03 · Strings e Regex

Objetivo: ler o nome de um produto e mostrá-lo todo em letras minúsculas.

Conceitos: .lower()
Revisão: input(), f-string (módulo 01)
Teoria: README.md desta pasta → "lower() e upper()"
"""

produto = input("Nome do produto: ")
produto_lower = produto.lower()     # "CAFÉ Premium" → "café premium"

print(f"O nome do produto é {produto_lower}")
