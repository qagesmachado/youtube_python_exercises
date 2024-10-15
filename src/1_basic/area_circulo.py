# Make a program that asks for the radius of a circle, calculates and shows its area.
# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math

raio = 3
valor_pi = 3.141592653589793

#forma 1
area = valor_pi*raio*raio
print(area)

#forma 2
area = math.pi * math.pow(3,2)
print(area)