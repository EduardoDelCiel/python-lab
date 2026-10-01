"""
Desafio 021: Tocando um MP3
Mundo 1 · Usando módulos

Enunciado: faça um programa em Python que abra e reproduza o áudio de um
arquivo MP3.
Conceitos: biblioteca externa (pygame), instalação com pip

Antes de rodar, instale o pygame:  pip install pygame
"""

from pathlib import Path

import pygame

# MELHORIA: o original carregava "mikolash.mp3" só pelo nome. Isso funciona
# quando o programa roda de dentro desta pasta, que é o que o PyCharm faz.
# Rodando de outra pasta, dava o erro "No file 'mikolash.mp3' found".
# Path(__file__).parent é a pasta onde este arquivo .py está, então o mp3 é
# encontrado de qualquer lugar.
arquivo = Path(__file__).parent / "mikolash.mp3"

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(str(arquivo))
pygame.mixer.music.play()

# Espera o áudio terminar. Sem isso, o programa fecharia na hora, sem tocar nada.
while pygame.mixer.music.get_busy():
    pygame.time.wait(100)
