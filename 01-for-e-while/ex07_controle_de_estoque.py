"""
Exercício 07 — Controle de estoque
Módulo 01 · for e while

Objetivo: registrar uma venda por vez até o estoque acabar, mostrando
quanto sobrou depois de cada venda.

Conceitos: while com contagem decrescente, atribuição composta (-=)
Teoria: README.md desta pasta → "while" e "Erros corrigidos"
"""

# CORREÇÃO: a variável se chamava `Contador_estoque`. Por convenção, nomes de
# variáveis em Python são em minúsculas (snake_case).
estoque = 5

# CORREÇÃO: o original era `while contador > 0`, mas `contador` era a variável
# do exercício 2 (valia 10 e nunca diminuía aqui dentro), então o laço nunca
# terminava. A condição precisa testar a mesma variável que muda dentro do laço.
while estoque > 0:
    # CORREÇÃO: primeiro desconta a venda, depois mostra o que restou.
    # No original, a primeira venda dizia "Estoque restante: 5".
    estoque -= 1
    print(f"Venda realizada! Estoque restante: {estoque}")

print("Estoque esgotado!")
