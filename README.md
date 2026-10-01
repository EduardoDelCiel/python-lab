# python-lab

Meu laboratório de Python: todos os meus estudos, exercícios e projetos reunidos num único lugar. Cada assunto fica na sua própria pasta, com os exercícios comentados e um README que explica, como numa aula, cada sintaxe nova que aparece ali.

## Módulos

| Módulo | Assunto | O que tem lá |
|---|---|---|
| [01-for-e-while](01-for-e-while/) | Laços de repetição | 10 exercícios: `for`, `while`, `range()`, `break`, `continue`, listas e dicionários |
| [02-funcoes](02-funcoes/) | Funções | Projeto *Sabor Express* (app de restaurantes): `def`, parâmetros, `import`, `elif`, `try`/`except` |
| [03-regex](03-regex/) | Strings e Regex | 10 exercícios: métodos de string, fatiamento e expressões regulares (`re.findall`, `re.sub`, `re.fullmatch`, `re.search`) |
| [gustavo-guanabara](gustavo-guanabara/) | Curso em Vídeo (Python 3) | Exercícios e anotações do curso do Gustavo Guanabara. Mundo 1 concluído: 35 desafios |

```
python-lab/
├── README.md              ← você está aqui (índice geral)
├── 01-for-e-while/
│   ├── README.md          ← teoria do módulo + lista de exercícios
│   └── ex01_...py … ex10_...py
├── 02-funcoes/
│   ├── README.md          ← teoria + mapa das funções do projeto
│   └── sabor_express.py
├── 03-regex/
│   ├── README.md          ← teoria de strings e regex + cola rápida
│   └── ex01_...py … ex10_...py
└── gustavo-guanabara/
    ├── README.md          ← sobre o curso e o que aprendi
    └── mundo-1/           ← 6 seções, 35 desafios + índice de sintaxe próprio
```

## Como estudar por aqui

1. **Procurando uma sintaxe?** Use o [Índice de sintaxe](#índice-de-sintaxe) abaixo (ou `Ctrl + F` nesta página) e clique no link da explicação.
2. **Tem um problema e não sabe qual ferramenta usar?** Veja a tabela [Eu quero...](#eu-quero).
3. **Cada pasta tem o seu README**, com a lista de exercícios primeiro e depois a teoria separada por categoria.
4. **Cada sintaxe é explicada uma vez só**, na pasta onde aparece pela primeira vez. As pastas seguintes apontam para a explicação original. A exceção é a pasta [gustavo-guanabara](gustavo-guanabara/), que é independente: ela tem as próprias explicações e o [próprio índice de sintaxe](gustavo-guanabara/mundo-1/README.md#índice-de-sintaxe).
5. **Nos arquivos `.py`**, o cabeçalho diz o objetivo e os conceitos do exercício. Os comentários `# CORREÇÃO` e `# MELHORIA` mostram o que foi ajustado em relação ao código original.

### Rodando um exercício

```bash
python3 01-for-e-while/ex01_lista_de_clientes.py
```

No Windows, use `python` em vez de `python3`.

---

## Índice de sintaxe

### 01 · for e while

| Sintaxe | Para que serve | Explicação |
|---|---|---|
| `for item in sequencia:` | percorrer uma sequência item por item | [for](01-for-e-while/README.md#for) |
| `while condicao:` | repetir enquanto a condição for verdadeira | [while](01-for-e-while/README.md#while) |
| `while True:` | laço sem fim, que só termina com `break` | [while True](01-for-e-while/README.md#while-true) |
| `range(inicio, fim, passo)` | gerar uma sequência de números | [range()](01-for-e-while/README.md#range) |
| `break` | sair do laço na hora | [break](01-for-e-while/README.md#break) |
| `continue` | pular para a próxima volta do laço | [continue](01-for-e-while/README.md#continue) |
| `if` / `else` | escolher entre dois caminhos | [if e else](01-for-e-while/README.md#if-e-else) |
| `==` `!=` `<` `>` `<=` `>=` | comparar valores | [Operadores de comparação](01-for-e-while/README.md#operadores-de-comparação) |
| `None` / `is None` | representar e testar a ausência de valor | [None](01-for-e-while/README.md#none) |
| `True` / `False` | valores lógicos | [Booleanos](01-for-e-while/README.md#booleanos) |
| `+=` `-=` `*=` `/=` | atualizar uma variável a partir dela mesma | [Atribuição composta](01-for-e-while/README.md#atribuição-composta) |
| `%` | resto da divisão (par ou ímpar) | [Resto da divisão](01-for-e-while/README.md#resto-da-divisão) |
| `[a, b, c]` | lista | [Listas](01-for-e-while/README.md#listas) |
| `{"chave": valor}` | dicionário | [Dicionários](01-for-e-while/README.md#dicionários) |
| `print()` | mostrar algo na tela | [print()](01-for-e-while/README.md#print) |
| `f"texto {variavel}"` | colocar variáveis dentro de um texto | [f-string](01-for-e-while/README.md#f-string) |
| `input()` | ler o que o usuário digita | [input()](01-for-e-while/README.md#input) |
| `len()` | tamanho de uma string ou lista | [len()](01-for-e-while/README.md#len) |
| `#` e `"""..."""` | comentários e documentação | [Comentários](01-for-e-while/README.md#comentários) |
| recuo de 4 espaços | definir os blocos de código | [Indentação](01-for-e-while/README.md#indentação) |
| `snake_case` | convenção de nomes | [Variáveis e nomes](01-for-e-while/README.md#variáveis-e-nomes) |
| contador / acumulador | padrões de laço | [Contador](01-for-e-while/README.md#contador) · [Acumulador](01-for-e-while/README.md#acumulador) |

### 02 · Funções

| Sintaxe | Para que serve | Explicação |
|---|---|---|
| `def nome():` | criar uma função | [def](02-funcoes/README.md#def) |
| `def nome(parametro):` | função que recebe valores | [Parâmetros e argumentos](02-funcoes/README.md#parâmetros-e-argumentos) |
| `"""texto"""` na 1ª linha da função | documentar a função | [Docstring](02-funcoes/README.md#docstring) |
| `return valor` | devolver um resultado | [return](02-funcoes/README.md#return) |
| função que chama a si mesma | recursão | [Recursão](02-funcoes/README.md#recursão) |
| variável fora das funções | variável global × local | [Variáveis globais](02-funcoes/README.md#variáveis-globais) |
| `if __name__ == '__main__':` | só rodar quando o arquivo é executado | [if \_\_name\_\_](02-funcoes/README.md#if-__name__--__main__) |
| `import modulo` | usar código pronto de um módulo | [import](02-funcoes/README.md#import) |
| `os.system()` / `os.name` | comandos do sistema, limpar a tela | [Módulo os](02-funcoes/README.md#módulo-os) |
| `elif` | testar mais de duas opções | [elif](02-funcoes/README.md#elif) |
| `A if condicao else B` | if/else em uma linha (ternário) | [Operador ternário](02-funcoes/README.md#operador-ternário) |
| `not` | inverter verdadeiro/falso | [not](02-funcoes/README.md#not) |
| `encontrado = False` … `= True` | lembrar se algo aconteceu no laço | [Variável bandeira](02-funcoes/README.md#variável-bandeira) |
| `int()` / `float()` / `str()` | converter tipos | [int()](02-funcoes/README.md#int) |
| `try:` / `except ValueError:` | tratar erros sem quebrar o programa | [try e except](02-funcoes/README.md#try-e-except) |
| `"""várias linhas"""` | string de várias linhas | [Aspas triplas](02-funcoes/README.md#aspas-triplas) |
| `\n` | quebra de linha | [Quebra de linha](02-funcoes/README.md#quebra-de-linha) |
| `'*' * 10` | repetir um texto | [Repetir texto](02-funcoes/README.md#repetir-texto) |
| `.ljust(n)` | alinhar texto em colunas | [ljust()](02-funcoes/README.md#ljust) |
| `lista.append(item)` | adicionar no fim da lista | [append()](02-funcoes/README.md#append) |
| `dicionario['chave'] = valor` | alterar um valor do dicionário | [Alterar um valor no dicionário](02-funcoes/README.md#alterar-um-valor-no-dicionário) |

### 03 · Strings e Regex

| Sintaxe | Para que serve | Explicação |
|---|---|---|
| `texto.metodo()` | chamar um método | [O que é um método](03-regex/README.md#o-que-é-um-método) |
| `.lower()` / `.upper()` / `.title()` | mudar maiúsculas e minúsculas | [lower() e upper()](03-regex/README.md#lower-e-upper) |
| `.startswith()` / `.endswith()` | conferir como um texto começa ou termina | [startswith() e endswith()](03-regex/README.md#startswith-e-endswith) |
| `.isupper()` `.isdigit()` `.isalpha()` `.isalnum()` | perguntar o tipo de caractere | [Métodos de verificação](03-regex/README.md#métodos-de-verificação) |
| `texto[0]` / `texto[-1]` | pegar um caractere pela posição | [Índices](03-regex/README.md#índices) |
| `texto[inicio:fim]` | pegar um pedaço do texto | [Fatiamento](03-regex/README.md#fatiamento) |
| `and` / `or` | juntar condições | [and](03-regex/README.md#and) |
| `all(... for ... in ...)` | testar se todos os itens atendem uma condição | [all()](03-regex/README.md#all) |
| `if lista:` / `if resultado:` | testar se algo está vazio | [Valores verdadeiros e falsos](03-regex/README.md#valores-verdadeiros-e-falsos) |
| `import re` | usar expressões regulares | [import re](03-regex/README.md#import-re) |
| `r'...'` / `rf'...'` | raw string para padrões de regex | [Raw string](03-regex/README.md#raw-string) |
| `re.findall()` | achar todas as ocorrências (lista) | [re.findall()](03-regex/README.md#refindall) |
| `re.sub()` | substituir ocorrências | [re.sub()](03-regex/README.md#resub) |
| `re.match()` / `re.fullmatch()` | validar o começo / o texto inteiro | [re.match() e re.fullmatch()](03-regex/README.md#rematch-e-refullmatch) |
| `re.search()` | achar a primeira ocorrência em qualquer lugar | [re.search()](03-regex/README.md#research) |
| `.group(n)` | pegar o que um grupo capturou | [Objeto Match](03-regex/README.md#objeto-match) |
| `re.IGNORECASE` | ignorar maiúsculas e minúsculas | [re.IGNORECASE](03-regex/README.md#reignorecase) |
| `re.escape()` | usar texto do usuário dentro de um padrão | [re.escape()](03-regex/README.md#reescape) |
| `\d` `\w` `\s` `.` | dígito, letra, espaço, qualquer caractere | [Dígitos e letras](03-regex/README.md#dígitos-e-letras) |
| `[A-Z]` `[a-zà-ÿ]` `[^0-9]` | um caractere de um conjunto ou faixa | [Colchetes](03-regex/README.md#colchetes) |
| `+` `*` `?` `{n}` `{n,m}` | quantas vezes algo se repete | [Quantificadores](03-regex/README.md#quantificadores) |
| `\b` | borda de palavra (palavra inteira) | [Borda de palavra](03-regex/README.md#borda-de-palavra) |
| `\.` `\(` | procurar um símbolo especial literalmente | [Escapando caracteres especiais](03-regex/README.md#escapando-caracteres-especiais) |
| `( )` | capturar partes do texto | [Grupos](03-regex/README.md#grupos) |

Todos os símbolos de regex numa tabela só: [Cola rápida de regex](03-regex/README.md#cola-rápida-de-regex).

---

## Eu quero...

| Eu quero... | Use | Exemplo |
|---|---|---|
| passar por todos os itens de uma lista | `for item in lista:` | [01/ex01](01-for-e-while/ex01_lista_de_clientes.py) |
| repetir algo N vezes | `for _ in range(N):` | [01/ex03](01-for-e-while/ex03_mensagem_repetida.py) |
| fazer uma contagem regressiva | `range(10, 0, -1)` | [01/ex08](01-for-e-while/ex08_contagem_regressiva.py) |
| repetir enquanto algo for verdade | `while condicao:` | [01/ex07](01-for-e-while/ex07_controle_de_estoque.py) |
| pedir um dado até o usuário digitar certo | `while True:` + `continue` / `break` | [01/ex10](01-for-e-while/ex10_cadastro_de_usuario.py) |
| parar o laço quando encontrar o que procuro | `break` | [01/ex06](01-for-e-while/ex06_busca_de_livro.py) |
| ignorar alguns itens do laço | `continue` | [01/ex09](01-for-e-while/ex09_livros_disponiveis.py) |
| somar os valores de uma lista | acumulador (ou `sum()`) | [01/ex04](01-for-e-while/ex04_soma_de_receitas.py) |
| saber se um número é par | `n % 2 == 0` | [01/ex08](01-for-e-while/ex08_contagem_regressiva.py) |
| guardar vários dados de uma coisa só | dicionário | [01/ex09](01-for-e-while/ex09_livros_disponiveis.py) |
| checar se um valor está vazio (`None`) | `is None` | [01/ex05](01-for-e-while/ex05_projetos_ausentes.py) |
| saber o tamanho de um texto | `len()` | [01/ex10](01-for-e-while/ex10_cadastro_de_usuario.py) |
| reaproveitar um pedaço de código | `def` (função) | [02/sabor_express](02-funcoes/sabor_express.py) |
| escolher entre 3 ou mais opções | `if` / `elif` / `else` | [02/sabor_express](02-funcoes/sabor_express.py) |
| transformar o que o usuário digitou em número | `int(input(...))` | [02/sabor_express](02-funcoes/sabor_express.py) |
| evitar que o programa quebre com entrada errada | `try` / `except ValueError` | [02/sabor_express](02-funcoes/sabor_express.py) |
| escolher entre dois valores numa linha só | `A if condicao else B` | [02/sabor_express](02-funcoes/sabor_express.py) |
| ligar/desligar um valor `True`/`False` | `x = not x` | [02/sabor_express](02-funcoes/sabor_express.py) |
| adicionar um item a uma lista | `.append()` | [02/sabor_express](02-funcoes/sabor_express.py) |
| alinhar textos em colunas | `.ljust(n)` | [02/sabor_express](02-funcoes/sabor_express.py) |
| limpar a tela do terminal | `os.system('cls' / 'clear')` | [02/sabor_express](02-funcoes/sabor_express.py) |
| fazer um menu que se repete | `while True` + `break` | [02/README](02-funcoes/README.md#para-ir-além-menu-com-while) |
| deixar um texto todo em minúsculas | `.lower()` | [03/ex01](03-regex/ex01_nome_do_produto.py) |
| pegar os primeiros ou os últimos caracteres | `texto[:3]` / `texto[-3:]` | [03/ex03](03-regex/ex03_partes_da_senha.py) |
| conferir se um texto começa/termina com algo | `.startswith()` / `.endswith()` | [03/ex04](03-regex/ex04_validar_url.py) |
| exigir duas condições ao mesmo tempo | `and` | [03/ex04](03-regex/ex04_validar_url.py) |
| achar números dentro de um texto | `re.findall(r'\d+', texto)` | [03/ex05](03-regex/ex05_numero_da_receita.py) |
| trocar uma palavra inteira por outra | `re.sub(rf'\b{palavra}\b', nova, texto)` | [03/ex06](03-regex/ex06_substituir_palavra.py) |
| validar se um nome só tem letras | `.isalpha()` ou `re.fullmatch()` | [03/ex07](03-regex/ex07_validar_nome.py) |
| validar um formato (CPF, CEP, telefone...) | `re.fullmatch()` | [03/ex08](03-regex/ex08_validar_cpf.py) |
| buscar sem diferenciar maiúsculas | `re.IGNORECASE` | [03/ex09](03-regex/ex09_palavras_por_letra.py) |
| separar partes de um texto (nome, ano...) | `re.search()` + grupos `( )` | [03/ex10](03-regex/ex10_nome_e_ano.py) |

---

## De onde veio o conteúdo

Este repositório junta o que antes estava espalhado em repositórios separados:

| Repositório original | Virou |
|---|---|
| [Python.For-and-While](https://github.com/EduardoDelCiel/Python.For-and-While) | [01-for-e-while](01-for-e-while/) |
| [funcoes.pyt](https://github.com/EduardoDelCiel/funcoes.pyt) | [02-funcoes](02-funcoes/) |
| [Regex.Python](https://github.com/EduardoDelCiel/Regex.Python) | [03-regex](03-regex/) |

## Licença

[MIT](LICENSE)
