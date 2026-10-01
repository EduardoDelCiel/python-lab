# Usando módulos

**Mundo 1 · Desafios 016 a 021**

Como usar código pronto: os módulos que já vêm com o Python (`math`, `random`) e as bibliotecas que a gente instala (`pygame`).

[← Voltar ao Mundo 1](../README.md)

## Desafios

| # | Arquivo | O que faz | Conceitos |
|---|---|---|---|
| 016 | [desafio016_parte_inteira.py](desafio016_parte_inteira.py) | Mostra a parte inteira de um número real | `import math`, `trunc()` |
| 017 | [desafio017_hipotenusa.py](desafio017_hipotenusa.py) | Calcula a hipotenusa | `from math import hypot`, `{:.2f}` |
| 018 | [desafio018_seno_cosseno_tangente.py](desafio018_seno_cosseno_tangente.py) | Seno, cosseno e tangente de um ângulo | `sin()`, `cos()`, `tan()`, `radians()`, f-string |
| 019 | [desafio019_sorteando_um_aluno.py](desafio019_sorteando_um_aluno.py) | Sorteia um aluno | `random.choice()`, lista |
| 020 | [desafio020_sorteando_a_ordem.py](desafio020_sorteando_a_ordem.py) | Sorteia a ordem dos alunos | `random.shuffle()` |
| 021 | [desafio021_tocando_mp3.py](desafio021_tocando_mp3.py) | Toca o arquivo [mikolash.mp3](mikolash.mp3) | `pygame`, `pip install` |

---

## Anotações

### O que é um módulo

Um **módulo** é um arquivo com funções prontas que você carrega no seu programa. O Python já vem com vários (a *biblioteca padrão*), e outros podem ser instalados.

### `import` e `from ... import`

Há dois jeitos de carregar um módulo:

| Jeito | Como usar depois | Quando usar |
|---|---|---|
| `import math` | `math.trunc(x)`, `math.sqrt(x)` | vai usar várias coisas do módulo |
| `from math import trunc` | `trunc(x)` | vai usar só uma ou outra função |
| `from math import sin, cos, tan` | `sin(x)`, `cos(x)` | várias funções, separadas por vírgula |

> Escolha um dos jeitos para cada módulo. No desafio 016 havia os dois ao mesmo tempo, mas só um era usado.
>
> Os `import` ficam sempre no **topo** do arquivo.

### Módulo `math`

Funções matemáticas:

| Função | O que faz | Exemplo |
|---|---|---|
| `trunc(x)` | corta a parte decimal | `trunc(6.75)` → `6` |
| `floor(x)` | arredonda para baixo | `floor(6.75)` → `6` |
| `ceil(x)` | arredonda para cima | `ceil(6.25)` → `7` |
| `sqrt(x)` | raiz quadrada | `sqrt(16)` → `4.0` |
| `hypot(a, b)` | hipotenusa (Pitágoras) | `hypot(3, 4)` → `5.0` |
| `sin(x)`, `cos(x)`, `tan(x)` | seno, cosseno, tangente | `sin(radians(30))` → `0.4999...` (≈ 0.5) |
| `radians(x)` | converte graus para radianos | `radians(180)` → `3.14159...` |
| `pi` | o número π (não é função, é um valor) | `pi` → `3.141592653589793` |

> As funções `sin`, `cos` e `tan` esperam o ângulo em **radianos**. Por isso o desafio 018 converte com `radians()` antes.

### Módulo `random`

Sorteios:

| Função | O que faz | Exemplo |
|---|---|---|
| `choice(lista)` | sorteia **um** item da lista | `choice(["Ana", "Bia"])` → `"Bia"` |
| `shuffle(lista)` | **embaralha** a própria lista | a lista muda de ordem |
| `randint(a, b)` | sorteia um inteiro de `a` até `b` (os dois entram) | `randint(0, 5)` → `3` |
| `random()` | sorteia um número entre 0 e 1 | `0.7253...` |

> O `randint` volta na seção [Condições](../05-condicoes/README.md), no jogo da adivinhação (desafio 028).

### Listas

Os desafios 019 e 020 juntam os nomes numa **lista**, que guarda vários valores em ordem, entre colchetes:

```python
alunos = ["Ana", "Bia", "Cadu", "Dudu"]
print(alunos)        # ['Ana', 'Bia', 'Cadu', 'Dudu']
```

As listas são assunto do Mundo 3. Por enquanto, é o jeito de entregar vários valores de uma vez para o `choice()` e o `shuffle()`.

### f-string

O desafio 018 trouxe a **f-string**, que faz o mesmo que o `.format()` de um jeito mais curto. Basta colocar `f` antes das aspas e o nome da variável direto dentro das chaves:

```python
nome = "Eduardo"
print("Olá, {}!".format(nome))     # com .format()
print(f"Olá, {nome}!")             # com f-string
```

A formatação também funciona, com `:` depois do nome:

```python
seno = 0.49999999999999994
print(f"O seno é {seno:.2f}")      # O seno é 0.50
```

### Bibliotecas externas e o `pip`

O `pygame` não vem com o Python. É uma biblioteca de terceiros, e precisa ser instalada com o **pip**:

```bash
pip install pygame
```

No PyCharm, dá para instalar também em *Settings → Project → Python Interpreter → +*.

> **Por que o `.venv` não foi para o GitHub?** O PyCharm cria um *ambiente virtual* (a pasta `.venv`) em cada projeto, e é lá que o `pygame` fica instalado. São milhares de arquivos que qualquer pessoa recria com um `pip install`, então essa pasta não é versionada. O mesmo vale para a pasta `.idea`, que guarda só configurações do PyCharm.

### Cuidado: não use nome de função como variável

No desafio 018 havia esta linha:

```python
cos = cos(radians(Angulo))
```

Ela funciona uma vez, mas **substitui a função `cos` por um número**. Dali em diante, `cos(...)` dá erro:

```
TypeError: 'float' object is not callable
```

A regra: nunca dê a uma variável o nome de uma função que você usa (`cos`, `print`, `input`, `len`, `sum`...). Use `cosseno`, `total`, `tamanho`.

### Caminho de arquivos

Quando o programa abre um arquivo pelo nome (`"mikolash.mp3"`), o Python procura na **pasta de onde o programa foi executado**, que nem sempre é a pasta do `.py`. Para achar o arquivo que está ao lado do código, o desafio 021 usa:

```python
from pathlib import Path

arquivo = Path(__file__).parent / "mikolash.mp3"
```

O `__file__` é o caminho do próprio `.py`, e o `.parent` é a pasta dele.

---

## Correções e dicas

| Desafio | O que mudou |
|---|---|
| 018 | **Correção:** a variável `cos` substituía a função `cos()`. Renomeada para `cosseno` ([por quê](#cuidado-não-use-nome-de-função-como-variável)) |
| 021 | **Melhoria:** o mp3 é encontrado pela pasta do arquivo, e não da execução. Antes, rodando de fora da pasta, dava `No file 'mikolash.mp3' found` ([por quê](#caminho-de-arquivos)). O desafio também ganhou o cabeçalho com o enunciado, que não tinha |
| 016 | **Melhoria:** removido o `from math import trunc`, que não era usado (o código já usava `import math`) |
| 017 | Nome da variável: `CateotoAdjacente` → `CatetoAdjacente` |
