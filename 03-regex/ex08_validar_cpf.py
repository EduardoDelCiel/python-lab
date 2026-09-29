"""
Exercício 08 — Validar formato do CPF
Módulo 03 · Strings e Regex

Objetivo: aceitar o CPF só se estiver no formato 000.000.000-00.
(Isso confere o FORMATO. Se o CPF existe de verdade depende dos dígitos
verificadores, que é outro assunto.)

Conceitos: quantificador {n}, escapar o ponto (\\.), re.fullmatch()
Teoria: README.md desta pasta → "Quantificadores" e "Escapando caracteres especiais"
"""

import re

cpf = input("Seu CPF (formato 000.000.000-00): ")

# \d{3} → exatamente 3 dígitos
# \.    → um ponto de verdade (sem a barra, "." quer dizer "qualquer caractere")
# -     → fora dos colchetes o hífen é um caractere comum e dispensa a barra
#
# CORREÇÃO: o original usava re.match(), que aceitava "123.456.789-0099"
# (dígitos sobrando no fim). O re.fullmatch() exige o formato exato, do
# começo ao fim.
if re.fullmatch(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
    print("CPF válido")
else:
    print("CPF inválido")
