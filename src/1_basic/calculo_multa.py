# The weight limit that can be carried without a fine is 50 kilos, if you exceed it you must pay a fine 
# of R$ 4.00 per kilo in excess. Write a program that reads the weight variable (weight of fish) 
# and calculates the excess.

# O limite de peso que pode ser carregado ser multa é de 50 quilos, caso ultrapasse deve pagar 
# uma multa de R$ 4,00 por quilo excedente. Faça um programa que leia a variável peso (peso de peixes) 
# e calcule o excesso.

peso = 51

if peso > 50:
    excesso = peso - 50
    multa = excesso *4
    print(f"Valor da multa é de {multa} reais")