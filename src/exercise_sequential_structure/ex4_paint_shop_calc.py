# https: // wiki.python.org.br / EstruturaSequencial

# 17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
# ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida
# em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o preço seja o menor. Sempre arredonde
# os valores para cima, isto é, considere latas cheias

import math

# variaveis
preco_galao = 25.00
tamanho_galao = 3.6
preco_lata = 80.00
tamanho_lata = 18
rendimento_tinta = 6

metros_quadrados = float(input('Digite a area em metros quadrados da parede a ser pintada: '))
print('\n- A tinta utilizada rende 1 litro a cada 6 metros quadrados\nPossui duas opções de compra:\n'
      'Lata de 18 litros, que custam R$ 80,00 \nGalão de 3,6 litros, que custam R$ 25,00\n\n')

litros_necessarios = metros_quadrados / rendimento_tinta

if litros_necessarios <= tamanho_galao:
    print('Foram neecessários {} litros de tinta'.format(litros_necessarios))
    print('Um galão de {} L é suficiente - Preço R$ {}'.format(tamanho_galao, preco_galao))
elif litros_necessarios == tamanho_lata:
    print('Foram neecessários {} litros de tinta'.format(litros_necessarios))
    print('Uma lata de {} L é suficiente - Preço R$ {}'.format(tamanho_lata, preco_lata))
elif tamanho_lata > litros_necessarios > tamanho_galao:
    quantidade_galao = math.ceil(litros_necessarios / tamanho_galao)
    preco_total_galao = quantidade_galao * preco_galao
    print('Foram neecessários {} litros de tinta'.format(litros_necessarios))
    print('São necessário {} galões de {} L - Preço R$ {}'.format(quantidade_galao, tamanho_galao, preco_total_galao))
elif litros_necessarios > tamanho_lata:

    print('Foram neecessários {} litros de tinta\n'.format(litros_necessarios))

    # Cálculo mistura
    resto = litros_necessarios - tamanho_lata
    while resto >= tamanho_lata:
        resto = resto - tamanho_lata
    quantidade_lata = (litros_necessarios / tamanho_lata)
    quantidade_lata = int(quantidade_lata)
    quantidade_galao = math.ceil(resto / tamanho_galao)
    preco_total_misturado = (quantidade_lata * preco_lata) + quantidade_galao * preco_galao

    print("--------------Misturado--------------")
    print('São necessário {} latas de {} L e {} galões de {} L - Preço R$ {}'.format(quantidade_lata, tamanho_lata,
                                                                                     quantidade_galao,
                                                                                     tamanho_galao,
                                                                                     preco_total_misturado))

    # Cálculo Galões
    quantidade_galao = math.ceil(litros_necessarios / tamanho_galao)
    preco_total_galao = quantidade_galao * preco_galao

    print("--------------Galões--------------")
    print('São necessário {} galões de {} L - Preço R$ {}'.format(quantidade_galao, tamanho_galao,
                                                                  preco_total_galao))

    # Cálculo Latas
    quantidade_lata = math.ceil(litros_necessarios / tamanho_lata)
    preco_total_lata = quantidade_lata * preco_lata

    print("--------------Latas--------------")
    print('São necessário {} latas de {} L - Preço R$ {}'.format(quantidade_lata, tamanho_lata,
                                                                 preco_total_lata))

    print("Preços:\nMisturado: R$ {}\nGalões:  R$ {}\nLatas: R$ {}\n".format(preco_total_misturado,
                                                                             preco_total_galao, preco_total_lata))