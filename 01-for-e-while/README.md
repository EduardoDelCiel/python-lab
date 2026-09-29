# 01 · Laços de repetição: `for` e `while`

Primeiro módulo do lab. O foco são os **laços de repetição**, mas junto com eles aparecem vários fundamentos que o resto do repositório usa: listas, dicionários, `if`/`else`, f-strings, `input()` e `len()`.

Tudo que é explicado aqui **não se repete** nos próximos módulos. Eles só apontam para cá.

[← Voltar ao índice geral](../README.md)

## Sumário

- [Exercícios](#exercícios)
- [Conceitos](#conceitos)
  - **Fundamentos:** [Indentação](#indentação) · [Comentários](#comentários) · [Variáveis e nomes](#variáveis-e-nomes) · [Booleanos](#booleanos)
  - **Estruturas de dados:** [Listas](#listas) · [Dicionários](#dicionários) · [None](#none)
  - **Laços:** [for](#for) · [while](#while) · [range()](#range) · [while True](#while-true)
  - **Controle do laço:** [break](#break) · [continue](#continue)
  - **Decisões:** [if e else](#if-e-else) · [Operadores de comparação](#operadores-de-comparação)
  - **Operadores:** [Atribuição composta](#atribuição-composta) · [Resto da divisão](#resto-da-divisão)
  - **Entrada e saída:** [print()](#print) · [f-string](#f-string) · [input()](#input) · [len()](#len)
  - **Padrões de laço:** [Contador](#contador) · [Acumulador](#acumulador)
- [for ou while?](#for-ou-while)
- [Erros corrigidos](#erros-corrigidos)

---

## Exercícios

| # | Arquivo | O que faz | Conceitos principais |
|---|---|---|---|
| 01 | [ex01_lista_de_clientes.py](ex01_lista_de_clientes.py) | Mostra cada cliente da lista | `for`, lista |
| 02 | [ex02_processando_dados.py](ex02_processando_dados.py) | Numera os lotes processados até terminar | `while`, contador, `+=` |
| 03 | [ex03_mensagem_repetida.py](ex03_mensagem_repetida.py) | Repete uma mensagem 5 vezes (duas soluções) | `while` × `for` + `range()` |
| 04 | [ex04_soma_de_receitas.py](ex04_soma_de_receitas.py) | Soma todos os valores de uma lista | acumulador, `+=` |
| 05 | [ex05_projetos_ausentes.py](ex05_projetos_ausentes.py) | Lista projetos e avisa quando falta um | `None`, `is`, `if`/`else` |
| 06 | [ex06_busca_de_livro.py](ex06_busca_de_livro.py) | Procura um livro e para quando encontra | `break`, `==` |
| 07 | [ex07_controle_de_estoque.py](ex07_controle_de_estoque.py) | Vende até o estoque zerar | `while` decrescente, `-=` |
| 08 | [ex08_contagem_regressiva.py](ex08_contagem_regressiva.py) | Contagem regressiva com mensagens para par/ímpar (duas soluções) | `%`, `range()` com passo negativo |
| 09 | [ex09_livros_disponiveis.py](ex09_livros_disponiveis.py) | Mostra só os livros que têm estoque | lista de dicionários, `continue` |
| 10 | [ex10_cadastro_de_usuario.py](ex10_cadastro_de_usuario.py) | Pede usuário e senha até serem válidos | `while True`, `input()`, `len()`, `break`/`continue` |

---

## Conceitos

### Fundamentos

#### Indentação

Em Python, **quem define os blocos de código é a indentação**, o recuo no começo da linha. Outras linguagens usam chaves `{}` para isso. Tudo que está "dentro" de um `for`, `while` ou `if` fica recuado **4 espaços**.

```python
for nome in clientes:
    print(nome)        # dentro do for → repete a cada volta
print("Fim")           # fora do for → roda uma vez só, no final
```

> Esquecer ou misturar a indentação gera `IndentationError`.

#### Comentários

Tudo depois de `#` é ignorado pelo Python. Serve para você deixar anotações no código.

Um texto entre três aspas (`"""..."""`) no topo do arquivo também serve de documentação. É o cabeçalho que todo exercício deste lab tem.

#### Variáveis e nomes

Uma variável guarda um valor com um nome: `estoque = 5`.

A convenção do Python (a **PEP 8**) é escrever nomes em **minúsculas, com `_` separando as palavras**. Esse estilo se chama *snake_case*: `nome_usuario`, `contador_estoque`.

| Estilo | Exemplo | Usado para |
|---|---|---|
| `snake_case` | `nome_usuario` | variáveis e funções |
| `PascalCase` | `ContadorEstoque` | classes (assunto futuro) |
| `MAIUSCULAS` | `LIMITE_MAXIMO` | constantes, ou seja, valores que não mudam |

#### Booleanos

`True` e `False` (sempre com a primeira letra maiúscula) são os dois valores lógicos do Python. Toda condição de um `if` ou de um `while` acaba virando um deles:

```python
5 > 3        # True
10 == 7      # False
```

**Usado em:** [ex10](ex10_cadastro_de_usuario.py) (`while True`)

---

### Estruturas de dados

#### Listas

Uma lista é uma coleção **ordenada** de itens, entre colchetes e separados por vírgula.

```python
clientes = ["João", "Maria", "Carlos"]
valores = [10, 20, 30]
```

O jeito mais comum de usar uma lista é percorrê-la com [`for`](#for).

**Usado em:** [ex01](ex01_lista_de_clientes.py) · [ex04](ex04_soma_de_receitas.py) · [ex05](ex05_projetos_ausentes.py) · [ex06](ex06_busca_de_livro.py) · [ex09](ex09_livros_disponiveis.py)

#### Dicionários

Um dicionário guarda pares **chave: valor** entre chaves `{}`. Na lista você acessa um item pela posição. No dicionário, acessa **pelo nome da chave**.

```python
livro = {"nome": "1984", "estoque": 5}

livro["nome"]      # "1984"
livro["estoque"]   # 5
```

Uma **lista de dicionários** é o jeito clássico de representar uma tabela: cada dicionário é uma linha e cada chave é uma coluna.

```python
livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "O Hobbit", "estoque": 0},
]

for livro in livros:
    print(livro["nome"], livro["estoque"])
```

**Usado em:** [ex09](ex09_livros_disponiveis.py)

#### `None`

`None` significa **"nenhum valor"**, ou seja, a ausência de valor. Para testar se algo é `None`, use `is` em vez de `==`:

```python
if projeto is None:
    print("Projeto ausente")

if projeto is not None:
    print("Tem projeto!")
```

> Por quê? O `is` verifica se é **o mesmo objeto**. Como só existe um `None` em todo o Python, `x is None` é a forma recomendada.

**Usado em:** [ex05](ex05_projetos_ausentes.py)

---

### Laços de repetição

#### `for`

O `for` percorre uma sequência **item por item**: uma lista, uma string, um `range()`... A cada volta, a variável recebe o próximo item. O laço termina sozinho quando os itens acabam.

```python
for variavel in sequencia:
    # bloco que se repete
```

```python
for nome in ["Ana", "Bia"]:
    print(nome)
# Ana
# Bia
```

**Usado em:** [ex01](ex01_lista_de_clientes.py) · [ex03](ex03_mensagem_repetida.py) · [ex04](ex04_soma_de_receitas.py) · [ex05](ex05_projetos_ausentes.py) · [ex06](ex06_busca_de_livro.py) · [ex08](ex08_contagem_regressiva.py) · [ex09](ex09_livros_disponiveis.py)

#### `while`

O `while` repete o bloco **enquanto a condição for verdadeira**. A condição é testada antes de cada volta.

```python
while condicao:
    # bloco que se repete
```

```python
contador = 1
while contador <= 3:
    print(contador)
    contador += 1
# 1
# 2
# 3
```

> **Atenção:** alguma coisa dentro do laço precisa, em algum momento, tornar a condição falsa. Se nada fizer isso, o laço nunca para (**laço infinito**). Esse era exatamente o erro do [ex07](#erros-corrigidos).

**Usado em:** [ex02](ex02_processando_dados.py) · [ex03](ex03_mensagem_repetida.py) · [ex07](ex07_controle_de_estoque.py) · [ex08](ex08_contagem_regressiva.py) · [ex10](ex10_cadastro_de_usuario.py)

#### `range()`

O `range()` gera uma sequência de números inteiros. Quase sempre é usado junto com o `for`.

| Forma | Gera | Exemplo |
|---|---|---|
| `range(fim)` | de 0 até `fim - 1` | `range(5)` → 0, 1, 2, 3, 4 |
| `range(inicio, fim)` | de `inicio` até `fim - 1` | `range(1, 4)` → 1, 2, 3 |
| `range(inicio, fim, passo)` | de `passo` em `passo` | `range(10, 0, -1)` → 10, 9, …, 1 |

> O `fim` **nunca** entra na sequência. Com passo negativo, a contagem é regressiva.
>
> Se o número gerado não é usado dentro do laço, a convenção é chamar a variável de `_`: `for _ in range(5):`.

**Usado em:** [ex03](ex03_mensagem_repetida.py) · [ex08](ex08_contagem_regressiva.py)

#### `while True`

Como `True` é sempre verdadeiro, esse laço nunca termina sozinho. A saída fica por conta de um [`break`](#break) lá dentro.

É ideal quando você **não sabe quantas tentativas vai precisar**, como ao validar o que o usuário digita:

```python
while True:
    senha = input("Senha: ")
    if len(senha) >= 8:
        break                      # válida → sai do laço
    print("Curta demais, tente de novo.")
```

**Usado em:** [ex10](ex10_cadastro_de_usuario.py)

---

### Controle do laço

#### `break`

O `break` **interrompe o laço na hora**, mesmo que ainda faltem itens ou que a condição continue verdadeira. O programa segue na primeira linha depois do laço.

```python
for livro in livros:
    if livro == "O Hobbit":
        print("Achei!")
        break        # não precisa olhar o resto da lista
```

**Usado em:** [ex06](ex06_busca_de_livro.py) · [ex10](ex10_cadastro_de_usuario.py)

#### `continue`

O `continue` **pula o resto desta volta** e vai direto para a próxima. É útil para ignorar alguns itens.

```python
for livro in livros:
    if livro["estoque"] == 0:
        continue     # sem estoque → ignora este livro
    print(livro["nome"])
```

| | `break` | `continue` |
|---|---|---|
| O que faz | encerra o laço inteiro | pula só a volta atual |
| Para onde vai | para a linha depois do laço | para o topo do laço (próxima volta) |

**Usado em:** [ex09](ex09_livros_disponiveis.py) · [ex10](ex10_cadastro_de_usuario.py)

---

### Decisões

#### `if` e `else`

O `if` executa um bloco **só se** a condição for verdadeira. O `else`, que é opcional, roda no caso contrário.

```python
if segundos % 2 == 0:
    print("par")
else:
    print("ímpar")
```

**Usado em:** [ex05](ex05_projetos_ausentes.py) · [ex06](ex06_busca_de_livro.py) · [ex08](ex08_contagem_regressiva.py) · [ex09](ex09_livros_disponiveis.py) · [ex10](ex10_cadastro_de_usuario.py)

#### Operadores de comparação

| Operador | Significa | Exemplo |
|---|---|---|
| `==` | igual a | `livro == "O Hobbit"` |
| `!=` | diferente de | `estoque != 0` |
| `<` e `>` | menor que e maior que | `contador < 10` |
| `<=` e `>=` | menor ou igual e maior ou igual | `len(senha) >= 8` |
| `is` | é o mesmo objeto (use com `None`) | `projeto is None` |

> Não confunda `=` (**guarda** um valor numa variável) com `==` (**compara** dois valores).

---

### Operadores

#### Atribuição composta

São atalhos para atualizar uma variável a partir do valor que ela já tem:

| Atalho | Equivale a |
|---|---|
| `x += 1` | `x = x + 1` |
| `x -= 1` | `x = x - 1` |
| `x *= 2` | `x = x * 2` |
| `x /= 2` | `x = x / 2` |

**Usado em:** [ex02](ex02_processando_dados.py) · [ex03](ex03_mensagem_repetida.py) · [ex04](ex04_soma_de_receitas.py) · [ex07](ex07_controle_de_estoque.py) · [ex08](ex08_contagem_regressiva.py)

#### Resto da divisão

O operador `%` (chamado de *módulo*) devolve o **resto** de uma divisão inteira:

```python
7 % 2     # 1  → 7 = 2 × 3 + 1
10 % 2    # 0  → 10 = 2 × 5 + 0
```

O uso mais comum é descobrir se um número é **par**: `n % 2 == 0`.

**Usado em:** [ex08](ex08_contagem_regressiva.py)

---

### Entrada e saída

#### `print()`

O `print()` mostra algo na tela. Ele aceita vários valores separados por vírgula e coloca um espaço entre eles:

```python
print("Total:", 150)   # Total: 150
print()                # linha em branco
```

#### f-string

Uma string com `f` antes das aspas permite colocar variáveis, e até contas, dentro de `{}`:

```python
nome = "Ana"
print(f"Olá, {nome}!")        # Olá, Ana!
print(f"Dobro: {2 * 5}")      # Dobro: 10
```

> Se a f-string usa aspas duplas, use aspas simples lá dentro, e vice-versa: `f"Livro: {livro['nome']}"`.
>
> Para mostrar só uma variável, `print(nome)` já basta. A f-string vale a pena quando você mistura texto e valores.

**Usado em:** quase todos os exercícios

#### `input()`

O `input()` mostra uma mensagem e **espera o usuário digitar** alguma coisa e apertar Enter.

```python
nome = input("Digite seu nome: ")
```

> O que o usuário digita volta **sempre como texto (`str`)**, mesmo que sejam números.

**Usado em:** [ex10](ex10_cadastro_de_usuario.py)

#### `len()`

O `len()` retorna o **tamanho** de algo: quantos caracteres tem uma string ou quantos itens tem uma lista.

```python
len("Eduardo")         # 7
len([10, 20, 30])      # 3
```

**Usado em:** [ex10](ex10_cadastro_de_usuario.py)

---

### Padrões de laço

Não são comandos do Python. São **receitas** que aparecem o tempo todo.

#### Contador

Um contador é uma variável que **conta** quantas vezes algo aconteceu, ou que controla quantas voltas o `while` dá. Ela começa com um valor e sobe ou desce a cada volta.

```python
contador = 0
while contador < 5:
    ...
    contador += 1
```

**Usado em:** [ex02](ex02_processando_dados.py) · [ex03](ex03_mensagem_repetida.py) · [ex07](ex07_controle_de_estoque.py) · [ex08](ex08_contagem_regressiva.py)

#### Acumulador

Um acumulador é uma variável que **vai juntando** um resultado ao longo do laço. Para somas, começa em `0`.

```python
soma = 0
for numero in valores:
    soma += numero
```

> Para somar uma lista, o Python já tem pronto o `sum(valores)`. Mesmo assim, vale entender o acumulador, porque nem todo acúmulo é uma soma simples.

**Usado em:** [ex04](ex04_soma_de_receitas.py)

---

## `for` ou `while`?

| Situação | Use | Exemplo |
|---|---|---|
| Percorrer todos os itens de uma lista | `for` | [ex01](ex01_lista_de_clientes.py), [ex04](ex04_soma_de_receitas.py), [ex09](ex09_livros_disponiveis.py) |
| Repetir um número conhecido de vezes | `for` + `range()` | [ex03](ex03_mensagem_repetida.py), [ex08](ex08_contagem_regressiva.py) |
| Repetir enquanto uma condição for verdadeira | `while` | [ex02](ex02_processando_dados.py), [ex07](ex07_controle_de_estoque.py) |
| Não sei quantas vezes (depende do usuário) | `while True` + `break` | [ex10](ex10_cadastro_de_usuario.py) |

> **Regra de bolso:** se você sabe *quantas vezes* vai repetir, ou *sobre o que* vai repetir, use `for`. Se a repetição depende de uma condição, use `while`.

---

## Erros corrigidos

Ao organizar os exercícios, alguns problemas do código original foram corrigidos. Nos arquivos, cada um está marcado com `# CORREÇÃO` ou `# MELHORIA`.

| Onde | Problema | O que foi feito |
|---|---|---|
| [ex07](ex07_controle_de_estoque.py) | `while contador > 0` usava a variável **do ex02**, que valia 10 e nunca diminuía, e o laço ficava **infinito** | A condição passou a testar a própria variável do estoque |
| [ex07](ex07_controle_de_estoque.py) | Mostrava o estoque **antes** de descontar a venda (a 1ª venda dizia "restante: 5") | Primeiro desconta, depois mostra |
| [ex07](ex07_controle_de_estoque.py) | Variável `Contador_estoque` com maiúscula; mensagem "esotque" | Renomeada para `estoque` ([convenção de nomes](#variáveis-e-nomes)); texto corrigido |
| [ex08](ex08_contagem_regressiva.py) | `-= 1` repetido dentro do `if` **e** do `else` | Uma única linha, fora do `if`/`else` |
| [ex01](ex01_lista_de_clientes.py) | `print(f"{nome}")` | `print(nome)`, porque f-string sem texto junto é desnecessária |
| Todos | 10 exercícios num único arquivo `for and while.py`, com variáveis de um vazando para o outro | Um arquivo por exercício, cada um roda sozinho |
