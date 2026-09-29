"""
Exercício 03 — Partes da senha
Módulo 03 · Strings e Regex

Objetivo: mostrar os 3 primeiros e os 3 últimos caracteres de uma senha.

Conceitos: fatiamento [inicio:fim], índices negativos
Teoria: README.md desta pasta → "Índices" e "Fatiamento"
"""

senha = input("Crie uma senha com mais de 8 caracteres: ")

parte1 = senha[:3]      # do início até o índice 3 (sem incluir) → 3 primeiros
parte2 = senha[-3:]     # do 3º caractere contando do fim até o final → 3 últimos

print(f"As 3 primeiras letras da sua senha são {parte1}")
print(f"As 3 últimas letras da sua senha são {parte2}")

# Desafio: a mensagem pede "mais de 8 caracteres", mas nada verifica isso.
# Que tal usar o while True + len() do módulo 01 (ex10) para exigir?
