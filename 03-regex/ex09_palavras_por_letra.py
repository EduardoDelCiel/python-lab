"""
Exercício 09 — Palavras que começam com uma letra
Módulo 03 · Strings e Regex

Objetivo: no nome de um livro, encontrar todas as palavras que começam com a
letra escolhida, ignorando maiúsculas/minúsculas e aceitando acentos.
(ex.: "O Senhor dos Anéis" + letra "a" → ['Anéis'])

Conceitos: re.findall() com flag re.IGNORECASE, \\b, colchetes com acentos [a-zà-ÿ]
Teoria: README.md desta pasta → "re.IGNORECASE" e "Colchetes"
"""

import re

livro = input("Nome do livro: ")
letra = input("Letra inicial que você procura: ")

# \b        → começo de palavra
# {letra}   → a letra digitada (o "f" de rf permite usar a variável)
# [a-zà-ÿ]* → o resto da palavra: letras com ou sem acento, quantas houver
# re.IGNORECASE → trata "A" e "a" como iguais
#
# CORREÇÃO: o original chamava `re.findal` (faltava um "l") e procurava na
# variável `texto` (do ex05) em vez de `livro`.
padrao = rf'\b{re.escape(letra)}[a-zà-ÿ]*'
palavras = re.findall(padrao, livro, re.IGNORECASE)

print(palavras)
