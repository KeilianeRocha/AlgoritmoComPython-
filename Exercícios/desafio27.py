"""
Faça um programa que leia uma frase pelo teclado e mostre:
a) Quantas vezes aparece a letra "A"
b) Em que posição ela aparece a primeira vez.
c) Em que posição ela aparece a última vez.
"""
phase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(phase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(phase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(phase.rfind('A')+1))
