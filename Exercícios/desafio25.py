"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".
"""
town = str(input('Em que cidade você nasceu? ')).upper().strip()
print(town[:5] == 'SANTO')
