# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

slrio = float(input('Qual é o salário do Funcionário? R$ '))
aumento = slrio + (slrio * 15 / 100)
print('Um funcionário que ganhava R${}, com 15% de aumento, vai passar a receber R${:.2f}'.format(slrio, aumento))
