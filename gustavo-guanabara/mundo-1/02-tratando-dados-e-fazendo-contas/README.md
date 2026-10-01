# Tratando dados e fazendo contas

**Mundo 1 · Desafios 003 a 015**

Os tipos de dados do Python, como converter o que o usuário digita e como fazer contas.

[← Voltar ao Mundo 1](../README.md)

## Desafios

| # | Arquivo | O que faz | Conceitos |
|---|---|---|---|
| 003 | [desafio003_soma_de_dois_numeros.py](desafio003_soma_de_dois_numeros.py) | Soma dois números | `int()`, `+` |
| 004 | [desafio004_dissecando_uma_variavel.py](desafio004_dissecando_uma_variavel.py) | Mostra o tipo e as características do que foi digitado | `type()`, métodos `is...()` |
| 005 | [desafio005_antecessor_e_sucessor.py](desafio005_antecessor_e_sucessor.py) | Mostra o antecessor e o sucessor | `+`, `-` |
| 006 | [desafio006_dobro_triplo_e_raiz.py](desafio006_dobro_triplo_e_raiz.py) | Dobro, triplo e raiz quadrada | `*`, `**` |
| 007 | [desafio007_media_das_notas.py](desafio007_media_das_notas.py) | Média de duas notas | `float()`, parênteses |
| 008 | [desafio008_conversor_de_medidas.py](desafio008_conversor_de_medidas.py) | Metros para centímetros e milímetros | multiplicação |
| 009 | [desafio009_tabuada.py](desafio009_tabuada.py) | Tabuada de um número | multiplicação |
| 010 | [desafio010_conversor_de_moedas.py](desafio010_conversor_de_moedas.py) | Reais para dólares | divisão, `{:.2f}` |
| 011 | [desafio011_pintando_parede.py](desafio011_pintando_parede.py) | Área da parede e litros de tinta | `*`, `/` |
| 012 | [desafio012_desconto_de_5.py](desafio012_desconto_de_5.py) | Preço com 5% de desconto | porcentagem |
| 013 | [desafio013_aumento_de_salario.py](desafio013_aumento_de_salario.py) | Salário com 15% de aumento | porcentagem |
| 014 | [desafio014_celsius_para_fahrenheit.py](desafio014_celsius_para_fahrenheit.py) | Converte °C para °F | fórmula, precedência |
| 015 | [desafio015_aluguel_de_carro.py](desafio015_aluguel_de_carro.py) | Preço do aluguel por dias e km | `int()` e `float()` juntos |

---

## Anotações

### Tipos primitivos

Todo valor em Python tem um **tipo**. Os quatro básicos:

| Tipo | Guarda | Exemplos |
|---|---|---|
| `int` | números inteiros | `7`, `-3`, `0` |
| `float` | números com casas decimais | `3.5`, `-0.15`, `7.0` |
| `str` | texto (string) | `"Olá"`, `"7"` |
| `bool` | verdadeiro ou falso | `True`, `False` |

> Em Python, a casa decimal é separada por **ponto**: `3.5`, e não `3,5`.

### `type()`

O `type()` mostra o tipo de um valor:

```python
type(7)        # <class 'int'>
type(7.0)      # <class 'float'>
type("7")      # <class 'str'>
type(True)     # <class 'bool'>
```

### Convertendo tipos

O `input()` **sempre devolve texto (`str`)**, mesmo que a pessoa digite um número. O desafio 004 mostra isso: o tipo sempre sai `str`. Para fazer contas, é preciso converter:

| Função | Converte para | Exemplo |
|---|---|---|
| `int()` | inteiro | `int("7")` → `7` |
| `float()` | número com casas decimais | `float("7.5")` → `7.5` |
| `str()` | texto | `str(7)` → `"7"` |
| `bool()` | verdadeiro/falso | `bool("")` → `False` |

O erro clássico de quem esquece a conversão:

```python
n1 = input("Número 1: ")    # digitou 2
n2 = input("Número 2: ")    # digitou 3
print(n1 + n2)              # 23  ← juntou os textos!

n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
print(n1 + n2)              # 5
```

> Use `int()` para coisas que não têm fração (idade, dias, quantidade) e `float()` para o resto (preço, peso, nota).

### Métodos de verificação

Os métodos que começam com `is` fazem uma pergunta sobre o texto e respondem `True` ou `False`:

| Método | Pergunta | `"123"` | `"abc"` | `"Abc"` | `"   "` |
|---|---|---|---|---|---|
| `.isnumeric()` | só tem números? | True | False | False | False |
| `.isalpha()` | só tem letras? | False | True | True | False |
| `.isalnum()` | só tem letras e/ou números? | True | True | True | False |
| `.isupper()` | está tudo em maiúsculas? | False | False | False | False |
| `.islower()` | está tudo em minúsculas? | False | True | False | False |
| `.istitle()` | está capitalizado (1ª letra maiúscula)? | False | False | True | False |
| `.isspace()` | só tem espaços? | False | False | False | True |

### Operadores aritméticos

| Operador | Operação | Exemplo | Resultado |
|---|---|---|---|
| `+` | soma | `7 + 2` | `9` |
| `-` | subtração | `7 - 2` | `5` |
| `*` | multiplicação | `7 * 2` | `14` |
| `/` | divisão | `7 / 2` | `3.5` |
| `**` | potência | `7 ** 2` | `49` |
| `//` | divisão inteira (sem a parte decimal) | `7 // 2` | `3` |
| `%` | resto da divisão | `7 % 2` | `1` |

> A divisão com `/` **sempre** dá `float`: `10 / 2` é `5.0`.

### Ordem de precedência

Como na matemática, o Python não faz as contas da esquerda para a direita. Ele segue esta ordem:

1. `()` parênteses
2. `**` potência
3. `*`, `/`, `//`, `%`
4. `+`, `-`

```python
5 + 3 * 2       # 11 → primeiro 3 * 2, depois + 5
(5 + 3) * 2     # 16 → o parêntese vem primeiro
```

Por isso a média do desafio 007 precisa de parênteses:

```python
(nota1 + nota2) / 2    # certo
nota1 + nota2 / 2      # errado: divide só a nota2
```

### Raiz quadrada

Elevar a `1/2` é o mesmo que tirar a raiz quadrada (e a `1/3`, a raiz cúbica):

```python
16 ** (1/2)     # 4.0
27 ** (1/3)     # 3.0
```

> Na seção [Usando módulos](../03-usando-modulos/README.md) aparece outra forma: `sqrt()`, do módulo `math`.

### Porcentagem

`5%` é `5 / 100`, ou seja, `0.05`:

| Cálculo | Fórmula | Atalho |
|---|---|---|
| desconto de 5% | `preco - preco * 0.05` | `preco * 0.95` |
| aumento de 15% | `salario + salario * 0.15` | `salario * 1.15` |
| quanto é 10% | `valor * 0.10` | — |

### Formatando números

Divisões costumam gerar muitas casas decimais: `100 / 5.23` dá `19.12045889101338`. Dentro das chaves dá para dizer **como** o número deve aparecer:

```python
valor = 100 / 5.23
print("{:.2f}".format(valor))     # 19.12  → 2 casas decimais
print("{:.0f}".format(valor))     # 19     → nenhuma casa
```

O `.2f` quer dizer "número com 2 casas depois do ponto". Para dinheiro, use sempre `{:.2f}`.

### Nomes de variáveis

Os nomes que você usou (`Numero`, `Salario`, `PrecoFinal`) funcionam normalmente. A convenção oficial do Python é outra, porém: **minúsculas, com `_` entre as palavras** (o chamado *snake_case*):

| Estilo | Exemplo | Uso em Python |
|---|---|---|
| `snake_case` | `preco_final` | variáveis e funções (o padrão) |
| `PascalCase` | `PrecoFinal` | classes, um assunto mais avançado |

Vale também dar nomes que digam **o que a variável guarda**. No desafio 012, `Desconto` guarda o preço novo, e não o desconto.

---

## Correções e dicas

Nenhum desafio desta seção tinha erro de lógica. Os ajustes foram nos textos e alguns comentários de dica:

| Desafio | O que mudou |
|---|---|
| 004 | Textos: "Alfanúmerico" → "alfanumérico". Dica: incluir também o `.isnumeric()` |
| 006 | Dica: usar `{:.2f}` para a raiz não sair com 14 casas |
| 008 | Texto: "Centimentros" → "centímetros" |
| 009 | Nova "outra forma" que mostra a conta inteira (`7 x 3 = 21`) |
| 010 | Texto: "atulamente tem ... e caso voce pode" → "atualmente tem ... e pode". Nova "outra forma" com `{:.2f}` para o valor em dinheiro |
| 012 e 013 | Dica sobre o nome da variável (ela guarda o valor novo, e não o desconto ou o aumento) |
