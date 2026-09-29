"""
Exercício 10 — Separar nome, sobrenome e ano
Módulo 03 · Strings e Regex

Objetivo: a partir de "Nome Sobrenome - AAAA", separar cada parte.
(ex.: "Eduardo Silva - 1995" → Eduardo / Silva / 1995)

Conceitos: re.search(), grupos (), .group(n), \\w
Teoria: README.md desta pasta → "re.search()", "Grupos" e "Objeto Match"
"""

import re

tudo = input("Nome, sobrenome e ano de nascimento (ex.: Eduardo Silva - 1995): ")

# (\w+)   → grupo 1: uma palavra (letras, números ou _)
# " "     → um espaço
# (\w+)   → grupo 2: outra palavra
# " - "   → espaço, hífen, espaço
# (\d{4}) → grupo 3: exatamente 4 dígitos
#
# CORREÇÃO: o padrão original começava com um espaço (r' (\w+) ...'), então
# "Eduardo Silva - 1995" não era reconhecido. Só funcionava se o usuário
# digitasse um espaço antes do nome.
padrao = r'(\w+) (\w+) - (\d{4})'

resultado = re.search(padrao, tudo)   # devolve um objeto Match, ou None

if resultado:                         # None conta como falso
    primeiro_nome = resultado.group(1)
    sobrenome = resultado.group(2)
    ano_nascimento = resultado.group(3)

    print(f"Primeiro Nome: {primeiro_nome}")
    print(f"Sobrenome: {sobrenome}")
    print(f"Ano de Nascimento: {ano_nascimento}")
else:
    print("Formato inválido!")
