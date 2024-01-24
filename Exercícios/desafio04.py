# Crie um script que leia dois numeros e tente mostrar a soma entre eles.

# Int
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
print('A soma de {0} + {1} é {2}'.format(n1, n2, s))  # ordenando

# Float
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
s = n1 + n2
print('A soma de {0} + {1} é {2}'.format(n1, n2, s))  # ordenando

# Bool
n1 = input('Digite um valor (True/False): ').lower() == 'true'
print(n1)

# Str
# Concatenando ´Str´
n1 = str(input('Digite algo: '))
n2 = str(input('Digite algo mais: '))
s = n1 + n2
print('A soma de {0} + {1} é {2}'.format(n1, n2, s))  # ordenando
