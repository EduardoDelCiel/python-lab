# Manipulando texto

**Mundo 1 · Desafios 022 a 027**

Tudo o que dá para fazer com uma string: medir, cortar, procurar, trocar, separar e mudar maiúsculas e minúsculas.

[← Voltar ao Mundo 1](../README.md)

## Desafios

| # | Arquivo | O que faz | Conceitos |
|---|---|---|---|
| 022 | [desafio022_analisando_um_nome.py](desafio022_analisando_um_nome.py) | Nome em maiúsculas/minúsculas e contagem de letras | `.upper()`, `.lower()`, `len()`, `.replace()`, `.split()`, `.count()` |
| 023 | [desafio023_separando_digitos.py](desafio023_separando_digitos.py) | Separa milhar, centena, dezena e unidade | `//`, `%` |
| 024 | [desafio024_comeca_com_santo.py](desafio024_comeca_com_santo.py) | Diz se a cidade começa com "Santo" | fatiamento `[:5]`, `.strip()` |
| 025 | [desafio025_tem_silva_no_nome.py](desafio025_tem_silva_no_nome.py) | Diz se o nome tem "Silva" | `in` |
| 026 | [desafio026_letra_a_na_frase.py](desafio026_letra_a_na_frase.py) | Conta a letra "A" e acha a 1ª e a última posição | `.count()`, `.find()`, `.rfind()` |
| 027 | [desafio027_primeiro_e_ultimo_nome.py](desafio027_primeiro_e_ultimo_nome.py) | Mostra o primeiro e o último nome | `.split()`, índices |

---

## Anotações

### Índices

Uma string é uma **sequência de caracteres**, e cada um tem uma posição (o **índice**), que começa em **0**. Índices negativos contam a partir do fim:

```
  C    u    r    s    o
  0    1    2    3    4
 -5   -4   -3   -2   -1
```

```python
texto = "Curso"
texto[0]      # 'C'
texto[-1]     # 'o' (o último)
```

> Por isso o desafio 026 soma `+ 1` na posição: para o Python a primeira letra é a 0, mas para as pessoas ela é a 1.

### Fatiamento

`texto[inicio:fim]` pega um **pedaço** da string, do `inicio` até o `fim`, **sem incluir o fim**. Se um dos lados ficar vazio, ele vale "desde o começo" ou "até o final":

| Fatia | Pega | Em `"Santo André"` |
|---|---|---|
| `[:5]` | as 5 primeiras letras | `'Santo'` |
| `[6:]` | do índice 6 até o fim | `'André'` |
| `[0:3]` | do índice 0 ao 2 | `'San'` |
| `[::2]` | pulando de 2 em 2 | `'SnoAdé'` |
| `[::-1]` | tudo, de trás para frente | `'érdnA otnaS'` |

### `len()`

O `len()` conta quantos caracteres a string tem (espaços também contam):

```python
len("Eduardo")          # 7
len("Ana Maria")        # 9
```

### Maiúsculas e minúsculas

| Método | Resultado para `"eDUARDO del ciel"` |
|---|---|
| `.upper()` | `'EDUARDO DEL CIEL'` |
| `.lower()` | `'eduardo del ciel'` |
| `.capitalize()` | `'Eduardo del ciel'` (só a 1ª letra do texto) |
| `.title()` | `'Eduardo Del Ciel'` (a 1ª letra de cada palavra) |

> Para comparar textos sem se preocupar com maiúsculas, converta os dois lados: `cidade[:5].upper() == "SANTO"`.

### Limpando espaços

| Método | Remove os espaços | `"  Ana  "` vira |
|---|---|---|
| `.strip()` | do começo e do fim | `'Ana'` |
| `.lstrip()` | só do começo (esquerda) | `'Ana  '` |
| `.rstrip()` | só do fim (direita) | `'  Ana'` |

> Use `.strip()` logo no `input()`: `nome = input("Nome: ").strip()`. Assim, espaços digitados sem querer não atrapalham.

### Procurando

| Uso | O que faz | Em `"banana"` |
|---|---|---|
| `.count("a")` | quantas vezes aparece | `3` |
| `.find("a")` | posição da **primeira** vez | `1` |
| `.rfind("a")` | posição da **última** vez | `5` |
| `"nan" in texto` | aparece em algum lugar? | `True` |

> Quando não encontra nada, o `.find()` e o `.rfind()` devolvem `-1`.

### Trocando

O `.replace(velho, novo)` troca todas as ocorrências de um texto por outro:

```python
"Ana Maria".replace(" ", "")      # 'AnaMaria' (troca espaço por nada)
"banana".replace("a", "o")        # 'bonono'
```

> Como todos os métodos de string, ele **não altera** a string original. Ele devolve uma string nova.

### Dividindo e juntando

O `.split()` quebra o texto nos espaços e devolve uma **lista** de palavras. O `.join()` faz o contrário:

```python
nome = "Eduardo Del Ciel".split()    # ['Eduardo', 'Del', 'Ciel']
nome[0]                              # 'Eduardo' (primeiro)
nome[-1]                             # 'Ciel' (último)
len(nome)                            # 3 (quantos nomes)

"-".join(nome)                       # 'Eduardo-Del-Ciel'
```

### Separando os dígitos de um número

O desafio 023 usa matemática em vez de texto. A ideia é combinar a **divisão inteira** (`//`), que corta os últimos dígitos, com o **resto** (`%`), que fica só com o último:

| Dígito | Conta | Com `1834` |
|---|---|---|
| unidade | `n % 10` | `4` |
| dezena | `n // 10 % 10` | `183 % 10` → `3` |
| centena | `n // 100 % 10` | `18 % 10` → `8` |
| milhar | `n // 1000 % 10` | `1 % 10` → `1` |

---

## Correções e dicas

| Desafio | O que mudou |
|---|---|
| 024 | **Melhoria:** `.strip()` no `input()`. Sem ele, " Santo André" (com espaço antes) dava `False` |
| 025 | Dica: o `in` também acha "Silva" dentro de "Silvana". Para a palavra inteira, use `.split()` |
| 026 | Dica: o `str()` em volta do `input()` não é necessário |
| 027 | Texto: "Último nome" ganhou os dois-pontos. Dica: `Nome[-1]` é o mesmo que `Nome[len(Nome) - 1]` |
| 023 | Dica: `numero // 1 % 10` pode ser só `numero % 10` |
