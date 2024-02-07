"""
Crie um programa que leia o nome de uma pessoa e diga se ele tem "Silva" no nome.
"""
name = str(input('Qual é o seu nome? ')).title().strip()
print('Seu nome tem Silva? {}'.format('Silva' in name))




