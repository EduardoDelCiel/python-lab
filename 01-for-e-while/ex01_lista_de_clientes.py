"""
Exercício 01 — Lista de clientes
Módulo 01 · for e while

Objetivo: mostrar o nome de cada cliente da lista, um por linha.

Conceitos: lista, for
Teoria: README.md desta pasta → "Listas" e "for"
"""

clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

# A cada volta do laço, `nome` recebe o próximo item da lista.
for nome in clientes:
    print(nome)

# MELHORIA: o original usava print(f"{nome}"). Funciona, mas a f-string só
# vale a pena quando você mistura texto com variáveis. Para a variável sozinha,
# print(nome) já basta.
