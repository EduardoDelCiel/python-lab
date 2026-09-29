"""
Exercício 07 — Validar nome de cadastro
Módulo 03 · Strings e Regex

Objetivo: aprovar o nome só se ele começar com letra maiúscula e tiver apenas
letras (sem números nem símbolos).

O mesmo problema resolvido de duas formas: com métodos de string e com regex.

Conceitos: .isupper(), .isdigit(), .isalnum(), all(), expressão geradora,
           re.fullmatch(), colchetes [A-Z], quantificador *
Teoria: README.md desta pasta → "Métodos de verificação", "all()",
        "re.match() e re.fullmatch()" e "Colchetes"
"""

import re

# ---------- Solução 1: métodos de string ----------
nome1 = input("Seu nome: ")

# CORREÇÃO: o original testava a variável `texto` (do ex05) em vez de `nome1`.
# CORREÇÃO: nome1[0] quebra se o nome vier vazio. Com `len(nome1) > 0 and ...`,
# se a primeira parte for falsa, o Python nem chega a olhar o nome1[0].
comeca_com_maiuscula = len(nome1) > 0 and nome1[0].isupper()
sem_numeros = all(not caractere.isdigit() for caractere in nome1)
sem_simbolos = all(caractere.isalnum() for caractere in nome1)

# MELHORIA: dar nome a cada condição deixa o if legível como uma frase.
if comeca_com_maiuscula and sem_numeros and sem_simbolos:
    print("Cadastro aprovado")
else:
    print("Cadastro negado")


# ---------- Solução 2: regex ----------
nome2 = input("Digite o nome do cliente para validação: ")

# [A-ZÀ-Ý]   → exatamente 1 letra maiúscula (inclui acentuadas, como É)
# [a-zà-ÿ]*  → zero ou mais letras minúsculas (inclui acentuadas, como ã em João)
# CORREÇÃO: o original usava re.match(), que só confere o COMEÇO do texto, e
# por isso "Ana123" passava (o "Ana" já bastava). O re.fullmatch() exige que o
# texto INTEIRO siga o padrão.
# Com o fullmatch, um [a-z]* sem acentos passaria a recusar "João" por causa do
# "ã". Por isso as faixas À-Ý e à-ÿ foram incluídas.
if re.fullmatch(r'[A-ZÀ-Ý][a-zà-ÿ]*', nome2):
    print("Nome válido!")
else:
    print("Nome inválido!")
