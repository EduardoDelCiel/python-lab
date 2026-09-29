"""
Exercício 02 — Processando dados
Módulo 01 · for e while

Objetivo: simular o processamento de vários lotes de dados, numerando cada um,
e avisar quando tudo terminar.

Conceitos: while, contador, atribuição composta (+=)
Teoria: README.md desta pasta → "while", "Contador" e "Atribuição composta"
"""

contador = 1

while contador < 10:            # repete enquanto a condição for verdadeira
    print(f"Processando dados {contador}")
    contador += 1               # o mesmo que: contador = contador + 1

print("Dados processados!")

# Repare: com `< 10` o laço roda 9 vezes (de 1 a 9).
# Para ir até 10, a condição seria `contador <= 10`.
