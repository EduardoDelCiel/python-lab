# 02 · Funções: projeto Sabor Express

No módulo 01 eram vários exercícios curtos. Aqui é **um programa completo**: o *Sabor Express*, um app de terminal para cadastrar e gerenciar restaurantes. O app inteiro é montado com **funções**, e cada tarefa tem a sua.

[← Voltar ao índice geral](../README.md)

## Sumário

- [O projeto](#o-projeto)
  - [Como rodar](#como-rodar)
  - [Mapa das funções](#mapa-das-funções)
- [Conceitos](#conceitos)
  - **Funções:** [def](#def) · [Parâmetros e argumentos](#parâmetros-e-argumentos) · [Docstring](#docstring) · [return](#return) · [Funções chamando funções](#funções-chamando-funções) · [Recursão](#recursão) · [Variáveis globais](#variáveis-globais) · [if name main](#if-__name__--__main__)
  - **Módulos:** [import](#import) · [Módulo os](#módulo-os)
  - **Decisões:** [elif](#elif) · [Operador ternário](#operador-ternário) · [not](#not) · [Variável bandeira](#variável-bandeira)
  - **Tratamento de erros:** [int()](#int) · [try e except](#try-e-except)
  - **Strings:** [Aspas triplas](#aspas-triplas) · [Quebra de linha](#quebra-de-linha) · [Repetir texto](#repetir-texto) · [ljust()](#ljust)
  - **Listas e dicionários:** [append()](#append) · [Alterar um valor no dicionário](#alterar-um-valor-no-dicionário)
- [Revisão: o que veio do módulo 01](#revisão-o-que-veio-do-módulo-01)
- [Para ir além: menu com while](#para-ir-além-menu-com-while)
- [Erros corrigidos](#erros-corrigidos)

---

## O projeto

| Arquivo | O que é |
|---|---|
| [sabor_express.py](sabor_express.py) | O app completo, dividido em seções: **dados**, **funções de tela**, **funções de navegação**, **funções de ação** e **menu** |

O menu tem 4 opções:

```
1. Cadastrar restaurante
2. Listar restaurantes
3. Alternar estado do restaurante
4. Sair
```

### Como rodar

```bash
python3 02-funcoes/sabor_express.py
```

### Mapa das funções

Quem chama quem:

```
main()
 ├─ limpar_tela()
 ├─ exibir_nome_do_programa()
 ├─ exibir_opcoes()
 └─ escolher_opcao()
      ├─ 1 → cadastrar_novo_restaurante()  ─┐
      ├─ 2 → listar_restaurantes()          ├─→ voltar_ao_menu_principal() ─→ main()  (de novo)
      ├─ 3 → alternar_estado_restaurante() ─┘
      ├─ 4 → finalizar_app()                    (não volta ao menu → fim do programa)
      └─ outra coisa → opcao_invalida() ───────→ voltar_ao_menu_principal() ─→ main()
```

| Seção | Função | O que faz |
|---|---|---|
| Tela | `limpar_tela()` | limpa o terminal (Windows, Linux ou macOS) |
| Tela | `exibir_nome_do_programa()` | mostra o título em ASCII art |
| Tela | `exibir_opcoes()` | mostra o menu |
| Tela | `exibir_subtitulo(texto)` | limpa a tela e mostra um título emoldurado com `*` |
| Navegação | `voltar_ao_menu_principal()` | espera o Enter e chama `main()` |
| Navegação | `opcao_invalida()` | avisa que a opção não existe |
| Navegação | `finalizar_app()` | mensagem de despedida |
| Ação | `cadastrar_novo_restaurante()` | opção 1 |
| Ação | `listar_restaurantes()` | opção 2 |
| Ação | `alternar_estado_restaurante()` | opção 3 |
| Menu | `escolher_opcao()` | lê a opção e chama a função certa |
| Menu | `main()` | ponto de partida do app |

---

## Conceitos

### Funções

#### `def`

Uma **função** é um bloco de código com nome, que você escreve uma vez e **reutiliza** quantas vezes quiser. Ela é criada com `def`:

```python
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
```

Criar a função **não executa** o código dela. Ele só roda quando a função é **chamada**, pelo nome e com parênteses:

```python
exibir_opcoes()      # agora sim, imprime as opções
```

> Por que usar funções? Porque elas dão **nome** a um pedaço do programa (`listar_restaurantes()` é autoexplicativo), **evitam repetição** e deixam cada parte **fácil de achar e de corrigir**.

#### Parâmetros e argumentos

Uma função pode receber valores de fora. Na definição, eles se chamam **parâmetros**. Na chamada, os valores enviados se chamam **argumentos**.

```python
def exibir_subtitulo(texto):          # `texto` é o parâmetro
    print(texto)

exibir_subtitulo('Finalizar app')     # 'Finalizar app' é o argumento
exibir_subtitulo('Listando restaurantes')
```

Com um parâmetro, a mesma função serve para vários títulos diferentes.

**No projeto:** `exibir_subtitulo(texto)`

#### Docstring

É um texto entre `"""` logo na primeira linha da função. Ele documenta o que a função faz, e editores como o VS Code mostram esse texto quando você passa o mouse sobre a função.

```python
def limpar_tela():
    """Limpa o terminal em qualquer sistema operacional."""
```

**No projeto:** todas as funções têm uma.

#### `return`

> O `return` não aparece no Sabor Express, mas é essencial em funções, então vale conhecer desde já.

Todas as funções do projeto **fazem algo** (imprimem, alteram a lista). Uma função também pode **devolver um valor** para quem a chamou, usando `return`:

```python
def dobro(numero):
    return numero * 2

resultado = dobro(5)      # resultado = 10
```

| Função que **imprime** | Função que **retorna** |
|---|---|
| mostra o valor na tela e acabou | entrega o valor para você guardar e usar depois |
| `print(x)` dentro dela | `return x` dentro dela |

> Uma função sem `return` devolve [`None`](../01-for-e-while/README.md#none).

#### Funções chamando funções

Uma função pode chamar outras. O `main()`, por exemplo, só organiza o trabalho e deixa o resto para outras funções:

```python
def main():
    limpar_tela()
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
```

> A ordem em que as funções são **definidas** no arquivo não importa. O que importa é que todas já existam no momento em que forem **chamadas**. Por isso `main()` só é chamado na última linha do arquivo.

#### Recursão

Quando uma função acaba chamando **a si mesma** (direta ou indiretamente), temos **recursão**. No projeto é isso que faz o menu reaparecer:

```
main() → escolher_opcao() → listar_restaurantes() → voltar_ao_menu_principal() → main() → ...
```

Funciona bem para um app pequeno, mas tem um custo. Cada volta ao menu abre chamadas novas **sem fechar as anteriores**. São 4 chamadas por volta, e o limite padrão do Python é 1000, então depois de umas **250 voltas ao menu** o programa quebra com `RecursionError`. Dá para testar! A forma mais comum de fazer menus é com um laço `while`. Veja [Para ir além](#para-ir-além-menu-com-while).

#### Variáveis globais

A lista `restaurantes` foi criada **fora** de qualquer função, no topo do arquivo. Por isso ela é *global*, e todas as funções conseguem ler e alterar o conteúdo dela:

```python
restaurantes = [...]                       # global

def cadastrar_novo_restaurante():
    restaurantes.append(dados_do_restaurante)   # usa a lista global
```

Já as variáveis criadas **dentro** de uma função, como `linha` em `exibir_subtitulo`, são *locais*: só existem enquanto a função está rodando.

#### `if __name__ == '__main__'`

```python
if __name__ == '__main__':
    main()
```

Todo arquivo Python tem uma variável automática chamada `__name__`:

- se você **executa** o arquivo (`python3 sabor_express.py`), ela vale `'__main__'`;
- se outro arquivo **importa** este (`import sabor_express`), ela vale `'sabor_express'`.

Resultado: o app só inicia quando o arquivo é executado diretamente. Se alguém importar o arquivo só para reaproveitar uma função, o menu não abre sozinho.

---

### Módulos

#### `import`

Um **módulo** é um arquivo com funções prontas. O Python já vem com vários (a *biblioteca padrão*), e o `import` os traz para o seu código:

```python
import os

os.system('clear')     # usa a função system do módulo os
```

Depois do `import`, você acessa o conteúdo do módulo com **`modulo.coisa`**.

#### Módulo `os`

O `os` conversa com o **sistema operacional**.

| Uso | O que faz |
|---|---|
| `os.system('comando')` | executa um comando do terminal |
| `os.name` | `'nt'` no Windows e `'posix'` no Linux/macOS |

O comando que limpa o terminal muda de sistema para sistema (`cls` no Windows, `clear` nos outros). Por isso o projeto usa:

```python
os.system('cls' if os.name == 'nt' else 'clear')
```

---

### Decisões

#### `elif`

O `elif` ("senão, se") testa **mais uma condição** quando a anterior deu falso. Com ele você cria vários caminhos, sem precisar encaixar um `if` dentro do outro:

```python
if opcao_escolhida == 1:
    cadastrar_novo_restaurante()
elif opcao_escolhida == 2:
    listar_restaurantes()
elif opcao_escolhida == 3:
    alternar_estado_restaurante()
else:
    opcao_invalida()          # nenhuma das anteriores
```

> O Python testa de cima para baixo e executa **só o primeiro** bloco verdadeiro. A base (`if`/`else`) está no [módulo 01](../01-for-e-while/README.md#if-e-else).

#### Operador ternário

É um `if`/`else` **em uma linha só**, usado para escolher entre dois valores:

```python
valor = A if condicao else B
```

```python
ativo = 'ativado' if restaurante['ativo'] else 'desativado'
```

É o mesmo que:

```python
if restaurante['ativo']:
    ativo = 'ativado'
else:
    ativo = 'desativado'
```

> Use para escolhas **simples entre dois valores**. Se a lógica for maior, prefira o `if` normal.

#### `not`

O `not` inverte um [booleano](../01-for-e-while/README.md#booleanos): `not True` dá `False`, e `not False` dá `True`.

```python
restaurante['ativo'] = not restaurante['ativo']   # liga ↔ desliga

if not restaurante_encontrado:                    # "se NÃO encontrou"
    print('O restaurante não foi encontrado')
```

#### Variável bandeira

Uma bandeira (*flag*) é uma variável booleana que **começa com um valor** e **muda quando algo acontece**. Depois do laço, ela conta se aquilo aconteceu:

```python
restaurante_encontrado = False          # ainda não achei
for restaurante in restaurantes:
    if nome_restaurante == restaurante['nome']:
        restaurante_encontrado = True   # achei!

if not restaurante_encontrado:
    print('O restaurante não foi encontrado')
```

**No projeto:** `alternar_estado_restaurante()`

---

### Tratamento de erros

#### `int()`

O [`input()`](../01-for-e-while/README.md#input) sempre devolve **texto**. Para comparar com números, é preciso converter com `int()`:

```python
opcao = int(input('Escolha uma opção: '))   # "2" → 2
```

| Conversão | Exemplo |
|---|---|
| `int("2")` | `2` (número inteiro) |
| `float("2.5")` | `2.5` (número com casas decimais) |
| `str(2)` | `"2"` (texto) |

> Se o texto não for um número, como `int("abc")`, o Python gera um erro chamado **`ValueError`**. O `try`/`except` existe justamente para tratar isso.

#### `try` e `except`

Serve para **tentar** executar um código e, **se der erro**, fazer outra coisa em vez de o programa quebrar:

```python
try:
    opcao = int(input('Escolha uma opção: '))   # pode dar erro
    ...
except ValueError:
    opcao_invalida()                            # só roda se deu ValueError
```

> **Sempre diga qual erro você espera** (`except ValueError:`). Um `except:` sozinho captura **qualquer** erro, até o Ctrl+C que o usuário aperta para sair, e ainda esconde bugs de verdade. O código original fazia isso, e foi [corrigido](#erros-corrigidos).

| Erro comum | Quando acontece |
|---|---|
| `ValueError` | valor com formato errado: `int("abc")` |
| `IndexError` | posição que não existe numa lista |
| `KeyError` | chave que não existe num dicionário |
| `NameError` | variável ou função que não existe |

---

### Strings

#### Aspas triplas

Com `"""` (ou `'''`) uma string pode ocupar **várias linhas**. O projeto usa isso para imprimir o título em ASCII art:

```python
print("""
Linha 1
Linha 2
""")
```

#### Quebra de linha

O `\n` dentro de uma string significa **"pule uma linha aqui"**:

```python
print('4. Sair\n')        # imprime e deixa uma linha em branco depois
input('\nPressione Enter para voltar ao menu ')
```

#### Repetir texto

Multiplicar uma string por um número **repete** a string:

```python
'*' * 5                   # '*****'
linha = '*' * len(texto)  # uma linha de * do tamanho exato do texto
```

**No projeto:** `exibir_subtitulo(texto)`

#### `ljust()`

`texto.ljust(n)` completa o texto **com espaços à direita** até ele ter `n` caracteres. É o que deixa as colunas da listagem alinhadas:

```python
'Praça'.ljust(10)         # 'Praça     '
```

```
- Praça                | Japonesa             | desativado
- Pizza Suprema        | Pizza                | ativado
```

> Os irmãos dele: `.rjust(n)` alinha à direita e `.center(n)` centraliza.

---

### Listas e dicionários

#### `append()`

`lista.append(item)` **adiciona um item no fim** da lista:

```python
restaurantes.append({'nome': 'Novo', 'categoria': 'Árabe', 'ativo': False})
```

**No projeto:** `cadastrar_novo_restaurante()`

#### Alterar um valor no dicionário

Você lê um valor com `dicionario['chave']` ([módulo 01](../01-for-e-while/README.md#dicionários)). Para **alterar**, é só atribuir:

```python
restaurante['ativo'] = True
restaurante['ativo'] = not restaurante['ativo']   # inverte o valor atual
```

---

## Revisão: o que veio do módulo 01

Estes itens aparecem no projeto e já foram explicados antes:

| Sintaxe | Onde aparece no projeto | Explicação |
|---|---|---|
| lista de dicionários | `restaurantes` | [Dicionários](../01-for-e-while/README.md#dicionários) |
| `for` | `listar_restaurantes()` e `alternar_estado_restaurante()` | [for](../01-for-e-while/README.md#for) |
| `if` / `else` | várias funções | [if e else](../01-for-e-while/README.md#if-e-else) |
| f-string | quase todos os `print` | [f-string](../01-for-e-while/README.md#f-string) |
| `input()` | leitura de opção, nome e categoria | [input()](../01-for-e-while/README.md#input) |
| `len()` | `exibir_subtitulo()` | [len()](../01-for-e-while/README.md#len) |
| `True` / `False` | chave `'ativo'` | [Booleanos](../01-for-e-while/README.md#booleanos) |

---

## Para ir além: menu com `while`

Como vimos em [Recursão](#recursão), o app volta ao menu chamando `main()` de novo. Uma alternativa comum é usar um laço [`while True`](../01-for-e-while/README.md#while-true) no `main()`. Assim as funções de ação não precisam mais chamar `voltar_ao_menu_principal()`, e a opção 4 só dá um `break`:

```python
def main():
    while True:
        limpar_tela()
        exibir_nome_do_programa()
        exibir_opcoes()
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            cadastrar_novo_restaurante()
        elif opcao == '2':
            listar_restaurantes()
        elif opcao == '3':
            alternar_estado_restaurante()
        elif opcao == '4':
            finalizar_app()
            break                   # sai do laço → o programa termina
        else:
            print('Opção inválida!')

        input('\nPressione Enter para voltar ao menu ')
```

Repare que, comparando com texto (`'1'` em vez de `1`), nem é preciso usar `int()` e `try`/`except`: qualquer coisa diferente de 1 a 4 cai no `else`.

---

## Erros corrigidos

| Onde | Problema | O que foi feito |
|---|---|---|
| `listar_restaurantes()` | chamava `voltar_ao_menu_principal()` **duas vezes** seguidas | removida a chamada repetida |
| `escolher_opcao()` | `except:` sem tipo capturava **qualquer** erro, inclusive o Ctrl+C | `except ValueError:` |
| `os.system('cls')` | só funciona no Windows (e estava repetido em dois lugares) | nova função `limpar_tela()`, que escolhe entre `cls` e `clear` |
| `alternar_estado_restaurante()` | o ternário repetia a frase inteira nos dois lados | o ternário escolhe só a palavra que muda (`ativado`/`desativado`) |
| `finalizar_app()` | indentação de 6 espaços (o padrão é 4) | 4 espaços |
| `voltar_ao_menu_principal()` | a mensagem dizia "Digite uma tecla", mas só o Enter funciona | "Pressione Enter para voltar ao menu" |
| `escolher_opcao()` | linha comentada que tinha sobrado (`# opcao_escolhida = int(...)`) | removida |
| textos | "ALterando" | "Alterando" |
| arquivo | chamava-se `sabor/.pyt`: sem nome e com extensão errada | `sabor_express.py` |
