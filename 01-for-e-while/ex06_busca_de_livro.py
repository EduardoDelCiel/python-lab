"""
Exercício 06 — Busca de livro
Módulo 01 · for e while

Objetivo: procurar "O Hobbit" na lista e parar assim que ele for encontrado.

Conceitos: break, comparação com ==
Teoria: README.md desta pasta → "break"
"""

livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

for livro in livros:
    if livro == "O Hobbit":
        print(f"Livro encontrado: {livro}")
        break                   # achou → encerra o laço, não olha o resto da lista
