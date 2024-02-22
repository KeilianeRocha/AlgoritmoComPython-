"""Faça um programa em Pythom que abra e reproduza um áudio em MP3."""

import pygame
pygame.init()
pygame.mixer.music.load('reproduzirMp3.mp3')
pygame.mixer.music.play()
pygame.event.wait()
"""
O programa não tocou o mp3
"""


