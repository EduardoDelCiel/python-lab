# Condições

**Mundo 1 · Desafios 028 a 035**

O programa começa a tomar decisões: fazer uma coisa **ou** outra, dependendo de uma condição.

[← Voltar ao Mundo 1](../README.md)

## Desafios

| # | Arquivo | O que faz | Conceitos |
|---|---|---|---|
| 028 | [desafio028_jogo_da_adivinhacao.py](desafio028_jogo_da_adivinhacao.py) | O computador sorteia de 0 a 5 e você tenta adivinhar | `randint()`, `if`/`else` |
| 029 | [desafio029_radar_eletronico.py](desafio029_radar_eletronico.py) | Multa de R$7 por km acima de 80 km/h | `>` |
| 030 | [desafio030_par_ou_impar.py](desafio030_par_ou_impar.py) | Diz se o número é par ou ímpar | `%` |
| 031 | [desafio031_preco_da_passagem.py](desafio031_preco_da_passagem.py) | Preço da passagem por faixa de distância | `<=` |
| 032 | [desafio032_ano_bissexto.py](desafio032_ano_bissexto.py) | Diz se o ano é bissexto | `and`, `or` |
| 033 | [desafio033_maior_e_menor.py](desafio033_maior_e_menor.py) | Maior e menor de três números (dois jeitos) | condições aninhadas |
| 034 | [desafio034_aumento_por_faixa_salarial.py](desafio034_aumento_por_faixa_salarial.py) | Aumento de 10% ou 15%, conforme o salário | faixas de valor |
| 035 | [desafio035_formando_triangulo.py](desafio035_formando_triangulo.py) | Diz se três retas formam um triângulo | `and` com três condições |

---

## Anotações

### `if` e `else`

O `if` executa um bloco **só se** a condição for verdadeira. O `else` executa o outro bloco, quando ela é falsa:

```python
if Numero % 2 == 0:
    print("Numero par")       # roda só se a condição for verdadeira
else:
    print("Numero impar")     # roda só se for falsa
```

Três regras de escrita:
- a linha do `if` e a do `else` terminam com **dois-pontos** (`:`);
- o que está "dentro" de cada um fica **recuado 4 espaços** (indentação). É o recuo que diz ao Python onde o bloco começa e termina;
- o `else` é opcional. Sem ele, quando a condição é falsa, o programa simplesmente segue em frente.

### Operadores de comparação

| Operador | Significa | Exemplo |
|---|---|---|
| `==` | igual a | `Numero == ChuteJogador` |
| `!=` | diferente de | `Ano % 100 != 0` |
| `>` | maior que | `Velocidade > 80` |
| `<` | menor que | `n1 < n2 + n3` |
| `>=` | maior ou igual a | `n1 >= n2` |
| `<=` | menor ou igual a | `Kms <= 200` |

> Não confunda `=` (**guarda** um valor numa variável) com `==` (**compara** dois valores).

### Operadores lógicos

Servem para juntar condições:

| Operador | Resultado | Exemplo |
|---|---|---|
| `and` | verdadeiro só se **todas** forem verdadeiras | `n1 >= n2 and n1 >= n3` |
| `or` | verdadeiro se **pelo menos uma** for verdadeira | `... or Ano % 400 == 0` |
| `not` | inverte: verdadeiro vira falso e vice-versa | `not (Velocidade > 80)` |

| A | B | `A and B` | `A or B` |
|---|---|---|---|
| True | True | True | True |
| True | False | False | True |
| False | True | False | True |
| False | False | False | False |

> **Ordem:** o Python resolve primeiro o `not`, depois o `and` e por último o `or`. É por isso que a regra do ano bissexto (032) funciona sem parênteses. Mesmo assim, os parênteses deixam a leitura mais fácil:
>
> ```python
> (Ano % 4 == 0 and Ano % 100 != 0) or Ano % 400 == 0
> ```

### Condições aninhadas

Um `if` pode ficar **dentro** de outro. O de dentro só é testado se o de fora for verdadeiro. É o "jeito longo" do desafio 033:

```python
if n1 >= n2 and n1 >= n3:      # n1 é o maior...
    if n2 > n3:                # ...e quem é o menor?
        print("menor é n3")
    else:
        print("menor é n2")
```

> No Mundo 2 aparece o `elif` ("senão, se"), que evita boa parte desse aninhamento.

### Achando o maior e o menor

O jeito mais seguro é começar supondo que o primeiro número é o maior (ou o menor) e comparar cada um dos outros **com o que você já tem**:

```python
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
```

Comparar cada número com **todos** os outros, como no "jeito curto" original do desafio 033, falha quando há números iguais. Veja em [Correções e dicas](#correções-e-dicas).

### Regras que viraram condições

| Regra | Condição em Python | Desafio |
|---|---|---|
| número par | `n % 2 == 0` | 030 |
| ano bissexto | `(ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0` | 032 |
| três retas formam triângulo | `a < b + c and b < a + c and c < a + b` | 035 |
| passou do limite | `velocidade > 80` | 029 |
| faixa de valor | `salario <= 1250` (senão, é maior) | 031 e 034 |

### Sorteando um número

O desafio 028 usa o `randint` do módulo `random`, que sorteia um inteiro **incluindo os dois extremos**:

```python
import random

numero = random.randint(0, 5)    # pode sair 0, 1, 2, 3, 4 ou 5
```

### Evite repetir código no `if`/`else`

Quando os dois caminhos terminam com a mesma linha, ela pode ficar uma vez só, depois do `if`/`else`. Assim, dentro dele fica só o que realmente muda:

```python
if Kms <= 200:
    Preco = Kms * 0.50
else:
    Preco = Kms * 0.45
print("A viagem custa R$ {}".format(Preco))    # vale para os dois casos
```

---

## Correções e dicas

| Desafio | O que mudou |
|---|---|
| 033 | **Correção:** o "jeito curto" errava quando o 2º e o 3º números eram iguais. Com 5, 3, 3 dizia que o menor era 5, e com 1, 5, 5 dizia que o maior era 1. Testando as 27 combinações de 1 a 3, eram 6 erradas. Agora cada número é comparado com o menor ou maior encontrado até ali, e as 27 dão certo. O jeito longo já estava correto |
| 033 | **Correção:** removida uma linha `maior = n1` que tinha sobrado no fim do arquivo |
| 029 | Dica: depois da conta, a variável `Velocidade` passava a guardar o excesso. Uma variável nova (`excesso`) seria mais clara. A multa ganhou o "R$" na mensagem |
| 031 e 034 | Dica: o `print` repetido no `if` e no `else` pode ficar uma vez só, depois |
| 032 | Dica: parênteses deixam a regra do bissexto mais fácil de ler |
