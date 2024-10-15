# Make a Program that asks for the temperature in degrees Fahrenheit or degrees Celsius, 
# transforms and displays the temperature in degrees Celsius or degrees Fahrenheit

# Faça um Programa que peça a temperatura em graus Fahrenheit ou graus Celsius, 
# transforme e mostre a temperatura em graus Celsius ou graus Fahrenheit

escolha = input("Qual tipo  de conversão você deseja fazer? \n1- Celsius para Fahrenheit\n2- Fahrenheit para Celsius\n")
temp = float(input("Digite a temperatura a ser convertida: "))

if escolha == "1":
    C = temp
    F = (C * 1.8) + 32
    print(f'A temperatura {C} em Celsius equivale a {F} em Fahrenheit')
else:
    F = temp
    C = 5 * ((F-32) / 9)
    print(f'A temperatura {F} em Fahrenheit equivale a {C} em Celsius')