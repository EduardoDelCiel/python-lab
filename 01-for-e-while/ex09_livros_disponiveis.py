"""
Exercício 09 — Livros disponíveis
Módulo 01 · for e while

Objetivo: mostrar apenas os livros que ainda têm estoque.

Conceitos: lista de dicionários, continue
Teoria: README.md desta pasta → "Dicionários" e "continue"
"""

# Cada livro é um dicionário. A lista junta todos, como as linhas de uma tabela.
livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2},
]

for livro in livros:
    if livro["estoque"] == 0:
        continue                # sem estoque → pula direto para o próximo livro
    # A f-string usa aspas duplas, então a chave vai com aspas simples: ['nome']
    print(f"Livro disponível: {livro['nome']}")
