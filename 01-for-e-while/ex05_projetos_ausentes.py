"""
Exercício 05 — Projetos ausentes
Módulo 01 · for e while

Objetivo: listar os projetos e avisar quando uma posição da lista estiver vazia.

Conceitos: None, is, if/else
Teoria: README.md desta pasta → "None" e "if e else"
"""

projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for projeto in projetos:
    if projeto is None:         # `is None` é o jeito certo de testar "sem valor"
        print("Projeto ausente")
    else:
        print(projeto)
