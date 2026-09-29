"""
Exercício 04 — Validar URL
Módulo 03 · Strings e Regex

Objetivo: aceitar a URL só se ela começar com "https://" e terminar com ".com".

Conceitos: .startswith(), .endswith(), and
Teoria: README.md desta pasta → "startswith() e endswith()" e "and"
"""

# MELHORIA: a variável se chamava `URL`. Nomes todos em maiúsculas são a
# convenção para constantes; para variáveis comuns usamos minúsculas.
url = input("Digite aqui sua URL: ")

# `and` → as DUAS condições precisam ser verdadeiras
if url.startswith("https://") and url.endswith(".com"):
    print("Sua URL é válida")
else:
    print("Sua URL é inválida")
