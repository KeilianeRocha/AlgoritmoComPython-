"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro nome e o último nome
 separadamente.
 ex.
 Ana Maria de Souza
 primeiro = Ana
 último = Souza

"""
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]).title())
print('O seu último nome é {}'.format(nome[len(nome)-1]).title())

