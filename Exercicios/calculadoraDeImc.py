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