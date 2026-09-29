"""
Exercício 02 — Mensagem de boas-vindas
Módulo 03 · Strings e Regex

Objetivo: ler o nome e a cidade do usuário e montar uma mensagem personalizada.

Conceitos: nenhum novo. É uma revisão de input() e de f-string com mais de
uma variável (módulo 01).
"""

nome = input("Digite seu nome: ")
cidade = input("Digite a sua cidade: ")

print(f"Olá, {nome}! Bem-vindo(a) ao sistema da cidade de {cidade}")
