# Make a program that converts meters to centimeters.
# Faça um Programa que converta metros para centímetros

var = input("Digite 1 para converter m ->cm \nDigite 2 para converter cm -> m\n")
valor = float(input("Digite o valor a ser convertido: "))

if var == "1":
    resultado = valor*100
else:
    resultado = valor/100

print(resultado)
