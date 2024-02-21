"""-----------------------------------------------------------------------------------------------------
# Crie um programa que calcule a média aritmética de 4 notas, sabendo que as notas são as seguintes:
#Nota1 => 5
#Nota2 => 7
#Nota3 => 10
#Nota4 => 3
n1 = 5
n2 = 7
n3 = 10
n4 = 3
soma = (n1 + n2 + n3 + n4)/4
print("A média das 4 notas é: {}".format(soma))
-----------------------------------------------------------------------------------------------------"""
"""-----------------------------------------------------------------------------------------------------
nota1 = int(input("Digite sua nota1: "))
nota2 = int(input("Digite sua nota2: "))
nota3 = int(input("Digite sua nota3: "))
nota4 = int(input("Digite sua nota14: "))
soma = (nota1 + nota2 + nota3 + nota4)
media = soma/4

print("A soma das sua 4 notas foi {}".format(soma))
print(" A media das sua 4 notas foi: {}".format(media))

if media >= 7:
    print("Voce passou!")
elif media < 7:
    print("Infelizmente vc reprovou.")
-----------------------------------------------------------------------------------------------------"""
"""-----------------------------------------------------------------------------------------------------
firstName = str(input("Digite seu primeiro nome: "))
lastName = str(input("Digite o seu Sobrenome: "))
fullName = firstName + " " + lastName
print("Seu nome completo é: {}".format(fullName))
-----------------------------------------------------------------------------------------------------"""
"""-----------------------------------------------------------------------------------------------------
# Laço de repetição
print("=" * 30)
n = 1 => 9*1 ...9*10
while n < 11:
    soma = 9 * n
    print("9 * {} = {}".format(n, soma))
    n += 1
print("=" * 30)
-----------------------------------------------------------------------------------------------------"""
"""-----------------------------------------------------------------------------------------------------
# If
nome = str(input("Escreva seu nome "))
nota1 = int(input("Digite sua nota1: "))
nota2 = int(input("Digite sua nota2: "))
nota3 = int(input("Digite sua nota3: "))
nota4 = int(input("Digite sua nota14: "))
soma = (nota1 + nota2 + nota3 + nota4)
media = soma/4

print("Seu nome é: {}\nA soma das suas 4 notas foi: {}".format(nome, soma))
print("A media das suas 4 notas foi: {}".format(media))

if media >= 7:
    print("Voce passou!")
else:
    print("Infelizmente vc reprovou.")
-----------------------------------------------------------------------------------------------------"""
"""-----------------------------------------------------------------------------------------------------
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso/(altura**2)

if imc < 18.5:
    print("Seu IMC:{:.1f} => ABAIXO do PESO".format(imc))
elif 18.5 <= imc <= 24.9:
    print("Seu IMC:{:.1f} => PESO ADEQUADO".format(imc))
elif 25 <= imc <= 29.9:
    print("Seu IMC:{:.1f} => EXCESSO de PESO".format(imc))
elif 30 <= imc <= 34.9:
    print("Seu IMC:{:.1f} => OBESIDADE CLASSE I".format(imc))
elif 35 <= imc <= 39.9:
    print("Seu IMC:{:.1f} => OBESIDADE CLASSE II".format(imc))
else:
    print("Seu IMC:{:.1f} => OBESIDADE CLASSE III".format(imc))
print("Classificação segundo a OMS a partir do IMC.")
-----------------------------------------------------------------------------------------------------"""
"""-----------------------------------------------------------------------------------------------------
print("=" * 30)
tabuada = int(input("Qual a tabuada que vc quer que eu resolva? "))
contador = 1
limite = 10

while contador <= limite:
    resultado = tabuada * contador
    print("{} x {} = {}".format(tabuada,contador, resultado))
    contador += 1
print("=" * 30)
-----------------------------------------------------------------------------------------------------"""
"""-----------------------------------------------------------------------------------------------------
# Tabuada
print('-' * 21 + '\n   Tabuada\n' + '-' * 21)
print("[1]=> ADIÇÃO\n[2]=> SUBTRAÇÃO\n[3]=> MULTIPLICAÇÃO\n[4]=> DIVISÃO")
escolha = int(input("Qual a tabuada que vc quer que eu resolva? "))
tabuada = int(input("Digite um número: "))
print("-" * 30)
if escolha == 1:
    n = 1
    while n < 11:
        soma = tabuada + n
        print("{} + {} = {}".format(tabuada, n,soma))
        n += 1
elif escolha == 2:
    n = 1
    while n < 11:
        subtracao = tabuada - n
        print("{} - {} = {}".format(tabuada, n, subtracao))
        n += 1
elif escolha == 3:
    n = 1
    while n < 11:
        multiplicacao = tabuada * n
        print("{} x {} = {}".format(tabuada, n, multiplicacao))
        n += 1
elif escolha == 4:
    n = 1
    while n < 11:
        divisao = tabuada / n
        print("{} / {} = {:.1f}".format(tabuada, n, divisao))
        n += 1
else:
    print("Opção INVÁLIDA, tente novamente.")
-----------------------------------------------------------------------------------------------------"""


