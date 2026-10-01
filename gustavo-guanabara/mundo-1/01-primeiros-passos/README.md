# Primeiros passos

**Mundo 1 · Desafios 001 e 002**

Os primeiros comandos: mostrar algo na tela, guardar valores em variáveis e conversar com o usuário.

[← Voltar ao Mundo 1](../README.md)

## Desafios

| # | Arquivo | O que faz | Conceitos |
|---|---|---|---|
| 001 | [desafio001_ola_mundo.py](desafio001_ola_mundo.py) | Escreve "Olá, Mundo!" na tela | `print()` |
| 002 | [desafio002_boas_vindas.py](desafio002_boas_vindas.py) | Lê o nome e dá boas-vindas | `input()`, variável, `.format()` |

---

## Anotações

### `print()`

O `print()` mostra uma mensagem na tela:

```python
print("Olá, Mundo!")      # Olá, Mundo!
print(7 + 3)              # 10 (faz a conta e mostra o resultado)
print("7 + 3")            # 7 + 3 (entre aspas é texto, não conta)
```

Com vírgula, ele mostra vários valores separados por espaço:

```python
print("Total:", 10)       # Total: 10
```

### Strings

Todo texto em Python é uma **string**, e fica entre aspas. Tanto faz usar aspas duplas ou simples, desde que abra e feche com a mesma:

```python
"Olá, Mundo!"
'Olá, Mundo!'
```

### Comentários

Tudo depois do `#` é ignorado pelo Python. Serve para fazer anotações no código:

```python
# isto é um comentário
print("isto aparece")   # comentário no fim da linha
```

### Variáveis

Uma variável é um **nome que guarda um valor**. O `=` significa "guarde", e não "igual":

```python
nome = "Eduardo"
idade = 30
```

Regras para os nomes:
- podem ter letras, números e `_`, mas não podem começar com número;
- não podem ter espaço (`primeiro nome` não funciona, `primeiro_nome` sim);
- maiúsculas e minúsculas são diferentes: `Nome` e `nome` são duas variáveis.

### `input()`

O `input()` mostra uma pergunta, **espera o usuário digitar** e devolve o que foi digitado:

```python
nome = input("Qual o seu nome? ")
```

> Deixe um espaço no fim da pergunta (`"Qual o seu nome? "`); senão a resposta aparece colada no texto.

### `.format()`

O `.format()` encaixa valores dentro de um texto. Cada `{}` é um espaço reservado, preenchido na ordem:

```python
nome = "Eduardo"
print("Seja bem-vindo, {}!".format(nome))          # Seja bem-vindo, Eduardo!
print("{} tem {} anos".format("Ana", 25))          # Ana tem 25 anos
```

> Mais adiante, na seção [Usando módulos](../03-usando-modulos/README.md), aparece a **f-string**, que faz a mesma coisa de um jeito mais curto: `f"Seja bem-vindo, {nome}!"`.

---

## Correções e dicas

| Desafio | O que mudou |
|---|---|
| 002 | Texto da mensagem: "bem vindo" → "bem-vindo" |
