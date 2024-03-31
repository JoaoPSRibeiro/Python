"""
Faça um programa em Pythin que abra e reproduza o ãudio de um arquivo em MP3
"""

import pygame

pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
print('Pressione Enter para encerrar a música')
input()
pygame.event.wait()

