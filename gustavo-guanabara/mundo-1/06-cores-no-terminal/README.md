# Cores no terminal

**Mundo 1 · Aula sem desafios**

Como colorir textos no terminal usando os códigos ANSI.

[← Voltar ao Mundo 1](../README.md)

## Arquivo

| Arquivo | O que tem |
|---|---|
| [cores_no_terminal.py](cores_no_terminal.py) | As anotações da aula e exemplos coloridos para rodar |

---

## Anotações

### O formato do código

```
\033[estilo;cor_do_texto;cor_do_fundo m
```

| Parte | O que é |
|---|---|
| `\033[` | abre o código de cor |
| `estilo;texto;fundo` | os números, separados por ponto e vírgula, em qualquer ordem |
| `m` | fecha o código |
| `\033[m` | **desliga tudo** e volta ao normal |

> Sempre termine com `\033[m`. Senão, tudo o que vier depois continua colorido.

### Estilo

| Código | Estilo |
|---|---|
| `0` | normal |
| `1` | negrito |
| `4` | sublinhado |
| `7` | inverte as cores do texto e do fundo |

### Cores

A cor de fundo é sempre a cor do texto **+ 10**:

| Cor | Texto | Fundo |
|---|---|---|
| preto | `30` | `40` |
| vermelho | `31` | `41` |
| verde | `32` | `42` |
| amarelo | `33` | `43` |
| azul | `34` | `44` |
| magenta | `35` | `45` |
| ciano | `36` | `46` |
| branco | `37` | `47` |

### Exemplos

```python
print("\033[31mTexto vermelho\033[m")
print("\033[41mFundo vermelho\033[m")
print("\033[1;33;44mNegrito, amarelo, fundo azul\033[m")
```

Com f-string, a variável vai no meio:

```python
nome = "Eduardo"
print(f"\033[32m{nome}\033[m")      # nome em verde
```

### Guardando as cores em variáveis

Os códigos são difíceis de ler no meio do texto. Dando um nome para cada um, o `print` fica bem mais claro:

```python
vermelho = "\033[31m"
verde = "\033[32m"
fim = "\033[m"

print(f"{verde}Tudo certo!{fim}")
print(f"{vermelho}Deu erro!{fim}")
```

> O console do PyCharm mostra as cores normalmente. Se algum terminal mostrar códigos estranhos, como `←[31m`, em vez das cores, é porque ele não entende os códigos ANSI.

---

## Correções e dicas

| Arquivo | O que mudou |
|---|---|
| `Cores.py` → `cores_no_terminal.py` | Nome do arquivo em minúsculas, como os outros. As anotações foram mantidas como estavam. Dica nova: guardar os códigos em variáveis |
