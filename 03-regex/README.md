# 03 · Strings e Regex (expressões regulares)

Este módulo tem duas partes:

1. **Strings:** os métodos prontos do Python para mexer com texto (`.lower()`, `.startswith()`, fatiamento...).
2. **Regex:** uma mini-linguagem para descrever **padrões** de texto, como "3 dígitos, um ponto, 3 dígitos...". Com ela dá para validar, encontrar, extrair e substituir pedaços de texto.

Alguns exercícios resolvem o mesmo problema dos dois jeitos, para você comparar.

[← Voltar ao índice geral](../README.md)

## Sumário

- [Exercícios](#exercícios)
- [Parte 1: Strings](#parte-1-strings)
  - **Métodos de string:** [O que é um método](#o-que-é-um-método) · [lower() e upper()](#lower-e-upper) · [startswith() e endswith()](#startswith-e-endswith) · [Métodos de verificação](#métodos-de-verificação)
  - **Índices e fatiamento:** [Índices](#índices) · [Fatiamento](#fatiamento)
  - **Lógica:** [and](#and) · [all()](#all) · [Valores verdadeiros e falsos](#valores-verdadeiros-e-falsos)
- [Parte 2: Regex](#parte-2-regex)
  - **O módulo re:** [O que é regex](#o-que-é-regex) · [import re](#import-re) · [Raw string](#raw-string)
  - **Funções:** [re.findall()](#refindall) · [re.sub()](#resub) · [re.match() e re.fullmatch()](#rematch-e-refullmatch) · [re.search()](#research) · [Objeto Match](#objeto-match) · [re.IGNORECASE](#reignorecase) · [re.escape()](#reescape) · [Qual função usar?](#qual-função-usar)
  - **Símbolos:** [Dígitos e letras](#dígitos-e-letras) · [Colchetes](#colchetes) · [Quantificadores](#quantificadores) · [Borda de palavra](#borda-de-palavra) · [Escapando caracteres especiais](#escapando-caracteres-especiais) · [Grupos](#grupos)
  - [Cola rápida de regex](#cola-rápida-de-regex)
- [Revisão: o que veio dos módulos anteriores](#revisão-o-que-veio-dos-módulos-anteriores)
- [Erros corrigidos](#erros-corrigidos)

---

## Exercícios

| # | Arquivo | O que faz | Conceitos principais |
|---|---|---|---|
| 01 | [ex01_nome_do_produto.py](ex01_nome_do_produto.py) | Mostra o nome do produto em minúsculas | `.lower()` |
| 02 | [ex02_boas_vindas.py](ex02_boas_vindas.py) | Monta uma mensagem com nome e cidade | revisão: `input()`, f-string |
| 03 | [ex03_partes_da_senha.py](ex03_partes_da_senha.py) | Mostra os 3 primeiros e os 3 últimos caracteres | fatiamento `[:3]` e `[-3:]` |
| 04 | [ex04_validar_url.py](ex04_validar_url.py) | Confere como a URL começa e termina | `.startswith()`, `.endswith()`, `and` |
| 05 | [ex05_numero_da_receita.py](ex05_numero_da_receita.py) | Encontra o primeiro número de um texto | `re.findall()`, `\d+` |
| 06 | [ex06_substituir_palavra.py](ex06_substituir_palavra.py) | Troca uma palavra inteira por outra | `re.sub()`, `\b`, `rf''`, `re.escape()` |
| 07 | [ex07_validar_nome.py](ex07_validar_nome.py) | Valida um nome (duas soluções: strings × regex) | `.isupper()`, `all()`, `re.fullmatch()`, `[A-Z]` |
| 08 | [ex08_validar_cpf.py](ex08_validar_cpf.py) | Valida o formato 000.000.000-00 | `\d{3}`, `\.`, `re.fullmatch()` |
| 09 | [ex09_palavras_por_letra.py](ex09_palavras_por_letra.py) | Lista as palavras que começam com uma letra | `re.findall()`, `re.IGNORECASE`, `[a-zà-ÿ]` |
| 10 | [ex10_nome_e_ano.py](ex10_nome_e_ano.py) | Separa nome, sobrenome e ano de nascimento | `re.search()`, grupos `()`, `.group()` |

---

## Parte 1: Strings

### Métodos de string

#### O que é um método

Um **método** é uma função que "pertence" a um tipo de dado e é chamada com **ponto**: `valor.metodo()`. Compare:

```python
len(nome)        # função: o valor vai dentro dos parênteses
nome.lower()     # método: o valor vem antes do ponto
```

Você já usou métodos no módulo 02: [`.append()`](../02-funcoes/README.md#append) e [`.ljust()`](../02-funcoes/README.md#ljust).

> Métodos de string **não alteram** a string original. Eles devolvem uma string **nova**, e por isso guardamos o resultado numa variável: `produto_lower = produto.lower()`.

#### `lower()` e `upper()`

| Método | Resultado para `"Café Premium"` |
|---|---|
| `.lower()` | `"café premium"` (tudo minúsculo) |
| `.upper()` | `"CAFÉ PREMIUM"` (tudo maiúsculo) |
| `.title()` | `"Café Premium"` (primeira letra de cada palavra maiúscula) |

> Truque comum para comparar sem se importar com maiúsculas: `if resposta.lower() == "sim":`.

**Usado em:** [ex01](ex01_nome_do_produto.py)

#### `startswith()` e `endswith()`

Respondem `True` ou `False`: a string **começa** ou **termina** com o texto indicado?

```python
url = "https://site.com"
url.startswith("https://")   # True
url.endswith(".com")         # True
url.endswith(".br")          # False
```

**Usado em:** [ex04](ex04_validar_url.py)

#### Métodos de verificação

Os métodos que começam com `is` **fazem uma pergunta** sobre a string e respondem `True` ou `False`:

| Método | Pergunta | `"A"` | `"a"` | `"7"` | `"@"` |
|---|---|---|---|---|---|
| `.isupper()` | é maiúscula? | True | False | False | False |
| `.islower()` | é minúscula? | False | True | False | False |
| `.isdigit()` | é dígito? | False | False | True | False |
| `.isalpha()` | é letra? | True | True | False | False |
| `.isalnum()` | é letra ou dígito? | True | True | True | False |

> Numa string com vários caracteres, a pergunta vale para **todos** eles: `"Ana".isalpha()` dá `True`, mas `"Ana Maria".isalpha()` dá `False`, porque o espaço não é letra.
>
> No ex07, `sem_numeros and sem_simbolos` equivale, na prática, a um simples `nome1.isalpha()`.

**Usado em:** [ex07](ex07_validar_nome.py)

---

### Índices e fatiamento

#### Índices

Cada caractere de uma string, e cada item de uma lista, tem uma **posição** (índice), começando em **0**. Índices negativos contam **a partir do fim**:

```
  P    y    t    h    o    n
  0    1    2    3    4    5
 -6   -5   -4   -3   -2   -1
```

```python
palavra = "Python"
palavra[0]     # 'P'
palavra[-1]    # 'n'
```

> Acessar uma posição que não existe dá `IndexError`, como em `""[0]` ou `[][0]`. Esse erro podia acontecer em dois exercícios ([veja as correções](#erros-corrigidos)).

**Usado em:** [ex05](ex05_numero_da_receita.py) (`numeros[0]`) · [ex07](ex07_validar_nome.py) (`nome1[0]`)

#### Fatiamento

`texto[inicio:fim]` pega um **pedaço** do texto: do `inicio` até o `fim`, **sem incluir o fim** (igual ao [`range()`](../01-for-e-while/README.md#range)). Se você deixar um dos lados vazio, ele vale "desde o começo" ou "até o final".

| Fatia | Pega | Em `"Python"` |
|---|---|---|
| `[:3]` | os 3 primeiros | `'Pyt'` |
| `[-3:]` | os 3 últimos | `'hon'` |
| `[1:4]` | do índice 1 ao 3 | `'yth'` |
| `[::-1]` | tudo, de trás para frente | `'nohtyP'` |

> Fatiar nunca dá erro. Se o texto for curto, vem o que tiver: `"ab"[:3]` dá `'ab'`.

**Usado em:** [ex03](ex03_partes_da_senha.py)

---

### Lógica

#### `and`

O `and` junta condições, e o resultado só é `True` se **todas** forem verdadeiras. O irmão dele é o `or`, que precisa de **pelo menos uma**. Já o [`not`](../02-funcoes/README.md#not) inverte o valor.

| A | B | `A and B` | `A or B` |
|---|---|---|---|
| True | True | True | True |
| True | False | False | True |
| False | False | False | False |

> **Curto-circuito:** o `and` para de avaliar assim que encontra um falso. O ex07 usa isso para se proteger: em `len(nome1) > 0 and nome1[0].isupper()`, se o nome estiver vazio, o Python nem chega a ler `nome1[0]`, que daria erro.

**Usado em:** [ex04](ex04_validar_url.py) · [ex07](ex07_validar_nome.py)

#### `all()`

O `all(...)` responde `True` se **todos** os itens forem verdadeiros. O irmão dele é o `any()`, que precisa de **pelo menos um**.

No ex07 ele aparece com uma **expressão geradora**, que é um [`for`](../01-for-e-while/README.md#for) escrito dentro dos parênteses e que produz um `True`/`False` para cada caractere:

```python
all(caractere.isalnum() for caractere in nome1)
```

Leia assim: *"para cada caractere de nome1, pergunte se ele é letra ou dígito. Todos responderam sim?"* É o mesmo que:

```python
todos_ok = True
for caractere in nome1:
    if not caractere.isalnum():
        todos_ok = False
        break
```

**Usado em:** [ex07](ex07_validar_nome.py)

#### Valores verdadeiros e falsos

Num `if`, qualquer valor pode servir de condição. Os valores "vazios" contam como **falsos**, e todo o resto conta como verdadeiro:

| Contam como falso | Contam como verdadeiro |
|---|---|
| `False`, `None`, `0`, `""`, `[]`, `{}` | todo o resto: `"abc"`, `[1]`, `42`, um objeto Match... |

```python
numeros = re.findall(r'\d+', texto)
if numeros:              # a lista tem alguma coisa?
    ...

resultado = re.search(padrao, tudo)
if resultado:            # achou? (o search devolve None quando não acha)
    ...
```

**Usado em:** [ex05](ex05_numero_da_receita.py) · [ex10](ex10_nome_e_ano.py)

---

## Parte 2: Regex

### O módulo `re`

#### O que é regex

**Regex** (*regular expression*, ou expressão regular) é uma mini-linguagem para descrever **padrões de texto**. Em vez de procurar um texto fixo, você descreve a **forma** dele:

```
\d{3}\.\d{3}\.\d{3}-\d{2}     →  casa com 123.456.789-09
```

Com regex você consegue **validar**, **encontrar**, **extrair** e **substituir** pedaços de texto.

> Para testar padrões antes de colocar no código, use o site [regex101.com](https://regex101.com) e escolha o *flavor* "Python".

#### `import re`

As funções de regex ficam no módulo `re`, que vem com o Python. Ele é carregado com [`import`](../02-funcoes/README.md#import):

```python
import re
```

> Basta um `import re` no topo do arquivo. No arquivo original ele estava repetido antes de cada exercício.

#### Raw string

Regex usa muita **barra invertida** (`\d`, `\b`, `\w`). O problema é que o Python também dá significado a algumas barras dentro de strings comuns: `\n` vira quebra de linha, e `\b` vira um caractere invisível de "backspace".

Para o Python **não mexer nas barras**, coloque um `r` antes das aspas. Isso é uma *raw string* (string bruta):

```python
r'\d+'          # o Python entrega \d+ intacto para o regex
```

Dá para juntar com a [f-string](../01-for-e-while/README.md#f-string): o **`rf''`** mantém as barras e ainda aceita variáveis dentro de `{}`.

```python
padrao = rf'\b{palavra}\b'
```

> **Regra de bolso:** padrão de regex leva sempre um `r` na frente.

**Usado em:** todos os exercícios de regex (ex05 a ex10). `rf` aparece em [ex06](ex06_substituir_palavra.py) e [ex09](ex09_palavras_por_letra.py).

---

### Funções do módulo `re`

#### `re.findall()`

`re.findall(padrao, texto)` encontra **todas** as ocorrências e devolve uma **lista** de textos. Se não achar nada, a lista vem vazia.

```python
re.findall(r'\d+', "Pedido 12, mesa 7")    # ['12', '7']
re.findall(r'\d+', "sem números")          # []
```

**Usado em:** [ex05](ex05_numero_da_receita.py) · [ex09](ex09_palavras_por_letra.py)

#### `re.sub()`

`re.sub(padrao, substituto, texto)` **troca** tudo que casar com o padrão e devolve o texto novo:

```python
re.sub(r'\d', '#', "Senha 1234")      # 'Senha ####'
```

**Usado em:** [ex06](ex06_substituir_palavra.py)

#### `re.match()` e `re.fullmatch()`

As duas conferem se um texto segue um padrão, mas com uma diferença importante:

| Função | Confere se... | `r'[A-Z][a-z]*'` em `"Ana123"` |
|---|---|---|
| `re.match()` | o **começo** do texto segue o padrão | casa com `"Ana"` e ignora o resto |
| `re.fullmatch()` | o texto **inteiro** segue o padrão | não casa |

> Para **validar** (nome, CPF, e-mail...) quase sempre o que você quer é `re.fullmatch()`. Esse era o bug do ex07 e do ex08.

**Usado em:** [ex07](ex07_validar_nome.py) · [ex08](ex08_validar_cpf.py)

#### `re.search()`

`re.search(padrao, texto)` procura o padrão **em qualquer lugar** do texto e para na **primeira** ocorrência. Devolve um [objeto Match](#objeto-match), ou `None` se não achar.

```python
re.search(r'\d{4}', "Nasci em 1995, em SP")    # acha '1995'
```

**Usado em:** [ex10](ex10_nome_e_ano.py)

#### Objeto Match

`re.match()`, `re.fullmatch()` e `re.search()` devolvem um **objeto Match** quando encontram algo, e `None` quando não encontram. O Match guarda o que foi encontrado:

| Uso | Devolve |
|---|---|
| `resultado.group()` | o trecho inteiro encontrado |
| `resultado.group(1)` | o que o **1º grupo** `( )` capturou |
| `resultado.group(2)` | o que o **2º grupo** capturou, e assim por diante |

```python
resultado = re.search(r'(\w+) (\w+) - (\d{4})', "Eduardo Silva - 1995")
resultado.group(1)    # 'Eduardo'
resultado.group(3)    # '1995'
```

> Sempre teste `if resultado:` antes de chamar `.group()`. Se nada foi encontrado, `resultado` é `None`, e `None.group()` dá erro.

**Usado em:** [ex10](ex10_nome_e_ano.py)

#### `re.IGNORECASE`

É uma *flag*, uma opção extra passada como último argumento. Ela faz o regex **ignorar maiúsculas e minúsculas**:

```python
re.findall(r'\bp\w*', "Pedro pulou", re.IGNORECASE)   # ['Pedro', 'pulou']
```

> Ela iguala "a" e "A", mas **não** iguala "a" e "á", que são letras diferentes. Por isso, no ex09, a letra "a" não encontra "Árvore".

**Usado em:** [ex09](ex09_palavras_por_letra.py)

#### `re.escape()`

Coloca uma barra antes de cada símbolo especial de um texto, gerando um padrão que casa **exatamente com aquele texto**. Use sempre que o padrão incluir algo **digitado pelo usuário**:

```python
re.escape("1.5")      # vira  1\.5  → o ponto passa a ser um ponto de verdade
```

**Usado em:** [ex06](ex06_substituir_palavra.py) · [ex09](ex09_palavras_por_letra.py)

#### Qual função usar?

| Eu quero... | Função | Devolve |
|---|---|---|
| saber se o texto **inteiro** segue um formato | `re.fullmatch()` | Match ou `None` |
| saber se o texto **começa** com um padrão | `re.match()` | Match ou `None` |
| achar a **primeira** ocorrência em qualquer lugar | `re.search()` | Match ou `None` |
| pegar **todas** as ocorrências | `re.findall()` | lista de textos |
| **trocar** ocorrências | `re.sub()` | texto novo |

---

### Símbolos dos padrões

#### Dígitos e letras

| Símbolo | Casa com | Exemplo |
|---|---|---|
| `\d` | um dígito (0 a 9) | `\d` em `"a7"` → `7` |
| `\w` | uma letra (com ou sem acento), dígito ou `_` | `\w+` em `"João!"` → `João` |
| `\s` | um espaço em branco (espaço, tab, quebra de linha) | `\s` em `"a b"` → `" "` |
| `.` | **qualquer** caractere (menos quebra de linha) | `a.c` casa com `"abc"`, `"a7c"`... |

> Em maiúscula, o sentido se inverte: `\D` é "não-dígito", `\W` é "não-letra" e `\S` é "não-espaço".

**Usado em:** `\d` em [ex05](ex05_numero_da_receita.py), [ex08](ex08_validar_cpf.py) e [ex10](ex10_nome_e_ano.py) · `\w` em [ex10](ex10_nome_e_ano.py)

#### Colchetes

`[...]` casa com **um** caractere dentre os que estão listados. Com hífen, você define uma **faixa**:

| Padrão | Casa com |
|---|---|
| `[abc]` | a, b ou c |
| `[A-Z]` | uma letra maiúscula sem acento |
| `[a-z]` | uma letra minúscula sem acento |
| `[0-9]` | um dígito (o mesmo que `\d`) |
| `[A-ZÀ-Ý]` | uma maiúscula, com ou sem acento |
| `[a-zà-ÿ]` | uma minúscula, com ou sem acento |
| `[^0-9]` | qualquer coisa que **não** seja dígito (o `^` no começo nega) |

> `[A-Z]` e `[a-z]` **não** incluem letras acentuadas. Para nomes em português, acrescente as faixas `À-Ý` e `à-ÿ`.

**Usado em:** [ex07](ex07_validar_nome.py) · [ex09](ex09_palavras_por_letra.py)

#### Quantificadores

Os quantificadores dizem **quantas vezes** o item anterior pode aparecer:

| Símbolo | Quantidade | Exemplo |
|---|---|---|
| `+` | 1 ou mais | `\d+` → `"7"`, `"42"`, `"2024"` |
| `*` | 0 ou mais | `[a-z]*` → `""`, `"a"`, `"ana"` |
| `?` | 0 ou 1 (opcional) | `https?` → `"http"` ou `"https"` |
| `{n}` | exatamente n | `\d{4}` → `"1995"` |
| `{n,m}` | de n até m | `\d{2,4}` → `"12"`, `"123"`, `"1234"` |

**Usado em:** `+` em [ex05](ex05_numero_da_receita.py) e [ex10](ex10_nome_e_ano.py) · `*` em [ex07](ex07_validar_nome.py) e [ex09](ex09_palavras_por_letra.py) · `{n}` em [ex08](ex08_validar_cpf.py) e [ex10](ex10_nome_e_ano.py)

#### Borda de palavra

O `\b` não casa com nenhum caractere. Ele marca a **fronteira** entre uma palavra e o que não é palavra: espaço, pontuação, início ou fim do texto.

```python
re.sub(r'\bgato\b', 'cão', "o gato e os gatos")   # 'o cão e os gatos'
re.sub(r'gato', 'cão', "o gato e os gatos")       # 'o cão e os cãos'   ← sem \b
```

**Usado em:** [ex06](ex06_substituir_palavra.py) · [ex09](ex09_palavras_por_letra.py)

#### Escapando caracteres especiais

Estes caracteres têm significado especial em regex: `. ^ $ * + ? { } [ ] \ ( ) |`

Para procurar o **próprio** caractere, coloque uma `\` antes dele:

| Padrão | Significa |
|---|---|
| `.` | qualquer caractere |
| `\.` | um ponto de verdade |
| `\(` | um parêntese de verdade |

> No CPF, sem a barra, o padrão `\d{3}.\d{3}` aceitaria `"123a456"`, porque o ponto casaria com o "a".
>
> Fora dos colchetes o hífen `-` é um caractere comum, então `\-` é desnecessário.

**Usado em:** [ex08](ex08_validar_cpf.py)

#### Grupos

Os parênteses `( )` criam **grupos**. Além de agrupar, eles **capturam** o trecho encontrado para você pegar depois com [`.group(n)`](#objeto-match). A contagem vai da esquerda para a direita:

```
(\w+) (\w+) - (\d{4})
  1     2       3
```

**Usado em:** [ex10](ex10_nome_e_ano.py)

---

### Cola rápida de regex

| Símbolo | Significado |
|---|---|
| `\d` | dígito |
| `\w` | letra, dígito ou `_` |
| `\s` | espaço em branco |
| `.` | qualquer caractere |
| `\.` | um ponto de verdade |
| `[abc]` | um caractere dentre a, b e c |
| `[a-z]` | um caractere da faixa |
| `[^abc]` | um caractere que **não** seja a, b nem c |
| `+` | 1 ou mais |
| `*` | 0 ou mais |
| `?` | 0 ou 1 |
| `{n}` | exatamente n |
| `{n,m}` | de n até m |
| `\b` | borda de palavra |
| `^` | início do texto |
| `$` | fim do texto |
| `( )` | grupo (captura um trecho) |

> `re.fullmatch(padrao, texto)` é o mesmo que usar `re.match` com `^` no começo e `$` no fim do padrão.

---

## Revisão: o que veio dos módulos anteriores

| Sintaxe | Onde aparece aqui | Explicação |
|---|---|---|
| `input()` | todos os exercícios | [input()](../01-for-e-while/README.md#input) |
| f-string | todos os exercícios | [f-string](../01-for-e-while/README.md#f-string) |
| `if` / `else` | ex04 a ex10 | [if e else](../01-for-e-while/README.md#if-e-else) |
| `for` | dentro do `all()` no ex07 | [for](../01-for-e-while/README.md#for) |
| `len()` | ex07 | [len()](../01-for-e-while/README.md#len) |
| `None` | ex10 (quando o `search` não acha) | [None](../01-for-e-while/README.md#none) |
| `import` | ex05 a ex10 | [import](../02-funcoes/README.md#import) |
| `not` | ex07 | [not](../02-funcoes/README.md#not) |

---

## Erros corrigidos

Nos arquivos, cada correção está marcada com `# CORREÇÃO` ou `# MELHORIA`.

| Onde | Problema | O que foi feito |
|---|---|---|
| [ex05](ex05_numero_da_receita.py) | `re.findall(...)[0]` quebrava com `IndexError` quando o texto não tinha número | testa se a lista tem algo antes de pegar o `[0]` |
| [ex06](ex06_substituir_palavra.py) | a palavra digitada entrava crua no padrão: pedir para trocar "1.5" trocava também "105", e digitar "(" quebrava o programa | `re.escape(palavra)` |
| [ex07](ex07_validar_nome.py) | a solução 1 testava a variável `texto` (do ex05) em vez do nome digitado | usa `nome1` |
| [ex07](ex07_validar_nome.py) | `nome1[0]` quebrava com o nome vazio | `len(nome1) > 0 and ...` ([curto-circuito](#and)) |
| [ex07](ex07_validar_nome.py) | `re.match()` aceitava "Ana123" | `re.fullmatch()`, com faixas de letras acentuadas |
| [ex08](ex08_validar_cpf.py) | `re.match()` aceitava "123.456.789-0999" | `re.fullmatch()` |
| [ex09](ex09_palavras_por_letra.py) | `re.findal` não existe (dava `AttributeError`), e a busca era feita em `texto` em vez de `livro` | `re.findall(..., livro, ...)` |
| [ex10](ex10_nome_e_ano.py) | o padrão começava com um espaço, então "Eduardo Silva - 1995" não era reconhecido | espaço removido |
| [ex04](ex04_validar_url.py) | variável `URL` toda em maiúsculas | `url` ([convenção de nomes](../01-for-e-while/README.md#variáveis-e-nomes)) |
| todos | 11 exercícios num arquivo chamado só `.pyt`, com `import re` repetido e variáveis de um exercício vazando para outro | um arquivo `.py` por exercício, cada um roda sozinho |
| ex11 | estava vazio no original | não foi incluído |
