"""
Exercício 06 — Substituir uma palavra
Módulo 03 · Strings e Regex

Objetivo: trocar uma palavra por outra numa frase, mas só quando ela aparece
como palavra inteira ("gato" troca em "o gato", mas não em "gatos").

Conceitos: re.sub(), rf'' (raw + f-string), \\b, re.escape()
Teoria: README.md desta pasta → "re.sub()", "Raw string" e "Borda de palavra"
"""

import re

historia = input("Escreva sua frase aqui: ")
palavra = input("Qual palavra você quer substituir? ")
palavra_nova = input("Qual palavra você deseja colocar no lugar? ")

# \b  → borda de palavra: garante que só a palavra inteira será trocada
# rf  → r (raw string, para o \b) + f (para colocar a variável dentro do padrão)
# MELHORIA: re.escape() faz a palavra digitada ser tratada como texto comum.
# Sem ele, ao pedir para trocar "1.5", o "." viraria "qualquer caractere" e
# "105" também seria trocado. E um "(" digitado quebraria o programa (re.error).
padrao = rf'\b{re.escape(palavra)}\b'

historia = re.sub(padrao, palavra_nova, historia)   # re.sub(padrão, troca, texto)
print(historia)
