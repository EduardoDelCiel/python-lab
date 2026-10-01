"""
Desafio 026: A letra "A" na frase
Mundo 1 · Manipulando texto

Enunciado: faça um programa que leia uma frase pelo teclado e mostre quantas
vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que
posição ela aparece a última vez.
Conceitos: .count(), .find(), .rfind(), .strip(), .lower()
"""

frase = str(input("Digite uma frase: ")).strip().lower()

print(frase.count("a"))         # quantas vezes aparece
print(frase.find("a") + 1)      # primeira posição (+1 porque o Python conta a partir do 0)
print(frase.rfind("a") + 1)     # última posição

# DICA: o input() já devolve texto, então o str() em volta dele não é necessário.
# Se a frase não tiver nenhum "a", o find() devolve -1, e o programa mostra 0.
