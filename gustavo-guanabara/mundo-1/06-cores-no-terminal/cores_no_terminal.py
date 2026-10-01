"""
Cores no terminal
Mundo 1 · Cores no terminal

Anotações e exemplos da aula (esta aula não tem desafios).
Conceitos: códigos de escape ANSI (\\033[...m)
"""

nome = "Eduardo"

# CORES NO TERMINAL (códigos ANSI)
# Formato: \033[estilo;cor_do_texto;cor_do_fundo m
#   \033[   -> abre o código de cor
#   m       -> fecha o código
#   \033[m  -> desliga tudo e volta ao normal (sempre usar no final,
#              senão as próximas linhas continuam coloridas)
#
# Estilo:   0 = normal | 1 = negrito | 4 = sublinhado | 7 = inverte texto e fundo
#
# Cor do texto:  30 preto | 31 vermelho | 32 verde | 33 amarelo
#                34 azul | 35 magenta | 36 ciano | 37 branco
#
# COR DE FUNDO: é a cor do texto + 10
#   40 preto | 41 vermelho | 42 verde | 43 amarelo
#   44 azul | 45 magenta | 46 ciano | 47 branco
#
# Os valores são separados por ponto e vírgula e a ordem não importa.

print(f"\033[31m{nome}\033[m")           # texto vermelho
print(f"\033[41m{nome}\033[m")           # fundo vermelho
print(f"\033[1;33;44m{nome}\033[m")      # negrito + texto amarelo + fundo azul

# DICA: guardar os códigos em variáveis deixa o print bem mais legível
vermelho = "\033[31m"
verde = "\033[32m"
fim = "\033[m"

print(f"{verde}Tudo certo!{fim} ... {vermelho}Deu erro!{fim}")
