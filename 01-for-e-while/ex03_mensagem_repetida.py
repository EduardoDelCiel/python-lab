"""
Exercício 03 — Mensagem repetida
Módulo 01 · for e while

Objetivo: exibir "Bem-vindo ao Buscante!" 5 vezes.

Conceitos: while com contador × for com range()
O mesmo problema resolvido de duas formas. Compare as duas!
Teoria: README.md desta pasta → "range()" e "for ou while?"
"""

# Solução 1 — while: você mesmo cria, testa e atualiza o contador.
contador = 0
while contador < 5:
    print("Bem-vindo ao Buscante!")
    contador += 1

print("--- agora com for ---")

# Solução 2 — for + range(): o range(5) gera 0, 1, 2, 3, 4 sozinho.
# Como o número em si não é usado, a convenção é chamar a variável de `_`.
for _ in range(5):
    print("Bem-vindo ao Buscante!")
