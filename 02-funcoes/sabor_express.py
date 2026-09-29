"""
Sabor Express — app de restaurantes no terminal
Módulo 02 · Funções

O programa mostra um menu e deixa o usuário:
  1. cadastrar um restaurante
  2. listar os restaurantes
  3. ativar/desativar um restaurante
  4. sair

Conceitos: def, parâmetros, docstring, import os, if/elif/else,
           try/except, int(), operador ternário, not, .append(), .ljust(),
           if __name__ == '__main__'
Teoria: README.md desta pasta (tem até um mapa de quem chama quem).
"""

import os


# =============================================================================
# DADOS
# =============================================================================
# Lista de dicionários: cada restaurante tem nome, categoria e se está ativo.
restaurantes = [
    {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
    {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
    {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False},
]


# =============================================================================
# FUNÇÕES DE TELA: só mostram coisas, não mudam nenhum dado
# =============================================================================
def limpar_tela():
    """Limpa o terminal em qualquer sistema operacional."""
    # MELHORIA: o original chamava os.system('cls') em dois lugares, e 'cls'
    # só existe no Windows. os.name vale 'nt' no Windows; no Linux/macOS o
    # comando equivalente é 'clear'.
    os.system('cls' if os.name == 'nt' else 'clear')


def exibir_nome_do_programa():
    """Mostra o título do app em ASCII art."""
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")


def exibir_opcoes():
    """Mostra as opções do menu principal."""
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')


def exibir_subtitulo(texto):
    """Limpa a tela e mostra `texto` entre duas linhas de asteriscos."""
    limpar_tela()
    linha = '*' * len(texto)    # repete o '*' o mesmo número de vezes que o texto
    print(linha)
    print(texto)
    print(linha)
    print()


# =============================================================================
# FUNÇÕES DE NAVEGAÇÃO: levam o usuário de uma tela para outra
# =============================================================================
def voltar_ao_menu_principal():
    """Espera o Enter e mostra o menu de novo."""
    input('\nPressione Enter para voltar ao menu ')
    main()                      # chama o menu de novo (ver "Recursão" no README)


def opcao_invalida():
    """Avisa que a opção não existe e volta ao menu."""
    print('Opção inválida!\n')
    voltar_ao_menu_principal()


def finalizar_app():
    """Mostra a despedida. Como não chama main(), o programa termina aqui."""
    exibir_subtitulo('Finalizar app')
    print('Encerrando o programa... Até logo!')
    input('\nPressione Enter para sair.')


# =============================================================================
# FUNÇÕES DE AÇÃO: uma para cada opção do menu
# =============================================================================
def cadastrar_novo_restaurante():
    """Opção 1: pede nome e categoria e adiciona um restaurante à lista."""
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')

    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)   # .append() coloca no fim da lista

    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()


def listar_restaurantes():
    """Opção 2: mostra todos os restaurantes em formato de tabela."""
    exibir_subtitulo('Listando restaurantes')

    # .ljust(n) completa o texto com espaços até ele ter n caracteres,
    # deixando as colunas alinhadas
    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'   # ternário
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    # CORREÇÃO: no original, voltar_ao_menu_principal() aparecia duas vezes
    # seguidas aqui.
    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    """Opção 3: ativa um restaurante desativado, e vice-versa."""
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False  # "bandeira": vira True se acharmos o restaurante

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']   # inverte True/False
            # MELHORIA: o ternário original repetia a frase inteira nos dois
            # lados; aqui ele escolhe só a palavra que muda.
            estado = 'ativado' if restaurante['ativo'] else 'desativado'
            print(f'O restaurante {nome_restaurante} foi {estado} com sucesso')

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()


# =============================================================================
# MENU E PONTO DE ENTRADA
# =============================================================================
def escolher_opcao():
    """Lê a opção digitada e chama a função correspondente."""
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))   # texto → número

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    # CORREÇÃO: era um `except:` sem tipo, que captura QUALQUER erro, até o
    # Ctrl+C. Aqui só queremos tratar o caso de o int() receber algo que não é
    # número (ex.: "abc"), e esse erro se chama ValueError.
    except ValueError:
        opcao_invalida()


def main():
    """Tela inicial: título, menu e escolha da opção."""
    limpar_tela()
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


# Só inicia o app se este arquivo for executado diretamente
# (e não quando for importado por outro arquivo).
if __name__ == '__main__':
    main()
