# Curso de Python 3 · Gustavo Guanabara

Meus exercícios e anotações do curso de **Python 3** do [Curso em Vídeo](https://www.cursoemvideo.com), com o professor **Gustavo Guanabara**.

[← Voltar ao python-lab](../README.md)

## Sobre o curso

É um curso gratuito, que começa do zero e vai até tópicos intermediários. Ele é dividido em três **Mundos**, e cada Mundo tem aulas teóricas seguidas de **desafios** práticos, numerados de 001 a 115.

| Mundo | Tema | Desafios | Status |
|---|---|---|---|
| [Mundo 1](mundo-1/) | Fundamentos | 001 a 035 | ✅ Concluído |
| Mundo 2 | Estruturas de controle | 036 a 071 | ⬜ A fazer |
| Mundo 3 | Estruturas compostas | 072 a 115 | ⬜ A fazer |

**Progresso total:** 35 de 115 desafios.

## O que aprendi no Mundo 1

### Primeiros passos
- Mostrar mensagens na tela com `print()` e ler o que o usuário digita com `input()`.
- Guardar valores em **variáveis** e montar textos com `.format()`.

### Tratando dados e fazendo contas
- Os **tipos primitivos** (`int`, `float`, `str`, `bool`) e como descobrir o tipo com `type()`.
- Que o `input()` sempre devolve **texto**, e por isso é preciso converter com `int()` ou `float()` antes de fazer contas.
- Os **operadores aritméticos**, incluindo potência (`**`), divisão inteira (`//`) e resto (`%`), e a **ordem de precedência**.
- Calcular **porcentagens** (descontos e aumentos) e **formatar números** com `{:.2f}`.

### Usando módulos
- Carregar código pronto com `import` e `from ... import`.
- O módulo `math` (raiz, hipotenusa, seno, cosseno, tangente) e o `random` (sortear e embaralhar).
- Instalar **bibliotecas externas** com o `pip` e usar o `pygame` para tocar um MP3.
- Escrever textos com **f-string**.

### Manipulando texto
- Acessar letras pelo **índice** e recortar pedaços com **fatiamento** (`[:5]`).
- Medir, procurar, contar, trocar e separar textos: `len()`, `.find()`, `.count()`, `.replace()`, `.split()`, `in`.
- Padronizar textos com `.upper()`, `.lower()` e `.strip()` antes de comparar.

### Condições
- Fazer o programa **decidir** com `if` e `else`.
- Comparar valores (`==`, `!=`, `>`, `<`...) e juntar condições com `and` e `or`.
- Colocar um `if` dentro de outro (**condições aninhadas**).
- Transformar regras do mundo real em condições: par ou ímpar, ano bissexto, triângulo, multa de trânsito.

### Cores no terminal
- Colorir textos com os **códigos ANSI** (`\033[...m`).

### O que os erros me ensinaram

Revisando os desafios, apareceram alguns erros que valem como lição:

| Lição | Desafio |
|---|---|
| Nunca dar a uma variável o nome de uma função (`cos = cos(...)` "apaga" a função `cos`) | [018](mundo-1/03-usando-modulos/desafio018_seno_cosseno_tangente.py) |
| Testar o programa com **valores repetidos**: o "jeito curto" do maior e menor falhava com 5, 3, 3 | [033](mundo-1/05-condicoes/desafio033_maior_e_menor.py) |
| Abrir arquivos pelo caminho do `.py`, e não pelo nome solto, para o programa rodar de qualquer pasta | [021](mundo-1/03-usando-modulos/desafio021_tocando_mp3.py) |
| Usar `.strip()` no `input()`, porque espaços digitados sem querer mudam o resultado | [024](mundo-1/04-manipulando-texto/desafio024_comeca_com_santo.py) |

## Como esta pasta está organizada

```
gustavo-guanabara/
├── README.md                              ← você está aqui
└── mundo-1/
    ├── README.md                          ← seções, progresso e índice de sintaxe
    ├── 01-primeiros-passos/               desafios 001 e 002
    ├── 02-tratando-dados-e-fazendo-contas/ desafios 003 a 015
    ├── 03-usando-modulos/                 desafios 016 a 021 (+ mikolash.mp3)
    ├── 04-manipulando-texto/              desafios 022 a 027
    ├── 05-condicoes/                      desafios 028 a 035
    └── 06-cores-no-terminal/              anotações da aula de cores
```

- Cada **seção** tem um README com as anotações organizadas por assunto e uma tabela de correções e dicas.
- Cada **desafio** tem um cabeçalho com o enunciado e os conceitos, seguido da minha solução.
- Para procurar uma sintaxe, use o [índice de sintaxe do Mundo 1](mundo-1/README.md#índice-de-sintaxe).

## Ambiente

- **Python 3.14**
- **PyCharm**, com um ambiente virtual (`.venv`) no projeto
- **pygame**, só para o desafio 021: `pip install pygame`

As pastas `.idea` e `.venv`, criadas pelo PyCharm, não entram no repositório. Elas só guardam configurações do editor e bibliotecas instaladas, e qualquer um recria com um `pip install`.

## Próximos passos

O **Mundo 2** traz as estruturas de controle: `elif`, os laços `for` e `while` e o `break`. Com eles, desafios como a tabuada (009), que precisou de 10 linhas de `print`, passam a caber em duas.
