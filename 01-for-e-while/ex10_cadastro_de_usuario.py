"""
Exercício 10 — Cadastro de usuário
Módulo 01 · for e while

Objetivo: pedir usuário e senha até que os dois sejam válidos:
  - usuário com pelo menos 5 caracteres
  - senha com pelo menos 8 caracteres

Conceitos: while True, input(), len(), continue, break
Teoria: README.md desta pasta → "while True", "input()" e "len()"
"""

while True:                     # laço sem fim: só termina com o break lá embaixo
    nome_usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    # len() conta quantos caracteres tem a string
    if len(nome_usuario) < 5:
        print("O nome de usuário deve ter pelo menos 5 caracteres.")
        continue                # volta para o topo e pede tudo de novo

    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
        continue

    print("Cadastro realizado com sucesso!")
    break                       # chegou aqui = tudo válido → sai do laço
